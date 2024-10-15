# SNMP MIB module (CISCO-FIREWALL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-FIREWALL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:00:34 2024
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

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

(DateAndTime,
 DisplayString,
 RowPointer,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowPointer",
    "TextualConvention")


# MODULE-IDENTITY

ciscoFirewallMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 147)
)
ciscoFirewallMIB.setRevisions(
        ("2005-12-06 00:00",
         "1999-04-29 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ResourceStatistics(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("average", 7),
          ("free", 8),
          ("high", 6),
          ("highLoad", 2),
          ("highUse", 1),
          ("inUse", 9),
          ("low", 5),
          ("maximum", 3),
          ("minimum", 4))
    )



class Hardware(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("cpu", 5),
          ("disk", 2),
          ("memory", 1),
          ("netInterface", 4),
          ("other", 8),
          ("power", 3),
          ("primaryUnit", 6),
          ("secondaryUnit", 7))
    )



class Services(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41)
        )
    )
    namedValues = NamedValues(
        *(("contInspProgLang", 23),
          ("contInspUrl", 24),
          ("dbMSsql", 22),
          ("dbOracle", 21),
          ("directoryDns", 26),
          ("directoryNetbiosdgm", 28),
          ("directoryNetbiosns", 27),
          ("directoryNetbiosssn", 29),
          ("directoryNis", 25),
          ("directoryWins", 30),
          ("fileXferFtp", 2),
          ("fileXferFtps", 4),
          ("fileXferTftp", 3),
          ("fsCifs", 36),
          ("fsNfs", 35),
          ("fsNfsStatus", 34),
          ("loginRlogin", 6),
          ("loginTelnet", 5),
          ("loginTelnets", 7),
          ("mailSmtp", 14),
          ("multimediaH323", 16),
          ("multimediaNetShow", 17),
          ("multimediaRTSP", 20),
          ("multimediaRealAV", 19),
          ("multimediaStreamworks", 15),
          ("multimediaVDOLive", 18),
          ("otherFWService", 1),
          ("protoIcmp", 37),
          ("protoIp", 40),
          ("protoSnmp", 41),
          ("protoTcp", 38),
          ("protoUdp", 39),
          ("qryFinger", 32),
          ("qryIdent", 33),
          ("qryWhois", 31),
          ("remoteExecMSRPC", 9),
          ("remoteExecRsh", 10),
          ("remoteExecSunRPC", 8),
          ("remoteExecXserver", 11),
          ("webHttp", 12),
          ("webHttps", 13))
    )



class HardwareStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("active", 9),
          ("backup", 8),
          ("busy", 6),
          ("down", 3),
          ("error", 4),
          ("noMedia", 7),
          ("other", 1),
          ("overTemp", 5),
          ("standby", 10),
          ("up", 2))
    )



class SecurityEvent(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("addrSpoof", 6),
          ("complete", 9),
          ("dos", 3),
          ("illegCom", 11),
          ("invalPak", 10),
          ("none", 2),
          ("other", 1),
          ("pakFwd", 5),
          ("policy", 12),
          ("recon", 4),
          ("svcSpoof", 7),
          ("thirdParty", 8))
    )



class ContentInspectionEvent(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("clean", 5),
          ("error", 3),
          ("found", 4),
          ("okay", 2),
          ("other", 1),
          ("reject", 6),
          ("saved", 7))
    )



class ConnectionEvent(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("accept", 2),
          ("close", 5),
          ("drop", 4),
          ("error", 3),
          ("noResp", 9),
          ("other", 1),
          ("refused", 7),
          ("reset", 8),
          ("timeout", 6))
    )



class ConnectionStat(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("currentClosing", 4),
          ("currentHalfOpen", 5),
          ("currentInUse", 6),
          ("currentOpen", 3),
          ("high", 7),
          ("other", 1),
          ("totalOpen", 2))
    )



class AccessEvent(Integer32, TextualConvention):
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
        *(("deny", 3),
          ("denyMult", 4),
          ("error", 5),
          ("grant", 2),
          ("other", 1))
    )



class AuthenticationEvent(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("error", 3),
          ("fail", 4),
          ("failMult", 7),
          ("failPriv", 6),
          ("other", 1),
          ("succ", 2),
          ("succPriv", 5))
    )



class GenericEvent(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("abnormal", 1),
          ("error", 3),
          ("okay", 2))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoFirewallMIBObjects_ObjectIdentity = ObjectIdentity
ciscoFirewallMIBObjects = _CiscoFirewallMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 147, 1)
)
_CfwEvents_ObjectIdentity = ObjectIdentity
cfwEvents = _CfwEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1)
)
_CfwBasicEvents_ObjectIdentity = ObjectIdentity
cfwBasicEvents = _CfwBasicEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 1)
)
_CfwBasicEventsTableLastRow_Type = Unsigned32
_CfwBasicEventsTableLastRow_Object = MibScalar
cfwBasicEventsTableLastRow = _CfwBasicEventsTableLastRow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 1, 1),
    _CfwBasicEventsTableLastRow_Type()
)
cfwBasicEventsTableLastRow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfwBasicEventsTableLastRow.setStatus("current")
_CfwBasicEventsTable_Object = MibTable
cfwBasicEventsTable = _CfwBasicEventsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cfwBasicEventsTable.setStatus("current")
_CfwBasicEventsEntry_Object = MibTableRow
cfwBasicEventsEntry = _CfwBasicEventsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 1, 2, 1)
)
cfwBasicEventsEntry.setIndexNames(
    (0, "CISCO-FIREWALL-MIB", "cfwBasicEventIndex"),
)
if mibBuilder.loadTexts:
    cfwBasicEventsEntry.setStatus("current")
_CfwBasicEventIndex_Type = Unsigned32
_CfwBasicEventIndex_Object = MibTableColumn
cfwBasicEventIndex = _CfwBasicEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 1, 2, 1, 1),
    _CfwBasicEventIndex_Type()
)
cfwBasicEventIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfwBasicEventIndex.setStatus("current")
_CfwBasicEventTime_Type = DateAndTime
_CfwBasicEventTime_Object = MibTableColumn
cfwBasicEventTime = _CfwBasicEventTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 1, 2, 1, 2),
    _CfwBasicEventTime_Type()
)
cfwBasicEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfwBasicEventTime.setStatus("current")
_CfwBasicSecurityEventType_Type = SecurityEvent
_CfwBasicSecurityEventType_Object = MibTableColumn
cfwBasicSecurityEventType = _CfwBasicSecurityEventType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 1, 2, 1, 3),
    _CfwBasicSecurityEventType_Type()
)
cfwBasicSecurityEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfwBasicSecurityEventType.setStatus("current")
_CfwBasicContentInspEventType_Type = ContentInspectionEvent
_CfwBasicContentInspEventType_Object = MibTableColumn
cfwBasicContentInspEventType = _CfwBasicContentInspEventType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 1, 2, 1, 4),
    _CfwBasicContentInspEventType_Type()
)
cfwBasicContentInspEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfwBasicContentInspEventType.setStatus("current")
_CfwBasicConnectionEventType_Type = ConnectionEvent
_CfwBasicConnectionEventType_Object = MibTableColumn
cfwBasicConnectionEventType = _CfwBasicConnectionEventType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 1, 2, 1, 5),
    _CfwBasicConnectionEventType_Type()
)
cfwBasicConnectionEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfwBasicConnectionEventType.setStatus("current")
_CfwBasicAccessEventType_Type = AccessEvent
_CfwBasicAccessEventType_Object = MibTableColumn
cfwBasicAccessEventType = _CfwBasicAccessEventType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 1, 2, 1, 6),
    _CfwBasicAccessEventType_Type()
)
cfwBasicAccessEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfwBasicAccessEventType.setStatus("current")
_CfwBasicAuthenticationEventType_Type = AuthenticationEvent
_CfwBasicAuthenticationEventType_Object = MibTableColumn
cfwBasicAuthenticationEventType = _CfwBasicAuthenticationEventType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 1, 2, 1, 7),
    _CfwBasicAuthenticationEventType_Type()
)
cfwBasicAuthenticationEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfwBasicAuthenticationEventType.setStatus("current")
_CfwBasicGenericEventType_Type = GenericEvent
_CfwBasicGenericEventType_Object = MibTableColumn
cfwBasicGenericEventType = _CfwBasicGenericEventType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 1, 2, 1, 8),
    _CfwBasicGenericEventType_Type()
)
cfwBasicGenericEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfwBasicGenericEventType.setStatus("current")
_CfwBasicEventDescription_Type = SnmpAdminString
_CfwBasicEventDescription_Object = MibTableColumn
cfwBasicEventDescription = _CfwBasicEventDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 1, 2, 1, 9),
    _CfwBasicEventDescription_Type()
)
cfwBasicEventDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfwBasicEventDescription.setStatus("current")
_CfwBasicEventDetailsTableRow_Type = RowPointer
_CfwBasicEventDetailsTableRow_Object = MibTableColumn
cfwBasicEventDetailsTableRow = _CfwBasicEventDetailsTableRow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 1, 2, 1, 10),
    _CfwBasicEventDetailsTableRow_Type()
)
cfwBasicEventDetailsTableRow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfwBasicEventDetailsTableRow.setStatus("current")
_CfwNetEvents_ObjectIdentity = ObjectIdentity
cfwNetEvents = _CfwNetEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 2)
)
_CfwNetEventsTableLastRow_Type = Unsigned32
_CfwNetEventsTableLastRow_Object = MibScalar
cfwNetEventsTableLastRow = _CfwNetEventsTableLastRow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 2, 1),
    _CfwNetEventsTableLastRow_Type()
)
cfwNetEventsTableLastRow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfwNetEventsTableLastRow.setStatus("current")
_CfwNetEventsTable_Object = MibTable
cfwNetEventsTable = _CfwNetEventsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cfwNetEventsTable.setStatus("current")
_CfwNetEventsEntry_Object = MibTableRow
cfwNetEventsEntry = _CfwNetEventsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 2, 2, 1)
)
cfwNetEventsEntry.setIndexNames(
    (0, "CISCO-FIREWALL-MIB", "cfwNetEventIndex"),
)
if mibBuilder.loadTexts:
    cfwNetEventsEntry.setStatus("current")
_CfwNetEventIndex_Type = Unsigned32
_CfwNetEventIndex_Object = MibTableColumn
cfwNetEventIndex = _CfwNetEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 2, 2, 1, 1),
    _CfwNetEventIndex_Type()
)
cfwNetEventIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfwNetEventIndex.setStatus("current")
_CfwNetEventInterface_Type = InterfaceIndexOrZero
_CfwNetEventInterface_Object = MibTableColumn
cfwNetEventInterface = _CfwNetEventInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 2, 2, 1, 2),
    _CfwNetEventInterface_Type()
)
cfwNetEventInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfwNetEventInterface.setStatus("current")
_CfwNetEventSrcIpAddress_Type = IpAddress
_CfwNetEventSrcIpAddress_Object = MibTableColumn
cfwNetEventSrcIpAddress = _CfwNetEventSrcIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 2, 2, 1, 3),
    _CfwNetEventSrcIpAddress_Type()
)
cfwNetEventSrcIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfwNetEventSrcIpAddress.setStatus("current")
_CfwNetEventInsideSrcIpAddress_Type = IpAddress
_CfwNetEventInsideSrcIpAddress_Object = MibTableColumn
cfwNetEventInsideSrcIpAddress = _CfwNetEventInsideSrcIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 2, 2, 1, 4),
    _CfwNetEventInsideSrcIpAddress_Type()
)
cfwNetEventInsideSrcIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfwNetEventInsideSrcIpAddress.setStatus("current")
_CfwNetEventDstIpAddress_Type = IpAddress
_CfwNetEventDstIpAddress_Object = MibTableColumn
cfwNetEventDstIpAddress = _CfwNetEventDstIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 2, 2, 1, 5),
    _CfwNetEventDstIpAddress_Type()
)
cfwNetEventDstIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfwNetEventDstIpAddress.setStatus("current")
_CfwNetEventInsideDstIpAddress_Type = IpAddress
_CfwNetEventInsideDstIpAddress_Object = MibTableColumn
cfwNetEventInsideDstIpAddress = _CfwNetEventInsideDstIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 2, 2, 1, 6),
    _CfwNetEventInsideDstIpAddress_Type()
)
cfwNetEventInsideDstIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfwNetEventInsideDstIpAddress.setStatus("current")


class _CfwNetEventSrcIpPort_Type(Integer32):
    """Custom type cfwNetEventSrcIpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CfwNetEventSrcIpPort_Type.__name__ = "Integer32"
_CfwNetEventSrcIpPort_Object = MibTableColumn
cfwNetEventSrcIpPort = _CfwNetEventSrcIpPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 2, 2, 1, 7),
    _CfwNetEventSrcIpPort_Type()
)
cfwNetEventSrcIpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfwNetEventSrcIpPort.setStatus("current")


class _CfwNetEventInsideSrcIpPort_Type(Integer32):
    """Custom type cfwNetEventInsideSrcIpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CfwNetEventInsideSrcIpPort_Type.__name__ = "Integer32"
_CfwNetEventInsideSrcIpPort_Object = MibTableColumn
cfwNetEventInsideSrcIpPort = _CfwNetEventInsideSrcIpPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 2, 2, 1, 8),
    _CfwNetEventInsideSrcIpPort_Type()
)
cfwNetEventInsideSrcIpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfwNetEventInsideSrcIpPort.setStatus("current")


class _CfwNetEventDstIpPort_Type(Integer32):
    """Custom type cfwNetEventDstIpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CfwNetEventDstIpPort_Type.__name__ = "Integer32"
_CfwNetEventDstIpPort_Object = MibTableColumn
cfwNetEventDstIpPort = _CfwNetEventDstIpPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 2, 2, 1, 9),
    _CfwNetEventDstIpPort_Type()
)
cfwNetEventDstIpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfwNetEventDstIpPort.setStatus("current")


class _CfwNetEventInsideDstIpPort_Type(Integer32):
    """Custom type cfwNetEventInsideDstIpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CfwNetEventInsideDstIpPort_Type.__name__ = "Integer32"
_CfwNetEventInsideDstIpPort_Object = MibTableColumn
cfwNetEventInsideDstIpPort = _CfwNetEventInsideDstIpPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 2, 2, 1, 10),
    _CfwNetEventInsideDstIpPort_Type()
)
cfwNetEventInsideDstIpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfwNetEventInsideDstIpPort.setStatus("current")
_CfwNetEventService_Type = Services
_CfwNetEventService_Object = MibTableColumn
cfwNetEventService = _CfwNetEventService_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 2, 2, 1, 11),
    _CfwNetEventService_Type()
)
cfwNetEventService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfwNetEventService.setStatus("current")
_CfwNetEventServiceInformation_Type = SnmpAdminString
_CfwNetEventServiceInformation_Object = MibTableColumn
cfwNetEventServiceInformation = _CfwNetEventServiceInformation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 2, 2, 1, 12),
    _CfwNetEventServiceInformation_Type()
)
cfwNetEventServiceInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfwNetEventServiceInformation.setStatus("current")
_CfwNetEventIdentity_Type = SnmpAdminString
_CfwNetEventIdentity_Object = MibTableColumn
cfwNetEventIdentity = _CfwNetEventIdentity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 2, 2, 1, 13),
    _CfwNetEventIdentity_Type()
)
cfwNetEventIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfwNetEventIdentity.setStatus("current")
_CfwNetEventDescription_Type = SnmpAdminString
_CfwNetEventDescription_Object = MibTableColumn
cfwNetEventDescription = _CfwNetEventDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 1, 2, 2, 1, 14),
    _CfwNetEventDescription_Type()
)
cfwNetEventDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfwNetEventDescription.setStatus("current")
_CfwSystem_ObjectIdentity = ObjectIdentity
cfwSystem = _CfwSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 2)
)
_CfwStatus_ObjectIdentity = ObjectIdentity
cfwStatus = _CfwStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 2, 1)
)
_CfwHardwareStatusTable_Object = MibTable
cfwHardwareStatusTable = _CfwHardwareStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cfwHardwareStatusTable.setStatus("current")
_CfwHardwareStatusEntry_Object = MibTableRow
cfwHardwareStatusEntry = _CfwHardwareStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 2, 1, 1, 1)
)
cfwHardwareStatusEntry.setIndexNames(
    (0, "CISCO-FIREWALL-MIB", "cfwHardwareType"),
)
if mibBuilder.loadTexts:
    cfwHardwareStatusEntry.setStatus("current")
_CfwHardwareType_Type = Hardware
_CfwHardwareType_Object = MibTableColumn
cfwHardwareType = _CfwHardwareType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 2, 1, 1, 1, 1),
    _CfwHardwareType_Type()
)
cfwHardwareType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfwHardwareType.setStatus("current")
_CfwHardwareInformation_Type = SnmpAdminString
_CfwHardwareInformation_Object = MibTableColumn
cfwHardwareInformation = _CfwHardwareInformation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 2, 1, 1, 1, 2),
    _CfwHardwareInformation_Type()
)
cfwHardwareInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfwHardwareInformation.setStatus("current")
_CfwHardwareStatusValue_Type = HardwareStatus
_CfwHardwareStatusValue_Object = MibTableColumn
cfwHardwareStatusValue = _CfwHardwareStatusValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 2, 1, 1, 1, 3),
    _CfwHardwareStatusValue_Type()
)
cfwHardwareStatusValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfwHardwareStatusValue.setStatus("current")
_CfwHardwareStatusDetail_Type = SnmpAdminString
_CfwHardwareStatusDetail_Object = MibTableColumn
cfwHardwareStatusDetail = _CfwHardwareStatusDetail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 2, 1, 1, 1, 4),
    _CfwHardwareStatusDetail_Type()
)
cfwHardwareStatusDetail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfwHardwareStatusDetail.setStatus("current")
_CfwStatistics_ObjectIdentity = ObjectIdentity
cfwStatistics = _CfwStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 2, 2)
)
_CfwBufferStatsTable_Object = MibTable
cfwBufferStatsTable = _CfwBufferStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cfwBufferStatsTable.setStatus("current")
_CfwBufferStatsEntry_Object = MibTableRow
cfwBufferStatsEntry = _CfwBufferStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 2, 2, 1, 1)
)
cfwBufferStatsEntry.setIndexNames(
    (0, "CISCO-FIREWALL-MIB", "cfwBufferStatSize"),
    (0, "CISCO-FIREWALL-MIB", "cfwBufferStatType"),
)
if mibBuilder.loadTexts:
    cfwBufferStatsEntry.setStatus("current")
_CfwBufferStatSize_Type = Unsigned32
_CfwBufferStatSize_Object = MibTableColumn
cfwBufferStatSize = _CfwBufferStatSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 2, 2, 1, 1, 1),
    _CfwBufferStatSize_Type()
)
cfwBufferStatSize.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfwBufferStatSize.setStatus("current")
_CfwBufferStatType_Type = ResourceStatistics
_CfwBufferStatType_Object = MibTableColumn
cfwBufferStatType = _CfwBufferStatType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 2, 2, 1, 1, 2),
    _CfwBufferStatType_Type()
)
cfwBufferStatType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfwBufferStatType.setStatus("current")
_CfwBufferStatInformation_Type = SnmpAdminString
_CfwBufferStatInformation_Object = MibTableColumn
cfwBufferStatInformation = _CfwBufferStatInformation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 2, 2, 1, 1, 3),
    _CfwBufferStatInformation_Type()
)
cfwBufferStatInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfwBufferStatInformation.setStatus("current")
_CfwBufferStatValue_Type = Gauge32
_CfwBufferStatValue_Object = MibTableColumn
cfwBufferStatValue = _CfwBufferStatValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 2, 2, 1, 1, 4),
    _CfwBufferStatValue_Type()
)
cfwBufferStatValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfwBufferStatValue.setStatus("current")
_CfwConnectionStatTable_Object = MibTable
cfwConnectionStatTable = _CfwConnectionStatTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    cfwConnectionStatTable.setStatus("current")
_CfwConnectionStatEntry_Object = MibTableRow
cfwConnectionStatEntry = _CfwConnectionStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 2, 2, 2, 1)
)
cfwConnectionStatEntry.setIndexNames(
    (0, "CISCO-FIREWALL-MIB", "cfwConnectionStatService"),
    (0, "CISCO-FIREWALL-MIB", "cfwConnectionStatType"),
)
if mibBuilder.loadTexts:
    cfwConnectionStatEntry.setStatus("current")
_CfwConnectionStatService_Type = Services
_CfwConnectionStatService_Object = MibTableColumn
cfwConnectionStatService = _CfwConnectionStatService_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 2, 2, 2, 1, 1),
    _CfwConnectionStatService_Type()
)
cfwConnectionStatService.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfwConnectionStatService.setStatus("current")
_CfwConnectionStatType_Type = ConnectionStat
_CfwConnectionStatType_Object = MibTableColumn
cfwConnectionStatType = _CfwConnectionStatType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 2, 2, 2, 1, 2),
    _CfwConnectionStatType_Type()
)
cfwConnectionStatType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfwConnectionStatType.setStatus("current")
_CfwConnectionStatDescription_Type = SnmpAdminString
_CfwConnectionStatDescription_Object = MibTableColumn
cfwConnectionStatDescription = _CfwConnectionStatDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 2, 2, 2, 1, 3),
    _CfwConnectionStatDescription_Type()
)
cfwConnectionStatDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfwConnectionStatDescription.setStatus("current")
_CfwConnectionStatCount_Type = Counter32
_CfwConnectionStatCount_Object = MibTableColumn
cfwConnectionStatCount = _CfwConnectionStatCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 2, 2, 2, 1, 4),
    _CfwConnectionStatCount_Type()
)
cfwConnectionStatCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfwConnectionStatCount.setStatus("current")
_CfwConnectionStatValue_Type = Gauge32
_CfwConnectionStatValue_Object = MibTableColumn
cfwConnectionStatValue = _CfwConnectionStatValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 147, 1, 2, 2, 2, 1, 5),
    _CfwConnectionStatValue_Type()
)
cfwConnectionStatValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfwConnectionStatValue.setStatus("current")
_CiscoFirewallMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
ciscoFirewallMIBNotificationPrefix = _CiscoFirewallMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 147, 2)
)
_CiscoFirewallMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoFirewallMIBNotifications = _CiscoFirewallMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 147, 2, 0)
)
_CiscoFirewallMIBConformance_ObjectIdentity = ObjectIdentity
ciscoFirewallMIBConformance = _CiscoFirewallMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 147, 3)
)
_CiscoFirewallMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoFirewallMIBCompliances = _CiscoFirewallMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 147, 3, 1)
)
_CiscoFirewallMIBGroups_ObjectIdentity = ObjectIdentity
ciscoFirewallMIBGroups = _CiscoFirewallMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 147, 3, 2)
)

# Managed Objects groups

ciscoFirewallMIBEventsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 147, 3, 2, 1)
)
ciscoFirewallMIBEventsGroup.setObjects(
      *(("CISCO-FIREWALL-MIB", "cfwBasicEventsTableLastRow"),
        ("CISCO-FIREWALL-MIB", "cfwBasicEventTime"),
        ("CISCO-FIREWALL-MIB", "cfwBasicSecurityEventType"),
        ("CISCO-FIREWALL-MIB", "cfwBasicContentInspEventType"),
        ("CISCO-FIREWALL-MIB", "cfwBasicConnectionEventType"),
        ("CISCO-FIREWALL-MIB", "cfwBasicAccessEventType"),
        ("CISCO-FIREWALL-MIB", "cfwBasicAuthenticationEventType"),
        ("CISCO-FIREWALL-MIB", "cfwBasicGenericEventType"),
        ("CISCO-FIREWALL-MIB", "cfwBasicEventDescription"),
        ("CISCO-FIREWALL-MIB", "cfwBasicEventDetailsTableRow"),
        ("CISCO-FIREWALL-MIB", "cfwNetEventsTableLastRow"),
        ("CISCO-FIREWALL-MIB", "cfwNetEventInterface"),
        ("CISCO-FIREWALL-MIB", "cfwNetEventSrcIpAddress"),
        ("CISCO-FIREWALL-MIB", "cfwNetEventInsideSrcIpAddress"),
        ("CISCO-FIREWALL-MIB", "cfwNetEventDstIpAddress"),
        ("CISCO-FIREWALL-MIB", "cfwNetEventInsideDstIpAddress"),
        ("CISCO-FIREWALL-MIB", "cfwNetEventSrcIpPort"),
        ("CISCO-FIREWALL-MIB", "cfwNetEventInsideSrcIpPort"),
        ("CISCO-FIREWALL-MIB", "cfwNetEventDstIpPort"),
        ("CISCO-FIREWALL-MIB", "cfwNetEventInsideDstIpPort"),
        ("CISCO-FIREWALL-MIB", "cfwNetEventService"),
        ("CISCO-FIREWALL-MIB", "cfwNetEventServiceInformation"),
        ("CISCO-FIREWALL-MIB", "cfwNetEventIdentity"),
        ("CISCO-FIREWALL-MIB", "cfwNetEventDescription"))
)
if mibBuilder.loadTexts:
    ciscoFirewallMIBEventsGroup.setStatus("current")

ciscoFirewallMIBStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 147, 3, 2, 2)
)
ciscoFirewallMIBStatisticsGroup.setObjects(
      *(("CISCO-FIREWALL-MIB", "cfwHardwareInformation"),
        ("CISCO-FIREWALL-MIB", "cfwHardwareStatusValue"),
        ("CISCO-FIREWALL-MIB", "cfwHardwareStatusDetail"),
        ("CISCO-FIREWALL-MIB", "cfwBufferStatInformation"),
        ("CISCO-FIREWALL-MIB", "cfwBufferStatValue"),
        ("CISCO-FIREWALL-MIB", "cfwConnectionStatDescription"),
        ("CISCO-FIREWALL-MIB", "cfwConnectionStatCount"),
        ("CISCO-FIREWALL-MIB", "cfwConnectionStatValue"))
)
if mibBuilder.loadTexts:
    ciscoFirewallMIBStatisticsGroup.setStatus("current")

ciscoFirewallMIBNotificationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 147, 3, 2, 3)
)
ciscoFirewallMIBNotificationGroup.setObjects(
      *(("CISCO-FIREWALL-MIB", "cfwBasicEventTime"),
        ("CISCO-FIREWALL-MIB", "cfwBasicSecurityEventType"),
        ("CISCO-FIREWALL-MIB", "cfwBasicContentInspEventType"),
        ("CISCO-FIREWALL-MIB", "cfwBasicConnectionEventType"),
        ("CISCO-FIREWALL-MIB", "cfwBasicAccessEventType"),
        ("CISCO-FIREWALL-MIB", "cfwBasicAuthenticationEventType"),
        ("CISCO-FIREWALL-MIB", "cfwBasicGenericEventType"),
        ("CISCO-FIREWALL-MIB", "cfwBasicEventDescription"),
        ("CISCO-FIREWALL-MIB", "cfwBasicEventDetailsTableRow"))
)
if mibBuilder.loadTexts:
    ciscoFirewallMIBNotificationGroup.setStatus("obsolete")


# Notification objects

cfwSecurityNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 147, 2, 0, 2)
)
cfwSecurityNotification.setObjects(
      *(("CISCO-FIREWALL-MIB", "cfwBasicEventTime"),
        ("CISCO-FIREWALL-MIB", "cfwBasicSecurityEventType"),
        ("CISCO-FIREWALL-MIB", "cfwBasicEventDescription"),
        ("CISCO-FIREWALL-MIB", "cfwBasicEventDetailsTableRow"))
)
if mibBuilder.loadTexts:
    cfwSecurityNotification.setStatus(
        "current"
    )

cfwContentInspectNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 147, 2, 0, 3)
)
cfwContentInspectNotification.setObjects(
      *(("CISCO-FIREWALL-MIB", "cfwBasicEventTime"),
        ("CISCO-FIREWALL-MIB", "cfwBasicContentInspEventType"),
        ("CISCO-FIREWALL-MIB", "cfwBasicEventDescription"),
        ("CISCO-FIREWALL-MIB", "cfwBasicEventDetailsTableRow"))
)
if mibBuilder.loadTexts:
    cfwContentInspectNotification.setStatus(
        "current"
    )

cfwConnNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 147, 2, 0, 4)
)
cfwConnNotification.setObjects(
      *(("CISCO-FIREWALL-MIB", "cfwBasicEventTime"),
        ("CISCO-FIREWALL-MIB", "cfwBasicConnectionEventType"),
        ("CISCO-FIREWALL-MIB", "cfwBasicEventDescription"),
        ("CISCO-FIREWALL-MIB", "cfwBasicEventDetailsTableRow"))
)
if mibBuilder.loadTexts:
    cfwConnNotification.setStatus(
        "current"
    )

cfwAccessNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 147, 2, 0, 5)
)
cfwAccessNotification.setObjects(
      *(("CISCO-FIREWALL-MIB", "cfwBasicEventTime"),
        ("CISCO-FIREWALL-MIB", "cfwBasicAccessEventType"),
        ("CISCO-FIREWALL-MIB", "cfwBasicEventDescription"),
        ("CISCO-FIREWALL-MIB", "cfwBasicEventDetailsTableRow"))
)
if mibBuilder.loadTexts:
    cfwAccessNotification.setStatus(
        "current"
    )

cfwAuthNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 147, 2, 0, 6)
)
cfwAuthNotification.setObjects(
      *(("CISCO-FIREWALL-MIB", "cfwBasicEventTime"),
        ("CISCO-FIREWALL-MIB", "cfwBasicAuthenticationEventType"),
        ("CISCO-FIREWALL-MIB", "cfwBasicEventDescription"),
        ("CISCO-FIREWALL-MIB", "cfwBasicEventDetailsTableRow"))
)
if mibBuilder.loadTexts:
    cfwAuthNotification.setStatus(
        "current"
    )

cfwGenericNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 147, 2, 0, 7)
)
cfwGenericNotification.setObjects(
      *(("CISCO-FIREWALL-MIB", "cfwBasicEventTime"),
        ("CISCO-FIREWALL-MIB", "cfwBasicGenericEventType"),
        ("CISCO-FIREWALL-MIB", "cfwBasicEventDescription"),
        ("CISCO-FIREWALL-MIB", "cfwBasicEventDetailsTableRow"))
)
if mibBuilder.loadTexts:
    cfwGenericNotification.setStatus(
        "current"
    )


# Notifications groups

ciscoFirewallMIBNotificationGroupRev1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 147, 3, 2, 4)
)
ciscoFirewallMIBNotificationGroupRev1.setObjects(
      *(("CISCO-FIREWALL-MIB", "cfwSecurityNotification"),
        ("CISCO-FIREWALL-MIB", "cfwContentInspectNotification"),
        ("CISCO-FIREWALL-MIB", "cfwConnNotification"),
        ("CISCO-FIREWALL-MIB", "cfwAccessNotification"),
        ("CISCO-FIREWALL-MIB", "cfwAuthNotification"),
        ("CISCO-FIREWALL-MIB", "cfwGenericNotification"))
)
if mibBuilder.loadTexts:
    ciscoFirewallMIBNotificationGroupRev1.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoFirewallMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 147, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoFirewallMIBCompliance.setStatus(
        "deprecated"
    )

ciscoFirewallMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 147, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoFirewallMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREWALL-MIB",
    **{"ResourceStatistics": ResourceStatistics,
       "Hardware": Hardware,
       "Services": Services,
       "HardwareStatus": HardwareStatus,
       "SecurityEvent": SecurityEvent,
       "ContentInspectionEvent": ContentInspectionEvent,
       "ConnectionEvent": ConnectionEvent,
       "ConnectionStat": ConnectionStat,
       "AccessEvent": AccessEvent,
       "AuthenticationEvent": AuthenticationEvent,
       "GenericEvent": GenericEvent,
       "ciscoFirewallMIB": ciscoFirewallMIB,
       "ciscoFirewallMIBObjects": ciscoFirewallMIBObjects,
       "cfwEvents": cfwEvents,
       "cfwBasicEvents": cfwBasicEvents,
       "cfwBasicEventsTableLastRow": cfwBasicEventsTableLastRow,
       "cfwBasicEventsTable": cfwBasicEventsTable,
       "cfwBasicEventsEntry": cfwBasicEventsEntry,
       "cfwBasicEventIndex": cfwBasicEventIndex,
       "cfwBasicEventTime": cfwBasicEventTime,
       "cfwBasicSecurityEventType": cfwBasicSecurityEventType,
       "cfwBasicContentInspEventType": cfwBasicContentInspEventType,
       "cfwBasicConnectionEventType": cfwBasicConnectionEventType,
       "cfwBasicAccessEventType": cfwBasicAccessEventType,
       "cfwBasicAuthenticationEventType": cfwBasicAuthenticationEventType,
       "cfwBasicGenericEventType": cfwBasicGenericEventType,
       "cfwBasicEventDescription": cfwBasicEventDescription,
       "cfwBasicEventDetailsTableRow": cfwBasicEventDetailsTableRow,
       "cfwNetEvents": cfwNetEvents,
       "cfwNetEventsTableLastRow": cfwNetEventsTableLastRow,
       "cfwNetEventsTable": cfwNetEventsTable,
       "cfwNetEventsEntry": cfwNetEventsEntry,
       "cfwNetEventIndex": cfwNetEventIndex,
       "cfwNetEventInterface": cfwNetEventInterface,
       "cfwNetEventSrcIpAddress": cfwNetEventSrcIpAddress,
       "cfwNetEventInsideSrcIpAddress": cfwNetEventInsideSrcIpAddress,
       "cfwNetEventDstIpAddress": cfwNetEventDstIpAddress,
       "cfwNetEventInsideDstIpAddress": cfwNetEventInsideDstIpAddress,
       "cfwNetEventSrcIpPort": cfwNetEventSrcIpPort,
       "cfwNetEventInsideSrcIpPort": cfwNetEventInsideSrcIpPort,
       "cfwNetEventDstIpPort": cfwNetEventDstIpPort,
       "cfwNetEventInsideDstIpPort": cfwNetEventInsideDstIpPort,
       "cfwNetEventService": cfwNetEventService,
       "cfwNetEventServiceInformation": cfwNetEventServiceInformation,
       "cfwNetEventIdentity": cfwNetEventIdentity,
       "cfwNetEventDescription": cfwNetEventDescription,
       "cfwSystem": cfwSystem,
       "cfwStatus": cfwStatus,
       "cfwHardwareStatusTable": cfwHardwareStatusTable,
       "cfwHardwareStatusEntry": cfwHardwareStatusEntry,
       "cfwHardwareType": cfwHardwareType,
       "cfwHardwareInformation": cfwHardwareInformation,
       "cfwHardwareStatusValue": cfwHardwareStatusValue,
       "cfwHardwareStatusDetail": cfwHardwareStatusDetail,
       "cfwStatistics": cfwStatistics,
       "cfwBufferStatsTable": cfwBufferStatsTable,
       "cfwBufferStatsEntry": cfwBufferStatsEntry,
       "cfwBufferStatSize": cfwBufferStatSize,
       "cfwBufferStatType": cfwBufferStatType,
       "cfwBufferStatInformation": cfwBufferStatInformation,
       "cfwBufferStatValue": cfwBufferStatValue,
       "cfwConnectionStatTable": cfwConnectionStatTable,
       "cfwConnectionStatEntry": cfwConnectionStatEntry,
       "cfwConnectionStatService": cfwConnectionStatService,
       "cfwConnectionStatType": cfwConnectionStatType,
       "cfwConnectionStatDescription": cfwConnectionStatDescription,
       "cfwConnectionStatCount": cfwConnectionStatCount,
       "cfwConnectionStatValue": cfwConnectionStatValue,
       "ciscoFirewallMIBNotificationPrefix": ciscoFirewallMIBNotificationPrefix,
       "ciscoFirewallMIBNotifications": ciscoFirewallMIBNotifications,
       "cfwSecurityNotification": cfwSecurityNotification,
       "cfwContentInspectNotification": cfwContentInspectNotification,
       "cfwConnNotification": cfwConnNotification,
       "cfwAccessNotification": cfwAccessNotification,
       "cfwAuthNotification": cfwAuthNotification,
       "cfwGenericNotification": cfwGenericNotification,
       "ciscoFirewallMIBConformance": ciscoFirewallMIBConformance,
       "ciscoFirewallMIBCompliances": ciscoFirewallMIBCompliances,
       "ciscoFirewallMIBCompliance": ciscoFirewallMIBCompliance,
       "ciscoFirewallMIBComplianceRev1": ciscoFirewallMIBComplianceRev1,
       "ciscoFirewallMIBGroups": ciscoFirewallMIBGroups,
       "ciscoFirewallMIBEventsGroup": ciscoFirewallMIBEventsGroup,
       "ciscoFirewallMIBStatisticsGroup": ciscoFirewallMIBStatisticsGroup,
       "ciscoFirewallMIBNotificationGroup": ciscoFirewallMIBNotificationGroup,
       "ciscoFirewallMIBNotificationGroupRev1": ciscoFirewallMIBNotificationGroupRev1}
)
