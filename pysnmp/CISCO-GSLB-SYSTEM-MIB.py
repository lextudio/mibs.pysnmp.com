# SNMP MIB module (CISCO-GSLB-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-GSLB-SYSTEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:01:03 2024
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

(CiscoGslbNodeServices,
 CiscoGslbPeerStatus) = mibBuilder.importSymbols(
    "CISCO-GSLB-TC-MIB",
    "CiscoGslbNodeServices",
    "CiscoGslbPeerStatus")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressDNS,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressDNS",
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

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoGslbSystemMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 589)
)
ciscoGslbSystemMIB.setRevisions(
        ("2011-06-06 00:00",
         "2006-12-04 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoGslbSystemMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoGslbSystemMIBNotifs = _CiscoGslbSystemMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 0)
)
_CiscoGslbSystemMIBObjects_ObjectIdentity = ObjectIdentity
ciscoGslbSystemMIBObjects = _CiscoGslbSystemMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1)
)
_CgsNotifControl_ObjectIdentity = ObjectIdentity
cgsNotifControl = _CgsNotifControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 1)
)


class _CgsPeerEventNotifEnable_Type(TruthValue):
    """Custom type cgsPeerEventNotifEnable based on TruthValue"""


_CgsPeerEventNotifEnable_Object = MibScalar
cgsPeerEventNotifEnable = _CgsPeerEventNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 1, 1),
    _CgsPeerEventNotifEnable_Type()
)
cgsPeerEventNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgsPeerEventNotifEnable.setStatus("current")
_CgsNotifObjects_ObjectIdentity = ObjectIdentity
cgsNotifObjects = _CgsNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 2)
)
_CgsPeerPrevStatus_Type = CiscoGslbPeerStatus
_CgsPeerPrevStatus_Object = MibScalar
cgsPeerPrevStatus = _CgsPeerPrevStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 2, 1),
    _CgsPeerPrevStatus_Type()
)
cgsPeerPrevStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgsPeerPrevStatus.setStatus("current")
_CgsGeneral_ObjectIdentity = ObjectIdentity
cgsGeneral = _CgsGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 3)
)
_CgsNodeService_Type = CiscoGslbNodeServices
_CgsNodeService_Object = MibScalar
cgsNodeService = _CgsNodeService_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 3, 1),
    _CgsNodeService_Type()
)
cgsNodeService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgsNodeService.setStatus("current")
_CgsNodeCommIfName_Type = SnmpAdminString
_CgsNodeCommIfName_Object = MibScalar
cgsNodeCommIfName = _CgsNodeCommIfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 3, 2),
    _CgsNodeCommIfName_Type()
)
cgsNodeCommIfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgsNodeCommIfName.setStatus("current")
_CgsNodeCommIfIndex_Type = InterfaceIndexOrZero
_CgsNodeCommIfIndex_Object = MibScalar
cgsNodeCommIfIndex = _CgsNodeCommIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 3, 3),
    _CgsNodeCommIfIndex_Type()
)
cgsNodeCommIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsNodeCommIfIndex.setStatus("current")
_CgsNodeStatus_Type = CiscoGslbPeerStatus
_CgsNodeStatus_Object = MibScalar
cgsNodeStatus = _CgsNodeStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 3, 4),
    _CgsNodeStatus_Type()
)
cgsNodeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsNodeStatus.setStatus("current")


class _CgsNodeLocation_Type(SnmpAdminString):
    """Custom type cgsNodeLocation based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_CgsNodeLocation_Type.__name__ = "SnmpAdminString"
_CgsNodeLocation_Object = MibScalar
cgsNodeLocation = _CgsNodeLocation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 3, 5),
    _CgsNodeLocation_Type()
)
cgsNodeLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgsNodeLocation.setStatus("current")


class _CgsNodeRegion_Type(SnmpAdminString):
    """Custom type cgsNodeRegion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_CgsNodeRegion_Type.__name__ = "SnmpAdminString"
_CgsNodeRegion_Object = MibScalar
cgsNodeRegion = _CgsNodeRegion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 3, 6),
    _CgsNodeRegion_Type()
)
cgsNodeRegion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsNodeRegion.setStatus("current")
_CgsPeer_ObjectIdentity = ObjectIdentity
cgsPeer = _CgsPeer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 4)
)
_CgsPeerTable_Object = MibTable
cgsPeerTable = _CgsPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cgsPeerTable.setStatus("current")
_CgsPeerEntry_Object = MibTableRow
cgsPeerEntry = _CgsPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 4, 1, 1)
)
cgsPeerEntry.setIndexNames(
    (0, "CISCO-GSLB-SYSTEM-MIB", "cgsPeerAddressType"),
    (0, "CISCO-GSLB-SYSTEM-MIB", "cgsPeerAddress"),
)
if mibBuilder.loadTexts:
    cgsPeerEntry.setStatus("current")
_CgsPeerAddressType_Type = InetAddressType
_CgsPeerAddressType_Object = MibTableColumn
cgsPeerAddressType = _CgsPeerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 4, 1, 1, 1),
    _CgsPeerAddressType_Type()
)
cgsPeerAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgsPeerAddressType.setStatus("current")


class _CgsPeerAddress_Type(InetAddress):
    """Custom type cgsPeerAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CgsPeerAddress_Type.__name__ = "InetAddress"
_CgsPeerAddress_Object = MibTableColumn
cgsPeerAddress = _CgsPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 4, 1, 1, 2),
    _CgsPeerAddress_Type()
)
cgsPeerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgsPeerAddress.setStatus("current")


class _CgsPeerLocation_Type(SnmpAdminString):
    """Custom type cgsPeerLocation based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_CgsPeerLocation_Type.__name__ = "SnmpAdminString"
_CgsPeerLocation_Object = MibTableColumn
cgsPeerLocation = _CgsPeerLocation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 4, 1, 1, 3),
    _CgsPeerLocation_Type()
)
cgsPeerLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgsPeerLocation.setStatus("current")
_CgsPeerDnsName_Type = InetAddressDNS
_CgsPeerDnsName_Object = MibTableColumn
cgsPeerDnsName = _CgsPeerDnsName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 4, 1, 1, 4),
    _CgsPeerDnsName_Type()
)
cgsPeerDnsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsPeerDnsName.setStatus("current")
_CgsPeerService_Type = CiscoGslbNodeServices
_CgsPeerService_Object = MibTableColumn
cgsPeerService = _CgsPeerService_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 4, 1, 1, 5),
    _CgsPeerService_Type()
)
cgsPeerService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsPeerService.setStatus("current")
_CgsPeerStatus_Type = CiscoGslbPeerStatus
_CgsPeerStatus_Object = MibTableColumn
cgsPeerStatus = _CgsPeerStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 4, 1, 1, 6),
    _CgsPeerStatus_Type()
)
cgsPeerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsPeerStatus.setStatus("current")
_CgsPeerVersion_Type = SnmpAdminString
_CgsPeerVersion_Object = MibTableColumn
cgsPeerVersion = _CgsPeerVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 4, 1, 1, 7),
    _CgsPeerVersion_Type()
)
cgsPeerVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsPeerVersion.setStatus("current")
_CgsProxZoneStats_ObjectIdentity = ObjectIdentity
cgsProxZoneStats = _CgsProxZoneStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 5)
)
_CgsProxZoneTable_Object = MibTable
cgsProxZoneTable = _CgsProxZoneTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cgsProxZoneTable.setStatus("current")
_CgsProxZoneEntry_Object = MibTableRow
cgsProxZoneEntry = _CgsProxZoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 5, 1, 1)
)
cgsProxZoneEntry.setIndexNames(
    (0, "CISCO-GSLB-SYSTEM-MIB", "cgsProxZoneName"),
)
if mibBuilder.loadTexts:
    cgsProxZoneEntry.setStatus("current")


class _CgsProxZoneName_Type(SnmpAdminString):
    """Custom type cgsProxZoneName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_CgsProxZoneName_Type.__name__ = "SnmpAdminString"
_CgsProxZoneName_Object = MibTableColumn
cgsProxZoneName = _CgsProxZoneName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 5, 1, 1, 1),
    _CgsProxZoneName_Type()
)
cgsProxZoneName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgsProxZoneName.setStatus("current")


class _CgsProxPrimaryAddressType_Type(InetAddressType):
    """Custom type cgsProxPrimaryAddressType based on InetAddressType"""


_CgsProxPrimaryAddressType_Object = MibTableColumn
cgsProxPrimaryAddressType = _CgsProxPrimaryAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 5, 1, 1, 2),
    _CgsProxPrimaryAddressType_Type()
)
cgsProxPrimaryAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsProxPrimaryAddressType.setStatus("current")
_CgsProxPrimaryAddress_Type = InetAddress
_CgsProxPrimaryAddress_Object = MibTableColumn
cgsProxPrimaryAddress = _CgsProxPrimaryAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 5, 1, 1, 3),
    _CgsProxPrimaryAddress_Type()
)
cgsProxPrimaryAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsProxPrimaryAddress.setStatus("current")


class _CgsProxSecondaryAddressType_Type(InetAddressType):
    """Custom type cgsProxSecondaryAddressType based on InetAddressType"""


_CgsProxSecondaryAddressType_Object = MibTableColumn
cgsProxSecondaryAddressType = _CgsProxSecondaryAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 5, 1, 1, 4),
    _CgsProxSecondaryAddressType_Type()
)
cgsProxSecondaryAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsProxSecondaryAddressType.setStatus("current")
_CgsProxSecondaryAddress_Type = InetAddress
_CgsProxSecondaryAddress_Object = MibTableColumn
cgsProxSecondaryAddress = _CgsProxSecondaryAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 5, 1, 1, 5),
    _CgsProxSecondaryAddress_Type()
)
cgsProxSecondaryAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsProxSecondaryAddress.setStatus("current")
_CgsProxEchoSentReqs_Type = Counter32
_CgsProxEchoSentReqs_Object = MibTableColumn
cgsProxEchoSentReqs = _CgsProxEchoSentReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 5, 1, 1, 6),
    _CgsProxEchoSentReqs_Type()
)
cgsProxEchoSentReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsProxEchoSentReqs.setStatus("current")
if mibBuilder.loadTexts:
    cgsProxEchoSentReqs.setUnits("requests")
_CgsProxEchoRcvdResps_Type = Counter32
_CgsProxEchoRcvdResps_Object = MibTableColumn
cgsProxEchoRcvdResps = _CgsProxEchoRcvdResps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 5, 1, 1, 7),
    _CgsProxEchoRcvdResps_Type()
)
cgsProxEchoRcvdResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsProxEchoRcvdResps.setStatus("current")
if mibBuilder.loadTexts:
    cgsProxEchoRcvdResps.setUnits("responses")
_CgsProxSentMeasureReqs_Type = Counter32
_CgsProxSentMeasureReqs_Object = MibTableColumn
cgsProxSentMeasureReqs = _CgsProxSentMeasureReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 5, 1, 1, 8),
    _CgsProxSentMeasureReqs_Type()
)
cgsProxSentMeasureReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsProxSentMeasureReqs.setStatus("current")
if mibBuilder.loadTexts:
    cgsProxSentMeasureReqs.setUnits("requests")
_CgsProxRcvdMeasureResps_Type = Counter32
_CgsProxRcvdMeasureResps_Object = MibTableColumn
cgsProxRcvdMeasureResps = _CgsProxRcvdMeasureResps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 5, 1, 1, 9),
    _CgsProxRcvdMeasureResps_Type()
)
cgsProxRcvdMeasureResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsProxRcvdMeasureResps.setStatus("current")
if mibBuilder.loadTexts:
    cgsProxRcvdMeasureResps.setUnits("responses")
_CgsProxTotalSentReqs_Type = Counter32
_CgsProxTotalSentReqs_Object = MibTableColumn
cgsProxTotalSentReqs = _CgsProxTotalSentReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 5, 1, 1, 10),
    _CgsProxTotalSentReqs_Type()
)
cgsProxTotalSentReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsProxTotalSentReqs.setStatus("current")
if mibBuilder.loadTexts:
    cgsProxTotalSentReqs.setUnits("requests")
_CgsProxTotalRcvdResps_Type = Counter32
_CgsProxTotalRcvdResps_Object = MibTableColumn
cgsProxTotalRcvdResps = _CgsProxTotalRcvdResps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 5, 1, 1, 11),
    _CgsProxTotalRcvdResps_Type()
)
cgsProxTotalRcvdResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsProxTotalRcvdResps.setStatus("current")
if mibBuilder.loadTexts:
    cgsProxTotalRcvdResps.setUnits("responses")
_CgsProxSendRate_Type = Unsigned32
_CgsProxSendRate_Object = MibTableColumn
cgsProxSendRate = _CgsProxSendRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 5, 1, 1, 12),
    _CgsProxSendRate_Type()
)
cgsProxSendRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsProxSendRate.setStatus("current")
if mibBuilder.loadTexts:
    cgsProxSendRate.setUnits("rate per second")
_CgsProxRcvdRate_Type = Unsigned32
_CgsProxRcvdRate_Object = MibTableColumn
cgsProxRcvdRate = _CgsProxRcvdRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 5, 1, 1, 13),
    _CgsProxRcvdRate_Type()
)
cgsProxRcvdRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsProxRcvdRate.setStatus("current")
if mibBuilder.loadTexts:
    cgsProxRcvdRate.setUnits("rate per second")
_CgsProxPeakSendRate_Type = Unsigned32
_CgsProxPeakSendRate_Object = MibTableColumn
cgsProxPeakSendRate = _CgsProxPeakSendRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 5, 1, 1, 14),
    _CgsProxPeakSendRate_Type()
)
cgsProxPeakSendRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsProxPeakSendRate.setStatus("current")
if mibBuilder.loadTexts:
    cgsProxPeakSendRate.setUnits("rate per second")
_CgsProxPeakRcvdRate_Type = Unsigned32
_CgsProxPeakRcvdRate_Object = MibTableColumn
cgsProxPeakRcvdRate = _CgsProxPeakRcvdRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 5, 1, 1, 15),
    _CgsProxPeakRcvdRate_Type()
)
cgsProxPeakRcvdRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsProxPeakRcvdRate.setStatus("current")
if mibBuilder.loadTexts:
    cgsProxPeakRcvdRate.setUnits("rate per second")


class _CgsProxStorageType_Type(StorageType):
    """Custom type cgsProxStorageType based on StorageType"""


_CgsProxStorageType_Object = MibTableColumn
cgsProxStorageType = _CgsProxStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 5, 1, 1, 16),
    _CgsProxStorageType_Type()
)
cgsProxStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsProxStorageType.setStatus("current")
_CgsProxRowStatus_Type = RowStatus
_CgsProxRowStatus_Object = MibTableColumn
cgsProxRowStatus = _CgsProxRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 5, 1, 1, 17),
    _CgsProxRowStatus_Type()
)
cgsProxRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsProxRowStatus.setStatus("current")
_CgsResources_ObjectIdentity = ObjectIdentity
cgsResources = _CgsResources_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 6)
)
_CgsRegionTable_Object = MibTable
cgsRegionTable = _CgsRegionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 6, 1)
)
if mibBuilder.loadTexts:
    cgsRegionTable.setStatus("deprecated")
_CgsRegionEntry_Object = MibTableRow
cgsRegionEntry = _CgsRegionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 6, 1, 1)
)
cgsRegionEntry.setIndexNames(
    (0, "CISCO-GSLB-SYSTEM-MIB", "cgsRegionName"),
)
if mibBuilder.loadTexts:
    cgsRegionEntry.setStatus("deprecated")


class _CgsRegionName_Type(SnmpAdminString):
    """Custom type cgsRegionName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_CgsRegionName_Type.__name__ = "SnmpAdminString"
_CgsRegionName_Object = MibTableColumn
cgsRegionName = _CgsRegionName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 6, 1, 1, 1),
    _CgsRegionName_Type()
)
cgsRegionName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgsRegionName.setStatus("deprecated")
_CgsRegionComments_Type = SnmpAdminString
_CgsRegionComments_Object = MibTableColumn
cgsRegionComments = _CgsRegionComments_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 6, 1, 1, 2),
    _CgsRegionComments_Type()
)
cgsRegionComments.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsRegionComments.setStatus("deprecated")


class _CgsRegionStorageType_Type(StorageType):
    """Custom type cgsRegionStorageType based on StorageType"""


_CgsRegionStorageType_Object = MibTableColumn
cgsRegionStorageType = _CgsRegionStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 6, 1, 1, 3),
    _CgsRegionStorageType_Type()
)
cgsRegionStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsRegionStorageType.setStatus("deprecated")
_CgsRegionRowStatus_Type = RowStatus
_CgsRegionRowStatus_Object = MibTableColumn
cgsRegionRowStatus = _CgsRegionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 6, 1, 1, 4),
    _CgsRegionRowStatus_Type()
)
cgsRegionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsRegionRowStatus.setStatus("deprecated")
_CgsLocationTable_Object = MibTable
cgsLocationTable = _CgsLocationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 6, 2)
)
if mibBuilder.loadTexts:
    cgsLocationTable.setStatus("current")
_CgsLocationEntry_Object = MibTableRow
cgsLocationEntry = _CgsLocationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 6, 2, 1)
)
cgsLocationEntry.setIndexNames(
    (0, "CISCO-GSLB-SYSTEM-MIB", "cgsLocationName"),
)
if mibBuilder.loadTexts:
    cgsLocationEntry.setStatus("current")


class _CgsLocationName_Type(SnmpAdminString):
    """Custom type cgsLocationName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_CgsLocationName_Type.__name__ = "SnmpAdminString"
_CgsLocationName_Object = MibTableColumn
cgsLocationName = _CgsLocationName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 6, 2, 1, 1),
    _CgsLocationName_Type()
)
cgsLocationName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgsLocationName.setStatus("current")
_CgsLocationRegion_Type = SnmpAdminString
_CgsLocationRegion_Object = MibTableColumn
cgsLocationRegion = _CgsLocationRegion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 6, 2, 1, 2),
    _CgsLocationRegion_Type()
)
cgsLocationRegion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsLocationRegion.setStatus("current")
_CgsLocationZone_Type = SnmpAdminString
_CgsLocationZone_Object = MibTableColumn
cgsLocationZone = _CgsLocationZone_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 6, 2, 1, 3),
    _CgsLocationZone_Type()
)
cgsLocationZone.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsLocationZone.setStatus("current")
_CgsLocationComments_Type = SnmpAdminString
_CgsLocationComments_Object = MibTableColumn
cgsLocationComments = _CgsLocationComments_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 6, 2, 1, 4),
    _CgsLocationComments_Type()
)
cgsLocationComments.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsLocationComments.setStatus("current")


class _CgsLocationStorageType_Type(StorageType):
    """Custom type cgsLocationStorageType based on StorageType"""


_CgsLocationStorageType_Object = MibTableColumn
cgsLocationStorageType = _CgsLocationStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 6, 2, 1, 5),
    _CgsLocationStorageType_Type()
)
cgsLocationStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsLocationStorageType.setStatus("current")
_CgsLocationRowStatus_Type = RowStatus
_CgsLocationRowStatus_Object = MibTableColumn
cgsLocationRowStatus = _CgsLocationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 6, 2, 1, 6),
    _CgsLocationRowStatus_Type()
)
cgsLocationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsLocationRowStatus.setStatus("current")
_CgsRegionIdTable_Object = MibTable
cgsRegionIdTable = _CgsRegionIdTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 6, 3)
)
if mibBuilder.loadTexts:
    cgsRegionIdTable.setStatus("current")
_CgsRegionIdEntry_Object = MibTableRow
cgsRegionIdEntry = _CgsRegionIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 6, 3, 1)
)
cgsRegionIdEntry.setIndexNames(
    (0, "CISCO-GSLB-SYSTEM-MIB", "cgsRegionId"),
)
if mibBuilder.loadTexts:
    cgsRegionIdEntry.setStatus("current")


class _CgsRegionId_Type(Unsigned32):
    """Custom type cgsRegionId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CgsRegionId_Type.__name__ = "Unsigned32"
_CgsRegionId_Object = MibTableColumn
cgsRegionId = _CgsRegionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 6, 3, 1, 1),
    _CgsRegionId_Type()
)
cgsRegionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgsRegionId.setStatus("current")


class _CgsRegionIdName_Type(SnmpAdminString):
    """Custom type cgsRegionIdName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_CgsRegionIdName_Type.__name__ = "SnmpAdminString"
_CgsRegionIdName_Object = MibTableColumn
cgsRegionIdName = _CgsRegionIdName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 6, 3, 1, 2),
    _CgsRegionIdName_Type()
)
cgsRegionIdName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsRegionIdName.setStatus("current")
_CgsRegionIdComments_Type = SnmpAdminString
_CgsRegionIdComments_Object = MibTableColumn
cgsRegionIdComments = _CgsRegionIdComments_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 6, 3, 1, 3),
    _CgsRegionIdComments_Type()
)
cgsRegionIdComments.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsRegionIdComments.setStatus("current")
_CgsReqCountPerRegionId_Type = Counter32
_CgsReqCountPerRegionId_Object = MibTableColumn
cgsReqCountPerRegionId = _CgsReqCountPerRegionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 6, 3, 1, 4),
    _CgsReqCountPerRegionId_Type()
)
cgsReqCountPerRegionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsReqCountPerRegionId.setStatus("current")
if mibBuilder.loadTexts:
    cgsReqCountPerRegionId.setUnits("number of hits")
_CgsReqCountRatePerRegionId1Min_Type = Gauge32
_CgsReqCountRatePerRegionId1Min_Object = MibTableColumn
cgsReqCountRatePerRegionId1Min = _CgsReqCountRatePerRegionId1Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 6, 3, 1, 5),
    _CgsReqCountRatePerRegionId1Min_Type()
)
cgsReqCountRatePerRegionId1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsReqCountRatePerRegionId1Min.setStatus("current")
if mibBuilder.loadTexts:
    cgsReqCountRatePerRegionId1Min.setUnits("hits per second")
_CgsReqCountRatePerRegionId5Min_Type = Gauge32
_CgsReqCountRatePerRegionId5Min_Object = MibTableColumn
cgsReqCountRatePerRegionId5Min = _CgsReqCountRatePerRegionId5Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 6, 3, 1, 6),
    _CgsReqCountRatePerRegionId5Min_Type()
)
cgsReqCountRatePerRegionId5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsReqCountRatePerRegionId5Min.setStatus("current")
if mibBuilder.loadTexts:
    cgsReqCountRatePerRegionId5Min.setUnits("hits per second")
_CgsReqCountRatePerRegionId30Min_Type = Gauge32
_CgsReqCountRatePerRegionId30Min_Object = MibTableColumn
cgsReqCountRatePerRegionId30Min = _CgsReqCountRatePerRegionId30Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 6, 3, 1, 7),
    _CgsReqCountRatePerRegionId30Min_Type()
)
cgsReqCountRatePerRegionId30Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsReqCountRatePerRegionId30Min.setStatus("current")
if mibBuilder.loadTexts:
    cgsReqCountRatePerRegionId30Min.setUnits("hits per second")
_CgsReqCountRatePerRegionId4Hr_Type = Gauge32
_CgsReqCountRatePerRegionId4Hr_Object = MibTableColumn
cgsReqCountRatePerRegionId4Hr = _CgsReqCountRatePerRegionId4Hr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 6, 3, 1, 8),
    _CgsReqCountRatePerRegionId4Hr_Type()
)
cgsReqCountRatePerRegionId4Hr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsReqCountRatePerRegionId4Hr.setStatus("current")
if mibBuilder.loadTexts:
    cgsReqCountRatePerRegionId4Hr.setUnits("hits per second")
_CgsAnswerCountPerRegionId_Type = Counter32
_CgsAnswerCountPerRegionId_Object = MibTableColumn
cgsAnswerCountPerRegionId = _CgsAnswerCountPerRegionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 6, 3, 1, 9),
    _CgsAnswerCountPerRegionId_Type()
)
cgsAnswerCountPerRegionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsAnswerCountPerRegionId.setStatus("current")
if mibBuilder.loadTexts:
    cgsAnswerCountPerRegionId.setUnits("number of hits")
_CgsAnswerCountRatePerRegionId1Min_Type = Gauge32
_CgsAnswerCountRatePerRegionId1Min_Object = MibTableColumn
cgsAnswerCountRatePerRegionId1Min = _CgsAnswerCountRatePerRegionId1Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 6, 3, 1, 10),
    _CgsAnswerCountRatePerRegionId1Min_Type()
)
cgsAnswerCountRatePerRegionId1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsAnswerCountRatePerRegionId1Min.setStatus("current")
if mibBuilder.loadTexts:
    cgsAnswerCountRatePerRegionId1Min.setUnits("hits per second")
_CgsAnswerCountRatePerRegionId5Min_Type = Gauge32
_CgsAnswerCountRatePerRegionId5Min_Object = MibTableColumn
cgsAnswerCountRatePerRegionId5Min = _CgsAnswerCountRatePerRegionId5Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 6, 3, 1, 11),
    _CgsAnswerCountRatePerRegionId5Min_Type()
)
cgsAnswerCountRatePerRegionId5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsAnswerCountRatePerRegionId5Min.setStatus("current")
if mibBuilder.loadTexts:
    cgsAnswerCountRatePerRegionId5Min.setUnits("hits per second")
_CgsAnswerCountRatePerRegionId30Min_Type = Gauge32
_CgsAnswerCountRatePerRegionId30Min_Object = MibTableColumn
cgsAnswerCountRatePerRegionId30Min = _CgsAnswerCountRatePerRegionId30Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 6, 3, 1, 12),
    _CgsAnswerCountRatePerRegionId30Min_Type()
)
cgsAnswerCountRatePerRegionId30Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsAnswerCountRatePerRegionId30Min.setStatus("current")
if mibBuilder.loadTexts:
    cgsAnswerCountRatePerRegionId30Min.setUnits("hits per second")
_CgsAnswerCountRatePerRegionId4Hr_Type = Gauge32
_CgsAnswerCountRatePerRegionId4Hr_Object = MibTableColumn
cgsAnswerCountRatePerRegionId4Hr = _CgsAnswerCountRatePerRegionId4Hr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 6, 3, 1, 13),
    _CgsAnswerCountRatePerRegionId4Hr_Type()
)
cgsAnswerCountRatePerRegionId4Hr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsAnswerCountRatePerRegionId4Hr.setStatus("current")
if mibBuilder.loadTexts:
    cgsAnswerCountRatePerRegionId4Hr.setUnits("hits per second")
_CgsUnAnswerCountPerRegionId_Type = Counter32
_CgsUnAnswerCountPerRegionId_Object = MibTableColumn
cgsUnAnswerCountPerRegionId = _CgsUnAnswerCountPerRegionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 6, 3, 1, 14),
    _CgsUnAnswerCountPerRegionId_Type()
)
cgsUnAnswerCountPerRegionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsUnAnswerCountPerRegionId.setStatus("current")
if mibBuilder.loadTexts:
    cgsUnAnswerCountPerRegionId.setUnits("number of hits")
_CgsUnAnswerCountRatePerRegionId1Min_Type = Gauge32
_CgsUnAnswerCountRatePerRegionId1Min_Object = MibTableColumn
cgsUnAnswerCountRatePerRegionId1Min = _CgsUnAnswerCountRatePerRegionId1Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 6, 3, 1, 15),
    _CgsUnAnswerCountRatePerRegionId1Min_Type()
)
cgsUnAnswerCountRatePerRegionId1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsUnAnswerCountRatePerRegionId1Min.setStatus("current")
if mibBuilder.loadTexts:
    cgsUnAnswerCountRatePerRegionId1Min.setUnits("hits per second")
_CgsUnAnswerCountRatePerRegionId5Min_Type = Gauge32
_CgsUnAnswerCountRatePerRegionId5Min_Object = MibTableColumn
cgsUnAnswerCountRatePerRegionId5Min = _CgsUnAnswerCountRatePerRegionId5Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 6, 3, 1, 16),
    _CgsUnAnswerCountRatePerRegionId5Min_Type()
)
cgsUnAnswerCountRatePerRegionId5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsUnAnswerCountRatePerRegionId5Min.setStatus("current")
if mibBuilder.loadTexts:
    cgsUnAnswerCountRatePerRegionId5Min.setUnits("hits per second")
_CgsUnAnswerCountRatePerRegionId30Min_Type = Gauge32
_CgsUnAnswerCountRatePerRegionId30Min_Object = MibTableColumn
cgsUnAnswerCountRatePerRegionId30Min = _CgsUnAnswerCountRatePerRegionId30Min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 6, 3, 1, 17),
    _CgsUnAnswerCountRatePerRegionId30Min_Type()
)
cgsUnAnswerCountRatePerRegionId30Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsUnAnswerCountRatePerRegionId30Min.setStatus("current")
if mibBuilder.loadTexts:
    cgsUnAnswerCountRatePerRegionId30Min.setUnits("hits per second")
_CgsUnAnswerCountRatePerRegionId4Hr_Type = Gauge32
_CgsUnAnswerCountRatePerRegionId4Hr_Object = MibTableColumn
cgsUnAnswerCountRatePerRegionId4Hr = _CgsUnAnswerCountRatePerRegionId4Hr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 6, 3, 1, 18),
    _CgsUnAnswerCountRatePerRegionId4Hr_Type()
)
cgsUnAnswerCountRatePerRegionId4Hr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsUnAnswerCountRatePerRegionId4Hr.setStatus("current")
if mibBuilder.loadTexts:
    cgsUnAnswerCountRatePerRegionId4Hr.setUnits("hits per second")


class _CgsRegionIdStorageType_Type(StorageType):
    """Custom type cgsRegionIdStorageType based on StorageType"""


_CgsRegionIdStorageType_Object = MibTableColumn
cgsRegionIdStorageType = _CgsRegionIdStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 6, 3, 1, 19),
    _CgsRegionIdStorageType_Type()
)
cgsRegionIdStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsRegionIdStorageType.setStatus("current")
_CgsRegionIdRowStatus_Type = RowStatus
_CgsRegionIdRowStatus_Object = MibTableColumn
cgsRegionIdRowStatus = _CgsRegionIdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 1, 6, 3, 1, 20),
    _CgsRegionIdRowStatus_Type()
)
cgsRegionIdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsRegionIdRowStatus.setStatus("current")
_CiscoGslbSystemMIBConform_ObjectIdentity = ObjectIdentity
ciscoGslbSystemMIBConform = _CiscoGslbSystemMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 2)
)
_CiscoGslbSystemMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoGslbSystemMIBCompliances = _CiscoGslbSystemMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 2, 1)
)
_CiscoGslbSystemMIBGroups_ObjectIdentity = ObjectIdentity
ciscoGslbSystemMIBGroups = _CiscoGslbSystemMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 2, 2)
)

# Managed Objects groups

ciscoGslbSystemGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 2, 2, 1)
)
ciscoGslbSystemGeneralGroup.setObjects(
      *(("CISCO-GSLB-SYSTEM-MIB", "cgsNodeService"),
        ("CISCO-GSLB-SYSTEM-MIB", "cgsNodeCommIfName"),
        ("CISCO-GSLB-SYSTEM-MIB", "cgsNodeCommIfIndex"),
        ("CISCO-GSLB-SYSTEM-MIB", "cgsNodeStatus"),
        ("CISCO-GSLB-SYSTEM-MIB", "cgsNodeLocation"),
        ("CISCO-GSLB-SYSTEM-MIB", "cgsNodeRegion"))
)
if mibBuilder.loadTexts:
    ciscoGslbSystemGeneralGroup.setStatus("current")

ciscoGslbSystemPeerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 2, 2, 2)
)
ciscoGslbSystemPeerGroup.setObjects(
      *(("CISCO-GSLB-SYSTEM-MIB", "cgsPeerLocation"),
        ("CISCO-GSLB-SYSTEM-MIB", "cgsPeerDnsName"),
        ("CISCO-GSLB-SYSTEM-MIB", "cgsPeerService"),
        ("CISCO-GSLB-SYSTEM-MIB", "cgsPeerStatus"),
        ("CISCO-GSLB-SYSTEM-MIB", "cgsPeerVersion"))
)
if mibBuilder.loadTexts:
    ciscoGslbSystemPeerGroup.setStatus("current")

ciscoGslbSystemProxZoneGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 2, 2, 3)
)
ciscoGslbSystemProxZoneGroup.setObjects(
      *(("CISCO-GSLB-SYSTEM-MIB", "cgsProxPrimaryAddressType"),
        ("CISCO-GSLB-SYSTEM-MIB", "cgsProxPrimaryAddress"),
        ("CISCO-GSLB-SYSTEM-MIB", "cgsProxSecondaryAddressType"),
        ("CISCO-GSLB-SYSTEM-MIB", "cgsProxSecondaryAddress"),
        ("CISCO-GSLB-SYSTEM-MIB", "cgsProxEchoSentReqs"),
        ("CISCO-GSLB-SYSTEM-MIB", "cgsProxEchoRcvdResps"),
        ("CISCO-GSLB-SYSTEM-MIB", "cgsProxSentMeasureReqs"),
        ("CISCO-GSLB-SYSTEM-MIB", "cgsProxRcvdMeasureResps"),
        ("CISCO-GSLB-SYSTEM-MIB", "cgsProxTotalSentReqs"),
        ("CISCO-GSLB-SYSTEM-MIB", "cgsProxTotalRcvdResps"),
        ("CISCO-GSLB-SYSTEM-MIB", "cgsProxSendRate"),
        ("CISCO-GSLB-SYSTEM-MIB", "cgsProxRcvdRate"),
        ("CISCO-GSLB-SYSTEM-MIB", "cgsProxPeakSendRate"),
        ("CISCO-GSLB-SYSTEM-MIB", "cgsProxPeakRcvdRate"),
        ("CISCO-GSLB-SYSTEM-MIB", "cgsProxStorageType"),
        ("CISCO-GSLB-SYSTEM-MIB", "cgsProxRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoGslbSystemProxZoneGroup.setStatus("current")

ciscoGslbSystemResourceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 2, 2, 4)
)
ciscoGslbSystemResourceGroup.setObjects(
      *(("CISCO-GSLB-SYSTEM-MIB", "cgsRegionComments"),
        ("CISCO-GSLB-SYSTEM-MIB", "cgsRegionStorageType"),
        ("CISCO-GSLB-SYSTEM-MIB", "cgsRegionRowStatus"),
        ("CISCO-GSLB-SYSTEM-MIB", "cgsLocationRegion"),
        ("CISCO-GSLB-SYSTEM-MIB", "cgsLocationZone"),
        ("CISCO-GSLB-SYSTEM-MIB", "cgsLocationComments"),
        ("CISCO-GSLB-SYSTEM-MIB", "cgsLocationStorageType"),
        ("CISCO-GSLB-SYSTEM-MIB", "cgsLocationRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoGslbSystemResourceGroup.setStatus("deprecated")

ciscoGslbSystemNotifControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 2, 2, 5)
)
ciscoGslbSystemNotifControlGroup.setObjects(
    ("CISCO-GSLB-SYSTEM-MIB", "cgsPeerEventNotifEnable")
)
if mibBuilder.loadTexts:
    ciscoGslbSystemNotifControlGroup.setStatus("current")

ciscoGslbSystemNotifObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 2, 2, 6)
)
ciscoGslbSystemNotifObjectsGroup.setObjects(
    ("CISCO-GSLB-SYSTEM-MIB", "cgsPeerPrevStatus")
)
if mibBuilder.loadTexts:
    ciscoGslbSystemNotifObjectsGroup.setStatus("current")

ciscoGslbSystemResourceLocationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 2, 2, 8)
)
ciscoGslbSystemResourceLocationGroup.setObjects(
      *(("CISCO-GSLB-SYSTEM-MIB", "cgsLocationRegion"),
        ("CISCO-GSLB-SYSTEM-MIB", "cgsLocationZone"),
        ("CISCO-GSLB-SYSTEM-MIB", "cgsLocationComments"),
        ("CISCO-GSLB-SYSTEM-MIB", "cgsLocationStorageType"),
        ("CISCO-GSLB-SYSTEM-MIB", "cgsLocationRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoGslbSystemResourceLocationGroup.setStatus("current")

ciscoGslbSystemResourceRegionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 2, 2, 9)
)
ciscoGslbSystemResourceRegionGroup.setObjects(
      *(("CISCO-GSLB-SYSTEM-MIB", "cgsRegionIdName"),
        ("CISCO-GSLB-SYSTEM-MIB", "cgsRegionIdComments"),
        ("CISCO-GSLB-SYSTEM-MIB", "cgsReqCountPerRegionId"),
        ("CISCO-GSLB-SYSTEM-MIB", "cgsReqCountRatePerRegionId1Min"),
        ("CISCO-GSLB-SYSTEM-MIB", "cgsReqCountRatePerRegionId5Min"),
        ("CISCO-GSLB-SYSTEM-MIB", "cgsReqCountRatePerRegionId30Min"),
        ("CISCO-GSLB-SYSTEM-MIB", "cgsReqCountRatePerRegionId4Hr"),
        ("CISCO-GSLB-SYSTEM-MIB", "cgsAnswerCountPerRegionId"),
        ("CISCO-GSLB-SYSTEM-MIB", "cgsAnswerCountRatePerRegionId1Min"),
        ("CISCO-GSLB-SYSTEM-MIB", "cgsAnswerCountRatePerRegionId5Min"),
        ("CISCO-GSLB-SYSTEM-MIB", "cgsAnswerCountRatePerRegionId30Min"),
        ("CISCO-GSLB-SYSTEM-MIB", "cgsAnswerCountRatePerRegionId4Hr"),
        ("CISCO-GSLB-SYSTEM-MIB", "cgsUnAnswerCountPerRegionId"),
        ("CISCO-GSLB-SYSTEM-MIB", "cgsUnAnswerCountRatePerRegionId1Min"),
        ("CISCO-GSLB-SYSTEM-MIB", "cgsUnAnswerCountRatePerRegionId5Min"),
        ("CISCO-GSLB-SYSTEM-MIB", "cgsUnAnswerCountRatePerRegionId30Min"),
        ("CISCO-GSLB-SYSTEM-MIB", "cgsUnAnswerCountRatePerRegionId4Hr"),
        ("CISCO-GSLB-SYSTEM-MIB", "cgsRegionIdStorageType"),
        ("CISCO-GSLB-SYSTEM-MIB", "cgsRegionIdRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoGslbSystemResourceRegionGroup.setStatus("current")


# Notification objects

ciscoGslbSystemPeerEventStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 0, 1)
)
ciscoGslbSystemPeerEventStatus.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CISCO-GSLB-SYSTEM-MIB", "cgsPeerDnsName"),
        ("CISCO-GSLB-SYSTEM-MIB", "cgsPeerService"),
        ("CISCO-GSLB-SYSTEM-MIB", "cgsPeerPrevStatus"),
        ("CISCO-GSLB-SYSTEM-MIB", "cgsPeerStatus"))
)
if mibBuilder.loadTexts:
    ciscoGslbSystemPeerEventStatus.setStatus(
        "current"
    )


# Notifications groups

ciscoGslbSystemNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 2, 2, 7)
)
ciscoGslbSystemNotifGroup.setObjects(
    ("CISCO-GSLB-SYSTEM-MIB", "ciscoGslbSystemPeerEventStatus")
)
if mibBuilder.loadTexts:
    ciscoGslbSystemNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoGslbSystemMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoGslbSystemMIBCompliance.setStatus(
        "deprecated"
    )

ciscoGslbSystemMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 589, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoGslbSystemMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-GSLB-SYSTEM-MIB",
    **{"ciscoGslbSystemMIB": ciscoGslbSystemMIB,
       "ciscoGslbSystemMIBNotifs": ciscoGslbSystemMIBNotifs,
       "ciscoGslbSystemPeerEventStatus": ciscoGslbSystemPeerEventStatus,
       "ciscoGslbSystemMIBObjects": ciscoGslbSystemMIBObjects,
       "cgsNotifControl": cgsNotifControl,
       "cgsPeerEventNotifEnable": cgsPeerEventNotifEnable,
       "cgsNotifObjects": cgsNotifObjects,
       "cgsPeerPrevStatus": cgsPeerPrevStatus,
       "cgsGeneral": cgsGeneral,
       "cgsNodeService": cgsNodeService,
       "cgsNodeCommIfName": cgsNodeCommIfName,
       "cgsNodeCommIfIndex": cgsNodeCommIfIndex,
       "cgsNodeStatus": cgsNodeStatus,
       "cgsNodeLocation": cgsNodeLocation,
       "cgsNodeRegion": cgsNodeRegion,
       "cgsPeer": cgsPeer,
       "cgsPeerTable": cgsPeerTable,
       "cgsPeerEntry": cgsPeerEntry,
       "cgsPeerAddressType": cgsPeerAddressType,
       "cgsPeerAddress": cgsPeerAddress,
       "cgsPeerLocation": cgsPeerLocation,
       "cgsPeerDnsName": cgsPeerDnsName,
       "cgsPeerService": cgsPeerService,
       "cgsPeerStatus": cgsPeerStatus,
       "cgsPeerVersion": cgsPeerVersion,
       "cgsProxZoneStats": cgsProxZoneStats,
       "cgsProxZoneTable": cgsProxZoneTable,
       "cgsProxZoneEntry": cgsProxZoneEntry,
       "cgsProxZoneName": cgsProxZoneName,
       "cgsProxPrimaryAddressType": cgsProxPrimaryAddressType,
       "cgsProxPrimaryAddress": cgsProxPrimaryAddress,
       "cgsProxSecondaryAddressType": cgsProxSecondaryAddressType,
       "cgsProxSecondaryAddress": cgsProxSecondaryAddress,
       "cgsProxEchoSentReqs": cgsProxEchoSentReqs,
       "cgsProxEchoRcvdResps": cgsProxEchoRcvdResps,
       "cgsProxSentMeasureReqs": cgsProxSentMeasureReqs,
       "cgsProxRcvdMeasureResps": cgsProxRcvdMeasureResps,
       "cgsProxTotalSentReqs": cgsProxTotalSentReqs,
       "cgsProxTotalRcvdResps": cgsProxTotalRcvdResps,
       "cgsProxSendRate": cgsProxSendRate,
       "cgsProxRcvdRate": cgsProxRcvdRate,
       "cgsProxPeakSendRate": cgsProxPeakSendRate,
       "cgsProxPeakRcvdRate": cgsProxPeakRcvdRate,
       "cgsProxStorageType": cgsProxStorageType,
       "cgsProxRowStatus": cgsProxRowStatus,
       "cgsResources": cgsResources,
       "cgsRegionTable": cgsRegionTable,
       "cgsRegionEntry": cgsRegionEntry,
       "cgsRegionName": cgsRegionName,
       "cgsRegionComments": cgsRegionComments,
       "cgsRegionStorageType": cgsRegionStorageType,
       "cgsRegionRowStatus": cgsRegionRowStatus,
       "cgsLocationTable": cgsLocationTable,
       "cgsLocationEntry": cgsLocationEntry,
       "cgsLocationName": cgsLocationName,
       "cgsLocationRegion": cgsLocationRegion,
       "cgsLocationZone": cgsLocationZone,
       "cgsLocationComments": cgsLocationComments,
       "cgsLocationStorageType": cgsLocationStorageType,
       "cgsLocationRowStatus": cgsLocationRowStatus,
       "cgsRegionIdTable": cgsRegionIdTable,
       "cgsRegionIdEntry": cgsRegionIdEntry,
       "cgsRegionId": cgsRegionId,
       "cgsRegionIdName": cgsRegionIdName,
       "cgsRegionIdComments": cgsRegionIdComments,
       "cgsReqCountPerRegionId": cgsReqCountPerRegionId,
       "cgsReqCountRatePerRegionId1Min": cgsReqCountRatePerRegionId1Min,
       "cgsReqCountRatePerRegionId5Min": cgsReqCountRatePerRegionId5Min,
       "cgsReqCountRatePerRegionId30Min": cgsReqCountRatePerRegionId30Min,
       "cgsReqCountRatePerRegionId4Hr": cgsReqCountRatePerRegionId4Hr,
       "cgsAnswerCountPerRegionId": cgsAnswerCountPerRegionId,
       "cgsAnswerCountRatePerRegionId1Min": cgsAnswerCountRatePerRegionId1Min,
       "cgsAnswerCountRatePerRegionId5Min": cgsAnswerCountRatePerRegionId5Min,
       "cgsAnswerCountRatePerRegionId30Min": cgsAnswerCountRatePerRegionId30Min,
       "cgsAnswerCountRatePerRegionId4Hr": cgsAnswerCountRatePerRegionId4Hr,
       "cgsUnAnswerCountPerRegionId": cgsUnAnswerCountPerRegionId,
       "cgsUnAnswerCountRatePerRegionId1Min": cgsUnAnswerCountRatePerRegionId1Min,
       "cgsUnAnswerCountRatePerRegionId5Min": cgsUnAnswerCountRatePerRegionId5Min,
       "cgsUnAnswerCountRatePerRegionId30Min": cgsUnAnswerCountRatePerRegionId30Min,
       "cgsUnAnswerCountRatePerRegionId4Hr": cgsUnAnswerCountRatePerRegionId4Hr,
       "cgsRegionIdStorageType": cgsRegionIdStorageType,
       "cgsRegionIdRowStatus": cgsRegionIdRowStatus,
       "ciscoGslbSystemMIBConform": ciscoGslbSystemMIBConform,
       "ciscoGslbSystemMIBCompliances": ciscoGslbSystemMIBCompliances,
       "ciscoGslbSystemMIBCompliance": ciscoGslbSystemMIBCompliance,
       "ciscoGslbSystemMIBComplianceRev1": ciscoGslbSystemMIBComplianceRev1,
       "ciscoGslbSystemMIBGroups": ciscoGslbSystemMIBGroups,
       "ciscoGslbSystemGeneralGroup": ciscoGslbSystemGeneralGroup,
       "ciscoGslbSystemPeerGroup": ciscoGslbSystemPeerGroup,
       "ciscoGslbSystemProxZoneGroup": ciscoGslbSystemProxZoneGroup,
       "ciscoGslbSystemResourceGroup": ciscoGslbSystemResourceGroup,
       "ciscoGslbSystemNotifControlGroup": ciscoGslbSystemNotifControlGroup,
       "ciscoGslbSystemNotifObjectsGroup": ciscoGslbSystemNotifObjectsGroup,
       "ciscoGslbSystemNotifGroup": ciscoGslbSystemNotifGroup,
       "ciscoGslbSystemResourceLocationGroup": ciscoGslbSystemResourceLocationGroup,
       "ciscoGslbSystemResourceRegionGroup": ciscoGslbSystemResourceRegionGroup}
)
