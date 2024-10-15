# SNMP MIB module (CISCO-CDMA-PDSN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-CDMA-PDSN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:57:12 2024
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(ZeroBasedCounter32,) = mibBuilder.importSymbols(
    "RMON2-MIB",
    "ZeroBasedCounter32")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoCdmaPdsnMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 157)
)
ciscoCdmaPdsnMIB.setRevisions(
        ("2009-08-05 00:00",
         "2005-02-02 00:00",
         "2003-08-26 00:00",
         "2002-09-09 00:00",
         "2002-02-19 00:00",
         "2001-10-18 00:00",
         "2001-04-10 00:00",
         "2001-01-22 00:00",
         "2000-03-06 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CCdmaMsidType(Integer32, TextualConvention):
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
        *(("imsi", 2),
          ("irm", 4),
          ("min", 3),
          ("other", 1))
    )



class CCdmaSystemStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("insufficientResources", 4),
          ("testing", 3),
          ("unknown", 0),
          ("up", 1))
    )



class CCdmaServiceAffectedLevel(Integer32, TextualConvention):
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
        *(("critical", 4),
          ("major", 3),
          ("minor", 2),
          ("warning", 1))
    )



class CCdmaServiceOption(Unsigned32, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_CiscoCdmaPdsnMIBObjects_ObjectIdentity = ObjectIdentity
ciscoCdmaPdsnMIBObjects = _CiscoCdmaPdsnMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1)
)
_CCdmaSystemInfo_ObjectIdentity = ObjectIdentity
cCdmaSystemInfo = _CCdmaSystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 1)
)
_CCdmaSessionTotal_Type = Gauge32
_CCdmaSessionTotal_Object = MibScalar
cCdmaSessionTotal = _CCdmaSessionTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 1, 1),
    _CCdmaSessionTotal_Type()
)
cCdmaSessionTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaSessionTotal.setStatus("current")
_CCdmaSessionMaxAllowed_Type = Unsigned32
_CCdmaSessionMaxAllowed_Object = MibScalar
cCdmaSessionMaxAllowed = _CCdmaSessionMaxAllowed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 1, 2),
    _CCdmaSessionMaxAllowed_Type()
)
cCdmaSessionMaxAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaSessionMaxAllowed.setStatus("current")
_CCdmaPcfTotal_Type = Gauge32
_CCdmaPcfTotal_Object = MibScalar
cCdmaPcfTotal = _CCdmaPcfTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 1, 3),
    _CCdmaPcfTotal_Type()
)
cCdmaPcfTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPcfTotal.setStatus("current")
_CCdmaPcfMaxAllowed_Type = Unsigned32
_CCdmaPcfMaxAllowed_Object = MibScalar
cCdmaPcfMaxAllowed = _CCdmaPcfMaxAllowed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 1, 4),
    _CCdmaPcfMaxAllowed_Type()
)
cCdmaPcfMaxAllowed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cCdmaPcfMaxAllowed.setStatus("current")
_CCdmaSimpleIpFlowTotal_Type = Gauge32
_CCdmaSimpleIpFlowTotal_Object = MibScalar
cCdmaSimpleIpFlowTotal = _CCdmaSimpleIpFlowTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 1, 5),
    _CCdmaSimpleIpFlowTotal_Type()
)
cCdmaSimpleIpFlowTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaSimpleIpFlowTotal.setStatus("current")
_CCdmaMobileIpFlowTotal_Type = Gauge32
_CCdmaMobileIpFlowTotal_Object = MibScalar
cCdmaMobileIpFlowTotal = _CCdmaMobileIpFlowTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 1, 6),
    _CCdmaMobileIpFlowTotal_Type()
)
cCdmaMobileIpFlowTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaMobileIpFlowTotal.setStatus("current")
_CCdmaProxyMobileIpFlowTotal_Type = Gauge32
_CCdmaProxyMobileIpFlowTotal_Object = MibScalar
cCdmaProxyMobileIpFlowTotal = _CCdmaProxyMobileIpFlowTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 1, 7),
    _CCdmaProxyMobileIpFlowTotal_Type()
)
cCdmaProxyMobileIpFlowTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaProxyMobileIpFlowTotal.setStatus("current")
_CCdmaSessionFailTotal_Type = ZeroBasedCounter32
_CCdmaSessionFailTotal_Object = MibScalar
cCdmaSessionFailTotal = _CCdmaSessionFailTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 1, 8),
    _CCdmaSessionFailTotal_Type()
)
cCdmaSessionFailTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaSessionFailTotal.setStatus("current")


class _CCdmaServingPdsnHostname_Type(SnmpAdminString):
    """Custom type cCdmaServingPdsnHostname based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CCdmaServingPdsnHostname_Type.__name__ = "SnmpAdminString"
_CCdmaServingPdsnHostname_Object = MibScalar
cCdmaServingPdsnHostname = _CCdmaServingPdsnHostname_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 1, 9),
    _CCdmaServingPdsnHostname_Type()
)
cCdmaServingPdsnHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaServingPdsnHostname.setStatus("current")
_CCdmaSessionPdsnAuthenTimer_Type = TimeTicks
_CCdmaSessionPdsnAuthenTimer_Object = MibScalar
cCdmaSessionPdsnAuthenTimer = _CCdmaSessionPdsnAuthenTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 1, 10),
    _CCdmaSessionPdsnAuthenTimer_Type()
)
cCdmaSessionPdsnAuthenTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cCdmaSessionPdsnAuthenTimer.setStatus("current")


class _CCdmaSessionPdsnMaxFailHistory_Type(Unsigned32):
    """Custom type cCdmaSessionPdsnMaxFailHistory based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_CCdmaSessionPdsnMaxFailHistory_Type.__name__ = "Unsigned32"
_CCdmaSessionPdsnMaxFailHistory_Object = MibScalar
cCdmaSessionPdsnMaxFailHistory = _CCdmaSessionPdsnMaxFailHistory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 1, 11),
    _CCdmaSessionPdsnMaxFailHistory_Type()
)
cCdmaSessionPdsnMaxFailHistory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cCdmaSessionPdsnMaxFailHistory.setStatus("current")


class _CCdmaSessionMaxNotifEnabled_Type(TruthValue):
    """Custom type cCdmaSessionMaxNotifEnabled based on TruthValue"""


_CCdmaSessionMaxNotifEnabled_Object = MibScalar
cCdmaSessionMaxNotifEnabled = _CCdmaSessionMaxNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 1, 12),
    _CCdmaSessionMaxNotifEnabled_Type()
)
cCdmaSessionMaxNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cCdmaSessionMaxNotifEnabled.setStatus("current")


class _CCdmaPcfMaxAllowedNotifEnabled_Type(TruthValue):
    """Custom type cCdmaPcfMaxAllowedNotifEnabled based on TruthValue"""


_CCdmaPcfMaxAllowedNotifEnabled_Object = MibScalar
cCdmaPcfMaxAllowedNotifEnabled = _CCdmaPcfMaxAllowedNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 1, 13),
    _CCdmaPcfMaxAllowedNotifEnabled_Type()
)
cCdmaPcfMaxAllowedNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cCdmaPcfMaxAllowedNotifEnabled.setStatus("current")


class _CCdmaFormatErrorNotifEnabled_Type(TruthValue):
    """Custom type cCdmaFormatErrorNotifEnabled based on TruthValue"""


_CCdmaFormatErrorNotifEnabled_Object = MibScalar
cCdmaFormatErrorNotifEnabled = _CCdmaFormatErrorNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 1, 14),
    _CCdmaFormatErrorNotifEnabled_Type()
)
cCdmaFormatErrorNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cCdmaFormatErrorNotifEnabled.setStatus("obsolete")


class _CCdmaRegReqFailedNotifEnabled_Type(TruthValue):
    """Custom type cCdmaRegReqFailedNotifEnabled based on TruthValue"""


_CCdmaRegReqFailedNotifEnabled_Object = MibScalar
cCdmaRegReqFailedNotifEnabled = _CCdmaRegReqFailedNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 1, 15),
    _CCdmaRegReqFailedNotifEnabled_Type()
)
cCdmaRegReqFailedNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cCdmaRegReqFailedNotifEnabled.setStatus("current")
_CCdmaSystemVersion_Type = SnmpAdminString
_CCdmaSystemVersion_Object = MibScalar
cCdmaSystemVersion = _CCdmaSystemVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 1, 16),
    _CCdmaSystemVersion_Type()
)
cCdmaSystemVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaSystemVersion.setStatus("current")
_CCdmaSystemStatus_Type = CCdmaSystemStatus
_CCdmaSystemStatus_Object = MibScalar
cCdmaSystemStatus = _CCdmaSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 1, 17),
    _CCdmaSystemStatus_Type()
)
cCdmaSystemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaSystemStatus.setStatus("current")
_CCdmaActiveSessions_Type = Gauge32
_CCdmaActiveSessions_Object = MibScalar
cCdmaActiveSessions = _CCdmaActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 1, 18),
    _CCdmaActiveSessions_Type()
)
cCdmaActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaActiveSessions.setStatus("current")
_CCdmaDormantSessions_Type = Gauge32
_CCdmaDormantSessions_Object = MibScalar
cCdmaDormantSessions = _CCdmaDormantSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 1, 19),
    _CCdmaDormantSessions_Type()
)
cCdmaDormantSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaDormantSessions.setStatus("current")
_CCdmaSrEnabled_Type = TruthValue
_CCdmaSrEnabled_Object = MibScalar
cCdmaSrEnabled = _CCdmaSrEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 1, 20),
    _CCdmaSrEnabled_Type()
)
cCdmaSrEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaSrEnabled.setStatus("current")
_CCdmaPPPoGRESessionTotal_Type = Gauge32
_CCdmaPPPoGRESessionTotal_Object = MibScalar
cCdmaPPPoGRESessionTotal = _CCdmaPPPoGRESessionTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 1, 21),
    _CCdmaPPPoGRESessionTotal_Type()
)
cCdmaPPPoGRESessionTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPPPoGRESessionTotal.setStatus("current")
_CCdmaHDLCoGRESessionTotal_Type = Gauge32
_CCdmaHDLCoGRESessionTotal_Object = MibScalar
cCdmaHDLCoGRESessionTotal = _CCdmaHDLCoGRESessionTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 1, 22),
    _CCdmaHDLCoGRESessionTotal_Type()
)
cCdmaHDLCoGRESessionTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaHDLCoGRESessionTotal.setStatus("current")
_CCdmaEstablishedSessions_Type = ZeroBasedCounter32
_CCdmaEstablishedSessions_Object = MibScalar
cCdmaEstablishedSessions = _CCdmaEstablishedSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 1, 23),
    _CCdmaEstablishedSessions_Type()
)
cCdmaEstablishedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaEstablishedSessions.setStatus("current")
_CCdmaReleasedSessions_Type = ZeroBasedCounter32
_CCdmaReleasedSessions_Object = MibScalar
cCdmaReleasedSessions = _CCdmaReleasedSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 1, 24),
    _CCdmaReleasedSessions_Type()
)
cCdmaReleasedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaReleasedSessions.setStatus("current")
_CCdmaMSIDFlowTotal_Type = Gauge32
_CCdmaMSIDFlowTotal_Object = MibScalar
cCdmaMSIDFlowTotal = _CCdmaMSIDFlowTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 1, 25),
    _CCdmaMSIDFlowTotal_Type()
)
cCdmaMSIDFlowTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaMSIDFlowTotal.setStatus("current")
_CCdmaVPDNFlowTotal_Type = Gauge32
_CCdmaVPDNFlowTotal_Object = MibScalar
cCdmaVPDNFlowTotal = _CCdmaVPDNFlowTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 1, 26),
    _CCdmaVPDNFlowTotal_Type()
)
cCdmaVPDNFlowTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaVPDNFlowTotal.setStatus("current")
_CCdmaPcfInfo_ObjectIdentity = ObjectIdentity
cCdmaPcfInfo = _CCdmaPcfInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 2)
)
_CCdmaPcfTable_Object = MibTable
cCdmaPcfTable = _CCdmaPcfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cCdmaPcfTable.setStatus("current")
_CCdmaPcfEntry_Object = MibTableRow
cCdmaPcfEntry = _CCdmaPcfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 2, 1, 1)
)
cCdmaPcfEntry.setIndexNames(
    (0, "CISCO-CDMA-PDSN-MIB", "cCdmaPcfIpAddress"),
)
if mibBuilder.loadTexts:
    cCdmaPcfEntry.setStatus("current")
_CCdmaPcfIpAddress_Type = IpAddress
_CCdmaPcfIpAddress_Object = MibTableColumn
cCdmaPcfIpAddress = _CCdmaPcfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 2, 1, 1, 1),
    _CCdmaPcfIpAddress_Type()
)
cCdmaPcfIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cCdmaPcfIpAddress.setStatus("current")
_CCdmaPcfSessionTotal_Type = Gauge32
_CCdmaPcfSessionTotal_Object = MibTableColumn
cCdmaPcfSessionTotal = _CCdmaPcfSessionTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 2, 1, 1, 2),
    _CCdmaPcfSessionTotal_Type()
)
cCdmaPcfSessionTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPcfSessionTotal.setStatus("current")
_CCdmaPcfSessionMaxTotal_Type = Gauge32
_CCdmaPcfSessionMaxTotal_Object = MibTableColumn
cCdmaPcfSessionMaxTotal = _CCdmaPcfSessionMaxTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 2, 1, 1, 3),
    _CCdmaPcfSessionMaxTotal_Type()
)
cCdmaPcfSessionMaxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPcfSessionMaxTotal.setStatus("current")
_CCdmaPcfErrorTotal_Type = Gauge32
_CCdmaPcfErrorTotal_Object = MibTableColumn
cCdmaPcfErrorTotal = _CCdmaPcfErrorTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 2, 1, 1, 4),
    _CCdmaPcfErrorTotal_Type()
)
cCdmaPcfErrorTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPcfErrorTotal.setStatus("current")
_CCdmaSessionInfo_ObjectIdentity = ObjectIdentity
cCdmaSessionInfo = _CCdmaSessionInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 3)
)
_CCdmaSessionTable_Object = MibTable
cCdmaSessionTable = _CCdmaSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cCdmaSessionTable.setStatus("obsolete")
_CCdmaSessionEntry_Object = MibTableRow
cCdmaSessionEntry = _CCdmaSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 3, 1, 1)
)
cCdmaSessionEntry.setIndexNames(
    (0, "CISCO-CDMA-PDSN-MIB", "cCdmaSessionMsid"),
)
if mibBuilder.loadTexts:
    cCdmaSessionEntry.setStatus("obsolete")


class _CCdmaSessionMsid_Type(OctetString):
    """Custom type cCdmaSessionMsid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 15),
    )


_CCdmaSessionMsid_Type.__name__ = "OctetString"
_CCdmaSessionMsid_Object = MibTableColumn
cCdmaSessionMsid = _CCdmaSessionMsid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 3, 1, 1, 1),
    _CCdmaSessionMsid_Type()
)
cCdmaSessionMsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cCdmaSessionMsid.setStatus("obsolete")
_CCdmaSessionMsidType_Type = CCdmaMsidType
_CCdmaSessionMsidType_Object = MibTableColumn
cCdmaSessionMsidType = _CCdmaSessionMsidType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 3, 1, 1, 2),
    _CCdmaSessionMsidType_Type()
)
cCdmaSessionMsidType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaSessionMsidType.setStatus("obsolete")


class _CCdmaSessionEsn_Type(OctetString):
    """Custom type cCdmaSessionEsn based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_CCdmaSessionEsn_Type.__name__ = "OctetString"
_CCdmaSessionEsn_Object = MibTableColumn
cCdmaSessionEsn = _CCdmaSessionEsn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 3, 1, 1, 3),
    _CCdmaSessionEsn_Type()
)
cCdmaSessionEsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaSessionEsn.setStatus("obsolete")
_CCdmaSessionPdsnIp_Type = IpAddress
_CCdmaSessionPdsnIp_Object = MibTableColumn
cCdmaSessionPdsnIp = _CCdmaSessionPdsnIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 3, 1, 1, 4),
    _CCdmaSessionPdsnIp_Type()
)
cCdmaSessionPdsnIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaSessionPdsnIp.setStatus("obsolete")
_CCdmaSessionFaIp_Type = IpAddress
_CCdmaSessionFaIp_Object = MibTableColumn
cCdmaSessionFaIp = _CCdmaSessionFaIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 3, 1, 1, 5),
    _CCdmaSessionFaIp_Type()
)
cCdmaSessionFaIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaSessionFaIp.setStatus("obsolete")
_CCdmaSessionA11HaIp_Type = IpAddress
_CCdmaSessionA11HaIp_Object = MibTableColumn
cCdmaSessionA11HaIp = _CCdmaSessionA11HaIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 3, 1, 1, 6),
    _CCdmaSessionA11HaIp_Type()
)
cCdmaSessionA11HaIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaSessionA11HaIp.setStatus("obsolete")
_CCdmaSessionA11FaIp_Type = IpAddress
_CCdmaSessionA11FaIp_Object = MibTableColumn
cCdmaSessionA11FaIp = _CCdmaSessionA11FaIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 3, 1, 1, 7),
    _CCdmaSessionA11FaIp_Type()
)
cCdmaSessionA11FaIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaSessionA11FaIp.setStatus("obsolete")


class _CCdmaSessionKey_Type(OctetString):
    """Custom type cCdmaSessionKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_CCdmaSessionKey_Type.__name__ = "OctetString"
_CCdmaSessionKey_Object = MibTableColumn
cCdmaSessionKey = _CCdmaSessionKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 3, 1, 1, 8),
    _CCdmaSessionKey_Type()
)
cCdmaSessionKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaSessionKey.setStatus("obsolete")


class _CCdmaSessionConnId_Type(OctetString):
    """Custom type cCdmaSessionConnId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_CCdmaSessionConnId_Type.__name__ = "OctetString"
_CCdmaSessionConnId_Object = MibTableColumn
cCdmaSessionConnId = _CCdmaSessionConnId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 3, 1, 1, 9),
    _CCdmaSessionConnId_Type()
)
cCdmaSessionConnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaSessionConnId.setStatus("obsolete")


class _CCdmaSessionMoMtInd_Type(Integer32):
    """Custom type cCdmaSessionMoMtInd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mobileOriginated", 2),
          ("mobileTerminated", 3),
          ("other", 1))
    )


_CCdmaSessionMoMtInd_Type.__name__ = "Integer32"
_CCdmaSessionMoMtInd_Object = MibTableColumn
cCdmaSessionMoMtInd = _CCdmaSessionMoMtInd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 3, 1, 1, 10),
    _CCdmaSessionMoMtInd_Type()
)
cCdmaSessionMoMtInd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaSessionMoMtInd.setStatus("obsolete")
_CCdmaSessionPppCompressEnabled_Type = TruthValue
_CCdmaSessionPppCompressEnabled_Object = MibTableColumn
cCdmaSessionPppCompressEnabled = _CCdmaSessionPppCompressEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 3, 1, 1, 11),
    _CCdmaSessionPppCompressEnabled_Type()
)
cCdmaSessionPppCompressEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaSessionPppCompressEnabled.setStatus("obsolete")
_CCdmaSessionVJCompressEnabled_Type = TruthValue
_CCdmaSessionVJCompressEnabled_Object = MibTableColumn
cCdmaSessionVJCompressEnabled = _CCdmaSessionVJCompressEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 3, 1, 1, 12),
    _CCdmaSessionVJCompressEnabled_Type()
)
cCdmaSessionVJCompressEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaSessionVJCompressEnabled.setStatus("obsolete")
_CCdmaSessionServiceOption_Type = Unsigned32
_CCdmaSessionServiceOption_Object = MibTableColumn
cCdmaSessionServiceOption = _CCdmaSessionServiceOption_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 3, 1, 1, 13),
    _CCdmaSessionServiceOption_Type()
)
cCdmaSessionServiceOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaSessionServiceOption.setStatus("obsolete")
_CCdmaSessionSentOctets_Type = ZeroBasedCounter32
_CCdmaSessionSentOctets_Object = MibTableColumn
cCdmaSessionSentOctets = _CCdmaSessionSentOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 3, 1, 1, 14),
    _CCdmaSessionSentOctets_Type()
)
cCdmaSessionSentOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaSessionSentOctets.setStatus("obsolete")
_CCdmaSessionRcvdOctets_Type = ZeroBasedCounter32
_CCdmaSessionRcvdOctets_Object = MibTableColumn
cCdmaSessionRcvdOctets = _CCdmaSessionRcvdOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 3, 1, 1, 15),
    _CCdmaSessionRcvdOctets_Type()
)
cCdmaSessionRcvdOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaSessionRcvdOctets.setStatus("obsolete")
_CCdmaSessionSentPkts_Type = ZeroBasedCounter32
_CCdmaSessionSentPkts_Object = MibTableColumn
cCdmaSessionSentPkts = _CCdmaSessionSentPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 3, 1, 1, 16),
    _CCdmaSessionSentPkts_Type()
)
cCdmaSessionSentPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaSessionSentPkts.setStatus("obsolete")
_CCdmaSessionRcvdPkts_Type = ZeroBasedCounter32
_CCdmaSessionRcvdPkts_Object = MibTableColumn
cCdmaSessionRcvdPkts = _CCdmaSessionRcvdPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 3, 1, 1, 17),
    _CCdmaSessionRcvdPkts_Type()
)
cCdmaSessionRcvdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaSessionRcvdPkts.setStatus("obsolete")
_CCdmaSessionDiscardedOutPkts_Type = ZeroBasedCounter32
_CCdmaSessionDiscardedOutPkts_Object = MibTableColumn
cCdmaSessionDiscardedOutPkts = _CCdmaSessionDiscardedOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 3, 1, 1, 18),
    _CCdmaSessionDiscardedOutPkts_Type()
)
cCdmaSessionDiscardedOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaSessionDiscardedOutPkts.setStatus("obsolete")
_CCdmaSessionDiscardedInPkts_Type = ZeroBasedCounter32
_CCdmaSessionDiscardedInPkts_Object = MibTableColumn
cCdmaSessionDiscardedInPkts = _CCdmaSessionDiscardedInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 3, 1, 1, 19),
    _CCdmaSessionDiscardedInPkts_Type()
)
cCdmaSessionDiscardedInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaSessionDiscardedInPkts.setStatus("obsolete")
_CCdmaSessionConnStartTime_Type = DateAndTime
_CCdmaSessionConnStartTime_Object = MibTableColumn
cCdmaSessionConnStartTime = _CCdmaSessionConnStartTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 3, 1, 1, 20),
    _CCdmaSessionConnStartTime_Type()
)
cCdmaSessionConnStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaSessionConnStartTime.setStatus("obsolete")
_CCdmaActiveConnTime_Type = Unsigned32
_CCdmaActiveConnTime_Object = MibTableColumn
cCdmaActiveConnTime = _CCdmaActiveConnTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 3, 1, 1, 21),
    _CCdmaActiveConnTime_Type()
)
cCdmaActiveConnTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaActiveConnTime.setStatus("obsolete")
if mibBuilder.loadTexts:
    cCdmaActiveConnTime.setUnits("seconds")
_CCdmaSessionFlowCount_Type = Gauge32
_CCdmaSessionFlowCount_Object = MibTableColumn
cCdmaSessionFlowCount = _CCdmaSessionFlowCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 3, 1, 1, 22),
    _CCdmaSessionFlowCount_Type()
)
cCdmaSessionFlowCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaSessionFlowCount.setStatus("obsolete")


class _CCdmaSessionStatus_Type(Integer32):
    """Custom type cCdmaSessionStatus based on Integer32"""
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
        *(("airlinksetup", 2),
          ("airlinkstart", 3),
          ("airlinkstop", 4),
          ("unknown", 1))
    )


_CCdmaSessionStatus_Type.__name__ = "Integer32"
_CCdmaSessionStatus_Object = MibTableColumn
cCdmaSessionStatus = _CCdmaSessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 3, 1, 1, 23),
    _CCdmaSessionStatus_Type()
)
cCdmaSessionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaSessionStatus.setStatus("obsolete")
_CCdmaSessionRegLifeTime_Type = TimeTicks
_CCdmaSessionRegLifeTime_Object = MibTableColumn
cCdmaSessionRegLifeTime = _CCdmaSessionRegLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 3, 1, 1, 24),
    _CCdmaSessionRegLifeTime_Type()
)
cCdmaSessionRegLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaSessionRegLifeTime.setStatus("obsolete")
_CCdmaSessionRegTimeToExpire_Type = TimeTicks
_CCdmaSessionRegTimeToExpire_Object = MibTableColumn
cCdmaSessionRegTimeToExpire = _CCdmaSessionRegTimeToExpire_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 3, 1, 1, 25),
    _CCdmaSessionRegTimeToExpire_Type()
)
cCdmaSessionRegTimeToExpire.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaSessionRegTimeToExpire.setStatus("obsolete")
_CCdmaSessionGREFromIPPkts_Type = ZeroBasedCounter32
_CCdmaSessionGREFromIPPkts_Object = MibTableColumn
cCdmaSessionGREFromIPPkts = _CCdmaSessionGREFromIPPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 3, 1, 1, 26),
    _CCdmaSessionGREFromIPPkts_Type()
)
cCdmaSessionGREFromIPPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaSessionGREFromIPPkts.setStatus("obsolete")
_CCdmaSessionGREToIPPkts_Type = ZeroBasedCounter32
_CCdmaSessionGREToIPPkts_Object = MibTableColumn
cCdmaSessionGREToIPPkts = _CCdmaSessionGREToIPPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 3, 1, 1, 27),
    _CCdmaSessionGREToIPPkts_Type()
)
cCdmaSessionGREToIPPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaSessionGREToIPPkts.setStatus("obsolete")
_CCdmaSessionFlowTable_Object = MibTable
cCdmaSessionFlowTable = _CCdmaSessionFlowTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cCdmaSessionFlowTable.setStatus("obsolete")
_CCdmaSessionFlowEntry_Object = MibTableRow
cCdmaSessionFlowEntry = _CCdmaSessionFlowEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 3, 2, 1)
)
cCdmaSessionFlowEntry.setIndexNames(
    (0, "CISCO-CDMA-PDSN-MIB", "cCdmaSessionMsid"),
    (0, "CISCO-CDMA-PDSN-MIB", "cCdmaSessionUserFlowIpAddress"),
)
if mibBuilder.loadTexts:
    cCdmaSessionFlowEntry.setStatus("obsolete")
_CCdmaSessionUserFlowIpAddress_Type = IpAddress
_CCdmaSessionUserFlowIpAddress_Object = MibTableColumn
cCdmaSessionUserFlowIpAddress = _CCdmaSessionUserFlowIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 3, 2, 1, 1),
    _CCdmaSessionUserFlowIpAddress_Type()
)
cCdmaSessionUserFlowIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cCdmaSessionUserFlowIpAddress.setStatus("obsolete")
_CCdmaSessionNai_Type = SnmpAdminString
_CCdmaSessionNai_Object = MibTableColumn
cCdmaSessionNai = _CCdmaSessionNai_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 3, 2, 1, 2),
    _CCdmaSessionNai_Type()
)
cCdmaSessionNai.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaSessionNai.setStatus("obsolete")


class _CCdmaSessionAddressingScheme_Type(Integer32):
    """Custom type cCdmaSessionAddressingScheme based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 3),
          ("other", 1),
          ("static", 2))
    )


_CCdmaSessionAddressingScheme_Type.__name__ = "Integer32"
_CCdmaSessionAddressingScheme_Object = MibTableColumn
cCdmaSessionAddressingScheme = _CCdmaSessionAddressingScheme_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 3, 2, 1, 3),
    _CCdmaSessionAddressingScheme_Type()
)
cCdmaSessionAddressingScheme.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaSessionAddressingScheme.setStatus("obsolete")


class _CCdmaSessionFlowTechnology_Type(Integer32):
    """Custom type cCdmaSessionFlowTechnology based on Integer32"""
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
        *(("mobileIp", 3),
          ("other", 1),
          ("proxyMobileIp", 4),
          ("simpleIp", 2))
    )


_CCdmaSessionFlowTechnology_Type.__name__ = "Integer32"
_CCdmaSessionFlowTechnology_Object = MibTableColumn
cCdmaSessionFlowTechnology = _CCdmaSessionFlowTechnology_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 3, 2, 1, 4),
    _CCdmaSessionFlowTechnology_Type()
)
cCdmaSessionFlowTechnology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaSessionFlowTechnology.setStatus("obsolete")
_CCdmaSessionHaIpAddress_Type = IpAddress
_CCdmaSessionHaIpAddress_Object = MibTableColumn
cCdmaSessionHaIpAddress = _CCdmaSessionHaIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 3, 2, 1, 5),
    _CCdmaSessionHaIpAddress_Type()
)
cCdmaSessionHaIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaSessionHaIpAddress.setStatus("obsolete")


class _CCdmaSessionTunnelProt_Type(Integer32):
    """Custom type cCdmaSessionTunnelProt based on Integer32"""
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
        *(("gre", 5),
          ("ipinip", 6),
          ("l2f", 4),
          ("l2tp", 3),
          ("notunnel", 2),
          ("other", 1))
    )


_CCdmaSessionTunnelProt_Type.__name__ = "Integer32"
_CCdmaSessionTunnelProt_Object = MibTableColumn
cCdmaSessionTunnelProt = _CCdmaSessionTunnelProt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 3, 2, 1, 6),
    _CCdmaSessionTunnelProt_Type()
)
cCdmaSessionTunnelProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaSessionTunnelProt.setStatus("obsolete")
_CCdmaFailHistInfo_ObjectIdentity = ObjectIdentity
cCdmaFailHistInfo = _CCdmaFailHistInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 4)
)
_CCdmaFailHistInfoTable_Object = MibTable
cCdmaFailHistInfoTable = _CCdmaFailHistInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cCdmaFailHistInfoTable.setStatus("current")
_CCdmaFailHistInfoEntry_Object = MibTableRow
cCdmaFailHistInfoEntry = _CCdmaFailHistInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 4, 1, 1)
)
cCdmaFailHistInfoEntry.setIndexNames(
    (0, "CISCO-CDMA-PDSN-MIB", "cCdmaFailSessionIndex"),
)
if mibBuilder.loadTexts:
    cCdmaFailHistInfoEntry.setStatus("current")
_CCdmaFailSessionIndex_Type = Unsigned32
_CCdmaFailSessionIndex_Object = MibTableColumn
cCdmaFailSessionIndex = _CCdmaFailSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 4, 1, 1, 1),
    _CCdmaFailSessionIndex_Type()
)
cCdmaFailSessionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cCdmaFailSessionIndex.setStatus("current")


class _CCdmaFailSessionMsid_Type(OctetString):
    """Custom type cCdmaFailSessionMsid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 15),
    )


_CCdmaFailSessionMsid_Type.__name__ = "OctetString"
_CCdmaFailSessionMsid_Object = MibTableColumn
cCdmaFailSessionMsid = _CCdmaFailSessionMsid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 4, 1, 1, 2),
    _CCdmaFailSessionMsid_Type()
)
cCdmaFailSessionMsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaFailSessionMsid.setStatus("current")
_CCdmaFailSessionMsidType_Type = CCdmaMsidType
_CCdmaFailSessionMsidType_Object = MibTableColumn
cCdmaFailSessionMsidType = _CCdmaFailSessionMsidType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 4, 1, 1, 3),
    _CCdmaFailSessionMsidType_Type()
)
cCdmaFailSessionMsidType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaFailSessionMsidType.setStatus("current")


class _CCdmaFailSessionEsn_Type(OctetString):
    """Custom type cCdmaFailSessionEsn based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_CCdmaFailSessionEsn_Type.__name__ = "OctetString"
_CCdmaFailSessionEsn_Object = MibTableColumn
cCdmaFailSessionEsn = _CCdmaFailSessionEsn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 4, 1, 1, 4),
    _CCdmaFailSessionEsn_Type()
)
cCdmaFailSessionEsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaFailSessionEsn.setStatus("deprecated")
_CCdmaFailSessionA11HaIp_Type = IpAddress
_CCdmaFailSessionA11HaIp_Object = MibTableColumn
cCdmaFailSessionA11HaIp = _CCdmaFailSessionA11HaIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 4, 1, 1, 5),
    _CCdmaFailSessionA11HaIp_Type()
)
cCdmaFailSessionA11HaIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaFailSessionA11HaIp.setStatus("current")
_CCdmaFailSessionA11FaIp_Type = IpAddress
_CCdmaFailSessionA11FaIp_Object = MibTableColumn
cCdmaFailSessionA11FaIp = _CCdmaFailSessionA11FaIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 4, 1, 1, 6),
    _CCdmaFailSessionA11FaIp_Type()
)
cCdmaFailSessionA11FaIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaFailSessionA11FaIp.setStatus("current")


class _CCdmaFailSessionConnId_Type(OctetString):
    """Custom type cCdmaFailSessionConnId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_CCdmaFailSessionConnId_Type.__name__ = "OctetString"
_CCdmaFailSessionConnId_Object = MibTableColumn
cCdmaFailSessionConnId = _CCdmaFailSessionConnId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 4, 1, 1, 7),
    _CCdmaFailSessionConnId_Type()
)
cCdmaFailSessionConnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaFailSessionConnId.setStatus("current")


class _CCdmaFailSessionKey_Type(OctetString):
    """Custom type cCdmaFailSessionKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_CCdmaFailSessionKey_Type.__name__ = "OctetString"
_CCdmaFailSessionKey_Object = MibTableColumn
cCdmaFailSessionKey = _CCdmaFailSessionKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 4, 1, 1, 8),
    _CCdmaFailSessionKey_Type()
)
cCdmaFailSessionKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaFailSessionKey.setStatus("current")
_CCdmaFailHistFailTime_Type = DateAndTime
_CCdmaFailHistFailTime_Object = MibTableColumn
cCdmaFailHistFailTime = _CCdmaFailHistFailTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 4, 1, 1, 9),
    _CCdmaFailHistFailTime_Type()
)
cCdmaFailHistFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaFailHistFailTime.setStatus("current")


class _CCdmaFailHistFailType_Type(Integer32):
    """Custom type cCdmaFailHistFailType based on Integer32"""
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
              21)
        )
    )
    namedValues = NamedValues(
        *(("a10a11SessionTimeout", 5),
          ("adminProhibited", 9),
          ("insufficientResource", 10),
          ("maxAllowedPcfReached", 7),
          ("maxAllowedSessionReached", 6),
          ("mnAuthenticationFailed", 11),
          ("mobileIpAuthenticationFailure", 3),
          ("mobileIpRegistrationTimeout", 4),
          ("other", 1),
          ("poorlyFormedRequest", 13),
          ("pppAuthenticationFailure", 2),
          ("pppIpcpNegotiationFailed", 21),
          ("pppIpcpTimeout", 20),
          ("pppLcpNegotiationFailed", 19),
          ("pppLcpTimeout", 18),
          ("registrationIdentMismatched", 12),
          ("reverseTunnelUnavail", 15),
          ("sessionFormatError", 8),
          ("tbitNotSet", 16),
          ("unknownHAAddress", 14),
          ("unsupportedVIDorBadCVSE", 17))
    )


_CCdmaFailHistFailType_Type.__name__ = "Integer32"
_CCdmaFailHistFailType_Object = MibTableColumn
cCdmaFailHistFailType = _CCdmaFailHistFailType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 4, 1, 1, 10),
    _CCdmaFailHistFailType_Type()
)
cCdmaFailHistFailType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaFailHistFailType.setStatus("current")


class _CCdmaFailHistServiceOption_Type(Unsigned32):
    """Custom type cCdmaFailHistServiceOption based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CCdmaFailHistServiceOption_Type.__name__ = "Unsigned32"
_CCdmaFailHistServiceOption_Object = MibTableColumn
cCdmaFailHistServiceOption = _CCdmaFailHistServiceOption_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 4, 1, 1, 11),
    _CCdmaFailHistServiceOption_Type()
)
cCdmaFailHistServiceOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaFailHistServiceOption.setStatus("current")


class _CCdmaFailHistPanId_Type(SnmpAdminString):
    """Custom type cCdmaFailHistPanId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_CCdmaFailHistPanId_Type.__name__ = "SnmpAdminString"
_CCdmaFailHistPanId_Object = MibTableColumn
cCdmaFailHistPanId = _CCdmaFailHistPanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 4, 1, 1, 12),
    _CCdmaFailHistPanId_Type()
)
cCdmaFailHistPanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaFailHistPanId.setStatus("current")


class _CCdmaFailHistCanId_Type(SnmpAdminString):
    """Custom type cCdmaFailHistCanId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_CCdmaFailHistCanId_Type.__name__ = "SnmpAdminString"
_CCdmaFailHistCanId_Object = MibTableColumn
cCdmaFailHistCanId = _CCdmaFailHistCanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 4, 1, 1, 13),
    _CCdmaFailHistCanId_Type()
)
cCdmaFailHistCanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaFailHistCanId.setStatus("current")


class _CCdmaFailHistBsid_Type(SnmpAdminString):
    """Custom type cCdmaFailHistBsid based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_CCdmaFailHistBsid_Type.__name__ = "SnmpAdminString"
_CCdmaFailHistBsid_Object = MibTableColumn
cCdmaFailHistBsid = _CCdmaFailHistBsid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 4, 1, 1, 14),
    _CCdmaFailHistBsid_Type()
)
cCdmaFailHistBsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaFailHistBsid.setStatus("current")


class _CCdmaFailSessionEsn2_Type(OctetString):
    """Custom type cCdmaFailSessionEsn2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_CCdmaFailSessionEsn2_Type.__name__ = "OctetString"
_CCdmaFailSessionEsn2_Object = MibTableColumn
cCdmaFailSessionEsn2 = _CCdmaFailSessionEsn2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 4, 1, 1, 15),
    _CCdmaFailSessionEsn2_Type()
)
cCdmaFailSessionEsn2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaFailSessionEsn2.setStatus("current")
_CCdmaRPRegistrationStats_ObjectIdentity = ObjectIdentity
cCdmaRPRegistrationStats = _CCdmaRPRegistrationStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 5)
)
_CCdmaRPRegValidRequests_Type = ZeroBasedCounter32
_CCdmaRPRegValidRequests_Object = MibScalar
cCdmaRPRegValidRequests = _CCdmaRPRegValidRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 5, 1),
    _CCdmaRPRegValidRequests_Type()
)
cCdmaRPRegValidRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRPRegValidRequests.setStatus("obsolete")
_CCdmaRPRegAcceptedReplies_Type = ZeroBasedCounter32
_CCdmaRPRegAcceptedReplies_Object = MibScalar
cCdmaRPRegAcceptedReplies = _CCdmaRPRegAcceptedReplies_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 5, 2),
    _CCdmaRPRegAcceptedReplies_Type()
)
cCdmaRPRegAcceptedReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRPRegAcceptedReplies.setStatus("obsolete")
_CCdmaRPRegLifeTimeZeroRequests_Type = ZeroBasedCounter32
_CCdmaRPRegLifeTimeZeroRequests_Object = MibScalar
cCdmaRPRegLifeTimeZeroRequests = _CCdmaRPRegLifeTimeZeroRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 5, 3),
    _CCdmaRPRegLifeTimeZeroRequests_Type()
)
cCdmaRPRegLifeTimeZeroRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRPRegLifeTimeZeroRequests.setStatus("obsolete")
_CCdmaRPDeRegAcceptedReplies_Type = ZeroBasedCounter32
_CCdmaRPDeRegAcceptedReplies_Object = MibScalar
cCdmaRPDeRegAcceptedReplies = _CCdmaRPDeRegAcceptedReplies_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 5, 4),
    _CCdmaRPDeRegAcceptedReplies_Type()
)
cCdmaRPDeRegAcceptedReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRPDeRegAcceptedReplies.setStatus("obsolete")
_CCdmaRPRegReasonUnSpecFailures_Type = ZeroBasedCounter32
_CCdmaRPRegReasonUnSpecFailures_Object = MibScalar
cCdmaRPRegReasonUnSpecFailures = _CCdmaRPRegReasonUnSpecFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 5, 5),
    _CCdmaRPRegReasonUnSpecFailures_Type()
)
cCdmaRPRegReasonUnSpecFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRPRegReasonUnSpecFailures.setStatus("obsolete")
_CCdmaRPRegAdminProhibFailures_Type = ZeroBasedCounter32
_CCdmaRPRegAdminProhibFailures_Object = MibScalar
cCdmaRPRegAdminProhibFailures = _CCdmaRPRegAdminProhibFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 5, 6),
    _CCdmaRPRegAdminProhibFailures_Type()
)
cCdmaRPRegAdminProhibFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRPRegAdminProhibFailures.setStatus("obsolete")
_CCdmaRPRegInsuffResFailures_Type = ZeroBasedCounter32
_CCdmaRPRegInsuffResFailures_Object = MibScalar
cCdmaRPRegInsuffResFailures = _CCdmaRPRegInsuffResFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 5, 7),
    _CCdmaRPRegInsuffResFailures_Type()
)
cCdmaRPRegInsuffResFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRPRegInsuffResFailures.setStatus("obsolete")
_CCdmaRPRegMNAuthenFailures_Type = ZeroBasedCounter32
_CCdmaRPRegMNAuthenFailures_Object = MibScalar
cCdmaRPRegMNAuthenFailures = _CCdmaRPRegMNAuthenFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 5, 8),
    _CCdmaRPRegMNAuthenFailures_Type()
)
cCdmaRPRegMNAuthenFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRPRegMNAuthenFailures.setStatus("obsolete")
_CCdmaRPRegIdentMismatchFailures_Type = ZeroBasedCounter32
_CCdmaRPRegIdentMismatchFailures_Object = MibScalar
cCdmaRPRegIdentMismatchFailures = _CCdmaRPRegIdentMismatchFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 5, 9),
    _CCdmaRPRegIdentMismatchFailures_Type()
)
cCdmaRPRegIdentMismatchFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRPRegIdentMismatchFailures.setStatus("obsolete")
_CCdmaRPRegBadRequestFailures_Type = ZeroBasedCounter32
_CCdmaRPRegBadRequestFailures_Object = MibScalar
cCdmaRPRegBadRequestFailures = _CCdmaRPRegBadRequestFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 5, 10),
    _CCdmaRPRegBadRequestFailures_Type()
)
cCdmaRPRegBadRequestFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRPRegBadRequestFailures.setStatus("obsolete")
_CCdmaRPRegUnknownHAAddrFailures_Type = ZeroBasedCounter32
_CCdmaRPRegUnknownHAAddrFailures_Object = MibScalar
cCdmaRPRegUnknownHAAddrFailures = _CCdmaRPRegUnknownHAAddrFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 5, 11),
    _CCdmaRPRegUnknownHAAddrFailures_Type()
)
cCdmaRPRegUnknownHAAddrFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRPRegUnknownHAAddrFailures.setStatus("obsolete")
_CCdmaRPRegNoRevTunnelFailures_Type = ZeroBasedCounter32
_CCdmaRPRegNoRevTunnelFailures_Object = MibScalar
cCdmaRPRegNoRevTunnelFailures = _CCdmaRPRegNoRevTunnelFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 5, 12),
    _CCdmaRPRegNoRevTunnelFailures_Type()
)
cCdmaRPRegNoRevTunnelFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRPRegNoRevTunnelFailures.setStatus("obsolete")
_CCdmaRPRegTBitNotSetFailures_Type = ZeroBasedCounter32
_CCdmaRPRegTBitNotSetFailures_Object = MibScalar
cCdmaRPRegTBitNotSetFailures = _CCdmaRPRegTBitNotSetFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 5, 13),
    _CCdmaRPRegTBitNotSetFailures_Type()
)
cCdmaRPRegTBitNotSetFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRPRegTBitNotSetFailures.setStatus("obsolete")
_CCdmaRPRegBadCVSEFailures_Type = ZeroBasedCounter32
_CCdmaRPRegBadCVSEFailures_Object = MibScalar
cCdmaRPRegBadCVSEFailures = _CCdmaRPRegBadCVSEFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 5, 14),
    _CCdmaRPRegBadCVSEFailures_Type()
)
cCdmaRPRegBadCVSEFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRPRegBadCVSEFailures.setStatus("obsolete")
_CCdmaRPUpdateStats_ObjectIdentity = ObjectIdentity
cCdmaRPUpdateStats = _CCdmaRPUpdateStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 6)
)
_CCdmaRPUpdValidRequests_Type = ZeroBasedCounter32
_CCdmaRPUpdValidRequests_Object = MibScalar
cCdmaRPUpdValidRequests = _CCdmaRPUpdValidRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 6, 1),
    _CCdmaRPUpdValidRequests_Type()
)
cCdmaRPUpdValidRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRPUpdValidRequests.setStatus("obsolete")
_CCdmaRPUpdAcceptedReplies_Type = ZeroBasedCounter32
_CCdmaRPUpdAcceptedReplies_Object = MibScalar
cCdmaRPUpdAcceptedReplies = _CCdmaRPUpdAcceptedReplies_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 6, 2),
    _CCdmaRPUpdAcceptedReplies_Type()
)
cCdmaRPUpdAcceptedReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRPUpdAcceptedReplies.setStatus("obsolete")
_CCdmaRPUpdReasonUnSpecFailures_Type = ZeroBasedCounter32
_CCdmaRPUpdReasonUnSpecFailures_Object = MibScalar
cCdmaRPUpdReasonUnSpecFailures = _CCdmaRPUpdReasonUnSpecFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 6, 3),
    _CCdmaRPUpdReasonUnSpecFailures_Type()
)
cCdmaRPUpdReasonUnSpecFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRPUpdReasonUnSpecFailures.setStatus("obsolete")
_CCdmaRPUpdAdminProhibFailures_Type = ZeroBasedCounter32
_CCdmaRPUpdAdminProhibFailures_Object = MibScalar
cCdmaRPUpdAdminProhibFailures = _CCdmaRPUpdAdminProhibFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 6, 4),
    _CCdmaRPUpdAdminProhibFailures_Type()
)
cCdmaRPUpdAdminProhibFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRPUpdAdminProhibFailures.setStatus("obsolete")
_CCdmaRPUpdMNAuthenFailures_Type = ZeroBasedCounter32
_CCdmaRPUpdMNAuthenFailures_Object = MibScalar
cCdmaRPUpdMNAuthenFailures = _CCdmaRPUpdMNAuthenFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 6, 5),
    _CCdmaRPUpdMNAuthenFailures_Type()
)
cCdmaRPUpdMNAuthenFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRPUpdMNAuthenFailures.setStatus("obsolete")
_CCdmaRPUpdIdentMismatchFailures_Type = ZeroBasedCounter32
_CCdmaRPUpdIdentMismatchFailures_Object = MibScalar
cCdmaRPUpdIdentMismatchFailures = _CCdmaRPUpdIdentMismatchFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 6, 6),
    _CCdmaRPUpdIdentMismatchFailures_Type()
)
cCdmaRPUpdIdentMismatchFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRPUpdIdentMismatchFailures.setStatus("obsolete")
_CCdmaRPUpdBadRequestFailures_Type = ZeroBasedCounter32
_CCdmaRPUpdBadRequestFailures_Object = MibScalar
cCdmaRPUpdBadRequestFailures = _CCdmaRPUpdBadRequestFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 6, 7),
    _CCdmaRPUpdBadRequestFailures_Type()
)
cCdmaRPUpdBadRequestFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRPUpdBadRequestFailures.setStatus("obsolete")
_CCdmaPerformanceStats_ObjectIdentity = ObjectIdentity
cCdmaPerformanceStats = _CCdmaPerformanceStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7)
)
_CCdmaRpRegStats_ObjectIdentity = ObjectIdentity
cCdmaRpRegStats = _CCdmaRpRegStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 1)
)
_CCdmaRpRegReceivedReqs_Type = Counter32
_CCdmaRpRegReceivedReqs_Object = MibScalar
cCdmaRpRegReceivedReqs = _CCdmaRpRegReceivedReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 1, 1),
    _CCdmaRpRegReceivedReqs_Type()
)
cCdmaRpRegReceivedReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpRegReceivedReqs.setStatus("current")
_CCdmaRpRegAcceptedReqs_Type = Counter32
_CCdmaRpRegAcceptedReqs_Object = MibScalar
cCdmaRpRegAcceptedReqs = _CCdmaRpRegAcceptedReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 1, 2),
    _CCdmaRpRegAcceptedReqs_Type()
)
cCdmaRpRegAcceptedReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpRegAcceptedReqs.setStatus("current")
_CCdmaRpRegDeniedReqs_Type = Counter32
_CCdmaRpRegDeniedReqs_Object = MibScalar
cCdmaRpRegDeniedReqs = _CCdmaRpRegDeniedReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 1, 3),
    _CCdmaRpRegDeniedReqs_Type()
)
cCdmaRpRegDeniedReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpRegDeniedReqs.setStatus("current")
_CCdmaRpRegDiscardedReqs_Type = Counter32
_CCdmaRpRegDiscardedReqs_Object = MibScalar
cCdmaRpRegDiscardedReqs = _CCdmaRpRegDiscardedReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 1, 4),
    _CCdmaRpRegDiscardedReqs_Type()
)
cCdmaRpRegDiscardedReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpRegDiscardedReqs.setStatus("current")
_CCdmaRpInitRegAcceptedReqs_Type = Counter32
_CCdmaRpInitRegAcceptedReqs_Object = MibScalar
cCdmaRpInitRegAcceptedReqs = _CCdmaRpInitRegAcceptedReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 1, 5),
    _CCdmaRpInitRegAcceptedReqs_Type()
)
cCdmaRpInitRegAcceptedReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpInitRegAcceptedReqs.setStatus("current")
_CCdmaRpInitRegDeniedReqs_Type = Counter32
_CCdmaRpInitRegDeniedReqs_Object = MibScalar
cCdmaRpInitRegDeniedReqs = _CCdmaRpInitRegDeniedReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 1, 6),
    _CCdmaRpInitRegDeniedReqs_Type()
)
cCdmaRpInitRegDeniedReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpInitRegDeniedReqs.setStatus("current")
_CCdmaRpReRegAcceptedReqs_Type = Counter32
_CCdmaRpReRegAcceptedReqs_Object = MibScalar
cCdmaRpReRegAcceptedReqs = _CCdmaRpReRegAcceptedReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 1, 7),
    _CCdmaRpReRegAcceptedReqs_Type()
)
cCdmaRpReRegAcceptedReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpReRegAcceptedReqs.setStatus("current")
_CCdmaRpReRegDeniedReqs_Type = Counter32
_CCdmaRpReRegDeniedReqs_Object = MibScalar
cCdmaRpReRegDeniedReqs = _CCdmaRpReRegDeniedReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 1, 8),
    _CCdmaRpReRegDeniedReqs_Type()
)
cCdmaRpReRegDeniedReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpReRegDeniedReqs.setStatus("current")
_CCdmaRpDeRegAcceptedReqs_Type = Counter32
_CCdmaRpDeRegAcceptedReqs_Object = MibScalar
cCdmaRpDeRegAcceptedReqs = _CCdmaRpDeRegAcceptedReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 1, 9),
    _CCdmaRpDeRegAcceptedReqs_Type()
)
cCdmaRpDeRegAcceptedReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpDeRegAcceptedReqs.setStatus("current")
_CCdmaRpDeRegDeniedReqs_Type = Counter32
_CCdmaRpDeRegDeniedReqs_Object = MibScalar
cCdmaRpDeRegDeniedReqs = _CCdmaRpDeRegDeniedReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 1, 10),
    _CCdmaRpDeRegDeniedReqs_Type()
)
cCdmaRpDeRegDeniedReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpDeRegDeniedReqs.setStatus("current")
_CCdmaRpRegReasonlUnSpecFailures_Type = Counter32
_CCdmaRpRegReasonlUnSpecFailures_Object = MibScalar
cCdmaRpRegReasonlUnSpecFailures = _CCdmaRpRegReasonlUnSpecFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 1, 11),
    _CCdmaRpRegReasonlUnSpecFailures_Type()
)
cCdmaRpRegReasonlUnSpecFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpRegReasonlUnSpecFailures.setStatus("deprecated")
_CCdmaRpRegAdminProhibFailures_Type = Counter32
_CCdmaRpRegAdminProhibFailures_Object = MibScalar
cCdmaRpRegAdminProhibFailures = _CCdmaRpRegAdminProhibFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 1, 12),
    _CCdmaRpRegAdminProhibFailures_Type()
)
cCdmaRpRegAdminProhibFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpRegAdminProhibFailures.setStatus("current")
_CCdmaRpRegInsuffResFailures_Type = Counter32
_CCdmaRpRegInsuffResFailures_Object = MibScalar
cCdmaRpRegInsuffResFailures = _CCdmaRpRegInsuffResFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 1, 13),
    _CCdmaRpRegInsuffResFailures_Type()
)
cCdmaRpRegInsuffResFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpRegInsuffResFailures.setStatus("current")
_CCdmaRpRegMNAuthFailures_Type = Counter32
_CCdmaRpRegMNAuthFailures_Object = MibScalar
cCdmaRpRegMNAuthFailures = _CCdmaRpRegMNAuthFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 1, 14),
    _CCdmaRpRegMNAuthFailures_Type()
)
cCdmaRpRegMNAuthFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpRegMNAuthFailures.setStatus("current")
_CCdmaRpRegIdMismatchFailures_Type = Counter32
_CCdmaRpRegIdMismatchFailures_Object = MibScalar
cCdmaRpRegIdMismatchFailures = _CCdmaRpRegIdMismatchFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 1, 15),
    _CCdmaRpRegIdMismatchFailures_Type()
)
cCdmaRpRegIdMismatchFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpRegIdMismatchFailures.setStatus("current")
_CCdmaRpRegBadReqFailures_Type = Counter32
_CCdmaRpRegBadReqFailures_Object = MibScalar
cCdmaRpRegBadReqFailures = _CCdmaRpRegBadReqFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 1, 16),
    _CCdmaRpRegBadReqFailures_Type()
)
cCdmaRpRegBadReqFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpRegBadReqFailures.setStatus("current")
_CCdmaRpRegUnknownPdsnFailures_Type = Counter32
_CCdmaRpRegUnknownPdsnFailures_Object = MibScalar
cCdmaRpRegUnknownPdsnFailures = _CCdmaRpRegUnknownPdsnFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 1, 17),
    _CCdmaRpRegUnknownPdsnFailures_Type()
)
cCdmaRpRegUnknownPdsnFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpRegUnknownPdsnFailures.setStatus("current")
_CCdmaRpRegNoRevTunnelFailures_Type = Counter32
_CCdmaRpRegNoRevTunnelFailures_Object = MibScalar
cCdmaRpRegNoRevTunnelFailures = _CCdmaRpRegNoRevTunnelFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 1, 18),
    _CCdmaRpRegNoRevTunnelFailures_Type()
)
cCdmaRpRegNoRevTunnelFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpRegNoRevTunnelFailures.setStatus("current")
_CCdmaRpRegTBitNotSetFailures_Type = Counter32
_CCdmaRpRegTBitNotSetFailures_Object = MibScalar
cCdmaRpRegTBitNotSetFailures = _CCdmaRpRegTBitNotSetFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 1, 19),
    _CCdmaRpRegTBitNotSetFailures_Type()
)
cCdmaRpRegTBitNotSetFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpRegTBitNotSetFailures.setStatus("current")
_CCdmaRpRegBadCVSEFailures_Type = Counter32
_CCdmaRpRegBadCVSEFailures_Object = MibScalar
cCdmaRpRegBadCVSEFailures = _CCdmaRpRegBadCVSEFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 1, 20),
    _CCdmaRpRegBadCVSEFailures_Type()
)
cCdmaRpRegBadCVSEFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpRegBadCVSEFailures.setStatus("current")
_CCdmaRpRegReasonUnSpecFailures_Type = Counter32
_CCdmaRpRegReasonUnSpecFailures_Object = MibScalar
cCdmaRpRegReasonUnSpecFailures = _CCdmaRpRegReasonUnSpecFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 1, 21),
    _CCdmaRpRegReasonUnSpecFailures_Type()
)
cCdmaRpRegReasonUnSpecFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpRegReasonUnSpecFailures.setStatus("current")
_CCdmaRpDeRegHandoffAcceptedReqs_Type = Counter32
_CCdmaRpDeRegHandoffAcceptedReqs_Object = MibScalar
cCdmaRpDeRegHandoffAcceptedReqs = _CCdmaRpDeRegHandoffAcceptedReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 1, 22),
    _CCdmaRpDeRegHandoffAcceptedReqs_Type()
)
cCdmaRpDeRegHandoffAcceptedReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpDeRegHandoffAcceptedReqs.setStatus("current")
_CCdmaRpDeRegHandoffDeniedReqs_Type = Counter32
_CCdmaRpDeRegHandoffDeniedReqs_Object = MibScalar
cCdmaRpDeRegHandoffDeniedReqs = _CCdmaRpDeRegHandoffDeniedReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 1, 23),
    _CCdmaRpDeRegHandoffDeniedReqs_Type()
)
cCdmaRpDeRegHandoffDeniedReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpDeRegHandoffDeniedReqs.setStatus("current")
_CCdmaRpInitRegReceivedReqs_Type = ZeroBasedCounter32
_CCdmaRpInitRegReceivedReqs_Object = MibScalar
cCdmaRpInitRegReceivedReqs = _CCdmaRpInitRegReceivedReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 1, 24),
    _CCdmaRpInitRegReceivedReqs_Type()
)
cCdmaRpInitRegReceivedReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpInitRegReceivedReqs.setStatus("current")
_CCdmaRpInitRegDiscardedReqs_Type = ZeroBasedCounter32
_CCdmaRpInitRegDiscardedReqs_Object = MibScalar
cCdmaRpInitRegDiscardedReqs = _CCdmaRpInitRegDiscardedReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 1, 25),
    _CCdmaRpInitRegDiscardedReqs_Type()
)
cCdmaRpInitRegDiscardedReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpInitRegDiscardedReqs.setStatus("current")
_CCdmaRpReRegReceivedReqs_Type = ZeroBasedCounter32
_CCdmaRpReRegReceivedReqs_Object = MibScalar
cCdmaRpReRegReceivedReqs = _CCdmaRpReRegReceivedReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 1, 26),
    _CCdmaRpReRegReceivedReqs_Type()
)
cCdmaRpReRegReceivedReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpReRegReceivedReqs.setStatus("current")
_CCdmaRpReRegDiscardedReqs_Type = ZeroBasedCounter32
_CCdmaRpReRegDiscardedReqs_Object = MibScalar
cCdmaRpReRegDiscardedReqs = _CCdmaRpReRegDiscardedReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 1, 27),
    _CCdmaRpReRegDiscardedReqs_Type()
)
cCdmaRpReRegDiscardedReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpReRegDiscardedReqs.setStatus("current")
_CCdmaRpDeRegReceivedReqs_Type = ZeroBasedCounter32
_CCdmaRpDeRegReceivedReqs_Object = MibScalar
cCdmaRpDeRegReceivedReqs = _CCdmaRpDeRegReceivedReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 1, 28),
    _CCdmaRpDeRegReceivedReqs_Type()
)
cCdmaRpDeRegReceivedReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpDeRegReceivedReqs.setStatus("current")
_CCdmaRpDeRegDiscardedReqs_Type = ZeroBasedCounter32
_CCdmaRpDeRegDiscardedReqs_Object = MibScalar
cCdmaRpDeRegDiscardedReqs = _CCdmaRpDeRegDiscardedReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 1, 29),
    _CCdmaRpDeRegDiscardedReqs_Type()
)
cCdmaRpDeRegDiscardedReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpDeRegDiscardedReqs.setStatus("current")
_CCdmaRpHandoffRegReceivedReqs_Type = ZeroBasedCounter32
_CCdmaRpHandoffRegReceivedReqs_Object = MibScalar
cCdmaRpHandoffRegReceivedReqs = _CCdmaRpHandoffRegReceivedReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 1, 30),
    _CCdmaRpHandoffRegReceivedReqs_Type()
)
cCdmaRpHandoffRegReceivedReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpHandoffRegReceivedReqs.setStatus("current")
_CCdmaRpHandoffRegAcceptedReqs_Type = ZeroBasedCounter32
_CCdmaRpHandoffRegAcceptedReqs_Object = MibScalar
cCdmaRpHandoffRegAcceptedReqs = _CCdmaRpHandoffRegAcceptedReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 1, 31),
    _CCdmaRpHandoffRegAcceptedReqs_Type()
)
cCdmaRpHandoffRegAcceptedReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpHandoffRegAcceptedReqs.setStatus("current")
_CCdmaRpHandoffRegDeniedReqs_Type = ZeroBasedCounter32
_CCdmaRpHandoffRegDeniedReqs_Object = MibScalar
cCdmaRpHandoffRegDeniedReqs = _CCdmaRpHandoffRegDeniedReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 1, 32),
    _CCdmaRpHandoffRegDeniedReqs_Type()
)
cCdmaRpHandoffRegDeniedReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpHandoffRegDeniedReqs.setStatus("current")
_CCdmaRpHandoffRegDiscardedReqs_Type = ZeroBasedCounter32
_CCdmaRpHandoffRegDiscardedReqs_Object = MibScalar
cCdmaRpHandoffRegDiscardedReqs = _CCdmaRpHandoffRegDiscardedReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 1, 33),
    _CCdmaRpHandoffRegDiscardedReqs_Type()
)
cCdmaRpHandoffRegDiscardedReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpHandoffRegDiscardedReqs.setStatus("current")
_CCdmaRpReRegAirlinkStarts_Type = ZeroBasedCounter32
_CCdmaRpReRegAirlinkStarts_Object = MibScalar
cCdmaRpReRegAirlinkStarts = _CCdmaRpReRegAirlinkStarts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 1, 34),
    _CCdmaRpReRegAirlinkStarts_Type()
)
cCdmaRpReRegAirlinkStarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpReRegAirlinkStarts.setStatus("current")
_CCdmaRpReRegAirlinkStops_Type = ZeroBasedCounter32
_CCdmaRpReRegAirlinkStops_Object = MibScalar
cCdmaRpReRegAirlinkStops = _CCdmaRpReRegAirlinkStops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 1, 35),
    _CCdmaRpReRegAirlinkStops_Type()
)
cCdmaRpReRegAirlinkStops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpReRegAirlinkStops.setStatus("current")
_CCdmaRpDeRegAirlinkStops_Type = ZeroBasedCounter32
_CCdmaRpDeRegAirlinkStops_Object = MibScalar
cCdmaRpDeRegAirlinkStops = _CCdmaRpDeRegAirlinkStops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 1, 36),
    _CCdmaRpDeRegAirlinkStops_Type()
)
cCdmaRpDeRegAirlinkStops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpDeRegAirlinkStops.setStatus("current")
_CCdmaRpInterPCFActiveHandoffs_Type = ZeroBasedCounter32
_CCdmaRpInterPCFActiveHandoffs_Object = MibScalar
cCdmaRpInterPCFActiveHandoffs = _CCdmaRpInterPCFActiveHandoffs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 1, 37),
    _CCdmaRpInterPCFActiveHandoffs_Type()
)
cCdmaRpInterPCFActiveHandoffs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpInterPCFActiveHandoffs.setStatus("current")
_CCdmaRpInterPCFDormantHandoffs_Type = ZeroBasedCounter32
_CCdmaRpInterPCFDormantHandoffs_Object = MibScalar
cCdmaRpInterPCFDormantHandoffs = _CCdmaRpInterPCFDormantHandoffs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 1, 38),
    _CCdmaRpInterPCFDormantHandoffs_Type()
)
cCdmaRpInterPCFDormantHandoffs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpInterPCFDormantHandoffs.setStatus("current")
_CCdmaRpUpdStats_ObjectIdentity = ObjectIdentity
cCdmaRpUpdStats = _CCdmaRpUpdStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 2)
)
_CCdmaRpUpdTransmittedReqs_Type = Counter32
_CCdmaRpUpdTransmittedReqs_Object = MibScalar
cCdmaRpUpdTransmittedReqs = _CCdmaRpUpdTransmittedReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 2, 1),
    _CCdmaRpUpdTransmittedReqs_Type()
)
cCdmaRpUpdTransmittedReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpUpdTransmittedReqs.setStatus("current")
_CCdmaRpUpdAcceptedReqs_Type = Counter32
_CCdmaRpUpdAcceptedReqs_Object = MibScalar
cCdmaRpUpdAcceptedReqs = _CCdmaRpUpdAcceptedReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 2, 2),
    _CCdmaRpUpdAcceptedReqs_Type()
)
cCdmaRpUpdAcceptedReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpUpdAcceptedReqs.setStatus("current")
_CCdmaRpUpdDeniedReqs_Type = Counter32
_CCdmaRpUpdDeniedReqs_Object = MibScalar
cCdmaRpUpdDeniedReqs = _CCdmaRpUpdDeniedReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 2, 3),
    _CCdmaRpUpdDeniedReqs_Type()
)
cCdmaRpUpdDeniedReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpUpdDeniedReqs.setStatus("current")
_CCdmaRpUpdNotAckedReqs_Type = Counter32
_CCdmaRpUpdNotAckedReqs_Object = MibScalar
cCdmaRpUpdNotAckedReqs = _CCdmaRpUpdNotAckedReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 2, 4),
    _CCdmaRpUpdNotAckedReqs_Type()
)
cCdmaRpUpdNotAckedReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpUpdNotAckedReqs.setStatus("current")
_CCdmaRpUpdInitTransmittedReqs_Type = Counter32
_CCdmaRpUpdInitTransmittedReqs_Object = MibScalar
cCdmaRpUpdInitTransmittedReqs = _CCdmaRpUpdInitTransmittedReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 2, 5),
    _CCdmaRpUpdInitTransmittedReqs_Type()
)
cCdmaRpUpdInitTransmittedReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpUpdInitTransmittedReqs.setStatus("current")
_CCdmaRpUpdReTransmittedReqs_Type = Counter32
_CCdmaRpUpdReTransmittedReqs_Object = MibScalar
cCdmaRpUpdReTransmittedReqs = _CCdmaRpUpdReTransmittedReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 2, 6),
    _CCdmaRpUpdReTransmittedReqs_Type()
)
cCdmaRpUpdReTransmittedReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpUpdReTransmittedReqs.setStatus("current")
_CCdmaRpUpdReceivedAcks_Type = Counter32
_CCdmaRpUpdReceivedAcks_Object = MibScalar
cCdmaRpUpdReceivedAcks = _CCdmaRpUpdReceivedAcks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 2, 7),
    _CCdmaRpUpdReceivedAcks_Type()
)
cCdmaRpUpdReceivedAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpUpdReceivedAcks.setStatus("current")
_CCdmaRpUpdDiscardedAcks_Type = Counter32
_CCdmaRpUpdDiscardedAcks_Object = MibScalar
cCdmaRpUpdDiscardedAcks = _CCdmaRpUpdDiscardedAcks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 2, 8),
    _CCdmaRpUpdDiscardedAcks_Type()
)
cCdmaRpUpdDiscardedAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpUpdDiscardedAcks.setStatus("current")
_CCdmaRpUpdRpLifeExpReqs_Type = Counter32
_CCdmaRpUpdRpLifeExpReqs_Object = MibScalar
cCdmaRpUpdRpLifeExpReqs = _CCdmaRpUpdRpLifeExpReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 2, 9),
    _CCdmaRpUpdRpLifeExpReqs_Type()
)
cCdmaRpUpdRpLifeExpReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpUpdRpLifeExpReqs.setStatus("current")
_CCdmaRpUpdPPPtermReqs_Type = Counter32
_CCdmaRpUpdPPPtermReqs_Object = MibScalar
cCdmaRpUpdPPPtermReqs = _CCdmaRpUpdPPPtermReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 2, 10),
    _CCdmaRpUpdPPPtermReqs_Type()
)
cCdmaRpUpdPPPtermReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpUpdPPPtermReqs.setStatus("current")
_CCdmaRpUpdOtherReasonReqs_Type = Counter32
_CCdmaRpUpdOtherReasonReqs_Object = MibScalar
cCdmaRpUpdOtherReasonReqs = _CCdmaRpUpdOtherReasonReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 2, 11),
    _CCdmaRpUpdOtherReasonReqs_Type()
)
cCdmaRpUpdOtherReasonReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpUpdOtherReasonReqs.setStatus("current")
_CCdmaRpUpdReasonUnSpecFailures_Type = Counter32
_CCdmaRpUpdReasonUnSpecFailures_Object = MibScalar
cCdmaRpUpdReasonUnSpecFailures = _CCdmaRpUpdReasonUnSpecFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 2, 12),
    _CCdmaRpUpdReasonUnSpecFailures_Type()
)
cCdmaRpUpdReasonUnSpecFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpUpdReasonUnSpecFailures.setStatus("current")
_CCdmaRpUpdAdminProhibFailures_Type = Counter32
_CCdmaRpUpdAdminProhibFailures_Object = MibScalar
cCdmaRpUpdAdminProhibFailures = _CCdmaRpUpdAdminProhibFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 2, 13),
    _CCdmaRpUpdAdminProhibFailures_Type()
)
cCdmaRpUpdAdminProhibFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpUpdAdminProhibFailures.setStatus("current")
_CCdmaRpUpdMNAuthenFailures_Type = Counter32
_CCdmaRpUpdMNAuthenFailures_Object = MibScalar
cCdmaRpUpdMNAuthenFailures = _CCdmaRpUpdMNAuthenFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 2, 14),
    _CCdmaRpUpdMNAuthenFailures_Type()
)
cCdmaRpUpdMNAuthenFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpUpdMNAuthenFailures.setStatus("current")
_CCdmaRpUpdIdentMismatchFailures_Type = Counter32
_CCdmaRpUpdIdentMismatchFailures_Object = MibScalar
cCdmaRpUpdIdentMismatchFailures = _CCdmaRpUpdIdentMismatchFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 2, 15),
    _CCdmaRpUpdIdentMismatchFailures_Type()
)
cCdmaRpUpdIdentMismatchFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpUpdIdentMismatchFailures.setStatus("current")
_CCdmaRpUpdBadReqFailures_Type = Counter32
_CCdmaRpUpdBadReqFailures_Object = MibScalar
cCdmaRpUpdBadReqFailures = _CCdmaRpUpdBadReqFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 2, 16),
    _CCdmaRpUpdBadReqFailures_Type()
)
cCdmaRpUpdBadReqFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpUpdBadReqFailures.setStatus("current")
_CCdmaRpUpdPcfHandoffs_Type = Counter32
_CCdmaRpUpdPcfHandoffs_Object = MibScalar
cCdmaRpUpdPcfHandoffs = _CCdmaRpUpdPcfHandoffs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 2, 17),
    _CCdmaRpUpdPcfHandoffs_Type()
)
cCdmaRpUpdPcfHandoffs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpUpdPcfHandoffs.setStatus("current")
_CCdmaRpUpdHandoffNotAckedReqs_Type = Counter32
_CCdmaRpUpdHandoffNotAckedReqs_Object = MibScalar
cCdmaRpUpdHandoffNotAckedReqs = _CCdmaRpUpdHandoffNotAckedReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 2, 18),
    _CCdmaRpUpdHandoffNotAckedReqs_Type()
)
cCdmaRpUpdHandoffNotAckedReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpUpdHandoffNotAckedReqs.setStatus("current")
_CCdmaRpUpdHandoffReceivedAcks_Type = Counter32
_CCdmaRpUpdHandoffReceivedAcks_Object = MibScalar
cCdmaRpUpdHandoffReceivedAcks = _CCdmaRpUpdHandoffReceivedAcks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 2, 19),
    _CCdmaRpUpdHandoffReceivedAcks_Type()
)
cCdmaRpUpdHandoffReceivedAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpUpdHandoffReceivedAcks.setStatus("current")
_CCdmaRpUpdHandoffAcceptedReqs_Type = Counter32
_CCdmaRpUpdHandoffAcceptedReqs_Object = MibScalar
cCdmaRpUpdHandoffAcceptedReqs = _CCdmaRpUpdHandoffAcceptedReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 2, 20),
    _CCdmaRpUpdHandoffAcceptedReqs_Type()
)
cCdmaRpUpdHandoffAcceptedReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpUpdHandoffAcceptedReqs.setStatus("current")
_CCdmaRpUpdHandoffDeniedReqs_Type = Counter32
_CCdmaRpUpdHandoffDeniedReqs_Object = MibScalar
cCdmaRpUpdHandoffDeniedReqs = _CCdmaRpUpdHandoffDeniedReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 2, 21),
    _CCdmaRpUpdHandoffDeniedReqs_Type()
)
cCdmaRpUpdHandoffDeniedReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpUpdHandoffDeniedReqs.setStatus("current")
_CCdmaRpUpdHandoffDiscardedAcks_Type = Counter32
_CCdmaRpUpdHandoffDiscardedAcks_Object = MibScalar
cCdmaRpUpdHandoffDiscardedAcks = _CCdmaRpUpdHandoffDiscardedAcks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 2, 22),
    _CCdmaRpUpdHandoffDiscardedAcks_Type()
)
cCdmaRpUpdHandoffDiscardedAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpUpdHandoffDiscardedAcks.setStatus("current")
_CCdmaRpUpdHandoffInitTxdReqs_Type = Counter32
_CCdmaRpUpdHandoffInitTxdReqs_Object = MibScalar
cCdmaRpUpdHandoffInitTxdReqs = _CCdmaRpUpdHandoffInitTxdReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 2, 23),
    _CCdmaRpUpdHandoffInitTxdReqs_Type()
)
cCdmaRpUpdHandoffInitTxdReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpUpdHandoffInitTxdReqs.setStatus("current")
_CCdmaRpUpdHandoffReTxdReqs_Type = Counter32
_CCdmaRpUpdHandoffReTxdReqs_Object = MibScalar
cCdmaRpUpdHandoffReTxdReqs = _CCdmaRpUpdHandoffReTxdReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 2, 24),
    _CCdmaRpUpdHandoffReTxdReqs_Type()
)
cCdmaRpUpdHandoffReTxdReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpUpdHandoffReTxdReqs.setStatus("current")
_CCdmaRpUpdHandoffReaUnSpecFails_Type = Counter32
_CCdmaRpUpdHandoffReaUnSpecFails_Object = MibScalar
cCdmaRpUpdHandoffReaUnSpecFails = _CCdmaRpUpdHandoffReaUnSpecFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 2, 25),
    _CCdmaRpUpdHandoffReaUnSpecFails_Type()
)
cCdmaRpUpdHandoffReaUnSpecFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpUpdHandoffReaUnSpecFails.setStatus("current")
_CCdmaRpUpdHandoffAdmProhibFails_Type = Counter32
_CCdmaRpUpdHandoffAdmProhibFails_Object = MibScalar
cCdmaRpUpdHandoffAdmProhibFails = _CCdmaRpUpdHandoffAdmProhibFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 2, 26),
    _CCdmaRpUpdHandoffAdmProhibFails_Type()
)
cCdmaRpUpdHandoffAdmProhibFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpUpdHandoffAdmProhibFails.setStatus("current")
_CCdmaRpUpdHandoffMNAuthenFails_Type = Counter32
_CCdmaRpUpdHandoffMNAuthenFails_Object = MibScalar
cCdmaRpUpdHandoffMNAuthenFails = _CCdmaRpUpdHandoffMNAuthenFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 2, 27),
    _CCdmaRpUpdHandoffMNAuthenFails_Type()
)
cCdmaRpUpdHandoffMNAuthenFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpUpdHandoffMNAuthenFails.setStatus("current")
_CCdmaRpUpdHandoffIdMismatchFails_Type = Counter32
_CCdmaRpUpdHandoffIdMismatchFails_Object = MibScalar
cCdmaRpUpdHandoffIdMismatchFails = _CCdmaRpUpdHandoffIdMismatchFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 2, 28),
    _CCdmaRpUpdHandoffIdMismatchFails_Type()
)
cCdmaRpUpdHandoffIdMismatchFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpUpdHandoffIdMismatchFails.setStatus("current")
_CCdmaRpUpdHandoffBadReqFails_Type = Counter32
_CCdmaRpUpdHandoffBadReqFails_Object = MibScalar
cCdmaRpUpdHandoffBadReqFails = _CCdmaRpUpdHandoffBadReqFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 2, 29),
    _CCdmaRpUpdHandoffBadReqFails_Type()
)
cCdmaRpUpdHandoffBadReqFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpUpdHandoffBadReqFails.setStatus("current")
_CCdmaPppStats_ObjectIdentity = ObjectIdentity
cCdmaPppStats = _CCdmaPppStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3)
)
_CCdmaPppSetupStats_ObjectIdentity = ObjectIdentity
cCdmaPppSetupStats = _CCdmaPppSetupStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 1)
)
_CCdmaPppCurrentConnections_Type = Gauge32
_CCdmaPppCurrentConnections_Object = MibScalar
cCdmaPppCurrentConnections = _CCdmaPppCurrentConnections_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 1, 1),
    _CCdmaPppCurrentConnections_Type()
)
cCdmaPppCurrentConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppCurrentConnections.setStatus("current")
_CCdmaPppConnectionInitiateReqs_Type = Counter32
_CCdmaPppConnectionInitiateReqs_Object = MibScalar
cCdmaPppConnectionInitiateReqs = _CCdmaPppConnectionInitiateReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 1, 2),
    _CCdmaPppConnectionInitiateReqs_Type()
)
cCdmaPppConnectionInitiateReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppConnectionInitiateReqs.setStatus("current")
_CCdmaPppConnectionSuccesses_Type = Counter32
_CCdmaPppConnectionSuccesses_Object = MibScalar
cCdmaPppConnectionSuccesses = _CCdmaPppConnectionSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 1, 3),
    _CCdmaPppConnectionSuccesses_Type()
)
cCdmaPppConnectionSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppConnectionSuccesses.setStatus("current")
_CCdmaPppConnectionFailures_Type = Counter32
_CCdmaPppConnectionFailures_Object = MibScalar
cCdmaPppConnectionFailures = _CCdmaPppConnectionFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 1, 4),
    _CCdmaPppConnectionFailures_Type()
)
cCdmaPppConnectionFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppConnectionFailures.setStatus("current")
_CCdmaPppLcpFailures_Type = Counter32
_CCdmaPppLcpFailures_Object = MibScalar
cCdmaPppLcpFailures = _CCdmaPppLcpFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 1, 5),
    _CCdmaPppLcpFailures_Type()
)
cCdmaPppLcpFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppLcpFailures.setStatus("current")
_CCdmaPppAuthFailures_Type = Counter32
_CCdmaPppAuthFailures_Object = MibScalar
cCdmaPppAuthFailures = _CCdmaPppAuthFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 1, 6),
    _CCdmaPppAuthFailures_Type()
)
cCdmaPppAuthFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppAuthFailures.setStatus("current")
_CCdmaPppIpcpFailures_Type = Counter32
_CCdmaPppIpcpFailures_Object = MibScalar
cCdmaPppIpcpFailures = _CCdmaPppIpcpFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 1, 7),
    _CCdmaPppIpcpFailures_Type()
)
cCdmaPppIpcpFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppIpcpFailures.setStatus("current")
_CCdmaPppEnterLcpNums_Type = Counter32
_CCdmaPppEnterLcpNums_Object = MibScalar
cCdmaPppEnterLcpNums = _CCdmaPppEnterLcpNums_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 1, 8),
    _CCdmaPppEnterLcpNums_Type()
)
cCdmaPppEnterLcpNums.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppEnterLcpNums.setStatus("current")
_CCdmaPppEnterAuthNums_Type = Counter32
_CCdmaPppEnterAuthNums_Object = MibScalar
cCdmaPppEnterAuthNums = _CCdmaPppEnterAuthNums_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 1, 9),
    _CCdmaPppEnterAuthNums_Type()
)
cCdmaPppEnterAuthNums.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppEnterAuthNums.setStatus("current")
_CCdmaPppEnterIpcpNums_Type = Counter32
_CCdmaPppEnterIpcpNums_Object = MibScalar
cCdmaPppEnterIpcpNums = _CCdmaPppEnterIpcpNums_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 1, 10),
    _CCdmaPppEnterIpcpNums_Type()
)
cCdmaPppEnterIpcpNums.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppEnterIpcpNums.setStatus("current")
_CCdmaPppLcpFailuresMaxRetrans_Type = ZeroBasedCounter32
_CCdmaPppLcpFailuresMaxRetrans_Object = MibScalar
cCdmaPppLcpFailuresMaxRetrans = _CCdmaPppLcpFailuresMaxRetrans_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 1, 11),
    _CCdmaPppLcpFailuresMaxRetrans_Type()
)
cCdmaPppLcpFailuresMaxRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppLcpFailuresMaxRetrans.setStatus("current")
_CCdmaPppLcpFailuresUnknown_Type = ZeroBasedCounter32
_CCdmaPppLcpFailuresUnknown_Object = MibScalar
cCdmaPppLcpFailuresUnknown = _CCdmaPppLcpFailuresUnknown_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 1, 12),
    _CCdmaPppLcpFailuresUnknown_Type()
)
cCdmaPppLcpFailuresUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppLcpFailuresUnknown.setStatus("current")
_CCdmaPppIpcpFailuresMaxRetrans_Type = ZeroBasedCounter32
_CCdmaPppIpcpFailuresMaxRetrans_Object = MibScalar
cCdmaPppIpcpFailuresMaxRetrans = _CCdmaPppIpcpFailuresMaxRetrans_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 1, 13),
    _CCdmaPppIpcpFailuresMaxRetrans_Type()
)
cCdmaPppIpcpFailuresMaxRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppIpcpFailuresMaxRetrans.setStatus("current")
_CCdmaPppIpcpFailuresUnknown_Type = ZeroBasedCounter32
_CCdmaPppIpcpFailuresUnknown_Object = MibScalar
cCdmaPppIpcpFailuresUnknown = _CCdmaPppIpcpFailuresUnknown_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 1, 14),
    _CCdmaPppIpcpFailuresUnknown_Type()
)
cCdmaPppIpcpFailuresUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppIpcpFailuresUnknown.setStatus("current")
_CCdmaPppConnectionsAborted_Type = ZeroBasedCounter32
_CCdmaPppConnectionsAborted_Object = MibScalar
cCdmaPppConnectionsAborted = _CCdmaPppConnectionsAborted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 1, 15),
    _CCdmaPppConnectionsAborted_Type()
)
cCdmaPppConnectionsAborted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppConnectionsAborted.setStatus("current")
_CCdmaPppLcpOptionIssueFailures_Type = ZeroBasedCounter32
_CCdmaPppLcpOptionIssueFailures_Object = MibScalar
cCdmaPppLcpOptionIssueFailures = _CCdmaPppLcpOptionIssueFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 1, 16),
    _CCdmaPppLcpOptionIssueFailures_Type()
)
cCdmaPppLcpOptionIssueFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppLcpOptionIssueFailures.setStatus("current")
_CCdmaPppIpcpOptionIssueFailures_Type = ZeroBasedCounter32
_CCdmaPppIpcpOptionIssueFailures_Object = MibScalar
cCdmaPppIpcpOptionIssueFailures = _CCdmaPppIpcpOptionIssueFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 1, 17),
    _CCdmaPppIpcpOptionIssueFailures_Type()
)
cCdmaPppIpcpOptionIssueFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppIpcpOptionIssueFailures.setStatus("current")
_CCdmaPppAuthMaxRetransFailures_Type = ZeroBasedCounter32
_CCdmaPppAuthMaxRetransFailures_Object = MibScalar
cCdmaPppAuthMaxRetransFailures = _CCdmaPppAuthMaxRetransFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 1, 18),
    _CCdmaPppAuthMaxRetransFailures_Type()
)
cCdmaPppAuthMaxRetransFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppAuthMaxRetransFailures.setStatus("current")
_CCdmaPppNoRemoteIpAddressReleases_Type = ZeroBasedCounter32
_CCdmaPppNoRemoteIpAddressReleases_Object = MibScalar
cCdmaPppNoRemoteIpAddressReleases = _CCdmaPppNoRemoteIpAddressReleases_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 1, 19),
    _CCdmaPppNoRemoteIpAddressReleases_Type()
)
cCdmaPppNoRemoteIpAddressReleases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppNoRemoteIpAddressReleases.setStatus("current")
_CCdmaPppLowerLayerReleaseFailures_Type = ZeroBasedCounter32
_CCdmaPppLowerLayerReleaseFailures_Object = MibScalar
cCdmaPppLowerLayerReleaseFailures = _CCdmaPppLowerLayerReleaseFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 1, 20),
    _CCdmaPppLowerLayerReleaseFailures_Type()
)
cCdmaPppLowerLayerReleaseFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppLowerLayerReleaseFailures.setStatus("current")
_CCdmaPppIpcpPhaseReceivedTermreqs_Type = ZeroBasedCounter32
_CCdmaPppIpcpPhaseReceivedTermreqs_Object = MibScalar
cCdmaPppIpcpPhaseReceivedTermreqs = _CCdmaPppIpcpPhaseReceivedTermreqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 1, 21),
    _CCdmaPppIpcpPhaseReceivedTermreqs_Type()
)
cCdmaPppIpcpPhaseReceivedTermreqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppIpcpPhaseReceivedTermreqs.setStatus("current")
_CCdmaPppIpcpPhaseSentTermreqs_Type = ZeroBasedCounter32
_CCdmaPppIpcpPhaseSentTermreqs_Object = MibScalar
cCdmaPppIpcpPhaseSentTermreqs = _CCdmaPppIpcpPhaseSentTermreqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 1, 22),
    _CCdmaPppIpcpPhaseSentTermreqs_Type()
)
cCdmaPppIpcpPhaseSentTermreqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppIpcpPhaseSentTermreqs.setStatus("current")
_CCdmaPppAuthPhaseReceivedTermreqs_Type = ZeroBasedCounter32
_CCdmaPppAuthPhaseReceivedTermreqs_Object = MibScalar
cCdmaPppAuthPhaseReceivedTermreqs = _CCdmaPppAuthPhaseReceivedTermreqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 1, 23),
    _CCdmaPppAuthPhaseReceivedTermreqs_Type()
)
cCdmaPppAuthPhaseReceivedTermreqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppAuthPhaseReceivedTermreqs.setStatus("current")
_CCdmaPppAuthPhaseSentTermreqs_Type = ZeroBasedCounter32
_CCdmaPppAuthPhaseSentTermreqs_Object = MibScalar
cCdmaPppAuthPhaseSentTermreqs = _CCdmaPppAuthPhaseSentTermreqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 1, 24),
    _CCdmaPppAuthPhaseSentTermreqs_Type()
)
cCdmaPppAuthPhaseSentTermreqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppAuthPhaseSentTermreqs.setStatus("current")
_CCdmaPppLcpPhaseReceivedTermreqs_Type = ZeroBasedCounter32
_CCdmaPppLcpPhaseReceivedTermreqs_Object = MibScalar
cCdmaPppLcpPhaseReceivedTermreqs = _CCdmaPppLcpPhaseReceivedTermreqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 1, 25),
    _CCdmaPppLcpPhaseReceivedTermreqs_Type()
)
cCdmaPppLcpPhaseReceivedTermreqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppLcpPhaseReceivedTermreqs.setStatus("current")
_CCdmaPppLcpPhaseSentTermreqs_Type = ZeroBasedCounter32
_CCdmaPppLcpPhaseSentTermreqs_Object = MibScalar
cCdmaPppLcpPhaseSentTermreqs = _CCdmaPppLcpPhaseSentTermreqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 1, 26),
    _CCdmaPppLcpPhaseSentTermreqs_Type()
)
cCdmaPppLcpPhaseSentTermreqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppLcpPhaseSentTermreqs.setStatus("current")
_CCdmaPppPreLCPPdsnA10Releases_Type = ZeroBasedCounter32
_CCdmaPppPreLCPPdsnA10Releases_Object = MibScalar
cCdmaPppPreLCPPdsnA10Releases = _CCdmaPppPreLCPPdsnA10Releases_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 1, 27),
    _CCdmaPppPreLCPPdsnA10Releases_Type()
)
cCdmaPppPreLCPPdsnA10Releases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppPreLCPPdsnA10Releases.setStatus("current")
_CCdmaPppPreLCPPcfA10Releases_Type = ZeroBasedCounter32
_CCdmaPppPreLCPPcfA10Releases_Object = MibScalar
cCdmaPppPreLCPPcfA10Releases = _CCdmaPppPreLCPPcfA10Releases_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 1, 28),
    _CCdmaPppPreLCPPcfA10Releases_Type()
)
cCdmaPppPreLCPPcfA10Releases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppPreLCPPcfA10Releases.setStatus("current")
_CCdmaPppLCPPdsnA10Releases_Type = ZeroBasedCounter32
_CCdmaPppLCPPdsnA10Releases_Object = MibScalar
cCdmaPppLCPPdsnA10Releases = _CCdmaPppLCPPdsnA10Releases_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 1, 29),
    _CCdmaPppLCPPdsnA10Releases_Type()
)
cCdmaPppLCPPdsnA10Releases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppLCPPdsnA10Releases.setStatus("current")
_CCdmaPppLCPPcfA10Releases_Type = ZeroBasedCounter32
_CCdmaPppLCPPcfA10Releases_Object = MibScalar
cCdmaPppLCPPcfA10Releases = _CCdmaPppLCPPcfA10Releases_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 1, 30),
    _CCdmaPppLCPPcfA10Releases_Type()
)
cCdmaPppLCPPcfA10Releases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppLCPPcfA10Releases.setStatus("current")
_CCdmaPppAuthPdsnA10Releases_Type = ZeroBasedCounter32
_CCdmaPppAuthPdsnA10Releases_Object = MibScalar
cCdmaPppAuthPdsnA10Releases = _CCdmaPppAuthPdsnA10Releases_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 1, 31),
    _CCdmaPppAuthPdsnA10Releases_Type()
)
cCdmaPppAuthPdsnA10Releases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppAuthPdsnA10Releases.setStatus("current")
_CCdmaPppAuthPcfA10Releases_Type = ZeroBasedCounter32
_CCdmaPppAuthPcfA10Releases_Object = MibScalar
cCdmaPppAuthPcfA10Releases = _CCdmaPppAuthPcfA10Releases_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 1, 32),
    _CCdmaPppAuthPcfA10Releases_Type()
)
cCdmaPppAuthPcfA10Releases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppAuthPcfA10Releases.setStatus("current")
_CCdmaPppIPCPPdsnA10Releases_Type = ZeroBasedCounter32
_CCdmaPppIPCPPdsnA10Releases_Object = MibScalar
cCdmaPppIPCPPdsnA10Releases = _CCdmaPppIPCPPdsnA10Releases_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 1, 33),
    _CCdmaPppIPCPPdsnA10Releases_Type()
)
cCdmaPppIPCPPdsnA10Releases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppIPCPPdsnA10Releases.setStatus("current")
_CCdmaPppIPCPPcfA10Releases_Type = ZeroBasedCounter32
_CCdmaPppIPCPPcfA10Releases_Object = MibScalar
cCdmaPppIPCPPcfA10Releases = _CCdmaPppIPCPPcfA10Releases_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 1, 34),
    _CCdmaPppIPCPPcfA10Releases_Type()
)
cCdmaPppIPCPPcfA10Releases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppIPCPPcfA10Releases.setStatus("current")
_CCdmaPppLcpSuccesses_Type = ZeroBasedCounter32
_CCdmaPppLcpSuccesses_Object = MibScalar
cCdmaPppLcpSuccesses = _CCdmaPppLcpSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 1, 35),
    _CCdmaPppLcpSuccesses_Type()
)
cCdmaPppLcpSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppLcpSuccesses.setStatus("current")
_CCdmaPppIpcpSuccesses_Type = ZeroBasedCounter32
_CCdmaPppIpcpSuccesses_Object = MibScalar
cCdmaPppIpcpSuccesses = _CCdmaPppIpcpSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 1, 36),
    _CCdmaPppIpcpSuccesses_Type()
)
cCdmaPppIpcpSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppIpcpSuccesses.setStatus("current")
_CCdmaPppAuthSuccesses_Type = ZeroBasedCounter32
_CCdmaPppAuthSuccesses_Object = MibScalar
cCdmaPppAuthSuccesses = _CCdmaPppAuthSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 1, 37),
    _CCdmaPppAuthSuccesses_Type()
)
cCdmaPppAuthSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppAuthSuccesses.setStatus("current")
_CCdmaPppConnectionOtherFailures_Type = ZeroBasedCounter32
_CCdmaPppConnectionOtherFailures_Object = MibScalar
cCdmaPppConnectionOtherFailures = _CCdmaPppConnectionOtherFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 1, 38),
    _CCdmaPppConnectionOtherFailures_Type()
)
cCdmaPppConnectionOtherFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppConnectionOtherFailures.setStatus("current")
_CCdmaPppReNegoStats_ObjectIdentity = ObjectIdentity
cCdmaPppReNegoStats = _CCdmaPppReNegoStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 2)
)
_CCdmaPppRenegTotalReqs_Type = Counter32
_CCdmaPppRenegTotalReqs_Object = MibScalar
cCdmaPppRenegTotalReqs = _CCdmaPppRenegTotalReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 2, 1),
    _CCdmaPppRenegTotalReqs_Type()
)
cCdmaPppRenegTotalReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppRenegTotalReqs.setStatus("current")
_CCdmaPppRenegByPdsnReqs_Type = Counter32
_CCdmaPppRenegByPdsnReqs_Object = MibScalar
cCdmaPppRenegByPdsnReqs = _CCdmaPppRenegByPdsnReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 2, 2),
    _CCdmaPppRenegByPdsnReqs_Type()
)
cCdmaPppRenegByPdsnReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppRenegByPdsnReqs.setStatus("current")
_CCdmaPppRenegByMobileReqs_Type = Counter32
_CCdmaPppRenegByMobileReqs_Object = MibScalar
cCdmaPppRenegByMobileReqs = _CCdmaPppRenegByMobileReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 2, 3),
    _CCdmaPppRenegByMobileReqs_Type()
)
cCdmaPppRenegByMobileReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppRenegByMobileReqs.setStatus("current")
_CCdmaPppRenegLcpIpcpReqs_Type = Counter32
_CCdmaPppRenegLcpIpcpReqs_Object = MibScalar
cCdmaPppRenegLcpIpcpReqs = _CCdmaPppRenegLcpIpcpReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 2, 4),
    _CCdmaPppRenegLcpIpcpReqs_Type()
)
cCdmaPppRenegLcpIpcpReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppRenegLcpIpcpReqs.setStatus("current")
_CCdmaPppRenegAddrMismatchReqs_Type = Counter32
_CCdmaPppRenegAddrMismatchReqs_Object = MibScalar
cCdmaPppRenegAddrMismatchReqs = _CCdmaPppRenegAddrMismatchReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 2, 5),
    _CCdmaPppRenegAddrMismatchReqs_Type()
)
cCdmaPppRenegAddrMismatchReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppRenegAddrMismatchReqs.setStatus("current")
_CCdmaPppRenegOtherReasonReqs_Type = Counter32
_CCdmaPppRenegOtherReasonReqs_Object = MibScalar
cCdmaPppRenegOtherReasonReqs = _CCdmaPppRenegOtherReasonReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 2, 10),
    _CCdmaPppRenegOtherReasonReqs_Type()
)
cCdmaPppRenegOtherReasonReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppRenegOtherReasonReqs.setStatus("current")
_CCdmaPppRenegSuccesses_Type = ZeroBasedCounter32
_CCdmaPppRenegSuccesses_Object = MibScalar
cCdmaPppRenegSuccesses = _CCdmaPppRenegSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 2, 11),
    _CCdmaPppRenegSuccesses_Type()
)
cCdmaPppRenegSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppRenegSuccesses.setStatus("current")
_CCdmaPppRenegFailures_Type = ZeroBasedCounter32
_CCdmaPppRenegFailures_Object = MibScalar
cCdmaPppRenegFailures = _CCdmaPppRenegFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 2, 12),
    _CCdmaPppRenegFailures_Type()
)
cCdmaPppRenegFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppRenegFailures.setStatus("current")
_CCdmaPppRenegConnectionsAborted_Type = ZeroBasedCounter32
_CCdmaPppRenegConnectionsAborted_Object = MibScalar
cCdmaPppRenegConnectionsAborted = _CCdmaPppRenegConnectionsAborted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 2, 13),
    _CCdmaPppRenegConnectionsAborted_Type()
)
cCdmaPppRenegConnectionsAborted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppRenegConnectionsAborted.setStatus("current")
_CCdmaPppRenegAnidChanges_Type = ZeroBasedCounter32
_CCdmaPppRenegAnidChanges_Object = MibScalar
cCdmaPppRenegAnidChanges = _CCdmaPppRenegAnidChanges_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 2, 14),
    _CCdmaPppRenegAnidChanges_Type()
)
cCdmaPppRenegAnidChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppRenegAnidChanges.setStatus("current")
_CCdmaPppAuthStats_ObjectIdentity = ObjectIdentity
cCdmaPppAuthStats = _CCdmaPppAuthStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 3)
)
_CCdmaPppAuthChapAttempts_Type = Counter32
_CCdmaPppAuthChapAttempts_Object = MibScalar
cCdmaPppAuthChapAttempts = _CCdmaPppAuthChapAttempts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 3, 1),
    _CCdmaPppAuthChapAttempts_Type()
)
cCdmaPppAuthChapAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppAuthChapAttempts.setStatus("current")
_CCdmaPppAuthChapSuccesses_Type = Counter32
_CCdmaPppAuthChapSuccesses_Object = MibScalar
cCdmaPppAuthChapSuccesses = _CCdmaPppAuthChapSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 3, 2),
    _CCdmaPppAuthChapSuccesses_Type()
)
cCdmaPppAuthChapSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppAuthChapSuccesses.setStatus("current")
_CCdmaPppAuthChapFailures_Type = Counter32
_CCdmaPppAuthChapFailures_Object = MibScalar
cCdmaPppAuthChapFailures = _CCdmaPppAuthChapFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 3, 3),
    _CCdmaPppAuthChapFailures_Type()
)
cCdmaPppAuthChapFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppAuthChapFailures.setStatus("current")
_CCdmaPppAuthPapAttempts_Type = Counter32
_CCdmaPppAuthPapAttempts_Object = MibScalar
cCdmaPppAuthPapAttempts = _CCdmaPppAuthPapAttempts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 3, 4),
    _CCdmaPppAuthPapAttempts_Type()
)
cCdmaPppAuthPapAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppAuthPapAttempts.setStatus("current")
_CCdmaPppAuthPapSuccesses_Type = Counter32
_CCdmaPppAuthPapSuccesses_Object = MibScalar
cCdmaPppAuthPapSuccesses = _CCdmaPppAuthPapSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 3, 5),
    _CCdmaPppAuthPapSuccesses_Type()
)
cCdmaPppAuthPapSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppAuthPapSuccesses.setStatus("current")
_CCdmaPppAuthPapFailures_Type = Counter32
_CCdmaPppAuthPapFailures_Object = MibScalar
cCdmaPppAuthPapFailures = _CCdmaPppAuthPapFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 3, 6),
    _CCdmaPppAuthPapFailures_Type()
)
cCdmaPppAuthPapFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppAuthPapFailures.setStatus("current")
_CCdmaPppAuthMschapAttempts_Type = Counter32
_CCdmaPppAuthMschapAttempts_Object = MibScalar
cCdmaPppAuthMschapAttempts = _CCdmaPppAuthMschapAttempts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 3, 7),
    _CCdmaPppAuthMschapAttempts_Type()
)
cCdmaPppAuthMschapAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppAuthMschapAttempts.setStatus("current")
_CCdmaPppAuthMschapSuccesses_Type = Counter32
_CCdmaPppAuthMschapSuccesses_Object = MibScalar
cCdmaPppAuthMschapSuccesses = _CCdmaPppAuthMschapSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 3, 8),
    _CCdmaPppAuthMschapSuccesses_Type()
)
cCdmaPppAuthMschapSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppAuthMschapSuccesses.setStatus("current")
_CCdmaPppAuthMschapFailures_Type = Counter32
_CCdmaPppAuthMschapFailures_Object = MibScalar
cCdmaPppAuthMschapFailures = _CCdmaPppAuthMschapFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 3, 9),
    _CCdmaPppAuthMschapFailures_Type()
)
cCdmaPppAuthMschapFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppAuthMschapFailures.setStatus("current")
_CCdmaPppAuthEapAttempts_Type = Counter32
_CCdmaPppAuthEapAttempts_Object = MibScalar
cCdmaPppAuthEapAttempts = _CCdmaPppAuthEapAttempts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 3, 10),
    _CCdmaPppAuthEapAttempts_Type()
)
cCdmaPppAuthEapAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppAuthEapAttempts.setStatus("current")
_CCdmaPppAuthEapSuccesses_Type = Counter32
_CCdmaPppAuthEapSuccesses_Object = MibScalar
cCdmaPppAuthEapSuccesses = _CCdmaPppAuthEapSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 3, 11),
    _CCdmaPppAuthEapSuccesses_Type()
)
cCdmaPppAuthEapSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppAuthEapSuccesses.setStatus("current")
_CCdmaPppAuthEapFailures_Type = Counter32
_CCdmaPppAuthEapFailures_Object = MibScalar
cCdmaPppAuthEapFailures = _CCdmaPppAuthEapFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 3, 12),
    _CCdmaPppAuthEapFailures_Type()
)
cCdmaPppAuthEapFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppAuthEapFailures.setStatus("current")
_CCdmaPppAuthMsidAttempts_Type = Counter32
_CCdmaPppAuthMsidAttempts_Object = MibScalar
cCdmaPppAuthMsidAttempts = _CCdmaPppAuthMsidAttempts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 3, 13),
    _CCdmaPppAuthMsidAttempts_Type()
)
cCdmaPppAuthMsidAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppAuthMsidAttempts.setStatus("current")
_CCdmaPppAuthMsidSuccesses_Type = Counter32
_CCdmaPppAuthMsidSuccesses_Object = MibScalar
cCdmaPppAuthMsidSuccesses = _CCdmaPppAuthMsidSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 3, 14),
    _CCdmaPppAuthMsidSuccesses_Type()
)
cCdmaPppAuthMsidSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppAuthMsidSuccesses.setStatus("current")
_CCdmaPppAuthMsidFailures_Type = Counter32
_CCdmaPppAuthMsidFailures_Object = MibScalar
cCdmaPppAuthMsidFailures = _CCdmaPppAuthMsidFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 3, 15),
    _CCdmaPppAuthMsidFailures_Type()
)
cCdmaPppAuthMsidFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppAuthMsidFailures.setStatus("current")
_CCdmaPppAuthAAATimeouts_Type = Counter32
_CCdmaPppAuthAAATimeouts_Object = MibScalar
cCdmaPppAuthAAATimeouts = _CCdmaPppAuthAAATimeouts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 3, 16),
    _CCdmaPppAuthAAATimeouts_Type()
)
cCdmaPppAuthAAATimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppAuthAAATimeouts.setStatus("current")
_CCdmaPppAuthChapTimeouts_Type = ZeroBasedCounter32
_CCdmaPppAuthChapTimeouts_Object = MibScalar
cCdmaPppAuthChapTimeouts = _CCdmaPppAuthChapTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 3, 17),
    _CCdmaPppAuthChapTimeouts_Type()
)
cCdmaPppAuthChapTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppAuthChapTimeouts.setStatus("current")
_CCdmaPppAuthPapTimeouts_Type = ZeroBasedCounter32
_CCdmaPppAuthPapTimeouts_Object = MibScalar
cCdmaPppAuthPapTimeouts = _CCdmaPppAuthPapTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 3, 18),
    _CCdmaPppAuthPapTimeouts_Type()
)
cCdmaPppAuthPapTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppAuthPapTimeouts.setStatus("current")
_CCdmaPppAuthMschapTimeouts_Type = ZeroBasedCounter32
_CCdmaPppAuthMschapTimeouts_Object = MibScalar
cCdmaPppAuthMschapTimeouts = _CCdmaPppAuthMschapTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 3, 19),
    _CCdmaPppAuthMschapTimeouts_Type()
)
cCdmaPppAuthMschapTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppAuthMschapTimeouts.setStatus("current")
_CCdmaPppAuthSkips_Type = ZeroBasedCounter32
_CCdmaPppAuthSkips_Object = MibScalar
cCdmaPppAuthSkips = _CCdmaPppAuthSkips_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 3, 20),
    _CCdmaPppAuthSkips_Type()
)
cCdmaPppAuthSkips.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppAuthSkips.setStatus("current")
_CCdmaPppReleaseStats_ObjectIdentity = ObjectIdentity
cCdmaPppReleaseStats = _CCdmaPppReleaseStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 4)
)
_CCdmaPppTotalReleases_Type = Counter32
_CCdmaPppTotalReleases_Object = MibScalar
cCdmaPppTotalReleases = _CCdmaPppTotalReleases_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 4, 1),
    _CCdmaPppTotalReleases_Type()
)
cCdmaPppTotalReleases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppTotalReleases.setStatus("current")
_CCdmaPppPdsnReleases_Type = Counter32
_CCdmaPppPdsnReleases_Object = MibScalar
cCdmaPppPdsnReleases = _CCdmaPppPdsnReleases_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 4, 2),
    _CCdmaPppPdsnReleases_Type()
)
cCdmaPppPdsnReleases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppPdsnReleases.setStatus("current")
_CCdmaPppMobileReleases_Type = Counter32
_CCdmaPppMobileReleases_Object = MibScalar
cCdmaPppMobileReleases = _CCdmaPppMobileReleases_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 4, 3),
    _CCdmaPppMobileReleases_Type()
)
cCdmaPppMobileReleases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppMobileReleases.setStatus("current")
_CCdmaPppAddrFilterReleases_Type = Counter32
_CCdmaPppAddrFilterReleases_Object = MibScalar
cCdmaPppAddrFilterReleases = _CCdmaPppAddrFilterReleases_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 4, 4),
    _CCdmaPppAddrFilterReleases_Type()
)
cCdmaPppAddrFilterReleases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppAddrFilterReleases.setStatus("current")
_CCdmaPppAdminReleases_Type = Counter32
_CCdmaPppAdminReleases_Object = MibScalar
cCdmaPppAdminReleases = _CCdmaPppAdminReleases_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 4, 5),
    _CCdmaPppAdminReleases_Type()
)
cCdmaPppAdminReleases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppAdminReleases.setStatus("current")
_CCdmaPppLcpTermReleases_Type = Counter32
_CCdmaPppLcpTermReleases_Object = MibScalar
cCdmaPppLcpTermReleases = _CCdmaPppLcpTermReleases_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 4, 6),
    _CCdmaPppLcpTermReleases_Type()
)
cCdmaPppLcpTermReleases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppLcpTermReleases.setStatus("deprecated")
_CCdmaPppIdleTimeoutReleases_Type = Counter32
_CCdmaPppIdleTimeoutReleases_Object = MibScalar
cCdmaPppIdleTimeoutReleases = _CCdmaPppIdleTimeoutReleases_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 4, 7),
    _CCdmaPppIdleTimeoutReleases_Type()
)
cCdmaPppIdleTimeoutReleases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppIdleTimeoutReleases.setStatus("current")
_CCdmaPppL2tpTunnelReleases_Type = Counter32
_CCdmaPppL2tpTunnelReleases_Object = MibScalar
cCdmaPppL2tpTunnelReleases = _CCdmaPppL2tpTunnelReleases_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 4, 8),
    _CCdmaPppL2tpTunnelReleases_Type()
)
cCdmaPppL2tpTunnelReleases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppL2tpTunnelReleases.setStatus("current")
_CCdmaPppInsufResReleases_Type = Counter32
_CCdmaPppInsufResReleases_Object = MibScalar
cCdmaPppInsufResReleases = _CCdmaPppInsufResReleases_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 4, 9),
    _CCdmaPppInsufResReleases_Type()
)
cCdmaPppInsufResReleases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppInsufResReleases.setStatus("deprecated")
_CCdmaPppSessTimeoutReleases_Type = Counter32
_CCdmaPppSessTimeoutReleases_Object = MibScalar
cCdmaPppSessTimeoutReleases = _CCdmaPppSessTimeoutReleases_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 4, 10),
    _CCdmaPppSessTimeoutReleases_Type()
)
cCdmaPppSessTimeoutReleases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppSessTimeoutReleases.setStatus("current")
_CCdmaPppSrvIntReleases_Type = Counter32
_CCdmaPppSrvIntReleases_Object = MibScalar
cCdmaPppSrvIntReleases = _CCdmaPppSrvIntReleases_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 4, 11),
    _CCdmaPppSrvIntReleases_Type()
)
cCdmaPppSrvIntReleases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppSrvIntReleases.setStatus("current")
_CCdmaPppSrvUnavailReleases_Type = Counter32
_CCdmaPppSrvUnavailReleases_Object = MibScalar
cCdmaPppSrvUnavailReleases = _CCdmaPppSrvUnavailReleases_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 4, 12),
    _CCdmaPppSrvUnavailReleases_Type()
)
cCdmaPppSrvUnavailReleases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppSrvUnavailReleases.setStatus("current")
_CCdmaPppMissEchoReleases_Type = Counter32
_CCdmaPppMissEchoReleases_Object = MibScalar
cCdmaPppMissEchoReleases = _CCdmaPppMissEchoReleases_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 4, 13),
    _CCdmaPppMissEchoReleases_Type()
)
cCdmaPppMissEchoReleases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppMissEchoReleases.setStatus("current")
_CCdmaPppDeregisterByPcfReleases_Type = ZeroBasedCounter32
_CCdmaPppDeregisterByPcfReleases_Object = MibScalar
cCdmaPppDeregisterByPcfReleases = _CCdmaPppDeregisterByPcfReleases_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 4, 14),
    _CCdmaPppDeregisterByPcfReleases_Type()
)
cCdmaPppDeregisterByPcfReleases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppDeregisterByPcfReleases.setStatus("current")
_CCdmaPppLifetimeExpiryReleases_Type = ZeroBasedCounter32
_CCdmaPppLifetimeExpiryReleases_Object = MibScalar
cCdmaPppLifetimeExpiryReleases = _CCdmaPppLifetimeExpiryReleases_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 4, 15),
    _CCdmaPppLifetimeExpiryReleases_Type()
)
cCdmaPppLifetimeExpiryReleases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppLifetimeExpiryReleases.setStatus("current")
_CCdmaPppOtherReasonReleases_Type = Counter32
_CCdmaPppOtherReasonReleases_Object = MibScalar
cCdmaPppOtherReasonReleases = _CCdmaPppOtherReasonReleases_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 4, 99),
    _CCdmaPppOtherReasonReleases_Type()
)
cCdmaPppOtherReasonReleases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppOtherReasonReleases.setStatus("current")
_CCdmaPppMiscStats_ObjectIdentity = ObjectIdentity
cCdmaPppMiscStats = _CCdmaPppMiscStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 99)
)
_CCdmaPppCompressNegoCons_Type = Counter32
_CCdmaPppCompressNegoCons_Object = MibScalar
cCdmaPppCompressNegoCons = _CCdmaPppCompressNegoCons_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 99, 1),
    _CCdmaPppCompressNegoCons_Type()
)
cCdmaPppCompressNegoCons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppCompressNegoCons.setStatus("current")
_CCdmaPppCompressMsftCons_Type = Counter32
_CCdmaPppCompressMsftCons_Object = MibScalar
cCdmaPppCompressMsftCons = _CCdmaPppCompressMsftCons_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 99, 2),
    _CCdmaPppCompressMsftCons_Type()
)
cCdmaPppCompressMsftCons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppCompressMsftCons.setStatus("current")
_CCdmaPppCompressAscendCons_Type = Counter32
_CCdmaPppCompressAscendCons_Object = MibScalar
cCdmaPppCompressAscendCons = _CCdmaPppCompressAscendCons_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 99, 3),
    _CCdmaPppCompressAscendCons_Type()
)
cCdmaPppCompressAscendCons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppCompressAscendCons.setStatus("current")
_CCdmaPppCompressStackCons_Type = Counter32
_CCdmaPppCompressStackCons_Object = MibScalar
cCdmaPppCompressStackCons = _CCdmaPppCompressStackCons_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 99, 4),
    _CCdmaPppCompressStackCons_Type()
)
cCdmaPppCompressStackCons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppCompressStackCons.setStatus("current")
_CCdmaPppCompressDeflateCons_Type = Counter32
_CCdmaPppCompressDeflateCons_Object = MibScalar
cCdmaPppCompressDeflateCons = _CCdmaPppCompressDeflateCons_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 99, 5),
    _CCdmaPppCompressDeflateCons_Type()
)
cCdmaPppCompressDeflateCons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppCompressDeflateCons.setStatus("current")
_CCdmaPppCompressOtherCons_Type = Counter32
_CCdmaPppCompressOtherCons_Object = MibScalar
cCdmaPppCompressOtherCons = _CCdmaPppCompressOtherCons_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 99, 10),
    _CCdmaPppCompressOtherCons_Type()
)
cCdmaPppCompressOtherCons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppCompressOtherCons.setStatus("current")
_CCdmaPppNegoMrruCons_Type = Counter32
_CCdmaPppNegoMrruCons_Object = MibScalar
cCdmaPppNegoMrruCons = _CCdmaPppNegoMrruCons_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 99, 11),
    _CCdmaPppNegoMrruCons_Type()
)
cCdmaPppNegoMrruCons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppNegoMrruCons.setStatus("current")
_CCdmaPppNegoIpxCons_Type = Counter32
_CCdmaPppNegoIpxCons_Object = MibScalar
cCdmaPppNegoIpxCons = _CCdmaPppNegoIpxCons_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 99, 12),
    _CCdmaPppNegoIpxCons_Type()
)
cCdmaPppNegoIpxCons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppNegoIpxCons.setStatus("current")
_CCdmaPppNegoIpCons_Type = Counter32
_CCdmaPppNegoIpCons_Object = MibScalar
cCdmaPppNegoIpCons = _CCdmaPppNegoIpCons_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 99, 13),
    _CCdmaPppNegoIpCons_Type()
)
cCdmaPppNegoIpCons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppNegoIpCons.setStatus("current")
_CCdmaPppNegoVjCompCons_Type = Counter32
_CCdmaPppNegoVjCompCons_Object = MibScalar
cCdmaPppNegoVjCompCons = _CCdmaPppNegoVjCompCons_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 99, 14),
    _CCdmaPppNegoVjCompCons_Type()
)
cCdmaPppNegoVjCompCons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppNegoVjCompCons.setStatus("current")
_CCdmaPppNegoBapCons_Type = Counter32
_CCdmaPppNegoBapCons_Object = MibScalar
cCdmaPppNegoBapCons = _CCdmaPppNegoBapCons_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 99, 15),
    _CCdmaPppNegoBapCons_Type()
)
cCdmaPppNegoBapCons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppNegoBapCons.setStatus("current")
_CCdmaPppConFormedBundles_Type = Counter32
_CCdmaPppConFormedBundles_Object = MibScalar
cCdmaPppConFormedBundles = _CCdmaPppConFormedBundles_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 99, 16),
    _CCdmaPppConFormedBundles_Type()
)
cCdmaPppConFormedBundles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppConFormedBundles.setStatus("current")
_CCdmaPppCompressNegoFailures_Type = ZeroBasedCounter32
_CCdmaPppCompressNegoFailures_Object = MibScalar
cCdmaPppCompressNegoFailures = _CCdmaPppCompressNegoFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 99, 17),
    _CCdmaPppCompressNegoFailures_Type()
)
cCdmaPppCompressNegoFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppCompressNegoFailures.setStatus("current")
_CCdmaPppTransmittedEchoReqs_Type = ZeroBasedCounter32
_CCdmaPppTransmittedEchoReqs_Object = MibScalar
cCdmaPppTransmittedEchoReqs = _CCdmaPppTransmittedEchoReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 99, 18),
    _CCdmaPppTransmittedEchoReqs_Type()
)
cCdmaPppTransmittedEchoReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppTransmittedEchoReqs.setStatus("current")
_CCdmaPppRetransmittedEchoReqs_Type = ZeroBasedCounter32
_CCdmaPppRetransmittedEchoReqs_Object = MibScalar
cCdmaPppRetransmittedEchoReqs = _CCdmaPppRetransmittedEchoReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 99, 19),
    _CCdmaPppRetransmittedEchoReqs_Type()
)
cCdmaPppRetransmittedEchoReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppRetransmittedEchoReqs.setStatus("current")
_CCdmaPppReceivedEchoReplies_Type = ZeroBasedCounter32
_CCdmaPppReceivedEchoReplies_Object = MibScalar
cCdmaPppReceivedEchoReplies = _CCdmaPppReceivedEchoReplies_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 99, 20),
    _CCdmaPppReceivedEchoReplies_Type()
)
cCdmaPppReceivedEchoReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppReceivedEchoReplies.setStatus("current")
_CCdmaPppEchoRequestTimeouts_Type = ZeroBasedCounter32
_CCdmaPppEchoRequestTimeouts_Object = MibScalar
cCdmaPppEchoRequestTimeouts = _CCdmaPppEchoRequestTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 99, 21),
    _CCdmaPppEchoRequestTimeouts_Type()
)
cCdmaPppEchoRequestTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppEchoRequestTimeouts.setStatus("current")
_CCdmaPppUnknownProtocolPktDiscards_Type = ZeroBasedCounter32
_CCdmaPppUnknownProtocolPktDiscards_Object = MibScalar
cCdmaPppUnknownProtocolPktDiscards = _CCdmaPppUnknownProtocolPktDiscards_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 99, 22),
    _CCdmaPppUnknownProtocolPktDiscards_Type()
)
cCdmaPppUnknownProtocolPktDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppUnknownProtocolPktDiscards.setStatus("current")
_CCdmaPppBadLengthPktDiscards_Type = ZeroBasedCounter32
_CCdmaPppBadLengthPktDiscards_Object = MibScalar
cCdmaPppBadLengthPktDiscards = _CCdmaPppBadLengthPktDiscards_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 3, 99, 23),
    _CCdmaPppBadLengthPktDiscards_Type()
)
cCdmaPppBadLengthPktDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPppBadLengthPktDiscards.setStatus("current")
_CCdmaTrafficStats_ObjectIdentity = ObjectIdentity
cCdmaTrafficStats = _CCdmaTrafficStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 4)
)
_CCdmaTransmittedSipKiloOctets_Type = Counter32
_CCdmaTransmittedSipKiloOctets_Object = MibScalar
cCdmaTransmittedSipKiloOctets = _CCdmaTransmittedSipKiloOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 4, 1),
    _CCdmaTransmittedSipKiloOctets_Type()
)
cCdmaTransmittedSipKiloOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaTransmittedSipKiloOctets.setStatus("current")
_CCdmaReceivedSipKiloOctets_Type = Counter32
_CCdmaReceivedSipKiloOctets_Object = MibScalar
cCdmaReceivedSipKiloOctets = _CCdmaReceivedSipKiloOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 4, 2),
    _CCdmaReceivedSipKiloOctets_Type()
)
cCdmaReceivedSipKiloOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaReceivedSipKiloOctets.setStatus("current")
_CCdmaTransmittedSipPkts_Type = Counter32
_CCdmaTransmittedSipPkts_Object = MibScalar
cCdmaTransmittedSipPkts = _CCdmaTransmittedSipPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 4, 3),
    _CCdmaTransmittedSipPkts_Type()
)
cCdmaTransmittedSipPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaTransmittedSipPkts.setStatus("current")
_CCdmaReceivedSipPkts_Type = Counter32
_CCdmaReceivedSipPkts_Object = MibScalar
cCdmaReceivedSipPkts = _CCdmaReceivedSipPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 4, 4),
    _CCdmaReceivedSipPkts_Type()
)
cCdmaReceivedSipPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaReceivedSipPkts.setStatus("current")
_CCdmaTransmittedMipKiloOctets_Type = Counter32
_CCdmaTransmittedMipKiloOctets_Object = MibScalar
cCdmaTransmittedMipKiloOctets = _CCdmaTransmittedMipKiloOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 4, 5),
    _CCdmaTransmittedMipKiloOctets_Type()
)
cCdmaTransmittedMipKiloOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaTransmittedMipKiloOctets.setStatus("current")
_CCdmaReceivedMipKiloOctets_Type = Counter32
_CCdmaReceivedMipKiloOctets_Object = MibScalar
cCdmaReceivedMipKiloOctets = _CCdmaReceivedMipKiloOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 4, 6),
    _CCdmaReceivedMipKiloOctets_Type()
)
cCdmaReceivedMipKiloOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaReceivedMipKiloOctets.setStatus("current")
_CCdmaTransmittedMipPkts_Type = Counter32
_CCdmaTransmittedMipPkts_Object = MibScalar
cCdmaTransmittedMipPkts = _CCdmaTransmittedMipPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 4, 7),
    _CCdmaTransmittedMipPkts_Type()
)
cCdmaTransmittedMipPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaTransmittedMipPkts.setStatus("current")
_CCdmaReceivedMipPkts_Type = Counter32
_CCdmaReceivedMipPkts_Object = MibScalar
cCdmaReceivedMipPkts = _CCdmaReceivedMipPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 4, 8),
    _CCdmaReceivedMipPkts_Type()
)
cCdmaReceivedMipPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaReceivedMipPkts.setStatus("current")
_CCdmaTransmittedPmipKiloOctets_Type = Counter32
_CCdmaTransmittedPmipKiloOctets_Object = MibScalar
cCdmaTransmittedPmipKiloOctets = _CCdmaTransmittedPmipKiloOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 4, 9),
    _CCdmaTransmittedPmipKiloOctets_Type()
)
cCdmaTransmittedPmipKiloOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaTransmittedPmipKiloOctets.setStatus("current")
_CCdmaReceivedPmipKiloOctets_Type = Counter32
_CCdmaReceivedPmipKiloOctets_Object = MibScalar
cCdmaReceivedPmipKiloOctets = _CCdmaReceivedPmipKiloOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 4, 10),
    _CCdmaReceivedPmipKiloOctets_Type()
)
cCdmaReceivedPmipKiloOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaReceivedPmipKiloOctets.setStatus("current")
_CCdmaTransmittedPmipPkts_Type = Counter32
_CCdmaTransmittedPmipPkts_Object = MibScalar
cCdmaTransmittedPmipPkts = _CCdmaTransmittedPmipPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 4, 11),
    _CCdmaTransmittedPmipPkts_Type()
)
cCdmaTransmittedPmipPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaTransmittedPmipPkts.setStatus("current")
_CCdmaReceivedPmipPkts_Type = Counter32
_CCdmaReceivedPmipPkts_Object = MibScalar
cCdmaReceivedPmipPkts = _CCdmaReceivedPmipPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 4, 12),
    _CCdmaReceivedPmipPkts_Type()
)
cCdmaReceivedPmipPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaReceivedPmipPkts.setStatus("current")
_CCdmaTransmittedSDBPkts_Type = ZeroBasedCounter32
_CCdmaTransmittedSDBPkts_Object = MibScalar
cCdmaTransmittedSDBPkts = _CCdmaTransmittedSDBPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 4, 13),
    _CCdmaTransmittedSDBPkts_Type()
)
cCdmaTransmittedSDBPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaTransmittedSDBPkts.setStatus("current")
_CCdmaTransmittedSDBOctets_Type = ZeroBasedCounter32
_CCdmaTransmittedSDBOctets_Object = MibScalar
cCdmaTransmittedSDBOctets = _CCdmaTransmittedSDBOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 4, 14),
    _CCdmaTransmittedSDBOctets_Type()
)
cCdmaTransmittedSDBOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaTransmittedSDBOctets.setStatus("current")
_CCdmaNoGREKeyPktDiscards_Type = ZeroBasedCounter32
_CCdmaNoGREKeyPktDiscards_Object = MibScalar
cCdmaNoGREKeyPktDiscards = _CCdmaNoGREKeyPktDiscards_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 4, 15),
    _CCdmaNoGREKeyPktDiscards_Type()
)
cCdmaNoGREKeyPktDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaNoGREKeyPktDiscards.setStatus("current")
_CCdmaNoSessionPktDiscards_Type = ZeroBasedCounter32
_CCdmaNoSessionPktDiscards_Object = MibScalar
cCdmaNoSessionPktDiscards = _CCdmaNoSessionPktDiscards_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 4, 16),
    _CCdmaNoSessionPktDiscards_Type()
)
cCdmaNoSessionPktDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaNoSessionPktDiscards.setStatus("current")
_CCdmaInvGREProtoPktDiscards_Type = ZeroBasedCounter32
_CCdmaInvGREProtoPktDiscards_Object = MibScalar
cCdmaInvGREProtoPktDiscards = _CCdmaInvGREProtoPktDiscards_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 4, 17),
    _CCdmaInvGREProtoPktDiscards_Type()
)
cCdmaInvGREProtoPktDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaInvGREProtoPktDiscards.setStatus("current")
_CCdmaInvCheckSumPktDiscards_Type = ZeroBasedCounter32
_CCdmaInvCheckSumPktDiscards_Object = MibScalar
cCdmaInvCheckSumPktDiscards = _CCdmaInvCheckSumPktDiscards_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 4, 18),
    _CCdmaInvCheckSumPktDiscards_Type()
)
cCdmaInvCheckSumPktDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaInvCheckSumPktDiscards.setStatus("current")
_CCdmaFlowTypeStats_ObjectIdentity = ObjectIdentity
cCdmaFlowTypeStats = _CCdmaFlowTypeStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 5)
)
_CCdmaFlowSimpleIpSuccesses_Type = Counter32
_CCdmaFlowSimpleIpSuccesses_Object = MibScalar
cCdmaFlowSimpleIpSuccesses = _CCdmaFlowSimpleIpSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 5, 1),
    _CCdmaFlowSimpleIpSuccesses_Type()
)
cCdmaFlowSimpleIpSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaFlowSimpleIpSuccesses.setStatus("current")
_CCdmaFlowMobilIpSuccesses_Type = Counter32
_CCdmaFlowMobilIpSuccesses_Object = MibScalar
cCdmaFlowMobilIpSuccesses = _CCdmaFlowMobilIpSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 5, 2),
    _CCdmaFlowMobilIpSuccesses_Type()
)
cCdmaFlowMobilIpSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaFlowMobilIpSuccesses.setStatus("current")
_CCdmaFlowProxyIpSuccesses_Type = Counter32
_CCdmaFlowProxyIpSuccesses_Object = MibScalar
cCdmaFlowProxyIpSuccesses = _CCdmaFlowProxyIpSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 5, 3),
    _CCdmaFlowProxyIpSuccesses_Type()
)
cCdmaFlowProxyIpSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaFlowProxyIpSuccesses.setStatus("current")
_CCdmaFlowVpdnSuccesses_Type = Counter32
_CCdmaFlowVpdnSuccesses_Object = MibScalar
cCdmaFlowVpdnSuccesses = _CCdmaFlowVpdnSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 5, 4),
    _CCdmaFlowVpdnSuccesses_Type()
)
cCdmaFlowVpdnSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaFlowVpdnSuccesses.setStatus("current")
_CCdmaFlowSimpleIpFailures_Type = Counter32
_CCdmaFlowSimpleIpFailures_Object = MibScalar
cCdmaFlowSimpleIpFailures = _CCdmaFlowSimpleIpFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 5, 5),
    _CCdmaFlowSimpleIpFailures_Type()
)
cCdmaFlowSimpleIpFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaFlowSimpleIpFailures.setStatus("current")
_CCdmaFlowMobileIpFailures_Type = Counter32
_CCdmaFlowMobileIpFailures_Object = MibScalar
cCdmaFlowMobileIpFailures = _CCdmaFlowMobileIpFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 5, 6),
    _CCdmaFlowMobileIpFailures_Type()
)
cCdmaFlowMobileIpFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaFlowMobileIpFailures.setStatus("current")
_CCdmaFlowProxyIpFailures_Type = Counter32
_CCdmaFlowProxyIpFailures_Object = MibScalar
cCdmaFlowProxyIpFailures = _CCdmaFlowProxyIpFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 5, 7),
    _CCdmaFlowProxyIpFailures_Type()
)
cCdmaFlowProxyIpFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaFlowProxyIpFailures.setStatus("current")
_CCdmaFlowVpdnFailures_Type = Counter32
_CCdmaFlowVpdnFailures_Object = MibScalar
cCdmaFlowVpdnFailures = _CCdmaFlowVpdnFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 5, 8),
    _CCdmaFlowVpdnFailures_Type()
)
cCdmaFlowVpdnFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaFlowVpdnFailures.setStatus("current")
_CCdmaFlowUnknownTypeFailures_Type = Counter32
_CCdmaFlowUnknownTypeFailures_Object = MibScalar
cCdmaFlowUnknownTypeFailures = _CCdmaFlowUnknownTypeFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 5, 9),
    _CCdmaFlowUnknownTypeFailures_Type()
)
cCdmaFlowUnknownTypeFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaFlowUnknownTypeFailures.setStatus("current")
_CCdmaServiceOptionStats_ObjectIdentity = ObjectIdentity
cCdmaServiceOptionStats = _CCdmaServiceOptionStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 6)
)
_CCdmaServiceTotalOptions_Type = Counter32
_CCdmaServiceTotalOptions_Object = MibScalar
cCdmaServiceTotalOptions = _CCdmaServiceTotalOptions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 6, 1),
    _CCdmaServiceTotalOptions_Type()
)
cCdmaServiceTotalOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaServiceTotalOptions.setStatus("current")
_CCdmaServiceOptionTable_Object = MibTable
cCdmaServiceOptionTable = _CCdmaServiceOptionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 6, 2)
)
if mibBuilder.loadTexts:
    cCdmaServiceOptionTable.setStatus("current")
_CCdmaServiceOptionEntry_Object = MibTableRow
cCdmaServiceOptionEntry = _CCdmaServiceOptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 6, 2, 1)
)
cCdmaServiceOptionEntry.setIndexNames(
    (0, "CISCO-CDMA-PDSN-MIB", "cCdmaServiceOptionIndex"),
)
if mibBuilder.loadTexts:
    cCdmaServiceOptionEntry.setStatus("current")


class _CCdmaServiceOptionIndex_Type(Integer32):
    """Custom type cCdmaServiceOptionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              9,
              12,
              13,
              14,
              15,
              18,
              19,
              22,
              23,
              24,
              25,
              32,
              33,
              37,
              54,
              55,
              4103)
        )
    )
    namedValues = NamedValues(
        *(("asyncDataRate2", 12),
          ("group3FaxRate2", 13),
          ("is2000Loopback", 55),
          ("is2000Markov", 54),
          ("is2000TestData", 32),
          ("isdn64k", 37),
          ("loopback13K", 9),
          ("otapaRate1", 18),
          ("otapaRate2", 19),
          ("packetData144k", 15),
          ("packetData3G", 33),
          ("packetDataRev1", 4103),
          ("packetDataRs1fRs1r", 22),
          ("packetDataRs1fRs2r", 23),
          ("packetDataRs2fRs1r", 24),
          ("packetDataRs2fRs2", 25),
          ("smsRate1", 6),
          ("smsRate2", 14))
    )


_CCdmaServiceOptionIndex_Type.__name__ = "Integer32"
_CCdmaServiceOptionIndex_Object = MibTableColumn
cCdmaServiceOptionIndex = _CCdmaServiceOptionIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 6, 2, 1, 1),
    _CCdmaServiceOptionIndex_Type()
)
cCdmaServiceOptionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cCdmaServiceOptionIndex.setStatus("current")
_CCdmaServiceOptionSucesses_Type = Counter32
_CCdmaServiceOptionSucesses_Object = MibTableColumn
cCdmaServiceOptionSucesses = _CCdmaServiceOptionSucesses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 6, 2, 1, 2),
    _CCdmaServiceOptionSucesses_Type()
)
cCdmaServiceOptionSucesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaServiceOptionSucesses.setStatus("current")
_CCdmaServiceOptionFailures_Type = Counter32
_CCdmaServiceOptionFailures_Object = MibTableColumn
cCdmaServiceOptionFailures = _CCdmaServiceOptionFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 6, 2, 1, 3),
    _CCdmaServiceOptionFailures_Type()
)
cCdmaServiceOptionFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaServiceOptionFailures.setStatus("current")
_CCdmaHandoffStats_ObjectIdentity = ObjectIdentity
cCdmaHandoffStats = _CCdmaHandoffStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 7)
)
_CCdmaInterPcfHandoffs_Type = Counter32
_CCdmaInterPcfHandoffs_Object = MibScalar
cCdmaInterPcfHandoffs = _CCdmaInterPcfHandoffs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 7, 1),
    _CCdmaInterPcfHandoffs_Type()
)
cCdmaInterPcfHandoffs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaInterPcfHandoffs.setStatus("current")
_CCdmaInterPdsnHandoffs_Type = Counter32
_CCdmaInterPdsnHandoffs_Object = MibScalar
cCdmaInterPdsnHandoffs = _CCdmaInterPdsnHandoffs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 7, 2),
    _CCdmaInterPdsnHandoffs_Type()
)
cCdmaInterPdsnHandoffs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaInterPdsnHandoffs.setStatus("current")
_CCdmaIdChangeHandoffs_Type = Counter32
_CCdmaIdChangeHandoffs_Object = MibScalar
cCdmaIdChangeHandoffs = _CCdmaIdChangeHandoffs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 7, 3),
    _CCdmaIdChangeHandoffs_Type()
)
cCdmaIdChangeHandoffs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaIdChangeHandoffs.setStatus("current")
_CCdmaStatusChangeStats_ObjectIdentity = ObjectIdentity
cCdmaStatusChangeStats = _CCdmaStatusChangeStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 8)
)
_CCdmaStatusIS2OOSes_Type = Counter32
_CCdmaStatusIS2OOSes_Object = MibScalar
cCdmaStatusIS2OOSes = _CCdmaStatusIS2OOSes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 8, 1),
    _CCdmaStatusIS2OOSes_Type()
)
cCdmaStatusIS2OOSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaStatusIS2OOSes.setStatus("current")
_CCdmaStatusOOS2ISes_Type = Counter32
_CCdmaStatusOOS2ISes_Object = MibScalar
cCdmaStatusOOS2ISes = _CCdmaStatusOOS2ISes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 8, 2),
    _CCdmaStatusOOS2ISes_Type()
)
cCdmaStatusOOS2ISes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaStatusOOS2ISes.setStatus("current")
_CCdmaAddressSchemeStats_ObjectIdentity = ObjectIdentity
cCdmaAddressSchemeStats = _CCdmaAddressSchemeStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 9)
)
_CCdmaAddressStaticSIPs_Type = Counter32
_CCdmaAddressStaticSIPs_Object = MibScalar
cCdmaAddressStaticSIPs = _CCdmaAddressStaticSIPs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 9, 1),
    _CCdmaAddressStaticSIPs_Type()
)
cCdmaAddressStaticSIPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaAddressStaticSIPs.setStatus("current")
_CCdmaAddressDynamicSIPs_Type = Counter32
_CCdmaAddressDynamicSIPs_Object = MibScalar
cCdmaAddressDynamicSIPs = _CCdmaAddressDynamicSIPs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 9, 2),
    _CCdmaAddressDynamicSIPs_Type()
)
cCdmaAddressDynamicSIPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaAddressDynamicSIPs.setStatus("current")
_CCdmaAddressStaticMIPs_Type = Counter32
_CCdmaAddressStaticMIPs_Object = MibScalar
cCdmaAddressStaticMIPs = _CCdmaAddressStaticMIPs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 9, 3),
    _CCdmaAddressStaticMIPs_Type()
)
cCdmaAddressStaticMIPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaAddressStaticMIPs.setStatus("current")
_CCdmaAddressDynamicMIPs_Type = Counter32
_CCdmaAddressDynamicMIPs_Object = MibScalar
cCdmaAddressDynamicMIPs = _CCdmaAddressDynamicMIPs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 9, 4),
    _CCdmaAddressDynamicMIPs_Type()
)
cCdmaAddressDynamicMIPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaAddressDynamicMIPs.setStatus("current")
_CCdmaAddressStaticPMIPs_Type = Counter32
_CCdmaAddressStaticPMIPs_Object = MibScalar
cCdmaAddressStaticPMIPs = _CCdmaAddressStaticPMIPs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 9, 5),
    _CCdmaAddressStaticPMIPs_Type()
)
cCdmaAddressStaticPMIPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaAddressStaticPMIPs.setStatus("current")
_CCdmaAddressDynamicPMIPs_Type = Counter32
_CCdmaAddressDynamicPMIPs_Object = MibScalar
cCdmaAddressDynamicPMIPs = _CCdmaAddressDynamicPMIPs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 9, 6),
    _CCdmaAddressDynamicPMIPs_Type()
)
cCdmaAddressDynamicPMIPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaAddressDynamicPMIPs.setStatus("current")
_CCdmaAddressStaticVPDNs_Type = Counter32
_CCdmaAddressStaticVPDNs_Object = MibScalar
cCdmaAddressStaticVPDNs = _CCdmaAddressStaticVPDNs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 9, 7),
    _CCdmaAddressStaticVPDNs_Type()
)
cCdmaAddressStaticVPDNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaAddressStaticVPDNs.setStatus("current")
_CCdmaAddressDynamicVPDNs_Type = Counter32
_CCdmaAddressDynamicVPDNs_Object = MibScalar
cCdmaAddressDynamicVPDNs = _CCdmaAddressDynamicVPDNs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 9, 8),
    _CCdmaAddressDynamicVPDNs_Type()
)
cCdmaAddressDynamicVPDNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaAddressDynamicVPDNs.setStatus("current")
_CCdmaPcfSoRpRegStats_ObjectIdentity = ObjectIdentity
cCdmaPcfSoRpRegStats = _CCdmaPcfSoRpRegStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 10)
)
_CCdmaPcfSoRpRegStatsTable_Object = MibTable
cCdmaPcfSoRpRegStatsTable = _CCdmaPcfSoRpRegStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 10, 1)
)
if mibBuilder.loadTexts:
    cCdmaPcfSoRpRegStatsTable.setStatus("current")
_CCdmaPcfSoRpRegStatsEntry_Object = MibTableRow
cCdmaPcfSoRpRegStatsEntry = _CCdmaPcfSoRpRegStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 10, 1, 1)
)
cCdmaPcfSoRpRegStatsEntry.setIndexNames(
    (0, "CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoRpRegIpAddrType"),
    (0, "CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoRpRegIpAddr"),
    (0, "CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoRpRegServiceOption"),
)
if mibBuilder.loadTexts:
    cCdmaPcfSoRpRegStatsEntry.setStatus("current")
_CCdmaPcfSoRpRegIpAddrType_Type = InetAddressType
_CCdmaPcfSoRpRegIpAddrType_Object = MibTableColumn
cCdmaPcfSoRpRegIpAddrType = _CCdmaPcfSoRpRegIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 10, 1, 1, 1),
    _CCdmaPcfSoRpRegIpAddrType_Type()
)
cCdmaPcfSoRpRegIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cCdmaPcfSoRpRegIpAddrType.setStatus("current")
_CCdmaPcfSoRpRegIpAddr_Type = InetAddress
_CCdmaPcfSoRpRegIpAddr_Object = MibTableColumn
cCdmaPcfSoRpRegIpAddr = _CCdmaPcfSoRpRegIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 10, 1, 1, 2),
    _CCdmaPcfSoRpRegIpAddr_Type()
)
cCdmaPcfSoRpRegIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cCdmaPcfSoRpRegIpAddr.setStatus("current")
_CCdmaPcfSoRpRegServiceOption_Type = CCdmaServiceOption
_CCdmaPcfSoRpRegServiceOption_Object = MibTableColumn
cCdmaPcfSoRpRegServiceOption = _CCdmaPcfSoRpRegServiceOption_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 10, 1, 1, 3),
    _CCdmaPcfSoRpRegServiceOption_Type()
)
cCdmaPcfSoRpRegServiceOption.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cCdmaPcfSoRpRegServiceOption.setStatus("current")
_CCdmaPcfSoRpRegRcvdReqs_Type = ZeroBasedCounter32
_CCdmaPcfSoRpRegRcvdReqs_Object = MibTableColumn
cCdmaPcfSoRpRegRcvdReqs = _CCdmaPcfSoRpRegRcvdReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 10, 1, 1, 4),
    _CCdmaPcfSoRpRegRcvdReqs_Type()
)
cCdmaPcfSoRpRegRcvdReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPcfSoRpRegRcvdReqs.setStatus("current")
_CCdmaPcfSoRpRegAcptdReqs_Type = ZeroBasedCounter32
_CCdmaPcfSoRpRegAcptdReqs_Object = MibTableColumn
cCdmaPcfSoRpRegAcptdReqs = _CCdmaPcfSoRpRegAcptdReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 10, 1, 1, 5),
    _CCdmaPcfSoRpRegAcptdReqs_Type()
)
cCdmaPcfSoRpRegAcptdReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPcfSoRpRegAcptdReqs.setStatus("current")
_CCdmaPcfSoRpRegDeniedReqs_Type = ZeroBasedCounter32
_CCdmaPcfSoRpRegDeniedReqs_Object = MibTableColumn
cCdmaPcfSoRpRegDeniedReqs = _CCdmaPcfSoRpRegDeniedReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 10, 1, 1, 6),
    _CCdmaPcfSoRpRegDeniedReqs_Type()
)
cCdmaPcfSoRpRegDeniedReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPcfSoRpRegDeniedReqs.setStatus("current")
_CCdmaPcfSoRpRegDiscardedReqs_Type = ZeroBasedCounter32
_CCdmaPcfSoRpRegDiscardedReqs_Object = MibTableColumn
cCdmaPcfSoRpRegDiscardedReqs = _CCdmaPcfSoRpRegDiscardedReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 10, 1, 1, 7),
    _CCdmaPcfSoRpRegDiscardedReqs_Type()
)
cCdmaPcfSoRpRegDiscardedReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPcfSoRpRegDiscardedReqs.setStatus("current")
_CCdmaPcfSoRpInitRegAcptdReqs_Type = ZeroBasedCounter32
_CCdmaPcfSoRpInitRegAcptdReqs_Object = MibTableColumn
cCdmaPcfSoRpInitRegAcptdReqs = _CCdmaPcfSoRpInitRegAcptdReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 10, 1, 1, 8),
    _CCdmaPcfSoRpInitRegAcptdReqs_Type()
)
cCdmaPcfSoRpInitRegAcptdReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPcfSoRpInitRegAcptdReqs.setStatus("current")
_CCdmaPcfSoRpInitRegDeniedReqs_Type = ZeroBasedCounter32
_CCdmaPcfSoRpInitRegDeniedReqs_Object = MibTableColumn
cCdmaPcfSoRpInitRegDeniedReqs = _CCdmaPcfSoRpInitRegDeniedReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 10, 1, 1, 9),
    _CCdmaPcfSoRpInitRegDeniedReqs_Type()
)
cCdmaPcfSoRpInitRegDeniedReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPcfSoRpInitRegDeniedReqs.setStatus("current")
_CCdmaPcfSoRpReRegAcptdReqs_Type = ZeroBasedCounter32
_CCdmaPcfSoRpReRegAcptdReqs_Object = MibTableColumn
cCdmaPcfSoRpReRegAcptdReqs = _CCdmaPcfSoRpReRegAcptdReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 10, 1, 1, 10),
    _CCdmaPcfSoRpReRegAcptdReqs_Type()
)
cCdmaPcfSoRpReRegAcptdReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPcfSoRpReRegAcptdReqs.setStatus("current")
_CCdmaPcfSoRpReRegDeniedReqs_Type = ZeroBasedCounter32
_CCdmaPcfSoRpReRegDeniedReqs_Object = MibTableColumn
cCdmaPcfSoRpReRegDeniedReqs = _CCdmaPcfSoRpReRegDeniedReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 10, 1, 1, 11),
    _CCdmaPcfSoRpReRegDeniedReqs_Type()
)
cCdmaPcfSoRpReRegDeniedReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPcfSoRpReRegDeniedReqs.setStatus("current")
_CCdmaPcfSoRpDeRegAcptdReqs_Type = ZeroBasedCounter32
_CCdmaPcfSoRpDeRegAcptdReqs_Object = MibTableColumn
cCdmaPcfSoRpDeRegAcptdReqs = _CCdmaPcfSoRpDeRegAcptdReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 10, 1, 1, 12),
    _CCdmaPcfSoRpDeRegAcptdReqs_Type()
)
cCdmaPcfSoRpDeRegAcptdReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPcfSoRpDeRegAcptdReqs.setStatus("current")
_CCdmaPcfSoRpDeRegDeniedReqs_Type = ZeroBasedCounter32
_CCdmaPcfSoRpDeRegDeniedReqs_Object = MibTableColumn
cCdmaPcfSoRpDeRegDeniedReqs = _CCdmaPcfSoRpDeRegDeniedReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 10, 1, 1, 13),
    _CCdmaPcfSoRpDeRegDeniedReqs_Type()
)
cCdmaPcfSoRpDeRegDeniedReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPcfSoRpDeRegDeniedReqs.setStatus("current")
_CCdmaPcfSoRpRegPcfUnknwnFails_Type = ZeroBasedCounter32
_CCdmaPcfSoRpRegPcfUnknwnFails_Object = MibTableColumn
cCdmaPcfSoRpRegPcfUnknwnFails = _CCdmaPcfSoRpRegPcfUnknwnFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 10, 1, 1, 14),
    _CCdmaPcfSoRpRegPcfUnknwnFails_Type()
)
cCdmaPcfSoRpRegPcfUnknwnFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPcfSoRpRegPcfUnknwnFails.setStatus("current")
_CCdmaPcfSoRpRegAdmnFails_Type = ZeroBasedCounter32
_CCdmaPcfSoRpRegAdmnFails_Object = MibTableColumn
cCdmaPcfSoRpRegAdmnFails = _CCdmaPcfSoRpRegAdmnFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 10, 1, 1, 15),
    _CCdmaPcfSoRpRegAdmnFails_Type()
)
cCdmaPcfSoRpRegAdmnFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPcfSoRpRegAdmnFails.setStatus("current")
_CCdmaPcfSoRpRegNoRsrcFails_Type = ZeroBasedCounter32
_CCdmaPcfSoRpRegNoRsrcFails_Object = MibTableColumn
cCdmaPcfSoRpRegNoRsrcFails = _CCdmaPcfSoRpRegNoRsrcFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 10, 1, 1, 16),
    _CCdmaPcfSoRpRegNoRsrcFails_Type()
)
cCdmaPcfSoRpRegNoRsrcFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPcfSoRpRegNoRsrcFails.setStatus("current")
_CCdmaPcfSoRpRegMNAuthFails_Type = ZeroBasedCounter32
_CCdmaPcfSoRpRegMNAuthFails_Object = MibTableColumn
cCdmaPcfSoRpRegMNAuthFails = _CCdmaPcfSoRpRegMNAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 10, 1, 1, 17),
    _CCdmaPcfSoRpRegMNAuthFails_Type()
)
cCdmaPcfSoRpRegMNAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPcfSoRpRegMNAuthFails.setStatus("current")
_CCdmaPcfSoRpRegIdMismatFails_Type = ZeroBasedCounter32
_CCdmaPcfSoRpRegIdMismatFails_Object = MibTableColumn
cCdmaPcfSoRpRegIdMismatFails = _CCdmaPcfSoRpRegIdMismatFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 10, 1, 1, 18),
    _CCdmaPcfSoRpRegIdMismatFails_Type()
)
cCdmaPcfSoRpRegIdMismatFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPcfSoRpRegIdMismatFails.setStatus("current")
_CCdmaPcfSoRpRegBadReqFails_Type = ZeroBasedCounter32
_CCdmaPcfSoRpRegBadReqFails_Object = MibTableColumn
cCdmaPcfSoRpRegBadReqFails = _CCdmaPcfSoRpRegBadReqFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 10, 1, 1, 19),
    _CCdmaPcfSoRpRegBadReqFails_Type()
)
cCdmaPcfSoRpRegBadReqFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPcfSoRpRegBadReqFails.setStatus("current")
_CCdmaPcfSoRpRegUnkPdsnFails_Type = ZeroBasedCounter32
_CCdmaPcfSoRpRegUnkPdsnFails_Object = MibTableColumn
cCdmaPcfSoRpRegUnkPdsnFails = _CCdmaPcfSoRpRegUnkPdsnFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 10, 1, 1, 20),
    _CCdmaPcfSoRpRegUnkPdsnFails_Type()
)
cCdmaPcfSoRpRegUnkPdsnFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPcfSoRpRegUnkPdsnFails.setStatus("current")
_CCdmaPcfSoRpRegNoRevTunFails_Type = ZeroBasedCounter32
_CCdmaPcfSoRpRegNoRevTunFails_Object = MibTableColumn
cCdmaPcfSoRpRegNoRevTunFails = _CCdmaPcfSoRpRegNoRevTunFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 10, 1, 1, 21),
    _CCdmaPcfSoRpRegNoRevTunFails_Type()
)
cCdmaPcfSoRpRegNoRevTunFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPcfSoRpRegNoRevTunFails.setStatus("current")
_CCdmaPcfSoRpRegTBitNSetFails_Type = ZeroBasedCounter32
_CCdmaPcfSoRpRegTBitNSetFails_Object = MibTableColumn
cCdmaPcfSoRpRegTBitNSetFails = _CCdmaPcfSoRpRegTBitNSetFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 10, 1, 1, 22),
    _CCdmaPcfSoRpRegTBitNSetFails_Type()
)
cCdmaPcfSoRpRegTBitNSetFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPcfSoRpRegTBitNSetFails.setStatus("current")
_CCdmaPcfSoRpRegBadCVSEFails_Type = ZeroBasedCounter32
_CCdmaPcfSoRpRegBadCVSEFails_Object = MibTableColumn
cCdmaPcfSoRpRegBadCVSEFails = _CCdmaPcfSoRpRegBadCVSEFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 10, 1, 1, 23),
    _CCdmaPcfSoRpRegBadCVSEFails_Type()
)
cCdmaPcfSoRpRegBadCVSEFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPcfSoRpRegBadCVSEFails.setStatus("current")
_CCdmaPcfSoRpInitRegRcvdReqs_Type = ZeroBasedCounter32
_CCdmaPcfSoRpInitRegRcvdReqs_Object = MibTableColumn
cCdmaPcfSoRpInitRegRcvdReqs = _CCdmaPcfSoRpInitRegRcvdReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 10, 1, 1, 24),
    _CCdmaPcfSoRpInitRegRcvdReqs_Type()
)
cCdmaPcfSoRpInitRegRcvdReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPcfSoRpInitRegRcvdReqs.setStatus("current")
_CCdmaPcfSoRpInitRegDiscardedReqs_Type = ZeroBasedCounter32
_CCdmaPcfSoRpInitRegDiscardedReqs_Object = MibTableColumn
cCdmaPcfSoRpInitRegDiscardedReqs = _CCdmaPcfSoRpInitRegDiscardedReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 10, 1, 1, 25),
    _CCdmaPcfSoRpInitRegDiscardedReqs_Type()
)
cCdmaPcfSoRpInitRegDiscardedReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPcfSoRpInitRegDiscardedReqs.setStatus("current")
_CCdmaPcfSoRpReRegRcvdReqs_Type = ZeroBasedCounter32
_CCdmaPcfSoRpReRegRcvdReqs_Object = MibTableColumn
cCdmaPcfSoRpReRegRcvdReqs = _CCdmaPcfSoRpReRegRcvdReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 10, 1, 1, 26),
    _CCdmaPcfSoRpReRegRcvdReqs_Type()
)
cCdmaPcfSoRpReRegRcvdReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPcfSoRpReRegRcvdReqs.setStatus("current")
_CCdmaPcfSoRpReRegDiscardedReqs_Type = ZeroBasedCounter32
_CCdmaPcfSoRpReRegDiscardedReqs_Object = MibTableColumn
cCdmaPcfSoRpReRegDiscardedReqs = _CCdmaPcfSoRpReRegDiscardedReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 10, 1, 1, 27),
    _CCdmaPcfSoRpReRegDiscardedReqs_Type()
)
cCdmaPcfSoRpReRegDiscardedReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPcfSoRpReRegDiscardedReqs.setStatus("current")
_CCdmaPcfSoRpDeRegRcvdReqs_Type = ZeroBasedCounter32
_CCdmaPcfSoRpDeRegRcvdReqs_Object = MibTableColumn
cCdmaPcfSoRpDeRegRcvdReqs = _CCdmaPcfSoRpDeRegRcvdReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 10, 1, 1, 28),
    _CCdmaPcfSoRpDeRegRcvdReqs_Type()
)
cCdmaPcfSoRpDeRegRcvdReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPcfSoRpDeRegRcvdReqs.setStatus("current")
_CCdmaPcfSoRpDeRegDiscardedReqs_Type = ZeroBasedCounter32
_CCdmaPcfSoRpDeRegDiscardedReqs_Object = MibTableColumn
cCdmaPcfSoRpDeRegDiscardedReqs = _CCdmaPcfSoRpDeRegDiscardedReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 10, 1, 1, 29),
    _CCdmaPcfSoRpDeRegDiscardedReqs_Type()
)
cCdmaPcfSoRpDeRegDiscardedReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPcfSoRpDeRegDiscardedReqs.setStatus("current")
_CCdmaPcfSoRpHandoffRegRcvdReqs_Type = ZeroBasedCounter32
_CCdmaPcfSoRpHandoffRegRcvdReqs_Object = MibTableColumn
cCdmaPcfSoRpHandoffRegRcvdReqs = _CCdmaPcfSoRpHandoffRegRcvdReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 10, 1, 1, 30),
    _CCdmaPcfSoRpHandoffRegRcvdReqs_Type()
)
cCdmaPcfSoRpHandoffRegRcvdReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPcfSoRpHandoffRegRcvdReqs.setStatus("current")
_CCdmaPcfSoRpHandoffRegAcptdReqs_Type = ZeroBasedCounter32
_CCdmaPcfSoRpHandoffRegAcptdReqs_Object = MibTableColumn
cCdmaPcfSoRpHandoffRegAcptdReqs = _CCdmaPcfSoRpHandoffRegAcptdReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 10, 1, 1, 31),
    _CCdmaPcfSoRpHandoffRegAcptdReqs_Type()
)
cCdmaPcfSoRpHandoffRegAcptdReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPcfSoRpHandoffRegAcptdReqs.setStatus("current")
_CCdmaPcfSoRpHandoffRegDeniedReqs_Type = ZeroBasedCounter32
_CCdmaPcfSoRpHandoffRegDeniedReqs_Object = MibTableColumn
cCdmaPcfSoRpHandoffRegDeniedReqs = _CCdmaPcfSoRpHandoffRegDeniedReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 10, 1, 1, 32),
    _CCdmaPcfSoRpHandoffRegDeniedReqs_Type()
)
cCdmaPcfSoRpHandoffRegDeniedReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPcfSoRpHandoffRegDeniedReqs.setStatus("current")
_CCdmaPcfSoRpHandoffRegDiscardedReqs_Type = ZeroBasedCounter32
_CCdmaPcfSoRpHandoffRegDiscardedReqs_Object = MibTableColumn
cCdmaPcfSoRpHandoffRegDiscardedReqs = _CCdmaPcfSoRpHandoffRegDiscardedReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 10, 1, 1, 33),
    _CCdmaPcfSoRpHandoffRegDiscardedReqs_Type()
)
cCdmaPcfSoRpHandoffRegDiscardedReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPcfSoRpHandoffRegDiscardedReqs.setStatus("current")
_CCdmaPcfSoRpReRegAirlinkStarts_Type = ZeroBasedCounter32
_CCdmaPcfSoRpReRegAirlinkStarts_Object = MibTableColumn
cCdmaPcfSoRpReRegAirlinkStarts = _CCdmaPcfSoRpReRegAirlinkStarts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 10, 1, 1, 34),
    _CCdmaPcfSoRpReRegAirlinkStarts_Type()
)
cCdmaPcfSoRpReRegAirlinkStarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPcfSoRpReRegAirlinkStarts.setStatus("current")
_CCdmaPcfSoRpReRegAirlinkStops_Type = ZeroBasedCounter32
_CCdmaPcfSoRpReRegAirlinkStops_Object = MibTableColumn
cCdmaPcfSoRpReRegAirlinkStops = _CCdmaPcfSoRpReRegAirlinkStops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 10, 1, 1, 35),
    _CCdmaPcfSoRpReRegAirlinkStops_Type()
)
cCdmaPcfSoRpReRegAirlinkStops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPcfSoRpReRegAirlinkStops.setStatus("current")
_CCdmaPcfSoRpDeRegAirlinkStops_Type = ZeroBasedCounter32
_CCdmaPcfSoRpDeRegAirlinkStops_Object = MibTableColumn
cCdmaPcfSoRpDeRegAirlinkStops = _CCdmaPcfSoRpDeRegAirlinkStops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 10, 1, 1, 36),
    _CCdmaPcfSoRpDeRegAirlinkStops_Type()
)
cCdmaPcfSoRpDeRegAirlinkStops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPcfSoRpDeRegAirlinkStops.setStatus("current")
_CCdmaPcfSoRpUpdStats_ObjectIdentity = ObjectIdentity
cCdmaPcfSoRpUpdStats = _CCdmaPcfSoRpUpdStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 11)
)
_CCdmaPcfSoRpUpdStatsTable_Object = MibTable
cCdmaPcfSoRpUpdStatsTable = _CCdmaPcfSoRpUpdStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 11, 1)
)
if mibBuilder.loadTexts:
    cCdmaPcfSoRpUpdStatsTable.setStatus("current")
_CCdmaPcfSoRpUpdStatsEntry_Object = MibTableRow
cCdmaPcfSoRpUpdStatsEntry = _CCdmaPcfSoRpUpdStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 11, 1, 1)
)
cCdmaPcfSoRpUpdStatsEntry.setIndexNames(
    (0, "CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoRpUpdIpAddrType"),
    (0, "CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoRpUpdIpAddr"),
    (0, "CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoRpUpdServiceOption"),
)
if mibBuilder.loadTexts:
    cCdmaPcfSoRpUpdStatsEntry.setStatus("current")
_CCdmaPcfSoRpUpdIpAddrType_Type = InetAddressType
_CCdmaPcfSoRpUpdIpAddrType_Object = MibTableColumn
cCdmaPcfSoRpUpdIpAddrType = _CCdmaPcfSoRpUpdIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 11, 1, 1, 1),
    _CCdmaPcfSoRpUpdIpAddrType_Type()
)
cCdmaPcfSoRpUpdIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cCdmaPcfSoRpUpdIpAddrType.setStatus("current")
_CCdmaPcfSoRpUpdIpAddr_Type = InetAddress
_CCdmaPcfSoRpUpdIpAddr_Object = MibTableColumn
cCdmaPcfSoRpUpdIpAddr = _CCdmaPcfSoRpUpdIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 11, 1, 1, 2),
    _CCdmaPcfSoRpUpdIpAddr_Type()
)
cCdmaPcfSoRpUpdIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cCdmaPcfSoRpUpdIpAddr.setStatus("current")
_CCdmaPcfSoRpUpdServiceOption_Type = CCdmaServiceOption
_CCdmaPcfSoRpUpdServiceOption_Object = MibTableColumn
cCdmaPcfSoRpUpdServiceOption = _CCdmaPcfSoRpUpdServiceOption_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 11, 1, 1, 3),
    _CCdmaPcfSoRpUpdServiceOption_Type()
)
cCdmaPcfSoRpUpdServiceOption.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cCdmaPcfSoRpUpdServiceOption.setStatus("current")
_CCdmaPcfSoRpUpdTxdReqs_Type = ZeroBasedCounter32
_CCdmaPcfSoRpUpdTxdReqs_Object = MibTableColumn
cCdmaPcfSoRpUpdTxdReqs = _CCdmaPcfSoRpUpdTxdReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 11, 1, 1, 4),
    _CCdmaPcfSoRpUpdTxdReqs_Type()
)
cCdmaPcfSoRpUpdTxdReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPcfSoRpUpdTxdReqs.setStatus("current")
_CCdmaPcfSoRpUpdAcptdReqs_Type = ZeroBasedCounter32
_CCdmaPcfSoRpUpdAcptdReqs_Object = MibTableColumn
cCdmaPcfSoRpUpdAcptdReqs = _CCdmaPcfSoRpUpdAcptdReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 11, 1, 1, 5),
    _CCdmaPcfSoRpUpdAcptdReqs_Type()
)
cCdmaPcfSoRpUpdAcptdReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPcfSoRpUpdAcptdReqs.setStatus("current")
_CCdmaPcfSoRpUpdDeniedReqs_Type = ZeroBasedCounter32
_CCdmaPcfSoRpUpdDeniedReqs_Object = MibTableColumn
cCdmaPcfSoRpUpdDeniedReqs = _CCdmaPcfSoRpUpdDeniedReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 11, 1, 1, 6),
    _CCdmaPcfSoRpUpdDeniedReqs_Type()
)
cCdmaPcfSoRpUpdDeniedReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPcfSoRpUpdDeniedReqs.setStatus("current")
_CCdmaPcfSoRpUpdNotAckedReqs_Type = ZeroBasedCounter32
_CCdmaPcfSoRpUpdNotAckedReqs_Object = MibTableColumn
cCdmaPcfSoRpUpdNotAckedReqs = _CCdmaPcfSoRpUpdNotAckedReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 11, 1, 1, 7),
    _CCdmaPcfSoRpUpdNotAckedReqs_Type()
)
cCdmaPcfSoRpUpdNotAckedReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPcfSoRpUpdNotAckedReqs.setStatus("current")
_CCdmaPcfSoRpUpdInitTxdReqs_Type = ZeroBasedCounter32
_CCdmaPcfSoRpUpdInitTxdReqs_Object = MibTableColumn
cCdmaPcfSoRpUpdInitTxdReqs = _CCdmaPcfSoRpUpdInitTxdReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 11, 1, 1, 8),
    _CCdmaPcfSoRpUpdInitTxdReqs_Type()
)
cCdmaPcfSoRpUpdInitTxdReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPcfSoRpUpdInitTxdReqs.setStatus("current")
_CCdmaPcfSoRpUpdReTxdReqs_Type = ZeroBasedCounter32
_CCdmaPcfSoRpUpdReTxdReqs_Object = MibTableColumn
cCdmaPcfSoRpUpdReTxdReqs = _CCdmaPcfSoRpUpdReTxdReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 11, 1, 1, 9),
    _CCdmaPcfSoRpUpdReTxdReqs_Type()
)
cCdmaPcfSoRpUpdReTxdReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPcfSoRpUpdReTxdReqs.setStatus("current")
_CCdmaPcfSoRpUpdRcvdAcks_Type = ZeroBasedCounter32
_CCdmaPcfSoRpUpdRcvdAcks_Object = MibTableColumn
cCdmaPcfSoRpUpdRcvdAcks = _CCdmaPcfSoRpUpdRcvdAcks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 11, 1, 1, 10),
    _CCdmaPcfSoRpUpdRcvdAcks_Type()
)
cCdmaPcfSoRpUpdRcvdAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPcfSoRpUpdRcvdAcks.setStatus("current")
_CCdmaPcfSoRpUpdDiscardedAcks_Type = ZeroBasedCounter32
_CCdmaPcfSoRpUpdDiscardedAcks_Object = MibTableColumn
cCdmaPcfSoRpUpdDiscardedAcks = _CCdmaPcfSoRpUpdDiscardedAcks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 11, 1, 1, 11),
    _CCdmaPcfSoRpUpdDiscardedAcks_Type()
)
cCdmaPcfSoRpUpdDiscardedAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPcfSoRpUpdDiscardedAcks.setStatus("current")
_CCdmaPcfSoRpUpdRpLifeExpReqs_Type = ZeroBasedCounter32
_CCdmaPcfSoRpUpdRpLifeExpReqs_Object = MibTableColumn
cCdmaPcfSoRpUpdRpLifeExpReqs = _CCdmaPcfSoRpUpdRpLifeExpReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 11, 1, 1, 12),
    _CCdmaPcfSoRpUpdRpLifeExpReqs_Type()
)
cCdmaPcfSoRpUpdRpLifeExpReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPcfSoRpUpdRpLifeExpReqs.setStatus("current")
_CCdmaPcfSoRpUpdPPPtermReqs_Type = ZeroBasedCounter32
_CCdmaPcfSoRpUpdPPPtermReqs_Object = MibTableColumn
cCdmaPcfSoRpUpdPPPtermReqs = _CCdmaPcfSoRpUpdPPPtermReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 11, 1, 1, 13),
    _CCdmaPcfSoRpUpdPPPtermReqs_Type()
)
cCdmaPcfSoRpUpdPPPtermReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPcfSoRpUpdPPPtermReqs.setStatus("current")
_CCdmaPcfSoRpUpdOtherReaReqs_Type = ZeroBasedCounter32
_CCdmaPcfSoRpUpdOtherReaReqs_Object = MibTableColumn
cCdmaPcfSoRpUpdOtherReaReqs = _CCdmaPcfSoRpUpdOtherReaReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 11, 1, 1, 14),
    _CCdmaPcfSoRpUpdOtherReaReqs_Type()
)
cCdmaPcfSoRpUpdOtherReaReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPcfSoRpUpdOtherReaReqs.setStatus("current")
_CCdmaPcfSoRpUpdReaUnSpecFails_Type = ZeroBasedCounter32
_CCdmaPcfSoRpUpdReaUnSpecFails_Object = MibTableColumn
cCdmaPcfSoRpUpdReaUnSpecFails = _CCdmaPcfSoRpUpdReaUnSpecFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 11, 1, 1, 15),
    _CCdmaPcfSoRpUpdReaUnSpecFails_Type()
)
cCdmaPcfSoRpUpdReaUnSpecFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPcfSoRpUpdReaUnSpecFails.setStatus("current")
_CCdmaPcfSoRpUpdAdmnFails_Type = ZeroBasedCounter32
_CCdmaPcfSoRpUpdAdmnFails_Object = MibTableColumn
cCdmaPcfSoRpUpdAdmnFails = _CCdmaPcfSoRpUpdAdmnFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 11, 1, 1, 16),
    _CCdmaPcfSoRpUpdAdmnFails_Type()
)
cCdmaPcfSoRpUpdAdmnFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPcfSoRpUpdAdmnFails.setStatus("current")
_CCdmaPcfSoRpUpdMNAuthFails_Type = ZeroBasedCounter32
_CCdmaPcfSoRpUpdMNAuthFails_Object = MibTableColumn
cCdmaPcfSoRpUpdMNAuthFails = _CCdmaPcfSoRpUpdMNAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 11, 1, 1, 17),
    _CCdmaPcfSoRpUpdMNAuthFails_Type()
)
cCdmaPcfSoRpUpdMNAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPcfSoRpUpdMNAuthFails.setStatus("current")
_CCdmaPcfSoRpUpdIdMismatFails_Type = ZeroBasedCounter32
_CCdmaPcfSoRpUpdIdMismatFails_Object = MibTableColumn
cCdmaPcfSoRpUpdIdMismatFails = _CCdmaPcfSoRpUpdIdMismatFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 11, 1, 1, 18),
    _CCdmaPcfSoRpUpdIdMismatFails_Type()
)
cCdmaPcfSoRpUpdIdMismatFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPcfSoRpUpdIdMismatFails.setStatus("current")
_CCdmaPcfSoRpUpdBadReqFails_Type = ZeroBasedCounter32
_CCdmaPcfSoRpUpdBadReqFails_Object = MibTableColumn
cCdmaPcfSoRpUpdBadReqFails = _CCdmaPcfSoRpUpdBadReqFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 11, 1, 1, 19),
    _CCdmaPcfSoRpUpdBadReqFails_Type()
)
cCdmaPcfSoRpUpdBadReqFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPcfSoRpUpdBadReqFails.setStatus("current")
_CCdmaSoRpUpdPcfHandoffs_Type = ZeroBasedCounter32
_CCdmaSoRpUpdPcfHandoffs_Object = MibTableColumn
cCdmaSoRpUpdPcfHandoffs = _CCdmaSoRpUpdPcfHandoffs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 11, 1, 1, 20),
    _CCdmaSoRpUpdPcfHandoffs_Type()
)
cCdmaSoRpUpdPcfHandoffs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaSoRpUpdPcfHandoffs.setStatus("current")
_CCdmaSoRpUpdHandoffNotAckedReqs_Type = ZeroBasedCounter32
_CCdmaSoRpUpdHandoffNotAckedReqs_Object = MibTableColumn
cCdmaSoRpUpdHandoffNotAckedReqs = _CCdmaSoRpUpdHandoffNotAckedReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 11, 1, 1, 21),
    _CCdmaSoRpUpdHandoffNotAckedReqs_Type()
)
cCdmaSoRpUpdHandoffNotAckedReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaSoRpUpdHandoffNotAckedReqs.setStatus("current")
_CCdmaSoRpUpdHandoffReceivedAcks_Type = ZeroBasedCounter32
_CCdmaSoRpUpdHandoffReceivedAcks_Object = MibTableColumn
cCdmaSoRpUpdHandoffReceivedAcks = _CCdmaSoRpUpdHandoffReceivedAcks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 11, 1, 1, 22),
    _CCdmaSoRpUpdHandoffReceivedAcks_Type()
)
cCdmaSoRpUpdHandoffReceivedAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaSoRpUpdHandoffReceivedAcks.setStatus("current")
_CCdmaSoRpUpdHandoffAcceptedReqs_Type = ZeroBasedCounter32
_CCdmaSoRpUpdHandoffAcceptedReqs_Object = MibTableColumn
cCdmaSoRpUpdHandoffAcceptedReqs = _CCdmaSoRpUpdHandoffAcceptedReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 11, 1, 1, 23),
    _CCdmaSoRpUpdHandoffAcceptedReqs_Type()
)
cCdmaSoRpUpdHandoffAcceptedReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaSoRpUpdHandoffAcceptedReqs.setStatus("current")
_CCdmaSoRpUpdHandoffDeniedReqs_Type = ZeroBasedCounter32
_CCdmaSoRpUpdHandoffDeniedReqs_Object = MibTableColumn
cCdmaSoRpUpdHandoffDeniedReqs = _CCdmaSoRpUpdHandoffDeniedReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 11, 1, 1, 24),
    _CCdmaSoRpUpdHandoffDeniedReqs_Type()
)
cCdmaSoRpUpdHandoffDeniedReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaSoRpUpdHandoffDeniedReqs.setStatus("current")
_CCdmaSoRpUpdHandoffDiscardedAcks_Type = ZeroBasedCounter32
_CCdmaSoRpUpdHandoffDiscardedAcks_Object = MibTableColumn
cCdmaSoRpUpdHandoffDiscardedAcks = _CCdmaSoRpUpdHandoffDiscardedAcks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 11, 1, 1, 25),
    _CCdmaSoRpUpdHandoffDiscardedAcks_Type()
)
cCdmaSoRpUpdHandoffDiscardedAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaSoRpUpdHandoffDiscardedAcks.setStatus("current")
_CCdmaSoRpUpdHandoffInitTxdReqs_Type = ZeroBasedCounter32
_CCdmaSoRpUpdHandoffInitTxdReqs_Object = MibTableColumn
cCdmaSoRpUpdHandoffInitTxdReqs = _CCdmaSoRpUpdHandoffInitTxdReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 11, 1, 1, 26),
    _CCdmaSoRpUpdHandoffInitTxdReqs_Type()
)
cCdmaSoRpUpdHandoffInitTxdReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaSoRpUpdHandoffInitTxdReqs.setStatus("current")
_CCdmaSoRpUpdHandoffReTxdReqs_Type = ZeroBasedCounter32
_CCdmaSoRpUpdHandoffReTxdReqs_Object = MibTableColumn
cCdmaSoRpUpdHandoffReTxdReqs = _CCdmaSoRpUpdHandoffReTxdReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 11, 1, 1, 27),
    _CCdmaSoRpUpdHandoffReTxdReqs_Type()
)
cCdmaSoRpUpdHandoffReTxdReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaSoRpUpdHandoffReTxdReqs.setStatus("current")
_CCdmaSoRpUpdHandoffReaUnSpecFails_Type = ZeroBasedCounter32
_CCdmaSoRpUpdHandoffReaUnSpecFails_Object = MibTableColumn
cCdmaSoRpUpdHandoffReaUnSpecFails = _CCdmaSoRpUpdHandoffReaUnSpecFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 11, 1, 1, 28),
    _CCdmaSoRpUpdHandoffReaUnSpecFails_Type()
)
cCdmaSoRpUpdHandoffReaUnSpecFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaSoRpUpdHandoffReaUnSpecFails.setStatus("current")
_CCdmaSoRpUpdHandoffAdmProhibFails_Type = ZeroBasedCounter32
_CCdmaSoRpUpdHandoffAdmProhibFails_Object = MibTableColumn
cCdmaSoRpUpdHandoffAdmProhibFails = _CCdmaSoRpUpdHandoffAdmProhibFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 11, 1, 1, 29),
    _CCdmaSoRpUpdHandoffAdmProhibFails_Type()
)
cCdmaSoRpUpdHandoffAdmProhibFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaSoRpUpdHandoffAdmProhibFails.setStatus("current")
_CCdmaSoRpUpdHandoffMNAuthenFails_Type = ZeroBasedCounter32
_CCdmaSoRpUpdHandoffMNAuthenFails_Object = MibTableColumn
cCdmaSoRpUpdHandoffMNAuthenFails = _CCdmaSoRpUpdHandoffMNAuthenFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 11, 1, 1, 30),
    _CCdmaSoRpUpdHandoffMNAuthenFails_Type()
)
cCdmaSoRpUpdHandoffMNAuthenFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaSoRpUpdHandoffMNAuthenFails.setStatus("current")
_CCdmaSoRpUpdHandoffIdMismatchFails_Type = ZeroBasedCounter32
_CCdmaSoRpUpdHandoffIdMismatchFails_Object = MibTableColumn
cCdmaSoRpUpdHandoffIdMismatchFails = _CCdmaSoRpUpdHandoffIdMismatchFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 11, 1, 1, 31),
    _CCdmaSoRpUpdHandoffIdMismatchFails_Type()
)
cCdmaSoRpUpdHandoffIdMismatchFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaSoRpUpdHandoffIdMismatchFails.setStatus("current")
_CCdmaSoRpUpdHandoffBadReqFails_Type = ZeroBasedCounter32
_CCdmaSoRpUpdHandoffBadReqFails_Object = MibTableColumn
cCdmaSoRpUpdHandoffBadReqFails = _CCdmaSoRpUpdHandoffBadReqFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 11, 1, 1, 32),
    _CCdmaSoRpUpdHandoffBadReqFails_Type()
)
cCdmaSoRpUpdHandoffBadReqFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaSoRpUpdHandoffBadReqFails.setStatus("current")
_CCdmaPcfSoPppSetupStats_ObjectIdentity = ObjectIdentity
cCdmaPcfSoPppSetupStats = _CCdmaPcfSoPppSetupStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 12)
)
_CCdmaPcfSoPppSetupStatsTable_Object = MibTable
cCdmaPcfSoPppSetupStatsTable = _CCdmaPcfSoPppSetupStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 12, 1)
)
if mibBuilder.loadTexts:
    cCdmaPcfSoPppSetupStatsTable.setStatus("current")
_CCdmaPcfSoPppSetupStatsEntry_Object = MibTableRow
cCdmaPcfSoPppSetupStatsEntry = _CCdmaPcfSoPppSetupStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 12, 1, 1)
)
cCdmaPcfSoPppSetupStatsEntry.setIndexNames(
    (0, "CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoPppSetupIpAddrType"),
    (0, "CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoPppSetupIpAddr"),
    (0, "CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoPppServiceOption"),
)
if mibBuilder.loadTexts:
    cCdmaPcfSoPppSetupStatsEntry.setStatus("current")
_CCdmaPcfSoPppSetupIpAddrType_Type = InetAddressType
_CCdmaPcfSoPppSetupIpAddrType_Object = MibTableColumn
cCdmaPcfSoPppSetupIpAddrType = _CCdmaPcfSoPppSetupIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 12, 1, 1, 1),
    _CCdmaPcfSoPppSetupIpAddrType_Type()
)
cCdmaPcfSoPppSetupIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cCdmaPcfSoPppSetupIpAddrType.setStatus("current")
_CCdmaPcfSoPppSetupIpAddr_Type = InetAddress
_CCdmaPcfSoPppSetupIpAddr_Object = MibTableColumn
cCdmaPcfSoPppSetupIpAddr = _CCdmaPcfSoPppSetupIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 12, 1, 1, 2),
    _CCdmaPcfSoPppSetupIpAddr_Type()
)
cCdmaPcfSoPppSetupIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cCdmaPcfSoPppSetupIpAddr.setStatus("current")
_CCdmaPcfSoPppServiceOption_Type = CCdmaServiceOption
_CCdmaPcfSoPppServiceOption_Object = MibTableColumn
cCdmaPcfSoPppServiceOption = _CCdmaPcfSoPppServiceOption_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 12, 1, 1, 3),
    _CCdmaPcfSoPppServiceOption_Type()
)
cCdmaPcfSoPppServiceOption.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cCdmaPcfSoPppServiceOption.setStatus("current")
_CCdmaPcfSoPppCurrentConns_Type = Gauge32
_CCdmaPcfSoPppCurrentConns_Object = MibTableColumn
cCdmaPcfSoPppCurrentConns = _CCdmaPcfSoPppCurrentConns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 12, 1, 1, 4),
    _CCdmaPcfSoPppCurrentConns_Type()
)
cCdmaPcfSoPppCurrentConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPcfSoPppCurrentConns.setStatus("current")
_CCdmaPcfSoPppConnInitiateReqs_Type = ZeroBasedCounter32
_CCdmaPcfSoPppConnInitiateReqs_Object = MibTableColumn
cCdmaPcfSoPppConnInitiateReqs = _CCdmaPcfSoPppConnInitiateReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 12, 1, 1, 5),
    _CCdmaPcfSoPppConnInitiateReqs_Type()
)
cCdmaPcfSoPppConnInitiateReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPcfSoPppConnInitiateReqs.setStatus("current")
_CCdmaPcfSoPppConnSuccesses_Type = ZeroBasedCounter32
_CCdmaPcfSoPppConnSuccesses_Object = MibTableColumn
cCdmaPcfSoPppConnSuccesses = _CCdmaPcfSoPppConnSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 12, 1, 1, 6),
    _CCdmaPcfSoPppConnSuccesses_Type()
)
cCdmaPcfSoPppConnSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPcfSoPppConnSuccesses.setStatus("current")
_CCdmaPcfSoPppConnFails_Type = ZeroBasedCounter32
_CCdmaPcfSoPppConnFails_Object = MibTableColumn
cCdmaPcfSoPppConnFails = _CCdmaPcfSoPppConnFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 12, 1, 1, 7),
    _CCdmaPcfSoPppConnFails_Type()
)
cCdmaPcfSoPppConnFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPcfSoPppConnFails.setStatus("current")
_CCdmaPcfSoPppConnAborts_Type = ZeroBasedCounter32
_CCdmaPcfSoPppConnAborts_Object = MibTableColumn
cCdmaPcfSoPppConnAborts = _CCdmaPcfSoPppConnAborts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 12, 1, 1, 8),
    _CCdmaPcfSoPppConnAborts_Type()
)
cCdmaPcfSoPppConnAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPcfSoPppConnAborts.setStatus("current")
_CCdmaRpSessUpdStats_ObjectIdentity = ObjectIdentity
cCdmaRpSessUpdStats = _CCdmaRpSessUpdStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 13)
)
_CCdmaRpSessUpdTransmittedReqs_Type = ZeroBasedCounter32
_CCdmaRpSessUpdTransmittedReqs_Object = MibScalar
cCdmaRpSessUpdTransmittedReqs = _CCdmaRpSessUpdTransmittedReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 13, 1),
    _CCdmaRpSessUpdTransmittedReqs_Type()
)
cCdmaRpSessUpdTransmittedReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpSessUpdTransmittedReqs.setStatus("current")
_CCdmaRpSessUpdAcceptedReqs_Type = ZeroBasedCounter32
_CCdmaRpSessUpdAcceptedReqs_Object = MibScalar
cCdmaRpSessUpdAcceptedReqs = _CCdmaRpSessUpdAcceptedReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 13, 2),
    _CCdmaRpSessUpdAcceptedReqs_Type()
)
cCdmaRpSessUpdAcceptedReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpSessUpdAcceptedReqs.setStatus("current")
_CCdmaRpSessUpdDeniedReqs_Type = ZeroBasedCounter32
_CCdmaRpSessUpdDeniedReqs_Object = MibScalar
cCdmaRpSessUpdDeniedReqs = _CCdmaRpSessUpdDeniedReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 13, 3),
    _CCdmaRpSessUpdDeniedReqs_Type()
)
cCdmaRpSessUpdDeniedReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpSessUpdDeniedReqs.setStatus("current")
_CCdmaRpSessUpdNotAckedReqs_Type = ZeroBasedCounter32
_CCdmaRpSessUpdNotAckedReqs_Object = MibScalar
cCdmaRpSessUpdNotAckedReqs = _CCdmaRpSessUpdNotAckedReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 13, 4),
    _CCdmaRpSessUpdNotAckedReqs_Type()
)
cCdmaRpSessUpdNotAckedReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpSessUpdNotAckedReqs.setStatus("current")
_CCdmaRpSessUpdInitTransmittedReqs_Type = ZeroBasedCounter32
_CCdmaRpSessUpdInitTransmittedReqs_Object = MibScalar
cCdmaRpSessUpdInitTransmittedReqs = _CCdmaRpSessUpdInitTransmittedReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 13, 5),
    _CCdmaRpSessUpdInitTransmittedReqs_Type()
)
cCdmaRpSessUpdInitTransmittedReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpSessUpdInitTransmittedReqs.setStatus("current")
_CCdmaRpSessUpdReTransmittedReqs_Type = ZeroBasedCounter32
_CCdmaRpSessUpdReTransmittedReqs_Object = MibScalar
cCdmaRpSessUpdReTransmittedReqs = _CCdmaRpSessUpdReTransmittedReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 13, 6),
    _CCdmaRpSessUpdReTransmittedReqs_Type()
)
cCdmaRpSessUpdReTransmittedReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpSessUpdReTransmittedReqs.setStatus("current")
_CCdmaRpSessUpdReceivedAcks_Type = ZeroBasedCounter32
_CCdmaRpSessUpdReceivedAcks_Object = MibScalar
cCdmaRpSessUpdReceivedAcks = _CCdmaRpSessUpdReceivedAcks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 13, 7),
    _CCdmaRpSessUpdReceivedAcks_Type()
)
cCdmaRpSessUpdReceivedAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpSessUpdReceivedAcks.setStatus("current")
_CCdmaRpSessUpdDiscardedAcks_Type = ZeroBasedCounter32
_CCdmaRpSessUpdDiscardedAcks_Object = MibScalar
cCdmaRpSessUpdDiscardedAcks = _CCdmaRpSessUpdDiscardedAcks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 13, 8),
    _CCdmaRpSessUpdDiscardedAcks_Type()
)
cCdmaRpSessUpdDiscardedAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpSessUpdDiscardedAcks.setStatus("current")
_CCdmaRpSessUpdAlwaysON_Type = ZeroBasedCounter32
_CCdmaRpSessUpdAlwaysON_Object = MibScalar
cCdmaRpSessUpdAlwaysON = _CCdmaRpSessUpdAlwaysON_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 13, 9),
    _CCdmaRpSessUpdAlwaysON_Type()
)
cCdmaRpSessUpdAlwaysON.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpSessUpdAlwaysON.setStatus("current")
_CCdmaRpSessUpdRNPDIT_Type = ZeroBasedCounter32
_CCdmaRpSessUpdRNPDIT_Object = MibScalar
cCdmaRpSessUpdRNPDIT = _CCdmaRpSessUpdRNPDIT_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 13, 10),
    _CCdmaRpSessUpdRNPDIT_Type()
)
cCdmaRpSessUpdRNPDIT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpSessUpdRNPDIT.setStatus("current")
_CCdmaRpSessUpdReasonUnSpecFailures_Type = ZeroBasedCounter32
_CCdmaRpSessUpdReasonUnSpecFailures_Object = MibScalar
cCdmaRpSessUpdReasonUnSpecFailures = _CCdmaRpSessUpdReasonUnSpecFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 13, 11),
    _CCdmaRpSessUpdReasonUnSpecFailures_Type()
)
cCdmaRpSessUpdReasonUnSpecFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpSessUpdReasonUnSpecFailures.setStatus("current")
_CCdmaRpSessUpdReasonParamNotUpdated_Type = ZeroBasedCounter32
_CCdmaRpSessUpdReasonParamNotUpdated_Object = MibScalar
cCdmaRpSessUpdReasonParamNotUpdated = _CCdmaRpSessUpdReasonParamNotUpdated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 13, 12),
    _CCdmaRpSessUpdReasonParamNotUpdated_Type()
)
cCdmaRpSessUpdReasonParamNotUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpSessUpdReasonParamNotUpdated.setStatus("current")
_CCdmaRpSessUpdMNAuthenFailures_Type = ZeroBasedCounter32
_CCdmaRpSessUpdMNAuthenFailures_Object = MibScalar
cCdmaRpSessUpdMNAuthenFailures = _CCdmaRpSessUpdMNAuthenFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 13, 13),
    _CCdmaRpSessUpdMNAuthenFailures_Type()
)
cCdmaRpSessUpdMNAuthenFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpSessUpdMNAuthenFailures.setStatus("current")
_CCdmaRpSessUpdIdentMismatchFailures_Type = ZeroBasedCounter32
_CCdmaRpSessUpdIdentMismatchFailures_Object = MibScalar
cCdmaRpSessUpdIdentMismatchFailures = _CCdmaRpSessUpdIdentMismatchFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 13, 14),
    _CCdmaRpSessUpdIdentMismatchFailures_Type()
)
cCdmaRpSessUpdIdentMismatchFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpSessUpdIdentMismatchFailures.setStatus("current")
_CCdmaRpSessUpdBadReqFailures_Type = ZeroBasedCounter32
_CCdmaRpSessUpdBadReqFailures_Object = MibScalar
cCdmaRpSessUpdBadReqFailures = _CCdmaRpSessUpdBadReqFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 13, 15),
    _CCdmaRpSessUpdBadReqFailures_Type()
)
cCdmaRpSessUpdBadReqFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpSessUpdBadReqFailures.setStatus("current")
_CCdmaPcfSoRpSessUpdStats_ObjectIdentity = ObjectIdentity
cCdmaPcfSoRpSessUpdStats = _CCdmaPcfSoRpSessUpdStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 14)
)
_CCdmaPcfSoRpSessUpdStatsTable_Object = MibTable
cCdmaPcfSoRpSessUpdStatsTable = _CCdmaPcfSoRpSessUpdStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 14, 1)
)
if mibBuilder.loadTexts:
    cCdmaPcfSoRpSessUpdStatsTable.setStatus("current")
_CCdmaPcfSoRpSessUpdStatsEntry_Object = MibTableRow
cCdmaPcfSoRpSessUpdStatsEntry = _CCdmaPcfSoRpSessUpdStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 14, 1, 1)
)
cCdmaPcfSoRpSessUpdStatsEntry.setIndexNames(
    (0, "CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoRpSessUpdIpAddrType"),
    (0, "CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoRpSessUpdIpAddr"),
    (0, "CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoRpSessUpdServiceOption"),
)
if mibBuilder.loadTexts:
    cCdmaPcfSoRpSessUpdStatsEntry.setStatus("current")
_CCdmaPcfSoRpSessUpdIpAddrType_Type = InetAddressType
_CCdmaPcfSoRpSessUpdIpAddrType_Object = MibTableColumn
cCdmaPcfSoRpSessUpdIpAddrType = _CCdmaPcfSoRpSessUpdIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 14, 1, 1, 1),
    _CCdmaPcfSoRpSessUpdIpAddrType_Type()
)
cCdmaPcfSoRpSessUpdIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cCdmaPcfSoRpSessUpdIpAddrType.setStatus("current")
_CCdmaPcfSoRpSessUpdIpAddr_Type = InetAddress
_CCdmaPcfSoRpSessUpdIpAddr_Object = MibTableColumn
cCdmaPcfSoRpSessUpdIpAddr = _CCdmaPcfSoRpSessUpdIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 14, 1, 1, 2),
    _CCdmaPcfSoRpSessUpdIpAddr_Type()
)
cCdmaPcfSoRpSessUpdIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cCdmaPcfSoRpSessUpdIpAddr.setStatus("current")
_CCdmaPcfSoRpSessUpdServiceOption_Type = CCdmaServiceOption
_CCdmaPcfSoRpSessUpdServiceOption_Object = MibTableColumn
cCdmaPcfSoRpSessUpdServiceOption = _CCdmaPcfSoRpSessUpdServiceOption_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 14, 1, 1, 3),
    _CCdmaPcfSoRpSessUpdServiceOption_Type()
)
cCdmaPcfSoRpSessUpdServiceOption.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cCdmaPcfSoRpSessUpdServiceOption.setStatus("current")
_CCdmaPcfSoRpSessUpdTxdReqs_Type = ZeroBasedCounter32
_CCdmaPcfSoRpSessUpdTxdReqs_Object = MibTableColumn
cCdmaPcfSoRpSessUpdTxdReqs = _CCdmaPcfSoRpSessUpdTxdReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 14, 1, 1, 4),
    _CCdmaPcfSoRpSessUpdTxdReqs_Type()
)
cCdmaPcfSoRpSessUpdTxdReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPcfSoRpSessUpdTxdReqs.setStatus("current")
_CCdmaPcfSoRpSessUpdAcptdReqs_Type = ZeroBasedCounter32
_CCdmaPcfSoRpSessUpdAcptdReqs_Object = MibTableColumn
cCdmaPcfSoRpSessUpdAcptdReqs = _CCdmaPcfSoRpSessUpdAcptdReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 14, 1, 1, 5),
    _CCdmaPcfSoRpSessUpdAcptdReqs_Type()
)
cCdmaPcfSoRpSessUpdAcptdReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPcfSoRpSessUpdAcptdReqs.setStatus("current")
_CCdmaPcfSoRpSessUpdDeniedReqs_Type = ZeroBasedCounter32
_CCdmaPcfSoRpSessUpdDeniedReqs_Object = MibTableColumn
cCdmaPcfSoRpSessUpdDeniedReqs = _CCdmaPcfSoRpSessUpdDeniedReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 14, 1, 1, 6),
    _CCdmaPcfSoRpSessUpdDeniedReqs_Type()
)
cCdmaPcfSoRpSessUpdDeniedReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPcfSoRpSessUpdDeniedReqs.setStatus("current")
_CCdmaPcfSoRpSessUpdNotAckedReqs_Type = ZeroBasedCounter32
_CCdmaPcfSoRpSessUpdNotAckedReqs_Object = MibTableColumn
cCdmaPcfSoRpSessUpdNotAckedReqs = _CCdmaPcfSoRpSessUpdNotAckedReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 14, 1, 1, 7),
    _CCdmaPcfSoRpSessUpdNotAckedReqs_Type()
)
cCdmaPcfSoRpSessUpdNotAckedReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPcfSoRpSessUpdNotAckedReqs.setStatus("current")
_CCdmaPcfSoRpSessUpdInitTxdReqs_Type = ZeroBasedCounter32
_CCdmaPcfSoRpSessUpdInitTxdReqs_Object = MibTableColumn
cCdmaPcfSoRpSessUpdInitTxdReqs = _CCdmaPcfSoRpSessUpdInitTxdReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 14, 1, 1, 8),
    _CCdmaPcfSoRpSessUpdInitTxdReqs_Type()
)
cCdmaPcfSoRpSessUpdInitTxdReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPcfSoRpSessUpdInitTxdReqs.setStatus("current")
_CCdmaPcfSoRpSessUpdReTxdReqs_Type = ZeroBasedCounter32
_CCdmaPcfSoRpSessUpdReTxdReqs_Object = MibTableColumn
cCdmaPcfSoRpSessUpdReTxdReqs = _CCdmaPcfSoRpSessUpdReTxdReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 14, 1, 1, 9),
    _CCdmaPcfSoRpSessUpdReTxdReqs_Type()
)
cCdmaPcfSoRpSessUpdReTxdReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPcfSoRpSessUpdReTxdReqs.setStatus("current")
_CCdmaPcfSoRpSessUpdRcvdAcks_Type = ZeroBasedCounter32
_CCdmaPcfSoRpSessUpdRcvdAcks_Object = MibTableColumn
cCdmaPcfSoRpSessUpdRcvdAcks = _CCdmaPcfSoRpSessUpdRcvdAcks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 14, 1, 1, 10),
    _CCdmaPcfSoRpSessUpdRcvdAcks_Type()
)
cCdmaPcfSoRpSessUpdRcvdAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPcfSoRpSessUpdRcvdAcks.setStatus("current")
_CCdmaPcfSoRpSessUpdDiscardedAcks_Type = ZeroBasedCounter32
_CCdmaPcfSoRpSessUpdDiscardedAcks_Object = MibTableColumn
cCdmaPcfSoRpSessUpdDiscardedAcks = _CCdmaPcfSoRpSessUpdDiscardedAcks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 14, 1, 1, 11),
    _CCdmaPcfSoRpSessUpdDiscardedAcks_Type()
)
cCdmaPcfSoRpSessUpdDiscardedAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPcfSoRpSessUpdDiscardedAcks.setStatus("current")
_CCdmaPcfSoRpSessUpdAlwaysOn_Type = ZeroBasedCounter32
_CCdmaPcfSoRpSessUpdAlwaysOn_Object = MibTableColumn
cCdmaPcfSoRpSessUpdAlwaysOn = _CCdmaPcfSoRpSessUpdAlwaysOn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 14, 1, 1, 12),
    _CCdmaPcfSoRpSessUpdAlwaysOn_Type()
)
cCdmaPcfSoRpSessUpdAlwaysOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPcfSoRpSessUpdAlwaysOn.setStatus("current")
_CCdmaPcfSoRpSessUpdRNPDIT_Type = ZeroBasedCounter32
_CCdmaPcfSoRpSessUpdRNPDIT_Object = MibTableColumn
cCdmaPcfSoRpSessUpdRNPDIT = _CCdmaPcfSoRpSessUpdRNPDIT_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 14, 1, 1, 13),
    _CCdmaPcfSoRpSessUpdRNPDIT_Type()
)
cCdmaPcfSoRpSessUpdRNPDIT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPcfSoRpSessUpdRNPDIT.setStatus("current")
_CCdmaPcfSoRpSessUpdParamNotUpdated_Type = ZeroBasedCounter32
_CCdmaPcfSoRpSessUpdParamNotUpdated_Object = MibTableColumn
cCdmaPcfSoRpSessUpdParamNotUpdated = _CCdmaPcfSoRpSessUpdParamNotUpdated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 14, 1, 1, 14),
    _CCdmaPcfSoRpSessUpdParamNotUpdated_Type()
)
cCdmaPcfSoRpSessUpdParamNotUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPcfSoRpSessUpdParamNotUpdated.setStatus("current")
_CCdmaPcfSoRpSessUpdReaUnSpecFails_Type = ZeroBasedCounter32
_CCdmaPcfSoRpSessUpdReaUnSpecFails_Object = MibTableColumn
cCdmaPcfSoRpSessUpdReaUnSpecFails = _CCdmaPcfSoRpSessUpdReaUnSpecFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 14, 1, 1, 15),
    _CCdmaPcfSoRpSessUpdReaUnSpecFails_Type()
)
cCdmaPcfSoRpSessUpdReaUnSpecFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPcfSoRpSessUpdReaUnSpecFails.setStatus("current")
_CCdmaPcfSoRpSessUpdMNAuthFails_Type = ZeroBasedCounter32
_CCdmaPcfSoRpSessUpdMNAuthFails_Object = MibTableColumn
cCdmaPcfSoRpSessUpdMNAuthFails = _CCdmaPcfSoRpSessUpdMNAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 14, 1, 1, 16),
    _CCdmaPcfSoRpSessUpdMNAuthFails_Type()
)
cCdmaPcfSoRpSessUpdMNAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPcfSoRpSessUpdMNAuthFails.setStatus("current")
_CCdmaPcfSoRpSessUpdIdMismatFails_Type = ZeroBasedCounter32
_CCdmaPcfSoRpSessUpdIdMismatFails_Object = MibTableColumn
cCdmaPcfSoRpSessUpdIdMismatFails = _CCdmaPcfSoRpSessUpdIdMismatFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 14, 1, 1, 17),
    _CCdmaPcfSoRpSessUpdIdMismatFails_Type()
)
cCdmaPcfSoRpSessUpdIdMismatFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPcfSoRpSessUpdIdMismatFails.setStatus("current")
_CCdmaPcfSoRpSessUpdBadReqFails_Type = ZeroBasedCounter32
_CCdmaPcfSoRpSessUpdBadReqFails_Object = MibTableColumn
cCdmaPcfSoRpSessUpdBadReqFails = _CCdmaPcfSoRpSessUpdBadReqFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 7, 14, 1, 1, 18),
    _CCdmaPcfSoRpSessUpdBadReqFails_Type()
)
cCdmaPcfSoRpSessUpdBadReqFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaPcfSoRpSessUpdBadReqFails.setStatus("current")
_CCdmaConfig_ObjectIdentity = ObjectIdentity
cCdmaConfig = _CCdmaConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 8)
)
_CCdmaThresholdConfig_ObjectIdentity = ObjectIdentity
cCdmaThresholdConfig = _CCdmaThresholdConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 8, 1)
)
_CCdmaSessionHighThreshold_Type = Unsigned32
_CCdmaSessionHighThreshold_Object = MibScalar
cCdmaSessionHighThreshold = _CCdmaSessionHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 8, 1, 1),
    _CCdmaSessionHighThreshold_Type()
)
cCdmaSessionHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cCdmaSessionHighThreshold.setStatus("current")
_CCdmaSessionLowThreshold_Type = Unsigned32
_CCdmaSessionLowThreshold_Object = MibScalar
cCdmaSessionLowThreshold = _CCdmaSessionLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 8, 1, 2),
    _CCdmaSessionLowThreshold_Type()
)
cCdmaSessionLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cCdmaSessionLowThreshold.setStatus("current")
_CCdmaPdsnCluster_ObjectIdentity = ObjectIdentity
cCdmaPdsnCluster = _CCdmaPdsnCluster_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 8, 2)
)
_CCdmaClusterCommon_ObjectIdentity = ObjectIdentity
cCdmaClusterCommon = _CCdmaClusterCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 8, 2, 1)
)


class _CCdmaClusterType_Type(Integer32):
    """Custom type cCdmaClusterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("controllerMember", 2),
          ("nonCluster", 0),
          ("peerToPeer", 1))
    )


_CCdmaClusterType_Type.__name__ = "Integer32"
_CCdmaClusterType_Object = MibScalar
cCdmaClusterType = _CCdmaClusterType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 8, 2, 1, 1),
    _CCdmaClusterType_Type()
)
cCdmaClusterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaClusterType.setStatus("current")


class _CCdmaClusterRole_Type(Integer32):
    """Custom type cCdmaClusterRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("collocated", 3),
          ("controller", 1),
          ("member", 2),
          ("notApply", 0))
    )


_CCdmaClusterRole_Type.__name__ = "Integer32"
_CCdmaClusterRole_Object = MibScalar
cCdmaClusterRole = _CCdmaClusterRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 8, 2, 1, 2),
    _CCdmaClusterRole_Type()
)
cCdmaClusterRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaClusterRole.setStatus("current")
_CCdmaClusterMemberInfo_ObjectIdentity = ObjectIdentity
cCdmaClusterMemberInfo = _CCdmaClusterMemberInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 8, 2, 2)
)
_CCdmaClusterTotalControllers_Type = Gauge32
_CCdmaClusterTotalControllers_Object = MibScalar
cCdmaClusterTotalControllers = _CCdmaClusterTotalControllers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 8, 2, 2, 1),
    _CCdmaClusterTotalControllers_Type()
)
cCdmaClusterTotalControllers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaClusterTotalControllers.setStatus("current")
_CCdmaClusterCtrlTable_Object = MibTable
cCdmaClusterCtrlTable = _CCdmaClusterCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 8, 2, 2, 2)
)
if mibBuilder.loadTexts:
    cCdmaClusterCtrlTable.setStatus("current")
_CCdmaClusterCtrlEntry_Object = MibTableRow
cCdmaClusterCtrlEntry = _CCdmaClusterCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 8, 2, 2, 2, 1)
)
cCdmaClusterCtrlEntry.setIndexNames(
    (0, "CISCO-CDMA-PDSN-MIB", "cCdmaClusterCtrlAddressType"),
    (0, "CISCO-CDMA-PDSN-MIB", "cCdmaClusterCtrlAddress"),
)
if mibBuilder.loadTexts:
    cCdmaClusterCtrlEntry.setStatus("current")
_CCdmaClusterCtrlAddressType_Type = InetAddressType
_CCdmaClusterCtrlAddressType_Object = MibTableColumn
cCdmaClusterCtrlAddressType = _CCdmaClusterCtrlAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 8, 2, 2, 2, 1, 1),
    _CCdmaClusterCtrlAddressType_Type()
)
cCdmaClusterCtrlAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cCdmaClusterCtrlAddressType.setStatus("current")
_CCdmaClusterCtrlAddress_Type = InetAddress
_CCdmaClusterCtrlAddress_Object = MibTableColumn
cCdmaClusterCtrlAddress = _CCdmaClusterCtrlAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 8, 2, 2, 2, 1, 2),
    _CCdmaClusterCtrlAddress_Type()
)
cCdmaClusterCtrlAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cCdmaClusterCtrlAddress.setStatus("current")


class _CCdmaClusterCtrlStatus_Type(Integer32):
    """Custom type cCdmaClusterCtrlStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alive", 3),
          ("configured", 2),
          ("notConfigured", 1))
    )


_CCdmaClusterCtrlStatus_Type.__name__ = "Integer32"
_CCdmaClusterCtrlStatus_Object = MibTableColumn
cCdmaClusterCtrlStatus = _CCdmaClusterCtrlStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 8, 2, 2, 2, 1, 3),
    _CCdmaClusterCtrlStatus_Type()
)
cCdmaClusterCtrlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaClusterCtrlStatus.setStatus("current")
_CCdmaClusterControllerInfo_ObjectIdentity = ObjectIdentity
cCdmaClusterControllerInfo = _CCdmaClusterControllerInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 8, 2, 3)
)
_CCdmaClusterTotalSessions_Type = Gauge32
_CCdmaClusterTotalSessions_Object = MibScalar
cCdmaClusterTotalSessions = _CCdmaClusterTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 8, 2, 3, 1),
    _CCdmaClusterTotalSessions_Type()
)
cCdmaClusterTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaClusterTotalSessions.setStatus("current")
_CCdmaClusterSessHighThreshold_Type = Unsigned32
_CCdmaClusterSessHighThreshold_Object = MibScalar
cCdmaClusterSessHighThreshold = _CCdmaClusterSessHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 8, 2, 3, 2),
    _CCdmaClusterSessHighThreshold_Type()
)
cCdmaClusterSessHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cCdmaClusterSessHighThreshold.setStatus("current")
_CCdmaClusterSessLowThreshold_Type = Unsigned32
_CCdmaClusterSessLowThreshold_Object = MibScalar
cCdmaClusterSessLowThreshold = _CCdmaClusterSessLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 8, 2, 3, 3),
    _CCdmaClusterSessLowThreshold_Type()
)
cCdmaClusterSessLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cCdmaClusterSessLowThreshold.setStatus("current")
_CCdmaClusterTotalMembers_Type = Gauge32
_CCdmaClusterTotalMembers_Object = MibScalar
cCdmaClusterTotalMembers = _CCdmaClusterTotalMembers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 8, 2, 3, 4),
    _CCdmaClusterTotalMembers_Type()
)
cCdmaClusterTotalMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaClusterTotalMembers.setStatus("current")
_CCdmaClusterMemberTable_Object = MibTable
cCdmaClusterMemberTable = _CCdmaClusterMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 8, 2, 3, 5)
)
if mibBuilder.loadTexts:
    cCdmaClusterMemberTable.setStatus("current")
_CCdmaClusterMemberEntry_Object = MibTableRow
cCdmaClusterMemberEntry = _CCdmaClusterMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 8, 2, 3, 5, 1)
)
cCdmaClusterMemberEntry.setIndexNames(
    (0, "CISCO-CDMA-PDSN-MIB", "cCdmaClusterMemberAddressType"),
    (0, "CISCO-CDMA-PDSN-MIB", "cCdmaClusterMemberAddress"),
)
if mibBuilder.loadTexts:
    cCdmaClusterMemberEntry.setStatus("current")
_CCdmaClusterMemberAddressType_Type = InetAddressType
_CCdmaClusterMemberAddressType_Object = MibTableColumn
cCdmaClusterMemberAddressType = _CCdmaClusterMemberAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 8, 2, 3, 5, 1, 1),
    _CCdmaClusterMemberAddressType_Type()
)
cCdmaClusterMemberAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cCdmaClusterMemberAddressType.setStatus("current")
_CCdmaClusterMemberAddress_Type = InetAddress
_CCdmaClusterMemberAddress_Object = MibTableColumn
cCdmaClusterMemberAddress = _CCdmaClusterMemberAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 8, 2, 3, 5, 1, 2),
    _CCdmaClusterMemberAddress_Type()
)
cCdmaClusterMemberAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cCdmaClusterMemberAddress.setStatus("current")


class _CCdmaClusterMemberStatus_Type(Integer32):
    """Custom type cCdmaClusterMemberStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("adminProhibit", 3),
          ("ready", 2),
          ("unknown", 1))
    )


_CCdmaClusterMemberStatus_Type.__name__ = "Integer32"
_CCdmaClusterMemberStatus_Object = MibTableColumn
cCdmaClusterMemberStatus = _CCdmaClusterMemberStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 8, 2, 3, 5, 1, 3),
    _CCdmaClusterMemberStatus_Type()
)
cCdmaClusterMemberStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaClusterMemberStatus.setStatus("current")
_CCdmaClusterMemberLoad_Type = Unsigned32
_CCdmaClusterMemberLoad_Object = MibTableColumn
cCdmaClusterMemberLoad = _CCdmaClusterMemberLoad_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 8, 2, 3, 5, 1, 4),
    _CCdmaClusterMemberLoad_Type()
)
cCdmaClusterMemberLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaClusterMemberLoad.setStatus("current")
if mibBuilder.loadTexts:
    cCdmaClusterMemberLoad.setUnits("1%")
_CCdmaNotifConfig_ObjectIdentity = ObjectIdentity
cCdmaNotifConfig = _CCdmaNotifConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 8, 3)
)


class _CCdmaNotifSeverityLevel_Type(CCdmaServiceAffectedLevel):
    """Custom type cCdmaNotifSeverityLevel based on CCdmaServiceAffectedLevel"""


_CCdmaNotifSeverityLevel_Object = MibScalar
cCdmaNotifSeverityLevel = _CCdmaNotifSeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 8, 3, 1),
    _CCdmaNotifSeverityLevel_Type()
)
cCdmaNotifSeverityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cCdmaNotifSeverityLevel.setStatus("current")
_CCdmaNotifObjects_ObjectIdentity = ObjectIdentity
cCdmaNotifObjects = _CCdmaNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 9)
)
_CCdmaServiceAffectedLevel_Type = CCdmaServiceAffectedLevel
_CCdmaServiceAffectedLevel_Object = MibScalar
cCdmaServiceAffectedLevel = _CCdmaServiceAffectedLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 9, 1),
    _CCdmaServiceAffectedLevel_Type()
)
cCdmaServiceAffectedLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaServiceAffectedLevel.setStatus("current")
_CCdmaAffectedAddressType_Type = InetAddressType
_CCdmaAffectedAddressType_Object = MibScalar
cCdmaAffectedAddressType = _CCdmaAffectedAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 9, 2),
    _CCdmaAffectedAddressType_Type()
)
cCdmaAffectedAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaAffectedAddressType.setStatus("deprecated")
_CCdmaAffectedAddress_Type = InetAddress
_CCdmaAffectedAddress_Object = MibScalar
cCdmaAffectedAddress = _CCdmaAffectedAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 9, 3),
    _CCdmaAffectedAddress_Type()
)
cCdmaAffectedAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaAffectedAddress.setStatus("deprecated")


class _CCdmaAffectedMemberStatus_Type(Integer32):
    """Custom type cCdmaAffectedMemberStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("adminProhibit", 2),
          ("ready", 1))
    )


_CCdmaAffectedMemberStatus_Type.__name__ = "Integer32"
_CCdmaAffectedMemberStatus_Object = MibScalar
cCdmaAffectedMemberStatus = _CCdmaAffectedMemberStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 9, 4),
    _CCdmaAffectedMemberStatus_Type()
)
cCdmaAffectedMemberStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaAffectedMemberStatus.setStatus("deprecated")


class _CCdmaAffectedCtrlStatus_Type(Integer32):
    """Custom type cCdmaAffectedCtrlStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alive", 2),
          ("configured", 1))
    )


_CCdmaAffectedCtrlStatus_Type.__name__ = "Integer32"
_CCdmaAffectedCtrlStatus_Object = MibScalar
cCdmaAffectedCtrlStatus = _CCdmaAffectedCtrlStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 9, 5),
    _CCdmaAffectedCtrlStatus_Type()
)
cCdmaAffectedCtrlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaAffectedCtrlStatus.setStatus("deprecated")
_CCdmaRpErrors_ObjectIdentity = ObjectIdentity
cCdmaRpErrors = _CCdmaRpErrors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10)
)
_CCdmaRPRegReqErrors_ObjectIdentity = ObjectIdentity
cCdmaRPRegReqErrors = _CCdmaRPRegReqErrors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 1)
)
_CCdmaRegReqInvPakLenErrs_Type = ZeroBasedCounter32
_CCdmaRegReqInvPakLenErrs_Object = MibScalar
cCdmaRegReqInvPakLenErrs = _CCdmaRegReqInvPakLenErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 1, 1),
    _CCdmaRegReqInvPakLenErrs_Type()
)
cCdmaRegReqInvPakLenErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRegReqInvPakLenErrs.setStatus("current")
_CCdmaRegReqInvProtocolErrs_Type = ZeroBasedCounter32
_CCdmaRegReqInvProtocolErrs_Object = MibScalar
cCdmaRegReqInvProtocolErrs = _CCdmaRegReqInvProtocolErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 1, 2),
    _CCdmaRegReqInvProtocolErrs_Type()
)
cCdmaRegReqInvProtocolErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRegReqInvProtocolErrs.setStatus("current")
_CCdmaRegReqInvFlagsErrs_Type = ZeroBasedCounter32
_CCdmaRegReqInvFlagsErrs_Object = MibScalar
cCdmaRegReqInvFlagsErrs = _CCdmaRegReqInvFlagsErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 1, 3),
    _CCdmaRegReqInvFlagsErrs_Type()
)
cCdmaRegReqInvFlagsErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRegReqInvFlagsErrs.setStatus("current")
_CCdmaRegReqInvMHAEKeyErrs_Type = ZeroBasedCounter32
_CCdmaRegReqInvMHAEKeyErrs_Object = MibScalar
cCdmaRegReqInvMHAEKeyErrs = _CCdmaRegReqInvMHAEKeyErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 1, 4),
    _CCdmaRegReqInvMHAEKeyErrs_Type()
)
cCdmaRegReqInvMHAEKeyErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRegReqInvMHAEKeyErrs.setStatus("current")
_CCdmaRegReqMismatchSPIErrs_Type = ZeroBasedCounter32
_CCdmaRegReqMismatchSPIErrs_Object = MibScalar
cCdmaRegReqMismatchSPIErrs = _CCdmaRegReqMismatchSPIErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 1, 5),
    _CCdmaRegReqMismatchSPIErrs_Type()
)
cCdmaRegReqMismatchSPIErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRegReqMismatchSPIErrs.setStatus("current")
_CCdmaRegReqInvSPIErrs_Type = ZeroBasedCounter32
_CCdmaRegReqInvSPIErrs_Object = MibScalar
cCdmaRegReqInvSPIErrs = _CCdmaRegReqInvSPIErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 1, 6),
    _CCdmaRegReqInvSPIErrs_Type()
)
cCdmaRegReqInvSPIErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRegReqInvSPIErrs.setStatus("current")
_CCdmaRegReqInvConnectionIDErrs_Type = ZeroBasedCounter32
_CCdmaRegReqInvConnectionIDErrs_Object = MibScalar
cCdmaRegReqInvConnectionIDErrs = _CCdmaRegReqInvConnectionIDErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 1, 7),
    _CCdmaRegReqInvConnectionIDErrs_Type()
)
cCdmaRegReqInvConnectionIDErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRegReqInvConnectionIDErrs.setStatus("current")
_CCdmaRegReqInvMNIDErrs_Type = ZeroBasedCounter32
_CCdmaRegReqInvMNIDErrs_Object = MibScalar
cCdmaRegReqInvMNIDErrs = _CCdmaRegReqInvMNIDErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 1, 8),
    _CCdmaRegReqInvMNIDErrs_Type()
)
cCdmaRegReqInvMNIDErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRegReqInvMNIDErrs.setStatus("current")
_CCdmaRegReqInvMNIDTypeErrs_Type = ZeroBasedCounter32
_CCdmaRegReqInvMNIDTypeErrs_Object = MibScalar
cCdmaRegReqInvMNIDTypeErrs = _CCdmaRegReqInvMNIDTypeErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 1, 9),
    _CCdmaRegReqInvMNIDTypeErrs_Type()
)
cCdmaRegReqInvMNIDTypeErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRegReqInvMNIDTypeErrs.setStatus("current")
_CCdmaRegReqInvMSIDLenErrs_Type = ZeroBasedCounter32
_CCdmaRegReqInvMSIDLenErrs_Object = MibScalar
cCdmaRegReqInvMSIDLenErrs = _CCdmaRegReqInvMSIDLenErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 1, 10),
    _CCdmaRegReqInvMSIDLenErrs_Type()
)
cCdmaRegReqInvMSIDLenErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRegReqInvMSIDLenErrs.setStatus("current")
_CCdmaRegReqMissingSSEErrs_Type = ZeroBasedCounter32
_CCdmaRegReqMissingSSEErrs_Object = MibScalar
cCdmaRegReqMissingSSEErrs = _CCdmaRegReqMissingSSEErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 1, 11),
    _CCdmaRegReqMissingSSEErrs_Type()
)
cCdmaRegReqMissingSSEErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRegReqMissingSSEErrs.setStatus("current")
_CCdmaRegReqMissingMHAEErrs_Type = ZeroBasedCounter32
_CCdmaRegReqMissingMHAEErrs_Object = MibScalar
cCdmaRegReqMissingMHAEErrs = _CCdmaRegReqMissingMHAEErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 1, 12),
    _CCdmaRegReqMissingMHAEErrs_Type()
)
cCdmaRegReqMissingMHAEErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRegReqMissingMHAEErrs.setStatus("current")
_CCdmaRegReqInvOrderErrs_Type = ZeroBasedCounter32
_CCdmaRegReqInvOrderErrs_Object = MibScalar
cCdmaRegReqInvOrderErrs = _CCdmaRegReqInvOrderErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 1, 13),
    _CCdmaRegReqInvOrderErrs_Type()
)
cCdmaRegReqInvOrderErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRegReqInvOrderErrs.setStatus("current")
_CCdmaRegReqInvVSEErrs_Type = ZeroBasedCounter32
_CCdmaRegReqInvVSEErrs_Object = MibScalar
cCdmaRegReqInvVSEErrs = _CCdmaRegReqInvVSEErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 1, 14),
    _CCdmaRegReqInvVSEErrs_Type()
)
cCdmaRegReqInvVSEErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRegReqInvVSEErrs.setStatus("current")
_CCdmaRegReqInvAppTypeInVSEErrs_Type = ZeroBasedCounter32
_CCdmaRegReqInvAppTypeInVSEErrs_Object = MibScalar
cCdmaRegReqInvAppTypeInVSEErrs = _CCdmaRegReqInvAppTypeInVSEErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 1, 15),
    _CCdmaRegReqInvAppTypeInVSEErrs_Type()
)
cCdmaRegReqInvAppTypeInVSEErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRegReqInvAppTypeInVSEErrs.setStatus("current")
_CCdmaRegReqDupAppTypeInVSEErrs_Type = ZeroBasedCounter32
_CCdmaRegReqDupAppTypeInVSEErrs_Object = MibScalar
cCdmaRegReqDupAppTypeInVSEErrs = _CCdmaRegReqDupAppTypeInVSEErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 1, 16),
    _CCdmaRegReqDupAppTypeInVSEErrs_Type()
)
cCdmaRegReqDupAppTypeInVSEErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRegReqDupAppTypeInVSEErrs.setStatus("current")
_CCdmaRegReqInvAppSubTypeInVSEErrs_Type = ZeroBasedCounter32
_CCdmaRegReqInvAppSubTypeInVSEErrs_Object = MibScalar
cCdmaRegReqInvAppSubTypeInVSEErrs = _CCdmaRegReqInvAppSubTypeInVSEErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 1, 17),
    _CCdmaRegReqInvAppSubTypeInVSEErrs_Type()
)
cCdmaRegReqInvAppSubTypeInVSEErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRegReqInvAppSubTypeInVSEErrs.setStatus("current")
_CCdmaRegReqInvVendorIDInVSEErrs_Type = ZeroBasedCounter32
_CCdmaRegReqInvVendorIDInVSEErrs_Object = MibScalar
cCdmaRegReqInvVendorIDInVSEErrs = _CCdmaRegReqInvVendorIDInVSEErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 1, 18),
    _CCdmaRegReqInvVendorIDInVSEErrs_Type()
)
cCdmaRegReqInvVendorIDInVSEErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRegReqInvVendorIDInVSEErrs.setStatus("current")
_CCdmaRegReqDupCVSEErrs_Type = ZeroBasedCounter32
_CCdmaRegReqDupCVSEErrs_Object = MibScalar
cCdmaRegReqDupCVSEErrs = _CCdmaRegReqDupCVSEErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 1, 19),
    _CCdmaRegReqDupCVSEErrs_Type()
)
cCdmaRegReqDupCVSEErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRegReqDupCVSEErrs.setStatus("current")
_CCdmaRegReqAcctUnknwnAttrErrs_Type = ZeroBasedCounter32
_CCdmaRegReqAcctUnknwnAttrErrs_Object = MibScalar
cCdmaRegReqAcctUnknwnAttrErrs = _CCdmaRegReqAcctUnknwnAttrErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 1, 20),
    _CCdmaRegReqAcctUnknwnAttrErrs_Type()
)
cCdmaRegReqAcctUnknwnAttrErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRegReqAcctUnknwnAttrErrs.setStatus("current")
_CCdmaRegReqAcctInvLenAttrErrs_Type = ZeroBasedCounter32
_CCdmaRegReqAcctInvLenAttrErrs_Object = MibScalar
cCdmaRegReqAcctInvLenAttrErrs = _CCdmaRegReqAcctInvLenAttrErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 1, 21),
    _CCdmaRegReqAcctInvLenAttrErrs_Type()
)
cCdmaRegReqAcctInvLenAttrErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRegReqAcctInvLenAttrErrs.setStatus("current")
_CCdmaRegReqAcctDupAttrErrs_Type = ZeroBasedCounter32
_CCdmaRegReqAcctDupAttrErrs_Object = MibScalar
cCdmaRegReqAcctDupAttrErrs = _CCdmaRegReqAcctDupAttrErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 1, 22),
    _CCdmaRegReqAcctDupAttrErrs_Type()
)
cCdmaRegReqAcctDupAttrErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRegReqAcctDupAttrErrs.setStatus("current")
_CCdmaRegReqAcctRecRetransErrs_Type = ZeroBasedCounter32
_CCdmaRegReqAcctRecRetransErrs_Object = MibScalar
cCdmaRegReqAcctRecRetransErrs = _CCdmaRegReqAcctRecRetransErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 1, 23),
    _CCdmaRegReqAcctRecRetransErrs_Type()
)
cCdmaRegReqAcctRecRetransErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRegReqAcctRecRetransErrs.setStatus("current")
_CCdmaRegReqAcctInvSeqNumErrs_Type = ZeroBasedCounter32
_CCdmaRegReqAcctInvSeqNumErrs_Object = MibScalar
cCdmaRegReqAcctInvSeqNumErrs = _CCdmaRegReqAcctInvSeqNumErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 1, 24),
    _CCdmaRegReqAcctInvSeqNumErrs_Type()
)
cCdmaRegReqAcctInvSeqNumErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRegReqAcctInvSeqNumErrs.setStatus("current")
_CCdmaRegReqDuplicateGREKeyErrs_Type = ZeroBasedCounter32
_CCdmaRegReqDuplicateGREKeyErrs_Object = MibScalar
cCdmaRegReqDuplicateGREKeyErrs = _CCdmaRegReqDuplicateGREKeyErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 1, 25),
    _CCdmaRegReqDuplicateGREKeyErrs_Type()
)
cCdmaRegReqDuplicateGREKeyErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRegReqDuplicateGREKeyErrs.setStatus("current")
_CCdmaRegReqSameGREKeySetupRcvdErrs_Type = ZeroBasedCounter32
_CCdmaRegReqSameGREKeySetupRcvdErrs_Object = MibScalar
cCdmaRegReqSameGREKeySetupRcvdErrs = _CCdmaRegReqSameGREKeySetupRcvdErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 1, 26),
    _CCdmaRegReqSameGREKeySetupRcvdErrs_Type()
)
cCdmaRegReqSameGREKeySetupRcvdErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRegReqSameGREKeySetupRcvdErrs.setStatus("current")
_CCdmaRegReqGREKeyChngNoSetupErrs_Type = ZeroBasedCounter32
_CCdmaRegReqGREKeyChngNoSetupErrs_Object = MibScalar
cCdmaRegReqGREKeyChngNoSetupErrs = _CCdmaRegReqGREKeyChngNoSetupErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 1, 27),
    _CCdmaRegReqGREKeyChngNoSetupErrs_Type()
)
cCdmaRegReqGREKeyChngNoSetupErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRegReqGREKeyChngNoSetupErrs.setStatus("current")
_CCdmaRegReqInitNoSetupErrs_Type = ZeroBasedCounter32
_CCdmaRegReqInitNoSetupErrs_Object = MibScalar
cCdmaRegReqInitNoSetupErrs = _CCdmaRegReqInitNoSetupErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 1, 28),
    _CCdmaRegReqInitNoSetupErrs_Type()
)
cCdmaRegReqInitNoSetupErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRegReqInitNoSetupErrs.setStatus("current")
_CCdmaRegReqStartBeforeSetupErrs_Type = ZeroBasedCounter32
_CCdmaRegReqStartBeforeSetupErrs_Object = MibScalar
cCdmaRegReqStartBeforeSetupErrs = _CCdmaRegReqStartBeforeSetupErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 1, 29),
    _CCdmaRegReqStartBeforeSetupErrs_Type()
)
cCdmaRegReqStartBeforeSetupErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRegReqStartBeforeSetupErrs.setStatus("current")
_CCdmaRegReqStartOnCloseErrs_Type = ZeroBasedCounter32
_CCdmaRegReqStartOnCloseErrs_Object = MibScalar
cCdmaRegReqStartOnCloseErrs = _CCdmaRegReqStartOnCloseErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 1, 30),
    _CCdmaRegReqStartOnCloseErrs_Type()
)
cCdmaRegReqStartOnCloseErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRegReqStartOnCloseErrs.setStatus("current")
_CCdmaRegReqStartOnActiveErrs_Type = ZeroBasedCounter32
_CCdmaRegReqStartOnActiveErrs_Object = MibScalar
cCdmaRegReqStartOnActiveErrs = _CCdmaRegReqStartOnActiveErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 1, 31),
    _CCdmaRegReqStartOnActiveErrs_Type()
)
cCdmaRegReqStartOnActiveErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRegReqStartOnActiveErrs.setStatus("current")
_CCdmaRegReqStopOnDormantErrs_Type = ZeroBasedCounter32
_CCdmaRegReqStopOnDormantErrs_Object = MibScalar
cCdmaRegReqStopOnDormantErrs = _CCdmaRegReqStopOnDormantErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 1, 32),
    _CCdmaRegReqStopOnDormantErrs_Type()
)
cCdmaRegReqStopOnDormantErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRegReqStopOnDormantErrs.setStatus("current")
_CCdmaRegReqInitRcvdStopErrs_Type = ZeroBasedCounter32
_CCdmaRegReqInitRcvdStopErrs_Object = MibScalar
cCdmaRegReqInitRcvdStopErrs = _CCdmaRegReqInitRcvdStopErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 1, 33),
    _CCdmaRegReqInitRcvdStopErrs_Type()
)
cCdmaRegReqInitRcvdStopErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRegReqInitRcvdStopErrs.setStatus("current")
_CCdmaRegReqInitRcvdSDBErrs_Type = ZeroBasedCounter32
_CCdmaRegReqInitRcvdSDBErrs_Object = MibScalar
cCdmaRegReqInitRcvdSDBErrs = _CCdmaRegReqInitRcvdSDBErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 1, 34),
    _CCdmaRegReqInitRcvdSDBErrs_Type()
)
cCdmaRegReqInitRcvdSDBErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRegReqInitRcvdSDBErrs.setStatus("current")
_CCdmaRegReqInvAirlinkRecErrs_Type = ZeroBasedCounter32
_CCdmaRegReqInvAirlinkRecErrs_Object = MibScalar
cCdmaRegReqInvAirlinkRecErrs = _CCdmaRegReqInvAirlinkRecErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 1, 35),
    _CCdmaRegReqInvAirlinkRecErrs_Type()
)
cCdmaRegReqInvAirlinkRecErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRegReqInvAirlinkRecErrs.setStatus("current")
_CCdmaRegReqDeRegNoSessionErrs_Type = ZeroBasedCounter32
_CCdmaRegReqDeRegNoSessionErrs_Object = MibScalar
cCdmaRegReqDeRegNoSessionErrs = _CCdmaRegReqDeRegNoSessionErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 1, 36),
    _CCdmaRegReqDeRegNoSessionErrs_Type()
)
cCdmaRegReqDeRegNoSessionErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRegReqDeRegNoSessionErrs.setStatus("current")
_CCdmaRegReqReRegInDisconnectErrs_Type = ZeroBasedCounter32
_CCdmaRegReqReRegInDisconnectErrs_Object = MibScalar
cCdmaRegReqReRegInDisconnectErrs = _CCdmaRegReqReRegInDisconnectErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 1, 37),
    _CCdmaRegReqReRegInDisconnectErrs_Type()
)
cCdmaRegReqReRegInDisconnectErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRegReqReRegInDisconnectErrs.setStatus("current")
_CCdmaRegReqMemFailErrs_Type = ZeroBasedCounter32
_CCdmaRegReqMemFailErrs_Object = MibScalar
cCdmaRegReqMemFailErrs = _CCdmaRegReqMemFailErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 1, 38),
    _CCdmaRegReqMemFailErrs_Type()
)
cCdmaRegReqMemFailErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRegReqMemFailErrs.setStatus("current")
_CCdmaRpRegReqMaxSessionReachedErrs_Type = ZeroBasedCounter32
_CCdmaRpRegReqMaxSessionReachedErrs_Object = MibScalar
cCdmaRpRegReqMaxSessionReachedErrs = _CCdmaRpRegReqMaxSessionReachedErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 1, 39),
    _CCdmaRpRegReqMaxSessionReachedErrs_Type()
)
cCdmaRpRegReqMaxSessionReachedErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpRegReqMaxSessionReachedErrs.setStatus("current")
_CCdmaRPRegUpdAckErrors_ObjectIdentity = ObjectIdentity
cCdmaRPRegUpdAckErrors = _CCdmaRPRegUpdAckErrors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 2)
)
_CCdmaRegUpdAckInvPakLenErrs_Type = ZeroBasedCounter32
_CCdmaRegUpdAckInvPakLenErrs_Object = MibScalar
cCdmaRegUpdAckInvPakLenErrs = _CCdmaRegUpdAckInvPakLenErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 2, 1),
    _CCdmaRegUpdAckInvPakLenErrs_Type()
)
cCdmaRegUpdAckInvPakLenErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRegUpdAckInvPakLenErrs.setStatus("current")
_CCdmaRegUpdAckInvProtocolErrs_Type = ZeroBasedCounter32
_CCdmaRegUpdAckInvProtocolErrs_Object = MibScalar
cCdmaRegUpdAckInvProtocolErrs = _CCdmaRegUpdAckInvProtocolErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 2, 2),
    _CCdmaRegUpdAckInvProtocolErrs_Type()
)
cCdmaRegUpdAckInvProtocolErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRegUpdAckInvProtocolErrs.setStatus("current")
_CCdmaRegUpdAckInvRUAEKeyErrs_Type = ZeroBasedCounter32
_CCdmaRegUpdAckInvRUAEKeyErrs_Object = MibScalar
cCdmaRegUpdAckInvRUAEKeyErrs = _CCdmaRegUpdAckInvRUAEKeyErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 2, 3),
    _CCdmaRegUpdAckInvRUAEKeyErrs_Type()
)
cCdmaRegUpdAckInvRUAEKeyErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRegUpdAckInvRUAEKeyErrs.setStatus("current")
_CCdmaRegUpdAckInvSPIErrs_Type = ZeroBasedCounter32
_CCdmaRegUpdAckInvSPIErrs_Object = MibScalar
cCdmaRegUpdAckInvSPIErrs = _CCdmaRegUpdAckInvSPIErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 2, 4),
    _CCdmaRegUpdAckInvSPIErrs_Type()
)
cCdmaRegUpdAckInvSPIErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRegUpdAckInvSPIErrs.setStatus("current")
_CCdmaRegUpdAckInvConnectionIDErrs_Type = ZeroBasedCounter32
_CCdmaRegUpdAckInvConnectionIDErrs_Object = MibScalar
cCdmaRegUpdAckInvConnectionIDErrs = _CCdmaRegUpdAckInvConnectionIDErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 2, 5),
    _CCdmaRegUpdAckInvConnectionIDErrs_Type()
)
cCdmaRegUpdAckInvConnectionIDErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRegUpdAckInvConnectionIDErrs.setStatus("current")
_CCdmaRegUpdAckInvMNIDErrs_Type = ZeroBasedCounter32
_CCdmaRegUpdAckInvMNIDErrs_Object = MibScalar
cCdmaRegUpdAckInvMNIDErrs = _CCdmaRegUpdAckInvMNIDErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 2, 6),
    _CCdmaRegUpdAckInvMNIDErrs_Type()
)
cCdmaRegUpdAckInvMNIDErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRegUpdAckInvMNIDErrs.setStatus("current")
_CCdmaRegUpdAckInvMNIDTypeErrs_Type = ZeroBasedCounter32
_CCdmaRegUpdAckInvMNIDTypeErrs_Object = MibScalar
cCdmaRegUpdAckInvMNIDTypeErrs = _CCdmaRegUpdAckInvMNIDTypeErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 2, 7),
    _CCdmaRegUpdAckInvMNIDTypeErrs_Type()
)
cCdmaRegUpdAckInvMNIDTypeErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRegUpdAckInvMNIDTypeErrs.setStatus("current")
_CCdmaRegUpdAckInvMSIDLenErrs_Type = ZeroBasedCounter32
_CCdmaRegUpdAckInvMSIDLenErrs_Object = MibScalar
cCdmaRegUpdAckInvMSIDLenErrs = _CCdmaRegUpdAckInvMSIDLenErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 2, 8),
    _CCdmaRegUpdAckInvMSIDLenErrs_Type()
)
cCdmaRegUpdAckInvMSIDLenErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRegUpdAckInvMSIDLenErrs.setStatus("current")
_CCdmaRegUpdAckMissingSSEErrs_Type = ZeroBasedCounter32
_CCdmaRegUpdAckMissingSSEErrs_Object = MibScalar
cCdmaRegUpdAckMissingSSEErrs = _CCdmaRegUpdAckMissingSSEErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 2, 9),
    _CCdmaRegUpdAckMissingSSEErrs_Type()
)
cCdmaRegUpdAckMissingSSEErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRegUpdAckMissingSSEErrs.setStatus("current")
_CCdmaRegUpdAckMissingRUAEErrs_Type = ZeroBasedCounter32
_CCdmaRegUpdAckMissingRUAEErrs_Object = MibScalar
cCdmaRegUpdAckMissingRUAEErrs = _CCdmaRegUpdAckMissingRUAEErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 2, 10),
    _CCdmaRegUpdAckMissingRUAEErrs_Type()
)
cCdmaRegUpdAckMissingRUAEErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRegUpdAckMissingRUAEErrs.setStatus("current")
_CCdmaRegUpdAckInvOrderErrs_Type = ZeroBasedCounter32
_CCdmaRegUpdAckInvOrderErrs_Object = MibScalar
cCdmaRegUpdAckInvOrderErrs = _CCdmaRegUpdAckInvOrderErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 2, 11),
    _CCdmaRegUpdAckInvOrderErrs_Type()
)
cCdmaRegUpdAckInvOrderErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRegUpdAckInvOrderErrs.setStatus("current")
_CCdmaRegUpdAckInvVSEErrs_Type = ZeroBasedCounter32
_CCdmaRegUpdAckInvVSEErrs_Object = MibScalar
cCdmaRegUpdAckInvVSEErrs = _CCdmaRegUpdAckInvVSEErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 2, 12),
    _CCdmaRegUpdAckInvVSEErrs_Type()
)
cCdmaRegUpdAckInvVSEErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRegUpdAckInvVSEErrs.setStatus("current")
_CCdmaRegUpdAckNoSessionErrs_Type = ZeroBasedCounter32
_CCdmaRegUpdAckNoSessionErrs_Object = MibScalar
cCdmaRegUpdAckNoSessionErrs = _CCdmaRegUpdAckNoSessionErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 2, 13),
    _CCdmaRegUpdAckNoSessionErrs_Type()
)
cCdmaRegUpdAckNoSessionErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRegUpdAckNoSessionErrs.setStatus("current")
_CCdmaRegUpdAckMemFailErrs_Type = ZeroBasedCounter32
_CCdmaRegUpdAckMemFailErrs_Object = MibScalar
cCdmaRegUpdAckMemFailErrs = _CCdmaRegUpdAckMemFailErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 2, 14),
    _CCdmaRegUpdAckMemFailErrs_Type()
)
cCdmaRegUpdAckMemFailErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRegUpdAckMemFailErrs.setStatus("current")
_CCdmaRPSessUpdAckErrors_ObjectIdentity = ObjectIdentity
cCdmaRPSessUpdAckErrors = _CCdmaRPSessUpdAckErrors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 3)
)
_CCdmaSessUpdAckInvPakLenErrs_Type = ZeroBasedCounter32
_CCdmaSessUpdAckInvPakLenErrs_Object = MibScalar
cCdmaSessUpdAckInvPakLenErrs = _CCdmaSessUpdAckInvPakLenErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 3, 1),
    _CCdmaSessUpdAckInvPakLenErrs_Type()
)
cCdmaSessUpdAckInvPakLenErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaSessUpdAckInvPakLenErrs.setStatus("current")
_CCdmaSessUpdAckInvProtocolErrs_Type = ZeroBasedCounter32
_CCdmaSessUpdAckInvProtocolErrs_Object = MibScalar
cCdmaSessUpdAckInvProtocolErrs = _CCdmaSessUpdAckInvProtocolErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 3, 2),
    _CCdmaSessUpdAckInvProtocolErrs_Type()
)
cCdmaSessUpdAckInvProtocolErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaSessUpdAckInvProtocolErrs.setStatus("current")
_CCdmaSessUpdAckInvRUAEKeyErrs_Type = ZeroBasedCounter32
_CCdmaSessUpdAckInvRUAEKeyErrs_Object = MibScalar
cCdmaSessUpdAckInvRUAEKeyErrs = _CCdmaSessUpdAckInvRUAEKeyErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 3, 3),
    _CCdmaSessUpdAckInvRUAEKeyErrs_Type()
)
cCdmaSessUpdAckInvRUAEKeyErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaSessUpdAckInvRUAEKeyErrs.setStatus("current")
_CCdmaSessUpdAckInvSPIErrs_Type = ZeroBasedCounter32
_CCdmaSessUpdAckInvSPIErrs_Object = MibScalar
cCdmaSessUpdAckInvSPIErrs = _CCdmaSessUpdAckInvSPIErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 3, 4),
    _CCdmaSessUpdAckInvSPIErrs_Type()
)
cCdmaSessUpdAckInvSPIErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaSessUpdAckInvSPIErrs.setStatus("current")
_CCdmaSessUpdAckInvConnectionIDErrs_Type = ZeroBasedCounter32
_CCdmaSessUpdAckInvConnectionIDErrs_Object = MibScalar
cCdmaSessUpdAckInvConnectionIDErrs = _CCdmaSessUpdAckInvConnectionIDErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 3, 5),
    _CCdmaSessUpdAckInvConnectionIDErrs_Type()
)
cCdmaSessUpdAckInvConnectionIDErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaSessUpdAckInvConnectionIDErrs.setStatus("current")
_CCdmaSessUpdAckInvMNIDErrs_Type = ZeroBasedCounter32
_CCdmaSessUpdAckInvMNIDErrs_Object = MibScalar
cCdmaSessUpdAckInvMNIDErrs = _CCdmaSessUpdAckInvMNIDErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 3, 6),
    _CCdmaSessUpdAckInvMNIDErrs_Type()
)
cCdmaSessUpdAckInvMNIDErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaSessUpdAckInvMNIDErrs.setStatus("current")
_CCdmaSessUpdAckInvMNIDTypeErrs_Type = ZeroBasedCounter32
_CCdmaSessUpdAckInvMNIDTypeErrs_Object = MibScalar
cCdmaSessUpdAckInvMNIDTypeErrs = _CCdmaSessUpdAckInvMNIDTypeErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 3, 7),
    _CCdmaSessUpdAckInvMNIDTypeErrs_Type()
)
cCdmaSessUpdAckInvMNIDTypeErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaSessUpdAckInvMNIDTypeErrs.setStatus("current")
_CCdmaSessUpdAckInvMSIDLenErrs_Type = ZeroBasedCounter32
_CCdmaSessUpdAckInvMSIDLenErrs_Object = MibScalar
cCdmaSessUpdAckInvMSIDLenErrs = _CCdmaSessUpdAckInvMSIDLenErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 3, 8),
    _CCdmaSessUpdAckInvMSIDLenErrs_Type()
)
cCdmaSessUpdAckInvMSIDLenErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaSessUpdAckInvMSIDLenErrs.setStatus("current")
_CCdmaSessUpdAckMissingSSEErrs_Type = ZeroBasedCounter32
_CCdmaSessUpdAckMissingSSEErrs_Object = MibScalar
cCdmaSessUpdAckMissingSSEErrs = _CCdmaSessUpdAckMissingSSEErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 3, 9),
    _CCdmaSessUpdAckMissingSSEErrs_Type()
)
cCdmaSessUpdAckMissingSSEErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaSessUpdAckMissingSSEErrs.setStatus("current")
_CCdmaSessUpdAckMissingRUAEErrs_Type = ZeroBasedCounter32
_CCdmaSessUpdAckMissingRUAEErrs_Object = MibScalar
cCdmaSessUpdAckMissingRUAEErrs = _CCdmaSessUpdAckMissingRUAEErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 3, 10),
    _CCdmaSessUpdAckMissingRUAEErrs_Type()
)
cCdmaSessUpdAckMissingRUAEErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaSessUpdAckMissingRUAEErrs.setStatus("current")
_CCdmaSessUpdAckInvOrderErrs_Type = ZeroBasedCounter32
_CCdmaSessUpdAckInvOrderErrs_Object = MibScalar
cCdmaSessUpdAckInvOrderErrs = _CCdmaSessUpdAckInvOrderErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 3, 11),
    _CCdmaSessUpdAckInvOrderErrs_Type()
)
cCdmaSessUpdAckInvOrderErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaSessUpdAckInvOrderErrs.setStatus("current")
_CCdmaSessUpdAckInvVSEErrs_Type = ZeroBasedCounter32
_CCdmaSessUpdAckInvVSEErrs_Object = MibScalar
cCdmaSessUpdAckInvVSEErrs = _CCdmaSessUpdAckInvVSEErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 3, 12),
    _CCdmaSessUpdAckInvVSEErrs_Type()
)
cCdmaSessUpdAckInvVSEErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaSessUpdAckInvVSEErrs.setStatus("current")
_CCdmaSessUpdAckNoSessionErrs_Type = ZeroBasedCounter32
_CCdmaSessUpdAckNoSessionErrs_Object = MibScalar
cCdmaSessUpdAckNoSessionErrs = _CCdmaSessUpdAckNoSessionErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 3, 13),
    _CCdmaSessUpdAckNoSessionErrs_Type()
)
cCdmaSessUpdAckNoSessionErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaSessUpdAckNoSessionErrs.setStatus("current")
_CCdmaSessUpdAckMemFailErrs_Type = ZeroBasedCounter32
_CCdmaSessUpdAckMemFailErrs_Object = MibScalar
cCdmaSessUpdAckMemFailErrs = _CCdmaSessUpdAckMemFailErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 3, 14),
    _CCdmaSessUpdAckMemFailErrs_Type()
)
cCdmaSessUpdAckMemFailErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaSessUpdAckMemFailErrs.setStatus("current")
_CCdmaRPRegReplyErrors_ObjectIdentity = ObjectIdentity
cCdmaRPRegReplyErrors = _CCdmaRPRegReplyErrors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 4)
)
_CCdmaRegRplyInternalErrs_Type = ZeroBasedCounter32
_CCdmaRegRplyInternalErrs_Object = MibScalar
cCdmaRegRplyInternalErrs = _CCdmaRegRplyInternalErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 4, 1),
    _CCdmaRegRplyInternalErrs_Type()
)
cCdmaRegRplyInternalErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRegRplyInternalErrs.setStatus("current")
_CCdmaRegRplyMemFailErrs_Type = ZeroBasedCounter32
_CCdmaRegRplyMemFailErrs_Object = MibScalar
cCdmaRegRplyMemFailErrs = _CCdmaRegRplyMemFailErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 4, 2),
    _CCdmaRegRplyMemFailErrs_Type()
)
cCdmaRegRplyMemFailErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRegRplyMemFailErrs.setStatus("current")
_CCdmaRpRplyPCFNoSecOrParseErrs_Type = ZeroBasedCounter32
_CCdmaRpRplyPCFNoSecOrParseErrs_Object = MibScalar
cCdmaRpRplyPCFNoSecOrParseErrs = _CCdmaRpRplyPCFNoSecOrParseErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 4, 3),
    _CCdmaRpRplyPCFNoSecOrParseErrs_Type()
)
cCdmaRpRplyPCFNoSecOrParseErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRpRplyPCFNoSecOrParseErrs.setStatus("current")
_CCdmaRPRegUpdErrors_ObjectIdentity = ObjectIdentity
cCdmaRPRegUpdErrors = _CCdmaRPRegUpdErrors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 5)
)
_CCdmaRegUpdInternalErrs_Type = ZeroBasedCounter32
_CCdmaRegUpdInternalErrs_Object = MibScalar
cCdmaRegUpdInternalErrs = _CCdmaRegUpdInternalErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 5, 1),
    _CCdmaRegUpdInternalErrs_Type()
)
cCdmaRegUpdInternalErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRegUpdInternalErrs.setStatus("current")
_CCdmaRegUpdMemFailErrs_Type = ZeroBasedCounter32
_CCdmaRegUpdMemFailErrs_Object = MibScalar
cCdmaRegUpdMemFailErrs = _CCdmaRegUpdMemFailErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 5, 2),
    _CCdmaRegUpdMemFailErrs_Type()
)
cCdmaRegUpdMemFailErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaRegUpdMemFailErrs.setStatus("current")
_CCdmaRPSessUpdErrors_ObjectIdentity = ObjectIdentity
cCdmaRPSessUpdErrors = _CCdmaRPSessUpdErrors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 6)
)
_CCdmaSessUpdInternalErrs_Type = ZeroBasedCounter32
_CCdmaSessUpdInternalErrs_Object = MibScalar
cCdmaSessUpdInternalErrs = _CCdmaSessUpdInternalErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 6, 1),
    _CCdmaSessUpdInternalErrs_Type()
)
cCdmaSessUpdInternalErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaSessUpdInternalErrs.setStatus("current")
_CCdmaSessUpdMemFailErrs_Type = ZeroBasedCounter32
_CCdmaSessUpdMemFailErrs_Object = MibScalar
cCdmaSessUpdMemFailErrs = _CCdmaSessUpdMemFailErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 1, 10, 6, 2),
    _CCdmaSessUpdMemFailErrs_Type()
)
cCdmaSessUpdMemFailErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cCdmaSessUpdMemFailErrs.setStatus("current")
_CCdmaPdsnMIBNotifPrefix_ObjectIdentity = ObjectIdentity
cCdmaPdsnMIBNotifPrefix = _CCdmaPdsnMIBNotifPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 2)
)
_CCdmaPdsnMIBNotifs_ObjectIdentity = ObjectIdentity
cCdmaPdsnMIBNotifs = _CCdmaPdsnMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 2, 0)
)
_CCdmaPdsnMIBConformance_ObjectIdentity = ObjectIdentity
cCdmaPdsnMIBConformance = _CCdmaPdsnMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 3)
)
_CCdmaPdsnMIBCompliances_ObjectIdentity = ObjectIdentity
cCdmaPdsnMIBCompliances = _CCdmaPdsnMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 3, 1)
)
_CCdmaPdsnMIBGroups_ObjectIdentity = ObjectIdentity
cCdmaPdsnMIBGroups = _CCdmaPdsnMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 3, 2)
)

# Managed Objects groups

cCdmaSystemPdsnGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 3, 2, 1)
)
cCdmaSystemPdsnGroup.setObjects(
      *(("CISCO-CDMA-PDSN-MIB", "cCdmaSessionTotal"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionMaxAllowed"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfTotal"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfMaxAllowed"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSimpleIpFlowTotal"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaMobileIpFlowTotal"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaProxyMobileIpFlowTotal"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionFailTotal"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaServingPdsnHostname"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionPdsnAuthenTimer"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionPdsnMaxFailHistory"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionMaxNotifEnabled"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfMaxAllowedNotifEnabled"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFormatErrorNotifEnabled"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSessionTotal"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSessionMaxTotal"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfErrorTotal"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionMsidType"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionConnId"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionEsn"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionPdsnIp"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionFaIp"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionA11HaIp"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionA11FaIp"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionKey"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionMoMtInd"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaActiveConnTime"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionPppCompressEnabled"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionVJCompressEnabled"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionServiceOption"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionConnStartTime"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionFlowCount"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionNai"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionHaIpAddress"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionFlowTechnology"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionAddressingScheme"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionTunnelProt"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFailSessionMsid"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFailSessionMsidType"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFailSessionEsn"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFailSessionA11HaIp"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFailSessionA11FaIp"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFailSessionConnId"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFailSessionKey"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFailHistFailTime"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFailHistFailType"))
)
if mibBuilder.loadTexts:
    cCdmaSystemPdsnGroup.setStatus("obsolete")

cCdmaSystemPdsnGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 3, 2, 3)
)
cCdmaSystemPdsnGroupRev1.setObjects(
      *(("CISCO-CDMA-PDSN-MIB", "cCdmaSessionTotal"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionMaxAllowed"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfTotal"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfMaxAllowed"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSimpleIpFlowTotal"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaMobileIpFlowTotal"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaProxyMobileIpFlowTotal"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionFailTotal"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaServingPdsnHostname"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionPdsnAuthenTimer"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionPdsnMaxFailHistory"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionMaxNotifEnabled"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfMaxAllowedNotifEnabled"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRegReqFailedNotifEnabled"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSessionTotal"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfErrorTotal"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionMsidType"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionEsn"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionPdsnIp"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionFaIp"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionA11HaIp"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionA11FaIp"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionKey"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionConnId"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionPppCompressEnabled"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionVJCompressEnabled"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionServiceOption"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionSentOctets"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionRcvdOctets"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionSentPkts"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionRcvdPkts"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionDiscardedOutPkts"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionDiscardedInPkts"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionConnStartTime"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaActiveConnTime"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionFlowCount"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionStatus"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionRegLifeTime"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionRegTimeToExpire"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionGREFromIPPkts"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionGREToIPPkts"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionNai"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionHaIpAddress"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionFlowTechnology"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionAddressingScheme"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionTunnelProt"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFailSessionMsid"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFailSessionMsidType"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFailSessionEsn"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFailSessionA11HaIp"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFailSessionA11FaIp"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFailSessionConnId"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFailSessionKey"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFailHistFailTime"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFailHistFailType"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRPRegValidRequests"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRPRegAcceptedReplies"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRPRegLifeTimeZeroRequests"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRPDeRegAcceptedReplies"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRPRegReasonUnSpecFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRPRegAdminProhibFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRPRegInsuffResFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRPRegMNAuthenFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRPRegIdentMismatchFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRPRegBadRequestFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRPRegUnknownHAAddrFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRPRegNoRevTunnelFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRPRegTBitNotSetFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRPRegBadCVSEFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRPUpdValidRequests"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRPUpdAcceptedReplies"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRPUpdAdminProhibFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRPUpdMNAuthenFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRPUpdIdentMismatchFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRPUpdReasonUnSpecFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRPUpdBadRequestFailures"))
)
if mibBuilder.loadTexts:
    cCdmaSystemPdsnGroupRev1.setStatus("obsolete")

cCdmaSystemPdsnGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 3, 2, 5)
)
cCdmaSystemPdsnGroupRev2.setObjects(
      *(("CISCO-CDMA-PDSN-MIB", "cCdmaSessionTotal"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionMaxAllowed"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfTotal"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfMaxAllowed"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSimpleIpFlowTotal"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaMobileIpFlowTotal"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaProxyMobileIpFlowTotal"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionFailTotal"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaServingPdsnHostname"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionPdsnAuthenTimer"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionPdsnMaxFailHistory"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionMaxNotifEnabled"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfMaxAllowedNotifEnabled"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRegReqFailedNotifEnabled"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSystemVersion"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSessionTotal"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSessionMaxTotal"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfErrorTotal"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFailSessionMsid"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFailSessionMsidType"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFailSessionA11HaIp"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFailSessionA11FaIp"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFailSessionConnId"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFailSessionKey"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFailHistFailTime"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFailHistFailType"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpRegReceivedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpRegAcceptedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpRegDeniedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpRegDiscardedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpInitRegAcceptedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpInitRegDeniedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpReRegAcceptedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpReRegDeniedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpDeRegAcceptedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpDeRegDeniedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpRegReasonlUnSpecFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpRegAdminProhibFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpRegInsuffResFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpRegMNAuthFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpRegIdMismatchFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpRegBadReqFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpRegUnknownPdsnFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpRegNoRevTunnelFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpRegTBitNotSetFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpRegBadCVSEFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdTransmittedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdAcceptedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdDeniedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdNotAckedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdInitTransmittedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdReTransmittedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdReceivedAcks"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdDiscardedAcks"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdRpLifeExpReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdPPPtermReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdOtherReasonReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdReasonUnSpecFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdAdminProhibFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdMNAuthenFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdIdentMismatchFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdBadReqFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppCurrentConnections"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppConnectionInitiateReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppConnectionSuccesses"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppConnectionFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppLcpFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAuthFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppIpcpFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppEnterLcpNums"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppEnterAuthNums"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppEnterIpcpNums"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppRenegTotalReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppRenegByPdsnReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppRenegByMobileReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppRenegLcpIpcpReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppRenegAddrMismatchReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppRenegOtherReasonReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAuthChapAttempts"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAuthChapSuccesses"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAuthChapFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAuthPapAttempts"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAuthPapSuccesses"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAuthPapFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAuthMschapAttempts"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAuthMschapSuccesses"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAuthMschapFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAuthEapAttempts"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAuthEapSuccesses"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAuthEapFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppTotalReleases"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppPdsnReleases"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppMobileReleases"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAddrFilterReleases"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAdminReleases"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppLcpTermReleases"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppIdleTimeoutReleases"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppL2tpTunnelReleases"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppInsufResReleases"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppSessTimeoutReleases"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppSrvIntReleases"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppSrvUnavailReleases"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppOtherReasonReleases"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppCompressNegoCons"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppCompressMsftCons"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppCompressAscendCons"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppCompressStackCons"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppCompressDeflateCons"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppCompressOtherCons"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppNegoMrruCons"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppNegoIpxCons"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppNegoIpCons"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppNegoVjCompCons"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppNegoBapCons"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppConFormedBundles"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaTransmittedSipKiloOctets"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaReceivedSipKiloOctets"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaTransmittedSipPkts"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaReceivedSipPkts"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaTransmittedMipKiloOctets"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaReceivedMipKiloOctets"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaTransmittedMipPkts"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaReceivedMipPkts"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaTransmittedPmipKiloOctets"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaReceivedPmipKiloOctets"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaTransmittedPmipPkts"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaReceivedPmipPkts"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFlowSimpleIpSuccesses"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFlowMobilIpSuccesses"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFlowProxyIpSuccesses"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFlowVpdnSuccesses"))
)
if mibBuilder.loadTexts:
    cCdmaSystemPdsnGroupRev2.setStatus("obsolete")

cCdmaSystemPdsnGroupRev3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 3, 2, 6)
)
cCdmaSystemPdsnGroupRev3.setObjects(
      *(("CISCO-CDMA-PDSN-MIB", "cCdmaSessionTotal"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionMaxAllowed"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfTotal"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfMaxAllowed"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSimpleIpFlowTotal"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaMobileIpFlowTotal"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaProxyMobileIpFlowTotal"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionFailTotal"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaServingPdsnHostname"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionPdsnAuthenTimer"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionPdsnMaxFailHistory"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionMaxNotifEnabled"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfMaxAllowedNotifEnabled"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRegReqFailedNotifEnabled"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSystemVersion"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSystemStatus"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSessionTotal"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSessionMaxTotal"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfErrorTotal"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFailSessionMsid"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFailSessionMsidType"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFailSessionEsn"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFailSessionA11HaIp"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFailSessionA11FaIp"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFailSessionConnId"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFailSessionKey"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFailHistFailTime"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFailHistFailType"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpRegReceivedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpRegAcceptedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpRegDeniedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpRegDiscardedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpInitRegAcceptedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpInitRegDeniedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpReRegAcceptedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpReRegDeniedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpDeRegAcceptedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpDeRegDeniedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpRegReasonlUnSpecFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpRegAdminProhibFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpRegInsuffResFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpRegMNAuthFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpRegIdMismatchFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpRegBadReqFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpRegUnknownPdsnFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpRegNoRevTunnelFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpRegTBitNotSetFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpRegBadCVSEFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdTransmittedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdAcceptedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdDeniedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdNotAckedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdInitTransmittedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdReTransmittedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdReceivedAcks"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdDiscardedAcks"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdRpLifeExpReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdPPPtermReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdOtherReasonReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdReasonUnSpecFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdAdminProhibFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdMNAuthenFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdIdentMismatchFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdBadReqFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppCurrentConnections"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppConnectionInitiateReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppConnectionSuccesses"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppConnectionFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppLcpFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAuthFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppIpcpFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppEnterLcpNums"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppEnterAuthNums"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppEnterIpcpNums"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppRenegTotalReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppRenegByPdsnReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppRenegByMobileReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppRenegLcpIpcpReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppRenegAddrMismatchReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppRenegOtherReasonReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAuthChapAttempts"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAuthChapSuccesses"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAuthChapFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAuthPapAttempts"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAuthPapSuccesses"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAuthPapFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAuthMschapAttempts"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAuthMschapSuccesses"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAuthMschapFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAuthEapAttempts"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAuthEapSuccesses"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAuthEapFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAuthMsidAttempts"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAuthMsidSuccesses"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAuthMsidFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppTotalReleases"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppPdsnReleases"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppMobileReleases"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAddrFilterReleases"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAdminReleases"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppLcpTermReleases"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppIdleTimeoutReleases"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppL2tpTunnelReleases"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppInsufResReleases"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppSessTimeoutReleases"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppSrvIntReleases"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppSrvUnavailReleases"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppOtherReasonReleases"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppCompressNegoCons"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppCompressMsftCons"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppCompressAscendCons"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppCompressStackCons"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppCompressDeflateCons"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppCompressOtherCons"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppNegoMrruCons"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppNegoIpxCons"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppNegoIpCons"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppNegoVjCompCons"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppNegoBapCons"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppConFormedBundles"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaTransmittedSipKiloOctets"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaReceivedSipKiloOctets"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaTransmittedSipPkts"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaReceivedSipPkts"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaTransmittedMipKiloOctets"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaReceivedMipKiloOctets"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaTransmittedMipPkts"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaReceivedMipPkts"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaTransmittedPmipKiloOctets"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaReceivedPmipKiloOctets"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaTransmittedPmipPkts"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaReceivedPmipPkts"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFlowSimpleIpSuccesses"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFlowMobilIpSuccesses"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFlowProxyIpSuccesses"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFlowVpdnSuccesses"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFlowSimpleIpFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFlowMobileIpFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFlowProxyIpFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFlowVpdnFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFlowUnknownTypeFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaServiceTotalOptions"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaServiceOptionSucesses"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaServiceOptionFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaInterPcfHandoffs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaInterPdsnHandoffs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaIdChangeHandoffs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaStatusIS2OOSes"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaStatusOOS2ISes"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaAddressStaticSIPs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaAddressDynamicSIPs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaAddressStaticMIPs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaAddressDynamicMIPs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaAddressStaticPMIPs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaAddressDynamicPMIPs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaAddressStaticVPDNs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaAddressDynamicVPDNs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionHighThreshold"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionLowThreshold"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaClusterType"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaClusterRole"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaClusterTotalControllers"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaClusterCtrlStatus"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaClusterSessHighThreshold"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaClusterSessLowThreshold"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaClusterTotalSessions"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaClusterTotalMembers"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaClusterMemberStatus"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaClusterMemberLoad"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaNotifSeverityLevel"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaServiceAffectedLevel"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaAffectedAddress"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaAffectedAddressType"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaAffectedMemberStatus"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaAffectedCtrlStatus"))
)
if mibBuilder.loadTexts:
    cCdmaSystemPdsnGroupRev3.setStatus("deprecated")

cCdmaSystemPdsnGroupRev4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 3, 2, 8)
)
cCdmaSystemPdsnGroupRev4.setObjects(
      *(("CISCO-CDMA-PDSN-MIB", "cCdmaSessionTotal"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionMaxAllowed"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfTotal"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfMaxAllowed"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSimpleIpFlowTotal"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaMobileIpFlowTotal"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaProxyMobileIpFlowTotal"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionFailTotal"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaServingPdsnHostname"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionPdsnAuthenTimer"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionPdsnMaxFailHistory"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionMaxNotifEnabled"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfMaxAllowedNotifEnabled"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRegReqFailedNotifEnabled"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSystemVersion"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSystemStatus"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSessionTotal"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSessionMaxTotal"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfErrorTotal"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFailSessionMsid"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFailSessionMsidType"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFailSessionEsn"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFailSessionA11HaIp"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFailSessionA11FaIp"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFailSessionConnId"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFailSessionKey"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFailHistFailTime"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFailHistFailType"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFailHistServiceOption"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFailHistPanId"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFailHistCanId"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFailHistBsid"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpRegReceivedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpRegAcceptedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpRegDeniedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpRegDiscardedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpInitRegAcceptedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpInitRegDeniedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpReRegAcceptedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpReRegDeniedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpDeRegAcceptedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpDeRegDeniedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpRegReasonlUnSpecFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpRegAdminProhibFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpRegInsuffResFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpRegMNAuthFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpRegIdMismatchFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpRegBadReqFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpRegUnknownPdsnFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpRegNoRevTunnelFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpRegTBitNotSetFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpRegBadCVSEFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdTransmittedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdAcceptedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdDeniedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdNotAckedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdInitTransmittedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdReTransmittedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdReceivedAcks"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdDiscardedAcks"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdRpLifeExpReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdPPPtermReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdOtherReasonReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdReasonUnSpecFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdAdminProhibFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdMNAuthenFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdIdentMismatchFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdBadReqFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppCurrentConnections"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppConnectionInitiateReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppConnectionSuccesses"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppConnectionFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppLcpFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAuthFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppIpcpFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppEnterLcpNums"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppEnterAuthNums"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppEnterIpcpNums"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppLcpFailuresMaxRetrans"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppLcpFailuresUnknown"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppIpcpFailuresMaxRetrans"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppIpcpFailuresUnknown"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppConnectionsAborted"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppRenegTotalReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppRenegByPdsnReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppRenegByMobileReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppRenegLcpIpcpReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppRenegAddrMismatchReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppRenegOtherReasonReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppRenegSuccesses"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppRenegFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppRenegConnectionsAborted"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAuthChapAttempts"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAuthChapSuccesses"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAuthChapFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAuthPapAttempts"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAuthPapSuccesses"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAuthPapFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAuthMschapAttempts"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAuthMschapSuccesses"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAuthMschapFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAuthEapAttempts"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAuthEapSuccesses"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAuthEapFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAuthMsidAttempts"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAuthMsidSuccesses"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAuthMsidFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppTotalReleases"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppPdsnReleases"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppMobileReleases"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAddrFilterReleases"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAdminReleases"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppLcpTermReleases"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppIdleTimeoutReleases"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppL2tpTunnelReleases"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppInsufResReleases"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppSessTimeoutReleases"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppSrvIntReleases"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppSrvUnavailReleases"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppOtherReasonReleases"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppCompressNegoCons"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppCompressMsftCons"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppCompressAscendCons"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppCompressStackCons"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppCompressDeflateCons"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppCompressOtherCons"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppNegoMrruCons"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppNegoIpxCons"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppNegoIpCons"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppNegoVjCompCons"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppNegoBapCons"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppConFormedBundles"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaTransmittedSipKiloOctets"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaReceivedSipKiloOctets"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaTransmittedSipPkts"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaReceivedSipPkts"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaTransmittedMipKiloOctets"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaReceivedMipKiloOctets"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaTransmittedMipPkts"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaReceivedMipPkts"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaTransmittedPmipKiloOctets"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaReceivedPmipKiloOctets"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaTransmittedPmipPkts"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaReceivedPmipPkts"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFlowSimpleIpSuccesses"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFlowMobilIpSuccesses"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFlowProxyIpSuccesses"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFlowVpdnSuccesses"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFlowSimpleIpFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFlowMobileIpFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFlowProxyIpFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFlowVpdnFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFlowUnknownTypeFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaServiceTotalOptions"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaServiceOptionSucesses"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaServiceOptionFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaInterPcfHandoffs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaInterPdsnHandoffs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaIdChangeHandoffs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaStatusIS2OOSes"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaStatusOOS2ISes"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaAddressStaticSIPs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaAddressDynamicSIPs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaAddressStaticMIPs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaAddressDynamicMIPs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaAddressStaticPMIPs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaAddressDynamicPMIPs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaAddressStaticVPDNs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaAddressDynamicVPDNs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionHighThreshold"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionLowThreshold"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaClusterType"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaClusterRole"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaClusterTotalControllers"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaClusterCtrlStatus"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaClusterSessHighThreshold"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaClusterSessLowThreshold"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaClusterTotalSessions"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaClusterTotalMembers"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaClusterMemberStatus"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaClusterMemberLoad"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaNotifSeverityLevel"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaServiceAffectedLevel"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaAffectedAddress"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaAffectedAddressType"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaAffectedMemberStatus"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaAffectedCtrlStatus"))
)
if mibBuilder.loadTexts:
    cCdmaSystemPdsnGroupRev4.setStatus("deprecated")

cCdmaPdsnPcfSoRpRegGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 3, 2, 9)
)
cCdmaPdsnPcfSoRpRegGroup.setObjects(
      *(("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoRpRegRcvdReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoRpRegAcptdReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoRpRegDeniedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoRpRegDiscardedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoRpInitRegAcptdReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoRpInitRegDeniedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoRpReRegAcptdReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoRpReRegDeniedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoRpDeRegAcptdReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoRpDeRegDeniedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoRpRegPcfUnknwnFails"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoRpRegAdmnFails"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoRpRegNoRsrcFails"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoRpRegMNAuthFails"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoRpRegIdMismatFails"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoRpRegBadReqFails"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoRpRegUnkPdsnFails"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoRpRegNoRevTunFails"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoRpRegTBitNSetFails"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoRpRegBadCVSEFails"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoRpUpdTxdReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoRpUpdAcptdReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoRpUpdDeniedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoRpUpdNotAckedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoRpUpdInitTxdReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoRpUpdReTxdReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoRpUpdRcvdAcks"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoRpUpdDiscardedAcks"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoRpUpdRpLifeExpReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoRpUpdPPPtermReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoRpUpdOtherReaReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoRpUpdReaUnSpecFails"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoRpUpdAdmnFails"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoRpUpdMNAuthFails"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoRpUpdIdMismatFails"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoRpUpdBadReqFails"))
)
if mibBuilder.loadTexts:
    cCdmaPdsnPcfSoRpRegGroup.setStatus("current")

cCdmaPdsnPcfSoPppGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 3, 2, 10)
)
cCdmaPdsnPcfSoPppGroup.setObjects(
      *(("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoPppCurrentConns"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoPppConnInitiateReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoPppConnSuccesses"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoPppConnFails"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoPppConnAborts"))
)
if mibBuilder.loadTexts:
    cCdmaPdsnPcfSoPppGroup.setStatus("current")

cCdmaSystemPdsnGroupRev5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 3, 2, 12)
)
cCdmaSystemPdsnGroupRev5.setObjects(
      *(("CISCO-CDMA-PDSN-MIB", "cCdmaSessionTotal"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionMaxAllowed"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfTotal"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfMaxAllowed"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSimpleIpFlowTotal"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaMobileIpFlowTotal"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaProxyMobileIpFlowTotal"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionFailTotal"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaServingPdsnHostname"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionPdsnAuthenTimer"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionPdsnMaxFailHistory"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionMaxNotifEnabled"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfMaxAllowedNotifEnabled"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRegReqFailedNotifEnabled"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSystemVersion"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSystemStatus"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSrEnabled"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaActiveSessions"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaDormantSessions"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSessionTotal"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSessionMaxTotal"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfErrorTotal"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFailSessionMsid"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFailSessionMsidType"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFailSessionA11HaIp"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFailSessionA11FaIp"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFailSessionConnId"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFailSessionKey"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFailHistFailTime"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFailHistFailType"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFailHistServiceOption"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFailHistPanId"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFailHistCanId"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFailHistBsid"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFailSessionEsn2"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpRegReceivedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpRegAcceptedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpRegDeniedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpRegDiscardedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpInitRegAcceptedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpInitRegDeniedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpReRegAcceptedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpReRegDeniedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpDeRegAcceptedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpDeRegDeniedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpRegReasonUnSpecFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpRegAdminProhibFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpRegInsuffResFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpRegMNAuthFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpRegIdMismatchFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpRegBadReqFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpRegUnknownPdsnFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpRegNoRevTunnelFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpRegTBitNotSetFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpRegBadCVSEFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdTransmittedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdAcceptedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdDeniedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdNotAckedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdInitTransmittedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdReTransmittedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdReceivedAcks"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdDiscardedAcks"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdRpLifeExpReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdPPPtermReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdOtherReasonReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdReasonUnSpecFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdAdminProhibFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdMNAuthenFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdIdentMismatchFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdBadReqFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppCurrentConnections"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppConnectionInitiateReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppConnectionSuccesses"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppConnectionFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppLcpFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAuthFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppIpcpFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppEnterLcpNums"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppEnterAuthNums"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppEnterIpcpNums"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppLcpFailuresMaxRetrans"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppLcpFailuresUnknown"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppIpcpFailuresMaxRetrans"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppIpcpFailuresUnknown"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppConnectionsAborted"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppRenegTotalReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppRenegByPdsnReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppRenegByMobileReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppRenegLcpIpcpReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppRenegAddrMismatchReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppRenegOtherReasonReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppRenegSuccesses"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppRenegFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppRenegConnectionsAborted"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAuthChapAttempts"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAuthChapSuccesses"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAuthChapFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAuthPapAttempts"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAuthPapSuccesses"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAuthPapFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAuthMschapAttempts"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAuthMschapSuccesses"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAuthMschapFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAuthEapAttempts"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAuthEapSuccesses"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAuthEapFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAuthMsidAttempts"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAuthMsidSuccesses"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAuthMsidFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAuthAAATimeouts"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppTotalReleases"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppPdsnReleases"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppMobileReleases"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAddrFilterReleases"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAdminReleases"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppIdleTimeoutReleases"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppL2tpTunnelReleases"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppSessTimeoutReleases"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppSrvIntReleases"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppSrvUnavailReleases"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppOtherReasonReleases"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppMissEchoReleases"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppCompressNegoCons"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppCompressMsftCons"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppCompressAscendCons"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppCompressStackCons"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppCompressDeflateCons"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppCompressOtherCons"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppNegoMrruCons"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppNegoIpxCons"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppNegoIpCons"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppNegoVjCompCons"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppNegoBapCons"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppConFormedBundles"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaTransmittedSipKiloOctets"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaReceivedSipKiloOctets"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaTransmittedSipPkts"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaReceivedSipPkts"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaTransmittedMipKiloOctets"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaReceivedMipKiloOctets"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaTransmittedMipPkts"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaReceivedMipPkts"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaTransmittedPmipKiloOctets"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaReceivedPmipKiloOctets"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaTransmittedPmipPkts"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaReceivedPmipPkts"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFlowSimpleIpSuccesses"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFlowMobilIpSuccesses"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFlowProxyIpSuccesses"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFlowVpdnSuccesses"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFlowSimpleIpFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFlowMobileIpFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFlowProxyIpFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFlowVpdnFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFlowUnknownTypeFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaServiceTotalOptions"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaServiceOptionSucesses"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaServiceOptionFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaInterPcfHandoffs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaInterPdsnHandoffs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaIdChangeHandoffs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdPcfHandoffs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdHandoffNotAckedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdHandoffInitTxdReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdHandoffReTxdReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdHandoffReceivedAcks"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdHandoffDiscardedAcks"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdHandoffReaUnSpecFails"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdHandoffAdmProhibFails"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdHandoffMNAuthenFails"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdHandoffIdMismatchFails"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdHandoffBadReqFails"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdHandoffAcceptedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpUpdHandoffDeniedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpDeRegHandoffAcceptedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpDeRegHandoffDeniedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaStatusIS2OOSes"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaStatusOOS2ISes"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaAddressStaticSIPs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaAddressDynamicSIPs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaAddressStaticMIPs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaAddressDynamicMIPs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaAddressStaticPMIPs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaAddressDynamicPMIPs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaAddressStaticVPDNs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaAddressDynamicVPDNs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionHighThreshold"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionLowThreshold"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaClusterType"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaClusterRole"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaClusterTotalControllers"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaClusterCtrlStatus"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaClusterSessHighThreshold"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaClusterSessLowThreshold"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaClusterTotalSessions"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaClusterTotalMembers"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaClusterMemberStatus"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaClusterMemberLoad"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaNotifSeverityLevel"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaServiceAffectedLevel"))
)
if mibBuilder.loadTexts:
    cCdmaSystemPdsnGroupRev5.setStatus("current")

cCdmaSystemPdsnGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 3, 2, 13)
)
cCdmaSystemPdsnGroupSup1.setObjects(
      *(("CISCO-CDMA-PDSN-MIB", "cCdmaPPPoGRESessionTotal"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaHDLCoGRESessionTotal"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaEstablishedSessions"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaReleasedSessions"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaMSIDFlowTotal"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaVPDNFlowTotal"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpInitRegReceivedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpInitRegDiscardedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpReRegReceivedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpReRegDiscardedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpReRegAirlinkStarts"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpReRegAirlinkStops"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpDeRegReceivedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpDeRegDiscardedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpDeRegAirlinkStops"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpHandoffRegReceivedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpHandoffRegAcceptedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpHandoffRegDeniedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpHandoffRegDiscardedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpSessUpdTransmittedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpSessUpdAcceptedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpSessUpdDeniedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpSessUpdNotAckedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpSessUpdInitTransmittedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpSessUpdReTransmittedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpSessUpdReceivedAcks"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpSessUpdDiscardedAcks"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpSessUpdAlwaysON"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpSessUpdRNPDIT"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpSessUpdReasonParamNotUpdated"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpSessUpdReasonUnSpecFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpSessUpdMNAuthenFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpSessUpdIdentMismatchFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpSessUpdBadReqFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppLcpOptionIssueFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppIpcpOptionIssueFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAuthMaxRetransFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppNoRemoteIpAddressReleases"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppLowerLayerReleaseFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppIpcpPhaseReceivedTermreqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppIpcpPhaseSentTermreqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAuthPhaseReceivedTermreqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAuthPhaseSentTermreqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppLcpPhaseReceivedTermreqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppLcpPhaseSentTermreqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppPreLCPPdsnA10Releases"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppPreLCPPcfA10Releases"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppLCPPdsnA10Releases"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppLCPPcfA10Releases"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAuthPdsnA10Releases"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAuthPcfA10Releases"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppIPCPPdsnA10Releases"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppIPCPPcfA10Releases"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppLcpSuccesses"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppIpcpSuccesses"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAuthSuccesses"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppConnectionOtherFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppRenegAnidChanges"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAuthChapTimeouts"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAuthPapTimeouts"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAuthMschapTimeouts"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppAuthSkips"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppDeregisterByPcfReleases"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppLifetimeExpiryReleases"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppCompressNegoFailures"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppTransmittedEchoReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppRetransmittedEchoReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppReceivedEchoReplies"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppEchoRequestTimeouts"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppUnknownProtocolPktDiscards"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPppBadLengthPktDiscards"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaTransmittedSDBPkts"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaTransmittedSDBOctets"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaNoGREKeyPktDiscards"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaNoSessionPktDiscards"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaInvGREProtoPktDiscards"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaInvCheckSumPktDiscards"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpInterPCFActiveHandoffs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpInterPCFDormantHandoffs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRegReqInvPakLenErrs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRegReqInvProtocolErrs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRegReqInvFlagsErrs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRegReqInvMHAEKeyErrs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRegReqMismatchSPIErrs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRegReqInvSPIErrs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRegReqInvConnectionIDErrs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRegReqInvMNIDErrs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRegReqInvMNIDTypeErrs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRegReqInvMSIDLenErrs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRegReqMissingSSEErrs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRegReqMissingMHAEErrs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRegReqInvOrderErrs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRegReqInvVSEErrs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRegReqInvAppTypeInVSEErrs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRegReqDupAppTypeInVSEErrs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRegReqInvAppSubTypeInVSEErrs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRegReqInvVendorIDInVSEErrs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRegReqDupCVSEErrs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRegReqAcctUnknwnAttrErrs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRegReqAcctInvLenAttrErrs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRegReqAcctDupAttrErrs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRegReqAcctRecRetransErrs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRegReqAcctInvSeqNumErrs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRegReqDuplicateGREKeyErrs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRegReqSameGREKeySetupRcvdErrs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRegReqGREKeyChngNoSetupErrs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRegReqInitNoSetupErrs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRegReqStartBeforeSetupErrs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRegReqStartOnCloseErrs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRegReqStartOnActiveErrs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRegReqStopOnDormantErrs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRegReqInitRcvdStopErrs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRegReqInitRcvdSDBErrs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRegReqInvAirlinkRecErrs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRegReqDeRegNoSessionErrs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRegReqReRegInDisconnectErrs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRegReqMemFailErrs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpRegReqMaxSessionReachedErrs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRegUpdAckInvPakLenErrs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRegUpdAckInvProtocolErrs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRegUpdAckInvRUAEKeyErrs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRegUpdAckInvSPIErrs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRegUpdAckInvConnectionIDErrs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRegUpdAckInvMNIDErrs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRegUpdAckInvMNIDTypeErrs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRegUpdAckInvMSIDLenErrs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRegUpdAckMissingSSEErrs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRegUpdAckMissingRUAEErrs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRegUpdAckInvOrderErrs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRegUpdAckInvVSEErrs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRegUpdAckNoSessionErrs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRegUpdAckMemFailErrs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessUpdAckInvPakLenErrs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessUpdAckInvProtocolErrs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessUpdAckInvRUAEKeyErrs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessUpdAckInvSPIErrs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessUpdAckInvConnectionIDErrs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessUpdAckInvMNIDErrs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessUpdAckInvMNIDTypeErrs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessUpdAckInvMSIDLenErrs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessUpdAckMissingSSEErrs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessUpdAckMissingRUAEErrs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessUpdAckInvOrderErrs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessUpdAckInvVSEErrs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessUpdAckNoSessionErrs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessUpdAckMemFailErrs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRegRplyInternalErrs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRegRplyMemFailErrs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRpRplyPCFNoSecOrParseErrs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRegUpdInternalErrs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaRegUpdMemFailErrs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessUpdInternalErrs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessUpdMemFailErrs"))
)
if mibBuilder.loadTexts:
    cCdmaSystemPdsnGroupSup1.setStatus("current")

cCdmaPdsnPcfSoRpRegGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 3, 2, 14)
)
cCdmaPdsnPcfSoRpRegGroupSup1.setObjects(
      *(("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoRpInitRegRcvdReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoRpInitRegDiscardedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoRpReRegRcvdReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoRpReRegDiscardedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoRpDeRegRcvdReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoRpDeRegDiscardedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoRpHandoffRegRcvdReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoRpHandoffRegAcptdReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoRpHandoffRegDeniedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoRpHandoffRegDiscardedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoRpReRegAirlinkStarts"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoRpReRegAirlinkStops"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoRpDeRegAirlinkStops"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSoRpUpdPcfHandoffs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSoRpUpdHandoffNotAckedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSoRpUpdHandoffReceivedAcks"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSoRpUpdHandoffAcceptedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSoRpUpdHandoffDeniedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSoRpUpdHandoffDiscardedAcks"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSoRpUpdHandoffInitTxdReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSoRpUpdHandoffReTxdReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSoRpUpdHandoffReaUnSpecFails"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSoRpUpdHandoffAdmProhibFails"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSoRpUpdHandoffMNAuthenFails"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSoRpUpdHandoffIdMismatchFails"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSoRpUpdHandoffBadReqFails"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoRpSessUpdTxdReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoRpSessUpdAcptdReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoRpSessUpdDeniedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoRpSessUpdNotAckedReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoRpSessUpdInitTxdReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoRpSessUpdReTxdReqs"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoRpSessUpdRcvdAcks"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoRpSessUpdDiscardedAcks"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoRpSessUpdAlwaysOn"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoRpSessUpdRNPDIT"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoRpSessUpdParamNotUpdated"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoRpSessUpdReaUnSpecFails"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoRpSessUpdMNAuthFails"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoRpSessUpdIdMismatFails"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfSoRpSessUpdBadReqFails"))
)
if mibBuilder.loadTexts:
    cCdmaPdsnPcfSoRpRegGroupSup1.setStatus("current")


# Notification objects

cCdmaSessionMaxAllowedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 2, 0, 1)
)
cCdmaSessionMaxAllowedNotif.setObjects(
    ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionMaxAllowed")
)
if mibBuilder.loadTexts:
    cCdmaSessionMaxAllowedNotif.setStatus(
        "current"
    )

cCdmaPcfMaxAllowedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 2, 0, 2)
)
cCdmaPcfMaxAllowedNotif.setObjects(
    ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfMaxAllowed")
)
if mibBuilder.loadTexts:
    cCdmaPcfMaxAllowedNotif.setStatus(
        "current"
    )

cCdmaSessionFormatErrorNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 2, 0, 3)
)
cCdmaSessionFormatErrorNotif.setObjects(
      *(("CISCO-CDMA-PDSN-MIB", "cCdmaFailSessionMsid"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFailSessionA11HaIp"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFailSessionA11FaIp"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFailSessionConnId"))
)
if mibBuilder.loadTexts:
    cCdmaSessionFormatErrorNotif.setStatus(
        "obsolete"
    )

cCdmaSessionRegReqFailedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 2, 0, 4)
)
cCdmaSessionRegReqFailedNotif.setObjects(
      *(("CISCO-CDMA-PDSN-MIB", "cCdmaFailSessionMsid"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFailSessionA11HaIp"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFailSessionA11FaIp"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFailSessionConnId"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaFailHistFailType"))
)
if mibBuilder.loadTexts:
    cCdmaSessionRegReqFailedNotif.setStatus(
        "current"
    )

cCdmaPdsnStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 2, 0, 5)
)
cCdmaPdsnStatusChange.setObjects(
      *(("CISCO-CDMA-PDSN-MIB", "cCdmaServiceAffectedLevel"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSystemStatus"))
)
if mibBuilder.loadTexts:
    cCdmaPdsnStatusChange.setStatus(
        "current"
    )

cCdmaSessionHighReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 2, 0, 6)
)
cCdmaSessionHighReached.setObjects(
      *(("CISCO-CDMA-PDSN-MIB", "cCdmaServiceAffectedLevel"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionHighThreshold"))
)
if mibBuilder.loadTexts:
    cCdmaSessionHighReached.setStatus(
        "current"
    )

cCdmaSessionLowReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 2, 0, 7)
)
cCdmaSessionLowReached.setObjects(
      *(("CISCO-CDMA-PDSN-MIB", "cCdmaServiceAffectedLevel"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionHighThreshold"))
)
if mibBuilder.loadTexts:
    cCdmaSessionLowReached.setStatus(
        "deprecated"
    )

cCdmaClusterSessionHighReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 2, 0, 8)
)
cCdmaClusterSessionHighReached.setObjects(
      *(("CISCO-CDMA-PDSN-MIB", "cCdmaServiceAffectedLevel"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaClusterSessHighThreshold"))
)
if mibBuilder.loadTexts:
    cCdmaClusterSessionHighReached.setStatus(
        "current"
    )

cCdmaClusterSessionLowReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 2, 0, 9)
)
cCdmaClusterSessionLowReached.setObjects(
      *(("CISCO-CDMA-PDSN-MIB", "cCdmaServiceAffectedLevel"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaClusterSessLowThreshold"))
)
if mibBuilder.loadTexts:
    cCdmaClusterSessionLowReached.setStatus(
        "current"
    )

cCdmaClusterMemberStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 2, 0, 10)
)
cCdmaClusterMemberStatusChange.setObjects(
      *(("CISCO-CDMA-PDSN-MIB", "cCdmaServiceAffectedLevel"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaAffectedAddressType"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaAffectedAddress"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaAffectedMemberStatus"))
)
if mibBuilder.loadTexts:
    cCdmaClusterMemberStatusChange.setStatus(
        "deprecated"
    )

cCdmaClusterCtrlStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 2, 0, 11)
)
cCdmaClusterCtrlStatusChange.setObjects(
      *(("CISCO-CDMA-PDSN-MIB", "cCdmaServiceAffectedLevel"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaAffectedAddressType"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaAffectedAddress"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaAffectedCtrlStatus"))
)
if mibBuilder.loadTexts:
    cCdmaClusterCtrlStatusChange.setStatus(
        "deprecated"
    )

cCdmaClusterMemberStatusChange2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 2, 0, 12)
)
cCdmaClusterMemberStatusChange2.setObjects(
    ("CISCO-CDMA-PDSN-MIB", "cCdmaClusterMemberStatus")
)
if mibBuilder.loadTexts:
    cCdmaClusterMemberStatusChange2.setStatus(
        "current"
    )

cCdmaClusterCtrlStatusChange2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 2, 0, 13)
)
cCdmaClusterCtrlStatusChange2.setObjects(
    ("CISCO-CDMA-PDSN-MIB", "cCdmaClusterCtrlStatus")
)
if mibBuilder.loadTexts:
    cCdmaClusterCtrlStatusChange2.setStatus(
        "current"
    )

cCdmaSessionLowReached2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 2, 0, 14)
)
cCdmaSessionLowReached2.setObjects(
      *(("CISCO-CDMA-PDSN-MIB", "cCdmaServiceAffectedLevel"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionLowThreshold"))
)
if mibBuilder.loadTexts:
    cCdmaSessionLowReached2.setStatus(
        "current"
    )


# Notifications groups

cCdmaNotifPdsnGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 3, 2, 2)
)
cCdmaNotifPdsnGroup.setObjects(
      *(("CISCO-CDMA-PDSN-MIB", "cCdmaSessionMaxAllowedNotif"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfMaxAllowedNotif"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionFormatErrorNotif"))
)
if mibBuilder.loadTexts:
    cCdmaNotifPdsnGroup.setStatus(
        "obsolete"
    )

cCdmaNotifPdsnGroupRev1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 3, 2, 4)
)
cCdmaNotifPdsnGroupRev1.setObjects(
      *(("CISCO-CDMA-PDSN-MIB", "cCdmaSessionMaxAllowedNotif"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfMaxAllowedNotif"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionRegReqFailedNotif"))
)
if mibBuilder.loadTexts:
    cCdmaNotifPdsnGroupRev1.setStatus(
        "deprecated"
    )

cCdmaNotifPdsnGroupRev2 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 3, 2, 7)
)
cCdmaNotifPdsnGroupRev2.setObjects(
      *(("CISCO-CDMA-PDSN-MIB", "cCdmaSessionMaxAllowedNotif"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfMaxAllowedNotif"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionRegReqFailedNotif"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPdsnStatusChange"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionHighReached"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionLowReached"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaClusterSessionHighReached"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaClusterSessionLowReached"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaClusterMemberStatusChange"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaClusterCtrlStatusChange"))
)
if mibBuilder.loadTexts:
    cCdmaNotifPdsnGroupRev2.setStatus(
        "deprecated"
    )

cCdmaNotifPdsnGroupRev3 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 3, 2, 11)
)
cCdmaNotifPdsnGroupRev3.setObjects(
      *(("CISCO-CDMA-PDSN-MIB", "cCdmaSessionMaxAllowedNotif"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPcfMaxAllowedNotif"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionRegReqFailedNotif"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaPdsnStatusChange"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionHighReached"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaSessionLowReached2"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaClusterSessionHighReached"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaClusterSessionLowReached"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaClusterMemberStatusChange2"),
        ("CISCO-CDMA-PDSN-MIB", "cCdmaClusterCtrlStatusChange2"))
)
if mibBuilder.loadTexts:
    cCdmaNotifPdsnGroupRev3.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cCdmaPdsnMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cCdmaPdsnMIBCompliance.setStatus(
        "obsolete"
    )

cCdmaPdsnMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 3, 1, 2)
)
if mibBuilder.loadTexts:
    cCdmaPdsnMIBComplianceRev1.setStatus(
        "obsolete"
    )

cCdmaPdsnMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 3, 1, 3)
)
if mibBuilder.loadTexts:
    cCdmaPdsnMIBComplianceRev2.setStatus(
        "obsolete"
    )

cCdmaPdsnMIBComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 3, 1, 4)
)
if mibBuilder.loadTexts:
    cCdmaPdsnMIBComplianceRev3.setStatus(
        "deprecated"
    )

cCdmaPdsnMIBComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 3, 1, 5)
)
if mibBuilder.loadTexts:
    cCdmaPdsnMIBComplianceRev4.setStatus(
        "deprecated"
    )

cCdmaPdsnMIBComplianceRev5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 3, 1, 6)
)
if mibBuilder.loadTexts:
    cCdmaPdsnMIBComplianceRev5.setStatus(
        "deprecated"
    )

cCdmaPdsnMIBComplianceRev6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 157, 3, 1, 7)
)
if mibBuilder.loadTexts:
    cCdmaPdsnMIBComplianceRev6.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CDMA-PDSN-MIB",
    **{"CCdmaMsidType": CCdmaMsidType,
       "CCdmaSystemStatus": CCdmaSystemStatus,
       "CCdmaServiceAffectedLevel": CCdmaServiceAffectedLevel,
       "CCdmaServiceOption": CCdmaServiceOption,
       "ciscoCdmaPdsnMIB": ciscoCdmaPdsnMIB,
       "ciscoCdmaPdsnMIBObjects": ciscoCdmaPdsnMIBObjects,
       "cCdmaSystemInfo": cCdmaSystemInfo,
       "cCdmaSessionTotal": cCdmaSessionTotal,
       "cCdmaSessionMaxAllowed": cCdmaSessionMaxAllowed,
       "cCdmaPcfTotal": cCdmaPcfTotal,
       "cCdmaPcfMaxAllowed": cCdmaPcfMaxAllowed,
       "cCdmaSimpleIpFlowTotal": cCdmaSimpleIpFlowTotal,
       "cCdmaMobileIpFlowTotal": cCdmaMobileIpFlowTotal,
       "cCdmaProxyMobileIpFlowTotal": cCdmaProxyMobileIpFlowTotal,
       "cCdmaSessionFailTotal": cCdmaSessionFailTotal,
       "cCdmaServingPdsnHostname": cCdmaServingPdsnHostname,
       "cCdmaSessionPdsnAuthenTimer": cCdmaSessionPdsnAuthenTimer,
       "cCdmaSessionPdsnMaxFailHistory": cCdmaSessionPdsnMaxFailHistory,
       "cCdmaSessionMaxNotifEnabled": cCdmaSessionMaxNotifEnabled,
       "cCdmaPcfMaxAllowedNotifEnabled": cCdmaPcfMaxAllowedNotifEnabled,
       "cCdmaFormatErrorNotifEnabled": cCdmaFormatErrorNotifEnabled,
       "cCdmaRegReqFailedNotifEnabled": cCdmaRegReqFailedNotifEnabled,
       "cCdmaSystemVersion": cCdmaSystemVersion,
       "cCdmaSystemStatus": cCdmaSystemStatus,
       "cCdmaActiveSessions": cCdmaActiveSessions,
       "cCdmaDormantSessions": cCdmaDormantSessions,
       "cCdmaSrEnabled": cCdmaSrEnabled,
       "cCdmaPPPoGRESessionTotal": cCdmaPPPoGRESessionTotal,
       "cCdmaHDLCoGRESessionTotal": cCdmaHDLCoGRESessionTotal,
       "cCdmaEstablishedSessions": cCdmaEstablishedSessions,
       "cCdmaReleasedSessions": cCdmaReleasedSessions,
       "cCdmaMSIDFlowTotal": cCdmaMSIDFlowTotal,
       "cCdmaVPDNFlowTotal": cCdmaVPDNFlowTotal,
       "cCdmaPcfInfo": cCdmaPcfInfo,
       "cCdmaPcfTable": cCdmaPcfTable,
       "cCdmaPcfEntry": cCdmaPcfEntry,
       "cCdmaPcfIpAddress": cCdmaPcfIpAddress,
       "cCdmaPcfSessionTotal": cCdmaPcfSessionTotal,
       "cCdmaPcfSessionMaxTotal": cCdmaPcfSessionMaxTotal,
       "cCdmaPcfErrorTotal": cCdmaPcfErrorTotal,
       "cCdmaSessionInfo": cCdmaSessionInfo,
       "cCdmaSessionTable": cCdmaSessionTable,
       "cCdmaSessionEntry": cCdmaSessionEntry,
       "cCdmaSessionMsid": cCdmaSessionMsid,
       "cCdmaSessionMsidType": cCdmaSessionMsidType,
       "cCdmaSessionEsn": cCdmaSessionEsn,
       "cCdmaSessionPdsnIp": cCdmaSessionPdsnIp,
       "cCdmaSessionFaIp": cCdmaSessionFaIp,
       "cCdmaSessionA11HaIp": cCdmaSessionA11HaIp,
       "cCdmaSessionA11FaIp": cCdmaSessionA11FaIp,
       "cCdmaSessionKey": cCdmaSessionKey,
       "cCdmaSessionConnId": cCdmaSessionConnId,
       "cCdmaSessionMoMtInd": cCdmaSessionMoMtInd,
       "cCdmaSessionPppCompressEnabled": cCdmaSessionPppCompressEnabled,
       "cCdmaSessionVJCompressEnabled": cCdmaSessionVJCompressEnabled,
       "cCdmaSessionServiceOption": cCdmaSessionServiceOption,
       "cCdmaSessionSentOctets": cCdmaSessionSentOctets,
       "cCdmaSessionRcvdOctets": cCdmaSessionRcvdOctets,
       "cCdmaSessionSentPkts": cCdmaSessionSentPkts,
       "cCdmaSessionRcvdPkts": cCdmaSessionRcvdPkts,
       "cCdmaSessionDiscardedOutPkts": cCdmaSessionDiscardedOutPkts,
       "cCdmaSessionDiscardedInPkts": cCdmaSessionDiscardedInPkts,
       "cCdmaSessionConnStartTime": cCdmaSessionConnStartTime,
       "cCdmaActiveConnTime": cCdmaActiveConnTime,
       "cCdmaSessionFlowCount": cCdmaSessionFlowCount,
       "cCdmaSessionStatus": cCdmaSessionStatus,
       "cCdmaSessionRegLifeTime": cCdmaSessionRegLifeTime,
       "cCdmaSessionRegTimeToExpire": cCdmaSessionRegTimeToExpire,
       "cCdmaSessionGREFromIPPkts": cCdmaSessionGREFromIPPkts,
       "cCdmaSessionGREToIPPkts": cCdmaSessionGREToIPPkts,
       "cCdmaSessionFlowTable": cCdmaSessionFlowTable,
       "cCdmaSessionFlowEntry": cCdmaSessionFlowEntry,
       "cCdmaSessionUserFlowIpAddress": cCdmaSessionUserFlowIpAddress,
       "cCdmaSessionNai": cCdmaSessionNai,
       "cCdmaSessionAddressingScheme": cCdmaSessionAddressingScheme,
       "cCdmaSessionFlowTechnology": cCdmaSessionFlowTechnology,
       "cCdmaSessionHaIpAddress": cCdmaSessionHaIpAddress,
       "cCdmaSessionTunnelProt": cCdmaSessionTunnelProt,
       "cCdmaFailHistInfo": cCdmaFailHistInfo,
       "cCdmaFailHistInfoTable": cCdmaFailHistInfoTable,
       "cCdmaFailHistInfoEntry": cCdmaFailHistInfoEntry,
       "cCdmaFailSessionIndex": cCdmaFailSessionIndex,
       "cCdmaFailSessionMsid": cCdmaFailSessionMsid,
       "cCdmaFailSessionMsidType": cCdmaFailSessionMsidType,
       "cCdmaFailSessionEsn": cCdmaFailSessionEsn,
       "cCdmaFailSessionA11HaIp": cCdmaFailSessionA11HaIp,
       "cCdmaFailSessionA11FaIp": cCdmaFailSessionA11FaIp,
       "cCdmaFailSessionConnId": cCdmaFailSessionConnId,
       "cCdmaFailSessionKey": cCdmaFailSessionKey,
       "cCdmaFailHistFailTime": cCdmaFailHistFailTime,
       "cCdmaFailHistFailType": cCdmaFailHistFailType,
       "cCdmaFailHistServiceOption": cCdmaFailHistServiceOption,
       "cCdmaFailHistPanId": cCdmaFailHistPanId,
       "cCdmaFailHistCanId": cCdmaFailHistCanId,
       "cCdmaFailHistBsid": cCdmaFailHistBsid,
       "cCdmaFailSessionEsn2": cCdmaFailSessionEsn2,
       "cCdmaRPRegistrationStats": cCdmaRPRegistrationStats,
       "cCdmaRPRegValidRequests": cCdmaRPRegValidRequests,
       "cCdmaRPRegAcceptedReplies": cCdmaRPRegAcceptedReplies,
       "cCdmaRPRegLifeTimeZeroRequests": cCdmaRPRegLifeTimeZeroRequests,
       "cCdmaRPDeRegAcceptedReplies": cCdmaRPDeRegAcceptedReplies,
       "cCdmaRPRegReasonUnSpecFailures": cCdmaRPRegReasonUnSpecFailures,
       "cCdmaRPRegAdminProhibFailures": cCdmaRPRegAdminProhibFailures,
       "cCdmaRPRegInsuffResFailures": cCdmaRPRegInsuffResFailures,
       "cCdmaRPRegMNAuthenFailures": cCdmaRPRegMNAuthenFailures,
       "cCdmaRPRegIdentMismatchFailures": cCdmaRPRegIdentMismatchFailures,
       "cCdmaRPRegBadRequestFailures": cCdmaRPRegBadRequestFailures,
       "cCdmaRPRegUnknownHAAddrFailures": cCdmaRPRegUnknownHAAddrFailures,
       "cCdmaRPRegNoRevTunnelFailures": cCdmaRPRegNoRevTunnelFailures,
       "cCdmaRPRegTBitNotSetFailures": cCdmaRPRegTBitNotSetFailures,
       "cCdmaRPRegBadCVSEFailures": cCdmaRPRegBadCVSEFailures,
       "cCdmaRPUpdateStats": cCdmaRPUpdateStats,
       "cCdmaRPUpdValidRequests": cCdmaRPUpdValidRequests,
       "cCdmaRPUpdAcceptedReplies": cCdmaRPUpdAcceptedReplies,
       "cCdmaRPUpdReasonUnSpecFailures": cCdmaRPUpdReasonUnSpecFailures,
       "cCdmaRPUpdAdminProhibFailures": cCdmaRPUpdAdminProhibFailures,
       "cCdmaRPUpdMNAuthenFailures": cCdmaRPUpdMNAuthenFailures,
       "cCdmaRPUpdIdentMismatchFailures": cCdmaRPUpdIdentMismatchFailures,
       "cCdmaRPUpdBadRequestFailures": cCdmaRPUpdBadRequestFailures,
       "cCdmaPerformanceStats": cCdmaPerformanceStats,
       "cCdmaRpRegStats": cCdmaRpRegStats,
       "cCdmaRpRegReceivedReqs": cCdmaRpRegReceivedReqs,
       "cCdmaRpRegAcceptedReqs": cCdmaRpRegAcceptedReqs,
       "cCdmaRpRegDeniedReqs": cCdmaRpRegDeniedReqs,
       "cCdmaRpRegDiscardedReqs": cCdmaRpRegDiscardedReqs,
       "cCdmaRpInitRegAcceptedReqs": cCdmaRpInitRegAcceptedReqs,
       "cCdmaRpInitRegDeniedReqs": cCdmaRpInitRegDeniedReqs,
       "cCdmaRpReRegAcceptedReqs": cCdmaRpReRegAcceptedReqs,
       "cCdmaRpReRegDeniedReqs": cCdmaRpReRegDeniedReqs,
       "cCdmaRpDeRegAcceptedReqs": cCdmaRpDeRegAcceptedReqs,
       "cCdmaRpDeRegDeniedReqs": cCdmaRpDeRegDeniedReqs,
       "cCdmaRpRegReasonlUnSpecFailures": cCdmaRpRegReasonlUnSpecFailures,
       "cCdmaRpRegAdminProhibFailures": cCdmaRpRegAdminProhibFailures,
       "cCdmaRpRegInsuffResFailures": cCdmaRpRegInsuffResFailures,
       "cCdmaRpRegMNAuthFailures": cCdmaRpRegMNAuthFailures,
       "cCdmaRpRegIdMismatchFailures": cCdmaRpRegIdMismatchFailures,
       "cCdmaRpRegBadReqFailures": cCdmaRpRegBadReqFailures,
       "cCdmaRpRegUnknownPdsnFailures": cCdmaRpRegUnknownPdsnFailures,
       "cCdmaRpRegNoRevTunnelFailures": cCdmaRpRegNoRevTunnelFailures,
       "cCdmaRpRegTBitNotSetFailures": cCdmaRpRegTBitNotSetFailures,
       "cCdmaRpRegBadCVSEFailures": cCdmaRpRegBadCVSEFailures,
       "cCdmaRpRegReasonUnSpecFailures": cCdmaRpRegReasonUnSpecFailures,
       "cCdmaRpDeRegHandoffAcceptedReqs": cCdmaRpDeRegHandoffAcceptedReqs,
       "cCdmaRpDeRegHandoffDeniedReqs": cCdmaRpDeRegHandoffDeniedReqs,
       "cCdmaRpInitRegReceivedReqs": cCdmaRpInitRegReceivedReqs,
       "cCdmaRpInitRegDiscardedReqs": cCdmaRpInitRegDiscardedReqs,
       "cCdmaRpReRegReceivedReqs": cCdmaRpReRegReceivedReqs,
       "cCdmaRpReRegDiscardedReqs": cCdmaRpReRegDiscardedReqs,
       "cCdmaRpDeRegReceivedReqs": cCdmaRpDeRegReceivedReqs,
       "cCdmaRpDeRegDiscardedReqs": cCdmaRpDeRegDiscardedReqs,
       "cCdmaRpHandoffRegReceivedReqs": cCdmaRpHandoffRegReceivedReqs,
       "cCdmaRpHandoffRegAcceptedReqs": cCdmaRpHandoffRegAcceptedReqs,
       "cCdmaRpHandoffRegDeniedReqs": cCdmaRpHandoffRegDeniedReqs,
       "cCdmaRpHandoffRegDiscardedReqs": cCdmaRpHandoffRegDiscardedReqs,
       "cCdmaRpReRegAirlinkStarts": cCdmaRpReRegAirlinkStarts,
       "cCdmaRpReRegAirlinkStops": cCdmaRpReRegAirlinkStops,
       "cCdmaRpDeRegAirlinkStops": cCdmaRpDeRegAirlinkStops,
       "cCdmaRpInterPCFActiveHandoffs": cCdmaRpInterPCFActiveHandoffs,
       "cCdmaRpInterPCFDormantHandoffs": cCdmaRpInterPCFDormantHandoffs,
       "cCdmaRpUpdStats": cCdmaRpUpdStats,
       "cCdmaRpUpdTransmittedReqs": cCdmaRpUpdTransmittedReqs,
       "cCdmaRpUpdAcceptedReqs": cCdmaRpUpdAcceptedReqs,
       "cCdmaRpUpdDeniedReqs": cCdmaRpUpdDeniedReqs,
       "cCdmaRpUpdNotAckedReqs": cCdmaRpUpdNotAckedReqs,
       "cCdmaRpUpdInitTransmittedReqs": cCdmaRpUpdInitTransmittedReqs,
       "cCdmaRpUpdReTransmittedReqs": cCdmaRpUpdReTransmittedReqs,
       "cCdmaRpUpdReceivedAcks": cCdmaRpUpdReceivedAcks,
       "cCdmaRpUpdDiscardedAcks": cCdmaRpUpdDiscardedAcks,
       "cCdmaRpUpdRpLifeExpReqs": cCdmaRpUpdRpLifeExpReqs,
       "cCdmaRpUpdPPPtermReqs": cCdmaRpUpdPPPtermReqs,
       "cCdmaRpUpdOtherReasonReqs": cCdmaRpUpdOtherReasonReqs,
       "cCdmaRpUpdReasonUnSpecFailures": cCdmaRpUpdReasonUnSpecFailures,
       "cCdmaRpUpdAdminProhibFailures": cCdmaRpUpdAdminProhibFailures,
       "cCdmaRpUpdMNAuthenFailures": cCdmaRpUpdMNAuthenFailures,
       "cCdmaRpUpdIdentMismatchFailures": cCdmaRpUpdIdentMismatchFailures,
       "cCdmaRpUpdBadReqFailures": cCdmaRpUpdBadReqFailures,
       "cCdmaRpUpdPcfHandoffs": cCdmaRpUpdPcfHandoffs,
       "cCdmaRpUpdHandoffNotAckedReqs": cCdmaRpUpdHandoffNotAckedReqs,
       "cCdmaRpUpdHandoffReceivedAcks": cCdmaRpUpdHandoffReceivedAcks,
       "cCdmaRpUpdHandoffAcceptedReqs": cCdmaRpUpdHandoffAcceptedReqs,
       "cCdmaRpUpdHandoffDeniedReqs": cCdmaRpUpdHandoffDeniedReqs,
       "cCdmaRpUpdHandoffDiscardedAcks": cCdmaRpUpdHandoffDiscardedAcks,
       "cCdmaRpUpdHandoffInitTxdReqs": cCdmaRpUpdHandoffInitTxdReqs,
       "cCdmaRpUpdHandoffReTxdReqs": cCdmaRpUpdHandoffReTxdReqs,
       "cCdmaRpUpdHandoffReaUnSpecFails": cCdmaRpUpdHandoffReaUnSpecFails,
       "cCdmaRpUpdHandoffAdmProhibFails": cCdmaRpUpdHandoffAdmProhibFails,
       "cCdmaRpUpdHandoffMNAuthenFails": cCdmaRpUpdHandoffMNAuthenFails,
       "cCdmaRpUpdHandoffIdMismatchFails": cCdmaRpUpdHandoffIdMismatchFails,
       "cCdmaRpUpdHandoffBadReqFails": cCdmaRpUpdHandoffBadReqFails,
       "cCdmaPppStats": cCdmaPppStats,
       "cCdmaPppSetupStats": cCdmaPppSetupStats,
       "cCdmaPppCurrentConnections": cCdmaPppCurrentConnections,
       "cCdmaPppConnectionInitiateReqs": cCdmaPppConnectionInitiateReqs,
       "cCdmaPppConnectionSuccesses": cCdmaPppConnectionSuccesses,
       "cCdmaPppConnectionFailures": cCdmaPppConnectionFailures,
       "cCdmaPppLcpFailures": cCdmaPppLcpFailures,
       "cCdmaPppAuthFailures": cCdmaPppAuthFailures,
       "cCdmaPppIpcpFailures": cCdmaPppIpcpFailures,
       "cCdmaPppEnterLcpNums": cCdmaPppEnterLcpNums,
       "cCdmaPppEnterAuthNums": cCdmaPppEnterAuthNums,
       "cCdmaPppEnterIpcpNums": cCdmaPppEnterIpcpNums,
       "cCdmaPppLcpFailuresMaxRetrans": cCdmaPppLcpFailuresMaxRetrans,
       "cCdmaPppLcpFailuresUnknown": cCdmaPppLcpFailuresUnknown,
       "cCdmaPppIpcpFailuresMaxRetrans": cCdmaPppIpcpFailuresMaxRetrans,
       "cCdmaPppIpcpFailuresUnknown": cCdmaPppIpcpFailuresUnknown,
       "cCdmaPppConnectionsAborted": cCdmaPppConnectionsAborted,
       "cCdmaPppLcpOptionIssueFailures": cCdmaPppLcpOptionIssueFailures,
       "cCdmaPppIpcpOptionIssueFailures": cCdmaPppIpcpOptionIssueFailures,
       "cCdmaPppAuthMaxRetransFailures": cCdmaPppAuthMaxRetransFailures,
       "cCdmaPppNoRemoteIpAddressReleases": cCdmaPppNoRemoteIpAddressReleases,
       "cCdmaPppLowerLayerReleaseFailures": cCdmaPppLowerLayerReleaseFailures,
       "cCdmaPppIpcpPhaseReceivedTermreqs": cCdmaPppIpcpPhaseReceivedTermreqs,
       "cCdmaPppIpcpPhaseSentTermreqs": cCdmaPppIpcpPhaseSentTermreqs,
       "cCdmaPppAuthPhaseReceivedTermreqs": cCdmaPppAuthPhaseReceivedTermreqs,
       "cCdmaPppAuthPhaseSentTermreqs": cCdmaPppAuthPhaseSentTermreqs,
       "cCdmaPppLcpPhaseReceivedTermreqs": cCdmaPppLcpPhaseReceivedTermreqs,
       "cCdmaPppLcpPhaseSentTermreqs": cCdmaPppLcpPhaseSentTermreqs,
       "cCdmaPppPreLCPPdsnA10Releases": cCdmaPppPreLCPPdsnA10Releases,
       "cCdmaPppPreLCPPcfA10Releases": cCdmaPppPreLCPPcfA10Releases,
       "cCdmaPppLCPPdsnA10Releases": cCdmaPppLCPPdsnA10Releases,
       "cCdmaPppLCPPcfA10Releases": cCdmaPppLCPPcfA10Releases,
       "cCdmaPppAuthPdsnA10Releases": cCdmaPppAuthPdsnA10Releases,
       "cCdmaPppAuthPcfA10Releases": cCdmaPppAuthPcfA10Releases,
       "cCdmaPppIPCPPdsnA10Releases": cCdmaPppIPCPPdsnA10Releases,
       "cCdmaPppIPCPPcfA10Releases": cCdmaPppIPCPPcfA10Releases,
       "cCdmaPppLcpSuccesses": cCdmaPppLcpSuccesses,
       "cCdmaPppIpcpSuccesses": cCdmaPppIpcpSuccesses,
       "cCdmaPppAuthSuccesses": cCdmaPppAuthSuccesses,
       "cCdmaPppConnectionOtherFailures": cCdmaPppConnectionOtherFailures,
       "cCdmaPppReNegoStats": cCdmaPppReNegoStats,
       "cCdmaPppRenegTotalReqs": cCdmaPppRenegTotalReqs,
       "cCdmaPppRenegByPdsnReqs": cCdmaPppRenegByPdsnReqs,
       "cCdmaPppRenegByMobileReqs": cCdmaPppRenegByMobileReqs,
       "cCdmaPppRenegLcpIpcpReqs": cCdmaPppRenegLcpIpcpReqs,
       "cCdmaPppRenegAddrMismatchReqs": cCdmaPppRenegAddrMismatchReqs,
       "cCdmaPppRenegOtherReasonReqs": cCdmaPppRenegOtherReasonReqs,
       "cCdmaPppRenegSuccesses": cCdmaPppRenegSuccesses,
       "cCdmaPppRenegFailures": cCdmaPppRenegFailures,
       "cCdmaPppRenegConnectionsAborted": cCdmaPppRenegConnectionsAborted,
       "cCdmaPppRenegAnidChanges": cCdmaPppRenegAnidChanges,
       "cCdmaPppAuthStats": cCdmaPppAuthStats,
       "cCdmaPppAuthChapAttempts": cCdmaPppAuthChapAttempts,
       "cCdmaPppAuthChapSuccesses": cCdmaPppAuthChapSuccesses,
       "cCdmaPppAuthChapFailures": cCdmaPppAuthChapFailures,
       "cCdmaPppAuthPapAttempts": cCdmaPppAuthPapAttempts,
       "cCdmaPppAuthPapSuccesses": cCdmaPppAuthPapSuccesses,
       "cCdmaPppAuthPapFailures": cCdmaPppAuthPapFailures,
       "cCdmaPppAuthMschapAttempts": cCdmaPppAuthMschapAttempts,
       "cCdmaPppAuthMschapSuccesses": cCdmaPppAuthMschapSuccesses,
       "cCdmaPppAuthMschapFailures": cCdmaPppAuthMschapFailures,
       "cCdmaPppAuthEapAttempts": cCdmaPppAuthEapAttempts,
       "cCdmaPppAuthEapSuccesses": cCdmaPppAuthEapSuccesses,
       "cCdmaPppAuthEapFailures": cCdmaPppAuthEapFailures,
       "cCdmaPppAuthMsidAttempts": cCdmaPppAuthMsidAttempts,
       "cCdmaPppAuthMsidSuccesses": cCdmaPppAuthMsidSuccesses,
       "cCdmaPppAuthMsidFailures": cCdmaPppAuthMsidFailures,
       "cCdmaPppAuthAAATimeouts": cCdmaPppAuthAAATimeouts,
       "cCdmaPppAuthChapTimeouts": cCdmaPppAuthChapTimeouts,
       "cCdmaPppAuthPapTimeouts": cCdmaPppAuthPapTimeouts,
       "cCdmaPppAuthMschapTimeouts": cCdmaPppAuthMschapTimeouts,
       "cCdmaPppAuthSkips": cCdmaPppAuthSkips,
       "cCdmaPppReleaseStats": cCdmaPppReleaseStats,
       "cCdmaPppTotalReleases": cCdmaPppTotalReleases,
       "cCdmaPppPdsnReleases": cCdmaPppPdsnReleases,
       "cCdmaPppMobileReleases": cCdmaPppMobileReleases,
       "cCdmaPppAddrFilterReleases": cCdmaPppAddrFilterReleases,
       "cCdmaPppAdminReleases": cCdmaPppAdminReleases,
       "cCdmaPppLcpTermReleases": cCdmaPppLcpTermReleases,
       "cCdmaPppIdleTimeoutReleases": cCdmaPppIdleTimeoutReleases,
       "cCdmaPppL2tpTunnelReleases": cCdmaPppL2tpTunnelReleases,
       "cCdmaPppInsufResReleases": cCdmaPppInsufResReleases,
       "cCdmaPppSessTimeoutReleases": cCdmaPppSessTimeoutReleases,
       "cCdmaPppSrvIntReleases": cCdmaPppSrvIntReleases,
       "cCdmaPppSrvUnavailReleases": cCdmaPppSrvUnavailReleases,
       "cCdmaPppMissEchoReleases": cCdmaPppMissEchoReleases,
       "cCdmaPppDeregisterByPcfReleases": cCdmaPppDeregisterByPcfReleases,
       "cCdmaPppLifetimeExpiryReleases": cCdmaPppLifetimeExpiryReleases,
       "cCdmaPppOtherReasonReleases": cCdmaPppOtherReasonReleases,
       "cCdmaPppMiscStats": cCdmaPppMiscStats,
       "cCdmaPppCompressNegoCons": cCdmaPppCompressNegoCons,
       "cCdmaPppCompressMsftCons": cCdmaPppCompressMsftCons,
       "cCdmaPppCompressAscendCons": cCdmaPppCompressAscendCons,
       "cCdmaPppCompressStackCons": cCdmaPppCompressStackCons,
       "cCdmaPppCompressDeflateCons": cCdmaPppCompressDeflateCons,
       "cCdmaPppCompressOtherCons": cCdmaPppCompressOtherCons,
       "cCdmaPppNegoMrruCons": cCdmaPppNegoMrruCons,
       "cCdmaPppNegoIpxCons": cCdmaPppNegoIpxCons,
       "cCdmaPppNegoIpCons": cCdmaPppNegoIpCons,
       "cCdmaPppNegoVjCompCons": cCdmaPppNegoVjCompCons,
       "cCdmaPppNegoBapCons": cCdmaPppNegoBapCons,
       "cCdmaPppConFormedBundles": cCdmaPppConFormedBundles,
       "cCdmaPppCompressNegoFailures": cCdmaPppCompressNegoFailures,
       "cCdmaPppTransmittedEchoReqs": cCdmaPppTransmittedEchoReqs,
       "cCdmaPppRetransmittedEchoReqs": cCdmaPppRetransmittedEchoReqs,
       "cCdmaPppReceivedEchoReplies": cCdmaPppReceivedEchoReplies,
       "cCdmaPppEchoRequestTimeouts": cCdmaPppEchoRequestTimeouts,
       "cCdmaPppUnknownProtocolPktDiscards": cCdmaPppUnknownProtocolPktDiscards,
       "cCdmaPppBadLengthPktDiscards": cCdmaPppBadLengthPktDiscards,
       "cCdmaTrafficStats": cCdmaTrafficStats,
       "cCdmaTransmittedSipKiloOctets": cCdmaTransmittedSipKiloOctets,
       "cCdmaReceivedSipKiloOctets": cCdmaReceivedSipKiloOctets,
       "cCdmaTransmittedSipPkts": cCdmaTransmittedSipPkts,
       "cCdmaReceivedSipPkts": cCdmaReceivedSipPkts,
       "cCdmaTransmittedMipKiloOctets": cCdmaTransmittedMipKiloOctets,
       "cCdmaReceivedMipKiloOctets": cCdmaReceivedMipKiloOctets,
       "cCdmaTransmittedMipPkts": cCdmaTransmittedMipPkts,
       "cCdmaReceivedMipPkts": cCdmaReceivedMipPkts,
       "cCdmaTransmittedPmipKiloOctets": cCdmaTransmittedPmipKiloOctets,
       "cCdmaReceivedPmipKiloOctets": cCdmaReceivedPmipKiloOctets,
       "cCdmaTransmittedPmipPkts": cCdmaTransmittedPmipPkts,
       "cCdmaReceivedPmipPkts": cCdmaReceivedPmipPkts,
       "cCdmaTransmittedSDBPkts": cCdmaTransmittedSDBPkts,
       "cCdmaTransmittedSDBOctets": cCdmaTransmittedSDBOctets,
       "cCdmaNoGREKeyPktDiscards": cCdmaNoGREKeyPktDiscards,
       "cCdmaNoSessionPktDiscards": cCdmaNoSessionPktDiscards,
       "cCdmaInvGREProtoPktDiscards": cCdmaInvGREProtoPktDiscards,
       "cCdmaInvCheckSumPktDiscards": cCdmaInvCheckSumPktDiscards,
       "cCdmaFlowTypeStats": cCdmaFlowTypeStats,
       "cCdmaFlowSimpleIpSuccesses": cCdmaFlowSimpleIpSuccesses,
       "cCdmaFlowMobilIpSuccesses": cCdmaFlowMobilIpSuccesses,
       "cCdmaFlowProxyIpSuccesses": cCdmaFlowProxyIpSuccesses,
       "cCdmaFlowVpdnSuccesses": cCdmaFlowVpdnSuccesses,
       "cCdmaFlowSimpleIpFailures": cCdmaFlowSimpleIpFailures,
       "cCdmaFlowMobileIpFailures": cCdmaFlowMobileIpFailures,
       "cCdmaFlowProxyIpFailures": cCdmaFlowProxyIpFailures,
       "cCdmaFlowVpdnFailures": cCdmaFlowVpdnFailures,
       "cCdmaFlowUnknownTypeFailures": cCdmaFlowUnknownTypeFailures,
       "cCdmaServiceOptionStats": cCdmaServiceOptionStats,
       "cCdmaServiceTotalOptions": cCdmaServiceTotalOptions,
       "cCdmaServiceOptionTable": cCdmaServiceOptionTable,
       "cCdmaServiceOptionEntry": cCdmaServiceOptionEntry,
       "cCdmaServiceOptionIndex": cCdmaServiceOptionIndex,
       "cCdmaServiceOptionSucesses": cCdmaServiceOptionSucesses,
       "cCdmaServiceOptionFailures": cCdmaServiceOptionFailures,
       "cCdmaHandoffStats": cCdmaHandoffStats,
       "cCdmaInterPcfHandoffs": cCdmaInterPcfHandoffs,
       "cCdmaInterPdsnHandoffs": cCdmaInterPdsnHandoffs,
       "cCdmaIdChangeHandoffs": cCdmaIdChangeHandoffs,
       "cCdmaStatusChangeStats": cCdmaStatusChangeStats,
       "cCdmaStatusIS2OOSes": cCdmaStatusIS2OOSes,
       "cCdmaStatusOOS2ISes": cCdmaStatusOOS2ISes,
       "cCdmaAddressSchemeStats": cCdmaAddressSchemeStats,
       "cCdmaAddressStaticSIPs": cCdmaAddressStaticSIPs,
       "cCdmaAddressDynamicSIPs": cCdmaAddressDynamicSIPs,
       "cCdmaAddressStaticMIPs": cCdmaAddressStaticMIPs,
       "cCdmaAddressDynamicMIPs": cCdmaAddressDynamicMIPs,
       "cCdmaAddressStaticPMIPs": cCdmaAddressStaticPMIPs,
       "cCdmaAddressDynamicPMIPs": cCdmaAddressDynamicPMIPs,
       "cCdmaAddressStaticVPDNs": cCdmaAddressStaticVPDNs,
       "cCdmaAddressDynamicVPDNs": cCdmaAddressDynamicVPDNs,
       "cCdmaPcfSoRpRegStats": cCdmaPcfSoRpRegStats,
       "cCdmaPcfSoRpRegStatsTable": cCdmaPcfSoRpRegStatsTable,
       "cCdmaPcfSoRpRegStatsEntry": cCdmaPcfSoRpRegStatsEntry,
       "cCdmaPcfSoRpRegIpAddrType": cCdmaPcfSoRpRegIpAddrType,
       "cCdmaPcfSoRpRegIpAddr": cCdmaPcfSoRpRegIpAddr,
       "cCdmaPcfSoRpRegServiceOption": cCdmaPcfSoRpRegServiceOption,
       "cCdmaPcfSoRpRegRcvdReqs": cCdmaPcfSoRpRegRcvdReqs,
       "cCdmaPcfSoRpRegAcptdReqs": cCdmaPcfSoRpRegAcptdReqs,
       "cCdmaPcfSoRpRegDeniedReqs": cCdmaPcfSoRpRegDeniedReqs,
       "cCdmaPcfSoRpRegDiscardedReqs": cCdmaPcfSoRpRegDiscardedReqs,
       "cCdmaPcfSoRpInitRegAcptdReqs": cCdmaPcfSoRpInitRegAcptdReqs,
       "cCdmaPcfSoRpInitRegDeniedReqs": cCdmaPcfSoRpInitRegDeniedReqs,
       "cCdmaPcfSoRpReRegAcptdReqs": cCdmaPcfSoRpReRegAcptdReqs,
       "cCdmaPcfSoRpReRegDeniedReqs": cCdmaPcfSoRpReRegDeniedReqs,
       "cCdmaPcfSoRpDeRegAcptdReqs": cCdmaPcfSoRpDeRegAcptdReqs,
       "cCdmaPcfSoRpDeRegDeniedReqs": cCdmaPcfSoRpDeRegDeniedReqs,
       "cCdmaPcfSoRpRegPcfUnknwnFails": cCdmaPcfSoRpRegPcfUnknwnFails,
       "cCdmaPcfSoRpRegAdmnFails": cCdmaPcfSoRpRegAdmnFails,
       "cCdmaPcfSoRpRegNoRsrcFails": cCdmaPcfSoRpRegNoRsrcFails,
       "cCdmaPcfSoRpRegMNAuthFails": cCdmaPcfSoRpRegMNAuthFails,
       "cCdmaPcfSoRpRegIdMismatFails": cCdmaPcfSoRpRegIdMismatFails,
       "cCdmaPcfSoRpRegBadReqFails": cCdmaPcfSoRpRegBadReqFails,
       "cCdmaPcfSoRpRegUnkPdsnFails": cCdmaPcfSoRpRegUnkPdsnFails,
       "cCdmaPcfSoRpRegNoRevTunFails": cCdmaPcfSoRpRegNoRevTunFails,
       "cCdmaPcfSoRpRegTBitNSetFails": cCdmaPcfSoRpRegTBitNSetFails,
       "cCdmaPcfSoRpRegBadCVSEFails": cCdmaPcfSoRpRegBadCVSEFails,
       "cCdmaPcfSoRpInitRegRcvdReqs": cCdmaPcfSoRpInitRegRcvdReqs,
       "cCdmaPcfSoRpInitRegDiscardedReqs": cCdmaPcfSoRpInitRegDiscardedReqs,
       "cCdmaPcfSoRpReRegRcvdReqs": cCdmaPcfSoRpReRegRcvdReqs,
       "cCdmaPcfSoRpReRegDiscardedReqs": cCdmaPcfSoRpReRegDiscardedReqs,
       "cCdmaPcfSoRpDeRegRcvdReqs": cCdmaPcfSoRpDeRegRcvdReqs,
       "cCdmaPcfSoRpDeRegDiscardedReqs": cCdmaPcfSoRpDeRegDiscardedReqs,
       "cCdmaPcfSoRpHandoffRegRcvdReqs": cCdmaPcfSoRpHandoffRegRcvdReqs,
       "cCdmaPcfSoRpHandoffRegAcptdReqs": cCdmaPcfSoRpHandoffRegAcptdReqs,
       "cCdmaPcfSoRpHandoffRegDeniedReqs": cCdmaPcfSoRpHandoffRegDeniedReqs,
       "cCdmaPcfSoRpHandoffRegDiscardedReqs": cCdmaPcfSoRpHandoffRegDiscardedReqs,
       "cCdmaPcfSoRpReRegAirlinkStarts": cCdmaPcfSoRpReRegAirlinkStarts,
       "cCdmaPcfSoRpReRegAirlinkStops": cCdmaPcfSoRpReRegAirlinkStops,
       "cCdmaPcfSoRpDeRegAirlinkStops": cCdmaPcfSoRpDeRegAirlinkStops,
       "cCdmaPcfSoRpUpdStats": cCdmaPcfSoRpUpdStats,
       "cCdmaPcfSoRpUpdStatsTable": cCdmaPcfSoRpUpdStatsTable,
       "cCdmaPcfSoRpUpdStatsEntry": cCdmaPcfSoRpUpdStatsEntry,
       "cCdmaPcfSoRpUpdIpAddrType": cCdmaPcfSoRpUpdIpAddrType,
       "cCdmaPcfSoRpUpdIpAddr": cCdmaPcfSoRpUpdIpAddr,
       "cCdmaPcfSoRpUpdServiceOption": cCdmaPcfSoRpUpdServiceOption,
       "cCdmaPcfSoRpUpdTxdReqs": cCdmaPcfSoRpUpdTxdReqs,
       "cCdmaPcfSoRpUpdAcptdReqs": cCdmaPcfSoRpUpdAcptdReqs,
       "cCdmaPcfSoRpUpdDeniedReqs": cCdmaPcfSoRpUpdDeniedReqs,
       "cCdmaPcfSoRpUpdNotAckedReqs": cCdmaPcfSoRpUpdNotAckedReqs,
       "cCdmaPcfSoRpUpdInitTxdReqs": cCdmaPcfSoRpUpdInitTxdReqs,
       "cCdmaPcfSoRpUpdReTxdReqs": cCdmaPcfSoRpUpdReTxdReqs,
       "cCdmaPcfSoRpUpdRcvdAcks": cCdmaPcfSoRpUpdRcvdAcks,
       "cCdmaPcfSoRpUpdDiscardedAcks": cCdmaPcfSoRpUpdDiscardedAcks,
       "cCdmaPcfSoRpUpdRpLifeExpReqs": cCdmaPcfSoRpUpdRpLifeExpReqs,
       "cCdmaPcfSoRpUpdPPPtermReqs": cCdmaPcfSoRpUpdPPPtermReqs,
       "cCdmaPcfSoRpUpdOtherReaReqs": cCdmaPcfSoRpUpdOtherReaReqs,
       "cCdmaPcfSoRpUpdReaUnSpecFails": cCdmaPcfSoRpUpdReaUnSpecFails,
       "cCdmaPcfSoRpUpdAdmnFails": cCdmaPcfSoRpUpdAdmnFails,
       "cCdmaPcfSoRpUpdMNAuthFails": cCdmaPcfSoRpUpdMNAuthFails,
       "cCdmaPcfSoRpUpdIdMismatFails": cCdmaPcfSoRpUpdIdMismatFails,
       "cCdmaPcfSoRpUpdBadReqFails": cCdmaPcfSoRpUpdBadReqFails,
       "cCdmaSoRpUpdPcfHandoffs": cCdmaSoRpUpdPcfHandoffs,
       "cCdmaSoRpUpdHandoffNotAckedReqs": cCdmaSoRpUpdHandoffNotAckedReqs,
       "cCdmaSoRpUpdHandoffReceivedAcks": cCdmaSoRpUpdHandoffReceivedAcks,
       "cCdmaSoRpUpdHandoffAcceptedReqs": cCdmaSoRpUpdHandoffAcceptedReqs,
       "cCdmaSoRpUpdHandoffDeniedReqs": cCdmaSoRpUpdHandoffDeniedReqs,
       "cCdmaSoRpUpdHandoffDiscardedAcks": cCdmaSoRpUpdHandoffDiscardedAcks,
       "cCdmaSoRpUpdHandoffInitTxdReqs": cCdmaSoRpUpdHandoffInitTxdReqs,
       "cCdmaSoRpUpdHandoffReTxdReqs": cCdmaSoRpUpdHandoffReTxdReqs,
       "cCdmaSoRpUpdHandoffReaUnSpecFails": cCdmaSoRpUpdHandoffReaUnSpecFails,
       "cCdmaSoRpUpdHandoffAdmProhibFails": cCdmaSoRpUpdHandoffAdmProhibFails,
       "cCdmaSoRpUpdHandoffMNAuthenFails": cCdmaSoRpUpdHandoffMNAuthenFails,
       "cCdmaSoRpUpdHandoffIdMismatchFails": cCdmaSoRpUpdHandoffIdMismatchFails,
       "cCdmaSoRpUpdHandoffBadReqFails": cCdmaSoRpUpdHandoffBadReqFails,
       "cCdmaPcfSoPppSetupStats": cCdmaPcfSoPppSetupStats,
       "cCdmaPcfSoPppSetupStatsTable": cCdmaPcfSoPppSetupStatsTable,
       "cCdmaPcfSoPppSetupStatsEntry": cCdmaPcfSoPppSetupStatsEntry,
       "cCdmaPcfSoPppSetupIpAddrType": cCdmaPcfSoPppSetupIpAddrType,
       "cCdmaPcfSoPppSetupIpAddr": cCdmaPcfSoPppSetupIpAddr,
       "cCdmaPcfSoPppServiceOption": cCdmaPcfSoPppServiceOption,
       "cCdmaPcfSoPppCurrentConns": cCdmaPcfSoPppCurrentConns,
       "cCdmaPcfSoPppConnInitiateReqs": cCdmaPcfSoPppConnInitiateReqs,
       "cCdmaPcfSoPppConnSuccesses": cCdmaPcfSoPppConnSuccesses,
       "cCdmaPcfSoPppConnFails": cCdmaPcfSoPppConnFails,
       "cCdmaPcfSoPppConnAborts": cCdmaPcfSoPppConnAborts,
       "cCdmaRpSessUpdStats": cCdmaRpSessUpdStats,
       "cCdmaRpSessUpdTransmittedReqs": cCdmaRpSessUpdTransmittedReqs,
       "cCdmaRpSessUpdAcceptedReqs": cCdmaRpSessUpdAcceptedReqs,
       "cCdmaRpSessUpdDeniedReqs": cCdmaRpSessUpdDeniedReqs,
       "cCdmaRpSessUpdNotAckedReqs": cCdmaRpSessUpdNotAckedReqs,
       "cCdmaRpSessUpdInitTransmittedReqs": cCdmaRpSessUpdInitTransmittedReqs,
       "cCdmaRpSessUpdReTransmittedReqs": cCdmaRpSessUpdReTransmittedReqs,
       "cCdmaRpSessUpdReceivedAcks": cCdmaRpSessUpdReceivedAcks,
       "cCdmaRpSessUpdDiscardedAcks": cCdmaRpSessUpdDiscardedAcks,
       "cCdmaRpSessUpdAlwaysON": cCdmaRpSessUpdAlwaysON,
       "cCdmaRpSessUpdRNPDIT": cCdmaRpSessUpdRNPDIT,
       "cCdmaRpSessUpdReasonUnSpecFailures": cCdmaRpSessUpdReasonUnSpecFailures,
       "cCdmaRpSessUpdReasonParamNotUpdated": cCdmaRpSessUpdReasonParamNotUpdated,
       "cCdmaRpSessUpdMNAuthenFailures": cCdmaRpSessUpdMNAuthenFailures,
       "cCdmaRpSessUpdIdentMismatchFailures": cCdmaRpSessUpdIdentMismatchFailures,
       "cCdmaRpSessUpdBadReqFailures": cCdmaRpSessUpdBadReqFailures,
       "cCdmaPcfSoRpSessUpdStats": cCdmaPcfSoRpSessUpdStats,
       "cCdmaPcfSoRpSessUpdStatsTable": cCdmaPcfSoRpSessUpdStatsTable,
       "cCdmaPcfSoRpSessUpdStatsEntry": cCdmaPcfSoRpSessUpdStatsEntry,
       "cCdmaPcfSoRpSessUpdIpAddrType": cCdmaPcfSoRpSessUpdIpAddrType,
       "cCdmaPcfSoRpSessUpdIpAddr": cCdmaPcfSoRpSessUpdIpAddr,
       "cCdmaPcfSoRpSessUpdServiceOption": cCdmaPcfSoRpSessUpdServiceOption,
       "cCdmaPcfSoRpSessUpdTxdReqs": cCdmaPcfSoRpSessUpdTxdReqs,
       "cCdmaPcfSoRpSessUpdAcptdReqs": cCdmaPcfSoRpSessUpdAcptdReqs,
       "cCdmaPcfSoRpSessUpdDeniedReqs": cCdmaPcfSoRpSessUpdDeniedReqs,
       "cCdmaPcfSoRpSessUpdNotAckedReqs": cCdmaPcfSoRpSessUpdNotAckedReqs,
       "cCdmaPcfSoRpSessUpdInitTxdReqs": cCdmaPcfSoRpSessUpdInitTxdReqs,
       "cCdmaPcfSoRpSessUpdReTxdReqs": cCdmaPcfSoRpSessUpdReTxdReqs,
       "cCdmaPcfSoRpSessUpdRcvdAcks": cCdmaPcfSoRpSessUpdRcvdAcks,
       "cCdmaPcfSoRpSessUpdDiscardedAcks": cCdmaPcfSoRpSessUpdDiscardedAcks,
       "cCdmaPcfSoRpSessUpdAlwaysOn": cCdmaPcfSoRpSessUpdAlwaysOn,
       "cCdmaPcfSoRpSessUpdRNPDIT": cCdmaPcfSoRpSessUpdRNPDIT,
       "cCdmaPcfSoRpSessUpdParamNotUpdated": cCdmaPcfSoRpSessUpdParamNotUpdated,
       "cCdmaPcfSoRpSessUpdReaUnSpecFails": cCdmaPcfSoRpSessUpdReaUnSpecFails,
       "cCdmaPcfSoRpSessUpdMNAuthFails": cCdmaPcfSoRpSessUpdMNAuthFails,
       "cCdmaPcfSoRpSessUpdIdMismatFails": cCdmaPcfSoRpSessUpdIdMismatFails,
       "cCdmaPcfSoRpSessUpdBadReqFails": cCdmaPcfSoRpSessUpdBadReqFails,
       "cCdmaConfig": cCdmaConfig,
       "cCdmaThresholdConfig": cCdmaThresholdConfig,
       "cCdmaSessionHighThreshold": cCdmaSessionHighThreshold,
       "cCdmaSessionLowThreshold": cCdmaSessionLowThreshold,
       "cCdmaPdsnCluster": cCdmaPdsnCluster,
       "cCdmaClusterCommon": cCdmaClusterCommon,
       "cCdmaClusterType": cCdmaClusterType,
       "cCdmaClusterRole": cCdmaClusterRole,
       "cCdmaClusterMemberInfo": cCdmaClusterMemberInfo,
       "cCdmaClusterTotalControllers": cCdmaClusterTotalControllers,
       "cCdmaClusterCtrlTable": cCdmaClusterCtrlTable,
       "cCdmaClusterCtrlEntry": cCdmaClusterCtrlEntry,
       "cCdmaClusterCtrlAddressType": cCdmaClusterCtrlAddressType,
       "cCdmaClusterCtrlAddress": cCdmaClusterCtrlAddress,
       "cCdmaClusterCtrlStatus": cCdmaClusterCtrlStatus,
       "cCdmaClusterControllerInfo": cCdmaClusterControllerInfo,
       "cCdmaClusterTotalSessions": cCdmaClusterTotalSessions,
       "cCdmaClusterSessHighThreshold": cCdmaClusterSessHighThreshold,
       "cCdmaClusterSessLowThreshold": cCdmaClusterSessLowThreshold,
       "cCdmaClusterTotalMembers": cCdmaClusterTotalMembers,
       "cCdmaClusterMemberTable": cCdmaClusterMemberTable,
       "cCdmaClusterMemberEntry": cCdmaClusterMemberEntry,
       "cCdmaClusterMemberAddressType": cCdmaClusterMemberAddressType,
       "cCdmaClusterMemberAddress": cCdmaClusterMemberAddress,
       "cCdmaClusterMemberStatus": cCdmaClusterMemberStatus,
       "cCdmaClusterMemberLoad": cCdmaClusterMemberLoad,
       "cCdmaNotifConfig": cCdmaNotifConfig,
       "cCdmaNotifSeverityLevel": cCdmaNotifSeverityLevel,
       "cCdmaNotifObjects": cCdmaNotifObjects,
       "cCdmaServiceAffectedLevel": cCdmaServiceAffectedLevel,
       "cCdmaAffectedAddressType": cCdmaAffectedAddressType,
       "cCdmaAffectedAddress": cCdmaAffectedAddress,
       "cCdmaAffectedMemberStatus": cCdmaAffectedMemberStatus,
       "cCdmaAffectedCtrlStatus": cCdmaAffectedCtrlStatus,
       "cCdmaRpErrors": cCdmaRpErrors,
       "cCdmaRPRegReqErrors": cCdmaRPRegReqErrors,
       "cCdmaRegReqInvPakLenErrs": cCdmaRegReqInvPakLenErrs,
       "cCdmaRegReqInvProtocolErrs": cCdmaRegReqInvProtocolErrs,
       "cCdmaRegReqInvFlagsErrs": cCdmaRegReqInvFlagsErrs,
       "cCdmaRegReqInvMHAEKeyErrs": cCdmaRegReqInvMHAEKeyErrs,
       "cCdmaRegReqMismatchSPIErrs": cCdmaRegReqMismatchSPIErrs,
       "cCdmaRegReqInvSPIErrs": cCdmaRegReqInvSPIErrs,
       "cCdmaRegReqInvConnectionIDErrs": cCdmaRegReqInvConnectionIDErrs,
       "cCdmaRegReqInvMNIDErrs": cCdmaRegReqInvMNIDErrs,
       "cCdmaRegReqInvMNIDTypeErrs": cCdmaRegReqInvMNIDTypeErrs,
       "cCdmaRegReqInvMSIDLenErrs": cCdmaRegReqInvMSIDLenErrs,
       "cCdmaRegReqMissingSSEErrs": cCdmaRegReqMissingSSEErrs,
       "cCdmaRegReqMissingMHAEErrs": cCdmaRegReqMissingMHAEErrs,
       "cCdmaRegReqInvOrderErrs": cCdmaRegReqInvOrderErrs,
       "cCdmaRegReqInvVSEErrs": cCdmaRegReqInvVSEErrs,
       "cCdmaRegReqInvAppTypeInVSEErrs": cCdmaRegReqInvAppTypeInVSEErrs,
       "cCdmaRegReqDupAppTypeInVSEErrs": cCdmaRegReqDupAppTypeInVSEErrs,
       "cCdmaRegReqInvAppSubTypeInVSEErrs": cCdmaRegReqInvAppSubTypeInVSEErrs,
       "cCdmaRegReqInvVendorIDInVSEErrs": cCdmaRegReqInvVendorIDInVSEErrs,
       "cCdmaRegReqDupCVSEErrs": cCdmaRegReqDupCVSEErrs,
       "cCdmaRegReqAcctUnknwnAttrErrs": cCdmaRegReqAcctUnknwnAttrErrs,
       "cCdmaRegReqAcctInvLenAttrErrs": cCdmaRegReqAcctInvLenAttrErrs,
       "cCdmaRegReqAcctDupAttrErrs": cCdmaRegReqAcctDupAttrErrs,
       "cCdmaRegReqAcctRecRetransErrs": cCdmaRegReqAcctRecRetransErrs,
       "cCdmaRegReqAcctInvSeqNumErrs": cCdmaRegReqAcctInvSeqNumErrs,
       "cCdmaRegReqDuplicateGREKeyErrs": cCdmaRegReqDuplicateGREKeyErrs,
       "cCdmaRegReqSameGREKeySetupRcvdErrs": cCdmaRegReqSameGREKeySetupRcvdErrs,
       "cCdmaRegReqGREKeyChngNoSetupErrs": cCdmaRegReqGREKeyChngNoSetupErrs,
       "cCdmaRegReqInitNoSetupErrs": cCdmaRegReqInitNoSetupErrs,
       "cCdmaRegReqStartBeforeSetupErrs": cCdmaRegReqStartBeforeSetupErrs,
       "cCdmaRegReqStartOnCloseErrs": cCdmaRegReqStartOnCloseErrs,
       "cCdmaRegReqStartOnActiveErrs": cCdmaRegReqStartOnActiveErrs,
       "cCdmaRegReqStopOnDormantErrs": cCdmaRegReqStopOnDormantErrs,
       "cCdmaRegReqInitRcvdStopErrs": cCdmaRegReqInitRcvdStopErrs,
       "cCdmaRegReqInitRcvdSDBErrs": cCdmaRegReqInitRcvdSDBErrs,
       "cCdmaRegReqInvAirlinkRecErrs": cCdmaRegReqInvAirlinkRecErrs,
       "cCdmaRegReqDeRegNoSessionErrs": cCdmaRegReqDeRegNoSessionErrs,
       "cCdmaRegReqReRegInDisconnectErrs": cCdmaRegReqReRegInDisconnectErrs,
       "cCdmaRegReqMemFailErrs": cCdmaRegReqMemFailErrs,
       "cCdmaRpRegReqMaxSessionReachedErrs": cCdmaRpRegReqMaxSessionReachedErrs,
       "cCdmaRPRegUpdAckErrors": cCdmaRPRegUpdAckErrors,
       "cCdmaRegUpdAckInvPakLenErrs": cCdmaRegUpdAckInvPakLenErrs,
       "cCdmaRegUpdAckInvProtocolErrs": cCdmaRegUpdAckInvProtocolErrs,
       "cCdmaRegUpdAckInvRUAEKeyErrs": cCdmaRegUpdAckInvRUAEKeyErrs,
       "cCdmaRegUpdAckInvSPIErrs": cCdmaRegUpdAckInvSPIErrs,
       "cCdmaRegUpdAckInvConnectionIDErrs": cCdmaRegUpdAckInvConnectionIDErrs,
       "cCdmaRegUpdAckInvMNIDErrs": cCdmaRegUpdAckInvMNIDErrs,
       "cCdmaRegUpdAckInvMNIDTypeErrs": cCdmaRegUpdAckInvMNIDTypeErrs,
       "cCdmaRegUpdAckInvMSIDLenErrs": cCdmaRegUpdAckInvMSIDLenErrs,
       "cCdmaRegUpdAckMissingSSEErrs": cCdmaRegUpdAckMissingSSEErrs,
       "cCdmaRegUpdAckMissingRUAEErrs": cCdmaRegUpdAckMissingRUAEErrs,
       "cCdmaRegUpdAckInvOrderErrs": cCdmaRegUpdAckInvOrderErrs,
       "cCdmaRegUpdAckInvVSEErrs": cCdmaRegUpdAckInvVSEErrs,
       "cCdmaRegUpdAckNoSessionErrs": cCdmaRegUpdAckNoSessionErrs,
       "cCdmaRegUpdAckMemFailErrs": cCdmaRegUpdAckMemFailErrs,
       "cCdmaRPSessUpdAckErrors": cCdmaRPSessUpdAckErrors,
       "cCdmaSessUpdAckInvPakLenErrs": cCdmaSessUpdAckInvPakLenErrs,
       "cCdmaSessUpdAckInvProtocolErrs": cCdmaSessUpdAckInvProtocolErrs,
       "cCdmaSessUpdAckInvRUAEKeyErrs": cCdmaSessUpdAckInvRUAEKeyErrs,
       "cCdmaSessUpdAckInvSPIErrs": cCdmaSessUpdAckInvSPIErrs,
       "cCdmaSessUpdAckInvConnectionIDErrs": cCdmaSessUpdAckInvConnectionIDErrs,
       "cCdmaSessUpdAckInvMNIDErrs": cCdmaSessUpdAckInvMNIDErrs,
       "cCdmaSessUpdAckInvMNIDTypeErrs": cCdmaSessUpdAckInvMNIDTypeErrs,
       "cCdmaSessUpdAckInvMSIDLenErrs": cCdmaSessUpdAckInvMSIDLenErrs,
       "cCdmaSessUpdAckMissingSSEErrs": cCdmaSessUpdAckMissingSSEErrs,
       "cCdmaSessUpdAckMissingRUAEErrs": cCdmaSessUpdAckMissingRUAEErrs,
       "cCdmaSessUpdAckInvOrderErrs": cCdmaSessUpdAckInvOrderErrs,
       "cCdmaSessUpdAckInvVSEErrs": cCdmaSessUpdAckInvVSEErrs,
       "cCdmaSessUpdAckNoSessionErrs": cCdmaSessUpdAckNoSessionErrs,
       "cCdmaSessUpdAckMemFailErrs": cCdmaSessUpdAckMemFailErrs,
       "cCdmaRPRegReplyErrors": cCdmaRPRegReplyErrors,
       "cCdmaRegRplyInternalErrs": cCdmaRegRplyInternalErrs,
       "cCdmaRegRplyMemFailErrs": cCdmaRegRplyMemFailErrs,
       "cCdmaRpRplyPCFNoSecOrParseErrs": cCdmaRpRplyPCFNoSecOrParseErrs,
       "cCdmaRPRegUpdErrors": cCdmaRPRegUpdErrors,
       "cCdmaRegUpdInternalErrs": cCdmaRegUpdInternalErrs,
       "cCdmaRegUpdMemFailErrs": cCdmaRegUpdMemFailErrs,
       "cCdmaRPSessUpdErrors": cCdmaRPSessUpdErrors,
       "cCdmaSessUpdInternalErrs": cCdmaSessUpdInternalErrs,
       "cCdmaSessUpdMemFailErrs": cCdmaSessUpdMemFailErrs,
       "cCdmaPdsnMIBNotifPrefix": cCdmaPdsnMIBNotifPrefix,
       "cCdmaPdsnMIBNotifs": cCdmaPdsnMIBNotifs,
       "cCdmaSessionMaxAllowedNotif": cCdmaSessionMaxAllowedNotif,
       "cCdmaPcfMaxAllowedNotif": cCdmaPcfMaxAllowedNotif,
       "cCdmaSessionFormatErrorNotif": cCdmaSessionFormatErrorNotif,
       "cCdmaSessionRegReqFailedNotif": cCdmaSessionRegReqFailedNotif,
       "cCdmaPdsnStatusChange": cCdmaPdsnStatusChange,
       "cCdmaSessionHighReached": cCdmaSessionHighReached,
       "cCdmaSessionLowReached": cCdmaSessionLowReached,
       "cCdmaClusterSessionHighReached": cCdmaClusterSessionHighReached,
       "cCdmaClusterSessionLowReached": cCdmaClusterSessionLowReached,
       "cCdmaClusterMemberStatusChange": cCdmaClusterMemberStatusChange,
       "cCdmaClusterCtrlStatusChange": cCdmaClusterCtrlStatusChange,
       "cCdmaClusterMemberStatusChange2": cCdmaClusterMemberStatusChange2,
       "cCdmaClusterCtrlStatusChange2": cCdmaClusterCtrlStatusChange2,
       "cCdmaSessionLowReached2": cCdmaSessionLowReached2,
       "cCdmaPdsnMIBConformance": cCdmaPdsnMIBConformance,
       "cCdmaPdsnMIBCompliances": cCdmaPdsnMIBCompliances,
       "cCdmaPdsnMIBCompliance": cCdmaPdsnMIBCompliance,
       "cCdmaPdsnMIBComplianceRev1": cCdmaPdsnMIBComplianceRev1,
       "cCdmaPdsnMIBComplianceRev2": cCdmaPdsnMIBComplianceRev2,
       "cCdmaPdsnMIBComplianceRev3": cCdmaPdsnMIBComplianceRev3,
       "cCdmaPdsnMIBComplianceRev4": cCdmaPdsnMIBComplianceRev4,
       "cCdmaPdsnMIBComplianceRev5": cCdmaPdsnMIBComplianceRev5,
       "cCdmaPdsnMIBComplianceRev6": cCdmaPdsnMIBComplianceRev6,
       "cCdmaPdsnMIBGroups": cCdmaPdsnMIBGroups,
       "cCdmaSystemPdsnGroup": cCdmaSystemPdsnGroup,
       "cCdmaNotifPdsnGroup": cCdmaNotifPdsnGroup,
       "cCdmaSystemPdsnGroupRev1": cCdmaSystemPdsnGroupRev1,
       "cCdmaNotifPdsnGroupRev1": cCdmaNotifPdsnGroupRev1,
       "cCdmaSystemPdsnGroupRev2": cCdmaSystemPdsnGroupRev2,
       "cCdmaSystemPdsnGroupRev3": cCdmaSystemPdsnGroupRev3,
       "cCdmaNotifPdsnGroupRev2": cCdmaNotifPdsnGroupRev2,
       "cCdmaSystemPdsnGroupRev4": cCdmaSystemPdsnGroupRev4,
       "cCdmaPdsnPcfSoRpRegGroup": cCdmaPdsnPcfSoRpRegGroup,
       "cCdmaPdsnPcfSoPppGroup": cCdmaPdsnPcfSoPppGroup,
       "cCdmaNotifPdsnGroupRev3": cCdmaNotifPdsnGroupRev3,
       "cCdmaSystemPdsnGroupRev5": cCdmaSystemPdsnGroupRev5,
       "cCdmaSystemPdsnGroupSup1": cCdmaSystemPdsnGroupSup1,
       "cCdmaPdsnPcfSoRpRegGroupSup1": cCdmaPdsnPcfSoRpRegGroupSup1}
)
