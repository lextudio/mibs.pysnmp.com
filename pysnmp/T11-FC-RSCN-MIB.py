# SNMP MIB module (T11-FC-RSCN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/T11-FC-RSCN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:00:33 2024
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

(FcAddressIdOrZero,
 FcNameIdOrZero,
 fcmInstanceIndex,
 fcmSwitchIndex) = mibBuilder.importSymbols(
    "FC-MGMT-MIB",
    "FcAddressIdOrZero",
    "FcNameIdOrZero",
    "fcmInstanceIndex",
    "fcmSwitchIndex")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")

(T11NsGs4RejectReasonCode,) = mibBuilder.importSymbols(
    "T11-FC-NAME-SERVER-MIB",
    "T11NsGs4RejectReasonCode")

(T11FabricIndex,) = mibBuilder.importSymbols(
    "T11-TC-MIB",
    "T11FabricIndex")


# MODULE-IDENTITY

t11FcRscnMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 161)
)
t11FcRscnMIB.setRevisions(
        ("2007-01-08 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_T11FcRscnNotifications_ObjectIdentity = ObjectIdentity
t11FcRscnNotifications = _T11FcRscnNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 161, 0)
)
_T11FcRscnObjects_ObjectIdentity = ObjectIdentity
t11FcRscnObjects = _T11FcRscnObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 161, 1)
)
_T11FcRscnRegistrations_ObjectIdentity = ObjectIdentity
t11FcRscnRegistrations = _T11FcRscnRegistrations_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 161, 1, 1)
)
_T11FcRscnRegTable_Object = MibTable
t11FcRscnRegTable = _T11FcRscnRegTable_Object(
    (1, 3, 6, 1, 2, 1, 161, 1, 1, 1)
)
if mibBuilder.loadTexts:
    t11FcRscnRegTable.setStatus("current")
_T11FcRscnRegEntry_Object = MibTableRow
t11FcRscnRegEntry = _T11FcRscnRegEntry_Object(
    (1, 3, 6, 1, 2, 1, 161, 1, 1, 1, 1)
)
t11FcRscnRegEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "FC-MGMT-MIB", "fcmSwitchIndex"),
    (0, "T11-FC-RSCN-MIB", "t11FcRscnFabricIndex"),
    (0, "T11-FC-RSCN-MIB", "t11FcRscnRegFcId"),
)
if mibBuilder.loadTexts:
    t11FcRscnRegEntry.setStatus("current")
_T11FcRscnFabricIndex_Type = T11FabricIndex
_T11FcRscnFabricIndex_Object = MibTableColumn
t11FcRscnFabricIndex = _T11FcRscnFabricIndex_Object(
    (1, 3, 6, 1, 2, 1, 161, 1, 1, 1, 1, 1),
    _T11FcRscnFabricIndex_Type()
)
t11FcRscnFabricIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcRscnFabricIndex.setStatus("current")


class _T11FcRscnRegFcId_Type(FcAddressIdOrZero):
    """Custom type t11FcRscnRegFcId based on FcAddressIdOrZero"""
    subtypeSpec = FcAddressIdOrZero.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_T11FcRscnRegFcId_Type.__name__ = "FcAddressIdOrZero"
_T11FcRscnRegFcId_Object = MibTableColumn
t11FcRscnRegFcId = _T11FcRscnRegFcId_Object(
    (1, 3, 6, 1, 2, 1, 161, 1, 1, 1, 1, 2),
    _T11FcRscnRegFcId_Type()
)
t11FcRscnRegFcId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcRscnRegFcId.setStatus("current")


class _T11FcRscnRegType_Type(Bits):
    """Custom type t11FcRscnRegType based on Bits"""
    namedValues = NamedValues(
        *(("fromFabricController", 0),
          ("fromNxPort", 1))
    )

_T11FcRscnRegType_Type.__name__ = "Bits"
_T11FcRscnRegType_Object = MibTableColumn
t11FcRscnRegType = _T11FcRscnRegType_Object(
    (1, 3, 6, 1, 2, 1, 161, 1, 1, 1, 1, 3),
    _T11FcRscnRegType_Type()
)
t11FcRscnRegType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcRscnRegType.setStatus("current")
_T11FcRscnStats_ObjectIdentity = ObjectIdentity
t11FcRscnStats = _T11FcRscnStats_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 161, 1, 2)
)
_T11FcRscnStatsTable_Object = MibTable
t11FcRscnStatsTable = _T11FcRscnStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 161, 1, 2, 1)
)
if mibBuilder.loadTexts:
    t11FcRscnStatsTable.setStatus("current")
_T11FcRscnStatsEntry_Object = MibTableRow
t11FcRscnStatsEntry = _T11FcRscnStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 161, 1, 2, 1, 1)
)
t11FcRscnStatsEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "FC-MGMT-MIB", "fcmSwitchIndex"),
    (0, "T11-FC-RSCN-MIB", "t11FcRscnFabricIndex"),
)
if mibBuilder.loadTexts:
    t11FcRscnStatsEntry.setStatus("current")
_T11FcRscnInScrs_Type = Counter32
_T11FcRscnInScrs_Object = MibTableColumn
t11FcRscnInScrs = _T11FcRscnInScrs_Object(
    (1, 3, 6, 1, 2, 1, 161, 1, 2, 1, 1, 1),
    _T11FcRscnInScrs_Type()
)
t11FcRscnInScrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcRscnInScrs.setStatus("current")
_T11FcRscnInRscns_Type = Counter32
_T11FcRscnInRscns_Object = MibTableColumn
t11FcRscnInRscns = _T11FcRscnInRscns_Object(
    (1, 3, 6, 1, 2, 1, 161, 1, 2, 1, 1, 2),
    _T11FcRscnInRscns_Type()
)
t11FcRscnInRscns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcRscnInRscns.setStatus("current")
_T11FcRscnOutRscns_Type = Counter32
_T11FcRscnOutRscns_Object = MibTableColumn
t11FcRscnOutRscns = _T11FcRscnOutRscns_Object(
    (1, 3, 6, 1, 2, 1, 161, 1, 2, 1, 1, 3),
    _T11FcRscnOutRscns_Type()
)
t11FcRscnOutRscns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcRscnOutRscns.setStatus("current")
_T11FcRscnInSwRscns_Type = Counter32
_T11FcRscnInSwRscns_Object = MibTableColumn
t11FcRscnInSwRscns = _T11FcRscnInSwRscns_Object(
    (1, 3, 6, 1, 2, 1, 161, 1, 2, 1, 1, 4),
    _T11FcRscnInSwRscns_Type()
)
t11FcRscnInSwRscns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcRscnInSwRscns.setStatus("current")
_T11FcRscnOutSwRscns_Type = Counter32
_T11FcRscnOutSwRscns_Object = MibTableColumn
t11FcRscnOutSwRscns = _T11FcRscnOutSwRscns_Object(
    (1, 3, 6, 1, 2, 1, 161, 1, 2, 1, 1, 5),
    _T11FcRscnOutSwRscns_Type()
)
t11FcRscnOutSwRscns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcRscnOutSwRscns.setStatus("current")
_T11FcRscnScrRejects_Type = Counter32
_T11FcRscnScrRejects_Object = MibTableColumn
t11FcRscnScrRejects = _T11FcRscnScrRejects_Object(
    (1, 3, 6, 1, 2, 1, 161, 1, 2, 1, 1, 6),
    _T11FcRscnScrRejects_Type()
)
t11FcRscnScrRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcRscnScrRejects.setStatus("current")
_T11FcRscnRscnRejects_Type = Counter32
_T11FcRscnRscnRejects_Object = MibTableColumn
t11FcRscnRscnRejects = _T11FcRscnRscnRejects_Object(
    (1, 3, 6, 1, 2, 1, 161, 1, 2, 1, 1, 7),
    _T11FcRscnRscnRejects_Type()
)
t11FcRscnRscnRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcRscnRscnRejects.setStatus("current")
_T11FcRscnSwRscnRejects_Type = Counter32
_T11FcRscnSwRscnRejects_Object = MibTableColumn
t11FcRscnSwRscnRejects = _T11FcRscnSwRscnRejects_Object(
    (1, 3, 6, 1, 2, 1, 161, 1, 2, 1, 1, 8),
    _T11FcRscnSwRscnRejects_Type()
)
t11FcRscnSwRscnRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcRscnSwRscnRejects.setStatus("current")
_T11FcRscnInUnspecifiedRscns_Type = Counter32
_T11FcRscnInUnspecifiedRscns_Object = MibTableColumn
t11FcRscnInUnspecifiedRscns = _T11FcRscnInUnspecifiedRscns_Object(
    (1, 3, 6, 1, 2, 1, 161, 1, 2, 1, 1, 9),
    _T11FcRscnInUnspecifiedRscns_Type()
)
t11FcRscnInUnspecifiedRscns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcRscnInUnspecifiedRscns.setStatus("current")
_T11FcRscnOutUnspecifiedRscns_Type = Counter32
_T11FcRscnOutUnspecifiedRscns_Object = MibTableColumn
t11FcRscnOutUnspecifiedRscns = _T11FcRscnOutUnspecifiedRscns_Object(
    (1, 3, 6, 1, 2, 1, 161, 1, 2, 1, 1, 10),
    _T11FcRscnOutUnspecifiedRscns_Type()
)
t11FcRscnOutUnspecifiedRscns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcRscnOutUnspecifiedRscns.setStatus("current")
_T11FcRscnInChangedAttribRscns_Type = Counter32
_T11FcRscnInChangedAttribRscns_Object = MibTableColumn
t11FcRscnInChangedAttribRscns = _T11FcRscnInChangedAttribRscns_Object(
    (1, 3, 6, 1, 2, 1, 161, 1, 2, 1, 1, 11),
    _T11FcRscnInChangedAttribRscns_Type()
)
t11FcRscnInChangedAttribRscns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcRscnInChangedAttribRscns.setStatus("current")
_T11FcRscnOutChangedAttribRscns_Type = Counter32
_T11FcRscnOutChangedAttribRscns_Object = MibTableColumn
t11FcRscnOutChangedAttribRscns = _T11FcRscnOutChangedAttribRscns_Object(
    (1, 3, 6, 1, 2, 1, 161, 1, 2, 1, 1, 12),
    _T11FcRscnOutChangedAttribRscns_Type()
)
t11FcRscnOutChangedAttribRscns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcRscnOutChangedAttribRscns.setStatus("current")
_T11FcRscnInChangedServiceRscns_Type = Counter32
_T11FcRscnInChangedServiceRscns_Object = MibTableColumn
t11FcRscnInChangedServiceRscns = _T11FcRscnInChangedServiceRscns_Object(
    (1, 3, 6, 1, 2, 1, 161, 1, 2, 1, 1, 13),
    _T11FcRscnInChangedServiceRscns_Type()
)
t11FcRscnInChangedServiceRscns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcRscnInChangedServiceRscns.setStatus("current")
_T11FcRscnOutChangedServiceRscns_Type = Counter32
_T11FcRscnOutChangedServiceRscns_Object = MibTableColumn
t11FcRscnOutChangedServiceRscns = _T11FcRscnOutChangedServiceRscns_Object(
    (1, 3, 6, 1, 2, 1, 161, 1, 2, 1, 1, 14),
    _T11FcRscnOutChangedServiceRscns_Type()
)
t11FcRscnOutChangedServiceRscns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcRscnOutChangedServiceRscns.setStatus("current")
_T11FcRscnInChangedSwitchRscns_Type = Counter32
_T11FcRscnInChangedSwitchRscns_Object = MibTableColumn
t11FcRscnInChangedSwitchRscns = _T11FcRscnInChangedSwitchRscns_Object(
    (1, 3, 6, 1, 2, 1, 161, 1, 2, 1, 1, 15),
    _T11FcRscnInChangedSwitchRscns_Type()
)
t11FcRscnInChangedSwitchRscns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcRscnInChangedSwitchRscns.setStatus("current")
_T11FcRscnOutChangedSwitchRscns_Type = Counter32
_T11FcRscnOutChangedSwitchRscns_Object = MibTableColumn
t11FcRscnOutChangedSwitchRscns = _T11FcRscnOutChangedSwitchRscns_Object(
    (1, 3, 6, 1, 2, 1, 161, 1, 2, 1, 1, 16),
    _T11FcRscnOutChangedSwitchRscns_Type()
)
t11FcRscnOutChangedSwitchRscns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcRscnOutChangedSwitchRscns.setStatus("current")
_T11FcRscnInRemovedRscns_Type = Counter32
_T11FcRscnInRemovedRscns_Object = MibTableColumn
t11FcRscnInRemovedRscns = _T11FcRscnInRemovedRscns_Object(
    (1, 3, 6, 1, 2, 1, 161, 1, 2, 1, 1, 17),
    _T11FcRscnInRemovedRscns_Type()
)
t11FcRscnInRemovedRscns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcRscnInRemovedRscns.setStatus("current")
_T11FcRscnOutRemovedRscns_Type = Counter32
_T11FcRscnOutRemovedRscns_Object = MibTableColumn
t11FcRscnOutRemovedRscns = _T11FcRscnOutRemovedRscns_Object(
    (1, 3, 6, 1, 2, 1, 161, 1, 2, 1, 1, 18),
    _T11FcRscnOutRemovedRscns_Type()
)
t11FcRscnOutRemovedRscns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcRscnOutRemovedRscns.setStatus("current")
_T11FcRscnInformation_ObjectIdentity = ObjectIdentity
t11FcRscnInformation = _T11FcRscnInformation_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 161, 1, 3)
)
_T11FcRscnNotifyControlTable_Object = MibTable
t11FcRscnNotifyControlTable = _T11FcRscnNotifyControlTable_Object(
    (1, 3, 6, 1, 2, 1, 161, 1, 3, 1)
)
if mibBuilder.loadTexts:
    t11FcRscnNotifyControlTable.setStatus("current")
_T11FcRscnNotifyControlEntry_Object = MibTableRow
t11FcRscnNotifyControlEntry = _T11FcRscnNotifyControlEntry_Object(
    (1, 3, 6, 1, 2, 1, 161, 1, 3, 1, 1)
)
t11FcRscnNotifyControlEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "FC-MGMT-MIB", "fcmSwitchIndex"),
    (0, "T11-FC-RSCN-MIB", "t11FcRscnFabricIndex"),
)
if mibBuilder.loadTexts:
    t11FcRscnNotifyControlEntry.setStatus("current")


class _T11FcRscnIlsRejectNotifyEnable_Type(TruthValue):
    """Custom type t11FcRscnIlsRejectNotifyEnable based on TruthValue"""


_T11FcRscnIlsRejectNotifyEnable_Object = MibTableColumn
t11FcRscnIlsRejectNotifyEnable = _T11FcRscnIlsRejectNotifyEnable_Object(
    (1, 3, 6, 1, 2, 1, 161, 1, 3, 1, 1, 1),
    _T11FcRscnIlsRejectNotifyEnable_Type()
)
t11FcRscnIlsRejectNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t11FcRscnIlsRejectNotifyEnable.setStatus("current")


class _T11FcRscnElsRejectNotifyEnable_Type(TruthValue):
    """Custom type t11FcRscnElsRejectNotifyEnable based on TruthValue"""


_T11FcRscnElsRejectNotifyEnable_Object = MibTableColumn
t11FcRscnElsRejectNotifyEnable = _T11FcRscnElsRejectNotifyEnable_Object(
    (1, 3, 6, 1, 2, 1, 161, 1, 3, 1, 1, 2),
    _T11FcRscnElsRejectNotifyEnable_Type()
)
t11FcRscnElsRejectNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t11FcRscnElsRejectNotifyEnable.setStatus("current")


class _T11FcRscnRejectedRequestString_Type(OctetString):
    """Custom type t11FcRscnRejectedRequestString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_T11FcRscnRejectedRequestString_Type.__name__ = "OctetString"
_T11FcRscnRejectedRequestString_Object = MibTableColumn
t11FcRscnRejectedRequestString = _T11FcRscnRejectedRequestString_Object(
    (1, 3, 6, 1, 2, 1, 161, 1, 3, 1, 1, 3),
    _T11FcRscnRejectedRequestString_Type()
)
t11FcRscnRejectedRequestString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcRscnRejectedRequestString.setStatus("current")
_T11FcRscnRejectedRequestSource_Type = FcNameIdOrZero
_T11FcRscnRejectedRequestSource_Object = MibTableColumn
t11FcRscnRejectedRequestSource = _T11FcRscnRejectedRequestSource_Object(
    (1, 3, 6, 1, 2, 1, 161, 1, 3, 1, 1, 4),
    _T11FcRscnRejectedRequestSource_Type()
)
t11FcRscnRejectedRequestSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcRscnRejectedRequestSource.setStatus("current")
_T11FcRscnRejectReasonCode_Type = T11NsGs4RejectReasonCode
_T11FcRscnRejectReasonCode_Object = MibTableColumn
t11FcRscnRejectReasonCode = _T11FcRscnRejectReasonCode_Object(
    (1, 3, 6, 1, 2, 1, 161, 1, 3, 1, 1, 5),
    _T11FcRscnRejectReasonCode_Type()
)
t11FcRscnRejectReasonCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcRscnRejectReasonCode.setStatus("current")


class _T11FcRscnRejectReasonCodeExp_Type(OctetString):
    """Custom type t11FcRscnRejectReasonCodeExp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_T11FcRscnRejectReasonCodeExp_Type.__name__ = "OctetString"
_T11FcRscnRejectReasonCodeExp_Object = MibTableColumn
t11FcRscnRejectReasonCodeExp = _T11FcRscnRejectReasonCodeExp_Object(
    (1, 3, 6, 1, 2, 1, 161, 1, 3, 1, 1, 6),
    _T11FcRscnRejectReasonCodeExp_Type()
)
t11FcRscnRejectReasonCodeExp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcRscnRejectReasonCodeExp.setStatus("current")


class _T11FcRscnRejectReasonVendorCode_Type(OctetString):
    """Custom type t11FcRscnRejectReasonVendorCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_T11FcRscnRejectReasonVendorCode_Type.__name__ = "OctetString"
_T11FcRscnRejectReasonVendorCode_Object = MibTableColumn
t11FcRscnRejectReasonVendorCode = _T11FcRscnRejectReasonVendorCode_Object(
    (1, 3, 6, 1, 2, 1, 161, 1, 3, 1, 1, 7),
    _T11FcRscnRejectReasonVendorCode_Type()
)
t11FcRscnRejectReasonVendorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcRscnRejectReasonVendorCode.setStatus("current")
_T11FcRscnConformance_ObjectIdentity = ObjectIdentity
t11FcRscnConformance = _T11FcRscnConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 161, 2)
)
_T11FcRscnCompliances_ObjectIdentity = ObjectIdentity
t11FcRscnCompliances = _T11FcRscnCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 161, 2, 1)
)
_T11FcRscnGroups_ObjectIdentity = ObjectIdentity
t11FcRscnGroups = _T11FcRscnGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 161, 2, 2)
)

# Managed Objects groups

t11FcRscnRegistrationGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 161, 2, 2, 1)
)
t11FcRscnRegistrationGroup.setObjects(
    ("T11-FC-RSCN-MIB", "t11FcRscnRegType")
)
if mibBuilder.loadTexts:
    t11FcRscnRegistrationGroup.setStatus("current")

t11FcRscnStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 161, 2, 2, 2)
)
t11FcRscnStatsGroup.setObjects(
      *(("T11-FC-RSCN-MIB", "t11FcRscnInScrs"),
        ("T11-FC-RSCN-MIB", "t11FcRscnInRscns"),
        ("T11-FC-RSCN-MIB", "t11FcRscnOutRscns"),
        ("T11-FC-RSCN-MIB", "t11FcRscnInSwRscns"),
        ("T11-FC-RSCN-MIB", "t11FcRscnOutSwRscns"),
        ("T11-FC-RSCN-MIB", "t11FcRscnScrRejects"),
        ("T11-FC-RSCN-MIB", "t11FcRscnRscnRejects"),
        ("T11-FC-RSCN-MIB", "t11FcRscnSwRscnRejects"),
        ("T11-FC-RSCN-MIB", "t11FcRscnInUnspecifiedRscns"),
        ("T11-FC-RSCN-MIB", "t11FcRscnOutUnspecifiedRscns"),
        ("T11-FC-RSCN-MIB", "t11FcRscnInChangedAttribRscns"),
        ("T11-FC-RSCN-MIB", "t11FcRscnOutChangedAttribRscns"),
        ("T11-FC-RSCN-MIB", "t11FcRscnInChangedServiceRscns"),
        ("T11-FC-RSCN-MIB", "t11FcRscnOutChangedServiceRscns"),
        ("T11-FC-RSCN-MIB", "t11FcRscnInChangedSwitchRscns"),
        ("T11-FC-RSCN-MIB", "t11FcRscnOutChangedSwitchRscns"),
        ("T11-FC-RSCN-MIB", "t11FcRscnInRemovedRscns"),
        ("T11-FC-RSCN-MIB", "t11FcRscnOutRemovedRscns"))
)
if mibBuilder.loadTexts:
    t11FcRscnStatsGroup.setStatus("current")

t11FcRscnNotifyControlGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 161, 2, 2, 3)
)
t11FcRscnNotifyControlGroup.setObjects(
      *(("T11-FC-RSCN-MIB", "t11FcRscnIlsRejectNotifyEnable"),
        ("T11-FC-RSCN-MIB", "t11FcRscnElsRejectNotifyEnable"),
        ("T11-FC-RSCN-MIB", "t11FcRscnRejectedRequestString"),
        ("T11-FC-RSCN-MIB", "t11FcRscnRejectedRequestSource"),
        ("T11-FC-RSCN-MIB", "t11FcRscnRejectReasonCode"),
        ("T11-FC-RSCN-MIB", "t11FcRscnRejectReasonCodeExp"),
        ("T11-FC-RSCN-MIB", "t11FcRscnRejectReasonVendorCode"))
)
if mibBuilder.loadTexts:
    t11FcRscnNotifyControlGroup.setStatus("current")


# Notification objects

t11FcRscnElsRejectReqNotify = NotificationType(
    (1, 3, 6, 1, 2, 1, 161, 0, 1)
)
t11FcRscnElsRejectReqNotify.setObjects(
      *(("T11-FC-RSCN-MIB", "t11FcRscnRejectedRequestString"),
        ("T11-FC-RSCN-MIB", "t11FcRscnRejectedRequestSource"),
        ("T11-FC-RSCN-MIB", "t11FcRscnRejectReasonCode"),
        ("T11-FC-RSCN-MIB", "t11FcRscnRejectReasonCodeExp"),
        ("T11-FC-RSCN-MIB", "t11FcRscnRejectReasonVendorCode"))
)
if mibBuilder.loadTexts:
    t11FcRscnElsRejectReqNotify.setStatus(
        "current"
    )

t11FcRscnIlsRejectReqNotify = NotificationType(
    (1, 3, 6, 1, 2, 1, 161, 0, 2)
)
t11FcRscnIlsRejectReqNotify.setObjects(
      *(("T11-FC-RSCN-MIB", "t11FcRscnRejectedRequestString"),
        ("T11-FC-RSCN-MIB", "t11FcRscnRejectedRequestSource"),
        ("T11-FC-RSCN-MIB", "t11FcRscnRejectReasonCode"),
        ("T11-FC-RSCN-MIB", "t11FcRscnRejectReasonCodeExp"),
        ("T11-FC-RSCN-MIB", "t11FcRscnRejectReasonVendorCode"))
)
if mibBuilder.loadTexts:
    t11FcRscnIlsRejectReqNotify.setStatus(
        "current"
    )


# Notifications groups

t11FcRscnNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 161, 2, 2, 4)
)
t11FcRscnNotifyGroup.setObjects(
      *(("T11-FC-RSCN-MIB", "t11FcRscnIlsRejectReqNotify"),
        ("T11-FC-RSCN-MIB", "t11FcRscnElsRejectReqNotify"))
)
if mibBuilder.loadTexts:
    t11FcRscnNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

t11FcRscnCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 161, 2, 1, 1)
)
if mibBuilder.loadTexts:
    t11FcRscnCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "T11-FC-RSCN-MIB",
    **{"t11FcRscnMIB": t11FcRscnMIB,
       "t11FcRscnNotifications": t11FcRscnNotifications,
       "t11FcRscnElsRejectReqNotify": t11FcRscnElsRejectReqNotify,
       "t11FcRscnIlsRejectReqNotify": t11FcRscnIlsRejectReqNotify,
       "t11FcRscnObjects": t11FcRscnObjects,
       "t11FcRscnRegistrations": t11FcRscnRegistrations,
       "t11FcRscnRegTable": t11FcRscnRegTable,
       "t11FcRscnRegEntry": t11FcRscnRegEntry,
       "t11FcRscnFabricIndex": t11FcRscnFabricIndex,
       "t11FcRscnRegFcId": t11FcRscnRegFcId,
       "t11FcRscnRegType": t11FcRscnRegType,
       "t11FcRscnStats": t11FcRscnStats,
       "t11FcRscnStatsTable": t11FcRscnStatsTable,
       "t11FcRscnStatsEntry": t11FcRscnStatsEntry,
       "t11FcRscnInScrs": t11FcRscnInScrs,
       "t11FcRscnInRscns": t11FcRscnInRscns,
       "t11FcRscnOutRscns": t11FcRscnOutRscns,
       "t11FcRscnInSwRscns": t11FcRscnInSwRscns,
       "t11FcRscnOutSwRscns": t11FcRscnOutSwRscns,
       "t11FcRscnScrRejects": t11FcRscnScrRejects,
       "t11FcRscnRscnRejects": t11FcRscnRscnRejects,
       "t11FcRscnSwRscnRejects": t11FcRscnSwRscnRejects,
       "t11FcRscnInUnspecifiedRscns": t11FcRscnInUnspecifiedRscns,
       "t11FcRscnOutUnspecifiedRscns": t11FcRscnOutUnspecifiedRscns,
       "t11FcRscnInChangedAttribRscns": t11FcRscnInChangedAttribRscns,
       "t11FcRscnOutChangedAttribRscns": t11FcRscnOutChangedAttribRscns,
       "t11FcRscnInChangedServiceRscns": t11FcRscnInChangedServiceRscns,
       "t11FcRscnOutChangedServiceRscns": t11FcRscnOutChangedServiceRscns,
       "t11FcRscnInChangedSwitchRscns": t11FcRscnInChangedSwitchRscns,
       "t11FcRscnOutChangedSwitchRscns": t11FcRscnOutChangedSwitchRscns,
       "t11FcRscnInRemovedRscns": t11FcRscnInRemovedRscns,
       "t11FcRscnOutRemovedRscns": t11FcRscnOutRemovedRscns,
       "t11FcRscnInformation": t11FcRscnInformation,
       "t11FcRscnNotifyControlTable": t11FcRscnNotifyControlTable,
       "t11FcRscnNotifyControlEntry": t11FcRscnNotifyControlEntry,
       "t11FcRscnIlsRejectNotifyEnable": t11FcRscnIlsRejectNotifyEnable,
       "t11FcRscnElsRejectNotifyEnable": t11FcRscnElsRejectNotifyEnable,
       "t11FcRscnRejectedRequestString": t11FcRscnRejectedRequestString,
       "t11FcRscnRejectedRequestSource": t11FcRscnRejectedRequestSource,
       "t11FcRscnRejectReasonCode": t11FcRscnRejectReasonCode,
       "t11FcRscnRejectReasonCodeExp": t11FcRscnRejectReasonCodeExp,
       "t11FcRscnRejectReasonVendorCode": t11FcRscnRejectReasonVendorCode,
       "t11FcRscnConformance": t11FcRscnConformance,
       "t11FcRscnCompliances": t11FcRscnCompliances,
       "t11FcRscnCompliance": t11FcRscnCompliance,
       "t11FcRscnGroups": t11FcRscnGroups,
       "t11FcRscnRegistrationGroup": t11FcRscnRegistrationGroup,
       "t11FcRscnStatsGroup": t11FcRscnStatsGroup,
       "t11FcRscnNotifyControlGroup": t11FcRscnNotifyControlGroup,
       "t11FcRscnNotifyGroup": t11FcRscnNotifyGroup}
)
