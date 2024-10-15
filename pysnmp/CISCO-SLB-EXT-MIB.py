# SNMP MIB module (CISCO-SLB-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SLB-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:59:26 2024
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

(SlbConnectionState,
 SlbPasswordString,
 SlbRealServerState,
 SlbServerString,
 slbEntity,
 slbServerFarmName,
 slbServerFarmTableEntry,
 slbStatsTableEntry,
 slbVirtualServerTableEntry) = mibBuilder.importSymbols(
    "CISCO-SLB-MIB",
    "SlbConnectionState",
    "SlbPasswordString",
    "SlbRealServerState",
    "SlbServerString",
    "slbEntity",
    "slbServerFarmName",
    "slbServerFarmTableEntry",
    "slbStatsTableEntry",
    "slbVirtualServerTableEntry")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CiscoHTTPResponseStatusCode,
 CiscoIpProtocol,
 CiscoPort) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoHTTPResponseStatusCode",
    "CiscoIpProtocol",
    "CiscoPort")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
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

(DateAndTime,
 DisplayString,
 RowStatus,
 StorageType,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoSlbExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 254)
)
ciscoSlbExtMIB.setRevisions(
        ("2008-03-13 00:00",
         "2006-01-20 00:00",
         "2005-02-24 10:00",
         "2002-08-19 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SlbObjectNameString(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )



class SlbFunctionNameString(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class SlbUrlString(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class SlbRegularExpression(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class SlbFailAction(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("purgeConns", 2),
          ("reassignConns", 3),
          ("undefined", 4))
    )



class SlbIpAdvertise(Integer32, TextualConvention):
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
        *(("activeAdvertise", 2),
          ("alwaysAdvertise", 1),
          ("undefined", 3))
    )



class SlbStickyType(Integer32, TextualConvention):
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
        *(("destIpSticky", 5),
          ("httpCookieSticky", 2),
          ("httpHeaderSticky", 7),
          ("srcDestSticky", 6),
          ("srcIpSticky", 1),
          ("sslSticky", 3),
          ("undefined", 4))
    )



class SlbMapType(Integer32, TextualConvention):
    status = "current"
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
        *(("cookieMap", 3),
          ("headerMap", 4),
          ("notCfgMap", 1),
          ("returnCodeMap", 5),
          ("undefined", 6),
          ("urlMap", 2))
    )



class SlbReplicationMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("replAll", 2),
          ("replConnection", 3),
          ("replNone", 1),
          ("replStickyData", 4))
    )



class SlbProbeAction(Integer32, TextualConvention):
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
        *(("countAction", 4),
          ("logAction", 2),
          ("noAction", 1),
          ("removeAction", 3),
          ("undefined", 5))
    )



class SlbVlanType(Integer32, TextualConvention):
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
        *(("clientVlan", 1),
          ("ftVlan", 3),
          ("serverVlan", 2))
    )



class SlbFtState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("activeFT", 3),
          ("initializingFT", 2),
          ("notConfigFT", 1),
          ("standbyFT", 4))
    )



class SlbDirectionalMode(Integer32, TextualConvention):
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
        *(("bidirectional", 2),
          ("defdirectional", 3),
          ("unidirectional", 1))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoSlbExtMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoSlbExtMIBNotifs = _CiscoSlbExtMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 0)
)
_CiscoSlbExtMIBObjects_ObjectIdentity = ObjectIdentity
ciscoSlbExtMIBObjects = _CiscoSlbExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1)
)
_CslbxStats_ObjectIdentity = ObjectIdentity
cslbxStats = _CslbxStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 1)
)
_CslbxStatsTable_Object = MibTable
cslbxStatsTable = _CslbxStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cslbxStatsTable.setStatus("current")
_CslbxStatsTableEntry_Object = MibTableRow
cslbxStatsTableEntry = _CslbxStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cslbxStatsTableEntry.setStatus("current")
_CslbxStatsServerInitConns_Type = Counter32
_CslbxStatsServerInitConns_Object = MibTableColumn
cslbxStatsServerInitConns = _CslbxStatsServerInitConns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 1, 1, 1, 1),
    _CslbxStatsServerInitConns_Type()
)
cslbxStatsServerInitConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxStatsServerInitConns.setStatus("current")
if mibBuilder.loadTexts:
    cslbxStatsServerInitConns.setUnits("connections")
_CslbxStatsServerInitHCConns_Type = Counter64
_CslbxStatsServerInitHCConns_Object = MibTableColumn
cslbxStatsServerInitHCConns = _CslbxStatsServerInitHCConns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 1, 1, 1, 2),
    _CslbxStatsServerInitHCConns_Type()
)
cslbxStatsServerInitHCConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxStatsServerInitHCConns.setStatus("current")
if mibBuilder.loadTexts:
    cslbxStatsServerInitHCConns.setUnits("connections")
_CslbxStatsCurrConnections_Type = Gauge32
_CslbxStatsCurrConnections_Object = MibTableColumn
cslbxStatsCurrConnections = _CslbxStatsCurrConnections_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 1, 1, 1, 3),
    _CslbxStatsCurrConnections_Type()
)
cslbxStatsCurrConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxStatsCurrConnections.setStatus("current")
if mibBuilder.loadTexts:
    cslbxStatsCurrConnections.setUnits("connections")
_CslbxStatsCurrServerInitConns_Type = Gauge32
_CslbxStatsCurrServerInitConns_Object = MibTableColumn
cslbxStatsCurrServerInitConns = _CslbxStatsCurrServerInitConns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 1, 1, 1, 4),
    _CslbxStatsCurrServerInitConns_Type()
)
cslbxStatsCurrServerInitConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxStatsCurrServerInitConns.setStatus("current")
if mibBuilder.loadTexts:
    cslbxStatsCurrServerInitConns.setUnits("connections")
_CslbxStatsFailedConns_Type = Counter32
_CslbxStatsFailedConns_Object = MibTableColumn
cslbxStatsFailedConns = _CslbxStatsFailedConns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 1, 1, 1, 5),
    _CslbxStatsFailedConns_Type()
)
cslbxStatsFailedConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxStatsFailedConns.setStatus("current")
if mibBuilder.loadTexts:
    cslbxStatsFailedConns.setUnits("connections")
_CslbxStatsFailedServerInitConns_Type = Counter32
_CslbxStatsFailedServerInitConns_Object = MibTableColumn
cslbxStatsFailedServerInitConns = _CslbxStatsFailedServerInitConns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 1, 1, 1, 6),
    _CslbxStatsFailedServerInitConns_Type()
)
cslbxStatsFailedServerInitConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxStatsFailedServerInitConns.setStatus("current")
if mibBuilder.loadTexts:
    cslbxStatsFailedServerInitConns.setUnits("connections")
_CslbxStatsL4PolicyConns_Type = Counter32
_CslbxStatsL4PolicyConns_Object = MibTableColumn
cslbxStatsL4PolicyConns = _CslbxStatsL4PolicyConns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 1, 1, 1, 7),
    _CslbxStatsL4PolicyConns_Type()
)
cslbxStatsL4PolicyConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxStatsL4PolicyConns.setStatus("current")
if mibBuilder.loadTexts:
    cslbxStatsL4PolicyConns.setUnits("connections")
_CslbxStatsL7PolicyConns_Type = Counter32
_CslbxStatsL7PolicyConns_Object = MibTableColumn
cslbxStatsL7PolicyConns = _CslbxStatsL7PolicyConns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 1, 1, 1, 8),
    _CslbxStatsL7PolicyConns_Type()
)
cslbxStatsL7PolicyConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxStatsL7PolicyConns.setStatus("current")
if mibBuilder.loadTexts:
    cslbxStatsL7PolicyConns.setUnits("connections")
_CslbxStatsDroppedL4PolicyConns_Type = Counter32
_CslbxStatsDroppedL4PolicyConns_Object = MibTableColumn
cslbxStatsDroppedL4PolicyConns = _CslbxStatsDroppedL4PolicyConns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 1, 1, 1, 9),
    _CslbxStatsDroppedL4PolicyConns_Type()
)
cslbxStatsDroppedL4PolicyConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxStatsDroppedL4PolicyConns.setStatus("current")
if mibBuilder.loadTexts:
    cslbxStatsDroppedL4PolicyConns.setUnits("connections")
_CslbxStatsDroppedL7PolicyConns_Type = Counter32
_CslbxStatsDroppedL7PolicyConns_Object = MibTableColumn
cslbxStatsDroppedL7PolicyConns = _CslbxStatsDroppedL7PolicyConns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 1, 1, 1, 10),
    _CslbxStatsDroppedL7PolicyConns_Type()
)
cslbxStatsDroppedL7PolicyConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxStatsDroppedL7PolicyConns.setStatus("current")
if mibBuilder.loadTexts:
    cslbxStatsDroppedL7PolicyConns.setUnits("connections")
_CslbxStatsFtpConns_Type = Counter32
_CslbxStatsFtpConns_Object = MibTableColumn
cslbxStatsFtpConns = _CslbxStatsFtpConns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 1, 1, 1, 11),
    _CslbxStatsFtpConns_Type()
)
cslbxStatsFtpConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxStatsFtpConns.setStatus("current")
if mibBuilder.loadTexts:
    cslbxStatsFtpConns.setUnits("connections")
_CslbxStatsHttpRedirectConns_Type = Counter32
_CslbxStatsHttpRedirectConns_Object = MibTableColumn
cslbxStatsHttpRedirectConns = _CslbxStatsHttpRedirectConns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 1, 1, 1, 12),
    _CslbxStatsHttpRedirectConns_Type()
)
cslbxStatsHttpRedirectConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxStatsHttpRedirectConns.setStatus("current")
if mibBuilder.loadTexts:
    cslbxStatsHttpRedirectConns.setUnits("connections")
_CslbxStatsDroppedRedirectConns_Type = Counter32
_CslbxStatsDroppedRedirectConns_Object = MibTableColumn
cslbxStatsDroppedRedirectConns = _CslbxStatsDroppedRedirectConns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 1, 1, 1, 13),
    _CslbxStatsDroppedRedirectConns_Type()
)
cslbxStatsDroppedRedirectConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxStatsDroppedRedirectConns.setStatus("current")
if mibBuilder.loadTexts:
    cslbxStatsDroppedRedirectConns.setUnits("connections")
_CslbxStatsNoMatchPolicyRejects_Type = Counter32
_CslbxStatsNoMatchPolicyRejects_Object = MibTableColumn
cslbxStatsNoMatchPolicyRejects = _CslbxStatsNoMatchPolicyRejects_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 1, 1, 1, 14),
    _CslbxStatsNoMatchPolicyRejects_Type()
)
cslbxStatsNoMatchPolicyRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxStatsNoMatchPolicyRejects.setStatus("current")
if mibBuilder.loadTexts:
    cslbxStatsNoMatchPolicyRejects.setUnits("connections")
_CslbxStatsNoCfgPolicyRejects_Type = Counter32
_CslbxStatsNoCfgPolicyRejects_Object = MibTableColumn
cslbxStatsNoCfgPolicyRejects = _CslbxStatsNoCfgPolicyRejects_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 1, 1, 1, 15),
    _CslbxStatsNoCfgPolicyRejects_Type()
)
cslbxStatsNoCfgPolicyRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxStatsNoCfgPolicyRejects.setStatus("current")
if mibBuilder.loadTexts:
    cslbxStatsNoCfgPolicyRejects.setUnits("connections")
_CslbxStatsNoActiveServerRejects_Type = Counter32
_CslbxStatsNoActiveServerRejects_Object = MibTableColumn
cslbxStatsNoActiveServerRejects = _CslbxStatsNoActiveServerRejects_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 1, 1, 1, 16),
    _CslbxStatsNoActiveServerRejects_Type()
)
cslbxStatsNoActiveServerRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxStatsNoActiveServerRejects.setStatus("current")
if mibBuilder.loadTexts:
    cslbxStatsNoActiveServerRejects.setUnits("connections")
_CslbxStatsAclDenyRejects_Type = Counter32
_CslbxStatsAclDenyRejects_Object = MibTableColumn
cslbxStatsAclDenyRejects = _CslbxStatsAclDenyRejects_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 1, 1, 1, 17),
    _CslbxStatsAclDenyRejects_Type()
)
cslbxStatsAclDenyRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxStatsAclDenyRejects.setStatus("current")
if mibBuilder.loadTexts:
    cslbxStatsAclDenyRejects.setUnits("connections")
_CslbxStatsMaxParseLenRejects_Type = Counter32
_CslbxStatsMaxParseLenRejects_Object = MibTableColumn
cslbxStatsMaxParseLenRejects = _CslbxStatsMaxParseLenRejects_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 1, 1, 1, 18),
    _CslbxStatsMaxParseLenRejects_Type()
)
cslbxStatsMaxParseLenRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxStatsMaxParseLenRejects.setStatus("current")
if mibBuilder.loadTexts:
    cslbxStatsMaxParseLenRejects.setUnits("connections")
_CslbxStatsBadSslFormatRejects_Type = Counter32
_CslbxStatsBadSslFormatRejects_Object = MibTableColumn
cslbxStatsBadSslFormatRejects = _CslbxStatsBadSslFormatRejects_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 1, 1, 1, 19),
    _CslbxStatsBadSslFormatRejects_Type()
)
cslbxStatsBadSslFormatRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxStatsBadSslFormatRejects.setStatus("current")
if mibBuilder.loadTexts:
    cslbxStatsBadSslFormatRejects.setUnits("connections")
_CslbxStatsL7ParserErrorRejects_Type = Counter32
_CslbxStatsL7ParserErrorRejects_Object = MibTableColumn
cslbxStatsL7ParserErrorRejects = _CslbxStatsL7ParserErrorRejects_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 1, 1, 1, 20),
    _CslbxStatsL7ParserErrorRejects_Type()
)
cslbxStatsL7ParserErrorRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxStatsL7ParserErrorRejects.setStatus("current")
if mibBuilder.loadTexts:
    cslbxStatsL7ParserErrorRejects.setUnits("connections")
_CslbxStatsVerMismatchRejects_Type = Counter32
_CslbxStatsVerMismatchRejects_Object = MibTableColumn
cslbxStatsVerMismatchRejects = _CslbxStatsVerMismatchRejects_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 1, 1, 1, 21),
    _CslbxStatsVerMismatchRejects_Type()
)
cslbxStatsVerMismatchRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxStatsVerMismatchRejects.setStatus("current")
if mibBuilder.loadTexts:
    cslbxStatsVerMismatchRejects.setUnits("connections")
_CslbxStatsOutOfMemoryRejects_Type = Counter32
_CslbxStatsOutOfMemoryRejects_Object = MibTableColumn
cslbxStatsOutOfMemoryRejects = _CslbxStatsOutOfMemoryRejects_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 1, 1, 1, 22),
    _CslbxStatsOutOfMemoryRejects_Type()
)
cslbxStatsOutOfMemoryRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxStatsOutOfMemoryRejects.setStatus("current")
if mibBuilder.loadTexts:
    cslbxStatsOutOfMemoryRejects.setUnits("connections")
_CslbxStatsTimedOutConnections_Type = Counter32
_CslbxStatsTimedOutConnections_Object = MibTableColumn
cslbxStatsTimedOutConnections = _CslbxStatsTimedOutConnections_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 1, 1, 1, 23),
    _CslbxStatsTimedOutConnections_Type()
)
cslbxStatsTimedOutConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxStatsTimedOutConnections.setStatus("current")
if mibBuilder.loadTexts:
    cslbxStatsTimedOutConnections.setUnits("connections")
_CslbxStatsTcpChecksumErrorPkts_Type = Counter32
_CslbxStatsTcpChecksumErrorPkts_Object = MibTableColumn
cslbxStatsTcpChecksumErrorPkts = _CslbxStatsTcpChecksumErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 1, 1, 1, 24),
    _CslbxStatsTcpChecksumErrorPkts_Type()
)
cslbxStatsTcpChecksumErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxStatsTcpChecksumErrorPkts.setStatus("current")
if mibBuilder.loadTexts:
    cslbxStatsTcpChecksumErrorPkts.setUnits("packets")
_CslbxStatsIpChecksumErrorPkts_Type = Counter32
_CslbxStatsIpChecksumErrorPkts_Object = MibTableColumn
cslbxStatsIpChecksumErrorPkts = _CslbxStatsIpChecksumErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 1, 1, 1, 25),
    _CslbxStatsIpChecksumErrorPkts_Type()
)
cslbxStatsIpChecksumErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxStatsIpChecksumErrorPkts.setStatus("current")
if mibBuilder.loadTexts:
    cslbxStatsIpChecksumErrorPkts.setUnits("packets")
_CslbxStatsL4PolicyHCConns_Type = Counter64
_CslbxStatsL4PolicyHCConns_Object = MibTableColumn
cslbxStatsL4PolicyHCConns = _CslbxStatsL4PolicyHCConns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 1, 1, 1, 26),
    _CslbxStatsL4PolicyHCConns_Type()
)
cslbxStatsL4PolicyHCConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxStatsL4PolicyHCConns.setStatus("current")
if mibBuilder.loadTexts:
    cslbxStatsL4PolicyHCConns.setUnits("connections")
_CslbxStatsL7PolicyHCConns_Type = Counter64
_CslbxStatsL7PolicyHCConns_Object = MibTableColumn
cslbxStatsL7PolicyHCConns = _CslbxStatsL7PolicyHCConns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 1, 1, 1, 27),
    _CslbxStatsL7PolicyHCConns_Type()
)
cslbxStatsL7PolicyHCConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxStatsL7PolicyHCConns.setStatus("current")
if mibBuilder.loadTexts:
    cslbxStatsL7PolicyHCConns.setUnits("connections")
_CslbxStatsDroppedL4PolicyHCConns_Type = Counter64
_CslbxStatsDroppedL4PolicyHCConns_Object = MibTableColumn
cslbxStatsDroppedL4PolicyHCConns = _CslbxStatsDroppedL4PolicyHCConns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 1, 1, 1, 28),
    _CslbxStatsDroppedL4PolicyHCConns_Type()
)
cslbxStatsDroppedL4PolicyHCConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxStatsDroppedL4PolicyHCConns.setStatus("current")
if mibBuilder.loadTexts:
    cslbxStatsDroppedL4PolicyHCConns.setUnits("connections")
_CslbxStatsDroppedL7PolicyHCConns_Type = Counter64
_CslbxStatsDroppedL7PolicyHCConns_Object = MibTableColumn
cslbxStatsDroppedL7PolicyHCConns = _CslbxStatsDroppedL7PolicyHCConns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 1, 1, 1, 29),
    _CslbxStatsDroppedL7PolicyHCConns_Type()
)
cslbxStatsDroppedL7PolicyHCConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxStatsDroppedL7PolicyHCConns.setStatus("current")
if mibBuilder.loadTexts:
    cslbxStatsDroppedL7PolicyHCConns.setUnits("connections")
_CslbxStatsNoMatchPolicyHCRejects_Type = Counter64
_CslbxStatsNoMatchPolicyHCRejects_Object = MibTableColumn
cslbxStatsNoMatchPolicyHCRejects = _CslbxStatsNoMatchPolicyHCRejects_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 1, 1, 1, 30),
    _CslbxStatsNoMatchPolicyHCRejects_Type()
)
cslbxStatsNoMatchPolicyHCRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxStatsNoMatchPolicyHCRejects.setStatus("current")
if mibBuilder.loadTexts:
    cslbxStatsNoMatchPolicyHCRejects.setUnits("connections")
_CslbxStatsNoCfgPolicyHCRejects_Type = Counter64
_CslbxStatsNoCfgPolicyHCRejects_Object = MibTableColumn
cslbxStatsNoCfgPolicyHCRejects = _CslbxStatsNoCfgPolicyHCRejects_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 1, 1, 1, 31),
    _CslbxStatsNoCfgPolicyHCRejects_Type()
)
cslbxStatsNoCfgPolicyHCRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxStatsNoCfgPolicyHCRejects.setStatus("current")
if mibBuilder.loadTexts:
    cslbxStatsNoCfgPolicyHCRejects.setUnits("connections")
_CslbxStatsAclDenyHCRejects_Type = Counter64
_CslbxStatsAclDenyHCRejects_Object = MibTableColumn
cslbxStatsAclDenyHCRejects = _CslbxStatsAclDenyHCRejects_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 1, 1, 1, 32),
    _CslbxStatsAclDenyHCRejects_Type()
)
cslbxStatsAclDenyHCRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxStatsAclDenyHCRejects.setStatus("current")
if mibBuilder.loadTexts:
    cslbxStatsAclDenyHCRejects.setUnits("connections")
_CslbxStatsVerMismatchHCRejects_Type = Counter64
_CslbxStatsVerMismatchHCRejects_Object = MibTableColumn
cslbxStatsVerMismatchHCRejects = _CslbxStatsVerMismatchHCRejects_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 1, 1, 1, 33),
    _CslbxStatsVerMismatchHCRejects_Type()
)
cslbxStatsVerMismatchHCRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxStatsVerMismatchHCRejects.setStatus("current")
if mibBuilder.loadTexts:
    cslbxStatsVerMismatchHCRejects.setUnits("connections")
_CslbxServerFarms_ObjectIdentity = ObjectIdentity
cslbxServerFarms = _CslbxServerFarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 2)
)
_CslbxServerFarmTable_Object = MibTable
cslbxServerFarmTable = _CslbxServerFarmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cslbxServerFarmTable.setStatus("current")
_CslbxServerFarmTableEntry_Object = MibTableRow
cslbxServerFarmTableEntry = _CslbxServerFarmTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cslbxServerFarmTableEntry.setStatus("current")


class _CslbxServerFarmHashMaskAddrType_Type(InetAddressType):
    """Custom type cslbxServerFarmHashMaskAddrType based on InetAddressType"""


_CslbxServerFarmHashMaskAddrType_Object = MibTableColumn
cslbxServerFarmHashMaskAddrType = _CslbxServerFarmHashMaskAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 2, 1, 1, 1),
    _CslbxServerFarmHashMaskAddrType_Type()
)
cslbxServerFarmHashMaskAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxServerFarmHashMaskAddrType.setStatus("current")


class _CslbxServerFarmHashMaskAddr_Type(InetAddress):
    """Custom type cslbxServerFarmHashMaskAddr based on InetAddress"""
    defaultHexValue = "FFFFFFFF"

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CslbxServerFarmHashMaskAddr_Type.__name__ = "InetAddress"
_CslbxServerFarmHashMaskAddr_Object = MibTableColumn
cslbxServerFarmHashMaskAddr = _CslbxServerFarmHashMaskAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 2, 1, 1, 2),
    _CslbxServerFarmHashMaskAddr_Type()
)
cslbxServerFarmHashMaskAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxServerFarmHashMaskAddr.setStatus("current")
_CslbxServerFarmClientNatPool_Type = SlbObjectNameString
_CslbxServerFarmClientNatPool_Object = MibTableColumn
cslbxServerFarmClientNatPool = _CslbxServerFarmClientNatPool_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 2, 1, 1, 3),
    _CslbxServerFarmClientNatPool_Type()
)
cslbxServerFarmClientNatPool.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxServerFarmClientNatPool.setStatus("current")


class _CslbxServerFarmFailAction_Type(SlbFailAction):
    """Custom type cslbxServerFarmFailAction based on SlbFailAction"""


_CslbxServerFarmFailAction_Object = MibTableColumn
cslbxServerFarmFailAction = _CslbxServerFarmFailAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 2, 1, 1, 4),
    _CslbxServerFarmFailAction_Type()
)
cslbxServerFarmFailAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxServerFarmFailAction.setStatus("current")
_CslbxServerFarmHttpReturnCodeMap_Type = SlbObjectNameString
_CslbxServerFarmHttpReturnCodeMap_Object = MibTableColumn
cslbxServerFarmHttpReturnCodeMap = _CslbxServerFarmHttpReturnCodeMap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 2, 1, 1, 5),
    _CslbxServerFarmHttpReturnCodeMap_Type()
)
cslbxServerFarmHttpReturnCodeMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxServerFarmHttpReturnCodeMap.setStatus("current")


class _CslbxServerFarmInFailedThreshold_Type(Unsigned32):
    """Custom type cslbxServerFarmInFailedThreshold based on Unsigned32"""
    defaultValue = 4294967295


_CslbxServerFarmInFailedThreshold_Object = MibTableColumn
cslbxServerFarmInFailedThreshold = _CslbxServerFarmInFailedThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 2, 1, 1, 6),
    _CslbxServerFarmInFailedThreshold_Type()
)
cslbxServerFarmInFailedThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxServerFarmInFailedThreshold.setStatus("current")


class _CslbxServerFarmInbandResetTimer_Type(TimeInterval):
    """Custom type cslbxServerFarmInbandResetTimer based on TimeInterval"""
    defaultValue = 0


_CslbxServerFarmInbandResetTimer_Object = MibTableColumn
cslbxServerFarmInbandResetTimer = _CslbxServerFarmInbandResetTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 2, 1, 1, 7),
    _CslbxServerFarmInbandResetTimer_Type()
)
cslbxServerFarmInbandResetTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxServerFarmInbandResetTimer.setStatus("current")
if mibBuilder.loadTexts:
    cslbxServerFarmInbandResetTimer.setUnits("seconds")


class _CslbxServerFarmTransparent_Type(TruthValue):
    """Custom type cslbxServerFarmTransparent based on TruthValue"""


_CslbxServerFarmTransparent_Object = MibTableColumn
cslbxServerFarmTransparent = _CslbxServerFarmTransparent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 2, 1, 1, 8),
    _CslbxServerFarmTransparent_Type()
)
cslbxServerFarmTransparent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxServerFarmTransparent.setStatus("current")


class _CslbxServerFarmSlowStart_Type(Unsigned32):
    """Custom type cslbxServerFarmSlowStart based on Unsigned32"""
    defaultValue = 0


_CslbxServerFarmSlowStart_Object = MibTableColumn
cslbxServerFarmSlowStart = _CslbxServerFarmSlowStart_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 2, 1, 1, 9),
    _CslbxServerFarmSlowStart_Type()
)
cslbxServerFarmSlowStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxServerFarmSlowStart.setStatus("current")
if mibBuilder.loadTexts:
    cslbxServerFarmSlowStart.setUnits("seconds")


class _CslbxServerFarmHashHeaderName_Type(SnmpAdminString):
    """Custom type cslbxServerFarmHashHeaderName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CslbxServerFarmHashHeaderName_Type.__name__ = "SnmpAdminString"
_CslbxServerFarmHashHeaderName_Object = MibTableColumn
cslbxServerFarmHashHeaderName = _CslbxServerFarmHashHeaderName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 2, 1, 1, 10),
    _CslbxServerFarmHashHeaderName_Type()
)
cslbxServerFarmHashHeaderName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxServerFarmHashHeaderName.setStatus("current")


class _CslbxServerFarmHashCookieName_Type(SnmpAdminString):
    """Custom type cslbxServerFarmHashCookieName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CslbxServerFarmHashCookieName_Type.__name__ = "SnmpAdminString"
_CslbxServerFarmHashCookieName_Object = MibTableColumn
cslbxServerFarmHashCookieName = _CslbxServerFarmHashCookieName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 2, 1, 1, 11),
    _CslbxServerFarmHashCookieName_Type()
)
cslbxServerFarmHashCookieName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxServerFarmHashCookieName.setStatus("current")


class _CslbxServerFarmUrlPatternBegin_Type(SnmpAdminString):
    """Custom type cslbxServerFarmUrlPatternBegin based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CslbxServerFarmUrlPatternBegin_Type.__name__ = "SnmpAdminString"
_CslbxServerFarmUrlPatternBegin_Object = MibTableColumn
cslbxServerFarmUrlPatternBegin = _CslbxServerFarmUrlPatternBegin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 2, 1, 1, 12),
    _CslbxServerFarmUrlPatternBegin_Type()
)
cslbxServerFarmUrlPatternBegin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxServerFarmUrlPatternBegin.setStatus("current")


class _CslbxServerFarmUrlPatternEnd_Type(SnmpAdminString):
    """Custom type cslbxServerFarmUrlPatternEnd based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CslbxServerFarmUrlPatternEnd_Type.__name__ = "SnmpAdminString"
_CslbxServerFarmUrlPatternEnd_Object = MibTableColumn
cslbxServerFarmUrlPatternEnd = _CslbxServerFarmUrlPatternEnd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 2, 1, 1, 13),
    _CslbxServerFarmUrlPatternEnd_Type()
)
cslbxServerFarmUrlPatternEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxServerFarmUrlPatternEnd.setStatus("current")


class _CslbxServerFarmDescription_Type(SnmpAdminString):
    """Custom type cslbxServerFarmDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CslbxServerFarmDescription_Type.__name__ = "SnmpAdminString"
_CslbxServerFarmDescription_Object = MibTableColumn
cslbxServerFarmDescription = _CslbxServerFarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 2, 1, 1, 14),
    _CslbxServerFarmDescription_Type()
)
cslbxServerFarmDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxServerFarmDescription.setStatus("current")


class _CslbxServerFarmType_Type(Integer32):
    """Custom type cslbxServerFarmType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("host", 2),
          ("redirect", 1))
    )


_CslbxServerFarmType_Type.__name__ = "Integer32"
_CslbxServerFarmType_Object = MibTableColumn
cslbxServerFarmType = _CslbxServerFarmType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 2, 1, 1, 15),
    _CslbxServerFarmType_Type()
)
cslbxServerFarmType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxServerFarmType.setStatus("current")


class _CslbxServerFarmState_Type(Integer32):
    """Custom type cslbxServerFarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_CslbxServerFarmState_Type.__name__ = "Integer32"
_CslbxServerFarmState_Object = MibTableColumn
cslbxServerFarmState = _CslbxServerFarmState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 2, 1, 1, 16),
    _CslbxServerFarmState_Type()
)
cslbxServerFarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxServerFarmState.setStatus("current")
_CslbxRedirectSvrTable_Object = MibTable
cslbxRedirectSvrTable = _CslbxRedirectSvrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cslbxRedirectSvrTable.setStatus("current")
_CslbxRedirectSvrTableEntry_Object = MibTableRow
cslbxRedirectSvrTableEntry = _CslbxRedirectSvrTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 2, 2, 1)
)
cslbxRedirectSvrTableEntry.setIndexNames(
    (0, "CISCO-SLB-MIB", "slbEntity"),
    (0, "CISCO-SLB-EXT-MIB", "cslbxRedirectSvrFarmName"),
    (0, "CISCO-SLB-EXT-MIB", "cslbxRedirectSvrName"),
)
if mibBuilder.loadTexts:
    cslbxRedirectSvrTableEntry.setStatus("current")
_CslbxRedirectSvrFarmName_Type = SlbServerString
_CslbxRedirectSvrFarmName_Object = MibTableColumn
cslbxRedirectSvrFarmName = _CslbxRedirectSvrFarmName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 2, 2, 1, 1),
    _CslbxRedirectSvrFarmName_Type()
)
cslbxRedirectSvrFarmName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cslbxRedirectSvrFarmName.setStatus("current")
_CslbxRedirectSvrName_Type = SlbServerString
_CslbxRedirectSvrName_Object = MibTableColumn
cslbxRedirectSvrName = _CslbxRedirectSvrName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 2, 2, 1, 2),
    _CslbxRedirectSvrName_Type()
)
cslbxRedirectSvrName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cslbxRedirectSvrName.setStatus("current")
_CslbxRedirectSvrRelocationStr_Type = SlbUrlString
_CslbxRedirectSvrRelocationStr_Object = MibTableColumn
cslbxRedirectSvrRelocationStr = _CslbxRedirectSvrRelocationStr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 2, 2, 1, 3),
    _CslbxRedirectSvrRelocationStr_Type()
)
cslbxRedirectSvrRelocationStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxRedirectSvrRelocationStr.setStatus("current")
_CslbxRedirectSvrBackupString_Type = SlbUrlString
_CslbxRedirectSvrBackupString_Object = MibTableColumn
cslbxRedirectSvrBackupString = _CslbxRedirectSvrBackupString_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 2, 2, 1, 4),
    _CslbxRedirectSvrBackupString_Type()
)
cslbxRedirectSvrBackupString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxRedirectSvrBackupString.setStatus("current")


class _CslbxRedirectSvrRedirectCode_Type(Unsigned32):
    """Custom type cslbxRedirectSvrRedirectCode based on Unsigned32"""
    defaultValue = 302


_CslbxRedirectSvrRedirectCode_Object = MibTableColumn
cslbxRedirectSvrRedirectCode = _CslbxRedirectSvrRedirectCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 2, 2, 1, 5),
    _CslbxRedirectSvrRedirectCode_Type()
)
cslbxRedirectSvrRedirectCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxRedirectSvrRedirectCode.setStatus("current")


class _CslbxRedirectSvrRedirectPort_Type(CiscoPort):
    """Custom type cslbxRedirectSvrRedirectPort based on CiscoPort"""
    defaultValue = 80


_CslbxRedirectSvrRedirectPort_Object = MibTableColumn
cslbxRedirectSvrRedirectPort = _CslbxRedirectSvrRedirectPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 2, 2, 1, 6),
    _CslbxRedirectSvrRedirectPort_Type()
)
cslbxRedirectSvrRedirectPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxRedirectSvrRedirectPort.setStatus("current")


class _CslbxRedirectSvrState_Type(SlbRealServerState):
    """Custom type cslbxRedirectSvrState based on SlbRealServerState"""


_CslbxRedirectSvrState_Object = MibTableColumn
cslbxRedirectSvrState = _CslbxRedirectSvrState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 2, 2, 1, 7),
    _CslbxRedirectSvrState_Type()
)
cslbxRedirectSvrState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxRedirectSvrState.setStatus("current")
_CslbxRedirectSvrNumberOfConns_Type = Gauge32
_CslbxRedirectSvrNumberOfConns_Object = MibTableColumn
cslbxRedirectSvrNumberOfConns = _CslbxRedirectSvrNumberOfConns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 2, 2, 1, 8),
    _CslbxRedirectSvrNumberOfConns_Type()
)
cslbxRedirectSvrNumberOfConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxRedirectSvrNumberOfConns.setStatus("current")


class _CslbxRedirectSvrMaxConns_Type(Unsigned32):
    """Custom type cslbxRedirectSvrMaxConns based on Unsigned32"""
    defaultValue = 4294967295


_CslbxRedirectSvrMaxConns_Object = MibTableColumn
cslbxRedirectSvrMaxConns = _CslbxRedirectSvrMaxConns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 2, 2, 1, 9),
    _CslbxRedirectSvrMaxConns_Type()
)
cslbxRedirectSvrMaxConns.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxRedirectSvrMaxConns.setStatus("current")


class _CslbxRedirectSvrAdminWeight_Type(Unsigned32):
    """Custom type cslbxRedirectSvrAdminWeight based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CslbxRedirectSvrAdminWeight_Type.__name__ = "Unsigned32"
_CslbxRedirectSvrAdminWeight_Object = MibTableColumn
cslbxRedirectSvrAdminWeight = _CslbxRedirectSvrAdminWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 2, 2, 1, 10),
    _CslbxRedirectSvrAdminWeight_Type()
)
cslbxRedirectSvrAdminWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxRedirectSvrAdminWeight.setStatus("current")
_CslbxRedirectSvrOperWeight_Type = Gauge32
_CslbxRedirectSvrOperWeight_Object = MibTableColumn
cslbxRedirectSvrOperWeight = _CslbxRedirectSvrOperWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 2, 2, 1, 11),
    _CslbxRedirectSvrOperWeight_Type()
)
cslbxRedirectSvrOperWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxRedirectSvrOperWeight.setStatus("current")
_CslbxRedirectSvrMetric_Type = Unsigned32
_CslbxRedirectSvrMetric_Object = MibTableColumn
cslbxRedirectSvrMetric = _CslbxRedirectSvrMetric_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 2, 2, 1, 12),
    _CslbxRedirectSvrMetric_Type()
)
cslbxRedirectSvrMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxRedirectSvrMetric.setStatus("current")
_CslbxRedirectSvrTotalConns_Type = Counter32
_CslbxRedirectSvrTotalConns_Object = MibTableColumn
cslbxRedirectSvrTotalConns = _CslbxRedirectSvrTotalConns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 2, 2, 1, 13),
    _CslbxRedirectSvrTotalConns_Type()
)
cslbxRedirectSvrTotalConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxRedirectSvrTotalConns.setStatus("current")
_CslbxRedirectSvrHCTotalConns_Type = Counter64
_CslbxRedirectSvrHCTotalConns_Object = MibTableColumn
cslbxRedirectSvrHCTotalConns = _CslbxRedirectSvrHCTotalConns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 2, 2, 1, 14),
    _CslbxRedirectSvrHCTotalConns_Type()
)
cslbxRedirectSvrHCTotalConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxRedirectSvrHCTotalConns.setStatus("current")
_CslbxRedirectSvrRowStatus_Type = RowStatus
_CslbxRedirectSvrRowStatus_Object = MibTableColumn
cslbxRedirectSvrRowStatus = _CslbxRedirectSvrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 2, 2, 1, 15),
    _CslbxRedirectSvrRowStatus_Type()
)
cslbxRedirectSvrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxRedirectSvrRowStatus.setStatus("current")
_CslbxServerFarmProbeTable_Object = MibTable
cslbxServerFarmProbeTable = _CslbxServerFarmProbeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cslbxServerFarmProbeTable.setStatus("current")
_CslbxServerFarmProbeTableEntry_Object = MibTableRow
cslbxServerFarmProbeTableEntry = _CslbxServerFarmProbeTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 2, 3, 1)
)
cslbxServerFarmProbeTableEntry.setIndexNames(
    (0, "CISCO-SLB-MIB", "slbEntity"),
    (0, "CISCO-SLB-EXT-MIB", "cslbxServerFarmProbeFarmName"),
    (0, "CISCO-SLB-EXT-MIB", "cslbxServerFarmProbeProbeName"),
)
if mibBuilder.loadTexts:
    cslbxServerFarmProbeTableEntry.setStatus("current")
_CslbxServerFarmProbeFarmName_Type = SlbServerString
_CslbxServerFarmProbeFarmName_Object = MibTableColumn
cslbxServerFarmProbeFarmName = _CslbxServerFarmProbeFarmName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 2, 3, 1, 1),
    _CslbxServerFarmProbeFarmName_Type()
)
cslbxServerFarmProbeFarmName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cslbxServerFarmProbeFarmName.setStatus("current")
_CslbxServerFarmProbeProbeName_Type = SlbServerString
_CslbxServerFarmProbeProbeName_Object = MibTableColumn
cslbxServerFarmProbeProbeName = _CslbxServerFarmProbeProbeName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 2, 3, 1, 2),
    _CslbxServerFarmProbeProbeName_Type()
)
cslbxServerFarmProbeProbeName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cslbxServerFarmProbeProbeName.setStatus("current")
_CslbxServerFarmProbeRowStatus_Type = RowStatus
_CslbxServerFarmProbeRowStatus_Object = MibTableColumn
cslbxServerFarmProbeRowStatus = _CslbxServerFarmProbeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 2, 3, 1, 3),
    _CslbxServerFarmProbeRowStatus_Type()
)
cslbxServerFarmProbeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxServerFarmProbeRowStatus.setStatus("current")
_CslbxSfarmHttpReturnCodeTable_Object = MibTable
cslbxSfarmHttpReturnCodeTable = _CslbxSfarmHttpReturnCodeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 2, 4)
)
if mibBuilder.loadTexts:
    cslbxSfarmHttpReturnCodeTable.setStatus("current")
_CslbxSfarmHttpReturnCodeEntry_Object = MibTableRow
cslbxSfarmHttpReturnCodeEntry = _CslbxSfarmHttpReturnCodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 2, 4, 1)
)
cslbxSfarmHttpReturnCodeEntry.setIndexNames(
    (0, "CISCO-SLB-MIB", "slbEntity"),
    (0, "CISCO-SLB-MIB", "slbServerFarmName"),
    (0, "CISCO-SLB-EXT-MIB", "cslbxSfarmHttpRetCodeMinValue"),
)
if mibBuilder.loadTexts:
    cslbxSfarmHttpReturnCodeEntry.setStatus("current")
_CslbxSfarmHttpRetCodeMinValue_Type = CiscoHTTPResponseStatusCode
_CslbxSfarmHttpRetCodeMinValue_Object = MibTableColumn
cslbxSfarmHttpRetCodeMinValue = _CslbxSfarmHttpRetCodeMinValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 2, 4, 1, 1),
    _CslbxSfarmHttpRetCodeMinValue_Type()
)
cslbxSfarmHttpRetCodeMinValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cslbxSfarmHttpRetCodeMinValue.setStatus("current")


class _CslbxSfarmHttpRetCodeMaxValue_Type(CiscoHTTPResponseStatusCode):
    """Custom type cslbxSfarmHttpRetCodeMaxValue based on CiscoHTTPResponseStatusCode"""
    defaultValue = 100


_CslbxSfarmHttpRetCodeMaxValue_Object = MibTableColumn
cslbxSfarmHttpRetCodeMaxValue = _CslbxSfarmHttpRetCodeMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 2, 4, 1, 2),
    _CslbxSfarmHttpRetCodeMaxValue_Type()
)
cslbxSfarmHttpRetCodeMaxValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxSfarmHttpRetCodeMaxValue.setStatus("current")
_CslbxSfarmHttpRetCodeActionType_Type = SlbProbeAction
_CslbxSfarmHttpRetCodeActionType_Object = MibTableColumn
cslbxSfarmHttpRetCodeActionType = _CslbxSfarmHttpRetCodeActionType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 2, 4, 1, 3),
    _CslbxSfarmHttpRetCodeActionType_Type()
)
cslbxSfarmHttpRetCodeActionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxSfarmHttpRetCodeActionType.setStatus("current")


class _CslbxSfarmHttpRetCodeThreshold_Type(Unsigned32):
    """Custom type cslbxSfarmHttpRetCodeThreshold based on Unsigned32"""
    defaultValue = 0


_CslbxSfarmHttpRetCodeThreshold_Object = MibTableColumn
cslbxSfarmHttpRetCodeThreshold = _CslbxSfarmHttpRetCodeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 2, 4, 1, 4),
    _CslbxSfarmHttpRetCodeThreshold_Type()
)
cslbxSfarmHttpRetCodeThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxSfarmHttpRetCodeThreshold.setStatus("current")
_CslbxSfarmHttpRetCodeResetTimer_Type = TimeInterval
_CslbxSfarmHttpRetCodeResetTimer_Object = MibTableColumn
cslbxSfarmHttpRetCodeResetTimer = _CslbxSfarmHttpRetCodeResetTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 2, 4, 1, 5),
    _CslbxSfarmHttpRetCodeResetTimer_Type()
)
cslbxSfarmHttpRetCodeResetTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxSfarmHttpRetCodeResetTimer.setStatus("current")
if mibBuilder.loadTexts:
    cslbxSfarmHttpRetCodeResetTimer.setUnits("seconds")


class _CslbxSfarmHttpRetCodeStorageType_Type(StorageType):
    """Custom type cslbxSfarmHttpRetCodeStorageType based on StorageType"""


_CslbxSfarmHttpRetCodeStorageType_Object = MibTableColumn
cslbxSfarmHttpRetCodeStorageType = _CslbxSfarmHttpRetCodeStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 2, 4, 1, 6),
    _CslbxSfarmHttpRetCodeStorageType_Type()
)
cslbxSfarmHttpRetCodeStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxSfarmHttpRetCodeStorageType.setStatus("current")
_CslbxSfarmHttpRetCodeRowStatus_Type = RowStatus
_CslbxSfarmHttpRetCodeRowStatus_Object = MibTableColumn
cslbxSfarmHttpRetCodeRowStatus = _CslbxSfarmHttpRetCodeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 2, 4, 1, 7),
    _CslbxSfarmHttpRetCodeRowStatus_Type()
)
cslbxSfarmHttpRetCodeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxSfarmHttpRetCodeRowStatus.setStatus("current")
_CslbxServerFarmStatsTable_Object = MibTable
cslbxServerFarmStatsTable = _CslbxServerFarmStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 2, 5)
)
if mibBuilder.loadTexts:
    cslbxServerFarmStatsTable.setStatus("current")
_CslbxServerFarmStatsEntry_Object = MibTableRow
cslbxServerFarmStatsEntry = _CslbxServerFarmStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 2, 5, 1)
)
if mibBuilder.loadTexts:
    cslbxServerFarmStatsEntry.setStatus("current")
_CslbxServerFarmTotalConns_Type = Counter64
_CslbxServerFarmTotalConns_Object = MibTableColumn
cslbxServerFarmTotalConns = _CslbxServerFarmTotalConns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 2, 5, 1, 1),
    _CslbxServerFarmTotalConns_Type()
)
cslbxServerFarmTotalConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxServerFarmTotalConns.setStatus("current")
if mibBuilder.loadTexts:
    cslbxServerFarmTotalConns.setUnits("connections")
_CslbxServerFarmCurrConns_Type = Counter64
_CslbxServerFarmCurrConns_Object = MibTableColumn
cslbxServerFarmCurrConns = _CslbxServerFarmCurrConns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 2, 5, 1, 2),
    _CslbxServerFarmCurrConns_Type()
)
cslbxServerFarmCurrConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxServerFarmCurrConns.setStatus("current")
if mibBuilder.loadTexts:
    cslbxServerFarmCurrConns.setUnits("connections")
_CslbxServerFarmFailedConns_Type = Counter64
_CslbxServerFarmFailedConns_Object = MibTableColumn
cslbxServerFarmFailedConns = _CslbxServerFarmFailedConns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 2, 5, 1, 3),
    _CslbxServerFarmFailedConns_Type()
)
cslbxServerFarmFailedConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxServerFarmFailedConns.setStatus("current")
if mibBuilder.loadTexts:
    cslbxServerFarmFailedConns.setUnits("connections")
_CslbxServerFarmNumOfTimeFailOvers_Type = Counter32
_CslbxServerFarmNumOfTimeFailOvers_Object = MibTableColumn
cslbxServerFarmNumOfTimeFailOvers = _CslbxServerFarmNumOfTimeFailOvers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 2, 5, 1, 4),
    _CslbxServerFarmNumOfTimeFailOvers_Type()
)
cslbxServerFarmNumOfTimeFailOvers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxServerFarmNumOfTimeFailOvers.setStatus("current")
_CslbxServerFarmNumOfTimeBkInServs_Type = Counter32
_CslbxServerFarmNumOfTimeBkInServs_Object = MibTableColumn
cslbxServerFarmNumOfTimeBkInServs = _CslbxServerFarmNumOfTimeBkInServs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 2, 5, 1, 5),
    _CslbxServerFarmNumOfTimeBkInServs_Type()
)
cslbxServerFarmNumOfTimeBkInServs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxServerFarmNumOfTimeBkInServs.setStatus("current")
_CslbxClientNatPools_ObjectIdentity = ObjectIdentity
cslbxClientNatPools = _CslbxClientNatPools_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 3)
)
_CslbxNatPoolTable_Object = MibTable
cslbxNatPoolTable = _CslbxNatPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cslbxNatPoolTable.setStatus("current")
_CslbxNatPoolEntry_Object = MibTableRow
cslbxNatPoolEntry = _CslbxNatPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 3, 1, 1)
)
cslbxNatPoolEntry.setIndexNames(
    (0, "CISCO-SLB-MIB", "slbEntity"),
    (0, "CISCO-SLB-EXT-MIB", "cslbxNatPoolName"),
)
if mibBuilder.loadTexts:
    cslbxNatPoolEntry.setStatus("current")
_CslbxNatPoolName_Type = SlbServerString
_CslbxNatPoolName_Object = MibTableColumn
cslbxNatPoolName = _CslbxNatPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 3, 1, 1, 1),
    _CslbxNatPoolName_Type()
)
cslbxNatPoolName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cslbxNatPoolName.setStatus("current")


class _CslbxNatPoolStartAddressType_Type(InetAddressType):
    """Custom type cslbxNatPoolStartAddressType based on InetAddressType"""


_CslbxNatPoolStartAddressType_Object = MibTableColumn
cslbxNatPoolStartAddressType = _CslbxNatPoolStartAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 3, 1, 1, 2),
    _CslbxNatPoolStartAddressType_Type()
)
cslbxNatPoolStartAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxNatPoolStartAddressType.setStatus("current")


class _CslbxNatPoolStartAddress_Type(InetAddress):
    """Custom type cslbxNatPoolStartAddress based on InetAddress"""
    defaultHexValue = "00000000"

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CslbxNatPoolStartAddress_Type.__name__ = "InetAddress"
_CslbxNatPoolStartAddress_Object = MibTableColumn
cslbxNatPoolStartAddress = _CslbxNatPoolStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 3, 1, 1, 3),
    _CslbxNatPoolStartAddress_Type()
)
cslbxNatPoolStartAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxNatPoolStartAddress.setStatus("current")


class _CslbxNatPoolEndAddressType_Type(InetAddressType):
    """Custom type cslbxNatPoolEndAddressType based on InetAddressType"""


_CslbxNatPoolEndAddressType_Object = MibTableColumn
cslbxNatPoolEndAddressType = _CslbxNatPoolEndAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 3, 1, 1, 4),
    _CslbxNatPoolEndAddressType_Type()
)
cslbxNatPoolEndAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxNatPoolEndAddressType.setStatus("current")


class _CslbxNatPoolEndAddress_Type(InetAddress):
    """Custom type cslbxNatPoolEndAddress based on InetAddress"""
    defaultHexValue = "00000000"

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CslbxNatPoolEndAddress_Type.__name__ = "InetAddress"
_CslbxNatPoolEndAddress_Object = MibTableColumn
cslbxNatPoolEndAddress = _CslbxNatPoolEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 3, 1, 1, 5),
    _CslbxNatPoolEndAddress_Type()
)
cslbxNatPoolEndAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxNatPoolEndAddress.setStatus("current")
_CslbxNatPoolRowStatus_Type = RowStatus
_CslbxNatPoolRowStatus_Object = MibTableColumn
cslbxNatPoolRowStatus = _CslbxNatPoolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 3, 1, 1, 6),
    _CslbxNatPoolRowStatus_Type()
)
cslbxNatPoolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxNatPoolRowStatus.setStatus("current")
_CslbxStickyObjects_ObjectIdentity = ObjectIdentity
cslbxStickyObjects = _CslbxStickyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 4)
)
_CslbxStickyGroupTable_Object = MibTable
cslbxStickyGroupTable = _CslbxStickyGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cslbxStickyGroupTable.setStatus("current")
_CslbxStickyGroupEntry_Object = MibTableRow
cslbxStickyGroupEntry = _CslbxStickyGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 4, 1, 1)
)
cslbxStickyGroupEntry.setIndexNames(
    (0, "CISCO-SLB-MIB", "slbEntity"),
    (0, "CISCO-SLB-EXT-MIB", "cslbxStickyGroupId"),
)
if mibBuilder.loadTexts:
    cslbxStickyGroupEntry.setStatus("current")
_CslbxStickyGroupId_Type = Unsigned32
_CslbxStickyGroupId_Object = MibTableColumn
cslbxStickyGroupId = _CslbxStickyGroupId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 4, 1, 1, 1),
    _CslbxStickyGroupId_Type()
)
cslbxStickyGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cslbxStickyGroupId.setStatus("current")
_CslbxStickyGroupType_Type = SlbStickyType
_CslbxStickyGroupType_Object = MibTableColumn
cslbxStickyGroupType = _CslbxStickyGroupType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 4, 1, 1, 2),
    _CslbxStickyGroupType_Type()
)
cslbxStickyGroupType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxStickyGroupType.setStatus("current")


class _CslbxStickyGroupMaskAddressType_Type(InetAddressType):
    """Custom type cslbxStickyGroupMaskAddressType based on InetAddressType"""


_CslbxStickyGroupMaskAddressType_Object = MibTableColumn
cslbxStickyGroupMaskAddressType = _CslbxStickyGroupMaskAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 4, 1, 1, 3),
    _CslbxStickyGroupMaskAddressType_Type()
)
cslbxStickyGroupMaskAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxStickyGroupMaskAddressType.setStatus("current")


class _CslbxStickyGroupMaskAddress_Type(InetAddress):
    """Custom type cslbxStickyGroupMaskAddress based on InetAddress"""
    defaultHexValue = "FFFFFFFF"

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CslbxStickyGroupMaskAddress_Type.__name__ = "InetAddress"
_CslbxStickyGroupMaskAddress_Object = MibTableColumn
cslbxStickyGroupMaskAddress = _CslbxStickyGroupMaskAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 4, 1, 1, 4),
    _CslbxStickyGroupMaskAddress_Type()
)
cslbxStickyGroupMaskAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxStickyGroupMaskAddress.setStatus("current")


class _CslbxStickyGroupCookieName_Type(SnmpAdminString):
    """Custom type cslbxStickyGroupCookieName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CslbxStickyGroupCookieName_Type.__name__ = "SnmpAdminString"
_CslbxStickyGroupCookieName_Object = MibTableColumn
cslbxStickyGroupCookieName = _CslbxStickyGroupCookieName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 4, 1, 1, 5),
    _CslbxStickyGroupCookieName_Type()
)
cslbxStickyGroupCookieName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxStickyGroupCookieName.setStatus("current")
_CslbxStickyGroupStickyTimer_Type = Unsigned32
_CslbxStickyGroupStickyTimer_Object = MibTableColumn
cslbxStickyGroupStickyTimer = _CslbxStickyGroupStickyTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 4, 1, 1, 6),
    _CslbxStickyGroupStickyTimer_Type()
)
cslbxStickyGroupStickyTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxStickyGroupStickyTimer.setStatus("current")
if mibBuilder.loadTexts:
    cslbxStickyGroupStickyTimer.setUnits("minutes")
_CslbxStickyGroupRowStatus_Type = RowStatus
_CslbxStickyGroupRowStatus_Object = MibTableColumn
cslbxStickyGroupRowStatus = _CslbxStickyGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 4, 1, 1, 7),
    _CslbxStickyGroupRowStatus_Type()
)
cslbxStickyGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxStickyGroupRowStatus.setStatus("current")


class _CslbxStickyGroupHeaderName_Type(SnmpAdminString):
    """Custom type cslbxStickyGroupHeaderName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CslbxStickyGroupHeaderName_Type.__name__ = "SnmpAdminString"
_CslbxStickyGroupHeaderName_Object = MibTableColumn
cslbxStickyGroupHeaderName = _CslbxStickyGroupHeaderName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 4, 1, 1, 8),
    _CslbxStickyGroupHeaderName_Type()
)
cslbxStickyGroupHeaderName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxStickyGroupHeaderName.setStatus("current")
_CslbxStickyGroupTimeoutActiveConn_Type = TruthValue
_CslbxStickyGroupTimeoutActiveConn_Object = MibTableColumn
cslbxStickyGroupTimeoutActiveConn = _CslbxStickyGroupTimeoutActiveConn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 4, 1, 1, 9),
    _CslbxStickyGroupTimeoutActiveConn_Type()
)
cslbxStickyGroupTimeoutActiveConn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxStickyGroupTimeoutActiveConn.setStatus("current")
_CslbxStickyGroupReplicate_Type = TruthValue
_CslbxStickyGroupReplicate_Object = MibTableColumn
cslbxStickyGroupReplicate = _CslbxStickyGroupReplicate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 4, 1, 1, 10),
    _CslbxStickyGroupReplicate_Type()
)
cslbxStickyGroupReplicate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxStickyGroupReplicate.setStatus("current")
_CslbxStickyObjectTable_Object = MibTable
cslbxStickyObjectTable = _CslbxStickyObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 4, 2)
)
if mibBuilder.loadTexts:
    cslbxStickyObjectTable.setStatus("current")
_CslbxStickyObjectTableEntry_Object = MibTableRow
cslbxStickyObjectTableEntry = _CslbxStickyObjectTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 4, 2, 1)
)
cslbxStickyObjectTableEntry.setIndexNames(
    (0, "CISCO-SLB-MIB", "slbEntity"),
    (0, "CISCO-SLB-EXT-MIB", "cslbxStickyObjectIndex"),
)
if mibBuilder.loadTexts:
    cslbxStickyObjectTableEntry.setStatus("current")
_CslbxStickyObjectIndex_Type = Unsigned32
_CslbxStickyObjectIndex_Object = MibTableColumn
cslbxStickyObjectIndex = _CslbxStickyObjectIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 4, 2, 1, 1),
    _CslbxStickyObjectIndex_Type()
)
cslbxStickyObjectIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cslbxStickyObjectIndex.setStatus("current")
_CslbxStickyObjectGroupId_Type = Unsigned32
_CslbxStickyObjectGroupId_Object = MibTableColumn
cslbxStickyObjectGroupId = _CslbxStickyObjectGroupId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 4, 2, 1, 2),
    _CslbxStickyObjectGroupId_Type()
)
cslbxStickyObjectGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxStickyObjectGroupId.setStatus("current")
_CslbxStickyObjectType_Type = SlbStickyType
_CslbxStickyObjectType_Object = MibTableColumn
cslbxStickyObjectType = _CslbxStickyObjectType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 4, 2, 1, 3),
    _CslbxStickyObjectType_Type()
)
cslbxStickyObjectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxStickyObjectType.setStatus("current")
_CslbxStickyObjectSourceInfo_Type = Unsigned32
_CslbxStickyObjectSourceInfo_Object = MibTableColumn
cslbxStickyObjectSourceInfo = _CslbxStickyObjectSourceInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 4, 2, 1, 4),
    _CslbxStickyObjectSourceInfo_Type()
)
cslbxStickyObjectSourceInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxStickyObjectSourceInfo.setStatus("current")
_CslbxStickyObjectRealAddressType_Type = InetAddressType
_CslbxStickyObjectRealAddressType_Object = MibTableColumn
cslbxStickyObjectRealAddressType = _CslbxStickyObjectRealAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 4, 2, 1, 5),
    _CslbxStickyObjectRealAddressType_Type()
)
cslbxStickyObjectRealAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxStickyObjectRealAddressType.setStatus("current")


class _CslbxStickyObjectRealAddress_Type(InetAddress):
    """Custom type cslbxStickyObjectRealAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CslbxStickyObjectRealAddress_Type.__name__ = "InetAddress"
_CslbxStickyObjectRealAddress_Object = MibTableColumn
cslbxStickyObjectRealAddress = _CslbxStickyObjectRealAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 4, 2, 1, 6),
    _CslbxStickyObjectRealAddress_Type()
)
cslbxStickyObjectRealAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxStickyObjectRealAddress.setStatus("current")
_CslbxStickyObjectRealPort_Type = CiscoPort
_CslbxStickyObjectRealPort_Object = MibTableColumn
cslbxStickyObjectRealPort = _CslbxStickyObjectRealPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 4, 2, 1, 7),
    _CslbxStickyObjectRealPort_Type()
)
cslbxStickyObjectRealPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxStickyObjectRealPort.setStatus("current")
_CslbxStickyGroupExtTable_Object = MibTable
cslbxStickyGroupExtTable = _CslbxStickyGroupExtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 4, 3)
)
if mibBuilder.loadTexts:
    cslbxStickyGroupExtTable.setStatus("current")
_CslbxStickyGroupExtEntry_Object = MibTableRow
cslbxStickyGroupExtEntry = _CslbxStickyGroupExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 4, 3, 1)
)
if mibBuilder.loadTexts:
    cslbxStickyGroupExtEntry.setStatus("current")
_CslbxStickyOffset_Type = Unsigned32
_CslbxStickyOffset_Object = MibTableColumn
cslbxStickyOffset = _CslbxStickyOffset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 4, 3, 1, 1),
    _CslbxStickyOffset_Type()
)
cslbxStickyOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxStickyOffset.setStatus("current")
_CslbxStickyLength_Type = Unsigned32
_CslbxStickyLength_Object = MibTableColumn
cslbxStickyLength = _CslbxStickyLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 4, 3, 1, 2),
    _CslbxStickyLength_Type()
)
cslbxStickyLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxStickyLength.setStatus("current")
if mibBuilder.loadTexts:
    cslbxStickyLength.setUnits("Bytes")
_CslbxStickyCookieSecondary_Type = SnmpAdminString
_CslbxStickyCookieSecondary_Object = MibTableColumn
cslbxStickyCookieSecondary = _CslbxStickyCookieSecondary_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 4, 3, 1, 3),
    _CslbxStickyCookieSecondary_Type()
)
cslbxStickyCookieSecondary.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxStickyCookieSecondary.setStatus("current")
_CslbxStickyCookieInsertEnable_Type = TruthValue
_CslbxStickyCookieInsertEnable_Object = MibTableColumn
cslbxStickyCookieInsertEnable = _CslbxStickyCookieInsertEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 4, 3, 1, 4),
    _CslbxStickyCookieInsertEnable_Type()
)
cslbxStickyCookieInsertEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxStickyCookieInsertEnable.setStatus("current")
_CslbxStickyCookieExpiryDate_Type = DateAndTime
_CslbxStickyCookieExpiryDate_Object = MibTableColumn
cslbxStickyCookieExpiryDate = _CslbxStickyCookieExpiryDate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 4, 3, 1, 5),
    _CslbxStickyCookieExpiryDate_Type()
)
cslbxStickyCookieExpiryDate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxStickyCookieExpiryDate.setStatus("current")
_CslbxMaps_ObjectIdentity = ObjectIdentity
cslbxMaps = _CslbxMaps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 5)
)
_CslbxMapTable_Object = MibTable
cslbxMapTable = _CslbxMapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cslbxMapTable.setStatus("current")
_CslbxMapTableEntry_Object = MibTableRow
cslbxMapTableEntry = _CslbxMapTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 5, 1, 1)
)
cslbxMapTableEntry.setIndexNames(
    (0, "CISCO-SLB-MIB", "slbEntity"),
    (0, "CISCO-SLB-EXT-MIB", "cslbxMapName"),
)
if mibBuilder.loadTexts:
    cslbxMapTableEntry.setStatus("current")
_CslbxMapName_Type = SlbServerString
_CslbxMapName_Object = MibTableColumn
cslbxMapName = _CslbxMapName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 5, 1, 1, 1),
    _CslbxMapName_Type()
)
cslbxMapName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cslbxMapName.setStatus("current")


class _CslbxMapType_Type(SlbMapType):
    """Custom type cslbxMapType based on SlbMapType"""


_CslbxMapType_Object = MibTableColumn
cslbxMapType = _CslbxMapType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 5, 1, 1, 2),
    _CslbxMapType_Type()
)
cslbxMapType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxMapType.setStatus("current")
_CslbxMapRowStatus_Type = RowStatus
_CslbxMapRowStatus_Object = MibTableColumn
cslbxMapRowStatus = _CslbxMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 5, 1, 1, 3),
    _CslbxMapRowStatus_Type()
)
cslbxMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxMapRowStatus.setStatus("current")
_CslbxHttpExpressionTable_Object = MibTable
cslbxHttpExpressionTable = _CslbxHttpExpressionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 5, 2)
)
if mibBuilder.loadTexts:
    cslbxHttpExpressionTable.setStatus("current")
_CslbxHttpExpressionTableEntry_Object = MibTableRow
cslbxHttpExpressionTableEntry = _CslbxHttpExpressionTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 5, 2, 1)
)
cslbxHttpExpressionTableEntry.setIndexNames(
    (0, "CISCO-SLB-MIB", "slbEntity"),
    (0, "CISCO-SLB-EXT-MIB", "cslbxHttpExpressionMapName"),
    (0, "CISCO-SLB-EXT-MIB", "cslbxHttpExpressionIndex"),
)
if mibBuilder.loadTexts:
    cslbxHttpExpressionTableEntry.setStatus("current")
_CslbxHttpExpressionMapName_Type = SlbServerString
_CslbxHttpExpressionMapName_Object = MibTableColumn
cslbxHttpExpressionMapName = _CslbxHttpExpressionMapName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 5, 2, 1, 1),
    _CslbxHttpExpressionMapName_Type()
)
cslbxHttpExpressionMapName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cslbxHttpExpressionMapName.setStatus("current")
_CslbxHttpExpressionIndex_Type = Unsigned32
_CslbxHttpExpressionIndex_Object = MibTableColumn
cslbxHttpExpressionIndex = _CslbxHttpExpressionIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 5, 2, 1, 2),
    _CslbxHttpExpressionIndex_Type()
)
cslbxHttpExpressionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cslbxHttpExpressionIndex.setStatus("current")
_CslbxHttpExpressionFieldName_Type = SlbRegularExpression
_CslbxHttpExpressionFieldName_Object = MibTableColumn
cslbxHttpExpressionFieldName = _CslbxHttpExpressionFieldName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 5, 2, 1, 3),
    _CslbxHttpExpressionFieldName_Type()
)
cslbxHttpExpressionFieldName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxHttpExpressionFieldName.setStatus("current")
_CslbxHttpExpressionValue_Type = SlbRegularExpression
_CslbxHttpExpressionValue_Object = MibTableColumn
cslbxHttpExpressionValue = _CslbxHttpExpressionValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 5, 2, 1, 4),
    _CslbxHttpExpressionValue_Type()
)
cslbxHttpExpressionValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxHttpExpressionValue.setStatus("current")
_CslbxHttpExpressionRowStatus_Type = RowStatus
_CslbxHttpExpressionRowStatus_Object = MibTableColumn
cslbxHttpExpressionRowStatus = _CslbxHttpExpressionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 5, 2, 1, 5),
    _CslbxHttpExpressionRowStatus_Type()
)
cslbxHttpExpressionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxHttpExpressionRowStatus.setStatus("current")


class _CslbxHttpExpressionRequestMethod_Type(SnmpAdminString):
    """Custom type cslbxHttpExpressionRequestMethod based on SnmpAdminString"""
    defaultHexValue = ""


_CslbxHttpExpressionRequestMethod_Object = MibTableColumn
cslbxHttpExpressionRequestMethod = _CslbxHttpExpressionRequestMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 5, 2, 1, 6),
    _CslbxHttpExpressionRequestMethod_Type()
)
cslbxHttpExpressionRequestMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxHttpExpressionRequestMethod.setStatus("current")
_CslbxHttpReturnCodeTable_Object = MibTable
cslbxHttpReturnCodeTable = _CslbxHttpReturnCodeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 5, 3)
)
if mibBuilder.loadTexts:
    cslbxHttpReturnCodeTable.setStatus("current")
_CslbxHttpReturnCodeEntry_Object = MibTableRow
cslbxHttpReturnCodeEntry = _CslbxHttpReturnCodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 5, 3, 1)
)
cslbxHttpReturnCodeEntry.setIndexNames(
    (0, "CISCO-SLB-MIB", "slbEntity"),
    (0, "CISCO-SLB-EXT-MIB", "cslbxHttpReturnCodeMapName"),
    (0, "CISCO-SLB-EXT-MIB", "cslbxHttpReturnCodeMinValue"),
)
if mibBuilder.loadTexts:
    cslbxHttpReturnCodeEntry.setStatus("current")
_CslbxHttpReturnCodeMapName_Type = SlbServerString
_CslbxHttpReturnCodeMapName_Object = MibTableColumn
cslbxHttpReturnCodeMapName = _CslbxHttpReturnCodeMapName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 5, 3, 1, 1),
    _CslbxHttpReturnCodeMapName_Type()
)
cslbxHttpReturnCodeMapName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cslbxHttpReturnCodeMapName.setStatus("current")
_CslbxHttpReturnCodeMinValue_Type = Unsigned32
_CslbxHttpReturnCodeMinValue_Object = MibTableColumn
cslbxHttpReturnCodeMinValue = _CslbxHttpReturnCodeMinValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 5, 3, 1, 2),
    _CslbxHttpReturnCodeMinValue_Type()
)
cslbxHttpReturnCodeMinValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cslbxHttpReturnCodeMinValue.setStatus("current")


class _CslbxHttpReturnCodeMaxValue_Type(Unsigned32):
    """Custom type cslbxHttpReturnCodeMaxValue based on Unsigned32"""
    defaultValue = 0


_CslbxHttpReturnCodeMaxValue_Object = MibTableColumn
cslbxHttpReturnCodeMaxValue = _CslbxHttpReturnCodeMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 5, 3, 1, 3),
    _CslbxHttpReturnCodeMaxValue_Type()
)
cslbxHttpReturnCodeMaxValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxHttpReturnCodeMaxValue.setStatus("current")


class _CslbxHttpReturnCodeThreshold_Type(Unsigned32):
    """Custom type cslbxHttpReturnCodeThreshold based on Unsigned32"""
    defaultValue = 0


_CslbxHttpReturnCodeThreshold_Object = MibTableColumn
cslbxHttpReturnCodeThreshold = _CslbxHttpReturnCodeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 5, 3, 1, 4),
    _CslbxHttpReturnCodeThreshold_Type()
)
cslbxHttpReturnCodeThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxHttpReturnCodeThreshold.setStatus("current")


class _CslbxHttpReturnCodeResetTimer_Type(TimeInterval):
    """Custom type cslbxHttpReturnCodeResetTimer based on TimeInterval"""
    defaultValue = 0


_CslbxHttpReturnCodeResetTimer_Object = MibTableColumn
cslbxHttpReturnCodeResetTimer = _CslbxHttpReturnCodeResetTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 5, 3, 1, 5),
    _CslbxHttpReturnCodeResetTimer_Type()
)
cslbxHttpReturnCodeResetTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxHttpReturnCodeResetTimer.setStatus("current")
if mibBuilder.loadTexts:
    cslbxHttpReturnCodeResetTimer.setUnits("seconds")


class _CslbxHttpReturnCodeType_Type(SlbProbeAction):
    """Custom type cslbxHttpReturnCodeType based on SlbProbeAction"""


_CslbxHttpReturnCodeType_Object = MibTableColumn
cslbxHttpReturnCodeType = _CslbxHttpReturnCodeType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 5, 3, 1, 6),
    _CslbxHttpReturnCodeType_Type()
)
cslbxHttpReturnCodeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxHttpReturnCodeType.setStatus("current")
_CslbxHttpReturnCodeRowStatus_Type = RowStatus
_CslbxHttpReturnCodeRowStatus_Object = MibTableColumn
cslbxHttpReturnCodeRowStatus = _CslbxHttpReturnCodeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 5, 3, 1, 7),
    _CslbxHttpReturnCodeRowStatus_Type()
)
cslbxHttpReturnCodeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxHttpReturnCodeRowStatus.setStatus("current")
_CslbxServerProbes_ObjectIdentity = ObjectIdentity
cslbxServerProbes = _CslbxServerProbes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 6)
)
_CslbxPolicies_ObjectIdentity = ObjectIdentity
cslbxPolicies = _CslbxPolicies_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 7)
)
_CslbxPolicyTable_Object = MibTable
cslbxPolicyTable = _CslbxPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 7, 1)
)
if mibBuilder.loadTexts:
    cslbxPolicyTable.setStatus("current")
_CslbxPolicyTableEntry_Object = MibTableRow
cslbxPolicyTableEntry = _CslbxPolicyTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 7, 1, 1)
)
cslbxPolicyTableEntry.setIndexNames(
    (0, "CISCO-SLB-MIB", "slbEntity"),
    (0, "CISCO-SLB-EXT-MIB", "cslbxPolicyName"),
)
if mibBuilder.loadTexts:
    cslbxPolicyTableEntry.setStatus("current")
_CslbxPolicyName_Type = SlbServerString
_CslbxPolicyName_Object = MibTableColumn
cslbxPolicyName = _CslbxPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 7, 1, 1, 1),
    _CslbxPolicyName_Type()
)
cslbxPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cslbxPolicyName.setStatus("current")
_CslbxPolicyClientGroupNumber_Type = Unsigned32
_CslbxPolicyClientGroupNumber_Object = MibTableColumn
cslbxPolicyClientGroupNumber = _CslbxPolicyClientGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 7, 1, 1, 2),
    _CslbxPolicyClientGroupNumber_Type()
)
cslbxPolicyClientGroupNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxPolicyClientGroupNumber.setStatus("current")
_CslbxPolicyClientGroupName_Type = SlbObjectNameString
_CslbxPolicyClientGroupName_Object = MibTableColumn
cslbxPolicyClientGroupName = _CslbxPolicyClientGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 7, 1, 1, 3),
    _CslbxPolicyClientGroupName_Type()
)
cslbxPolicyClientGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxPolicyClientGroupName.setStatus("current")
_CslbxPolicyUrlMap_Type = SlbObjectNameString
_CslbxPolicyUrlMap_Object = MibTableColumn
cslbxPolicyUrlMap = _CslbxPolicyUrlMap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 7, 1, 1, 4),
    _CslbxPolicyUrlMap_Type()
)
cslbxPolicyUrlMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxPolicyUrlMap.setStatus("current")
_CslbxPolicyCookieMap_Type = SlbObjectNameString
_CslbxPolicyCookieMap_Object = MibTableColumn
cslbxPolicyCookieMap = _CslbxPolicyCookieMap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 7, 1, 1, 5),
    _CslbxPolicyCookieMap_Type()
)
cslbxPolicyCookieMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxPolicyCookieMap.setStatus("current")
_CslbxPolicyGenericHeaderMap_Type = SlbObjectNameString
_CslbxPolicyGenericHeaderMap_Object = MibTableColumn
cslbxPolicyGenericHeaderMap = _CslbxPolicyGenericHeaderMap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 7, 1, 1, 6),
    _CslbxPolicyGenericHeaderMap_Type()
)
cslbxPolicyGenericHeaderMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxPolicyGenericHeaderMap.setStatus("current")


class _CslbxPolicyStickyGroup_Type(Unsigned32):
    """Custom type cslbxPolicyStickyGroup based on Unsigned32"""
    defaultValue = 0


_CslbxPolicyStickyGroup_Object = MibTableColumn
cslbxPolicyStickyGroup = _CslbxPolicyStickyGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 7, 1, 1, 7),
    _CslbxPolicyStickyGroup_Type()
)
cslbxPolicyStickyGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxPolicyStickyGroup.setStatus("current")


class _CslbxPolicyDscpEnabled_Type(TruthValue):
    """Custom type cslbxPolicyDscpEnabled based on TruthValue"""


_CslbxPolicyDscpEnabled_Object = MibTableColumn
cslbxPolicyDscpEnabled = _CslbxPolicyDscpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 7, 1, 1, 8),
    _CslbxPolicyDscpEnabled_Type()
)
cslbxPolicyDscpEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxPolicyDscpEnabled.setStatus("current")


class _CslbxPolicyDscpStamping_Type(Unsigned32):
    """Custom type cslbxPolicyDscpStamping based on Unsigned32"""
    defaultValue = 0


_CslbxPolicyDscpStamping_Object = MibTableColumn
cslbxPolicyDscpStamping = _CslbxPolicyDscpStamping_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 7, 1, 1, 9),
    _CslbxPolicyDscpStamping_Type()
)
cslbxPolicyDscpStamping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxPolicyDscpStamping.setStatus("current")
_CslbxPolicyFarmName_Type = SlbObjectNameString
_CslbxPolicyFarmName_Object = MibTableColumn
cslbxPolicyFarmName = _CslbxPolicyFarmName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 7, 1, 1, 10),
    _CslbxPolicyFarmName_Type()
)
cslbxPolicyFarmName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxPolicyFarmName.setStatus("current")
_CslbxPolicyRowStatus_Type = RowStatus
_CslbxPolicyRowStatus_Object = MibTableColumn
cslbxPolicyRowStatus = _CslbxPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 7, 1, 1, 11),
    _CslbxPolicyRowStatus_Type()
)
cslbxPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxPolicyRowStatus.setStatus("current")


class _CslbxPolicyBackupFarmName_Type(SlbObjectNameString):
    """Custom type cslbxPolicyBackupFarmName based on SlbObjectNameString"""
    defaultHexValue = ""


_CslbxPolicyBackupFarmName_Object = MibTableColumn
cslbxPolicyBackupFarmName = _CslbxPolicyBackupFarmName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 7, 1, 1, 12),
    _CslbxPolicyBackupFarmName_Type()
)
cslbxPolicyBackupFarmName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxPolicyBackupFarmName.setStatus("current")


class _CslbxPolicyBkFarmStickyEnabled_Type(TruthValue):
    """Custom type cslbxPolicyBkFarmStickyEnabled based on TruthValue"""


_CslbxPolicyBkFarmStickyEnabled_Object = MibTableColumn
cslbxPolicyBkFarmStickyEnabled = _CslbxPolicyBkFarmStickyEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 7, 1, 1, 13),
    _CslbxPolicyBkFarmStickyEnabled_Type()
)
cslbxPolicyBkFarmStickyEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxPolicyBkFarmStickyEnabled.setStatus("current")


class _CslbxPolicyReverseStickyGroup_Type(Unsigned32):
    """Custom type cslbxPolicyReverseStickyGroup based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CslbxPolicyReverseStickyGroup_Type.__name__ = "Unsigned32"
_CslbxPolicyReverseStickyGroup_Object = MibTableColumn
cslbxPolicyReverseStickyGroup = _CslbxPolicyReverseStickyGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 7, 1, 1, 14),
    _CslbxPolicyReverseStickyGroup_Type()
)
cslbxPolicyReverseStickyGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxPolicyReverseStickyGroup.setStatus("current")
_CslbxVirtualServers_ObjectIdentity = ObjectIdentity
cslbxVirtualServers = _CslbxVirtualServers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 8)
)
_CslbxVirtualServerTable_Object = MibTable
cslbxVirtualServerTable = _CslbxVirtualServerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 8, 1)
)
if mibBuilder.loadTexts:
    cslbxVirtualServerTable.setStatus("current")
_CslbxVirtualServerTableEntry_Object = MibTableRow
cslbxVirtualServerTableEntry = _CslbxVirtualServerTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 8, 1, 1)
)
if mibBuilder.loadTexts:
    cslbxVirtualServerTableEntry.setStatus("current")


class _CslbxVirtualAdvertiseOption_Type(SlbIpAdvertise):
    """Custom type cslbxVirtualAdvertiseOption based on SlbIpAdvertise"""


_CslbxVirtualAdvertiseOption_Object = MibTableColumn
cslbxVirtualAdvertiseOption = _CslbxVirtualAdvertiseOption_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 8, 1, 1, 1),
    _CslbxVirtualAdvertiseOption_Type()
)
cslbxVirtualAdvertiseOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxVirtualAdvertiseOption.setStatus("current")


class _CslbxVirtualVlanId_Type(Unsigned32):
    """Custom type cslbxVirtualVlanId based on Unsigned32"""
    defaultValue = 0


_CslbxVirtualVlanId_Object = MibTableColumn
cslbxVirtualVlanId = _CslbxVirtualVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 8, 1, 1, 2),
    _CslbxVirtualVlanId_Type()
)
cslbxVirtualVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxVirtualVlanId.setStatus("current")


class _CslbxVirtualReplicationMode_Type(SlbReplicationMode):
    """Custom type cslbxVirtualReplicationMode based on SlbReplicationMode"""


_CslbxVirtualReplicationMode_Object = MibTableColumn
cslbxVirtualReplicationMode = _CslbxVirtualReplicationMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 8, 1, 1, 3),
    _CslbxVirtualReplicationMode_Type()
)
cslbxVirtualReplicationMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxVirtualReplicationMode.setStatus("current")


class _CslbxVirtualPendingTimer_Type(TimeInterval):
    """Custom type cslbxVirtualPendingTimer based on TimeInterval"""
    defaultValue = 3000


_CslbxVirtualPendingTimer_Object = MibTableColumn
cslbxVirtualPendingTimer = _CslbxVirtualPendingTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 8, 1, 1, 4),
    _CslbxVirtualPendingTimer_Type()
)
cslbxVirtualPendingTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxVirtualPendingTimer.setStatus("current")
if mibBuilder.loadTexts:
    cslbxVirtualPendingTimer.setUnits("seconds")


class _CslbxVirtualL7MaxParseLength_Type(Unsigned32):
    """Custom type cslbxVirtualL7MaxParseLength based on Unsigned32"""
    defaultValue = 600


_CslbxVirtualL7MaxParseLength_Object = MibTableColumn
cslbxVirtualL7MaxParseLength = _CslbxVirtualL7MaxParseLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 8, 1, 1, 5),
    _CslbxVirtualL7MaxParseLength_Type()
)
cslbxVirtualL7MaxParseLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxVirtualL7MaxParseLength.setStatus("current")


class _CslbxVirtualHttpPersistenceSlb_Type(TruthValue):
    """Custom type cslbxVirtualHttpPersistenceSlb based on TruthValue"""


_CslbxVirtualHttpPersistenceSlb_Object = MibTableColumn
cslbxVirtualHttpPersistenceSlb = _CslbxVirtualHttpPersistenceSlb_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 8, 1, 1, 6),
    _CslbxVirtualHttpPersistenceSlb_Type()
)
cslbxVirtualHttpPersistenceSlb.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxVirtualHttpPersistenceSlb.setStatus("current")
_CslbxVirtualURLHashBeginString_Type = SlbRegularExpression
_CslbxVirtualURLHashBeginString_Object = MibTableColumn
cslbxVirtualURLHashBeginString = _CslbxVirtualURLHashBeginString_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 8, 1, 1, 7),
    _CslbxVirtualURLHashBeginString_Type()
)
cslbxVirtualURLHashBeginString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxVirtualURLHashBeginString.setStatus("current")
_CslbxVirtualURLHashEndString_Type = SlbRegularExpression
_CslbxVirtualURLHashEndString_Object = MibTableColumn
cslbxVirtualURLHashEndString = _CslbxVirtualURLHashEndString_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 8, 1, 1, 8),
    _CslbxVirtualURLHashEndString_Type()
)
cslbxVirtualURLHashEndString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxVirtualURLHashEndString.setStatus("current")


class _CslbxVirtualMaxConns_Type(Unsigned32):
    """Custom type cslbxVirtualMaxConns based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CslbxVirtualMaxConns_Type.__name__ = "Unsigned32"
_CslbxVirtualMaxConns_Object = MibTableColumn
cslbxVirtualMaxConns = _CslbxVirtualMaxConns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 8, 1, 1, 9),
    _CslbxVirtualMaxConns_Type()
)
cslbxVirtualMaxConns.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxVirtualMaxConns.setStatus("current")


class _CslbxVirtualOwnerName_Type(SlbObjectNameString):
    """Custom type cslbxVirtualOwnerName based on SlbObjectNameString"""
    defaultHexValue = ""


_CslbxVirtualOwnerName_Object = MibTableColumn
cslbxVirtualOwnerName = _CslbxVirtualOwnerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 8, 1, 1, 10),
    _CslbxVirtualOwnerName_Type()
)
cslbxVirtualOwnerName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxVirtualOwnerName.setStatus("current")


class _CslbxVirtualFlowMode_Type(SlbDirectionalMode):
    """Custom type cslbxVirtualFlowMode based on SlbDirectionalMode"""


_CslbxVirtualFlowMode_Object = MibTableColumn
cslbxVirtualFlowMode = _CslbxVirtualFlowMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 8, 1, 1, 11),
    _CslbxVirtualFlowMode_Type()
)
cslbxVirtualFlowMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxVirtualFlowMode.setStatus("current")


class _CslbxVirtualSSLStickyOffset_Type(Unsigned32):
    """Custom type cslbxVirtualSSLStickyOffset based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_CslbxVirtualSSLStickyOffset_Type.__name__ = "Unsigned32"
_CslbxVirtualSSLStickyOffset_Object = MibTableColumn
cslbxVirtualSSLStickyOffset = _CslbxVirtualSSLStickyOffset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 8, 1, 1, 12),
    _CslbxVirtualSSLStickyOffset_Type()
)
cslbxVirtualSSLStickyOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxVirtualSSLStickyOffset.setStatus("current")
if mibBuilder.loadTexts:
    cslbxVirtualSSLStickyOffset.setUnits("bytes")


class _CslbxVirtualSSLStickyLength_Type(Unsigned32):
    """Custom type cslbxVirtualSSLStickyLength based on Unsigned32"""
    defaultValue = 32

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_CslbxVirtualSSLStickyLength_Type.__name__ = "Unsigned32"
_CslbxVirtualSSLStickyLength_Object = MibTableColumn
cslbxVirtualSSLStickyLength = _CslbxVirtualSSLStickyLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 8, 1, 1, 13),
    _CslbxVirtualSSLStickyLength_Type()
)
cslbxVirtualSSLStickyLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxVirtualSSLStickyLength.setStatus("current")
if mibBuilder.loadTexts:
    cslbxVirtualSSLStickyLength.setUnits("bytes")


class _CslbxVirtualReverseStickyGroup_Type(Unsigned32):
    """Custom type cslbxVirtualReverseStickyGroup based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CslbxVirtualReverseStickyGroup_Type.__name__ = "Unsigned32"
_CslbxVirtualReverseStickyGroup_Object = MibTableColumn
cslbxVirtualReverseStickyGroup = _CslbxVirtualReverseStickyGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 8, 1, 1, 14),
    _CslbxVirtualReverseStickyGroup_Type()
)
cslbxVirtualReverseStickyGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxVirtualReverseStickyGroup.setStatus("current")


class _CslbxVirtualBackupFarmName_Type(SlbObjectNameString):
    """Custom type cslbxVirtualBackupFarmName based on SlbObjectNameString"""
    defaultHexValue = ""


_CslbxVirtualBackupFarmName_Object = MibTableColumn
cslbxVirtualBackupFarmName = _CslbxVirtualBackupFarmName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 8, 1, 1, 15),
    _CslbxVirtualBackupFarmName_Type()
)
cslbxVirtualBackupFarmName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxVirtualBackupFarmName.setStatus("current")


class _CslbxVirtualBkFarmStickyEnabled_Type(TruthValue):
    """Custom type cslbxVirtualBkFarmStickyEnabled based on TruthValue"""


_CslbxVirtualBkFarmStickyEnabled_Object = MibTableColumn
cslbxVirtualBkFarmStickyEnabled = _CslbxVirtualBkFarmStickyEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 8, 1, 1, 16),
    _CslbxVirtualBkFarmStickyEnabled_Type()
)
cslbxVirtualBkFarmStickyEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxVirtualBkFarmStickyEnabled.setStatus("current")
_CslbxRuleTable_Object = MibTable
cslbxRuleTable = _CslbxRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 8, 2)
)
if mibBuilder.loadTexts:
    cslbxRuleTable.setStatus("current")
_CslbxRuleEntry_Object = MibTableRow
cslbxRuleEntry = _CslbxRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 8, 2, 1)
)
cslbxRuleEntry.setIndexNames(
    (0, "CISCO-SLB-MIB", "slbEntity"),
    (0, "CISCO-SLB-EXT-MIB", "cslbxRuleVirtualServerName"),
    (0, "CISCO-SLB-EXT-MIB", "cslbxRulePolicyName"),
)
if mibBuilder.loadTexts:
    cslbxRuleEntry.setStatus("current")
_CslbxRuleVirtualServerName_Type = SlbServerString
_CslbxRuleVirtualServerName_Object = MibTableColumn
cslbxRuleVirtualServerName = _CslbxRuleVirtualServerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 8, 2, 1, 1),
    _CslbxRuleVirtualServerName_Type()
)
cslbxRuleVirtualServerName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cslbxRuleVirtualServerName.setStatus("current")
_CslbxRulePolicyName_Type = SlbServerString
_CslbxRulePolicyName_Object = MibTableColumn
cslbxRulePolicyName = _CslbxRulePolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 8, 2, 1, 2),
    _CslbxRulePolicyName_Type()
)
cslbxRulePolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cslbxRulePolicyName.setStatus("current")
_CslbxRuleCurrentConnections_Type = Gauge32
_CslbxRuleCurrentConnections_Object = MibTableColumn
cslbxRuleCurrentConnections = _CslbxRuleCurrentConnections_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 8, 2, 1, 3),
    _CslbxRuleCurrentConnections_Type()
)
cslbxRuleCurrentConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxRuleCurrentConnections.setStatus("current")
_CslbxRuleTotalConnections_Type = Counter32
_CslbxRuleTotalConnections_Object = MibTableColumn
cslbxRuleTotalConnections = _CslbxRuleTotalConnections_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 8, 2, 1, 4),
    _CslbxRuleTotalConnections_Type()
)
cslbxRuleTotalConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxRuleTotalConnections.setStatus("current")
_CslbxRuleHCTotalConnections_Type = Counter64
_CslbxRuleHCTotalConnections_Object = MibTableColumn
cslbxRuleHCTotalConnections = _CslbxRuleHCTotalConnections_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 8, 2, 1, 5),
    _CslbxRuleHCTotalConnections_Type()
)
cslbxRuleHCTotalConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxRuleHCTotalConnections.setStatus("current")
_CslbxRuleTotalClientPackets_Type = Counter32
_CslbxRuleTotalClientPackets_Object = MibTableColumn
cslbxRuleTotalClientPackets = _CslbxRuleTotalClientPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 8, 2, 1, 6),
    _CslbxRuleTotalClientPackets_Type()
)
cslbxRuleTotalClientPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxRuleTotalClientPackets.setStatus("current")
_CslbxRuleHCTotalClientPackets_Type = Counter64
_CslbxRuleHCTotalClientPackets_Object = MibTableColumn
cslbxRuleHCTotalClientPackets = _CslbxRuleHCTotalClientPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 8, 2, 1, 7),
    _CslbxRuleHCTotalClientPackets_Type()
)
cslbxRuleHCTotalClientPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxRuleHCTotalClientPackets.setStatus("current")
_CslbxRuleTotalServerPackets_Type = Counter32
_CslbxRuleTotalServerPackets_Object = MibTableColumn
cslbxRuleTotalServerPackets = _CslbxRuleTotalServerPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 8, 2, 1, 8),
    _CslbxRuleTotalServerPackets_Type()
)
cslbxRuleTotalServerPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxRuleTotalServerPackets.setStatus("current")
_CslbxRuleHCTotalServerPackets_Type = Counter64
_CslbxRuleHCTotalServerPackets_Object = MibTableColumn
cslbxRuleHCTotalServerPackets = _CslbxRuleHCTotalServerPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 8, 2, 1, 9),
    _CslbxRuleHCTotalServerPackets_Type()
)
cslbxRuleHCTotalServerPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxRuleHCTotalServerPackets.setStatus("current")
_CslbxRuleRowStatus_Type = RowStatus
_CslbxRuleRowStatus_Object = MibTableColumn
cslbxRuleRowStatus = _CslbxRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 8, 2, 1, 10),
    _CslbxRuleRowStatus_Type()
)
cslbxRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxRuleRowStatus.setStatus("current")
_CslbxRuleTotalClientOctets_Type = Counter32
_CslbxRuleTotalClientOctets_Object = MibTableColumn
cslbxRuleTotalClientOctets = _CslbxRuleTotalClientOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 8, 2, 1, 11),
    _CslbxRuleTotalClientOctets_Type()
)
cslbxRuleTotalClientOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxRuleTotalClientOctets.setStatus("current")
if mibBuilder.loadTexts:
    cslbxRuleTotalClientOctets.setUnits("octets")
_CslbxRuleHCTotalClientOctets_Type = Counter64
_CslbxRuleHCTotalClientOctets_Object = MibTableColumn
cslbxRuleHCTotalClientOctets = _CslbxRuleHCTotalClientOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 8, 2, 1, 12),
    _CslbxRuleHCTotalClientOctets_Type()
)
cslbxRuleHCTotalClientOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxRuleHCTotalClientOctets.setStatus("current")
if mibBuilder.loadTexts:
    cslbxRuleHCTotalClientOctets.setUnits("octets")
_CslbxRuleTotalServerOctets_Type = Counter32
_CslbxRuleTotalServerOctets_Object = MibTableColumn
cslbxRuleTotalServerOctets = _CslbxRuleTotalServerOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 8, 2, 1, 13),
    _CslbxRuleTotalServerOctets_Type()
)
cslbxRuleTotalServerOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxRuleTotalServerOctets.setStatus("current")
if mibBuilder.loadTexts:
    cslbxRuleTotalServerOctets.setUnits("octets")
_CslbxRuleHCTotalServerOctets_Type = Counter64
_CslbxRuleHCTotalServerOctets_Object = MibTableColumn
cslbxRuleHCTotalServerOctets = _CslbxRuleHCTotalServerOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 8, 2, 1, 14),
    _CslbxRuleHCTotalServerOctets_Type()
)
cslbxRuleHCTotalServerOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxRuleHCTotalServerOctets.setStatus("current")
if mibBuilder.loadTexts:
    cslbxRuleHCTotalServerOctets.setUnits("octets")
_CslbxVlans_ObjectIdentity = ObjectIdentity
cslbxVlans = _CslbxVlans_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 9)
)
_CslbxVlanTable_Object = MibTable
cslbxVlanTable = _CslbxVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 9, 1)
)
if mibBuilder.loadTexts:
    cslbxVlanTable.setStatus("current")
_CslbxVlanEntry_Object = MibTableRow
cslbxVlanEntry = _CslbxVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 9, 1, 1)
)
cslbxVlanEntry.setIndexNames(
    (0, "CISCO-SLB-MIB", "slbEntity"),
    (0, "CISCO-SLB-EXT-MIB", "cslbxVlanId"),
)
if mibBuilder.loadTexts:
    cslbxVlanEntry.setStatus("current")
_CslbxVlanId_Type = Unsigned32
_CslbxVlanId_Object = MibTableColumn
cslbxVlanId = _CslbxVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 9, 1, 1, 1),
    _CslbxVlanId_Type()
)
cslbxVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cslbxVlanId.setStatus("current")
_CslbxVlanType_Type = SlbVlanType
_CslbxVlanType_Object = MibTableColumn
cslbxVlanType = _CslbxVlanType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 9, 1, 1, 2),
    _CslbxVlanType_Type()
)
cslbxVlanType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxVlanType.setStatus("current")


class _CslbxVlanAddressType_Type(InetAddressType):
    """Custom type cslbxVlanAddressType based on InetAddressType"""


_CslbxVlanAddressType_Object = MibTableColumn
cslbxVlanAddressType = _CslbxVlanAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 9, 1, 1, 3),
    _CslbxVlanAddressType_Type()
)
cslbxVlanAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxVlanAddressType.setStatus("current")


class _CslbxVlanAddress_Type(InetAddress):
    """Custom type cslbxVlanAddress based on InetAddress"""
    defaultHexValue = "00000000"

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CslbxVlanAddress_Type.__name__ = "InetAddress"
_CslbxVlanAddress_Object = MibTableColumn
cslbxVlanAddress = _CslbxVlanAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 9, 1, 1, 4),
    _CslbxVlanAddress_Type()
)
cslbxVlanAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxVlanAddress.setStatus("current")


class _CslbxVlanMaskAddressType_Type(InetAddressType):
    """Custom type cslbxVlanMaskAddressType based on InetAddressType"""


_CslbxVlanMaskAddressType_Object = MibTableColumn
cslbxVlanMaskAddressType = _CslbxVlanMaskAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 9, 1, 1, 5),
    _CslbxVlanMaskAddressType_Type()
)
cslbxVlanMaskAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxVlanMaskAddressType.setStatus("current")


class _CslbxVlanMaskAddress_Type(InetAddress):
    """Custom type cslbxVlanMaskAddress based on InetAddress"""
    defaultHexValue = "00000000"

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CslbxVlanMaskAddress_Type.__name__ = "InetAddress"
_CslbxVlanMaskAddress_Object = MibTableColumn
cslbxVlanMaskAddress = _CslbxVlanMaskAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 9, 1, 1, 6),
    _CslbxVlanMaskAddress_Type()
)
cslbxVlanMaskAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxVlanMaskAddress.setStatus("current")
_CslbxVlanRowStatus_Type = RowStatus
_CslbxVlanRowStatus_Object = MibTableColumn
cslbxVlanRowStatus = _CslbxVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 9, 1, 1, 7),
    _CslbxVlanRowStatus_Type()
)
cslbxVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxVlanRowStatus.setStatus("current")
_CslbxAliasAddrTable_Object = MibTable
cslbxAliasAddrTable = _CslbxAliasAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 9, 2)
)
if mibBuilder.loadTexts:
    cslbxAliasAddrTable.setStatus("current")
_CslbxAliasAddrEntry_Object = MibTableRow
cslbxAliasAddrEntry = _CslbxAliasAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 9, 2, 1)
)
cslbxAliasAddrEntry.setIndexNames(
    (0, "CISCO-SLB-MIB", "slbEntity"),
    (0, "CISCO-SLB-EXT-MIB", "cslbxAliasAddrVlanId"),
    (0, "CISCO-SLB-EXT-MIB", "cslbxAliasAddrAddressType"),
    (0, "CISCO-SLB-EXT-MIB", "cslbxAliasAddrAddress"),
)
if mibBuilder.loadTexts:
    cslbxAliasAddrEntry.setStatus("current")
_CslbxAliasAddrVlanId_Type = Unsigned32
_CslbxAliasAddrVlanId_Object = MibTableColumn
cslbxAliasAddrVlanId = _CslbxAliasAddrVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 9, 2, 1, 1),
    _CslbxAliasAddrVlanId_Type()
)
cslbxAliasAddrVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cslbxAliasAddrVlanId.setStatus("current")
_CslbxAliasAddrAddressType_Type = InetAddressType
_CslbxAliasAddrAddressType_Object = MibTableColumn
cslbxAliasAddrAddressType = _CslbxAliasAddrAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 9, 2, 1, 2),
    _CslbxAliasAddrAddressType_Type()
)
cslbxAliasAddrAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cslbxAliasAddrAddressType.setStatus("current")


class _CslbxAliasAddrAddress_Type(InetAddress):
    """Custom type cslbxAliasAddrAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_CslbxAliasAddrAddress_Type.__name__ = "InetAddress"
_CslbxAliasAddrAddress_Object = MibTableColumn
cslbxAliasAddrAddress = _CslbxAliasAddrAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 9, 2, 1, 3),
    _CslbxAliasAddrAddress_Type()
)
cslbxAliasAddrAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cslbxAliasAddrAddress.setStatus("current")
_CslbxAliasAddrRowStatus_Type = RowStatus
_CslbxAliasAddrRowStatus_Object = MibTableColumn
cslbxAliasAddrRowStatus = _CslbxAliasAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 9, 2, 1, 4),
    _CslbxAliasAddrRowStatus_Type()
)
cslbxAliasAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxAliasAddrRowStatus.setStatus("current")
_CslbxStaticRouteTable_Object = MibTable
cslbxStaticRouteTable = _CslbxStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 9, 3)
)
if mibBuilder.loadTexts:
    cslbxStaticRouteTable.setStatus("current")
_CslbxStaticRouteEntry_Object = MibTableRow
cslbxStaticRouteEntry = _CslbxStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 9, 3, 1)
)
cslbxStaticRouteEntry.setIndexNames(
    (0, "CISCO-SLB-MIB", "slbEntity"),
    (0, "CISCO-SLB-EXT-MIB", "cslbxStaticRouteVlanId"),
    (0, "CISCO-SLB-EXT-MIB", "cslbxStaticRouteSubnetAddrType"),
    (0, "CISCO-SLB-EXT-MIB", "cslbxStaticRouteSubnetAddr"),
    (0, "CISCO-SLB-EXT-MIB", "cslbxStaticRouteMaskAddrType"),
    (0, "CISCO-SLB-EXT-MIB", "cslbxStaticRouteMaskAddr"),
    (0, "CISCO-SLB-EXT-MIB", "cslbxStaticRouteGatewayAddrType"),
    (0, "CISCO-SLB-EXT-MIB", "cslbxStaticRouteGatewayAddr"),
)
if mibBuilder.loadTexts:
    cslbxStaticRouteEntry.setStatus("current")
_CslbxStaticRouteVlanId_Type = Unsigned32
_CslbxStaticRouteVlanId_Object = MibTableColumn
cslbxStaticRouteVlanId = _CslbxStaticRouteVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 9, 3, 1, 1),
    _CslbxStaticRouteVlanId_Type()
)
cslbxStaticRouteVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cslbxStaticRouteVlanId.setStatus("current")
_CslbxStaticRouteSubnetAddrType_Type = InetAddressType
_CslbxStaticRouteSubnetAddrType_Object = MibTableColumn
cslbxStaticRouteSubnetAddrType = _CslbxStaticRouteSubnetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 9, 3, 1, 2),
    _CslbxStaticRouteSubnetAddrType_Type()
)
cslbxStaticRouteSubnetAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cslbxStaticRouteSubnetAddrType.setStatus("current")


class _CslbxStaticRouteSubnetAddr_Type(InetAddress):
    """Custom type cslbxStaticRouteSubnetAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_CslbxStaticRouteSubnetAddr_Type.__name__ = "InetAddress"
_CslbxStaticRouteSubnetAddr_Object = MibTableColumn
cslbxStaticRouteSubnetAddr = _CslbxStaticRouteSubnetAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 9, 3, 1, 3),
    _CslbxStaticRouteSubnetAddr_Type()
)
cslbxStaticRouteSubnetAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cslbxStaticRouteSubnetAddr.setStatus("current")
_CslbxStaticRouteMaskAddrType_Type = InetAddressType
_CslbxStaticRouteMaskAddrType_Object = MibTableColumn
cslbxStaticRouteMaskAddrType = _CslbxStaticRouteMaskAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 9, 3, 1, 4),
    _CslbxStaticRouteMaskAddrType_Type()
)
cslbxStaticRouteMaskAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cslbxStaticRouteMaskAddrType.setStatus("current")


class _CslbxStaticRouteMaskAddr_Type(InetAddress):
    """Custom type cslbxStaticRouteMaskAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_CslbxStaticRouteMaskAddr_Type.__name__ = "InetAddress"
_CslbxStaticRouteMaskAddr_Object = MibTableColumn
cslbxStaticRouteMaskAddr = _CslbxStaticRouteMaskAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 9, 3, 1, 5),
    _CslbxStaticRouteMaskAddr_Type()
)
cslbxStaticRouteMaskAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cslbxStaticRouteMaskAddr.setStatus("current")
_CslbxStaticRouteGatewayAddrType_Type = InetAddressType
_CslbxStaticRouteGatewayAddrType_Object = MibTableColumn
cslbxStaticRouteGatewayAddrType = _CslbxStaticRouteGatewayAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 9, 3, 1, 6),
    _CslbxStaticRouteGatewayAddrType_Type()
)
cslbxStaticRouteGatewayAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cslbxStaticRouteGatewayAddrType.setStatus("current")


class _CslbxStaticRouteGatewayAddr_Type(InetAddress):
    """Custom type cslbxStaticRouteGatewayAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_CslbxStaticRouteGatewayAddr_Type.__name__ = "InetAddress"
_CslbxStaticRouteGatewayAddr_Object = MibTableColumn
cslbxStaticRouteGatewayAddr = _CslbxStaticRouteGatewayAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 9, 3, 1, 7),
    _CslbxStaticRouteGatewayAddr_Type()
)
cslbxStaticRouteGatewayAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cslbxStaticRouteGatewayAddr.setStatus("current")
_CslbxStaticRouteRowStatus_Type = RowStatus
_CslbxStaticRouteRowStatus_Object = MibTableColumn
cslbxStaticRouteRowStatus = _CslbxStaticRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 9, 3, 1, 8),
    _CslbxStaticRouteRowStatus_Type()
)
cslbxStaticRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxStaticRouteRowStatus.setStatus("current")
_CslbxFaultTolerance_ObjectIdentity = ObjectIdentity
cslbxFaultTolerance = _CslbxFaultTolerance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 10)
)
_CslbxFtTable_Object = MibTable
cslbxFtTable = _CslbxFtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 10, 1)
)
if mibBuilder.loadTexts:
    cslbxFtTable.setStatus("current")
_CslbxFtTableEntry_Object = MibTableRow
cslbxFtTableEntry = _CslbxFtTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 10, 1, 1)
)
cslbxFtTableEntry.setIndexNames(
    (0, "CISCO-SLB-MIB", "slbEntity"),
)
if mibBuilder.loadTexts:
    cslbxFtTableEntry.setStatus("current")


class _CslbxFtGroupId_Type(Unsigned32):
    """Custom type cslbxFtGroupId based on Unsigned32"""
    defaultValue = 0


_CslbxFtGroupId_Object = MibTableColumn
cslbxFtGroupId = _CslbxFtGroupId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 10, 1, 1, 1),
    _CslbxFtGroupId_Type()
)
cslbxFtGroupId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxFtGroupId.setStatus("current")


class _CslbxFtVlanId_Type(Unsigned32):
    """Custom type cslbxFtVlanId based on Unsigned32"""
    defaultValue = 0


_CslbxFtVlanId_Object = MibTableColumn
cslbxFtVlanId = _CslbxFtVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 10, 1, 1, 2),
    _CslbxFtVlanId_Type()
)
cslbxFtVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxFtVlanId.setStatus("current")


class _CslbxFtPreempt_Type(TruthValue):
    """Custom type cslbxFtPreempt based on TruthValue"""


_CslbxFtPreempt_Object = MibTableColumn
cslbxFtPreempt = _CslbxFtPreempt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 10, 1, 1, 3),
    _CslbxFtPreempt_Type()
)
cslbxFtPreempt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxFtPreempt.setStatus("current")


class _CslbxFtPriority_Type(Unsigned32):
    """Custom type cslbxFtPriority based on Unsigned32"""
    defaultValue = 10


_CslbxFtPriority_Object = MibTableColumn
cslbxFtPriority = _CslbxFtPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 10, 1, 1, 4),
    _CslbxFtPriority_Type()
)
cslbxFtPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxFtPriority.setStatus("current")


class _CslbxFtHeartBeatTimer_Type(TimeInterval):
    """Custom type cslbxFtHeartBeatTimer based on TimeInterval"""
    defaultValue = 100


_CslbxFtHeartBeatTimer_Object = MibTableColumn
cslbxFtHeartBeatTimer = _CslbxFtHeartBeatTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 10, 1, 1, 5),
    _CslbxFtHeartBeatTimer_Type()
)
cslbxFtHeartBeatTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxFtHeartBeatTimer.setStatus("current")
if mibBuilder.loadTexts:
    cslbxFtHeartBeatTimer.setUnits("seconds")


class _CslbxFtFailThreshold_Type(Unsigned32):
    """Custom type cslbxFtFailThreshold based on Unsigned32"""
    defaultValue = 3


_CslbxFtFailThreshold_Object = MibTableColumn
cslbxFtFailThreshold = _CslbxFtFailThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 10, 1, 1, 6),
    _CslbxFtFailThreshold_Type()
)
cslbxFtFailThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxFtFailThreshold.setStatus("current")
_CslbxFtState_Type = SlbFtState
_CslbxFtState_Object = MibTableColumn
cslbxFtState = _CslbxFtState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 10, 1, 1, 7),
    _CslbxFtState_Type()
)
cslbxFtState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxFtState.setStatus("current")
_CslbxFtStateChangeTime_Type = TimeStamp
_CslbxFtStateChangeTime_Object = MibTableColumn
cslbxFtStateChangeTime = _CslbxFtStateChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 10, 1, 1, 8),
    _CslbxFtStateChangeTime_Type()
)
cslbxFtStateChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxFtStateChangeTime.setStatus("current")
_CslbxFtRxHeartBeatMsgs_Type = Counter32
_CslbxFtRxHeartBeatMsgs_Object = MibTableColumn
cslbxFtRxHeartBeatMsgs = _CslbxFtRxHeartBeatMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 10, 1, 1, 9),
    _CslbxFtRxHeartBeatMsgs_Type()
)
cslbxFtRxHeartBeatMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxFtRxHeartBeatMsgs.setStatus("current")
_CslbxFtTxHeartBeatMsgs_Type = Counter32
_CslbxFtTxHeartBeatMsgs_Object = MibTableColumn
cslbxFtTxHeartBeatMsgs = _CslbxFtTxHeartBeatMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 10, 1, 1, 10),
    _CslbxFtTxHeartBeatMsgs_Type()
)
cslbxFtTxHeartBeatMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxFtTxHeartBeatMsgs.setStatus("current")
_CslbxFtRxUpdateMsgs_Type = Counter32
_CslbxFtRxUpdateMsgs_Object = MibTableColumn
cslbxFtRxUpdateMsgs = _CslbxFtRxUpdateMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 10, 1, 1, 11),
    _CslbxFtRxUpdateMsgs_Type()
)
cslbxFtRxUpdateMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxFtRxUpdateMsgs.setStatus("current")
_CslbxFtTxUpdateMsgs_Type = Counter32
_CslbxFtTxUpdateMsgs_Object = MibTableColumn
cslbxFtTxUpdateMsgs = _CslbxFtTxUpdateMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 10, 1, 1, 12),
    _CslbxFtTxUpdateMsgs_Type()
)
cslbxFtTxUpdateMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxFtTxUpdateMsgs.setStatus("current")
_CslbxFtRxCoupMsgs_Type = Counter32
_CslbxFtRxCoupMsgs_Object = MibTableColumn
cslbxFtRxCoupMsgs = _CslbxFtRxCoupMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 10, 1, 1, 13),
    _CslbxFtRxCoupMsgs_Type()
)
cslbxFtRxCoupMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxFtRxCoupMsgs.setStatus("current")
_CslbxFtTxCoupMsgs_Type = Counter32
_CslbxFtTxCoupMsgs_Object = MibTableColumn
cslbxFtTxCoupMsgs = _CslbxFtTxCoupMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 10, 1, 1, 14),
    _CslbxFtTxCoupMsgs_Type()
)
cslbxFtTxCoupMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxFtTxCoupMsgs.setStatus("current")
_CslbxFtRxElectMsgs_Type = Counter32
_CslbxFtRxElectMsgs_Object = MibTableColumn
cslbxFtRxElectMsgs = _CslbxFtRxElectMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 10, 1, 1, 15),
    _CslbxFtRxElectMsgs_Type()
)
cslbxFtRxElectMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxFtRxElectMsgs.setStatus("current")
_CslbxFtTxElectMsgs_Type = Counter32
_CslbxFtTxElectMsgs_Object = MibTableColumn
cslbxFtTxElectMsgs = _CslbxFtTxElectMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 10, 1, 1, 16),
    _CslbxFtTxElectMsgs_Type()
)
cslbxFtTxElectMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxFtTxElectMsgs.setStatus("current")
_CslbxFtRxConnReplMsgs_Type = Counter32
_CslbxFtRxConnReplMsgs_Object = MibTableColumn
cslbxFtRxConnReplMsgs = _CslbxFtRxConnReplMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 10, 1, 1, 17),
    _CslbxFtRxConnReplMsgs_Type()
)
cslbxFtRxConnReplMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxFtRxConnReplMsgs.setStatus("current")
_CslbxFtTxConnReplMsgs_Type = Counter32
_CslbxFtTxConnReplMsgs_Object = MibTableColumn
cslbxFtTxConnReplMsgs = _CslbxFtTxConnReplMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 10, 1, 1, 18),
    _CslbxFtTxConnReplMsgs_Type()
)
cslbxFtTxConnReplMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxFtTxConnReplMsgs.setStatus("current")
_CslbxFtRxPackets_Type = Counter32
_CslbxFtRxPackets_Object = MibTableColumn
cslbxFtRxPackets = _CslbxFtRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 10, 1, 1, 19),
    _CslbxFtRxPackets_Type()
)
cslbxFtRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxFtRxPackets.setStatus("current")
_CslbxFtDropPackets_Type = Counter32
_CslbxFtDropPackets_Object = MibTableColumn
cslbxFtDropPackets = _CslbxFtDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 10, 1, 1, 20),
    _CslbxFtDropPackets_Type()
)
cslbxFtDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxFtDropPackets.setStatus("current")
_CslbxFtDuplPackets_Type = Counter32
_CslbxFtDuplPackets_Object = MibTableColumn
cslbxFtDuplPackets = _CslbxFtDuplPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 10, 1, 1, 21),
    _CslbxFtDuplPackets_Type()
)
cslbxFtDuplPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxFtDuplPackets.setStatus("current")
_CslbxFtXsumErrPackets_Type = Counter32
_CslbxFtXsumErrPackets_Object = MibTableColumn
cslbxFtXsumErrPackets = _CslbxFtXsumErrPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 10, 1, 1, 22),
    _CslbxFtXsumErrPackets_Type()
)
cslbxFtXsumErrPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxFtXsumErrPackets.setStatus("current")
_CslbxFtBuffErrPackets_Type = Counter32
_CslbxFtBuffErrPackets_Object = MibTableColumn
cslbxFtBuffErrPackets = _CslbxFtBuffErrPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 10, 1, 1, 23),
    _CslbxFtBuffErrPackets_Type()
)
cslbxFtBuffErrPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxFtBuffErrPackets.setStatus("current")
_CslbxFtRowStatus_Type = RowStatus
_CslbxFtRowStatus_Object = MibTableColumn
cslbxFtRowStatus = _CslbxFtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 10, 1, 1, 24),
    _CslbxFtRowStatus_Type()
)
cslbxFtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxFtRowStatus.setStatus("current")
_CslbxXmlConfig_ObjectIdentity = ObjectIdentity
cslbxXmlConfig = _CslbxXmlConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 11)
)
_CslbxXmlConfigTable_Object = MibTable
cslbxXmlConfigTable = _CslbxXmlConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 11, 1)
)
if mibBuilder.loadTexts:
    cslbxXmlConfigTable.setStatus("current")
_CslbxXmlConfigTableEntry_Object = MibTableRow
cslbxXmlConfigTableEntry = _CslbxXmlConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 11, 1, 1)
)
cslbxXmlConfigTableEntry.setIndexNames(
    (0, "CISCO-SLB-MIB", "slbEntity"),
)
if mibBuilder.loadTexts:
    cslbxXmlConfigTableEntry.setStatus("current")


class _CslbxXmlConfigEnabled_Type(TruthValue):
    """Custom type cslbxXmlConfigEnabled based on TruthValue"""


_CslbxXmlConfigEnabled_Object = MibTableColumn
cslbxXmlConfigEnabled = _CslbxXmlConfigEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 11, 1, 1, 1),
    _CslbxXmlConfigEnabled_Type()
)
cslbxXmlConfigEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxXmlConfigEnabled.setStatus("current")


class _CslbxXmlConfigVlanId_Type(Unsigned32):
    """Custom type cslbxXmlConfigVlanId based on Unsigned32"""
    defaultValue = 0


_CslbxXmlConfigVlanId_Object = MibTableColumn
cslbxXmlConfigVlanId = _CslbxXmlConfigVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 11, 1, 1, 2),
    _CslbxXmlConfigVlanId_Type()
)
cslbxXmlConfigVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxXmlConfigVlanId.setStatus("current")


class _CslbxXmlConfigListeningPort_Type(CiscoPort):
    """Custom type cslbxXmlConfigListeningPort based on CiscoPort"""
    defaultValue = 80


_CslbxXmlConfigListeningPort_Object = MibTableColumn
cslbxXmlConfigListeningPort = _CslbxXmlConfigListeningPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 11, 1, 1, 3),
    _CslbxXmlConfigListeningPort_Type()
)
cslbxXmlConfigListeningPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxXmlConfigListeningPort.setStatus("current")
_CslbxXmlConfigRowStatus_Type = RowStatus
_CslbxXmlConfigRowStatus_Object = MibTableColumn
cslbxXmlConfigRowStatus = _CslbxXmlConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 11, 1, 1, 4),
    _CslbxXmlConfigRowStatus_Type()
)
cslbxXmlConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxXmlConfigRowStatus.setStatus("current")


class _CslbxXmlConfigUserName_Type(SlbObjectNameString):
    """Custom type cslbxXmlConfigUserName based on SlbObjectNameString"""
    defaultHexValue = ""


_CslbxXmlConfigUserName_Object = MibTableColumn
cslbxXmlConfigUserName = _CslbxXmlConfigUserName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 11, 1, 1, 5),
    _CslbxXmlConfigUserName_Type()
)
cslbxXmlConfigUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxXmlConfigUserName.setStatus("current")


class _CslbxXmlConfigPassword_Type(SlbPasswordString):
    """Custom type cslbxXmlConfigPassword based on SlbPasswordString"""
    defaultHexValue = ""


_CslbxXmlConfigPassword_Object = MibTableColumn
cslbxXmlConfigPassword = _CslbxXmlConfigPassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 11, 1, 1, 6),
    _CslbxXmlConfigPassword_Type()
)
cslbxXmlConfigPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxXmlConfigPassword.setStatus("current")


class _CslbxXmlConfigClientGroupNumber_Type(Unsigned32):
    """Custom type cslbxXmlConfigClientGroupNumber based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CslbxXmlConfigClientGroupNumber_Type.__name__ = "Unsigned32"
_CslbxXmlConfigClientGroupNumber_Object = MibTableColumn
cslbxXmlConfigClientGroupNumber = _CslbxXmlConfigClientGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 11, 1, 1, 7),
    _CslbxXmlConfigClientGroupNumber_Type()
)
cslbxXmlConfigClientGroupNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxXmlConfigClientGroupNumber.setStatus("current")


class _CslbxXmlConfigClientGroupName_Type(SlbObjectNameString):
    """Custom type cslbxXmlConfigClientGroupName based on SlbObjectNameString"""
    defaultHexValue = ""


_CslbxXmlConfigClientGroupName_Object = MibTableColumn
cslbxXmlConfigClientGroupName = _CslbxXmlConfigClientGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 11, 1, 1, 8),
    _CslbxXmlConfigClientGroupName_Type()
)
cslbxXmlConfigClientGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxXmlConfigClientGroupName.setStatus("current")
_CslbxConnections_ObjectIdentity = ObjectIdentity
cslbxConnections = _CslbxConnections_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 12)
)
_CslbxConnTable_Object = MibTable
cslbxConnTable = _CslbxConnTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 12, 1)
)
if mibBuilder.loadTexts:
    cslbxConnTable.setStatus("current")
_CslbxConnTableEntry_Object = MibTableRow
cslbxConnTableEntry = _CslbxConnTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 12, 1, 1)
)
cslbxConnTableEntry.setIndexNames(
    (0, "CISCO-SLB-MIB", "slbEntity"),
    (0, "CISCO-SLB-EXT-MIB", "cslbxConnIndex"),
)
if mibBuilder.loadTexts:
    cslbxConnTableEntry.setStatus("current")
_CslbxConnIndex_Type = Unsigned32
_CslbxConnIndex_Object = MibTableColumn
cslbxConnIndex = _CslbxConnIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 12, 1, 1, 1),
    _CslbxConnIndex_Type()
)
cslbxConnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cslbxConnIndex.setStatus("current")
_CslbxConnInDestAddrType_Type = InetAddressType
_CslbxConnInDestAddrType_Object = MibTableColumn
cslbxConnInDestAddrType = _CslbxConnInDestAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 12, 1, 1, 2),
    _CslbxConnInDestAddrType_Type()
)
cslbxConnInDestAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxConnInDestAddrType.setStatus("current")


class _CslbxConnInDestAddr_Type(InetAddress):
    """Custom type cslbxConnInDestAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CslbxConnInDestAddr_Type.__name__ = "InetAddress"
_CslbxConnInDestAddr_Object = MibTableColumn
cslbxConnInDestAddr = _CslbxConnInDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 12, 1, 1, 3),
    _CslbxConnInDestAddr_Type()
)
cslbxConnInDestAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxConnInDestAddr.setStatus("current")
_CslbxConnInDestPort_Type = CiscoPort
_CslbxConnInDestPort_Object = MibTableColumn
cslbxConnInDestPort = _CslbxConnInDestPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 12, 1, 1, 4),
    _CslbxConnInDestPort_Type()
)
cslbxConnInDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxConnInDestPort.setStatus("current")
_CslbxConnInSourceAddrType_Type = InetAddressType
_CslbxConnInSourceAddrType_Object = MibTableColumn
cslbxConnInSourceAddrType = _CslbxConnInSourceAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 12, 1, 1, 5),
    _CslbxConnInSourceAddrType_Type()
)
cslbxConnInSourceAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxConnInSourceAddrType.setStatus("current")


class _CslbxConnInSourceAddr_Type(InetAddress):
    """Custom type cslbxConnInSourceAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CslbxConnInSourceAddr_Type.__name__ = "InetAddress"
_CslbxConnInSourceAddr_Object = MibTableColumn
cslbxConnInSourceAddr = _CslbxConnInSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 12, 1, 1, 6),
    _CslbxConnInSourceAddr_Type()
)
cslbxConnInSourceAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxConnInSourceAddr.setStatus("current")
_CslbxConnInSourcePort_Type = CiscoPort
_CslbxConnInSourcePort_Object = MibTableColumn
cslbxConnInSourcePort = _CslbxConnInSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 12, 1, 1, 7),
    _CslbxConnInSourcePort_Type()
)
cslbxConnInSourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxConnInSourcePort.setStatus("current")
_CslbxConnProtocol_Type = CiscoIpProtocol
_CslbxConnProtocol_Object = MibTableColumn
cslbxConnProtocol = _CslbxConnProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 12, 1, 1, 8),
    _CslbxConnProtocol_Type()
)
cslbxConnProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxConnProtocol.setStatus("current")
_CslbxConnOutDestAddrType_Type = InetAddressType
_CslbxConnOutDestAddrType_Object = MibTableColumn
cslbxConnOutDestAddrType = _CslbxConnOutDestAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 12, 1, 1, 9),
    _CslbxConnOutDestAddrType_Type()
)
cslbxConnOutDestAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxConnOutDestAddrType.setStatus("current")


class _CslbxConnOutDestAddr_Type(InetAddress):
    """Custom type cslbxConnOutDestAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CslbxConnOutDestAddr_Type.__name__ = "InetAddress"
_CslbxConnOutDestAddr_Object = MibTableColumn
cslbxConnOutDestAddr = _CslbxConnOutDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 12, 1, 1, 10),
    _CslbxConnOutDestAddr_Type()
)
cslbxConnOutDestAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxConnOutDestAddr.setStatus("current")
_CslbxConnOutDestPort_Type = CiscoPort
_CslbxConnOutDestPort_Object = MibTableColumn
cslbxConnOutDestPort = _CslbxConnOutDestPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 12, 1, 1, 11),
    _CslbxConnOutDestPort_Type()
)
cslbxConnOutDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxConnOutDestPort.setStatus("current")
_CslbxConnOutSourceAddrType_Type = InetAddressType
_CslbxConnOutSourceAddrType_Object = MibTableColumn
cslbxConnOutSourceAddrType = _CslbxConnOutSourceAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 12, 1, 1, 12),
    _CslbxConnOutSourceAddrType_Type()
)
cslbxConnOutSourceAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxConnOutSourceAddrType.setStatus("current")


class _CslbxConnOutSourceAddr_Type(InetAddress):
    """Custom type cslbxConnOutSourceAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CslbxConnOutSourceAddr_Type.__name__ = "InetAddress"
_CslbxConnOutSourceAddr_Object = MibTableColumn
cslbxConnOutSourceAddr = _CslbxConnOutSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 12, 1, 1, 13),
    _CslbxConnOutSourceAddr_Type()
)
cslbxConnOutSourceAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxConnOutSourceAddr.setStatus("current")
_CslbxConnOutSourcePort_Type = CiscoPort
_CslbxConnOutSourcePort_Object = MibTableColumn
cslbxConnOutSourcePort = _CslbxConnOutSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 12, 1, 1, 14),
    _CslbxConnOutSourcePort_Type()
)
cslbxConnOutSourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxConnOutSourcePort.setStatus("current")
_CslbxConnState_Type = SlbConnectionState
_CslbxConnState_Object = MibTableColumn
cslbxConnState = _CslbxConnState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 12, 1, 1, 15),
    _CslbxConnState_Type()
)
cslbxConnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cslbxConnState.setStatus("current")
_CslbxNotifObjects_ObjectIdentity = ObjectIdentity
cslbxNotifObjects = _CslbxNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 13)
)


class _CslbxFtStateChangeNotifEnabled_Type(TruthValue):
    """Custom type cslbxFtStateChangeNotifEnabled based on TruthValue"""


_CslbxFtStateChangeNotifEnabled_Object = MibScalar
cslbxFtStateChangeNotifEnabled = _CslbxFtStateChangeNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 13, 1),
    _CslbxFtStateChangeNotifEnabled_Type()
)
cslbxFtStateChangeNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cslbxFtStateChangeNotifEnabled.setStatus("current")
_CslbxOwnerObjects_ObjectIdentity = ObjectIdentity
cslbxOwnerObjects = _CslbxOwnerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 14)
)
_CslbxOwnerTable_Object = MibTable
cslbxOwnerTable = _CslbxOwnerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 14, 1)
)
if mibBuilder.loadTexts:
    cslbxOwnerTable.setStatus("current")
_CslbxOwnerTableEntry_Object = MibTableRow
cslbxOwnerTableEntry = _CslbxOwnerTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 14, 1, 1)
)
cslbxOwnerTableEntry.setIndexNames(
    (0, "CISCO-SLB-MIB", "slbEntity"),
    (0, "CISCO-SLB-EXT-MIB", "cslbxOwnerName"),
)
if mibBuilder.loadTexts:
    cslbxOwnerTableEntry.setStatus("current")
_CslbxOwnerName_Type = SlbObjectNameString
_CslbxOwnerName_Object = MibTableColumn
cslbxOwnerName = _CslbxOwnerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 14, 1, 1, 1),
    _CslbxOwnerName_Type()
)
cslbxOwnerName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cslbxOwnerName.setStatus("current")


class _CslbxOwnerContactInfo_Type(SnmpAdminString):
    """Custom type cslbxOwnerContactInfo based on SnmpAdminString"""
    defaultHexValue = ""


_CslbxOwnerContactInfo_Object = MibTableColumn
cslbxOwnerContactInfo = _CslbxOwnerContactInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 14, 1, 1, 2),
    _CslbxOwnerContactInfo_Type()
)
cslbxOwnerContactInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxOwnerContactInfo.setStatus("current")


class _CslbxOwnerBillingInfo_Type(SnmpAdminString):
    """Custom type cslbxOwnerBillingInfo based on SnmpAdminString"""
    defaultHexValue = ""


_CslbxOwnerBillingInfo_Object = MibTableColumn
cslbxOwnerBillingInfo = _CslbxOwnerBillingInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 14, 1, 1, 3),
    _CslbxOwnerBillingInfo_Type()
)
cslbxOwnerBillingInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxOwnerBillingInfo.setStatus("current")


class _CslbxOwnerMaxConns_Type(Unsigned32):
    """Custom type cslbxOwnerMaxConns based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CslbxOwnerMaxConns_Type.__name__ = "Unsigned32"
_CslbxOwnerMaxConns_Object = MibTableColumn
cslbxOwnerMaxConns = _CslbxOwnerMaxConns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 14, 1, 1, 4),
    _CslbxOwnerMaxConns_Type()
)
cslbxOwnerMaxConns.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxOwnerMaxConns.setStatus("current")
_CslbxOwnerRowStatus_Type = RowStatus
_CslbxOwnerRowStatus_Object = MibTableColumn
cslbxOwnerRowStatus = _CslbxOwnerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 14, 1, 1, 5),
    _CslbxOwnerRowStatus_Type()
)
cslbxOwnerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxOwnerRowStatus.setStatus("current")
_CslbxScriptObjects_ObjectIdentity = ObjectIdentity
cslbxScriptObjects = _CslbxScriptObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 15)
)
_CslbxScriptFileTable_Object = MibTable
cslbxScriptFileTable = _CslbxScriptFileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 15, 1)
)
if mibBuilder.loadTexts:
    cslbxScriptFileTable.setStatus("current")
_CslbxScriptFileTableEntry_Object = MibTableRow
cslbxScriptFileTableEntry = _CslbxScriptFileTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 15, 1, 1)
)
cslbxScriptFileTableEntry.setIndexNames(
    (0, "CISCO-SLB-MIB", "slbEntity"),
    (0, "CISCO-SLB-EXT-MIB", "cslbxScriptFileIndex"),
)
if mibBuilder.loadTexts:
    cslbxScriptFileTableEntry.setStatus("current")


class _CslbxScriptFileIndex_Type(Unsigned32):
    """Custom type cslbxScriptFileIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CslbxScriptFileIndex_Type.__name__ = "Unsigned32"
_CslbxScriptFileIndex_Object = MibTableColumn
cslbxScriptFileIndex = _CslbxScriptFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 15, 1, 1, 1),
    _CslbxScriptFileIndex_Type()
)
cslbxScriptFileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cslbxScriptFileIndex.setStatus("current")


class _CslbxScriptFileUrl_Type(SnmpAdminString):
    """Custom type cslbxScriptFileUrl based on SnmpAdminString"""
    defaultHexValue = ""


_CslbxScriptFileUrl_Object = MibTableColumn
cslbxScriptFileUrl = _CslbxScriptFileUrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 15, 1, 1, 2),
    _CslbxScriptFileUrl_Type()
)
cslbxScriptFileUrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxScriptFileUrl.setStatus("current")
_CslbxScriptFileRowStatus_Type = RowStatus
_CslbxScriptFileRowStatus_Object = MibTableColumn
cslbxScriptFileRowStatus = _CslbxScriptFileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 15, 1, 1, 3),
    _CslbxScriptFileRowStatus_Type()
)
cslbxScriptFileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxScriptFileRowStatus.setStatus("current")
_CslbxScriptTaskTable_Object = MibTable
cslbxScriptTaskTable = _CslbxScriptTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 15, 2)
)
if mibBuilder.loadTexts:
    cslbxScriptTaskTable.setStatus("current")
_CslbxScriptTaskTableEntry_Object = MibTableRow
cslbxScriptTaskTableEntry = _CslbxScriptTaskTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 15, 2, 1)
)
cslbxScriptTaskTableEntry.setIndexNames(
    (0, "CISCO-SLB-MIB", "slbEntity"),
    (0, "CISCO-SLB-EXT-MIB", "cslbxScriptTaskIndex"),
)
if mibBuilder.loadTexts:
    cslbxScriptTaskTableEntry.setStatus("current")


class _CslbxScriptTaskIndex_Type(Unsigned32):
    """Custom type cslbxScriptTaskIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CslbxScriptTaskIndex_Type.__name__ = "Unsigned32"
_CslbxScriptTaskIndex_Object = MibTableColumn
cslbxScriptTaskIndex = _CslbxScriptTaskIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 15, 2, 1, 1),
    _CslbxScriptTaskIndex_Type()
)
cslbxScriptTaskIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cslbxScriptTaskIndex.setStatus("current")


class _CslbxScriptTaskScriptName_Type(SlbFunctionNameString):
    """Custom type cslbxScriptTaskScriptName based on SlbFunctionNameString"""
    defaultHexValue = ""


_CslbxScriptTaskScriptName_Object = MibTableColumn
cslbxScriptTaskScriptName = _CslbxScriptTaskScriptName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 15, 2, 1, 2),
    _CslbxScriptTaskScriptName_Type()
)
cslbxScriptTaskScriptName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxScriptTaskScriptName.setStatus("current")


class _CslbxScriptTaskScriptArguments_Type(SnmpAdminString):
    """Custom type cslbxScriptTaskScriptArguments based on SnmpAdminString"""
    defaultHexValue = ""


_CslbxScriptTaskScriptArguments_Object = MibTableColumn
cslbxScriptTaskScriptArguments = _CslbxScriptTaskScriptArguments_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 15, 2, 1, 3),
    _CslbxScriptTaskScriptArguments_Type()
)
cslbxScriptTaskScriptArguments.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxScriptTaskScriptArguments.setStatus("current")
_CslbxScriptTaskRowStatus_Type = RowStatus
_CslbxScriptTaskRowStatus_Object = MibTableColumn
cslbxScriptTaskRowStatus = _CslbxScriptTaskRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 1, 15, 2, 1, 4),
    _CslbxScriptTaskRowStatus_Type()
)
cslbxScriptTaskRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cslbxScriptTaskRowStatus.setStatus("current")
_CiscoSlbExtMIBConform_ObjectIdentity = ObjectIdentity
ciscoSlbExtMIBConform = _CiscoSlbExtMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 2)
)
_CslbxMIBCompliances_ObjectIdentity = ObjectIdentity
cslbxMIBCompliances = _CslbxMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 2, 1)
)
_CslbxMIBGroups_ObjectIdentity = ObjectIdentity
cslbxMIBGroups = _CslbxMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 2, 2)
)
slbStatsTableEntry.registerAugmentions(
    ("CISCO-SLB-EXT-MIB",
     "cslbxStatsTableEntry")
)
cslbxStatsTableEntry.setIndexNames(*slbStatsTableEntry.getIndexNames())
slbServerFarmTableEntry.registerAugmentions(
    ("CISCO-SLB-EXT-MIB",
     "cslbxServerFarmTableEntry")
)
cslbxServerFarmTableEntry.setIndexNames(*slbServerFarmTableEntry.getIndexNames())
slbServerFarmTableEntry.registerAugmentions(
    ("CISCO-SLB-EXT-MIB",
     "cslbxServerFarmStatsEntry")
)
cslbxServerFarmStatsEntry.setIndexNames(*slbServerFarmTableEntry.getIndexNames())
cslbxStickyGroupEntry.registerAugmentions(
    ("CISCO-SLB-EXT-MIB",
     "cslbxStickyGroupExtEntry")
)
cslbxStickyGroupExtEntry.setIndexNames(*cslbxStickyGroupEntry.getIndexNames())
slbVirtualServerTableEntry.registerAugmentions(
    ("CISCO-SLB-EXT-MIB",
     "cslbxVirtualServerTableEntry")
)
cslbxVirtualServerTableEntry.setIndexNames(*slbVirtualServerTableEntry.getIndexNames())

# Managed Objects groups

cslbxStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 2, 2, 1)
)
cslbxStatsGroup.setObjects(
      *(("CISCO-SLB-EXT-MIB", "cslbxStatsServerInitConns"),
        ("CISCO-SLB-EXT-MIB", "cslbxStatsServerInitHCConns"),
        ("CISCO-SLB-EXT-MIB", "cslbxStatsCurrConnections"),
        ("CISCO-SLB-EXT-MIB", "cslbxStatsCurrServerInitConns"),
        ("CISCO-SLB-EXT-MIB", "cslbxStatsFailedConns"),
        ("CISCO-SLB-EXT-MIB", "cslbxStatsFailedServerInitConns"),
        ("CISCO-SLB-EXT-MIB", "cslbxStatsL4PolicyConns"),
        ("CISCO-SLB-EXT-MIB", "cslbxStatsL7PolicyConns"),
        ("CISCO-SLB-EXT-MIB", "cslbxStatsDroppedL4PolicyConns"),
        ("CISCO-SLB-EXT-MIB", "cslbxStatsDroppedL7PolicyConns"),
        ("CISCO-SLB-EXT-MIB", "cslbxStatsFtpConns"),
        ("CISCO-SLB-EXT-MIB", "cslbxStatsHttpRedirectConns"),
        ("CISCO-SLB-EXT-MIB", "cslbxStatsDroppedRedirectConns"),
        ("CISCO-SLB-EXT-MIB", "cslbxStatsNoMatchPolicyRejects"),
        ("CISCO-SLB-EXT-MIB", "cslbxStatsNoCfgPolicyRejects"),
        ("CISCO-SLB-EXT-MIB", "cslbxStatsNoActiveServerRejects"),
        ("CISCO-SLB-EXT-MIB", "cslbxStatsAclDenyRejects"),
        ("CISCO-SLB-EXT-MIB", "cslbxStatsMaxParseLenRejects"),
        ("CISCO-SLB-EXT-MIB", "cslbxStatsBadSslFormatRejects"),
        ("CISCO-SLB-EXT-MIB", "cslbxStatsL7ParserErrorRejects"),
        ("CISCO-SLB-EXT-MIB", "cslbxStatsVerMismatchRejects"),
        ("CISCO-SLB-EXT-MIB", "cslbxStatsOutOfMemoryRejects"),
        ("CISCO-SLB-EXT-MIB", "cslbxStatsTimedOutConnections"),
        ("CISCO-SLB-EXT-MIB", "cslbxStatsTcpChecksumErrorPkts"),
        ("CISCO-SLB-EXT-MIB", "cslbxStatsIpChecksumErrorPkts"))
)
if mibBuilder.loadTexts:
    cslbxStatsGroup.setStatus("current")

cslbxServerFarmsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 2, 2, 2)
)
cslbxServerFarmsGroup.setObjects(
      *(("CISCO-SLB-EXT-MIB", "cslbxServerFarmHashMaskAddrType"),
        ("CISCO-SLB-EXT-MIB", "cslbxServerFarmHashMaskAddr"),
        ("CISCO-SLB-EXT-MIB", "cslbxServerFarmClientNatPool"),
        ("CISCO-SLB-EXT-MIB", "cslbxServerFarmFailAction"),
        ("CISCO-SLB-EXT-MIB", "cslbxServerFarmHttpReturnCodeMap"),
        ("CISCO-SLB-EXT-MIB", "cslbxServerFarmInFailedThreshold"),
        ("CISCO-SLB-EXT-MIB", "cslbxServerFarmInbandResetTimer"),
        ("CISCO-SLB-EXT-MIB", "cslbxRedirectSvrRelocationStr"),
        ("CISCO-SLB-EXT-MIB", "cslbxRedirectSvrBackupString"),
        ("CISCO-SLB-EXT-MIB", "cslbxRedirectSvrRedirectCode"),
        ("CISCO-SLB-EXT-MIB", "cslbxRedirectSvrRedirectPort"),
        ("CISCO-SLB-EXT-MIB", "cslbxRedirectSvrState"),
        ("CISCO-SLB-EXT-MIB", "cslbxRedirectSvrNumberOfConns"),
        ("CISCO-SLB-EXT-MIB", "cslbxRedirectSvrMaxConns"),
        ("CISCO-SLB-EXT-MIB", "cslbxRedirectSvrAdminWeight"),
        ("CISCO-SLB-EXT-MIB", "cslbxRedirectSvrOperWeight"),
        ("CISCO-SLB-EXT-MIB", "cslbxRedirectSvrMetric"),
        ("CISCO-SLB-EXT-MIB", "cslbxRedirectSvrTotalConns"),
        ("CISCO-SLB-EXT-MIB", "cslbxRedirectSvrHCTotalConns"),
        ("CISCO-SLB-EXT-MIB", "cslbxRedirectSvrRowStatus"),
        ("CISCO-SLB-EXT-MIB", "cslbxServerFarmProbeRowStatus"))
)
if mibBuilder.loadTexts:
    cslbxServerFarmsGroup.setStatus("current")

cslbxClientNatPoolsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 2, 2, 3)
)
cslbxClientNatPoolsGroup.setObjects(
      *(("CISCO-SLB-EXT-MIB", "cslbxNatPoolStartAddressType"),
        ("CISCO-SLB-EXT-MIB", "cslbxNatPoolStartAddress"),
        ("CISCO-SLB-EXT-MIB", "cslbxNatPoolEndAddressType"),
        ("CISCO-SLB-EXT-MIB", "cslbxNatPoolEndAddress"),
        ("CISCO-SLB-EXT-MIB", "cslbxNatPoolRowStatus"))
)
if mibBuilder.loadTexts:
    cslbxClientNatPoolsGroup.setStatus("current")

cslbxStickyGroupsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 2, 2, 4)
)
cslbxStickyGroupsGroup.setObjects(
      *(("CISCO-SLB-EXT-MIB", "cslbxStickyGroupType"),
        ("CISCO-SLB-EXT-MIB", "cslbxStickyGroupMaskAddressType"),
        ("CISCO-SLB-EXT-MIB", "cslbxStickyGroupMaskAddress"),
        ("CISCO-SLB-EXT-MIB", "cslbxStickyGroupCookieName"),
        ("CISCO-SLB-EXT-MIB", "cslbxStickyGroupStickyTimer"),
        ("CISCO-SLB-EXT-MIB", "cslbxStickyGroupRowStatus"))
)
if mibBuilder.loadTexts:
    cslbxStickyGroupsGroup.setStatus("deprecated")

cslbxStickyObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 2, 2, 5)
)
cslbxStickyObjectsGroup.setObjects(
      *(("CISCO-SLB-EXT-MIB", "cslbxStickyObjectGroupId"),
        ("CISCO-SLB-EXT-MIB", "cslbxStickyObjectType"),
        ("CISCO-SLB-EXT-MIB", "cslbxStickyObjectSourceInfo"),
        ("CISCO-SLB-EXT-MIB", "cslbxStickyObjectRealAddressType"),
        ("CISCO-SLB-EXT-MIB", "cslbxStickyObjectRealAddress"),
        ("CISCO-SLB-EXT-MIB", "cslbxStickyObjectRealPort"))
)
if mibBuilder.loadTexts:
    cslbxStickyObjectsGroup.setStatus("current")

cslbxMapsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 2, 2, 6)
)
cslbxMapsGroup.setObjects(
      *(("CISCO-SLB-EXT-MIB", "cslbxMapType"),
        ("CISCO-SLB-EXT-MIB", "cslbxMapRowStatus"),
        ("CISCO-SLB-EXT-MIB", "cslbxHttpExpressionFieldName"),
        ("CISCO-SLB-EXT-MIB", "cslbxHttpExpressionValue"),
        ("CISCO-SLB-EXT-MIB", "cslbxHttpExpressionRowStatus"),
        ("CISCO-SLB-EXT-MIB", "cslbxHttpReturnCodeMaxValue"),
        ("CISCO-SLB-EXT-MIB", "cslbxHttpReturnCodeThreshold"),
        ("CISCO-SLB-EXT-MIB", "cslbxHttpReturnCodeResetTimer"),
        ("CISCO-SLB-EXT-MIB", "cslbxHttpReturnCodeType"),
        ("CISCO-SLB-EXT-MIB", "cslbxHttpReturnCodeRowStatus"))
)
if mibBuilder.loadTexts:
    cslbxMapsGroup.setStatus("current")

cslbxPoliciesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 2, 2, 8)
)
cslbxPoliciesGroup.setObjects(
      *(("CISCO-SLB-EXT-MIB", "cslbxPolicyClientGroupNumber"),
        ("CISCO-SLB-EXT-MIB", "cslbxPolicyClientGroupName"),
        ("CISCO-SLB-EXT-MIB", "cslbxPolicyUrlMap"),
        ("CISCO-SLB-EXT-MIB", "cslbxPolicyCookieMap"),
        ("CISCO-SLB-EXT-MIB", "cslbxPolicyGenericHeaderMap"),
        ("CISCO-SLB-EXT-MIB", "cslbxPolicyStickyGroup"),
        ("CISCO-SLB-EXT-MIB", "cslbxPolicyDscpEnabled"),
        ("CISCO-SLB-EXT-MIB", "cslbxPolicyDscpStamping"),
        ("CISCO-SLB-EXT-MIB", "cslbxPolicyFarmName"),
        ("CISCO-SLB-EXT-MIB", "cslbxPolicyRowStatus"))
)
if mibBuilder.loadTexts:
    cslbxPoliciesGroup.setStatus("current")

cslbxVirtualServersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 2, 2, 9)
)
cslbxVirtualServersGroup.setObjects(
      *(("CISCO-SLB-EXT-MIB", "cslbxVirtualAdvertiseOption"),
        ("CISCO-SLB-EXT-MIB", "cslbxVirtualVlanId"),
        ("CISCO-SLB-EXT-MIB", "cslbxVirtualReplicationMode"),
        ("CISCO-SLB-EXT-MIB", "cslbxVirtualPendingTimer"),
        ("CISCO-SLB-EXT-MIB", "cslbxVirtualL7MaxParseLength"),
        ("CISCO-SLB-EXT-MIB", "cslbxVirtualHttpPersistenceSlb"),
        ("CISCO-SLB-EXT-MIB", "cslbxVirtualURLHashBeginString"),
        ("CISCO-SLB-EXT-MIB", "cslbxVirtualURLHashEndString"),
        ("CISCO-SLB-EXT-MIB", "cslbxRuleCurrentConnections"),
        ("CISCO-SLB-EXT-MIB", "cslbxRuleTotalConnections"),
        ("CISCO-SLB-EXT-MIB", "cslbxRuleHCTotalConnections"),
        ("CISCO-SLB-EXT-MIB", "cslbxRuleTotalClientPackets"),
        ("CISCO-SLB-EXT-MIB", "cslbxRuleHCTotalClientPackets"),
        ("CISCO-SLB-EXT-MIB", "cslbxRuleTotalServerPackets"),
        ("CISCO-SLB-EXT-MIB", "cslbxRuleHCTotalServerPackets"),
        ("CISCO-SLB-EXT-MIB", "cslbxRuleRowStatus"))
)
if mibBuilder.loadTexts:
    cslbxVirtualServersGroup.setStatus("current")

cslbxVlansGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 2, 2, 10)
)
cslbxVlansGroup.setObjects(
      *(("CISCO-SLB-EXT-MIB", "cslbxVlanType"),
        ("CISCO-SLB-EXT-MIB", "cslbxVlanAddressType"),
        ("CISCO-SLB-EXT-MIB", "cslbxVlanAddress"),
        ("CISCO-SLB-EXT-MIB", "cslbxVlanMaskAddressType"),
        ("CISCO-SLB-EXT-MIB", "cslbxVlanMaskAddress"),
        ("CISCO-SLB-EXT-MIB", "cslbxVlanRowStatus"),
        ("CISCO-SLB-EXT-MIB", "cslbxAliasAddrRowStatus"),
        ("CISCO-SLB-EXT-MIB", "cslbxStaticRouteRowStatus"))
)
if mibBuilder.loadTexts:
    cslbxVlansGroup.setStatus("current")

cslbxFaultToleranceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 2, 2, 11)
)
cslbxFaultToleranceGroup.setObjects(
      *(("CISCO-SLB-EXT-MIB", "cslbxFtGroupId"),
        ("CISCO-SLB-EXT-MIB", "cslbxFtVlanId"),
        ("CISCO-SLB-EXT-MIB", "cslbxFtPreempt"),
        ("CISCO-SLB-EXT-MIB", "cslbxFtPriority"),
        ("CISCO-SLB-EXT-MIB", "cslbxFtHeartBeatTimer"),
        ("CISCO-SLB-EXT-MIB", "cslbxFtFailThreshold"),
        ("CISCO-SLB-EXT-MIB", "cslbxFtState"),
        ("CISCO-SLB-EXT-MIB", "cslbxFtStateChangeTime"),
        ("CISCO-SLB-EXT-MIB", "cslbxFtRxHeartBeatMsgs"),
        ("CISCO-SLB-EXT-MIB", "cslbxFtTxHeartBeatMsgs"),
        ("CISCO-SLB-EXT-MIB", "cslbxFtRxUpdateMsgs"),
        ("CISCO-SLB-EXT-MIB", "cslbxFtTxUpdateMsgs"),
        ("CISCO-SLB-EXT-MIB", "cslbxFtRxCoupMsgs"),
        ("CISCO-SLB-EXT-MIB", "cslbxFtTxCoupMsgs"),
        ("CISCO-SLB-EXT-MIB", "cslbxFtRxElectMsgs"),
        ("CISCO-SLB-EXT-MIB", "cslbxFtTxElectMsgs"),
        ("CISCO-SLB-EXT-MIB", "cslbxFtRxConnReplMsgs"),
        ("CISCO-SLB-EXT-MIB", "cslbxFtTxConnReplMsgs"),
        ("CISCO-SLB-EXT-MIB", "cslbxFtRxPackets"),
        ("CISCO-SLB-EXT-MIB", "cslbxFtDropPackets"),
        ("CISCO-SLB-EXT-MIB", "cslbxFtDuplPackets"),
        ("CISCO-SLB-EXT-MIB", "cslbxFtXsumErrPackets"),
        ("CISCO-SLB-EXT-MIB", "cslbxFtBuffErrPackets"),
        ("CISCO-SLB-EXT-MIB", "cslbxFtRowStatus"))
)
if mibBuilder.loadTexts:
    cslbxFaultToleranceGroup.setStatus("current")

cslbxConnsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 2, 2, 12)
)
cslbxConnsGroup.setObjects(
      *(("CISCO-SLB-EXT-MIB", "cslbxConnInDestAddrType"),
        ("CISCO-SLB-EXT-MIB", "cslbxConnInDestAddr"),
        ("CISCO-SLB-EXT-MIB", "cslbxConnInDestPort"),
        ("CISCO-SLB-EXT-MIB", "cslbxConnInSourceAddrType"),
        ("CISCO-SLB-EXT-MIB", "cslbxConnInSourceAddr"),
        ("CISCO-SLB-EXT-MIB", "cslbxConnInSourcePort"),
        ("CISCO-SLB-EXT-MIB", "cslbxConnProtocol"),
        ("CISCO-SLB-EXT-MIB", "cslbxConnOutDestAddrType"),
        ("CISCO-SLB-EXT-MIB", "cslbxConnOutDestAddr"),
        ("CISCO-SLB-EXT-MIB", "cslbxConnOutDestPort"),
        ("CISCO-SLB-EXT-MIB", "cslbxConnOutSourceAddrType"),
        ("CISCO-SLB-EXT-MIB", "cslbxConnOutSourceAddr"),
        ("CISCO-SLB-EXT-MIB", "cslbxConnOutSourcePort"),
        ("CISCO-SLB-EXT-MIB", "cslbxConnState"))
)
if mibBuilder.loadTexts:
    cslbxConnsGroup.setStatus("current")

cslbxXmlConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 2, 2, 13)
)
cslbxXmlConfigGroup.setObjects(
      *(("CISCO-SLB-EXT-MIB", "cslbxXmlConfigEnabled"),
        ("CISCO-SLB-EXT-MIB", "cslbxXmlConfigVlanId"),
        ("CISCO-SLB-EXT-MIB", "cslbxXmlConfigListeningPort"),
        ("CISCO-SLB-EXT-MIB", "cslbxXmlConfigRowStatus"))
)
if mibBuilder.loadTexts:
    cslbxXmlConfigGroup.setStatus("current")

cslbxNotifControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 2, 2, 14)
)
cslbxNotifControlGroup.setObjects(
    ("CISCO-SLB-EXT-MIB", "cslbxFtStateChangeNotifEnabled")
)
if mibBuilder.loadTexts:
    cslbxNotifControlGroup.setStatus("current")

cslbxXmlUserAccessGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 2, 2, 16)
)
cslbxXmlUserAccessGroup.setObjects(
      *(("CISCO-SLB-EXT-MIB", "cslbxXmlConfigUserName"),
        ("CISCO-SLB-EXT-MIB", "cslbxXmlConfigPassword"),
        ("CISCO-SLB-EXT-MIB", "cslbxXmlConfigClientGroupNumber"),
        ("CISCO-SLB-EXT-MIB", "cslbxXmlConfigClientGroupName"))
)
if mibBuilder.loadTexts:
    cslbxXmlUserAccessGroup.setStatus("current")

cslbxOwnerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 2, 2, 17)
)
cslbxOwnerGroup.setObjects(
      *(("CISCO-SLB-EXT-MIB", "cslbxVirtualOwnerName"),
        ("CISCO-SLB-EXT-MIB", "cslbxOwnerContactInfo"),
        ("CISCO-SLB-EXT-MIB", "cslbxOwnerBillingInfo"),
        ("CISCO-SLB-EXT-MIB", "cslbxOwnerMaxConns"),
        ("CISCO-SLB-EXT-MIB", "cslbxOwnerRowStatus"))
)
if mibBuilder.loadTexts:
    cslbxOwnerGroup.setStatus("current")

cslbxBackupServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 2, 2, 18)
)
cslbxBackupServerGroup.setObjects(
      *(("CISCO-SLB-EXT-MIB", "cslbxPolicyBackupFarmName"),
        ("CISCO-SLB-EXT-MIB", "cslbxPolicyBkFarmStickyEnabled"),
        ("CISCO-SLB-EXT-MIB", "cslbxVirtualBackupFarmName"),
        ("CISCO-SLB-EXT-MIB", "cslbxVirtualBkFarmStickyEnabled"))
)
if mibBuilder.loadTexts:
    cslbxBackupServerGroup.setStatus("current")

cslbxScriptedProbeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 2, 2, 19)
)
cslbxScriptedProbeGroup.setObjects(
      *(("CISCO-SLB-EXT-MIB", "cslbxScriptFileUrl"),
        ("CISCO-SLB-EXT-MIB", "cslbxScriptFileRowStatus"),
        ("CISCO-SLB-EXT-MIB", "cslbxScriptTaskScriptName"),
        ("CISCO-SLB-EXT-MIB", "cslbxScriptTaskScriptArguments"),
        ("CISCO-SLB-EXT-MIB", "cslbxScriptTaskRowStatus"))
)
if mibBuilder.loadTexts:
    cslbxScriptedProbeGroup.setStatus("current")

cslbxReverseStickyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 2, 2, 20)
)
cslbxReverseStickyGroup.setObjects(
      *(("CISCO-SLB-EXT-MIB", "cslbxPolicyReverseStickyGroup"),
        ("CISCO-SLB-EXT-MIB", "cslbxVirtualReverseStickyGroup"))
)
if mibBuilder.loadTexts:
    cslbxReverseStickyGroup.setStatus("current")

cslbxVirtualServersExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 2, 2, 22)
)
cslbxVirtualServersExtGroup.setObjects(
      *(("CISCO-SLB-EXT-MIB", "cslbxVirtualMaxConns"),
        ("CISCO-SLB-EXT-MIB", "cslbxVirtualFlowMode"),
        ("CISCO-SLB-EXT-MIB", "cslbxVirtualSSLStickyOffset"),
        ("CISCO-SLB-EXT-MIB", "cslbxVirtualSSLStickyLength"),
        ("CISCO-SLB-EXT-MIB", "cslbxRuleTotalClientOctets"),
        ("CISCO-SLB-EXT-MIB", "cslbxRuleHCTotalClientOctets"),
        ("CISCO-SLB-EXT-MIB", "cslbxRuleTotalServerOctets"),
        ("CISCO-SLB-EXT-MIB", "cslbxRuleHCTotalServerOctets"))
)
if mibBuilder.loadTexts:
    cslbxVirtualServersExtGroup.setStatus("current")

cslbxMapsRev2Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 2, 2, 23)
)
cslbxMapsRev2Group.setObjects(
      *(("CISCO-SLB-EXT-MIB", "cslbxMapType"),
        ("CISCO-SLB-EXT-MIB", "cslbxMapRowStatus"),
        ("CISCO-SLB-EXT-MIB", "cslbxHttpExpressionFieldName"),
        ("CISCO-SLB-EXT-MIB", "cslbxHttpExpressionValue"),
        ("CISCO-SLB-EXT-MIB", "cslbxHttpExpressionRowStatus"),
        ("CISCO-SLB-EXT-MIB", "cslbxHttpExpressionRequestMethod"),
        ("CISCO-SLB-EXT-MIB", "cslbxHttpReturnCodeMaxValue"),
        ("CISCO-SLB-EXT-MIB", "cslbxHttpReturnCodeThreshold"),
        ("CISCO-SLB-EXT-MIB", "cslbxHttpReturnCodeResetTimer"),
        ("CISCO-SLB-EXT-MIB", "cslbxHttpReturnCodeType"),
        ("CISCO-SLB-EXT-MIB", "cslbxHttpReturnCodeRowStatus"))
)
if mibBuilder.loadTexts:
    cslbxMapsRev2Group.setStatus("current")

cslbxServerFarmsExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 2, 2, 24)
)
cslbxServerFarmsExtGroup.setObjects(
      *(("CISCO-SLB-EXT-MIB", "cslbxServerFarmTransparent"),
        ("CISCO-SLB-EXT-MIB", "cslbxServerFarmSlowStart"),
        ("CISCO-SLB-EXT-MIB", "cslbxServerFarmHashHeaderName"),
        ("CISCO-SLB-EXT-MIB", "cslbxServerFarmHashCookieName"),
        ("CISCO-SLB-EXT-MIB", "cslbxServerFarmUrlPatternBegin"),
        ("CISCO-SLB-EXT-MIB", "cslbxServerFarmUrlPatternEnd"),
        ("CISCO-SLB-EXT-MIB", "cslbxServerFarmDescription"),
        ("CISCO-SLB-EXT-MIB", "cslbxServerFarmType"))
)
if mibBuilder.loadTexts:
    cslbxServerFarmsExtGroup.setStatus("deprecated")

cslbxServerFarmsHttpRetCodeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 2, 2, 25)
)
cslbxServerFarmsHttpRetCodeGroup.setObjects(
      *(("CISCO-SLB-EXT-MIB", "cslbxSfarmHttpRetCodeMaxValue"),
        ("CISCO-SLB-EXT-MIB", "cslbxSfarmHttpRetCodeActionType"),
        ("CISCO-SLB-EXT-MIB", "cslbxSfarmHttpRetCodeThreshold"),
        ("CISCO-SLB-EXT-MIB", "cslbxSfarmHttpRetCodeResetTimer"),
        ("CISCO-SLB-EXT-MIB", "cslbxSfarmHttpRetCodeStorageType"),
        ("CISCO-SLB-EXT-MIB", "cslbxSfarmHttpRetCodeRowStatus"))
)
if mibBuilder.loadTexts:
    cslbxServerFarmsHttpRetCodeGroup.setStatus("current")

cslbxStickyGroupsGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 2, 2, 26)
)
cslbxStickyGroupsGroupRev2.setObjects(
      *(("CISCO-SLB-EXT-MIB", "cslbxStickyGroupType"),
        ("CISCO-SLB-EXT-MIB", "cslbxStickyGroupMaskAddressType"),
        ("CISCO-SLB-EXT-MIB", "cslbxStickyGroupMaskAddress"),
        ("CISCO-SLB-EXT-MIB", "cslbxStickyGroupCookieName"),
        ("CISCO-SLB-EXT-MIB", "cslbxStickyGroupStickyTimer"),
        ("CISCO-SLB-EXT-MIB", "cslbxStickyGroupRowStatus"),
        ("CISCO-SLB-EXT-MIB", "cslbxStickyGroupHeaderName"),
        ("CISCO-SLB-EXT-MIB", "cslbxStickyGroupTimeoutActiveConn"),
        ("CISCO-SLB-EXT-MIB", "cslbxStickyGroupReplicate"),
        ("CISCO-SLB-EXT-MIB", "cslbxStickyOffset"),
        ("CISCO-SLB-EXT-MIB", "cslbxStickyLength"))
)
if mibBuilder.loadTexts:
    cslbxStickyGroupsGroupRev2.setStatus("current")

cslbxCookieStickyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 2, 2, 27)
)
cslbxCookieStickyGroup.setObjects(
      *(("CISCO-SLB-EXT-MIB", "cslbxStickyCookieInsertEnable"),
        ("CISCO-SLB-EXT-MIB", "cslbxStickyCookieSecondary"),
        ("CISCO-SLB-EXT-MIB", "cslbxStickyCookieExpiryDate"))
)
if mibBuilder.loadTexts:
    cslbxCookieStickyGroup.setStatus("current")

cslbxStatsHCGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 2, 2, 35)
)
cslbxStatsHCGroup.setObjects(
      *(("CISCO-SLB-EXT-MIB", "cslbxStatsL4PolicyHCConns"),
        ("CISCO-SLB-EXT-MIB", "cslbxStatsL7PolicyHCConns"),
        ("CISCO-SLB-EXT-MIB", "cslbxStatsDroppedL4PolicyHCConns"),
        ("CISCO-SLB-EXT-MIB", "cslbxStatsDroppedL7PolicyHCConns"),
        ("CISCO-SLB-EXT-MIB", "cslbxStatsNoMatchPolicyHCRejects"),
        ("CISCO-SLB-EXT-MIB", "cslbxStatsNoCfgPolicyHCRejects"),
        ("CISCO-SLB-EXT-MIB", "cslbxStatsAclDenyHCRejects"),
        ("CISCO-SLB-EXT-MIB", "cslbxStatsVerMismatchHCRejects"))
)
if mibBuilder.loadTexts:
    cslbxStatsHCGroup.setStatus("current")

cslbxServerFarmStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 2, 2, 36)
)
cslbxServerFarmStatsGroup.setObjects(
      *(("CISCO-SLB-EXT-MIB", "cslbxServerFarmTotalConns"),
        ("CISCO-SLB-EXT-MIB", "cslbxServerFarmCurrConns"),
        ("CISCO-SLB-EXT-MIB", "cslbxServerFarmFailedConns"),
        ("CISCO-SLB-EXT-MIB", "cslbxServerFarmNumOfTimeFailOvers"),
        ("CISCO-SLB-EXT-MIB", "cslbxServerFarmNumOfTimeBkInServs"))
)
if mibBuilder.loadTexts:
    cslbxServerFarmStatsGroup.setStatus("current")

cslbxServerFarmsExtGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 2, 2, 37)
)
cslbxServerFarmsExtGroupRev1.setObjects(
      *(("CISCO-SLB-EXT-MIB", "cslbxServerFarmTransparent"),
        ("CISCO-SLB-EXT-MIB", "cslbxServerFarmSlowStart"),
        ("CISCO-SLB-EXT-MIB", "cslbxServerFarmHashHeaderName"),
        ("CISCO-SLB-EXT-MIB", "cslbxServerFarmHashCookieName"),
        ("CISCO-SLB-EXT-MIB", "cslbxServerFarmUrlPatternBegin"),
        ("CISCO-SLB-EXT-MIB", "cslbxServerFarmUrlPatternEnd"),
        ("CISCO-SLB-EXT-MIB", "cslbxServerFarmDescription"),
        ("CISCO-SLB-EXT-MIB", "cslbxServerFarmType"),
        ("CISCO-SLB-EXT-MIB", "cslbxServerFarmState"))
)
if mibBuilder.loadTexts:
    cslbxServerFarmsExtGroupRev1.setStatus("current")


# Notification objects

cslbxFtStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 0, 1)
)
cslbxFtStateChange.setObjects(
    ("CISCO-SLB-EXT-MIB", "cslbxFtState")
)
if mibBuilder.loadTexts:
    cslbxFtStateChange.setStatus(
        "current"
    )


# Notifications groups

cslbxNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 2, 2, 15)
)
cslbxNotifGroup.setObjects(
    ("CISCO-SLB-EXT-MIB", "cslbxFtStateChange")
)
if mibBuilder.loadTexts:
    cslbxNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cslbxMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cslbxMIBCompliance.setStatus(
        "deprecated"
    )

cslbxMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 2, 1, 2)
)
if mibBuilder.loadTexts:
    cslbxMIBComplianceRev1.setStatus(
        "deprecated"
    )

cslbxMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 2, 1, 3)
)
if mibBuilder.loadTexts:
    cslbxMIBComplianceRev2.setStatus(
        "deprecated"
    )

cslbxMIBComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 254, 2, 1, 4)
)
if mibBuilder.loadTexts:
    cslbxMIBComplianceRev3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SLB-EXT-MIB",
    **{"SlbObjectNameString": SlbObjectNameString,
       "SlbFunctionNameString": SlbFunctionNameString,
       "SlbUrlString": SlbUrlString,
       "SlbRegularExpression": SlbRegularExpression,
       "SlbFailAction": SlbFailAction,
       "SlbIpAdvertise": SlbIpAdvertise,
       "SlbStickyType": SlbStickyType,
       "SlbMapType": SlbMapType,
       "SlbReplicationMode": SlbReplicationMode,
       "SlbProbeAction": SlbProbeAction,
       "SlbVlanType": SlbVlanType,
       "SlbFtState": SlbFtState,
       "SlbDirectionalMode": SlbDirectionalMode,
       "ciscoSlbExtMIB": ciscoSlbExtMIB,
       "ciscoSlbExtMIBNotifs": ciscoSlbExtMIBNotifs,
       "cslbxFtStateChange": cslbxFtStateChange,
       "ciscoSlbExtMIBObjects": ciscoSlbExtMIBObjects,
       "cslbxStats": cslbxStats,
       "cslbxStatsTable": cslbxStatsTable,
       "cslbxStatsTableEntry": cslbxStatsTableEntry,
       "cslbxStatsServerInitConns": cslbxStatsServerInitConns,
       "cslbxStatsServerInitHCConns": cslbxStatsServerInitHCConns,
       "cslbxStatsCurrConnections": cslbxStatsCurrConnections,
       "cslbxStatsCurrServerInitConns": cslbxStatsCurrServerInitConns,
       "cslbxStatsFailedConns": cslbxStatsFailedConns,
       "cslbxStatsFailedServerInitConns": cslbxStatsFailedServerInitConns,
       "cslbxStatsL4PolicyConns": cslbxStatsL4PolicyConns,
       "cslbxStatsL7PolicyConns": cslbxStatsL7PolicyConns,
       "cslbxStatsDroppedL4PolicyConns": cslbxStatsDroppedL4PolicyConns,
       "cslbxStatsDroppedL7PolicyConns": cslbxStatsDroppedL7PolicyConns,
       "cslbxStatsFtpConns": cslbxStatsFtpConns,
       "cslbxStatsHttpRedirectConns": cslbxStatsHttpRedirectConns,
       "cslbxStatsDroppedRedirectConns": cslbxStatsDroppedRedirectConns,
       "cslbxStatsNoMatchPolicyRejects": cslbxStatsNoMatchPolicyRejects,
       "cslbxStatsNoCfgPolicyRejects": cslbxStatsNoCfgPolicyRejects,
       "cslbxStatsNoActiveServerRejects": cslbxStatsNoActiveServerRejects,
       "cslbxStatsAclDenyRejects": cslbxStatsAclDenyRejects,
       "cslbxStatsMaxParseLenRejects": cslbxStatsMaxParseLenRejects,
       "cslbxStatsBadSslFormatRejects": cslbxStatsBadSslFormatRejects,
       "cslbxStatsL7ParserErrorRejects": cslbxStatsL7ParserErrorRejects,
       "cslbxStatsVerMismatchRejects": cslbxStatsVerMismatchRejects,
       "cslbxStatsOutOfMemoryRejects": cslbxStatsOutOfMemoryRejects,
       "cslbxStatsTimedOutConnections": cslbxStatsTimedOutConnections,
       "cslbxStatsTcpChecksumErrorPkts": cslbxStatsTcpChecksumErrorPkts,
       "cslbxStatsIpChecksumErrorPkts": cslbxStatsIpChecksumErrorPkts,
       "cslbxStatsL4PolicyHCConns": cslbxStatsL4PolicyHCConns,
       "cslbxStatsL7PolicyHCConns": cslbxStatsL7PolicyHCConns,
       "cslbxStatsDroppedL4PolicyHCConns": cslbxStatsDroppedL4PolicyHCConns,
       "cslbxStatsDroppedL7PolicyHCConns": cslbxStatsDroppedL7PolicyHCConns,
       "cslbxStatsNoMatchPolicyHCRejects": cslbxStatsNoMatchPolicyHCRejects,
       "cslbxStatsNoCfgPolicyHCRejects": cslbxStatsNoCfgPolicyHCRejects,
       "cslbxStatsAclDenyHCRejects": cslbxStatsAclDenyHCRejects,
       "cslbxStatsVerMismatchHCRejects": cslbxStatsVerMismatchHCRejects,
       "cslbxServerFarms": cslbxServerFarms,
       "cslbxServerFarmTable": cslbxServerFarmTable,
       "cslbxServerFarmTableEntry": cslbxServerFarmTableEntry,
       "cslbxServerFarmHashMaskAddrType": cslbxServerFarmHashMaskAddrType,
       "cslbxServerFarmHashMaskAddr": cslbxServerFarmHashMaskAddr,
       "cslbxServerFarmClientNatPool": cslbxServerFarmClientNatPool,
       "cslbxServerFarmFailAction": cslbxServerFarmFailAction,
       "cslbxServerFarmHttpReturnCodeMap": cslbxServerFarmHttpReturnCodeMap,
       "cslbxServerFarmInFailedThreshold": cslbxServerFarmInFailedThreshold,
       "cslbxServerFarmInbandResetTimer": cslbxServerFarmInbandResetTimer,
       "cslbxServerFarmTransparent": cslbxServerFarmTransparent,
       "cslbxServerFarmSlowStart": cslbxServerFarmSlowStart,
       "cslbxServerFarmHashHeaderName": cslbxServerFarmHashHeaderName,
       "cslbxServerFarmHashCookieName": cslbxServerFarmHashCookieName,
       "cslbxServerFarmUrlPatternBegin": cslbxServerFarmUrlPatternBegin,
       "cslbxServerFarmUrlPatternEnd": cslbxServerFarmUrlPatternEnd,
       "cslbxServerFarmDescription": cslbxServerFarmDescription,
       "cslbxServerFarmType": cslbxServerFarmType,
       "cslbxServerFarmState": cslbxServerFarmState,
       "cslbxRedirectSvrTable": cslbxRedirectSvrTable,
       "cslbxRedirectSvrTableEntry": cslbxRedirectSvrTableEntry,
       "cslbxRedirectSvrFarmName": cslbxRedirectSvrFarmName,
       "cslbxRedirectSvrName": cslbxRedirectSvrName,
       "cslbxRedirectSvrRelocationStr": cslbxRedirectSvrRelocationStr,
       "cslbxRedirectSvrBackupString": cslbxRedirectSvrBackupString,
       "cslbxRedirectSvrRedirectCode": cslbxRedirectSvrRedirectCode,
       "cslbxRedirectSvrRedirectPort": cslbxRedirectSvrRedirectPort,
       "cslbxRedirectSvrState": cslbxRedirectSvrState,
       "cslbxRedirectSvrNumberOfConns": cslbxRedirectSvrNumberOfConns,
       "cslbxRedirectSvrMaxConns": cslbxRedirectSvrMaxConns,
       "cslbxRedirectSvrAdminWeight": cslbxRedirectSvrAdminWeight,
       "cslbxRedirectSvrOperWeight": cslbxRedirectSvrOperWeight,
       "cslbxRedirectSvrMetric": cslbxRedirectSvrMetric,
       "cslbxRedirectSvrTotalConns": cslbxRedirectSvrTotalConns,
       "cslbxRedirectSvrHCTotalConns": cslbxRedirectSvrHCTotalConns,
       "cslbxRedirectSvrRowStatus": cslbxRedirectSvrRowStatus,
       "cslbxServerFarmProbeTable": cslbxServerFarmProbeTable,
       "cslbxServerFarmProbeTableEntry": cslbxServerFarmProbeTableEntry,
       "cslbxServerFarmProbeFarmName": cslbxServerFarmProbeFarmName,
       "cslbxServerFarmProbeProbeName": cslbxServerFarmProbeProbeName,
       "cslbxServerFarmProbeRowStatus": cslbxServerFarmProbeRowStatus,
       "cslbxSfarmHttpReturnCodeTable": cslbxSfarmHttpReturnCodeTable,
       "cslbxSfarmHttpReturnCodeEntry": cslbxSfarmHttpReturnCodeEntry,
       "cslbxSfarmHttpRetCodeMinValue": cslbxSfarmHttpRetCodeMinValue,
       "cslbxSfarmHttpRetCodeMaxValue": cslbxSfarmHttpRetCodeMaxValue,
       "cslbxSfarmHttpRetCodeActionType": cslbxSfarmHttpRetCodeActionType,
       "cslbxSfarmHttpRetCodeThreshold": cslbxSfarmHttpRetCodeThreshold,
       "cslbxSfarmHttpRetCodeResetTimer": cslbxSfarmHttpRetCodeResetTimer,
       "cslbxSfarmHttpRetCodeStorageType": cslbxSfarmHttpRetCodeStorageType,
       "cslbxSfarmHttpRetCodeRowStatus": cslbxSfarmHttpRetCodeRowStatus,
       "cslbxServerFarmStatsTable": cslbxServerFarmStatsTable,
       "cslbxServerFarmStatsEntry": cslbxServerFarmStatsEntry,
       "cslbxServerFarmTotalConns": cslbxServerFarmTotalConns,
       "cslbxServerFarmCurrConns": cslbxServerFarmCurrConns,
       "cslbxServerFarmFailedConns": cslbxServerFarmFailedConns,
       "cslbxServerFarmNumOfTimeFailOvers": cslbxServerFarmNumOfTimeFailOvers,
       "cslbxServerFarmNumOfTimeBkInServs": cslbxServerFarmNumOfTimeBkInServs,
       "cslbxClientNatPools": cslbxClientNatPools,
       "cslbxNatPoolTable": cslbxNatPoolTable,
       "cslbxNatPoolEntry": cslbxNatPoolEntry,
       "cslbxNatPoolName": cslbxNatPoolName,
       "cslbxNatPoolStartAddressType": cslbxNatPoolStartAddressType,
       "cslbxNatPoolStartAddress": cslbxNatPoolStartAddress,
       "cslbxNatPoolEndAddressType": cslbxNatPoolEndAddressType,
       "cslbxNatPoolEndAddress": cslbxNatPoolEndAddress,
       "cslbxNatPoolRowStatus": cslbxNatPoolRowStatus,
       "cslbxStickyObjects": cslbxStickyObjects,
       "cslbxStickyGroupTable": cslbxStickyGroupTable,
       "cslbxStickyGroupEntry": cslbxStickyGroupEntry,
       "cslbxStickyGroupId": cslbxStickyGroupId,
       "cslbxStickyGroupType": cslbxStickyGroupType,
       "cslbxStickyGroupMaskAddressType": cslbxStickyGroupMaskAddressType,
       "cslbxStickyGroupMaskAddress": cslbxStickyGroupMaskAddress,
       "cslbxStickyGroupCookieName": cslbxStickyGroupCookieName,
       "cslbxStickyGroupStickyTimer": cslbxStickyGroupStickyTimer,
       "cslbxStickyGroupRowStatus": cslbxStickyGroupRowStatus,
       "cslbxStickyGroupHeaderName": cslbxStickyGroupHeaderName,
       "cslbxStickyGroupTimeoutActiveConn": cslbxStickyGroupTimeoutActiveConn,
       "cslbxStickyGroupReplicate": cslbxStickyGroupReplicate,
       "cslbxStickyObjectTable": cslbxStickyObjectTable,
       "cslbxStickyObjectTableEntry": cslbxStickyObjectTableEntry,
       "cslbxStickyObjectIndex": cslbxStickyObjectIndex,
       "cslbxStickyObjectGroupId": cslbxStickyObjectGroupId,
       "cslbxStickyObjectType": cslbxStickyObjectType,
       "cslbxStickyObjectSourceInfo": cslbxStickyObjectSourceInfo,
       "cslbxStickyObjectRealAddressType": cslbxStickyObjectRealAddressType,
       "cslbxStickyObjectRealAddress": cslbxStickyObjectRealAddress,
       "cslbxStickyObjectRealPort": cslbxStickyObjectRealPort,
       "cslbxStickyGroupExtTable": cslbxStickyGroupExtTable,
       "cslbxStickyGroupExtEntry": cslbxStickyGroupExtEntry,
       "cslbxStickyOffset": cslbxStickyOffset,
       "cslbxStickyLength": cslbxStickyLength,
       "cslbxStickyCookieSecondary": cslbxStickyCookieSecondary,
       "cslbxStickyCookieInsertEnable": cslbxStickyCookieInsertEnable,
       "cslbxStickyCookieExpiryDate": cslbxStickyCookieExpiryDate,
       "cslbxMaps": cslbxMaps,
       "cslbxMapTable": cslbxMapTable,
       "cslbxMapTableEntry": cslbxMapTableEntry,
       "cslbxMapName": cslbxMapName,
       "cslbxMapType": cslbxMapType,
       "cslbxMapRowStatus": cslbxMapRowStatus,
       "cslbxHttpExpressionTable": cslbxHttpExpressionTable,
       "cslbxHttpExpressionTableEntry": cslbxHttpExpressionTableEntry,
       "cslbxHttpExpressionMapName": cslbxHttpExpressionMapName,
       "cslbxHttpExpressionIndex": cslbxHttpExpressionIndex,
       "cslbxHttpExpressionFieldName": cslbxHttpExpressionFieldName,
       "cslbxHttpExpressionValue": cslbxHttpExpressionValue,
       "cslbxHttpExpressionRowStatus": cslbxHttpExpressionRowStatus,
       "cslbxHttpExpressionRequestMethod": cslbxHttpExpressionRequestMethod,
       "cslbxHttpReturnCodeTable": cslbxHttpReturnCodeTable,
       "cslbxHttpReturnCodeEntry": cslbxHttpReturnCodeEntry,
       "cslbxHttpReturnCodeMapName": cslbxHttpReturnCodeMapName,
       "cslbxHttpReturnCodeMinValue": cslbxHttpReturnCodeMinValue,
       "cslbxHttpReturnCodeMaxValue": cslbxHttpReturnCodeMaxValue,
       "cslbxHttpReturnCodeThreshold": cslbxHttpReturnCodeThreshold,
       "cslbxHttpReturnCodeResetTimer": cslbxHttpReturnCodeResetTimer,
       "cslbxHttpReturnCodeType": cslbxHttpReturnCodeType,
       "cslbxHttpReturnCodeRowStatus": cslbxHttpReturnCodeRowStatus,
       "cslbxServerProbes": cslbxServerProbes,
       "cslbxPolicies": cslbxPolicies,
       "cslbxPolicyTable": cslbxPolicyTable,
       "cslbxPolicyTableEntry": cslbxPolicyTableEntry,
       "cslbxPolicyName": cslbxPolicyName,
       "cslbxPolicyClientGroupNumber": cslbxPolicyClientGroupNumber,
       "cslbxPolicyClientGroupName": cslbxPolicyClientGroupName,
       "cslbxPolicyUrlMap": cslbxPolicyUrlMap,
       "cslbxPolicyCookieMap": cslbxPolicyCookieMap,
       "cslbxPolicyGenericHeaderMap": cslbxPolicyGenericHeaderMap,
       "cslbxPolicyStickyGroup": cslbxPolicyStickyGroup,
       "cslbxPolicyDscpEnabled": cslbxPolicyDscpEnabled,
       "cslbxPolicyDscpStamping": cslbxPolicyDscpStamping,
       "cslbxPolicyFarmName": cslbxPolicyFarmName,
       "cslbxPolicyRowStatus": cslbxPolicyRowStatus,
       "cslbxPolicyBackupFarmName": cslbxPolicyBackupFarmName,
       "cslbxPolicyBkFarmStickyEnabled": cslbxPolicyBkFarmStickyEnabled,
       "cslbxPolicyReverseStickyGroup": cslbxPolicyReverseStickyGroup,
       "cslbxVirtualServers": cslbxVirtualServers,
       "cslbxVirtualServerTable": cslbxVirtualServerTable,
       "cslbxVirtualServerTableEntry": cslbxVirtualServerTableEntry,
       "cslbxVirtualAdvertiseOption": cslbxVirtualAdvertiseOption,
       "cslbxVirtualVlanId": cslbxVirtualVlanId,
       "cslbxVirtualReplicationMode": cslbxVirtualReplicationMode,
       "cslbxVirtualPendingTimer": cslbxVirtualPendingTimer,
       "cslbxVirtualL7MaxParseLength": cslbxVirtualL7MaxParseLength,
       "cslbxVirtualHttpPersistenceSlb": cslbxVirtualHttpPersistenceSlb,
       "cslbxVirtualURLHashBeginString": cslbxVirtualURLHashBeginString,
       "cslbxVirtualURLHashEndString": cslbxVirtualURLHashEndString,
       "cslbxVirtualMaxConns": cslbxVirtualMaxConns,
       "cslbxVirtualOwnerName": cslbxVirtualOwnerName,
       "cslbxVirtualFlowMode": cslbxVirtualFlowMode,
       "cslbxVirtualSSLStickyOffset": cslbxVirtualSSLStickyOffset,
       "cslbxVirtualSSLStickyLength": cslbxVirtualSSLStickyLength,
       "cslbxVirtualReverseStickyGroup": cslbxVirtualReverseStickyGroup,
       "cslbxVirtualBackupFarmName": cslbxVirtualBackupFarmName,
       "cslbxVirtualBkFarmStickyEnabled": cslbxVirtualBkFarmStickyEnabled,
       "cslbxRuleTable": cslbxRuleTable,
       "cslbxRuleEntry": cslbxRuleEntry,
       "cslbxRuleVirtualServerName": cslbxRuleVirtualServerName,
       "cslbxRulePolicyName": cslbxRulePolicyName,
       "cslbxRuleCurrentConnections": cslbxRuleCurrentConnections,
       "cslbxRuleTotalConnections": cslbxRuleTotalConnections,
       "cslbxRuleHCTotalConnections": cslbxRuleHCTotalConnections,
       "cslbxRuleTotalClientPackets": cslbxRuleTotalClientPackets,
       "cslbxRuleHCTotalClientPackets": cslbxRuleHCTotalClientPackets,
       "cslbxRuleTotalServerPackets": cslbxRuleTotalServerPackets,
       "cslbxRuleHCTotalServerPackets": cslbxRuleHCTotalServerPackets,
       "cslbxRuleRowStatus": cslbxRuleRowStatus,
       "cslbxRuleTotalClientOctets": cslbxRuleTotalClientOctets,
       "cslbxRuleHCTotalClientOctets": cslbxRuleHCTotalClientOctets,
       "cslbxRuleTotalServerOctets": cslbxRuleTotalServerOctets,
       "cslbxRuleHCTotalServerOctets": cslbxRuleHCTotalServerOctets,
       "cslbxVlans": cslbxVlans,
       "cslbxVlanTable": cslbxVlanTable,
       "cslbxVlanEntry": cslbxVlanEntry,
       "cslbxVlanId": cslbxVlanId,
       "cslbxVlanType": cslbxVlanType,
       "cslbxVlanAddressType": cslbxVlanAddressType,
       "cslbxVlanAddress": cslbxVlanAddress,
       "cslbxVlanMaskAddressType": cslbxVlanMaskAddressType,
       "cslbxVlanMaskAddress": cslbxVlanMaskAddress,
       "cslbxVlanRowStatus": cslbxVlanRowStatus,
       "cslbxAliasAddrTable": cslbxAliasAddrTable,
       "cslbxAliasAddrEntry": cslbxAliasAddrEntry,
       "cslbxAliasAddrVlanId": cslbxAliasAddrVlanId,
       "cslbxAliasAddrAddressType": cslbxAliasAddrAddressType,
       "cslbxAliasAddrAddress": cslbxAliasAddrAddress,
       "cslbxAliasAddrRowStatus": cslbxAliasAddrRowStatus,
       "cslbxStaticRouteTable": cslbxStaticRouteTable,
       "cslbxStaticRouteEntry": cslbxStaticRouteEntry,
       "cslbxStaticRouteVlanId": cslbxStaticRouteVlanId,
       "cslbxStaticRouteSubnetAddrType": cslbxStaticRouteSubnetAddrType,
       "cslbxStaticRouteSubnetAddr": cslbxStaticRouteSubnetAddr,
       "cslbxStaticRouteMaskAddrType": cslbxStaticRouteMaskAddrType,
       "cslbxStaticRouteMaskAddr": cslbxStaticRouteMaskAddr,
       "cslbxStaticRouteGatewayAddrType": cslbxStaticRouteGatewayAddrType,
       "cslbxStaticRouteGatewayAddr": cslbxStaticRouteGatewayAddr,
       "cslbxStaticRouteRowStatus": cslbxStaticRouteRowStatus,
       "cslbxFaultTolerance": cslbxFaultTolerance,
       "cslbxFtTable": cslbxFtTable,
       "cslbxFtTableEntry": cslbxFtTableEntry,
       "cslbxFtGroupId": cslbxFtGroupId,
       "cslbxFtVlanId": cslbxFtVlanId,
       "cslbxFtPreempt": cslbxFtPreempt,
       "cslbxFtPriority": cslbxFtPriority,
       "cslbxFtHeartBeatTimer": cslbxFtHeartBeatTimer,
       "cslbxFtFailThreshold": cslbxFtFailThreshold,
       "cslbxFtState": cslbxFtState,
       "cslbxFtStateChangeTime": cslbxFtStateChangeTime,
       "cslbxFtRxHeartBeatMsgs": cslbxFtRxHeartBeatMsgs,
       "cslbxFtTxHeartBeatMsgs": cslbxFtTxHeartBeatMsgs,
       "cslbxFtRxUpdateMsgs": cslbxFtRxUpdateMsgs,
       "cslbxFtTxUpdateMsgs": cslbxFtTxUpdateMsgs,
       "cslbxFtRxCoupMsgs": cslbxFtRxCoupMsgs,
       "cslbxFtTxCoupMsgs": cslbxFtTxCoupMsgs,
       "cslbxFtRxElectMsgs": cslbxFtRxElectMsgs,
       "cslbxFtTxElectMsgs": cslbxFtTxElectMsgs,
       "cslbxFtRxConnReplMsgs": cslbxFtRxConnReplMsgs,
       "cslbxFtTxConnReplMsgs": cslbxFtTxConnReplMsgs,
       "cslbxFtRxPackets": cslbxFtRxPackets,
       "cslbxFtDropPackets": cslbxFtDropPackets,
       "cslbxFtDuplPackets": cslbxFtDuplPackets,
       "cslbxFtXsumErrPackets": cslbxFtXsumErrPackets,
       "cslbxFtBuffErrPackets": cslbxFtBuffErrPackets,
       "cslbxFtRowStatus": cslbxFtRowStatus,
       "cslbxXmlConfig": cslbxXmlConfig,
       "cslbxXmlConfigTable": cslbxXmlConfigTable,
       "cslbxXmlConfigTableEntry": cslbxXmlConfigTableEntry,
       "cslbxXmlConfigEnabled": cslbxXmlConfigEnabled,
       "cslbxXmlConfigVlanId": cslbxXmlConfigVlanId,
       "cslbxXmlConfigListeningPort": cslbxXmlConfigListeningPort,
       "cslbxXmlConfigRowStatus": cslbxXmlConfigRowStatus,
       "cslbxXmlConfigUserName": cslbxXmlConfigUserName,
       "cslbxXmlConfigPassword": cslbxXmlConfigPassword,
       "cslbxXmlConfigClientGroupNumber": cslbxXmlConfigClientGroupNumber,
       "cslbxXmlConfigClientGroupName": cslbxXmlConfigClientGroupName,
       "cslbxConnections": cslbxConnections,
       "cslbxConnTable": cslbxConnTable,
       "cslbxConnTableEntry": cslbxConnTableEntry,
       "cslbxConnIndex": cslbxConnIndex,
       "cslbxConnInDestAddrType": cslbxConnInDestAddrType,
       "cslbxConnInDestAddr": cslbxConnInDestAddr,
       "cslbxConnInDestPort": cslbxConnInDestPort,
       "cslbxConnInSourceAddrType": cslbxConnInSourceAddrType,
       "cslbxConnInSourceAddr": cslbxConnInSourceAddr,
       "cslbxConnInSourcePort": cslbxConnInSourcePort,
       "cslbxConnProtocol": cslbxConnProtocol,
       "cslbxConnOutDestAddrType": cslbxConnOutDestAddrType,
       "cslbxConnOutDestAddr": cslbxConnOutDestAddr,
       "cslbxConnOutDestPort": cslbxConnOutDestPort,
       "cslbxConnOutSourceAddrType": cslbxConnOutSourceAddrType,
       "cslbxConnOutSourceAddr": cslbxConnOutSourceAddr,
       "cslbxConnOutSourcePort": cslbxConnOutSourcePort,
       "cslbxConnState": cslbxConnState,
       "cslbxNotifObjects": cslbxNotifObjects,
       "cslbxFtStateChangeNotifEnabled": cslbxFtStateChangeNotifEnabled,
       "cslbxOwnerObjects": cslbxOwnerObjects,
       "cslbxOwnerTable": cslbxOwnerTable,
       "cslbxOwnerTableEntry": cslbxOwnerTableEntry,
       "cslbxOwnerName": cslbxOwnerName,
       "cslbxOwnerContactInfo": cslbxOwnerContactInfo,
       "cslbxOwnerBillingInfo": cslbxOwnerBillingInfo,
       "cslbxOwnerMaxConns": cslbxOwnerMaxConns,
       "cslbxOwnerRowStatus": cslbxOwnerRowStatus,
       "cslbxScriptObjects": cslbxScriptObjects,
       "cslbxScriptFileTable": cslbxScriptFileTable,
       "cslbxScriptFileTableEntry": cslbxScriptFileTableEntry,
       "cslbxScriptFileIndex": cslbxScriptFileIndex,
       "cslbxScriptFileUrl": cslbxScriptFileUrl,
       "cslbxScriptFileRowStatus": cslbxScriptFileRowStatus,
       "cslbxScriptTaskTable": cslbxScriptTaskTable,
       "cslbxScriptTaskTableEntry": cslbxScriptTaskTableEntry,
       "cslbxScriptTaskIndex": cslbxScriptTaskIndex,
       "cslbxScriptTaskScriptName": cslbxScriptTaskScriptName,
       "cslbxScriptTaskScriptArguments": cslbxScriptTaskScriptArguments,
       "cslbxScriptTaskRowStatus": cslbxScriptTaskRowStatus,
       "ciscoSlbExtMIBConform": ciscoSlbExtMIBConform,
       "cslbxMIBCompliances": cslbxMIBCompliances,
       "cslbxMIBCompliance": cslbxMIBCompliance,
       "cslbxMIBComplianceRev1": cslbxMIBComplianceRev1,
       "cslbxMIBComplianceRev2": cslbxMIBComplianceRev2,
       "cslbxMIBComplianceRev3": cslbxMIBComplianceRev3,
       "cslbxMIBGroups": cslbxMIBGroups,
       "cslbxStatsGroup": cslbxStatsGroup,
       "cslbxServerFarmsGroup": cslbxServerFarmsGroup,
       "cslbxClientNatPoolsGroup": cslbxClientNatPoolsGroup,
       "cslbxStickyGroupsGroup": cslbxStickyGroupsGroup,
       "cslbxStickyObjectsGroup": cslbxStickyObjectsGroup,
       "cslbxMapsGroup": cslbxMapsGroup,
       "cslbxPoliciesGroup": cslbxPoliciesGroup,
       "cslbxVirtualServersGroup": cslbxVirtualServersGroup,
       "cslbxVlansGroup": cslbxVlansGroup,
       "cslbxFaultToleranceGroup": cslbxFaultToleranceGroup,
       "cslbxConnsGroup": cslbxConnsGroup,
       "cslbxXmlConfigGroup": cslbxXmlConfigGroup,
       "cslbxNotifControlGroup": cslbxNotifControlGroup,
       "cslbxNotifGroup": cslbxNotifGroup,
       "cslbxXmlUserAccessGroup": cslbxXmlUserAccessGroup,
       "cslbxOwnerGroup": cslbxOwnerGroup,
       "cslbxBackupServerGroup": cslbxBackupServerGroup,
       "cslbxScriptedProbeGroup": cslbxScriptedProbeGroup,
       "cslbxReverseStickyGroup": cslbxReverseStickyGroup,
       "cslbxVirtualServersExtGroup": cslbxVirtualServersExtGroup,
       "cslbxMapsRev2Group": cslbxMapsRev2Group,
       "cslbxServerFarmsExtGroup": cslbxServerFarmsExtGroup,
       "cslbxServerFarmsHttpRetCodeGroup": cslbxServerFarmsHttpRetCodeGroup,
       "cslbxStickyGroupsGroupRev2": cslbxStickyGroupsGroupRev2,
       "cslbxCookieStickyGroup": cslbxCookieStickyGroup,
       "cslbxStatsHCGroup": cslbxStatsHCGroup,
       "cslbxServerFarmStatsGroup": cslbxServerFarmStatsGroup,
       "cslbxServerFarmsExtGroupRev1": cslbxServerFarmsExtGroupRev1}
)
