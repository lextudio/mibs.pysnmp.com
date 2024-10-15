# SNMP MIB module (CISCO-ITP-DSMR-UCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ITP-DSMR-UCP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:03:18 2024
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

(cgspCLLICode,
 cgspEventSequenceNumber,
 cgspInstNetwork) = mibBuilder.importSymbols(
    "CISCO-ITP-GSP-MIB",
    "cgspCLLICode",
    "cgspEventSequenceNumber",
    "cgspInstNetwork")

(CmlrName,) = mibBuilder.importSymbols(
    "CISCO-ITP-MLR-MIB",
    "CmlrName")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

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

ciscoItpDsmrUcpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1302)
)
ciscoItpDsmrUcpMIB.setRevisions(
        ("2005-05-18 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CdsmrUcpInactivityTimer(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1000, 9000000),
    )



class CdsmrUcpResponseTimer(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1000, 10000),
    )



class CdsmrUcpSendWindow(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 100),
    )



class CdsmrUcpSessionInitTimer(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(500, 120000),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoItpDsmrUcpMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoItpDsmrUcpMIBNotifs = _CiscoItpDsmrUcpMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1302, 0)
)
_CiscoItpDsmrUcpMIBObjects_ObjectIdentity = ObjectIdentity
ciscoItpDsmrUcpMIBObjects = _CiscoItpDsmrUcpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1302, 1)
)
_CdsmrUcpScalars_ObjectIdentity = ObjectIdentity
cdsmrUcpScalars = _CdsmrUcpScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1302, 1, 0)
)


class _CdsmrUcpSessionStateNotifEnabled_Type(TruthValue):
    """Custom type cdsmrUcpSessionStateNotifEnabled based on TruthValue"""


_CdsmrUcpSessionStateNotifEnabled_Object = MibScalar
cdsmrUcpSessionStateNotifEnabled = _CdsmrUcpSessionStateNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1302, 1, 0, 1),
    _CdsmrUcpSessionStateNotifEnabled_Type()
)
cdsmrUcpSessionStateNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdsmrUcpSessionStateNotifEnabled.setStatus("current")
_CdsmrUcpProfileTable_Object = MibTable
cdsmrUcpProfileTable = _CdsmrUcpProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1302, 1, 5)
)
if mibBuilder.loadTexts:
    cdsmrUcpProfileTable.setStatus("current")
_CdsmrUcpProfileTableEntry_Object = MibTableRow
cdsmrUcpProfileTableEntry = _CdsmrUcpProfileTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1302, 1, 5, 1)
)
cdsmrUcpProfileTableEntry.setIndexNames(
    (0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"),
    (0, "CISCO-ITP-DSMR-UCP-MIB", "cdsmrUcpProfileName"),
)
if mibBuilder.loadTexts:
    cdsmrUcpProfileTableEntry.setStatus("current")
_CdsmrUcpProfileName_Type = CmlrName
_CdsmrUcpProfileName_Object = MibTableColumn
cdsmrUcpProfileName = _CdsmrUcpProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1302, 1, 5, 1, 1),
    _CdsmrUcpProfileName_Type()
)
cdsmrUcpProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdsmrUcpProfileName.setStatus("current")
_CdsmrUcpProfileInactivityTimer_Type = CdsmrUcpInactivityTimer
_CdsmrUcpProfileInactivityTimer_Object = MibTableColumn
cdsmrUcpProfileInactivityTimer = _CdsmrUcpProfileInactivityTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1302, 1, 5, 1, 2),
    _CdsmrUcpProfileInactivityTimer_Type()
)
cdsmrUcpProfileInactivityTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrUcpProfileInactivityTimer.setStatus("current")
if mibBuilder.loadTexts:
    cdsmrUcpProfileInactivityTimer.setUnits("milliseconds")
_CdsmrUcpProfileResponseTimer_Type = CdsmrUcpResponseTimer
_CdsmrUcpProfileResponseTimer_Object = MibTableColumn
cdsmrUcpProfileResponseTimer = _CdsmrUcpProfileResponseTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1302, 1, 5, 1, 3),
    _CdsmrUcpProfileResponseTimer_Type()
)
cdsmrUcpProfileResponseTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrUcpProfileResponseTimer.setStatus("current")
if mibBuilder.loadTexts:
    cdsmrUcpProfileResponseTimer.setUnits("milliseconds")
_CdsmrUcpProfileSendWindow_Type = CdsmrUcpSendWindow
_CdsmrUcpProfileSendWindow_Object = MibTableColumn
cdsmrUcpProfileSendWindow = _CdsmrUcpProfileSendWindow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1302, 1, 5, 1, 7),
    _CdsmrUcpProfileSendWindow_Type()
)
cdsmrUcpProfileSendWindow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrUcpProfileSendWindow.setStatus("current")
if mibBuilder.loadTexts:
    cdsmrUcpProfileSendWindow.setUnits("bytes")
_CdsmrUcpProfileSessionInitTimer_Type = CdsmrUcpSessionInitTimer
_CdsmrUcpProfileSessionInitTimer_Object = MibTableColumn
cdsmrUcpProfileSessionInitTimer = _CdsmrUcpProfileSessionInitTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1302, 1, 5, 1, 8),
    _CdsmrUcpProfileSessionInitTimer_Type()
)
cdsmrUcpProfileSessionInitTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrUcpProfileSessionInitTimer.setStatus("current")
if mibBuilder.loadTexts:
    cdsmrUcpProfileSessionInitTimer.setUnits("milliseconds")
_CdsmrUcpProfileRowStatus_Type = RowStatus
_CdsmrUcpProfileRowStatus_Object = MibTableColumn
cdsmrUcpProfileRowStatus = _CdsmrUcpProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1302, 1, 5, 1, 9),
    _CdsmrUcpProfileRowStatus_Type()
)
cdsmrUcpProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrUcpProfileRowStatus.setStatus("current")
_CdsmrUcpSessionTable_Object = MibTable
cdsmrUcpSessionTable = _CdsmrUcpSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1302, 1, 6)
)
if mibBuilder.loadTexts:
    cdsmrUcpSessionTable.setStatus("current")
_CdsmrUcpSessionTableEntry_Object = MibTableRow
cdsmrUcpSessionTableEntry = _CdsmrUcpSessionTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1302, 1, 6, 1)
)
cdsmrUcpSessionTableEntry.setIndexNames(
    (0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"),
    (0, "CISCO-ITP-DSMR-UCP-MIB", "cdsmrUcpSessionLocalPortNumber"),
)
if mibBuilder.loadTexts:
    cdsmrUcpSessionTableEntry.setStatus("current")
_CdsmrUcpSessionLocalPortNumber_Type = InetPortNumber
_CdsmrUcpSessionLocalPortNumber_Object = MibTableColumn
cdsmrUcpSessionLocalPortNumber = _CdsmrUcpSessionLocalPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1302, 1, 6, 1, 1),
    _CdsmrUcpSessionLocalPortNumber_Type()
)
cdsmrUcpSessionLocalPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdsmrUcpSessionLocalPortNumber.setStatus("current")
_CdsmrUcpSessionLocalIpAddrType_Type = InetAddressType
_CdsmrUcpSessionLocalIpAddrType_Object = MibTableColumn
cdsmrUcpSessionLocalIpAddrType = _CdsmrUcpSessionLocalIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1302, 1, 6, 1, 2),
    _CdsmrUcpSessionLocalIpAddrType_Type()
)
cdsmrUcpSessionLocalIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrUcpSessionLocalIpAddrType.setStatus("current")
_CdsmrUcpSessionLocalIpAddress_Type = InetAddress
_CdsmrUcpSessionLocalIpAddress_Object = MibTableColumn
cdsmrUcpSessionLocalIpAddress = _CdsmrUcpSessionLocalIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1302, 1, 6, 1, 3),
    _CdsmrUcpSessionLocalIpAddress_Type()
)
cdsmrUcpSessionLocalIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrUcpSessionLocalIpAddress.setStatus("current")
_CdsmrUcpSessionDynamicDest_Type = TruthValue
_CdsmrUcpSessionDynamicDest_Object = MibTableColumn
cdsmrUcpSessionDynamicDest = _CdsmrUcpSessionDynamicDest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1302, 1, 6, 1, 4),
    _CdsmrUcpSessionDynamicDest_Type()
)
cdsmrUcpSessionDynamicDest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrUcpSessionDynamicDest.setStatus("current")
_CdsmrUcpSessionRowStatus_Type = RowStatus
_CdsmrUcpSessionRowStatus_Object = MibTableColumn
cdsmrUcpSessionRowStatus = _CdsmrUcpSessionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1302, 1, 6, 1, 5),
    _CdsmrUcpSessionRowStatus_Type()
)
cdsmrUcpSessionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrUcpSessionRowStatus.setStatus("current")
_CdsmrUcpDestTable_Object = MibTable
cdsmrUcpDestTable = _CdsmrUcpDestTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1302, 1, 7)
)
if mibBuilder.loadTexts:
    cdsmrUcpDestTable.setStatus("current")
_CdsmrUcpDestTableEntry_Object = MibTableRow
cdsmrUcpDestTableEntry = _CdsmrUcpDestTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1302, 1, 7, 1)
)
cdsmrUcpDestTableEntry.setIndexNames(
    (0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"),
    (0, "CISCO-ITP-DSMR-UCP-MIB", "cdsmrUcpSessionLocalPortNumber"),
    (0, "CISCO-ITP-DSMR-UCP-MIB", "cdsmrUcpDestName"),
)
if mibBuilder.loadTexts:
    cdsmrUcpDestTableEntry.setStatus("current")
_CdsmrUcpDestName_Type = CmlrName
_CdsmrUcpDestName_Object = MibTableColumn
cdsmrUcpDestName = _CdsmrUcpDestName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1302, 1, 7, 1, 1),
    _CdsmrUcpDestName_Type()
)
cdsmrUcpDestName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdsmrUcpDestName.setStatus("current")
_CdsmrUcpDestInactivityTimer_Type = CdsmrUcpInactivityTimer
_CdsmrUcpDestInactivityTimer_Object = MibTableColumn
cdsmrUcpDestInactivityTimer = _CdsmrUcpDestInactivityTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1302, 1, 7, 1, 2),
    _CdsmrUcpDestInactivityTimer_Type()
)
cdsmrUcpDestInactivityTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrUcpDestInactivityTimer.setStatus("current")
if mibBuilder.loadTexts:
    cdsmrUcpDestInactivityTimer.setUnits("milliseconds")
_CdsmrUcpDestResponseTimer_Type = CdsmrUcpResponseTimer
_CdsmrUcpDestResponseTimer_Object = MibTableColumn
cdsmrUcpDestResponseTimer = _CdsmrUcpDestResponseTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1302, 1, 7, 1, 3),
    _CdsmrUcpDestResponseTimer_Type()
)
cdsmrUcpDestResponseTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrUcpDestResponseTimer.setStatus("current")
if mibBuilder.loadTexts:
    cdsmrUcpDestResponseTimer.setUnits("milliseconds")
_CdsmrUcpDestSendWindow_Type = CdsmrUcpSendWindow
_CdsmrUcpDestSendWindow_Object = MibTableColumn
cdsmrUcpDestSendWindow = _CdsmrUcpDestSendWindow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1302, 1, 7, 1, 4),
    _CdsmrUcpDestSendWindow_Type()
)
cdsmrUcpDestSendWindow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrUcpDestSendWindow.setStatus("current")
if mibBuilder.loadTexts:
    cdsmrUcpDestSendWindow.setUnits("bytes")
_CdsmrUcpDestSessionInitTimer_Type = CdsmrUcpSessionInitTimer
_CdsmrUcpDestSessionInitTimer_Object = MibTableColumn
cdsmrUcpDestSessionInitTimer = _CdsmrUcpDestSessionInitTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1302, 1, 7, 1, 5),
    _CdsmrUcpDestSessionInitTimer_Type()
)
cdsmrUcpDestSessionInitTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrUcpDestSessionInitTimer.setStatus("current")
if mibBuilder.loadTexts:
    cdsmrUcpDestSessionInitTimer.setUnits("milliseconds")
_CdsmrUcpDestRemotePortNumber_Type = InetPortNumber
_CdsmrUcpDestRemotePortNumber_Object = MibTableColumn
cdsmrUcpDestRemotePortNumber = _CdsmrUcpDestRemotePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1302, 1, 7, 1, 6),
    _CdsmrUcpDestRemotePortNumber_Type()
)
cdsmrUcpDestRemotePortNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrUcpDestRemotePortNumber.setStatus("current")
_CdsmrUcpDestRemoteIpAddrType_Type = InetAddressType
_CdsmrUcpDestRemoteIpAddrType_Object = MibTableColumn
cdsmrUcpDestRemoteIpAddrType = _CdsmrUcpDestRemoteIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1302, 1, 7, 1, 7),
    _CdsmrUcpDestRemoteIpAddrType_Type()
)
cdsmrUcpDestRemoteIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrUcpDestRemoteIpAddrType.setStatus("current")
_CdsmrUcpDestRemoteIpAddress_Type = InetAddress
_CdsmrUcpDestRemoteIpAddress_Object = MibTableColumn
cdsmrUcpDestRemoteIpAddress = _CdsmrUcpDestRemoteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1302, 1, 7, 1, 8),
    _CdsmrUcpDestRemoteIpAddress_Type()
)
cdsmrUcpDestRemoteIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrUcpDestRemoteIpAddress.setStatus("current")
_CdsmrUcpDestProfileName_Type = CmlrName
_CdsmrUcpDestProfileName_Object = MibTableColumn
cdsmrUcpDestProfileName = _CdsmrUcpDestProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1302, 1, 7, 1, 9),
    _CdsmrUcpDestProfileName_Type()
)
cdsmrUcpDestProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrUcpDestProfileName.setStatus("current")


class _CdsmrUcpDestState_Type(Integer32):
    """Custom type cdsmrUcpDestState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2),
          ("open", 3))
    )


_CdsmrUcpDestState_Type.__name__ = "Integer32"
_CdsmrUcpDestState_Object = MibTableColumn
cdsmrUcpDestState = _CdsmrUcpDestState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1302, 1, 7, 1, 10),
    _CdsmrUcpDestState_Type()
)
cdsmrUcpDestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdsmrUcpDestState.setStatus("current")
_CdsmrUcpDestSentRequests_Type = Counter32
_CdsmrUcpDestSentRequests_Object = MibTableColumn
cdsmrUcpDestSentRequests = _CdsmrUcpDestSentRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1302, 1, 7, 1, 11),
    _CdsmrUcpDestSentRequests_Type()
)
cdsmrUcpDestSentRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdsmrUcpDestSentRequests.setStatus("current")
if mibBuilder.loadTexts:
    cdsmrUcpDestSentRequests.setUnits("requests")
_CdsmrUcpDestRcvdRequests_Type = Counter32
_CdsmrUcpDestRcvdRequests_Object = MibTableColumn
cdsmrUcpDestRcvdRequests = _CdsmrUcpDestRcvdRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1302, 1, 7, 1, 12),
    _CdsmrUcpDestRcvdRequests_Type()
)
cdsmrUcpDestRcvdRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdsmrUcpDestRcvdRequests.setStatus("current")
if mibBuilder.loadTexts:
    cdsmrUcpDestRcvdRequests.setUnits("requests")
_CdsmrUcpDestSentResponses_Type = Counter32
_CdsmrUcpDestSentResponses_Object = MibTableColumn
cdsmrUcpDestSentResponses = _CdsmrUcpDestSentResponses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1302, 1, 7, 1, 13),
    _CdsmrUcpDestSentResponses_Type()
)
cdsmrUcpDestSentResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdsmrUcpDestSentResponses.setStatus("current")
if mibBuilder.loadTexts:
    cdsmrUcpDestSentResponses.setUnits("responses")
_CdsmrUcpDestRcvdResponses_Type = Counter32
_CdsmrUcpDestRcvdResponses_Object = MibTableColumn
cdsmrUcpDestRcvdResponses = _CdsmrUcpDestRcvdResponses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1302, 1, 7, 1, 14),
    _CdsmrUcpDestRcvdResponses_Type()
)
cdsmrUcpDestRcvdResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdsmrUcpDestRcvdResponses.setStatus("current")
if mibBuilder.loadTexts:
    cdsmrUcpDestRcvdResponses.setUnits("responses")
_CdsmrUcpDestRowStatus_Type = RowStatus
_CdsmrUcpDestRowStatus_Object = MibTableColumn
cdsmrUcpDestRowStatus = _CdsmrUcpDestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1302, 1, 7, 1, 15),
    _CdsmrUcpDestRowStatus_Type()
)
cdsmrUcpDestRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cdsmrUcpDestRowStatus.setStatus("current")
_CiscoItpDsmrUcpMIBConform_ObjectIdentity = ObjectIdentity
ciscoItpDsmrUcpMIBConform = _CiscoItpDsmrUcpMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1302, 2)
)
_CiscoItpDsmrUcpMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoItpDsmrUcpMIBCompliances = _CiscoItpDsmrUcpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1302, 2, 1)
)
_CiscoItpDsmrUcpMIBGroups_ObjectIdentity = ObjectIdentity
ciscoItpDsmrUcpMIBGroups = _CiscoItpDsmrUcpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1302, 2, 2)
)

# Managed Objects groups

ciscoItpDsmrUcpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1302, 2, 2, 1)
)
ciscoItpDsmrUcpGroup.setObjects(
      *(("CISCO-ITP-DSMR-UCP-MIB", "cdsmrUcpSessionStateNotifEnabled"),
        ("CISCO-ITP-DSMR-UCP-MIB", "cdsmrUcpProfileInactivityTimer"),
        ("CISCO-ITP-DSMR-UCP-MIB", "cdsmrUcpProfileResponseTimer"),
        ("CISCO-ITP-DSMR-UCP-MIB", "cdsmrUcpProfileSendWindow"),
        ("CISCO-ITP-DSMR-UCP-MIB", "cdsmrUcpProfileSessionInitTimer"),
        ("CISCO-ITP-DSMR-UCP-MIB", "cdsmrUcpProfileRowStatus"),
        ("CISCO-ITP-DSMR-UCP-MIB", "cdsmrUcpSessionLocalIpAddrType"),
        ("CISCO-ITP-DSMR-UCP-MIB", "cdsmrUcpSessionLocalIpAddress"),
        ("CISCO-ITP-DSMR-UCP-MIB", "cdsmrUcpSessionDynamicDest"),
        ("CISCO-ITP-DSMR-UCP-MIB", "cdsmrUcpSessionRowStatus"),
        ("CISCO-ITP-DSMR-UCP-MIB", "cdsmrUcpDestInactivityTimer"),
        ("CISCO-ITP-DSMR-UCP-MIB", "cdsmrUcpDestResponseTimer"),
        ("CISCO-ITP-DSMR-UCP-MIB", "cdsmrUcpDestSendWindow"),
        ("CISCO-ITP-DSMR-UCP-MIB", "cdsmrUcpDestSessionInitTimer"),
        ("CISCO-ITP-DSMR-UCP-MIB", "cdsmrUcpDestRemotePortNumber"),
        ("CISCO-ITP-DSMR-UCP-MIB", "cdsmrUcpDestRemoteIpAddrType"),
        ("CISCO-ITP-DSMR-UCP-MIB", "cdsmrUcpDestRemoteIpAddress"),
        ("CISCO-ITP-DSMR-UCP-MIB", "cdsmrUcpDestProfileName"),
        ("CISCO-ITP-DSMR-UCP-MIB", "cdsmrUcpDestState"),
        ("CISCO-ITP-DSMR-UCP-MIB", "cdsmrUcpDestSentRequests"),
        ("CISCO-ITP-DSMR-UCP-MIB", "cdsmrUcpDestRcvdRequests"),
        ("CISCO-ITP-DSMR-UCP-MIB", "cdsmrUcpDestSentResponses"),
        ("CISCO-ITP-DSMR-UCP-MIB", "cdsmrUcpDestRcvdResponses"),
        ("CISCO-ITP-DSMR-UCP-MIB", "cdsmrUcpDestRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoItpDsmrUcpGroup.setStatus("current")


# Notification objects

ciscoItpDsmrUcpSessionState = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 1302, 0, 1)
)
ciscoItpDsmrUcpSessionState.setObjects(
      *(("CISCO-ITP-GSP-MIB", "cgspEventSequenceNumber"),
        ("CISCO-ITP-GSP-MIB", "cgspCLLICode"),
        ("CISCO-ITP-DSMR-UCP-MIB", "cdsmrUcpDestState"))
)
if mibBuilder.loadTexts:
    ciscoItpDsmrUcpSessionState.setStatus(
        "current"
    )


# Notifications groups

ciscoItpDsmrUcpNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 1302, 2, 2, 2)
)
ciscoItpDsmrUcpNotificationsGroup.setObjects(
    ("CISCO-ITP-DSMR-UCP-MIB", "ciscoItpDsmrUcpSessionState")
)
if mibBuilder.loadTexts:
    ciscoItpDsmrUcpNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoItpDsmrUcpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 1302, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoItpDsmrUcpMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ITP-DSMR-UCP-MIB",
    **{"CdsmrUcpInactivityTimer": CdsmrUcpInactivityTimer,
       "CdsmrUcpResponseTimer": CdsmrUcpResponseTimer,
       "CdsmrUcpSendWindow": CdsmrUcpSendWindow,
       "CdsmrUcpSessionInitTimer": CdsmrUcpSessionInitTimer,
       "ciscoItpDsmrUcpMIB": ciscoItpDsmrUcpMIB,
       "ciscoItpDsmrUcpMIBNotifs": ciscoItpDsmrUcpMIBNotifs,
       "ciscoItpDsmrUcpSessionState": ciscoItpDsmrUcpSessionState,
       "ciscoItpDsmrUcpMIBObjects": ciscoItpDsmrUcpMIBObjects,
       "cdsmrUcpScalars": cdsmrUcpScalars,
       "cdsmrUcpSessionStateNotifEnabled": cdsmrUcpSessionStateNotifEnabled,
       "cdsmrUcpProfileTable": cdsmrUcpProfileTable,
       "cdsmrUcpProfileTableEntry": cdsmrUcpProfileTableEntry,
       "cdsmrUcpProfileName": cdsmrUcpProfileName,
       "cdsmrUcpProfileInactivityTimer": cdsmrUcpProfileInactivityTimer,
       "cdsmrUcpProfileResponseTimer": cdsmrUcpProfileResponseTimer,
       "cdsmrUcpProfileSendWindow": cdsmrUcpProfileSendWindow,
       "cdsmrUcpProfileSessionInitTimer": cdsmrUcpProfileSessionInitTimer,
       "cdsmrUcpProfileRowStatus": cdsmrUcpProfileRowStatus,
       "cdsmrUcpSessionTable": cdsmrUcpSessionTable,
       "cdsmrUcpSessionTableEntry": cdsmrUcpSessionTableEntry,
       "cdsmrUcpSessionLocalPortNumber": cdsmrUcpSessionLocalPortNumber,
       "cdsmrUcpSessionLocalIpAddrType": cdsmrUcpSessionLocalIpAddrType,
       "cdsmrUcpSessionLocalIpAddress": cdsmrUcpSessionLocalIpAddress,
       "cdsmrUcpSessionDynamicDest": cdsmrUcpSessionDynamicDest,
       "cdsmrUcpSessionRowStatus": cdsmrUcpSessionRowStatus,
       "cdsmrUcpDestTable": cdsmrUcpDestTable,
       "cdsmrUcpDestTableEntry": cdsmrUcpDestTableEntry,
       "cdsmrUcpDestName": cdsmrUcpDestName,
       "cdsmrUcpDestInactivityTimer": cdsmrUcpDestInactivityTimer,
       "cdsmrUcpDestResponseTimer": cdsmrUcpDestResponseTimer,
       "cdsmrUcpDestSendWindow": cdsmrUcpDestSendWindow,
       "cdsmrUcpDestSessionInitTimer": cdsmrUcpDestSessionInitTimer,
       "cdsmrUcpDestRemotePortNumber": cdsmrUcpDestRemotePortNumber,
       "cdsmrUcpDestRemoteIpAddrType": cdsmrUcpDestRemoteIpAddrType,
       "cdsmrUcpDestRemoteIpAddress": cdsmrUcpDestRemoteIpAddress,
       "cdsmrUcpDestProfileName": cdsmrUcpDestProfileName,
       "cdsmrUcpDestState": cdsmrUcpDestState,
       "cdsmrUcpDestSentRequests": cdsmrUcpDestSentRequests,
       "cdsmrUcpDestRcvdRequests": cdsmrUcpDestRcvdRequests,
       "cdsmrUcpDestSentResponses": cdsmrUcpDestSentResponses,
       "cdsmrUcpDestRcvdResponses": cdsmrUcpDestRcvdResponses,
       "cdsmrUcpDestRowStatus": cdsmrUcpDestRowStatus,
       "ciscoItpDsmrUcpMIBConform": ciscoItpDsmrUcpMIBConform,
       "ciscoItpDsmrUcpMIBCompliances": ciscoItpDsmrUcpMIBCompliances,
       "ciscoItpDsmrUcpMIBCompliance": ciscoItpDsmrUcpMIBCompliance,
       "ciscoItpDsmrUcpMIBGroups": ciscoItpDsmrUcpMIBGroups,
       "ciscoItpDsmrUcpGroup": ciscoItpDsmrUcpGroup,
       "ciscoItpDsmrUcpNotificationsGroup": ciscoItpDsmrUcpNotificationsGroup}
)
