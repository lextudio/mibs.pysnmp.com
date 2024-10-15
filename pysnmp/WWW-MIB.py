# SNMP MIB module (WWW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WWW-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:15:29 2024
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

(DateAndTime,
 DisplayString,
 TextualConvention,
 TimeInterval) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TimeInterval")

(Utf8String,) = mibBuilder.importSymbols(
    "SYSAPPL-MIB",
    "Utf8String")


# MODULE-IDENTITY

wwwMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 65)
)
wwwMIB.setRevisions(
        ("1999-02-25 14:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class WwwRequestType(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )



class WwwResponseType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class WwwOperStatus(Integer32, TextualConvention):
    status = "current"
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
        *(("congested", 4),
          ("down", 1),
          ("halted", 3),
          ("restarting", 5),
          ("running", 2))
    )



class WwwDocName(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs

_WwwMIBObjects_ObjectIdentity = ObjectIdentity
wwwMIBObjects = _WwwMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 65, 1)
)
_WwwService_ObjectIdentity = ObjectIdentity
wwwService = _WwwService_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 65, 1, 1)
)
_WwwServiceTable_Object = MibTable
wwwServiceTable = _WwwServiceTable_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 1, 1)
)
if mibBuilder.loadTexts:
    wwwServiceTable.setStatus("current")
_WwwServiceEntry_Object = MibTableRow
wwwServiceEntry = _WwwServiceEntry_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 1, 1, 1)
)
wwwServiceEntry.setIndexNames(
    (0, "WWW-MIB", "wwwServiceIndex"),
)
if mibBuilder.loadTexts:
    wwwServiceEntry.setStatus("current")


class _WwwServiceIndex_Type(Unsigned32):
    """Custom type wwwServiceIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_WwwServiceIndex_Type.__name__ = "Unsigned32"
_WwwServiceIndex_Object = MibTableColumn
wwwServiceIndex = _WwwServiceIndex_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 1, 1, 1, 1),
    _WwwServiceIndex_Type()
)
wwwServiceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwwServiceIndex.setStatus("current")
_WwwServiceDescription_Type = Utf8String
_WwwServiceDescription_Object = MibTableColumn
wwwServiceDescription = _WwwServiceDescription_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 1, 1, 1, 2),
    _WwwServiceDescription_Type()
)
wwwServiceDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwServiceDescription.setStatus("current")
_WwwServiceContact_Type = Utf8String
_WwwServiceContact_Object = MibTableColumn
wwwServiceContact = _WwwServiceContact_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 1, 1, 1, 3),
    _WwwServiceContact_Type()
)
wwwServiceContact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwServiceContact.setStatus("current")
_WwwServiceProtocol_Type = ObjectIdentifier
_WwwServiceProtocol_Object = MibTableColumn
wwwServiceProtocol = _WwwServiceProtocol_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 1, 1, 1, 4),
    _WwwServiceProtocol_Type()
)
wwwServiceProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwServiceProtocol.setStatus("current")
_WwwServiceName_Type = DisplayString
_WwwServiceName_Object = MibTableColumn
wwwServiceName = _WwwServiceName_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 1, 1, 1, 5),
    _WwwServiceName_Type()
)
wwwServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwServiceName.setStatus("current")


class _WwwServiceType_Type(Integer32):
    """Custom type wwwServiceType based on Integer32"""
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
        *(("wwwCachingProxy", 5),
          ("wwwClient", 3),
          ("wwwOther", 1),
          ("wwwProxy", 4),
          ("wwwServer", 2))
    )


_WwwServiceType_Type.__name__ = "Integer32"
_WwwServiceType_Object = MibTableColumn
wwwServiceType = _WwwServiceType_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 1, 1, 1, 6),
    _WwwServiceType_Type()
)
wwwServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwServiceType.setStatus("current")
_WwwServiceStartTime_Type = DateAndTime
_WwwServiceStartTime_Object = MibTableColumn
wwwServiceStartTime = _WwwServiceStartTime_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 1, 1, 1, 7),
    _WwwServiceStartTime_Type()
)
wwwServiceStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwServiceStartTime.setStatus("current")
_WwwServiceOperStatus_Type = WwwOperStatus
_WwwServiceOperStatus_Object = MibTableColumn
wwwServiceOperStatus = _WwwServiceOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 1, 1, 1, 8),
    _WwwServiceOperStatus_Type()
)
wwwServiceOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwServiceOperStatus.setStatus("current")
_WwwServiceLastChange_Type = DateAndTime
_WwwServiceLastChange_Object = MibTableColumn
wwwServiceLastChange = _WwwServiceLastChange_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 1, 1, 1, 9),
    _WwwServiceLastChange_Type()
)
wwwServiceLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwServiceLastChange.setStatus("current")
_WwwProtocolStatistics_ObjectIdentity = ObjectIdentity
wwwProtocolStatistics = _WwwProtocolStatistics_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 65, 1, 2)
)
_WwwSummaryTable_Object = MibTable
wwwSummaryTable = _WwwSummaryTable_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 2, 1)
)
if mibBuilder.loadTexts:
    wwwSummaryTable.setStatus("current")
_WwwSummaryEntry_Object = MibTableRow
wwwSummaryEntry = _WwwSummaryEntry_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 2, 1, 1)
)
wwwSummaryEntry.setIndexNames(
    (0, "WWW-MIB", "wwwServiceIndex"),
)
if mibBuilder.loadTexts:
    wwwSummaryEntry.setStatus("current")
_WwwSummaryInRequests_Type = Counter32
_WwwSummaryInRequests_Object = MibTableColumn
wwwSummaryInRequests = _WwwSummaryInRequests_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 2, 1, 1, 1),
    _WwwSummaryInRequests_Type()
)
wwwSummaryInRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwSummaryInRequests.setStatus("current")
_WwwSummaryOutRequests_Type = Counter32
_WwwSummaryOutRequests_Object = MibTableColumn
wwwSummaryOutRequests = _WwwSummaryOutRequests_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 2, 1, 1, 2),
    _WwwSummaryOutRequests_Type()
)
wwwSummaryOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwSummaryOutRequests.setStatus("current")
_WwwSummaryInResponses_Type = Counter32
_WwwSummaryInResponses_Object = MibTableColumn
wwwSummaryInResponses = _WwwSummaryInResponses_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 2, 1, 1, 3),
    _WwwSummaryInResponses_Type()
)
wwwSummaryInResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwSummaryInResponses.setStatus("current")
_WwwSummaryOutResponses_Type = Counter32
_WwwSummaryOutResponses_Object = MibTableColumn
wwwSummaryOutResponses = _WwwSummaryOutResponses_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 2, 1, 1, 4),
    _WwwSummaryOutResponses_Type()
)
wwwSummaryOutResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwSummaryOutResponses.setStatus("current")
_WwwSummaryInBytes_Type = Counter64
_WwwSummaryInBytes_Object = MibTableColumn
wwwSummaryInBytes = _WwwSummaryInBytes_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 2, 1, 1, 5),
    _WwwSummaryInBytes_Type()
)
wwwSummaryInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwSummaryInBytes.setStatus("current")
_WwwSummaryInLowBytes_Type = Counter32
_WwwSummaryInLowBytes_Object = MibTableColumn
wwwSummaryInLowBytes = _WwwSummaryInLowBytes_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 2, 1, 1, 6),
    _WwwSummaryInLowBytes_Type()
)
wwwSummaryInLowBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwSummaryInLowBytes.setStatus("current")
_WwwSummaryOutBytes_Type = Counter64
_WwwSummaryOutBytes_Object = MibTableColumn
wwwSummaryOutBytes = _WwwSummaryOutBytes_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 2, 1, 1, 7),
    _WwwSummaryOutBytes_Type()
)
wwwSummaryOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwSummaryOutBytes.setStatus("current")
_WwwSummaryOutLowBytes_Type = Counter32
_WwwSummaryOutLowBytes_Object = MibTableColumn
wwwSummaryOutLowBytes = _WwwSummaryOutLowBytes_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 2, 1, 1, 8),
    _WwwSummaryOutLowBytes_Type()
)
wwwSummaryOutLowBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwSummaryOutLowBytes.setStatus("current")
_WwwRequestInTable_Object = MibTable
wwwRequestInTable = _WwwRequestInTable_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 2, 2)
)
if mibBuilder.loadTexts:
    wwwRequestInTable.setStatus("current")
_WwwRequestInEntry_Object = MibTableRow
wwwRequestInEntry = _WwwRequestInEntry_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 2, 2, 1)
)
wwwRequestInEntry.setIndexNames(
    (0, "WWW-MIB", "wwwServiceIndex"),
    (0, "WWW-MIB", "wwwRequestInIndex"),
)
if mibBuilder.loadTexts:
    wwwRequestInEntry.setStatus("current")
_WwwRequestInIndex_Type = WwwRequestType
_WwwRequestInIndex_Object = MibTableColumn
wwwRequestInIndex = _WwwRequestInIndex_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 2, 2, 1, 1),
    _WwwRequestInIndex_Type()
)
wwwRequestInIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwwRequestInIndex.setStatus("current")
_WwwRequestInRequests_Type = Counter32
_WwwRequestInRequests_Object = MibTableColumn
wwwRequestInRequests = _WwwRequestInRequests_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 2, 2, 1, 2),
    _WwwRequestInRequests_Type()
)
wwwRequestInRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwRequestInRequests.setStatus("current")
_WwwRequestInBytes_Type = Counter32
_WwwRequestInBytes_Object = MibTableColumn
wwwRequestInBytes = _WwwRequestInBytes_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 2, 2, 1, 3),
    _WwwRequestInBytes_Type()
)
wwwRequestInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwRequestInBytes.setStatus("current")
_WwwRequestInLastTime_Type = DateAndTime
_WwwRequestInLastTime_Object = MibTableColumn
wwwRequestInLastTime = _WwwRequestInLastTime_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 2, 2, 1, 4),
    _WwwRequestInLastTime_Type()
)
wwwRequestInLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwRequestInLastTime.setStatus("current")
_WwwRequestOutTable_Object = MibTable
wwwRequestOutTable = _WwwRequestOutTable_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 2, 3)
)
if mibBuilder.loadTexts:
    wwwRequestOutTable.setStatus("current")
_WwwRequestOutEntry_Object = MibTableRow
wwwRequestOutEntry = _WwwRequestOutEntry_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 2, 3, 1)
)
wwwRequestOutEntry.setIndexNames(
    (0, "WWW-MIB", "wwwServiceIndex"),
    (0, "WWW-MIB", "wwwRequestOutIndex"),
)
if mibBuilder.loadTexts:
    wwwRequestOutEntry.setStatus("current")
_WwwRequestOutIndex_Type = WwwRequestType
_WwwRequestOutIndex_Object = MibTableColumn
wwwRequestOutIndex = _WwwRequestOutIndex_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 2, 3, 1, 1),
    _WwwRequestOutIndex_Type()
)
wwwRequestOutIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwwRequestOutIndex.setStatus("current")
_WwwRequestOutRequests_Type = Counter32
_WwwRequestOutRequests_Object = MibTableColumn
wwwRequestOutRequests = _WwwRequestOutRequests_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 2, 3, 1, 2),
    _WwwRequestOutRequests_Type()
)
wwwRequestOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwRequestOutRequests.setStatus("current")
_WwwRequestOutBytes_Type = Counter32
_WwwRequestOutBytes_Object = MibTableColumn
wwwRequestOutBytes = _WwwRequestOutBytes_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 2, 3, 1, 3),
    _WwwRequestOutBytes_Type()
)
wwwRequestOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwRequestOutBytes.setStatus("current")
_WwwRequestOutLastTime_Type = DateAndTime
_WwwRequestOutLastTime_Object = MibTableColumn
wwwRequestOutLastTime = _WwwRequestOutLastTime_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 2, 3, 1, 4),
    _WwwRequestOutLastTime_Type()
)
wwwRequestOutLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwRequestOutLastTime.setStatus("current")
_WwwResponseInTable_Object = MibTable
wwwResponseInTable = _WwwResponseInTable_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 2, 4)
)
if mibBuilder.loadTexts:
    wwwResponseInTable.setStatus("current")
_WwwResponseInEntry_Object = MibTableRow
wwwResponseInEntry = _WwwResponseInEntry_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 2, 4, 1)
)
wwwResponseInEntry.setIndexNames(
    (0, "WWW-MIB", "wwwServiceIndex"),
    (0, "WWW-MIB", "wwwResponseInIndex"),
)
if mibBuilder.loadTexts:
    wwwResponseInEntry.setStatus("current")
_WwwResponseInIndex_Type = WwwResponseType
_WwwResponseInIndex_Object = MibTableColumn
wwwResponseInIndex = _WwwResponseInIndex_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 2, 4, 1, 1),
    _WwwResponseInIndex_Type()
)
wwwResponseInIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwwResponseInIndex.setStatus("current")
_WwwResponseInResponses_Type = Counter32
_WwwResponseInResponses_Object = MibTableColumn
wwwResponseInResponses = _WwwResponseInResponses_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 2, 4, 1, 2),
    _WwwResponseInResponses_Type()
)
wwwResponseInResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwResponseInResponses.setStatus("current")
_WwwResponseInBytes_Type = Counter32
_WwwResponseInBytes_Object = MibTableColumn
wwwResponseInBytes = _WwwResponseInBytes_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 2, 4, 1, 3),
    _WwwResponseInBytes_Type()
)
wwwResponseInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwResponseInBytes.setStatus("current")
_WwwResponseInLastTime_Type = DateAndTime
_WwwResponseInLastTime_Object = MibTableColumn
wwwResponseInLastTime = _WwwResponseInLastTime_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 2, 4, 1, 4),
    _WwwResponseInLastTime_Type()
)
wwwResponseInLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwResponseInLastTime.setStatus("current")
_WwwResponseOutTable_Object = MibTable
wwwResponseOutTable = _WwwResponseOutTable_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 2, 5)
)
if mibBuilder.loadTexts:
    wwwResponseOutTable.setStatus("current")
_WwwResponseOutEntry_Object = MibTableRow
wwwResponseOutEntry = _WwwResponseOutEntry_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 2, 5, 1)
)
wwwResponseOutEntry.setIndexNames(
    (0, "WWW-MIB", "wwwServiceIndex"),
    (0, "WWW-MIB", "wwwResponseOutIndex"),
)
if mibBuilder.loadTexts:
    wwwResponseOutEntry.setStatus("current")
_WwwResponseOutIndex_Type = WwwResponseType
_WwwResponseOutIndex_Object = MibTableColumn
wwwResponseOutIndex = _WwwResponseOutIndex_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 2, 5, 1, 1),
    _WwwResponseOutIndex_Type()
)
wwwResponseOutIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwwResponseOutIndex.setStatus("current")
_WwwResponseOutResponses_Type = Counter32
_WwwResponseOutResponses_Object = MibTableColumn
wwwResponseOutResponses = _WwwResponseOutResponses_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 2, 5, 1, 2),
    _WwwResponseOutResponses_Type()
)
wwwResponseOutResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwResponseOutResponses.setStatus("current")
_WwwResponseOutBytes_Type = Counter32
_WwwResponseOutBytes_Object = MibTableColumn
wwwResponseOutBytes = _WwwResponseOutBytes_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 2, 5, 1, 3),
    _WwwResponseOutBytes_Type()
)
wwwResponseOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwResponseOutBytes.setStatus("current")
_WwwResponseOutLastTime_Type = DateAndTime
_WwwResponseOutLastTime_Object = MibTableColumn
wwwResponseOutLastTime = _WwwResponseOutLastTime_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 2, 5, 1, 4),
    _WwwResponseOutLastTime_Type()
)
wwwResponseOutLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwResponseOutLastTime.setStatus("current")
_WwwDocumentStatistics_ObjectIdentity = ObjectIdentity
wwwDocumentStatistics = _WwwDocumentStatistics_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 65, 1, 3)
)
_WwwDocCtrlTable_Object = MibTable
wwwDocCtrlTable = _WwwDocCtrlTable_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 3, 1)
)
if mibBuilder.loadTexts:
    wwwDocCtrlTable.setStatus("current")
_WwwDocCtrlEntry_Object = MibTableRow
wwwDocCtrlEntry = _WwwDocCtrlEntry_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 3, 1, 1)
)
wwwDocCtrlEntry.setIndexNames(
    (0, "WWW-MIB", "wwwServiceIndex"),
)
if mibBuilder.loadTexts:
    wwwDocCtrlEntry.setStatus("current")


class _WwwDocCtrlLastNSize_Type(Unsigned32):
    """Custom type wwwDocCtrlLastNSize based on Unsigned32"""
    defaultValue = 25


_WwwDocCtrlLastNSize_Object = MibTableColumn
wwwDocCtrlLastNSize = _WwwDocCtrlLastNSize_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 3, 1, 1, 1),
    _WwwDocCtrlLastNSize_Type()
)
wwwDocCtrlLastNSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwwDocCtrlLastNSize.setStatus("current")
_WwwDocCtrlLastNLock_Type = TimeTicks
_WwwDocCtrlLastNLock_Object = MibTableColumn
wwwDocCtrlLastNLock = _WwwDocCtrlLastNLock_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 3, 1, 1, 2),
    _WwwDocCtrlLastNLock_Type()
)
wwwDocCtrlLastNLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwwDocCtrlLastNLock.setStatus("current")


class _WwwDocCtrlBuckets_Type(Unsigned32):
    """Custom type wwwDocCtrlBuckets based on Unsigned32"""
    defaultValue = 4


_WwwDocCtrlBuckets_Object = MibTableColumn
wwwDocCtrlBuckets = _WwwDocCtrlBuckets_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 3, 1, 1, 3),
    _WwwDocCtrlBuckets_Type()
)
wwwDocCtrlBuckets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwwDocCtrlBuckets.setStatus("current")


class _WwwDocCtrlBucketTimeInterval_Type(TimeInterval):
    """Custom type wwwDocCtrlBucketTimeInterval based on TimeInterval"""
    defaultValue = 90000


_WwwDocCtrlBucketTimeInterval_Object = MibTableColumn
wwwDocCtrlBucketTimeInterval = _WwwDocCtrlBucketTimeInterval_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 3, 1, 1, 4),
    _WwwDocCtrlBucketTimeInterval_Type()
)
wwwDocCtrlBucketTimeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwwDocCtrlBucketTimeInterval.setStatus("current")


class _WwwDocCtrlTopNSize_Type(Unsigned32):
    """Custom type wwwDocCtrlTopNSize based on Unsigned32"""
    defaultValue = 25


_WwwDocCtrlTopNSize_Object = MibTableColumn
wwwDocCtrlTopNSize = _WwwDocCtrlTopNSize_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 3, 1, 1, 5),
    _WwwDocCtrlTopNSize_Type()
)
wwwDocCtrlTopNSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwwDocCtrlTopNSize.setStatus("current")
_WwwDocLastNTable_Object = MibTable
wwwDocLastNTable = _WwwDocLastNTable_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 3, 2)
)
if mibBuilder.loadTexts:
    wwwDocLastNTable.setStatus("current")
_WwwDocLastNEntry_Object = MibTableRow
wwwDocLastNEntry = _WwwDocLastNEntry_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 3, 2, 1)
)
wwwDocLastNEntry.setIndexNames(
    (0, "WWW-MIB", "wwwServiceIndex"),
    (0, "WWW-MIB", "wwwDocLastNIndex"),
)
if mibBuilder.loadTexts:
    wwwDocLastNEntry.setStatus("current")


class _WwwDocLastNIndex_Type(Unsigned32):
    """Custom type wwwDocLastNIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_WwwDocLastNIndex_Type.__name__ = "Unsigned32"
_WwwDocLastNIndex_Object = MibTableColumn
wwwDocLastNIndex = _WwwDocLastNIndex_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 3, 2, 1, 1),
    _WwwDocLastNIndex_Type()
)
wwwDocLastNIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwwDocLastNIndex.setStatus("current")
_WwwDocLastNName_Type = WwwDocName
_WwwDocLastNName_Object = MibTableColumn
wwwDocLastNName = _WwwDocLastNName_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 3, 2, 1, 2),
    _WwwDocLastNName_Type()
)
wwwDocLastNName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwDocLastNName.setStatus("current")
_WwwDocLastNTimeStamp_Type = DateAndTime
_WwwDocLastNTimeStamp_Object = MibTableColumn
wwwDocLastNTimeStamp = _WwwDocLastNTimeStamp_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 3, 2, 1, 3),
    _WwwDocLastNTimeStamp_Type()
)
wwwDocLastNTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwDocLastNTimeStamp.setStatus("current")
_WwwDocLastNRequestType_Type = WwwRequestType
_WwwDocLastNRequestType_Object = MibTableColumn
wwwDocLastNRequestType = _WwwDocLastNRequestType_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 3, 2, 1, 4),
    _WwwDocLastNRequestType_Type()
)
wwwDocLastNRequestType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwDocLastNRequestType.setStatus("current")
_WwwDocLastNResponseType_Type = WwwResponseType
_WwwDocLastNResponseType_Object = MibTableColumn
wwwDocLastNResponseType = _WwwDocLastNResponseType_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 3, 2, 1, 5),
    _WwwDocLastNResponseType_Type()
)
wwwDocLastNResponseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwDocLastNResponseType.setStatus("current")
_WwwDocLastNStatusMsg_Type = Utf8String
_WwwDocLastNStatusMsg_Object = MibTableColumn
wwwDocLastNStatusMsg = _WwwDocLastNStatusMsg_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 3, 2, 1, 6),
    _WwwDocLastNStatusMsg_Type()
)
wwwDocLastNStatusMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwDocLastNStatusMsg.setStatus("current")
_WwwDocLastNBytes_Type = Unsigned32
_WwwDocLastNBytes_Object = MibTableColumn
wwwDocLastNBytes = _WwwDocLastNBytes_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 3, 2, 1, 7),
    _WwwDocLastNBytes_Type()
)
wwwDocLastNBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwDocLastNBytes.setStatus("current")
_WwwDocBucketTable_Object = MibTable
wwwDocBucketTable = _WwwDocBucketTable_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 3, 3)
)
if mibBuilder.loadTexts:
    wwwDocBucketTable.setStatus("current")
_WwwDocBucketEntry_Object = MibTableRow
wwwDocBucketEntry = _WwwDocBucketEntry_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 3, 3, 1)
)
wwwDocBucketEntry.setIndexNames(
    (0, "WWW-MIB", "wwwServiceIndex"),
    (0, "WWW-MIB", "wwwDocBucketIndex"),
)
if mibBuilder.loadTexts:
    wwwDocBucketEntry.setStatus("current")


class _WwwDocBucketIndex_Type(Unsigned32):
    """Custom type wwwDocBucketIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_WwwDocBucketIndex_Type.__name__ = "Unsigned32"
_WwwDocBucketIndex_Object = MibTableColumn
wwwDocBucketIndex = _WwwDocBucketIndex_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 3, 3, 1, 1),
    _WwwDocBucketIndex_Type()
)
wwwDocBucketIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwwDocBucketIndex.setStatus("current")
_WwwDocBucketTimeStamp_Type = DateAndTime
_WwwDocBucketTimeStamp_Object = MibTableColumn
wwwDocBucketTimeStamp = _WwwDocBucketTimeStamp_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 3, 3, 1, 2),
    _WwwDocBucketTimeStamp_Type()
)
wwwDocBucketTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwDocBucketTimeStamp.setStatus("current")
_WwwDocBucketAccesses_Type = Unsigned32
_WwwDocBucketAccesses_Object = MibTableColumn
wwwDocBucketAccesses = _WwwDocBucketAccesses_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 3, 3, 1, 3),
    _WwwDocBucketAccesses_Type()
)
wwwDocBucketAccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwDocBucketAccesses.setStatus("current")
_WwwDocBucketDocuments_Type = Unsigned32
_WwwDocBucketDocuments_Object = MibTableColumn
wwwDocBucketDocuments = _WwwDocBucketDocuments_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 3, 3, 1, 4),
    _WwwDocBucketDocuments_Type()
)
wwwDocBucketDocuments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwDocBucketDocuments.setStatus("current")
_WwwDocBucketBytes_Type = Unsigned32
_WwwDocBucketBytes_Object = MibTableColumn
wwwDocBucketBytes = _WwwDocBucketBytes_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 3, 3, 1, 5),
    _WwwDocBucketBytes_Type()
)
wwwDocBucketBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwDocBucketBytes.setStatus("current")
_WwwDocAccessTopNTable_Object = MibTable
wwwDocAccessTopNTable = _WwwDocAccessTopNTable_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 3, 4)
)
if mibBuilder.loadTexts:
    wwwDocAccessTopNTable.setStatus("current")
_WwwDocAccessTopNEntry_Object = MibTableRow
wwwDocAccessTopNEntry = _WwwDocAccessTopNEntry_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 3, 4, 1)
)
wwwDocAccessTopNEntry.setIndexNames(
    (0, "WWW-MIB", "wwwServiceIndex"),
    (0, "WWW-MIB", "wwwDocBucketIndex"),
    (0, "WWW-MIB", "wwwDocAccessTopNIndex"),
)
if mibBuilder.loadTexts:
    wwwDocAccessTopNEntry.setStatus("current")


class _WwwDocAccessTopNIndex_Type(Unsigned32):
    """Custom type wwwDocAccessTopNIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_WwwDocAccessTopNIndex_Type.__name__ = "Unsigned32"
_WwwDocAccessTopNIndex_Object = MibTableColumn
wwwDocAccessTopNIndex = _WwwDocAccessTopNIndex_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 3, 4, 1, 1),
    _WwwDocAccessTopNIndex_Type()
)
wwwDocAccessTopNIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwwDocAccessTopNIndex.setStatus("current")
_WwwDocAccessTopNName_Type = WwwDocName
_WwwDocAccessTopNName_Object = MibTableColumn
wwwDocAccessTopNName = _WwwDocAccessTopNName_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 3, 4, 1, 2),
    _WwwDocAccessTopNName_Type()
)
wwwDocAccessTopNName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwDocAccessTopNName.setStatus("current")
_WwwDocAccessTopNAccesses_Type = Unsigned32
_WwwDocAccessTopNAccesses_Object = MibTableColumn
wwwDocAccessTopNAccesses = _WwwDocAccessTopNAccesses_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 3, 4, 1, 3),
    _WwwDocAccessTopNAccesses_Type()
)
wwwDocAccessTopNAccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwDocAccessTopNAccesses.setStatus("current")
_WwwDocAccessTopNBytes_Type = Unsigned32
_WwwDocAccessTopNBytes_Object = MibTableColumn
wwwDocAccessTopNBytes = _WwwDocAccessTopNBytes_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 3, 4, 1, 4),
    _WwwDocAccessTopNBytes_Type()
)
wwwDocAccessTopNBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwDocAccessTopNBytes.setStatus("current")
_WwwDocAccessTopNLastResponseType_Type = WwwResponseType
_WwwDocAccessTopNLastResponseType_Object = MibTableColumn
wwwDocAccessTopNLastResponseType = _WwwDocAccessTopNLastResponseType_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 3, 4, 1, 5),
    _WwwDocAccessTopNLastResponseType_Type()
)
wwwDocAccessTopNLastResponseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwDocAccessTopNLastResponseType.setStatus("current")
_WwwDocBytesTopNTable_Object = MibTable
wwwDocBytesTopNTable = _WwwDocBytesTopNTable_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 3, 5)
)
if mibBuilder.loadTexts:
    wwwDocBytesTopNTable.setStatus("current")
_WwwDocBytesTopNEntry_Object = MibTableRow
wwwDocBytesTopNEntry = _WwwDocBytesTopNEntry_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 3, 5, 1)
)
wwwDocBytesTopNEntry.setIndexNames(
    (0, "WWW-MIB", "wwwServiceIndex"),
    (0, "WWW-MIB", "wwwDocBucketIndex"),
    (0, "WWW-MIB", "wwwDocBytesTopNIndex"),
)
if mibBuilder.loadTexts:
    wwwDocBytesTopNEntry.setStatus("current")


class _WwwDocBytesTopNIndex_Type(Unsigned32):
    """Custom type wwwDocBytesTopNIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_WwwDocBytesTopNIndex_Type.__name__ = "Unsigned32"
_WwwDocBytesTopNIndex_Object = MibTableColumn
wwwDocBytesTopNIndex = _WwwDocBytesTopNIndex_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 3, 5, 1, 1),
    _WwwDocBytesTopNIndex_Type()
)
wwwDocBytesTopNIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwwDocBytesTopNIndex.setStatus("current")
_WwwDocBytesTopNName_Type = WwwDocName
_WwwDocBytesTopNName_Object = MibTableColumn
wwwDocBytesTopNName = _WwwDocBytesTopNName_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 3, 5, 1, 2),
    _WwwDocBytesTopNName_Type()
)
wwwDocBytesTopNName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwDocBytesTopNName.setStatus("current")
_WwwDocBytesTopNAccesses_Type = Unsigned32
_WwwDocBytesTopNAccesses_Object = MibTableColumn
wwwDocBytesTopNAccesses = _WwwDocBytesTopNAccesses_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 3, 5, 1, 3),
    _WwwDocBytesTopNAccesses_Type()
)
wwwDocBytesTopNAccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwDocBytesTopNAccesses.setStatus("current")
_WwwDocBytesTopNBytes_Type = Unsigned32
_WwwDocBytesTopNBytes_Object = MibTableColumn
wwwDocBytesTopNBytes = _WwwDocBytesTopNBytes_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 3, 5, 1, 4),
    _WwwDocBytesTopNBytes_Type()
)
wwwDocBytesTopNBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwDocBytesTopNBytes.setStatus("current")
_WwwDocBytesTopNLastResponseType_Type = WwwResponseType
_WwwDocBytesTopNLastResponseType_Object = MibTableColumn
wwwDocBytesTopNLastResponseType = _WwwDocBytesTopNLastResponseType_Object(
    (1, 3, 6, 1, 2, 1, 65, 1, 3, 5, 1, 5),
    _WwwDocBytesTopNLastResponseType_Type()
)
wwwDocBytesTopNLastResponseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwwDocBytesTopNLastResponseType.setStatus("current")
_WwwMIBConformance_ObjectIdentity = ObjectIdentity
wwwMIBConformance = _WwwMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 65, 2)
)
_WwwMIBCompliances_ObjectIdentity = ObjectIdentity
wwwMIBCompliances = _WwwMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 65, 2, 1)
)
_WwwMIBGroups_ObjectIdentity = ObjectIdentity
wwwMIBGroups = _WwwMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 65, 2, 2)
)

# Managed Objects groups

wwwServiceGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 65, 2, 2, 1)
)
wwwServiceGroup.setObjects(
      *(("WWW-MIB", "wwwServiceDescription"),
        ("WWW-MIB", "wwwServiceContact"),
        ("WWW-MIB", "wwwServiceProtocol"),
        ("WWW-MIB", "wwwServiceName"),
        ("WWW-MIB", "wwwServiceType"),
        ("WWW-MIB", "wwwServiceStartTime"),
        ("WWW-MIB", "wwwServiceOperStatus"),
        ("WWW-MIB", "wwwServiceLastChange"))
)
if mibBuilder.loadTexts:
    wwwServiceGroup.setStatus("current")

wwwSummaryGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 65, 2, 2, 2)
)
wwwSummaryGroup.setObjects(
      *(("WWW-MIB", "wwwSummaryInRequests"),
        ("WWW-MIB", "wwwSummaryOutRequests"),
        ("WWW-MIB", "wwwSummaryInResponses"),
        ("WWW-MIB", "wwwSummaryOutResponses"),
        ("WWW-MIB", "wwwSummaryInBytes"),
        ("WWW-MIB", "wwwSummaryInLowBytes"),
        ("WWW-MIB", "wwwSummaryOutBytes"),
        ("WWW-MIB", "wwwSummaryOutLowBytes"))
)
if mibBuilder.loadTexts:
    wwwSummaryGroup.setStatus("current")

wwwRequestInGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 65, 2, 2, 3)
)
wwwRequestInGroup.setObjects(
      *(("WWW-MIB", "wwwRequestInRequests"),
        ("WWW-MIB", "wwwRequestInBytes"),
        ("WWW-MIB", "wwwRequestInLastTime"))
)
if mibBuilder.loadTexts:
    wwwRequestInGroup.setStatus("current")

wwwRequestOutGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 65, 2, 2, 4)
)
wwwRequestOutGroup.setObjects(
      *(("WWW-MIB", "wwwRequestOutRequests"),
        ("WWW-MIB", "wwwRequestOutBytes"),
        ("WWW-MIB", "wwwRequestOutLastTime"))
)
if mibBuilder.loadTexts:
    wwwRequestOutGroup.setStatus("current")

wwwResponseInGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 65, 2, 2, 5)
)
wwwResponseInGroup.setObjects(
      *(("WWW-MIB", "wwwResponseInResponses"),
        ("WWW-MIB", "wwwResponseInBytes"),
        ("WWW-MIB", "wwwResponseInLastTime"))
)
if mibBuilder.loadTexts:
    wwwResponseInGroup.setStatus("current")

wwwResponseOutGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 65, 2, 2, 6)
)
wwwResponseOutGroup.setObjects(
      *(("WWW-MIB", "wwwResponseOutResponses"),
        ("WWW-MIB", "wwwResponseOutBytes"),
        ("WWW-MIB", "wwwResponseOutLastTime"))
)
if mibBuilder.loadTexts:
    wwwResponseOutGroup.setStatus("current")

wwwDocumentGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 65, 2, 2, 7)
)
wwwDocumentGroup.setObjects(
      *(("WWW-MIB", "wwwDocCtrlLastNSize"),
        ("WWW-MIB", "wwwDocCtrlLastNLock"),
        ("WWW-MIB", "wwwDocCtrlBuckets"),
        ("WWW-MIB", "wwwDocCtrlBucketTimeInterval"),
        ("WWW-MIB", "wwwDocCtrlTopNSize"),
        ("WWW-MIB", "wwwDocLastNName"),
        ("WWW-MIB", "wwwDocLastNTimeStamp"),
        ("WWW-MIB", "wwwDocLastNRequestType"),
        ("WWW-MIB", "wwwDocLastNResponseType"),
        ("WWW-MIB", "wwwDocLastNStatusMsg"),
        ("WWW-MIB", "wwwDocLastNBytes"),
        ("WWW-MIB", "wwwDocBucketTimeStamp"),
        ("WWW-MIB", "wwwDocBucketAccesses"),
        ("WWW-MIB", "wwwDocBucketDocuments"),
        ("WWW-MIB", "wwwDocBucketBytes"),
        ("WWW-MIB", "wwwDocAccessTopNName"),
        ("WWW-MIB", "wwwDocAccessTopNAccesses"),
        ("WWW-MIB", "wwwDocAccessTopNBytes"),
        ("WWW-MIB", "wwwDocAccessTopNLastResponseType"),
        ("WWW-MIB", "wwwDocBytesTopNName"),
        ("WWW-MIB", "wwwDocBytesTopNAccesses"),
        ("WWW-MIB", "wwwDocBytesTopNBytes"),
        ("WWW-MIB", "wwwDocBytesTopNLastResponseType"))
)
if mibBuilder.loadTexts:
    wwwDocumentGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

wwwMinimalCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 65, 2, 1, 1)
)
if mibBuilder.loadTexts:
    wwwMinimalCompliance.setStatus(
        "current"
    )

wwwFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 65, 2, 1, 2)
)
if mibBuilder.loadTexts:
    wwwFullCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWW-MIB",
    **{"WwwRequestType": WwwRequestType,
       "WwwResponseType": WwwResponseType,
       "WwwOperStatus": WwwOperStatus,
       "WwwDocName": WwwDocName,
       "wwwMIB": wwwMIB,
       "wwwMIBObjects": wwwMIBObjects,
       "wwwService": wwwService,
       "wwwServiceTable": wwwServiceTable,
       "wwwServiceEntry": wwwServiceEntry,
       "wwwServiceIndex": wwwServiceIndex,
       "wwwServiceDescription": wwwServiceDescription,
       "wwwServiceContact": wwwServiceContact,
       "wwwServiceProtocol": wwwServiceProtocol,
       "wwwServiceName": wwwServiceName,
       "wwwServiceType": wwwServiceType,
       "wwwServiceStartTime": wwwServiceStartTime,
       "wwwServiceOperStatus": wwwServiceOperStatus,
       "wwwServiceLastChange": wwwServiceLastChange,
       "wwwProtocolStatistics": wwwProtocolStatistics,
       "wwwSummaryTable": wwwSummaryTable,
       "wwwSummaryEntry": wwwSummaryEntry,
       "wwwSummaryInRequests": wwwSummaryInRequests,
       "wwwSummaryOutRequests": wwwSummaryOutRequests,
       "wwwSummaryInResponses": wwwSummaryInResponses,
       "wwwSummaryOutResponses": wwwSummaryOutResponses,
       "wwwSummaryInBytes": wwwSummaryInBytes,
       "wwwSummaryInLowBytes": wwwSummaryInLowBytes,
       "wwwSummaryOutBytes": wwwSummaryOutBytes,
       "wwwSummaryOutLowBytes": wwwSummaryOutLowBytes,
       "wwwRequestInTable": wwwRequestInTable,
       "wwwRequestInEntry": wwwRequestInEntry,
       "wwwRequestInIndex": wwwRequestInIndex,
       "wwwRequestInRequests": wwwRequestInRequests,
       "wwwRequestInBytes": wwwRequestInBytes,
       "wwwRequestInLastTime": wwwRequestInLastTime,
       "wwwRequestOutTable": wwwRequestOutTable,
       "wwwRequestOutEntry": wwwRequestOutEntry,
       "wwwRequestOutIndex": wwwRequestOutIndex,
       "wwwRequestOutRequests": wwwRequestOutRequests,
       "wwwRequestOutBytes": wwwRequestOutBytes,
       "wwwRequestOutLastTime": wwwRequestOutLastTime,
       "wwwResponseInTable": wwwResponseInTable,
       "wwwResponseInEntry": wwwResponseInEntry,
       "wwwResponseInIndex": wwwResponseInIndex,
       "wwwResponseInResponses": wwwResponseInResponses,
       "wwwResponseInBytes": wwwResponseInBytes,
       "wwwResponseInLastTime": wwwResponseInLastTime,
       "wwwResponseOutTable": wwwResponseOutTable,
       "wwwResponseOutEntry": wwwResponseOutEntry,
       "wwwResponseOutIndex": wwwResponseOutIndex,
       "wwwResponseOutResponses": wwwResponseOutResponses,
       "wwwResponseOutBytes": wwwResponseOutBytes,
       "wwwResponseOutLastTime": wwwResponseOutLastTime,
       "wwwDocumentStatistics": wwwDocumentStatistics,
       "wwwDocCtrlTable": wwwDocCtrlTable,
       "wwwDocCtrlEntry": wwwDocCtrlEntry,
       "wwwDocCtrlLastNSize": wwwDocCtrlLastNSize,
       "wwwDocCtrlLastNLock": wwwDocCtrlLastNLock,
       "wwwDocCtrlBuckets": wwwDocCtrlBuckets,
       "wwwDocCtrlBucketTimeInterval": wwwDocCtrlBucketTimeInterval,
       "wwwDocCtrlTopNSize": wwwDocCtrlTopNSize,
       "wwwDocLastNTable": wwwDocLastNTable,
       "wwwDocLastNEntry": wwwDocLastNEntry,
       "wwwDocLastNIndex": wwwDocLastNIndex,
       "wwwDocLastNName": wwwDocLastNName,
       "wwwDocLastNTimeStamp": wwwDocLastNTimeStamp,
       "wwwDocLastNRequestType": wwwDocLastNRequestType,
       "wwwDocLastNResponseType": wwwDocLastNResponseType,
       "wwwDocLastNStatusMsg": wwwDocLastNStatusMsg,
       "wwwDocLastNBytes": wwwDocLastNBytes,
       "wwwDocBucketTable": wwwDocBucketTable,
       "wwwDocBucketEntry": wwwDocBucketEntry,
       "wwwDocBucketIndex": wwwDocBucketIndex,
       "wwwDocBucketTimeStamp": wwwDocBucketTimeStamp,
       "wwwDocBucketAccesses": wwwDocBucketAccesses,
       "wwwDocBucketDocuments": wwwDocBucketDocuments,
       "wwwDocBucketBytes": wwwDocBucketBytes,
       "wwwDocAccessTopNTable": wwwDocAccessTopNTable,
       "wwwDocAccessTopNEntry": wwwDocAccessTopNEntry,
       "wwwDocAccessTopNIndex": wwwDocAccessTopNIndex,
       "wwwDocAccessTopNName": wwwDocAccessTopNName,
       "wwwDocAccessTopNAccesses": wwwDocAccessTopNAccesses,
       "wwwDocAccessTopNBytes": wwwDocAccessTopNBytes,
       "wwwDocAccessTopNLastResponseType": wwwDocAccessTopNLastResponseType,
       "wwwDocBytesTopNTable": wwwDocBytesTopNTable,
       "wwwDocBytesTopNEntry": wwwDocBytesTopNEntry,
       "wwwDocBytesTopNIndex": wwwDocBytesTopNIndex,
       "wwwDocBytesTopNName": wwwDocBytesTopNName,
       "wwwDocBytesTopNAccesses": wwwDocBytesTopNAccesses,
       "wwwDocBytesTopNBytes": wwwDocBytesTopNBytes,
       "wwwDocBytesTopNLastResponseType": wwwDocBytesTopNLastResponseType,
       "wwwMIBConformance": wwwMIBConformance,
       "wwwMIBCompliances": wwwMIBCompliances,
       "wwwMinimalCompliance": wwwMinimalCompliance,
       "wwwFullCompliance": wwwFullCompliance,
       "wwwMIBGroups": wwwMIBGroups,
       "wwwServiceGroup": wwwServiceGroup,
       "wwwSummaryGroup": wwwSummaryGroup,
       "wwwRequestInGroup": wwwRequestInGroup,
       "wwwRequestOutGroup": wwwRequestOutGroup,
       "wwwResponseInGroup": wwwResponseInGroup,
       "wwwResponseOutGroup": wwwResponseOutGroup,
       "wwwDocumentGroup": wwwDocumentGroup}
)
