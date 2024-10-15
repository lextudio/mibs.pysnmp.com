# SNMP MIB module (CISCO-EIGRP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-EIGRP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:59:18 2024
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

(InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifIndex")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoEigrpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 449)
)
ciscoEigrpMIB.setRevisions(
        ("2011-11-24 00:00",
         "2004-11-16 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class EigrpUpTimeString(OctetString, TextualConvention):
    status = "current"
    displayHint = "8a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )



class EigrpVersionString(OctetString, TextualConvention):
    status = "current"
    displayHint = "1d.1d/1d.1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )



# MIB Managed Objects in the order of their OIDs

_CEigrpMIBNotifications_ObjectIdentity = ObjectIdentity
cEigrpMIBNotifications = _CEigrpMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 0)
)
_CEigrpMIBObjects_ObjectIdentity = ObjectIdentity
cEigrpMIBObjects = _CEigrpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1)
)
_CEigrpVpnInfo_ObjectIdentity = ObjectIdentity
cEigrpVpnInfo = _CEigrpVpnInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 1)
)
_CEigrpVpnTable_Object = MibTable
cEigrpVpnTable = _CEigrpVpnTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cEigrpVpnTable.setStatus("current")
_CEigrpVpnEntry_Object = MibTableRow
cEigrpVpnEntry = _CEigrpVpnEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 1, 1, 1)
)
cEigrpVpnEntry.setIndexNames(
    (0, "CISCO-EIGRP-MIB", "cEigrpVpnId"),
)
if mibBuilder.loadTexts:
    cEigrpVpnEntry.setStatus("current")
_CEigrpVpnId_Type = Unsigned32
_CEigrpVpnId_Object = MibTableColumn
cEigrpVpnId = _CEigrpVpnId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 1, 1, 1, 1),
    _CEigrpVpnId_Type()
)
cEigrpVpnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cEigrpVpnId.setStatus("current")
_CEigrpVpnName_Type = SnmpAdminString
_CEigrpVpnName_Object = MibTableColumn
cEigrpVpnName = _CEigrpVpnName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 1, 1, 1, 2),
    _CEigrpVpnName_Type()
)
cEigrpVpnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEigrpVpnName.setStatus("current")
_CEigrpAsInfo_ObjectIdentity = ObjectIdentity
cEigrpAsInfo = _CEigrpAsInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 2)
)
_CEigrpTraffStatsTable_Object = MibTable
cEigrpTraffStatsTable = _CEigrpTraffStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cEigrpTraffStatsTable.setStatus("current")
_CEigrpTraffStatsEntry_Object = MibTableRow
cEigrpTraffStatsEntry = _CEigrpTraffStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 2, 1, 1)
)
cEigrpTraffStatsEntry.setIndexNames(
    (0, "CISCO-EIGRP-MIB", "cEigrpVpnId"),
    (0, "CISCO-EIGRP-MIB", "cEigrpAsNumber"),
)
if mibBuilder.loadTexts:
    cEigrpTraffStatsEntry.setStatus("current")
_CEigrpAsNumber_Type = Unsigned32
_CEigrpAsNumber_Object = MibTableColumn
cEigrpAsNumber = _CEigrpAsNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 2, 1, 1, 1),
    _CEigrpAsNumber_Type()
)
cEigrpAsNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cEigrpAsNumber.setStatus("current")
_CEigrpNbrCount_Type = Unsigned32
_CEigrpNbrCount_Object = MibTableColumn
cEigrpNbrCount = _CEigrpNbrCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 2, 1, 1, 2),
    _CEigrpNbrCount_Type()
)
cEigrpNbrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEigrpNbrCount.setStatus("current")
_CEigrpHellosSent_Type = Counter32
_CEigrpHellosSent_Object = MibTableColumn
cEigrpHellosSent = _CEigrpHellosSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 2, 1, 1, 3),
    _CEigrpHellosSent_Type()
)
cEigrpHellosSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEigrpHellosSent.setStatus("current")
_CEigrpHellosRcvd_Type = Counter32
_CEigrpHellosRcvd_Object = MibTableColumn
cEigrpHellosRcvd = _CEigrpHellosRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 2, 1, 1, 4),
    _CEigrpHellosRcvd_Type()
)
cEigrpHellosRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEigrpHellosRcvd.setStatus("current")
_CEigrpUpdatesSent_Type = Counter32
_CEigrpUpdatesSent_Object = MibTableColumn
cEigrpUpdatesSent = _CEigrpUpdatesSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 2, 1, 1, 5),
    _CEigrpUpdatesSent_Type()
)
cEigrpUpdatesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEigrpUpdatesSent.setStatus("current")
_CEigrpUpdatesRcvd_Type = Counter32
_CEigrpUpdatesRcvd_Object = MibTableColumn
cEigrpUpdatesRcvd = _CEigrpUpdatesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 2, 1, 1, 6),
    _CEigrpUpdatesRcvd_Type()
)
cEigrpUpdatesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEigrpUpdatesRcvd.setStatus("current")
_CEigrpQueriesSent_Type = Counter32
_CEigrpQueriesSent_Object = MibTableColumn
cEigrpQueriesSent = _CEigrpQueriesSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 2, 1, 1, 7),
    _CEigrpQueriesSent_Type()
)
cEigrpQueriesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEigrpQueriesSent.setStatus("current")
_CEigrpQueriesRcvd_Type = Counter32
_CEigrpQueriesRcvd_Object = MibTableColumn
cEigrpQueriesRcvd = _CEigrpQueriesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 2, 1, 1, 8),
    _CEigrpQueriesRcvd_Type()
)
cEigrpQueriesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEigrpQueriesRcvd.setStatus("current")
_CEigrpRepliesSent_Type = Counter32
_CEigrpRepliesSent_Object = MibTableColumn
cEigrpRepliesSent = _CEigrpRepliesSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 2, 1, 1, 9),
    _CEigrpRepliesSent_Type()
)
cEigrpRepliesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEigrpRepliesSent.setStatus("current")
_CEigrpRepliesRcvd_Type = Counter32
_CEigrpRepliesRcvd_Object = MibTableColumn
cEigrpRepliesRcvd = _CEigrpRepliesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 2, 1, 1, 10),
    _CEigrpRepliesRcvd_Type()
)
cEigrpRepliesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEigrpRepliesRcvd.setStatus("current")
_CEigrpAcksSent_Type = Counter32
_CEigrpAcksSent_Object = MibTableColumn
cEigrpAcksSent = _CEigrpAcksSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 2, 1, 1, 11),
    _CEigrpAcksSent_Type()
)
cEigrpAcksSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEigrpAcksSent.setStatus("current")
_CEigrpAcksRcvd_Type = Counter32
_CEigrpAcksRcvd_Object = MibTableColumn
cEigrpAcksRcvd = _CEigrpAcksRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 2, 1, 1, 12),
    _CEigrpAcksRcvd_Type()
)
cEigrpAcksRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEigrpAcksRcvd.setStatus("current")
_CEigrpInputQHighMark_Type = Unsigned32
_CEigrpInputQHighMark_Object = MibTableColumn
cEigrpInputQHighMark = _CEigrpInputQHighMark_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 2, 1, 1, 13),
    _CEigrpInputQHighMark_Type()
)
cEigrpInputQHighMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEigrpInputQHighMark.setStatus("current")
_CEigrpInputQDrops_Type = Counter32
_CEigrpInputQDrops_Object = MibTableColumn
cEigrpInputQDrops = _CEigrpInputQDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 2, 1, 1, 14),
    _CEigrpInputQDrops_Type()
)
cEigrpInputQDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEigrpInputQDrops.setStatus("current")
_CEigrpSiaQueriesSent_Type = Counter32
_CEigrpSiaQueriesSent_Object = MibTableColumn
cEigrpSiaQueriesSent = _CEigrpSiaQueriesSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 2, 1, 1, 15),
    _CEigrpSiaQueriesSent_Type()
)
cEigrpSiaQueriesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEigrpSiaQueriesSent.setStatus("current")
_CEigrpSiaQueriesRcvd_Type = Counter32
_CEigrpSiaQueriesRcvd_Object = MibTableColumn
cEigrpSiaQueriesRcvd = _CEigrpSiaQueriesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 2, 1, 1, 16),
    _CEigrpSiaQueriesRcvd_Type()
)
cEigrpSiaQueriesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEigrpSiaQueriesRcvd.setStatus("current")
_CEigrpAsRouterIdType_Type = InetAddressType
_CEigrpAsRouterIdType_Object = MibTableColumn
cEigrpAsRouterIdType = _CEigrpAsRouterIdType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 2, 1, 1, 17),
    _CEigrpAsRouterIdType_Type()
)
cEigrpAsRouterIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEigrpAsRouterIdType.setStatus("current")
_CEigrpAsRouterId_Type = InetAddress
_CEigrpAsRouterId_Object = MibTableColumn
cEigrpAsRouterId = _CEigrpAsRouterId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 2, 1, 1, 18),
    _CEigrpAsRouterId_Type()
)
cEigrpAsRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEigrpAsRouterId.setStatus("current")
_CEigrpTopoRoutes_Type = Counter32
_CEigrpTopoRoutes_Object = MibTableColumn
cEigrpTopoRoutes = _CEigrpTopoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 2, 1, 1, 19),
    _CEigrpTopoRoutes_Type()
)
cEigrpTopoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEigrpTopoRoutes.setStatus("current")
_CEigrpHeadSerial_Type = Counter64
_CEigrpHeadSerial_Object = MibTableColumn
cEigrpHeadSerial = _CEigrpHeadSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 2, 1, 1, 20),
    _CEigrpHeadSerial_Type()
)
cEigrpHeadSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEigrpHeadSerial.setStatus("current")
_CEigrpNextSerial_Type = Counter64
_CEigrpNextSerial_Object = MibTableColumn
cEigrpNextSerial = _CEigrpNextSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 2, 1, 1, 21),
    _CEigrpNextSerial_Type()
)
cEigrpNextSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEigrpNextSerial.setStatus("current")
_CEigrpXmitPendReplies_Type = Unsigned32
_CEigrpXmitPendReplies_Object = MibTableColumn
cEigrpXmitPendReplies = _CEigrpXmitPendReplies_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 2, 1, 1, 22),
    _CEigrpXmitPendReplies_Type()
)
cEigrpXmitPendReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEigrpXmitPendReplies.setStatus("current")
_CEigrpXmitDummies_Type = Unsigned32
_CEigrpXmitDummies_Object = MibTableColumn
cEigrpXmitDummies = _CEigrpXmitDummies_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 2, 1, 1, 23),
    _CEigrpXmitDummies_Type()
)
cEigrpXmitDummies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEigrpXmitDummies.setStatus("current")
_CEigrpTopologyInfo_ObjectIdentity = ObjectIdentity
cEigrpTopologyInfo = _CEigrpTopologyInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 3)
)
_CEigrpTopoTable_Object = MibTable
cEigrpTopoTable = _CEigrpTopoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cEigrpTopoTable.setStatus("current")
_CEigrpTopoEntry_Object = MibTableRow
cEigrpTopoEntry = _CEigrpTopoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 3, 1, 1)
)
cEigrpTopoEntry.setIndexNames(
    (0, "CISCO-EIGRP-MIB", "cEigrpVpnId"),
    (0, "CISCO-EIGRP-MIB", "cEigrpAsNumber"),
    (0, "CISCO-EIGRP-MIB", "cEigrpDestNetType"),
    (0, "CISCO-EIGRP-MIB", "cEigrpDestNet"),
    (0, "CISCO-EIGRP-MIB", "cEigrpDestNetPrefixLen"),
)
if mibBuilder.loadTexts:
    cEigrpTopoEntry.setStatus("current")
_CEigrpDestNetType_Type = InetAddressType
_CEigrpDestNetType_Object = MibTableColumn
cEigrpDestNetType = _CEigrpDestNetType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 3, 1, 1, 1),
    _CEigrpDestNetType_Type()
)
cEigrpDestNetType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cEigrpDestNetType.setStatus("current")
_CEigrpDestNet_Type = InetAddress
_CEigrpDestNet_Object = MibTableColumn
cEigrpDestNet = _CEigrpDestNet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 3, 1, 1, 2),
    _CEigrpDestNet_Type()
)
cEigrpDestNet.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cEigrpDestNet.setStatus("current")
_CEigrpDestNetPrefixLen_Type = InetAddressPrefixLength
_CEigrpDestNetPrefixLen_Object = MibTableColumn
cEigrpDestNetPrefixLen = _CEigrpDestNetPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 3, 1, 1, 4),
    _CEigrpDestNetPrefixLen_Type()
)
cEigrpDestNetPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cEigrpDestNetPrefixLen.setStatus("current")
_CEigrpActive_Type = TruthValue
_CEigrpActive_Object = MibTableColumn
cEigrpActive = _CEigrpActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 3, 1, 1, 5),
    _CEigrpActive_Type()
)
cEigrpActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEigrpActive.setStatus("current")
_CEigrpStuckInActive_Type = TruthValue
_CEigrpStuckInActive_Object = MibTableColumn
cEigrpStuckInActive = _CEigrpStuckInActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 3, 1, 1, 6),
    _CEigrpStuckInActive_Type()
)
cEigrpStuckInActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEigrpStuckInActive.setStatus("current")
_CEigrpDestSuccessors_Type = Unsigned32
_CEigrpDestSuccessors_Object = MibTableColumn
cEigrpDestSuccessors = _CEigrpDestSuccessors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 3, 1, 1, 7),
    _CEigrpDestSuccessors_Type()
)
cEigrpDestSuccessors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEigrpDestSuccessors.setStatus("current")
_CEigrpFdistance_Type = Unsigned32
_CEigrpFdistance_Object = MibTableColumn
cEigrpFdistance = _CEigrpFdistance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 3, 1, 1, 8),
    _CEigrpFdistance_Type()
)
cEigrpFdistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEigrpFdistance.setStatus("current")
_CEigrpRouteOriginType_Type = SnmpAdminString
_CEigrpRouteOriginType_Object = MibTableColumn
cEigrpRouteOriginType = _CEigrpRouteOriginType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 3, 1, 1, 9),
    _CEigrpRouteOriginType_Type()
)
cEigrpRouteOriginType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEigrpRouteOriginType.setStatus("current")
_CEigrpRouteOriginAddrType_Type = InetAddressType
_CEigrpRouteOriginAddrType_Object = MibTableColumn
cEigrpRouteOriginAddrType = _CEigrpRouteOriginAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 3, 1, 1, 10),
    _CEigrpRouteOriginAddrType_Type()
)
cEigrpRouteOriginAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEigrpRouteOriginAddrType.setStatus("current")
_CEigrpRouteOriginAddr_Type = InetAddress
_CEigrpRouteOriginAddr_Object = MibTableColumn
cEigrpRouteOriginAddr = _CEigrpRouteOriginAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 3, 1, 1, 11),
    _CEigrpRouteOriginAddr_Type()
)
cEigrpRouteOriginAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEigrpRouteOriginAddr.setStatus("current")
_CEigrpNextHopAddressType_Type = InetAddressType
_CEigrpNextHopAddressType_Object = MibTableColumn
cEigrpNextHopAddressType = _CEigrpNextHopAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 3, 1, 1, 12),
    _CEigrpNextHopAddressType_Type()
)
cEigrpNextHopAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEigrpNextHopAddressType.setStatus("current")
_CEigrpNextHopAddress_Type = InetAddress
_CEigrpNextHopAddress_Object = MibTableColumn
cEigrpNextHopAddress = _CEigrpNextHopAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 3, 1, 1, 13),
    _CEigrpNextHopAddress_Type()
)
cEigrpNextHopAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEigrpNextHopAddress.setStatus("current")
_CEigrpNextHopInterface_Type = SnmpAdminString
_CEigrpNextHopInterface_Object = MibTableColumn
cEigrpNextHopInterface = _CEigrpNextHopInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 3, 1, 1, 14),
    _CEigrpNextHopInterface_Type()
)
cEigrpNextHopInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEigrpNextHopInterface.setStatus("current")
_CEigrpDistance_Type = Unsigned32
_CEigrpDistance_Object = MibTableColumn
cEigrpDistance = _CEigrpDistance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 3, 1, 1, 15),
    _CEigrpDistance_Type()
)
cEigrpDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEigrpDistance.setStatus("current")
_CEigrpReportDistance_Type = Unsigned32
_CEigrpReportDistance_Object = MibTableColumn
cEigrpReportDistance = _CEigrpReportDistance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 3, 1, 1, 16),
    _CEigrpReportDistance_Type()
)
cEigrpReportDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEigrpReportDistance.setStatus("current")
_CEigrpFdistanceWide_Type = Counter64
_CEigrpFdistanceWide_Object = MibTableColumn
cEigrpFdistanceWide = _CEigrpFdistanceWide_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 3, 1, 1, 17),
    _CEigrpFdistanceWide_Type()
)
cEigrpFdistanceWide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEigrpFdistanceWide.setStatus("current")
_CEigrpDistanceWide_Type = Counter64
_CEigrpDistanceWide_Object = MibTableColumn
cEigrpDistanceWide = _CEigrpDistanceWide_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 3, 1, 1, 18),
    _CEigrpDistanceWide_Type()
)
cEigrpDistanceWide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEigrpDistanceWide.setStatus("current")
_CEigrpReportDistanceWide_Type = Counter64
_CEigrpReportDistanceWide_Object = MibTableColumn
cEigrpReportDistanceWide = _CEigrpReportDistanceWide_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 3, 1, 1, 19),
    _CEigrpReportDistanceWide_Type()
)
cEigrpReportDistanceWide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEigrpReportDistanceWide.setStatus("current")
_CEigrpPeerInfo_ObjectIdentity = ObjectIdentity
cEigrpPeerInfo = _CEigrpPeerInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 4)
)
_CEigrpPeerTable_Object = MibTable
cEigrpPeerTable = _CEigrpPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cEigrpPeerTable.setStatus("current")
_CEigrpPeerEntry_Object = MibTableRow
cEigrpPeerEntry = _CEigrpPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 4, 1, 1)
)
cEigrpPeerEntry.setIndexNames(
    (0, "CISCO-EIGRP-MIB", "cEigrpVpnId"),
    (0, "CISCO-EIGRP-MIB", "cEigrpAsNumber"),
    (0, "CISCO-EIGRP-MIB", "cEigrpHandle"),
)
if mibBuilder.loadTexts:
    cEigrpPeerEntry.setStatus("current")
_CEigrpHandle_Type = Unsigned32
_CEigrpHandle_Object = MibTableColumn
cEigrpHandle = _CEigrpHandle_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 4, 1, 1, 1),
    _CEigrpHandle_Type()
)
cEigrpHandle.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cEigrpHandle.setStatus("current")
_CEigrpPeerAddrType_Type = InetAddressType
_CEigrpPeerAddrType_Object = MibTableColumn
cEigrpPeerAddrType = _CEigrpPeerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 4, 1, 1, 2),
    _CEigrpPeerAddrType_Type()
)
cEigrpPeerAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEigrpPeerAddrType.setStatus("current")
_CEigrpPeerAddr_Type = InetAddress
_CEigrpPeerAddr_Object = MibTableColumn
cEigrpPeerAddr = _CEigrpPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 4, 1, 1, 3),
    _CEigrpPeerAddr_Type()
)
cEigrpPeerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEigrpPeerAddr.setStatus("current")
_CEigrpPeerIfIndex_Type = InterfaceIndexOrZero
_CEigrpPeerIfIndex_Object = MibTableColumn
cEigrpPeerIfIndex = _CEigrpPeerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 4, 1, 1, 4),
    _CEigrpPeerIfIndex_Type()
)
cEigrpPeerIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEigrpPeerIfIndex.setStatus("current")
_CEigrpHoldTime_Type = Unsigned32
_CEigrpHoldTime_Object = MibTableColumn
cEigrpHoldTime = _CEigrpHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 4, 1, 1, 5),
    _CEigrpHoldTime_Type()
)
cEigrpHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEigrpHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    cEigrpHoldTime.setUnits("seconds")
_CEigrpUpTime_Type = EigrpUpTimeString
_CEigrpUpTime_Object = MibTableColumn
cEigrpUpTime = _CEigrpUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 4, 1, 1, 6),
    _CEigrpUpTime_Type()
)
cEigrpUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEigrpUpTime.setStatus("current")
_CEigrpSrtt_Type = Unsigned32
_CEigrpSrtt_Object = MibTableColumn
cEigrpSrtt = _CEigrpSrtt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 4, 1, 1, 7),
    _CEigrpSrtt_Type()
)
cEigrpSrtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEigrpSrtt.setStatus("current")
if mibBuilder.loadTexts:
    cEigrpSrtt.setUnits("milliseconds")
_CEigrpRto_Type = Unsigned32
_CEigrpRto_Object = MibTableColumn
cEigrpRto = _CEigrpRto_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 4, 1, 1, 8),
    _CEigrpRto_Type()
)
cEigrpRto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEigrpRto.setStatus("current")
if mibBuilder.loadTexts:
    cEigrpRto.setUnits("milliseconds")
_CEigrpPktsEnqueued_Type = Unsigned32
_CEigrpPktsEnqueued_Object = MibTableColumn
cEigrpPktsEnqueued = _CEigrpPktsEnqueued_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 4, 1, 1, 9),
    _CEigrpPktsEnqueued_Type()
)
cEigrpPktsEnqueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEigrpPktsEnqueued.setStatus("current")
_CEigrpLastSeq_Type = Unsigned32
_CEigrpLastSeq_Object = MibTableColumn
cEigrpLastSeq = _CEigrpLastSeq_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 4, 1, 1, 10),
    _CEigrpLastSeq_Type()
)
cEigrpLastSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEigrpLastSeq.setStatus("current")
_CEigrpVersion_Type = EigrpVersionString
_CEigrpVersion_Object = MibTableColumn
cEigrpVersion = _CEigrpVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 4, 1, 1, 11),
    _CEigrpVersion_Type()
)
cEigrpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEigrpVersion.setStatus("current")
_CEigrpRetrans_Type = Counter32
_CEigrpRetrans_Object = MibTableColumn
cEigrpRetrans = _CEigrpRetrans_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 4, 1, 1, 12),
    _CEigrpRetrans_Type()
)
cEigrpRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEigrpRetrans.setStatus("current")
_CEigrpRetries_Type = Unsigned32
_CEigrpRetries_Object = MibTableColumn
cEigrpRetries = _CEigrpRetries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 4, 1, 1, 13),
    _CEigrpRetries_Type()
)
cEigrpRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEigrpRetries.setStatus("current")
_CEigrpInterfaceInfo_ObjectIdentity = ObjectIdentity
cEigrpInterfaceInfo = _CEigrpInterfaceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 5)
)
_CEigrpInterfaceTable_Object = MibTable
cEigrpInterfaceTable = _CEigrpInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cEigrpInterfaceTable.setStatus("current")
_CEigrpInterfaceEntry_Object = MibTableRow
cEigrpInterfaceEntry = _CEigrpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 5, 1, 1)
)
cEigrpInterfaceEntry.setIndexNames(
    (0, "CISCO-EIGRP-MIB", "cEigrpVpnId"),
    (0, "CISCO-EIGRP-MIB", "cEigrpAsNumber"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cEigrpInterfaceEntry.setStatus("current")
_CEigrpPeerCount_Type = Gauge32
_CEigrpPeerCount_Object = MibTableColumn
cEigrpPeerCount = _CEigrpPeerCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 5, 1, 1, 3),
    _CEigrpPeerCount_Type()
)
cEigrpPeerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEigrpPeerCount.setStatus("current")
_CEigrpXmitReliableQ_Type = Gauge32
_CEigrpXmitReliableQ_Object = MibTableColumn
cEigrpXmitReliableQ = _CEigrpXmitReliableQ_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 5, 1, 1, 4),
    _CEigrpXmitReliableQ_Type()
)
cEigrpXmitReliableQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEigrpXmitReliableQ.setStatus("current")
_CEigrpXmitUnreliableQ_Type = Gauge32
_CEigrpXmitUnreliableQ_Object = MibTableColumn
cEigrpXmitUnreliableQ = _CEigrpXmitUnreliableQ_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 5, 1, 1, 5),
    _CEigrpXmitUnreliableQ_Type()
)
cEigrpXmitUnreliableQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEigrpXmitUnreliableQ.setStatus("current")
_CEigrpMeanSrtt_Type = Unsigned32
_CEigrpMeanSrtt_Object = MibTableColumn
cEigrpMeanSrtt = _CEigrpMeanSrtt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 5, 1, 1, 6),
    _CEigrpMeanSrtt_Type()
)
cEigrpMeanSrtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEigrpMeanSrtt.setStatus("current")
if mibBuilder.loadTexts:
    cEigrpMeanSrtt.setUnits("milliseconds")
_CEigrpPacingReliable_Type = Unsigned32
_CEigrpPacingReliable_Object = MibTableColumn
cEigrpPacingReliable = _CEigrpPacingReliable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 5, 1, 1, 7),
    _CEigrpPacingReliable_Type()
)
cEigrpPacingReliable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEigrpPacingReliable.setStatus("current")
if mibBuilder.loadTexts:
    cEigrpPacingReliable.setUnits("milliseconds")
_CEigrpPacingUnreliable_Type = Unsigned32
_CEigrpPacingUnreliable_Object = MibTableColumn
cEigrpPacingUnreliable = _CEigrpPacingUnreliable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 5, 1, 1, 8),
    _CEigrpPacingUnreliable_Type()
)
cEigrpPacingUnreliable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEigrpPacingUnreliable.setStatus("current")
if mibBuilder.loadTexts:
    cEigrpPacingUnreliable.setUnits("milliseconds")
_CEigrpMFlowTimer_Type = Unsigned32
_CEigrpMFlowTimer_Object = MibTableColumn
cEigrpMFlowTimer = _CEigrpMFlowTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 5, 1, 1, 9),
    _CEigrpMFlowTimer_Type()
)
cEigrpMFlowTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEigrpMFlowTimer.setStatus("current")
if mibBuilder.loadTexts:
    cEigrpMFlowTimer.setUnits("milliseconds")
_CEigrpPendingRoutes_Type = Gauge32
_CEigrpPendingRoutes_Object = MibTableColumn
cEigrpPendingRoutes = _CEigrpPendingRoutes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 5, 1, 1, 10),
    _CEigrpPendingRoutes_Type()
)
cEigrpPendingRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEigrpPendingRoutes.setStatus("current")
_CEigrpHelloInterval_Type = Unsigned32
_CEigrpHelloInterval_Object = MibTableColumn
cEigrpHelloInterval = _CEigrpHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 5, 1, 1, 11),
    _CEigrpHelloInterval_Type()
)
cEigrpHelloInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEigrpHelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    cEigrpHelloInterval.setUnits("seconds")
_CEigrpXmitNextSerial_Type = Counter64
_CEigrpXmitNextSerial_Object = MibTableColumn
cEigrpXmitNextSerial = _CEigrpXmitNextSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 5, 1, 1, 12),
    _CEigrpXmitNextSerial_Type()
)
cEigrpXmitNextSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEigrpXmitNextSerial.setStatus("current")
_CEigrpUMcasts_Type = Counter32
_CEigrpUMcasts_Object = MibTableColumn
cEigrpUMcasts = _CEigrpUMcasts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 5, 1, 1, 13),
    _CEigrpUMcasts_Type()
)
cEigrpUMcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEigrpUMcasts.setStatus("current")
_CEigrpRMcasts_Type = Counter32
_CEigrpRMcasts_Object = MibTableColumn
cEigrpRMcasts = _CEigrpRMcasts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 5, 1, 1, 14),
    _CEigrpRMcasts_Type()
)
cEigrpRMcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEigrpRMcasts.setStatus("current")
_CEigrpUUcasts_Type = Counter32
_CEigrpUUcasts_Object = MibTableColumn
cEigrpUUcasts = _CEigrpUUcasts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 5, 1, 1, 15),
    _CEigrpUUcasts_Type()
)
cEigrpUUcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEigrpUUcasts.setStatus("current")
_CEigrpRUcasts_Type = Counter32
_CEigrpRUcasts_Object = MibTableColumn
cEigrpRUcasts = _CEigrpRUcasts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 5, 1, 1, 16),
    _CEigrpRUcasts_Type()
)
cEigrpRUcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEigrpRUcasts.setStatus("current")
_CEigrpMcastExcepts_Type = Counter32
_CEigrpMcastExcepts_Object = MibTableColumn
cEigrpMcastExcepts = _CEigrpMcastExcepts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 5, 1, 1, 17),
    _CEigrpMcastExcepts_Type()
)
cEigrpMcastExcepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEigrpMcastExcepts.setStatus("current")
_CEigrpCRpkts_Type = Counter32
_CEigrpCRpkts_Object = MibTableColumn
cEigrpCRpkts = _CEigrpCRpkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 5, 1, 1, 18),
    _CEigrpCRpkts_Type()
)
cEigrpCRpkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEigrpCRpkts.setStatus("current")
_CEigrpAcksSuppressed_Type = Counter32
_CEigrpAcksSuppressed_Object = MibTableColumn
cEigrpAcksSuppressed = _CEigrpAcksSuppressed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 5, 1, 1, 19),
    _CEigrpAcksSuppressed_Type()
)
cEigrpAcksSuppressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEigrpAcksSuppressed.setStatus("current")
_CEigrpRetransSent_Type = Counter32
_CEigrpRetransSent_Object = MibTableColumn
cEigrpRetransSent = _CEigrpRetransSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 5, 1, 1, 20),
    _CEigrpRetransSent_Type()
)
cEigrpRetransSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEigrpRetransSent.setStatus("current")
_CEigrpOOSrvcd_Type = Counter32
_CEigrpOOSrvcd_Object = MibTableColumn
cEigrpOOSrvcd = _CEigrpOOSrvcd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 5, 1, 1, 21),
    _CEigrpOOSrvcd_Type()
)
cEigrpOOSrvcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEigrpOOSrvcd.setStatus("current")


class _CEigrpAuthMode_Type(Integer32):
    """Custom type cEigrpAuthMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("md5", 2),
          ("none", 1))
    )


_CEigrpAuthMode_Type.__name__ = "Integer32"
_CEigrpAuthMode_Object = MibTableColumn
cEigrpAuthMode = _CEigrpAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 5, 1, 1, 22),
    _CEigrpAuthMode_Type()
)
cEigrpAuthMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEigrpAuthMode.setStatus("current")
_CEigrpAuthKeyChain_Type = SnmpAdminString
_CEigrpAuthKeyChain_Object = MibTableColumn
cEigrpAuthKeyChain = _CEigrpAuthKeyChain_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 1, 5, 1, 1, 23),
    _CEigrpAuthKeyChain_Type()
)
cEigrpAuthKeyChain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cEigrpAuthKeyChain.setStatus("current")
_CEigrpMIBConformance_ObjectIdentity = ObjectIdentity
cEigrpMIBConformance = _CEigrpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 2)
)
_CEigrpMIBCompliances_ObjectIdentity = ObjectIdentity
cEigrpMIBCompliances = _CEigrpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 2, 1)
)
_CEigrpMIBGroups_ObjectIdentity = ObjectIdentity
cEigrpMIBGroups = _CEigrpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 2, 2)
)

# Managed Objects groups

cEigrpVpnDataGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 2, 2, 1)
)
cEigrpVpnDataGroup.setObjects(
    ("CISCO-EIGRP-MIB", "cEigrpVpnName")
)
if mibBuilder.loadTexts:
    cEigrpVpnDataGroup.setStatus("current")

cEigrpTrafficStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 2, 2, 2)
)
cEigrpTrafficStatsGroup.setObjects(
      *(("CISCO-EIGRP-MIB", "cEigrpHellosSent"),
        ("CISCO-EIGRP-MIB", "cEigrpHellosRcvd"),
        ("CISCO-EIGRP-MIB", "cEigrpUpdatesSent"),
        ("CISCO-EIGRP-MIB", "cEigrpUpdatesRcvd"),
        ("CISCO-EIGRP-MIB", "cEigrpQueriesSent"),
        ("CISCO-EIGRP-MIB", "cEigrpQueriesRcvd"),
        ("CISCO-EIGRP-MIB", "cEigrpRepliesSent"),
        ("CISCO-EIGRP-MIB", "cEigrpRepliesRcvd"),
        ("CISCO-EIGRP-MIB", "cEigrpAcksSent"),
        ("CISCO-EIGRP-MIB", "cEigrpAcksRcvd"),
        ("CISCO-EIGRP-MIB", "cEigrpInputQHighMark"),
        ("CISCO-EIGRP-MIB", "cEigrpInputQDrops"),
        ("CISCO-EIGRP-MIB", "cEigrpSiaQueriesSent"),
        ("CISCO-EIGRP-MIB", "cEigrpSiaQueriesRcvd"))
)
if mibBuilder.loadTexts:
    cEigrpTrafficStatsGroup.setStatus("current")

cEigrpInterfaceDataGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 2, 2, 3)
)
cEigrpInterfaceDataGroup.setObjects(
      *(("CISCO-EIGRP-MIB", "cEigrpPeerCount"),
        ("CISCO-EIGRP-MIB", "cEigrpXmitReliableQ"),
        ("CISCO-EIGRP-MIB", "cEigrpXmitUnreliableQ"),
        ("CISCO-EIGRP-MIB", "cEigrpMeanSrtt"),
        ("CISCO-EIGRP-MIB", "cEigrpPacingReliable"),
        ("CISCO-EIGRP-MIB", "cEigrpPacingUnreliable"),
        ("CISCO-EIGRP-MIB", "cEigrpMFlowTimer"),
        ("CISCO-EIGRP-MIB", "cEigrpPendingRoutes"),
        ("CISCO-EIGRP-MIB", "cEigrpHelloInterval"),
        ("CISCO-EIGRP-MIB", "cEigrpXmitNextSerial"),
        ("CISCO-EIGRP-MIB", "cEigrpUMcasts"),
        ("CISCO-EIGRP-MIB", "cEigrpRMcasts"),
        ("CISCO-EIGRP-MIB", "cEigrpUUcasts"),
        ("CISCO-EIGRP-MIB", "cEigrpRUcasts"),
        ("CISCO-EIGRP-MIB", "cEigrpMcastExcepts"),
        ("CISCO-EIGRP-MIB", "cEigrpCRpkts"),
        ("CISCO-EIGRP-MIB", "cEigrpAcksSuppressed"),
        ("CISCO-EIGRP-MIB", "cEigrpRetransSent"),
        ("CISCO-EIGRP-MIB", "cEigrpOOSrvcd"),
        ("CISCO-EIGRP-MIB", "cEigrpAuthMode"),
        ("CISCO-EIGRP-MIB", "cEigrpAuthKeyChain"))
)
if mibBuilder.loadTexts:
    cEigrpInterfaceDataGroup.setStatus("current")

cEigrpPeerDataGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 2, 2, 4)
)
cEigrpPeerDataGroup.setObjects(
      *(("CISCO-EIGRP-MIB", "cEigrpNbrCount"),
        ("CISCO-EIGRP-MIB", "cEigrpPeerAddrType"),
        ("CISCO-EIGRP-MIB", "cEigrpPeerAddr"),
        ("CISCO-EIGRP-MIB", "cEigrpPeerIfIndex"),
        ("CISCO-EIGRP-MIB", "cEigrpHoldTime"),
        ("CISCO-EIGRP-MIB", "cEigrpUpTime"),
        ("CISCO-EIGRP-MIB", "cEigrpSrtt"),
        ("CISCO-EIGRP-MIB", "cEigrpRto"),
        ("CISCO-EIGRP-MIB", "cEigrpPktsEnqueued"),
        ("CISCO-EIGRP-MIB", "cEigrpLastSeq"),
        ("CISCO-EIGRP-MIB", "cEigrpVersion"),
        ("CISCO-EIGRP-MIB", "cEigrpRetrans"),
        ("CISCO-EIGRP-MIB", "cEigrpRetries"))
)
if mibBuilder.loadTexts:
    cEigrpPeerDataGroup.setStatus("current")

cEigrpTopoDataGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 2, 2, 5)
)
cEigrpTopoDataGroup.setObjects(
      *(("CISCO-EIGRP-MIB", "cEigrpAsRouterId"),
        ("CISCO-EIGRP-MIB", "cEigrpAsRouterIdType"),
        ("CISCO-EIGRP-MIB", "cEigrpTopoRoutes"),
        ("CISCO-EIGRP-MIB", "cEigrpHeadSerial"),
        ("CISCO-EIGRP-MIB", "cEigrpNextSerial"),
        ("CISCO-EIGRP-MIB", "cEigrpXmitPendReplies"),
        ("CISCO-EIGRP-MIB", "cEigrpXmitDummies"),
        ("CISCO-EIGRP-MIB", "cEigrpActive"),
        ("CISCO-EIGRP-MIB", "cEigrpStuckInActive"),
        ("CISCO-EIGRP-MIB", "cEigrpDestSuccessors"),
        ("CISCO-EIGRP-MIB", "cEigrpFdistance"),
        ("CISCO-EIGRP-MIB", "cEigrpRouteOriginType"),
        ("CISCO-EIGRP-MIB", "cEigrpRouteOriginAddrType"),
        ("CISCO-EIGRP-MIB", "cEigrpRouteOriginAddr"),
        ("CISCO-EIGRP-MIB", "cEigrpNextHopAddressType"),
        ("CISCO-EIGRP-MIB", "cEigrpNextHopAddress"),
        ("CISCO-EIGRP-MIB", "cEigrpNextHopInterface"),
        ("CISCO-EIGRP-MIB", "cEigrpDistance"),
        ("CISCO-EIGRP-MIB", "cEigrpReportDistance"))
)
if mibBuilder.loadTexts:
    cEigrpTopoDataGroup.setStatus("current")

cEigrpTopoDataGroupSupR01 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 2, 2, 8)
)
cEigrpTopoDataGroupSupR01.setObjects(
      *(("CISCO-EIGRP-MIB", "cEigrpFdistanceWide"),
        ("CISCO-EIGRP-MIB", "cEigrpDistanceWide"),
        ("CISCO-EIGRP-MIB", "cEigrpReportDistanceWide"))
)
if mibBuilder.loadTexts:
    cEigrpTopoDataGroupSupR01.setStatus("current")


# Notification objects

cEigrpAuthFailureEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 0, 1)
)
cEigrpAuthFailureEvent.setObjects(
      *(("CISCO-EIGRP-MIB", "cEigrpPeerAddrType"),
        ("CISCO-EIGRP-MIB", "cEigrpPeerAddr"))
)
if mibBuilder.loadTexts:
    cEigrpAuthFailureEvent.setStatus(
        "current"
    )

cEigrpRouteStuckInActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 0, 2)
)
cEigrpRouteStuckInActive.setObjects(
      *(("CISCO-EIGRP-MIB", "cEigrpPeerAddrType"),
        ("CISCO-EIGRP-MIB", "cEigrpPeerAddr"),
        ("CISCO-EIGRP-MIB", "cEigrpStuckInActive"))
)
if mibBuilder.loadTexts:
    cEigrpRouteStuckInActive.setStatus(
        "current"
    )

cEigrpNbrDownEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 0, 3)
)
cEigrpNbrDownEvent.setObjects(
      *(("CISCO-EIGRP-MIB", "cEigrpPeerAddrType"),
        ("CISCO-EIGRP-MIB", "cEigrpPeerAddr"))
)
if mibBuilder.loadTexts:
    cEigrpNbrDownEvent.setStatus(
        "current"
    )


# Notifications groups

cEigrpNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 2, 2, 6)
)
cEigrpNotificationsGroup.setObjects(
      *(("CISCO-EIGRP-MIB", "cEigrpAuthFailureEvent"),
        ("CISCO-EIGRP-MIB", "cEigrpRouteStuckInActive"))
)
if mibBuilder.loadTexts:
    cEigrpNotificationsGroup.setStatus(
        "current"
    )

cEigrpNotificationsGroupSupR01 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 2, 2, 7)
)
cEigrpNotificationsGroupSupR01.setObjects(
    ("CISCO-EIGRP-MIB", "cEigrpNbrDownEvent")
)
if mibBuilder.loadTexts:
    cEigrpNotificationsGroupSupR01.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cEigrpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cEigrpMIBCompliance.setStatus(
        "deprecated"
    )

cEigrpMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 449, 2, 1, 2)
)
if mibBuilder.loadTexts:
    cEigrpMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-EIGRP-MIB",
    **{"EigrpUpTimeString": EigrpUpTimeString,
       "EigrpVersionString": EigrpVersionString,
       "ciscoEigrpMIB": ciscoEigrpMIB,
       "cEigrpMIBNotifications": cEigrpMIBNotifications,
       "cEigrpAuthFailureEvent": cEigrpAuthFailureEvent,
       "cEigrpRouteStuckInActive": cEigrpRouteStuckInActive,
       "cEigrpNbrDownEvent": cEigrpNbrDownEvent,
       "cEigrpMIBObjects": cEigrpMIBObjects,
       "cEigrpVpnInfo": cEigrpVpnInfo,
       "cEigrpVpnTable": cEigrpVpnTable,
       "cEigrpVpnEntry": cEigrpVpnEntry,
       "cEigrpVpnId": cEigrpVpnId,
       "cEigrpVpnName": cEigrpVpnName,
       "cEigrpAsInfo": cEigrpAsInfo,
       "cEigrpTraffStatsTable": cEigrpTraffStatsTable,
       "cEigrpTraffStatsEntry": cEigrpTraffStatsEntry,
       "cEigrpAsNumber": cEigrpAsNumber,
       "cEigrpNbrCount": cEigrpNbrCount,
       "cEigrpHellosSent": cEigrpHellosSent,
       "cEigrpHellosRcvd": cEigrpHellosRcvd,
       "cEigrpUpdatesSent": cEigrpUpdatesSent,
       "cEigrpUpdatesRcvd": cEigrpUpdatesRcvd,
       "cEigrpQueriesSent": cEigrpQueriesSent,
       "cEigrpQueriesRcvd": cEigrpQueriesRcvd,
       "cEigrpRepliesSent": cEigrpRepliesSent,
       "cEigrpRepliesRcvd": cEigrpRepliesRcvd,
       "cEigrpAcksSent": cEigrpAcksSent,
       "cEigrpAcksRcvd": cEigrpAcksRcvd,
       "cEigrpInputQHighMark": cEigrpInputQHighMark,
       "cEigrpInputQDrops": cEigrpInputQDrops,
       "cEigrpSiaQueriesSent": cEigrpSiaQueriesSent,
       "cEigrpSiaQueriesRcvd": cEigrpSiaQueriesRcvd,
       "cEigrpAsRouterIdType": cEigrpAsRouterIdType,
       "cEigrpAsRouterId": cEigrpAsRouterId,
       "cEigrpTopoRoutes": cEigrpTopoRoutes,
       "cEigrpHeadSerial": cEigrpHeadSerial,
       "cEigrpNextSerial": cEigrpNextSerial,
       "cEigrpXmitPendReplies": cEigrpXmitPendReplies,
       "cEigrpXmitDummies": cEigrpXmitDummies,
       "cEigrpTopologyInfo": cEigrpTopologyInfo,
       "cEigrpTopoTable": cEigrpTopoTable,
       "cEigrpTopoEntry": cEigrpTopoEntry,
       "cEigrpDestNetType": cEigrpDestNetType,
       "cEigrpDestNet": cEigrpDestNet,
       "cEigrpDestNetPrefixLen": cEigrpDestNetPrefixLen,
       "cEigrpActive": cEigrpActive,
       "cEigrpStuckInActive": cEigrpStuckInActive,
       "cEigrpDestSuccessors": cEigrpDestSuccessors,
       "cEigrpFdistance": cEigrpFdistance,
       "cEigrpRouteOriginType": cEigrpRouteOriginType,
       "cEigrpRouteOriginAddrType": cEigrpRouteOriginAddrType,
       "cEigrpRouteOriginAddr": cEigrpRouteOriginAddr,
       "cEigrpNextHopAddressType": cEigrpNextHopAddressType,
       "cEigrpNextHopAddress": cEigrpNextHopAddress,
       "cEigrpNextHopInterface": cEigrpNextHopInterface,
       "cEigrpDistance": cEigrpDistance,
       "cEigrpReportDistance": cEigrpReportDistance,
       "cEigrpFdistanceWide": cEigrpFdistanceWide,
       "cEigrpDistanceWide": cEigrpDistanceWide,
       "cEigrpReportDistanceWide": cEigrpReportDistanceWide,
       "cEigrpPeerInfo": cEigrpPeerInfo,
       "cEigrpPeerTable": cEigrpPeerTable,
       "cEigrpPeerEntry": cEigrpPeerEntry,
       "cEigrpHandle": cEigrpHandle,
       "cEigrpPeerAddrType": cEigrpPeerAddrType,
       "cEigrpPeerAddr": cEigrpPeerAddr,
       "cEigrpPeerIfIndex": cEigrpPeerIfIndex,
       "cEigrpHoldTime": cEigrpHoldTime,
       "cEigrpUpTime": cEigrpUpTime,
       "cEigrpSrtt": cEigrpSrtt,
       "cEigrpRto": cEigrpRto,
       "cEigrpPktsEnqueued": cEigrpPktsEnqueued,
       "cEigrpLastSeq": cEigrpLastSeq,
       "cEigrpVersion": cEigrpVersion,
       "cEigrpRetrans": cEigrpRetrans,
       "cEigrpRetries": cEigrpRetries,
       "cEigrpInterfaceInfo": cEigrpInterfaceInfo,
       "cEigrpInterfaceTable": cEigrpInterfaceTable,
       "cEigrpInterfaceEntry": cEigrpInterfaceEntry,
       "cEigrpPeerCount": cEigrpPeerCount,
       "cEigrpXmitReliableQ": cEigrpXmitReliableQ,
       "cEigrpXmitUnreliableQ": cEigrpXmitUnreliableQ,
       "cEigrpMeanSrtt": cEigrpMeanSrtt,
       "cEigrpPacingReliable": cEigrpPacingReliable,
       "cEigrpPacingUnreliable": cEigrpPacingUnreliable,
       "cEigrpMFlowTimer": cEigrpMFlowTimer,
       "cEigrpPendingRoutes": cEigrpPendingRoutes,
       "cEigrpHelloInterval": cEigrpHelloInterval,
       "cEigrpXmitNextSerial": cEigrpXmitNextSerial,
       "cEigrpUMcasts": cEigrpUMcasts,
       "cEigrpRMcasts": cEigrpRMcasts,
       "cEigrpUUcasts": cEigrpUUcasts,
       "cEigrpRUcasts": cEigrpRUcasts,
       "cEigrpMcastExcepts": cEigrpMcastExcepts,
       "cEigrpCRpkts": cEigrpCRpkts,
       "cEigrpAcksSuppressed": cEigrpAcksSuppressed,
       "cEigrpRetransSent": cEigrpRetransSent,
       "cEigrpOOSrvcd": cEigrpOOSrvcd,
       "cEigrpAuthMode": cEigrpAuthMode,
       "cEigrpAuthKeyChain": cEigrpAuthKeyChain,
       "cEigrpMIBConformance": cEigrpMIBConformance,
       "cEigrpMIBCompliances": cEigrpMIBCompliances,
       "cEigrpMIBCompliance": cEigrpMIBCompliance,
       "cEigrpMIBComplianceRev1": cEigrpMIBComplianceRev1,
       "cEigrpMIBGroups": cEigrpMIBGroups,
       "cEigrpVpnDataGroup": cEigrpVpnDataGroup,
       "cEigrpTrafficStatsGroup": cEigrpTrafficStatsGroup,
       "cEigrpInterfaceDataGroup": cEigrpInterfaceDataGroup,
       "cEigrpPeerDataGroup": cEigrpPeerDataGroup,
       "cEigrpTopoDataGroup": cEigrpTopoDataGroup,
       "cEigrpNotificationsGroup": cEigrpNotificationsGroup,
       "cEigrpNotificationsGroupSupR01": cEigrpNotificationsGroupSupR01,
       "cEigrpTopoDataGroupSupR01": cEigrpTopoDataGroupSupR01}
)
