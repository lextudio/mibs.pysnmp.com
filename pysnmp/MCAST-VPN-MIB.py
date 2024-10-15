# SNMP MIB module (MCAST-VPN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MCAST-VPN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:20:42 2024
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(ipMRouteEntry,) = mibBuilder.importSymbols(
    "IPMROUTE-STD-MIB",
    "ipMRouteEntry")

(jnxMvpnExperiment,) = mibBuilder.importSymbols(
    "JUNIPER-EXPERIMENT-MIB",
    "jnxMvpnExperiment")

(jnxMibs,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxMibs")

(JnxL2L3VpnMcastProviderTunnelType,) = mibBuilder.importSymbols(
    "L2L3-VPN-MCAST-MIB",
    "JnxL2L3VpnMcastProviderTunnelType")

(MplsLabel,) = mibBuilder.importSymbols(
    "MPLS-TC-STD-MIB",
    "MplsLabel")

(MplsVpnRouteDistinguisher,
 mplsVpnVrfName) = mibBuilder.importSymbols(
    "MPLS-VPN-MIB",
    "MplsVpnRouteDistinguisher",
    "mplsVpnVrfName")

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
 RowPointer,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowPointer",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

jnxMvpnMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1)
)
jnxMvpnMIB.setRevisions(
        ("2013-01-07 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxMvpnNotifications_ObjectIdentity = ObjectIdentity
jnxMvpnNotifications = _JnxMvpnNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 0)
)
_JnxMvpnObjects_ObjectIdentity = ObjectIdentity
jnxMvpnObjects = _JnxMvpnObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1)
)
_JnxMvpnScalars_ObjectIdentity = ObjectIdentity
jnxMvpnScalars = _JnxMvpnScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 1)
)
_JnxMvpnMvrfNumber_Type = Unsigned32
_JnxMvpnMvrfNumber_Object = MibScalar
jnxMvpnMvrfNumber = _JnxMvpnMvrfNumber_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 1, 1),
    _JnxMvpnMvrfNumber_Type()
)
jnxMvpnMvrfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMvpnMvrfNumber.setStatus("current")
_JnxMvpnMvrfNumberV4_Type = Unsigned32
_JnxMvpnMvrfNumberV4_Object = MibScalar
jnxMvpnMvrfNumberV4 = _JnxMvpnMvrfNumberV4_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 1, 2),
    _JnxMvpnMvrfNumberV4_Type()
)
jnxMvpnMvrfNumberV4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMvpnMvrfNumberV4.setStatus("current")
_JnxMvpnMvrfNumberV6_Type = Unsigned32
_JnxMvpnMvrfNumberV6_Object = MibScalar
jnxMvpnMvrfNumberV6 = _JnxMvpnMvrfNumberV6_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 1, 3),
    _JnxMvpnMvrfNumberV6_Type()
)
jnxMvpnMvrfNumberV6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMvpnMvrfNumberV6.setStatus("current")
_JnxMvpnMvrfNumberPimV4_Type = Unsigned32
_JnxMvpnMvrfNumberPimV4_Object = MibScalar
jnxMvpnMvrfNumberPimV4 = _JnxMvpnMvrfNumberPimV4_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 1, 4),
    _JnxMvpnMvrfNumberPimV4_Type()
)
jnxMvpnMvrfNumberPimV4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMvpnMvrfNumberPimV4.setStatus("current")
_JnxMvpnMvrfNumberPimV6_Type = Unsigned32
_JnxMvpnMvrfNumberPimV6_Object = MibScalar
jnxMvpnMvrfNumberPimV6 = _JnxMvpnMvrfNumberPimV6_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 1, 5),
    _JnxMvpnMvrfNumberPimV6_Type()
)
jnxMvpnMvrfNumberPimV6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMvpnMvrfNumberPimV6.setStatus("current")
_JnxMvpnMvrfNumberBgpV4_Type = Unsigned32
_JnxMvpnMvrfNumberBgpV4_Object = MibScalar
jnxMvpnMvrfNumberBgpV4 = _JnxMvpnMvrfNumberBgpV4_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 1, 6),
    _JnxMvpnMvrfNumberBgpV4_Type()
)
jnxMvpnMvrfNumberBgpV4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMvpnMvrfNumberBgpV4.setStatus("current")
_JnxMvpnMvrfNumberBgpV6_Type = Unsigned32
_JnxMvpnMvrfNumberBgpV6_Object = MibScalar
jnxMvpnMvrfNumberBgpV6 = _JnxMvpnMvrfNumberBgpV6_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 1, 7),
    _JnxMvpnMvrfNumberBgpV6_Type()
)
jnxMvpnMvrfNumberBgpV6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMvpnMvrfNumberBgpV6.setStatus("current")
_JnxMvpnMvrfNumberMldp_Type = Unsigned32
_JnxMvpnMvrfNumberMldp_Object = MibScalar
jnxMvpnMvrfNumberMldp = _JnxMvpnMvrfNumberMldp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 1, 8),
    _JnxMvpnMvrfNumberMldp_Type()
)
jnxMvpnMvrfNumberMldp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMvpnMvrfNumberMldp.setStatus("current")


class _JnxMvpnNotificationEnable_Type(TruthValue):
    """Custom type jnxMvpnNotificationEnable based on TruthValue"""


_JnxMvpnNotificationEnable_Object = MibScalar
jnxMvpnNotificationEnable = _JnxMvpnNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 1, 9),
    _JnxMvpnNotificationEnable_Type()
)
jnxMvpnNotificationEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMvpnNotificationEnable.setStatus("current")
_JnxMvpnGeneral_ObjectIdentity = ObjectIdentity
jnxMvpnGeneral = _JnxMvpnGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 2)
)
_JnxMvpnGeneralTable_Object = MibTable
jnxMvpnGeneralTable = _JnxMvpnGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    jnxMvpnGeneralTable.setStatus("current")
_JnxMvpnGeneralEntry_Object = MibTableRow
jnxMvpnGeneralEntry = _JnxMvpnGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 2, 1, 1)
)
jnxMvpnGeneralEntry.setIndexNames(
    (0, "MPLS-VPN-MIB", "mplsVpnVrfName"),
)
if mibBuilder.loadTexts:
    jnxMvpnGeneralEntry.setStatus("current")


class _JnxMvpnGenOperStatusChange_Type(Integer32):
    """Custom type jnxMvpnGenOperStatusChange based on Integer32"""
    defaultValue = 1

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
        *(("createdMvrf", 1),
          ("deletedMvrf", 2),
          ("modifiedMvrfIpmsiConfig", 3),
          ("modifiedMvrfSpmsiConfig", 4))
    )


_JnxMvpnGenOperStatusChange_Type.__name__ = "Integer32"
_JnxMvpnGenOperStatusChange_Object = MibTableColumn
jnxMvpnGenOperStatusChange = _JnxMvpnGenOperStatusChange_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 2, 1, 1, 1),
    _JnxMvpnGenOperStatusChange_Type()
)
jnxMvpnGenOperStatusChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMvpnGenOperStatusChange.setStatus("current")
_JnxMvpnGenOperChangeTime_Type = TimeStamp
_JnxMvpnGenOperChangeTime_Object = MibTableColumn
jnxMvpnGenOperChangeTime = _JnxMvpnGenOperChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 2, 1, 1, 2),
    _JnxMvpnGenOperChangeTime_Type()
)
jnxMvpnGenOperChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMvpnGenOperChangeTime.setStatus("current")


class _JnxMvpnGenCmcastRouteProtocolV4_Type(Integer32):
    """Custom type jnxMvpnGenCmcastRouteProtocolV4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bgp", 2),
          ("pim", 1))
    )


_JnxMvpnGenCmcastRouteProtocolV4_Type.__name__ = "Integer32"
_JnxMvpnGenCmcastRouteProtocolV4_Object = MibTableColumn
jnxMvpnGenCmcastRouteProtocolV4 = _JnxMvpnGenCmcastRouteProtocolV4_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 2, 1, 1, 3),
    _JnxMvpnGenCmcastRouteProtocolV4_Type()
)
jnxMvpnGenCmcastRouteProtocolV4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMvpnGenCmcastRouteProtocolV4.setStatus("current")


class _JnxMvpnGenCmcastRouteProtocolV6_Type(Integer32):
    """Custom type jnxMvpnGenCmcastRouteProtocolV6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bgp", 2),
          ("pim", 1))
    )


_JnxMvpnGenCmcastRouteProtocolV6_Type.__name__ = "Integer32"
_JnxMvpnGenCmcastRouteProtocolV6_Object = MibTableColumn
jnxMvpnGenCmcastRouteProtocolV6 = _JnxMvpnGenCmcastRouteProtocolV6_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 2, 1, 1, 4),
    _JnxMvpnGenCmcastRouteProtocolV6_Type()
)
jnxMvpnGenCmcastRouteProtocolV6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMvpnGenCmcastRouteProtocolV6.setStatus("current")
_JnxMvpnGenIpmsiConfigV4_Type = RowPointer
_JnxMvpnGenIpmsiConfigV4_Object = MibTableColumn
jnxMvpnGenIpmsiConfigV4 = _JnxMvpnGenIpmsiConfigV4_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 2, 1, 1, 5),
    _JnxMvpnGenIpmsiConfigV4_Type()
)
jnxMvpnGenIpmsiConfigV4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMvpnGenIpmsiConfigV4.setStatus("current")
_JnxMvpnGenIpmsiConfigV6_Type = RowPointer
_JnxMvpnGenIpmsiConfigV6_Object = MibTableColumn
jnxMvpnGenIpmsiConfigV6 = _JnxMvpnGenIpmsiConfigV6_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 2, 1, 1, 6),
    _JnxMvpnGenIpmsiConfigV6_Type()
)
jnxMvpnGenIpmsiConfigV6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMvpnGenIpmsiConfigV6.setStatus("current")
_JnxMvpnGenInterAsPmsiConfigV4_Type = RowPointer
_JnxMvpnGenInterAsPmsiConfigV4_Object = MibTableColumn
jnxMvpnGenInterAsPmsiConfigV4 = _JnxMvpnGenInterAsPmsiConfigV4_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 2, 1, 1, 7),
    _JnxMvpnGenInterAsPmsiConfigV4_Type()
)
jnxMvpnGenInterAsPmsiConfigV4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMvpnGenInterAsPmsiConfigV4.setStatus("current")
_JnxMvpnGenInterAsPmsiConfigV6_Type = RowPointer
_JnxMvpnGenInterAsPmsiConfigV6_Object = MibTableColumn
jnxMvpnGenInterAsPmsiConfigV6 = _JnxMvpnGenInterAsPmsiConfigV6_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 2, 1, 1, 8),
    _JnxMvpnGenInterAsPmsiConfigV6_Type()
)
jnxMvpnGenInterAsPmsiConfigV6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMvpnGenInterAsPmsiConfigV6.setStatus("current")
_JnxMvpnGenRowStatus_Type = RowStatus
_JnxMvpnGenRowStatus_Object = MibTableColumn
jnxMvpnGenRowStatus = _JnxMvpnGenRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 2, 1, 1, 9),
    _JnxMvpnGenRowStatus_Type()
)
jnxMvpnGenRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMvpnGenRowStatus.setStatus("current")
_JnxMvpnBgpGeneralTable_Object = MibTable
jnxMvpnBgpGeneralTable = _JnxMvpnBgpGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    jnxMvpnBgpGeneralTable.setStatus("current")
_JnxMvpnBgpGeneralEntry_Object = MibTableRow
jnxMvpnBgpGeneralEntry = _JnxMvpnBgpGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    jnxMvpnBgpGeneralEntry.setStatus("current")


class _JnxMvpnBgpGenMode_Type(Integer32):
    """Custom type jnxMvpnBgpGenMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rpt-spt", 1),
          ("spt-only", 2))
    )


_JnxMvpnBgpGenMode_Type.__name__ = "Integer32"
_JnxMvpnBgpGenMode_Object = MibTableColumn
jnxMvpnBgpGenMode = _JnxMvpnBgpGenMode_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 2, 2, 1, 1),
    _JnxMvpnBgpGenMode_Type()
)
jnxMvpnBgpGenMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMvpnBgpGenMode.setStatus("current")


class _JnxMvpnBgpGenUmhSelection_Type(Integer32):
    """Custom type jnxMvpnBgpGenUmhSelection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("c-root-group-hashing", 2),
          ("highest-pe-address", 1),
          ("ucast-umh-route", 3))
    )


_JnxMvpnBgpGenUmhSelection_Type.__name__ = "Integer32"
_JnxMvpnBgpGenUmhSelection_Object = MibTableColumn
jnxMvpnBgpGenUmhSelection = _JnxMvpnBgpGenUmhSelection_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 2, 2, 1, 2),
    _JnxMvpnBgpGenUmhSelection_Type()
)
jnxMvpnBgpGenUmhSelection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMvpnBgpGenUmhSelection.setStatus("current")


class _JnxMvpnBgpGenSiteType_Type(Integer32):
    """Custom type jnxMvpnBgpGenSiteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("receiver-only", 2),
          ("sender-only", 3),
          ("sender-receiver", 1))
    )


_JnxMvpnBgpGenSiteType_Type.__name__ = "Integer32"
_JnxMvpnBgpGenSiteType_Object = MibTableColumn
jnxMvpnBgpGenSiteType = _JnxMvpnBgpGenSiteType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 2, 2, 1, 3),
    _JnxMvpnBgpGenSiteType_Type()
)
jnxMvpnBgpGenSiteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMvpnBgpGenSiteType.setStatus("current")
_JnxMvpnBgpGenCmcastImportRt_Type = MplsVpnRouteDistinguisher
_JnxMvpnBgpGenCmcastImportRt_Object = MibTableColumn
jnxMvpnBgpGenCmcastImportRt = _JnxMvpnBgpGenCmcastImportRt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 2, 2, 1, 4),
    _JnxMvpnBgpGenCmcastImportRt_Type()
)
jnxMvpnBgpGenCmcastImportRt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMvpnBgpGenCmcastImportRt.setStatus("current")
_JnxMvpnBgpGenSrcAs_Type = Unsigned32
_JnxMvpnBgpGenSrcAs_Object = MibTableColumn
jnxMvpnBgpGenSrcAs = _JnxMvpnBgpGenSrcAs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 2, 2, 1, 5),
    _JnxMvpnBgpGenSrcAs_Type()
)
jnxMvpnBgpGenSrcAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMvpnBgpGenSrcAs.setStatus("current")
_JnxMvpnBgpGenSptnlLimit_Type = Unsigned32
_JnxMvpnBgpGenSptnlLimit_Object = MibTableColumn
jnxMvpnBgpGenSptnlLimit = _JnxMvpnBgpGenSptnlLimit_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 2, 2, 1, 6),
    _JnxMvpnBgpGenSptnlLimit_Type()
)
jnxMvpnBgpGenSptnlLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMvpnBgpGenSptnlLimit.setStatus("current")
_JnxMvpnConfig_ObjectIdentity = ObjectIdentity
jnxMvpnConfig = _JnxMvpnConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 3)
)
_JnxMvpnPmsiConfigTable_Object = MibTable
jnxMvpnPmsiConfigTable = _JnxMvpnPmsiConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    jnxMvpnPmsiConfigTable.setStatus("current")
_JnxMvpnPmsiConfigEntry_Object = MibTableRow
jnxMvpnPmsiConfigEntry = _JnxMvpnPmsiConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 3, 1, 1)
)
jnxMvpnPmsiConfigEntry.setIndexNames(
    (0, "MCAST-VPN-MIB", "jnxMvpnPmsiConfigTunnelType"),
    (0, "MCAST-VPN-MIB", "jnxMvpnPmsiConfigTunnelAuxInfo"),
    (0, "MCAST-VPN-MIB", "jnxMvpnPmsiConfigTunnelPimGroupAddressType"),
    (0, "MCAST-VPN-MIB", "jnxMvpnPmsiConfigTunnelPimGroupAddress"),
    (0, "MCAST-VPN-MIB", "jnxMvpnPmsiConfigTunnelOrTemplateName"),
)
if mibBuilder.loadTexts:
    jnxMvpnPmsiConfigEntry.setStatus("current")
_JnxMvpnPmsiConfigTunnelType_Type = JnxL2L3VpnMcastProviderTunnelType
_JnxMvpnPmsiConfigTunnelType_Object = MibTableColumn
jnxMvpnPmsiConfigTunnelType = _JnxMvpnPmsiConfigTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 3, 1, 1, 1),
    _JnxMvpnPmsiConfigTunnelType_Type()
)
jnxMvpnPmsiConfigTunnelType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMvpnPmsiConfigTunnelType.setStatus("current")
_JnxMvpnPmsiConfigTunnelAuxInfo_Type = Unsigned32
_JnxMvpnPmsiConfigTunnelAuxInfo_Object = MibTableColumn
jnxMvpnPmsiConfigTunnelAuxInfo = _JnxMvpnPmsiConfigTunnelAuxInfo_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 3, 1, 1, 2),
    _JnxMvpnPmsiConfigTunnelAuxInfo_Type()
)
jnxMvpnPmsiConfigTunnelAuxInfo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMvpnPmsiConfigTunnelAuxInfo.setStatus("current")
_JnxMvpnPmsiConfigTunnelPimGroupAddressType_Type = InetAddressType
_JnxMvpnPmsiConfigTunnelPimGroupAddressType_Object = MibTableColumn
jnxMvpnPmsiConfigTunnelPimGroupAddressType = _JnxMvpnPmsiConfigTunnelPimGroupAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 3, 1, 1, 3),
    _JnxMvpnPmsiConfigTunnelPimGroupAddressType_Type()
)
jnxMvpnPmsiConfigTunnelPimGroupAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMvpnPmsiConfigTunnelPimGroupAddressType.setStatus("current")
_JnxMvpnPmsiConfigTunnelPimGroupAddress_Type = InetAddress
_JnxMvpnPmsiConfigTunnelPimGroupAddress_Object = MibTableColumn
jnxMvpnPmsiConfigTunnelPimGroupAddress = _JnxMvpnPmsiConfigTunnelPimGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 3, 1, 1, 4),
    _JnxMvpnPmsiConfigTunnelPimGroupAddress_Type()
)
jnxMvpnPmsiConfigTunnelPimGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMvpnPmsiConfigTunnelPimGroupAddress.setStatus("current")
_JnxMvpnPmsiConfigTunnelOrTemplateName_Type = SnmpAdminString
_JnxMvpnPmsiConfigTunnelOrTemplateName_Object = MibTableColumn
jnxMvpnPmsiConfigTunnelOrTemplateName = _JnxMvpnPmsiConfigTunnelOrTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 3, 1, 1, 5),
    _JnxMvpnPmsiConfigTunnelOrTemplateName_Type()
)
jnxMvpnPmsiConfigTunnelOrTemplateName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMvpnPmsiConfigTunnelOrTemplateName.setStatus("current")


class _JnxMvpnPmsiConfigEncapsType_Type(Integer32):
    """Custom type jnxMvpnPmsiConfigEncapsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("greIp", 1),
          ("ipIp", 2),
          ("mpls", 3))
    )


_JnxMvpnPmsiConfigEncapsType_Type.__name__ = "Integer32"
_JnxMvpnPmsiConfigEncapsType_Object = MibTableColumn
jnxMvpnPmsiConfigEncapsType = _JnxMvpnPmsiConfigEncapsType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 3, 1, 1, 6),
    _JnxMvpnPmsiConfigEncapsType_Type()
)
jnxMvpnPmsiConfigEncapsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMvpnPmsiConfigEncapsType.setStatus("current")
_JnxMvpnPmsiConfigRowStatus_Type = RowStatus
_JnxMvpnPmsiConfigRowStatus_Object = MibTableColumn
jnxMvpnPmsiConfigRowStatus = _JnxMvpnPmsiConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 3, 1, 1, 7),
    _JnxMvpnPmsiConfigRowStatus_Type()
)
jnxMvpnPmsiConfigRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMvpnPmsiConfigRowStatus.setStatus("current")
_JnxMvpnSpmsiConfigTable_Object = MibTable
jnxMvpnSpmsiConfigTable = _JnxMvpnSpmsiConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    jnxMvpnSpmsiConfigTable.setStatus("current")
_JnxMvpnSpmsiConfigEntry_Object = MibTableRow
jnxMvpnSpmsiConfigEntry = _JnxMvpnSpmsiConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 3, 2, 1)
)
jnxMvpnSpmsiConfigEntry.setIndexNames(
    (0, "MPLS-VPN-MIB", "mplsVpnVrfName"),
    (0, "MCAST-VPN-MIB", "jnxMvpnSpmsiConfigCmcastAddressType"),
    (0, "MCAST-VPN-MIB", "jnxMvpnSpmsiConfigCmcastGroupAddress"),
    (0, "MCAST-VPN-MIB", "jnxMvpnSpmsiConfigCmcastGroupPrefixLen"),
    (0, "MCAST-VPN-MIB", "jnxMvpnSpmsiConfigCmcastSourceAddress"),
    (0, "MCAST-VPN-MIB", "jnxMvpnSpmsiConfigCmcastSourcePrefixLen"),
)
if mibBuilder.loadTexts:
    jnxMvpnSpmsiConfigEntry.setStatus("current")
_JnxMvpnSpmsiConfigCmcastAddressType_Type = InetAddressType
_JnxMvpnSpmsiConfigCmcastAddressType_Object = MibTableColumn
jnxMvpnSpmsiConfigCmcastAddressType = _JnxMvpnSpmsiConfigCmcastAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 3, 2, 1, 1),
    _JnxMvpnSpmsiConfigCmcastAddressType_Type()
)
jnxMvpnSpmsiConfigCmcastAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMvpnSpmsiConfigCmcastAddressType.setStatus("current")
_JnxMvpnSpmsiConfigCmcastGroupAddress_Type = InetAddress
_JnxMvpnSpmsiConfigCmcastGroupAddress_Object = MibTableColumn
jnxMvpnSpmsiConfigCmcastGroupAddress = _JnxMvpnSpmsiConfigCmcastGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 3, 2, 1, 2),
    _JnxMvpnSpmsiConfigCmcastGroupAddress_Type()
)
jnxMvpnSpmsiConfigCmcastGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMvpnSpmsiConfigCmcastGroupAddress.setStatus("current")
_JnxMvpnSpmsiConfigCmcastGroupPrefixLen_Type = Unsigned32
_JnxMvpnSpmsiConfigCmcastGroupPrefixLen_Object = MibTableColumn
jnxMvpnSpmsiConfigCmcastGroupPrefixLen = _JnxMvpnSpmsiConfigCmcastGroupPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 3, 2, 1, 3),
    _JnxMvpnSpmsiConfigCmcastGroupPrefixLen_Type()
)
jnxMvpnSpmsiConfigCmcastGroupPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMvpnSpmsiConfigCmcastGroupPrefixLen.setStatus("current")
_JnxMvpnSpmsiConfigCmcastSourceAddress_Type = InetAddress
_JnxMvpnSpmsiConfigCmcastSourceAddress_Object = MibTableColumn
jnxMvpnSpmsiConfigCmcastSourceAddress = _JnxMvpnSpmsiConfigCmcastSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 3, 2, 1, 4),
    _JnxMvpnSpmsiConfigCmcastSourceAddress_Type()
)
jnxMvpnSpmsiConfigCmcastSourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMvpnSpmsiConfigCmcastSourceAddress.setStatus("current")
_JnxMvpnSpmsiConfigCmcastSourcePrefixLen_Type = Unsigned32
_JnxMvpnSpmsiConfigCmcastSourcePrefixLen_Object = MibTableColumn
jnxMvpnSpmsiConfigCmcastSourcePrefixLen = _JnxMvpnSpmsiConfigCmcastSourcePrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 3, 2, 1, 5),
    _JnxMvpnSpmsiConfigCmcastSourcePrefixLen_Type()
)
jnxMvpnSpmsiConfigCmcastSourcePrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMvpnSpmsiConfigCmcastSourcePrefixLen.setStatus("current")


class _JnxMvpnSpmsiConfigThreshold_Type(Unsigned32):
    """Custom type jnxMvpnSpmsiConfigThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_JnxMvpnSpmsiConfigThreshold_Type.__name__ = "Unsigned32"
_JnxMvpnSpmsiConfigThreshold_Object = MibTableColumn
jnxMvpnSpmsiConfigThreshold = _JnxMvpnSpmsiConfigThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 3, 2, 1, 6),
    _JnxMvpnSpmsiConfigThreshold_Type()
)
jnxMvpnSpmsiConfigThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMvpnSpmsiConfigThreshold.setStatus("current")
if mibBuilder.loadTexts:
    jnxMvpnSpmsiConfigThreshold.setUnits("kilobits per second")
_JnxMvpnSpmsiConfigPmsiPointer_Type = RowPointer
_JnxMvpnSpmsiConfigPmsiPointer_Object = MibTableColumn
jnxMvpnSpmsiConfigPmsiPointer = _JnxMvpnSpmsiConfigPmsiPointer_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 3, 2, 1, 7),
    _JnxMvpnSpmsiConfigPmsiPointer_Type()
)
jnxMvpnSpmsiConfigPmsiPointer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMvpnSpmsiConfigPmsiPointer.setStatus("current")
_JnxMvpnSpmsiConfigRowStatus_Type = RowStatus
_JnxMvpnSpmsiConfigRowStatus_Object = MibTableColumn
jnxMvpnSpmsiConfigRowStatus = _JnxMvpnSpmsiConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 3, 2, 1, 8),
    _JnxMvpnSpmsiConfigRowStatus_Type()
)
jnxMvpnSpmsiConfigRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMvpnSpmsiConfigRowStatus.setStatus("current")
_JnxMvpnStates_ObjectIdentity = ObjectIdentity
jnxMvpnStates = _JnxMvpnStates_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 4)
)
_JnxMvpnIpmsiTable_Object = MibTable
jnxMvpnIpmsiTable = _JnxMvpnIpmsiTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    jnxMvpnIpmsiTable.setStatus("current")
_JnxMvpnIpmsiEntry_Object = MibTableRow
jnxMvpnIpmsiEntry = _JnxMvpnIpmsiEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 4, 1, 1)
)
jnxMvpnIpmsiEntry.setIndexNames(
    (0, "MPLS-VPN-MIB", "mplsVpnVrfName"),
    (0, "MCAST-VPN-MIB", "jnxMvpnIpmsiAfi"),
    (0, "MCAST-VPN-MIB", "jnxMvpnIpmsiRD"),
    (0, "MCAST-VPN-MIB", "jnxMvpnIpmsiOrigAddrType"),
    (0, "MCAST-VPN-MIB", "jnxMvpnIpmsiOrigAddress"),
)
if mibBuilder.loadTexts:
    jnxMvpnIpmsiEntry.setStatus("current")


class _JnxMvpnIpmsiAfi_Type(Unsigned32):
    """Custom type jnxMvpnIpmsiAfi based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_JnxMvpnIpmsiAfi_Type.__name__ = "Unsigned32"
_JnxMvpnIpmsiAfi_Object = MibTableColumn
jnxMvpnIpmsiAfi = _JnxMvpnIpmsiAfi_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 4, 1, 1, 1),
    _JnxMvpnIpmsiAfi_Type()
)
jnxMvpnIpmsiAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMvpnIpmsiAfi.setStatus("current")
_JnxMvpnIpmsiRD_Type = MplsVpnRouteDistinguisher
_JnxMvpnIpmsiRD_Object = MibTableColumn
jnxMvpnIpmsiRD = _JnxMvpnIpmsiRD_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 4, 1, 1, 2),
    _JnxMvpnIpmsiRD_Type()
)
jnxMvpnIpmsiRD.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMvpnIpmsiRD.setStatus("current")
_JnxMvpnIpmsiOrigAddrType_Type = InetAddressType
_JnxMvpnIpmsiOrigAddrType_Object = MibTableColumn
jnxMvpnIpmsiOrigAddrType = _JnxMvpnIpmsiOrigAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 4, 1, 1, 3),
    _JnxMvpnIpmsiOrigAddrType_Type()
)
jnxMvpnIpmsiOrigAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMvpnIpmsiOrigAddrType.setStatus("current")
_JnxMvpnIpmsiOrigAddress_Type = InetAddress
_JnxMvpnIpmsiOrigAddress_Object = MibTableColumn
jnxMvpnIpmsiOrigAddress = _JnxMvpnIpmsiOrigAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 4, 1, 1, 4),
    _JnxMvpnIpmsiOrigAddress_Type()
)
jnxMvpnIpmsiOrigAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMvpnIpmsiOrigAddress.setStatus("current")
_JnxMvpnIpmsiUpTime_Type = TimeInterval
_JnxMvpnIpmsiUpTime_Object = MibTableColumn
jnxMvpnIpmsiUpTime = _JnxMvpnIpmsiUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 4, 1, 1, 5),
    _JnxMvpnIpmsiUpTime_Type()
)
jnxMvpnIpmsiUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMvpnIpmsiUpTime.setStatus("current")
_JnxMvpnIpmsiAttribute_Type = RowPointer
_JnxMvpnIpmsiAttribute_Object = MibTableColumn
jnxMvpnIpmsiAttribute = _JnxMvpnIpmsiAttribute_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 4, 1, 1, 6),
    _JnxMvpnIpmsiAttribute_Type()
)
jnxMvpnIpmsiAttribute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMvpnIpmsiAttribute.setStatus("current")
_JnxMvpnInterasIpmsiTable_Object = MibTable
jnxMvpnInterasIpmsiTable = _JnxMvpnInterasIpmsiTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    jnxMvpnInterasIpmsiTable.setStatus("current")
_JnxMvpnInterasIpmsiEntry_Object = MibTableRow
jnxMvpnInterasIpmsiEntry = _JnxMvpnInterasIpmsiEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 4, 2, 1)
)
jnxMvpnInterasIpmsiEntry.setIndexNames(
    (0, "MPLS-VPN-MIB", "mplsVpnVrfName"),
    (0, "MCAST-VPN-MIB", "jnxMvpnInterasIpmsiAfi"),
    (0, "MCAST-VPN-MIB", "jnxMvpnInterasIpmsiRD"),
    (0, "MCAST-VPN-MIB", "jnxMvpnInterasIpmsiSrcAs"),
)
if mibBuilder.loadTexts:
    jnxMvpnInterasIpmsiEntry.setStatus("current")


class _JnxMvpnInterasIpmsiAfi_Type(Unsigned32):
    """Custom type jnxMvpnInterasIpmsiAfi based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_JnxMvpnInterasIpmsiAfi_Type.__name__ = "Unsigned32"
_JnxMvpnInterasIpmsiAfi_Object = MibTableColumn
jnxMvpnInterasIpmsiAfi = _JnxMvpnInterasIpmsiAfi_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 4, 2, 1, 1),
    _JnxMvpnInterasIpmsiAfi_Type()
)
jnxMvpnInterasIpmsiAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMvpnInterasIpmsiAfi.setStatus("current")
_JnxMvpnInterasIpmsiRD_Type = MplsVpnRouteDistinguisher
_JnxMvpnInterasIpmsiRD_Object = MibTableColumn
jnxMvpnInterasIpmsiRD = _JnxMvpnInterasIpmsiRD_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 4, 2, 1, 2),
    _JnxMvpnInterasIpmsiRD_Type()
)
jnxMvpnInterasIpmsiRD.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMvpnInterasIpmsiRD.setStatus("current")
_JnxMvpnInterasIpmsiSrcAs_Type = Unsigned32
_JnxMvpnInterasIpmsiSrcAs_Object = MibTableColumn
jnxMvpnInterasIpmsiSrcAs = _JnxMvpnInterasIpmsiSrcAs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 4, 2, 1, 3),
    _JnxMvpnInterasIpmsiSrcAs_Type()
)
jnxMvpnInterasIpmsiSrcAs.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMvpnInterasIpmsiSrcAs.setStatus("current")
_JnxMvpnInterasIpmsiAttribute_Type = RowPointer
_JnxMvpnInterasIpmsiAttribute_Object = MibTableColumn
jnxMvpnInterasIpmsiAttribute = _JnxMvpnInterasIpmsiAttribute_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 4, 2, 1, 4),
    _JnxMvpnInterasIpmsiAttribute_Type()
)
jnxMvpnInterasIpmsiAttribute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMvpnInterasIpmsiAttribute.setStatus("current")
_JnxMvpnSpmsiTable_Object = MibTable
jnxMvpnSpmsiTable = _JnxMvpnSpmsiTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 4, 3)
)
if mibBuilder.loadTexts:
    jnxMvpnSpmsiTable.setStatus("current")
_JnxMvpnSpmsiEntry_Object = MibTableRow
jnxMvpnSpmsiEntry = _JnxMvpnSpmsiEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 4, 3, 1)
)
jnxMvpnSpmsiEntry.setIndexNames(
    (0, "MPLS-VPN-MIB", "mplsVpnVrfName"),
    (0, "MCAST-VPN-MIB", "jnxMvpnSpmsiOrigAddrType"),
    (0, "MCAST-VPN-MIB", "jnxMvpnSpmsiOrigAddress"),
    (0, "MCAST-VPN-MIB", "jnxMvpnSpmsiCmcastAddrType"),
    (0, "MCAST-VPN-MIB", "jnxMvpnSpmsiCmcastGroup"),
    (0, "MCAST-VPN-MIB", "jnxMvpnSpmsiCmcastGroupPrefixLen"),
    (0, "MCAST-VPN-MIB", "jnxMvpnSpmsiCmcastSource"),
    (0, "MCAST-VPN-MIB", "jnxMvpnSpmsiCmcastSourcePrefixLen"),
)
if mibBuilder.loadTexts:
    jnxMvpnSpmsiEntry.setStatus("current")
_JnxMvpnSpmsiOrigAddrType_Type = InetAddressType
_JnxMvpnSpmsiOrigAddrType_Object = MibTableColumn
jnxMvpnSpmsiOrigAddrType = _JnxMvpnSpmsiOrigAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 4, 3, 1, 1),
    _JnxMvpnSpmsiOrigAddrType_Type()
)
jnxMvpnSpmsiOrigAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMvpnSpmsiOrigAddrType.setStatus("current")
_JnxMvpnSpmsiOrigAddress_Type = InetAddress
_JnxMvpnSpmsiOrigAddress_Object = MibTableColumn
jnxMvpnSpmsiOrigAddress = _JnxMvpnSpmsiOrigAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 4, 3, 1, 2),
    _JnxMvpnSpmsiOrigAddress_Type()
)
jnxMvpnSpmsiOrigAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMvpnSpmsiOrigAddress.setStatus("current")
_JnxMvpnSpmsiCmcastAddrType_Type = InetAddressType
_JnxMvpnSpmsiCmcastAddrType_Object = MibTableColumn
jnxMvpnSpmsiCmcastAddrType = _JnxMvpnSpmsiCmcastAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 4, 3, 1, 3),
    _JnxMvpnSpmsiCmcastAddrType_Type()
)
jnxMvpnSpmsiCmcastAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMvpnSpmsiCmcastAddrType.setStatus("current")
_JnxMvpnSpmsiCmcastGroup_Type = InetAddress
_JnxMvpnSpmsiCmcastGroup_Object = MibTableColumn
jnxMvpnSpmsiCmcastGroup = _JnxMvpnSpmsiCmcastGroup_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 4, 3, 1, 4),
    _JnxMvpnSpmsiCmcastGroup_Type()
)
jnxMvpnSpmsiCmcastGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMvpnSpmsiCmcastGroup.setStatus("current")
_JnxMvpnSpmsiCmcastGroupPrefixLen_Type = Unsigned32
_JnxMvpnSpmsiCmcastGroupPrefixLen_Object = MibTableColumn
jnxMvpnSpmsiCmcastGroupPrefixLen = _JnxMvpnSpmsiCmcastGroupPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 4, 3, 1, 5),
    _JnxMvpnSpmsiCmcastGroupPrefixLen_Type()
)
jnxMvpnSpmsiCmcastGroupPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMvpnSpmsiCmcastGroupPrefixLen.setStatus("current")
_JnxMvpnSpmsiCmcastSource_Type = InetAddress
_JnxMvpnSpmsiCmcastSource_Object = MibTableColumn
jnxMvpnSpmsiCmcastSource = _JnxMvpnSpmsiCmcastSource_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 4, 3, 1, 6),
    _JnxMvpnSpmsiCmcastSource_Type()
)
jnxMvpnSpmsiCmcastSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMvpnSpmsiCmcastSource.setStatus("current")
_JnxMvpnSpmsiCmcastSourcePrefixLen_Type = Unsigned32
_JnxMvpnSpmsiCmcastSourcePrefixLen_Object = MibTableColumn
jnxMvpnSpmsiCmcastSourcePrefixLen = _JnxMvpnSpmsiCmcastSourcePrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 4, 3, 1, 7),
    _JnxMvpnSpmsiCmcastSourcePrefixLen_Type()
)
jnxMvpnSpmsiCmcastSourcePrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMvpnSpmsiCmcastSourcePrefixLen.setStatus("current")
_JnxMvpnSpmsiTunnelAttribute_Type = RowPointer
_JnxMvpnSpmsiTunnelAttribute_Object = MibTableColumn
jnxMvpnSpmsiTunnelAttribute = _JnxMvpnSpmsiTunnelAttribute_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 4, 3, 1, 8),
    _JnxMvpnSpmsiTunnelAttribute_Type()
)
jnxMvpnSpmsiTunnelAttribute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMvpnSpmsiTunnelAttribute.setStatus("current")
_JnxMvpnSpmsiUpTime_Type = TimeInterval
_JnxMvpnSpmsiUpTime_Object = MibTableColumn
jnxMvpnSpmsiUpTime = _JnxMvpnSpmsiUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 4, 3, 1, 9),
    _JnxMvpnSpmsiUpTime_Type()
)
jnxMvpnSpmsiUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMvpnSpmsiUpTime.setStatus("current")
_JnxMvpnSpmsiExpTime_Type = TimeInterval
_JnxMvpnSpmsiExpTime_Object = MibTableColumn
jnxMvpnSpmsiExpTime = _JnxMvpnSpmsiExpTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 4, 3, 1, 10),
    _JnxMvpnSpmsiExpTime_Type()
)
jnxMvpnSpmsiExpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMvpnSpmsiExpTime.setStatus("current")
_JnxMvpnSpmsiRefCnt_Type = Unsigned32
_JnxMvpnSpmsiRefCnt_Object = MibTableColumn
jnxMvpnSpmsiRefCnt = _JnxMvpnSpmsiRefCnt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 4, 3, 1, 11),
    _JnxMvpnSpmsiRefCnt_Type()
)
jnxMvpnSpmsiRefCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMvpnSpmsiRefCnt.setStatus("current")
_JnxMvpnMrouteTable_Object = MibTable
jnxMvpnMrouteTable = _JnxMvpnMrouteTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 4, 4)
)
if mibBuilder.loadTexts:
    jnxMvpnMrouteTable.setStatus("current")
_JnxMvpnMrouteEntry_Object = MibTableRow
jnxMvpnMrouteEntry = _JnxMvpnMrouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 4, 4, 1)
)
if mibBuilder.loadTexts:
    jnxMvpnMrouteEntry.setStatus("current")
_JnxMvpnMroutePmsiPointer_Type = RowPointer
_JnxMvpnMroutePmsiPointer_Object = MibTableColumn
jnxMvpnMroutePmsiPointer = _JnxMvpnMroutePmsiPointer_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 4, 4, 1, 1),
    _JnxMvpnMroutePmsiPointer_Type()
)
jnxMvpnMroutePmsiPointer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMvpnMroutePmsiPointer.setStatus("current")
_JnxMvpnMrouteNumberOfLocalReplication_Type = Unsigned32
_JnxMvpnMrouteNumberOfLocalReplication_Object = MibTableColumn
jnxMvpnMrouteNumberOfLocalReplication = _JnxMvpnMrouteNumberOfLocalReplication_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 4, 4, 1, 2),
    _JnxMvpnMrouteNumberOfLocalReplication_Type()
)
jnxMvpnMrouteNumberOfLocalReplication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMvpnMrouteNumberOfLocalReplication.setStatus("current")
_JnxMvpnMrouteNumberOfRemoteReplication_Type = Unsigned32
_JnxMvpnMrouteNumberOfRemoteReplication_Object = MibTableColumn
jnxMvpnMrouteNumberOfRemoteReplication = _JnxMvpnMrouteNumberOfRemoteReplication_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 4, 4, 1, 3),
    _JnxMvpnMrouteNumberOfRemoteReplication_Type()
)
jnxMvpnMrouteNumberOfRemoteReplication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMvpnMrouteNumberOfRemoteReplication.setStatus("current")


class _JnxMvpnMrouteDataRate_Type(Unsigned32):
    """Custom type jnxMvpnMrouteDataRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_JnxMvpnMrouteDataRate_Type.__name__ = "Unsigned32"
_JnxMvpnMrouteDataRate_Object = MibTableColumn
jnxMvpnMrouteDataRate = _JnxMvpnMrouteDataRate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 1, 4, 4, 1, 4),
    _JnxMvpnMrouteDataRate_Type()
)
jnxMvpnMrouteDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMvpnMrouteDataRate.setStatus("current")
if mibBuilder.loadTexts:
    jnxMvpnMrouteDataRate.setUnits("kilobits per second")
jnxMvpnGeneralEntry.registerAugmentions(
    ("MCAST-VPN-MIB",
     "jnxMvpnBgpGeneralEntry")
)
jnxMvpnBgpGeneralEntry.setIndexNames(*jnxMvpnGeneralEntry.getIndexNames())
ipMRouteEntry.registerAugmentions(
    ("MCAST-VPN-MIB",
     "jnxMvpnMrouteEntry")
)
jnxMvpnMrouteEntry.setIndexNames(*ipMRouteEntry.getIndexNames())

# Managed Objects groups


# Notification objects

jnxMvpnMvrfChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 5, 12, 1, 0, 2)
)
jnxMvpnMvrfChange.setObjects(
    ("MCAST-VPN-MIB", "jnxMvpnGenOperStatusChange")
)
if mibBuilder.loadTexts:
    jnxMvpnMvrfChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MCAST-VPN-MIB",
    **{"jnxMvpnMIB": jnxMvpnMIB,
       "jnxMvpnNotifications": jnxMvpnNotifications,
       "jnxMvpnMvrfChange": jnxMvpnMvrfChange,
       "jnxMvpnObjects": jnxMvpnObjects,
       "jnxMvpnScalars": jnxMvpnScalars,
       "jnxMvpnMvrfNumber": jnxMvpnMvrfNumber,
       "jnxMvpnMvrfNumberV4": jnxMvpnMvrfNumberV4,
       "jnxMvpnMvrfNumberV6": jnxMvpnMvrfNumberV6,
       "jnxMvpnMvrfNumberPimV4": jnxMvpnMvrfNumberPimV4,
       "jnxMvpnMvrfNumberPimV6": jnxMvpnMvrfNumberPimV6,
       "jnxMvpnMvrfNumberBgpV4": jnxMvpnMvrfNumberBgpV4,
       "jnxMvpnMvrfNumberBgpV6": jnxMvpnMvrfNumberBgpV6,
       "jnxMvpnMvrfNumberMldp": jnxMvpnMvrfNumberMldp,
       "jnxMvpnNotificationEnable": jnxMvpnNotificationEnable,
       "jnxMvpnGeneral": jnxMvpnGeneral,
       "jnxMvpnGeneralTable": jnxMvpnGeneralTable,
       "jnxMvpnGeneralEntry": jnxMvpnGeneralEntry,
       "jnxMvpnGenOperStatusChange": jnxMvpnGenOperStatusChange,
       "jnxMvpnGenOperChangeTime": jnxMvpnGenOperChangeTime,
       "jnxMvpnGenCmcastRouteProtocolV4": jnxMvpnGenCmcastRouteProtocolV4,
       "jnxMvpnGenCmcastRouteProtocolV6": jnxMvpnGenCmcastRouteProtocolV6,
       "jnxMvpnGenIpmsiConfigV4": jnxMvpnGenIpmsiConfigV4,
       "jnxMvpnGenIpmsiConfigV6": jnxMvpnGenIpmsiConfigV6,
       "jnxMvpnGenInterAsPmsiConfigV4": jnxMvpnGenInterAsPmsiConfigV4,
       "jnxMvpnGenInterAsPmsiConfigV6": jnxMvpnGenInterAsPmsiConfigV6,
       "jnxMvpnGenRowStatus": jnxMvpnGenRowStatus,
       "jnxMvpnBgpGeneralTable": jnxMvpnBgpGeneralTable,
       "jnxMvpnBgpGeneralEntry": jnxMvpnBgpGeneralEntry,
       "jnxMvpnBgpGenMode": jnxMvpnBgpGenMode,
       "jnxMvpnBgpGenUmhSelection": jnxMvpnBgpGenUmhSelection,
       "jnxMvpnBgpGenSiteType": jnxMvpnBgpGenSiteType,
       "jnxMvpnBgpGenCmcastImportRt": jnxMvpnBgpGenCmcastImportRt,
       "jnxMvpnBgpGenSrcAs": jnxMvpnBgpGenSrcAs,
       "jnxMvpnBgpGenSptnlLimit": jnxMvpnBgpGenSptnlLimit,
       "jnxMvpnConfig": jnxMvpnConfig,
       "jnxMvpnPmsiConfigTable": jnxMvpnPmsiConfigTable,
       "jnxMvpnPmsiConfigEntry": jnxMvpnPmsiConfigEntry,
       "jnxMvpnPmsiConfigTunnelType": jnxMvpnPmsiConfigTunnelType,
       "jnxMvpnPmsiConfigTunnelAuxInfo": jnxMvpnPmsiConfigTunnelAuxInfo,
       "jnxMvpnPmsiConfigTunnelPimGroupAddressType": jnxMvpnPmsiConfigTunnelPimGroupAddressType,
       "jnxMvpnPmsiConfigTunnelPimGroupAddress": jnxMvpnPmsiConfigTunnelPimGroupAddress,
       "jnxMvpnPmsiConfigTunnelOrTemplateName": jnxMvpnPmsiConfigTunnelOrTemplateName,
       "jnxMvpnPmsiConfigEncapsType": jnxMvpnPmsiConfigEncapsType,
       "jnxMvpnPmsiConfigRowStatus": jnxMvpnPmsiConfigRowStatus,
       "jnxMvpnSpmsiConfigTable": jnxMvpnSpmsiConfigTable,
       "jnxMvpnSpmsiConfigEntry": jnxMvpnSpmsiConfigEntry,
       "jnxMvpnSpmsiConfigCmcastAddressType": jnxMvpnSpmsiConfigCmcastAddressType,
       "jnxMvpnSpmsiConfigCmcastGroupAddress": jnxMvpnSpmsiConfigCmcastGroupAddress,
       "jnxMvpnSpmsiConfigCmcastGroupPrefixLen": jnxMvpnSpmsiConfigCmcastGroupPrefixLen,
       "jnxMvpnSpmsiConfigCmcastSourceAddress": jnxMvpnSpmsiConfigCmcastSourceAddress,
       "jnxMvpnSpmsiConfigCmcastSourcePrefixLen": jnxMvpnSpmsiConfigCmcastSourcePrefixLen,
       "jnxMvpnSpmsiConfigThreshold": jnxMvpnSpmsiConfigThreshold,
       "jnxMvpnSpmsiConfigPmsiPointer": jnxMvpnSpmsiConfigPmsiPointer,
       "jnxMvpnSpmsiConfigRowStatus": jnxMvpnSpmsiConfigRowStatus,
       "jnxMvpnStates": jnxMvpnStates,
       "jnxMvpnIpmsiTable": jnxMvpnIpmsiTable,
       "jnxMvpnIpmsiEntry": jnxMvpnIpmsiEntry,
       "jnxMvpnIpmsiAfi": jnxMvpnIpmsiAfi,
       "jnxMvpnIpmsiRD": jnxMvpnIpmsiRD,
       "jnxMvpnIpmsiOrigAddrType": jnxMvpnIpmsiOrigAddrType,
       "jnxMvpnIpmsiOrigAddress": jnxMvpnIpmsiOrigAddress,
       "jnxMvpnIpmsiUpTime": jnxMvpnIpmsiUpTime,
       "jnxMvpnIpmsiAttribute": jnxMvpnIpmsiAttribute,
       "jnxMvpnInterasIpmsiTable": jnxMvpnInterasIpmsiTable,
       "jnxMvpnInterasIpmsiEntry": jnxMvpnInterasIpmsiEntry,
       "jnxMvpnInterasIpmsiAfi": jnxMvpnInterasIpmsiAfi,
       "jnxMvpnInterasIpmsiRD": jnxMvpnInterasIpmsiRD,
       "jnxMvpnInterasIpmsiSrcAs": jnxMvpnInterasIpmsiSrcAs,
       "jnxMvpnInterasIpmsiAttribute": jnxMvpnInterasIpmsiAttribute,
       "jnxMvpnSpmsiTable": jnxMvpnSpmsiTable,
       "jnxMvpnSpmsiEntry": jnxMvpnSpmsiEntry,
       "jnxMvpnSpmsiOrigAddrType": jnxMvpnSpmsiOrigAddrType,
       "jnxMvpnSpmsiOrigAddress": jnxMvpnSpmsiOrigAddress,
       "jnxMvpnSpmsiCmcastAddrType": jnxMvpnSpmsiCmcastAddrType,
       "jnxMvpnSpmsiCmcastGroup": jnxMvpnSpmsiCmcastGroup,
       "jnxMvpnSpmsiCmcastGroupPrefixLen": jnxMvpnSpmsiCmcastGroupPrefixLen,
       "jnxMvpnSpmsiCmcastSource": jnxMvpnSpmsiCmcastSource,
       "jnxMvpnSpmsiCmcastSourcePrefixLen": jnxMvpnSpmsiCmcastSourcePrefixLen,
       "jnxMvpnSpmsiTunnelAttribute": jnxMvpnSpmsiTunnelAttribute,
       "jnxMvpnSpmsiUpTime": jnxMvpnSpmsiUpTime,
       "jnxMvpnSpmsiExpTime": jnxMvpnSpmsiExpTime,
       "jnxMvpnSpmsiRefCnt": jnxMvpnSpmsiRefCnt,
       "jnxMvpnMrouteTable": jnxMvpnMrouteTable,
       "jnxMvpnMrouteEntry": jnxMvpnMrouteEntry,
       "jnxMvpnMroutePmsiPointer": jnxMvpnMroutePmsiPointer,
       "jnxMvpnMrouteNumberOfLocalReplication": jnxMvpnMrouteNumberOfLocalReplication,
       "jnxMvpnMrouteNumberOfRemoteReplication": jnxMvpnMrouteNumberOfRemoteReplication,
       "jnxMvpnMrouteDataRate": jnxMvpnMrouteDataRate}
)
