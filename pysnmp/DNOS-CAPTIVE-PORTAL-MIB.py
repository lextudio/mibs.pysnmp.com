# SNMP MIB module (DNOS-CAPTIVE-PORTAL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DNOS-CAPTIVE-PORTAL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:31:51 2024
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

(dnOS,) = mibBuilder.importSymbols(
    "DELL-REF-MIB",
    "dnOS")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 MacAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

fastPathCaptivePortal = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38)
)
fastPathCaptivePortal.setRevisions(
        ("2011-01-26 00:00",
         "2007-07-09 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CpCaptivePortalIntfCapabilitiesMap(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_CpConfigGroup_ObjectIdentity = ObjectIdentity
cpConfigGroup = _CpConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 1)
)
_CpGlobalConfigGroup_ObjectIdentity = ObjectIdentity
cpGlobalConfigGroup = _CpGlobalConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 1, 1)
)


class _CpAdminMode_Type(Integer32):
    """Custom type cpAdminMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_CpAdminMode_Type.__name__ = "Integer32"
_CpAdminMode_Object = MibScalar
cpAdminMode = _CpAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 1, 1, 1),
    _CpAdminMode_Type()
)
cpAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpAdminMode.setStatus("current")


class _CpAdditionalHttpPort_Type(Integer32):
    """Custom type cpAdditionalHttpPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpAdditionalHttpPort_Type.__name__ = "Integer32"
_CpAdditionalHttpPort_Object = MibScalar
cpAdditionalHttpPort = _CpAdditionalHttpPort_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 1, 1, 2),
    _CpAdditionalHttpPort_Type()
)
cpAdditionalHttpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpAdditionalHttpPort.setStatus("current")


class _CpAdditionalHttpSecurePort_Type(Integer32):
    """Custom type cpAdditionalHttpSecurePort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpAdditionalHttpSecurePort_Type.__name__ = "Integer32"
_CpAdditionalHttpSecurePort_Object = MibScalar
cpAdditionalHttpSecurePort = _CpAdditionalHttpSecurePort_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 1, 1, 3),
    _CpAdditionalHttpSecurePort_Type()
)
cpAdditionalHttpSecurePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpAdditionalHttpSecurePort.setStatus("current")


class _CpPeerStatsReportingInterval_Type(Integer32):
    """Custom type cpPeerStatsReportingInterval based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(15, 3600),
    )


_CpPeerStatsReportingInterval_Type.__name__ = "Integer32"
_CpPeerStatsReportingInterval_Object = MibScalar
cpPeerStatsReportingInterval = _CpPeerStatsReportingInterval_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 1, 1, 4),
    _CpPeerStatsReportingInterval_Type()
)
cpPeerStatsReportingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpPeerStatsReportingInterval.setStatus("current")


class _CpAuthTimeout_Type(Integer32):
    """Custom type cpAuthTimeout based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 600),
    )


_CpAuthTimeout_Type.__name__ = "Integer32"
_CpAuthTimeout_Object = MibScalar
cpAuthTimeout = _CpAuthTimeout_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 1, 1, 5),
    _CpAuthTimeout_Type()
)
cpAuthTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpAuthTimeout.setStatus("current")
_CpCaptivePortalConfigGroup_ObjectIdentity = ObjectIdentity
cpCaptivePortalConfigGroup = _CpCaptivePortalConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 1, 2)
)
_CpCaptivePortalTable_Object = MibTable
cpCaptivePortalTable = _CpCaptivePortalTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cpCaptivePortalTable.setStatus("current")
_CpCaptivePortalEntry_Object = MibTableRow
cpCaptivePortalEntry = _CpCaptivePortalEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 1, 2, 1, 1)
)
cpCaptivePortalEntry.setIndexNames(
    (0, "DNOS-CAPTIVE-PORTAL-MIB", "cpCaptivePortalInstanceId"),
)
if mibBuilder.loadTexts:
    cpCaptivePortalEntry.setStatus("current")
_CpCaptivePortalInstanceId_Type = Unsigned32
_CpCaptivePortalInstanceId_Object = MibTableColumn
cpCaptivePortalInstanceId = _CpCaptivePortalInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 1, 2, 1, 1, 1),
    _CpCaptivePortalInstanceId_Type()
)
cpCaptivePortalInstanceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpCaptivePortalInstanceId.setStatus("current")


class _CpCaptivePortalConfigName_Type(DisplayString):
    """Custom type cpCaptivePortalConfigName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CpCaptivePortalConfigName_Type.__name__ = "DisplayString"
_CpCaptivePortalConfigName_Object = MibTableColumn
cpCaptivePortalConfigName = _CpCaptivePortalConfigName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 1, 2, 1, 1, 2),
    _CpCaptivePortalConfigName_Type()
)
cpCaptivePortalConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpCaptivePortalConfigName.setStatus("current")


class _CpCaptivePortalAdminMode_Type(Integer32):
    """Custom type cpCaptivePortalAdminMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_CpCaptivePortalAdminMode_Type.__name__ = "Integer32"
_CpCaptivePortalAdminMode_Object = MibTableColumn
cpCaptivePortalAdminMode = _CpCaptivePortalAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 1, 2, 1, 1, 3),
    _CpCaptivePortalAdminMode_Type()
)
cpCaptivePortalAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpCaptivePortalAdminMode.setStatus("current")


class _CpCaptivePortalProtocolMode_Type(Integer32):
    """Custom type cpCaptivePortalProtocolMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("http", 1),
          ("https", 0))
    )


_CpCaptivePortalProtocolMode_Type.__name__ = "Integer32"
_CpCaptivePortalProtocolMode_Object = MibTableColumn
cpCaptivePortalProtocolMode = _CpCaptivePortalProtocolMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 1, 2, 1, 1, 4),
    _CpCaptivePortalProtocolMode_Type()
)
cpCaptivePortalProtocolMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpCaptivePortalProtocolMode.setStatus("current")


class _CpCaptivePortalVerificationMode_Type(Integer32):
    """Custom type cpCaptivePortalVerificationMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("guest", 0),
          ("local", 1),
          ("radius", 2))
    )


_CpCaptivePortalVerificationMode_Type.__name__ = "Integer32"
_CpCaptivePortalVerificationMode_Object = MibTableColumn
cpCaptivePortalVerificationMode = _CpCaptivePortalVerificationMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 1, 2, 1, 1, 5),
    _CpCaptivePortalVerificationMode_Type()
)
cpCaptivePortalVerificationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpCaptivePortalVerificationMode.setStatus("current")


class _CpCaptivePortalUserGroup_Type(Unsigned32):
    """Custom type cpCaptivePortalUserGroup based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CpCaptivePortalUserGroup_Type.__name__ = "Unsigned32"
_CpCaptivePortalUserGroup_Object = MibTableColumn
cpCaptivePortalUserGroup = _CpCaptivePortalUserGroup_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 1, 2, 1, 1, 6),
    _CpCaptivePortalUserGroup_Type()
)
cpCaptivePortalUserGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpCaptivePortalUserGroup.setStatus("current")


class _CpCaptivePortalURLRedirectMode_Type(Integer32):
    """Custom type cpCaptivePortalURLRedirectMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_CpCaptivePortalURLRedirectMode_Type.__name__ = "Integer32"
_CpCaptivePortalURLRedirectMode_Object = MibTableColumn
cpCaptivePortalURLRedirectMode = _CpCaptivePortalURLRedirectMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 1, 2, 1, 1, 7),
    _CpCaptivePortalURLRedirectMode_Type()
)
cpCaptivePortalURLRedirectMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpCaptivePortalURLRedirectMode.setStatus("current")


class _CpCaptivePortalRedirectURL_Type(DisplayString):
    """Custom type cpCaptivePortalRedirectURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_CpCaptivePortalRedirectURL_Type.__name__ = "DisplayString"
_CpCaptivePortalRedirectURL_Object = MibTableColumn
cpCaptivePortalRedirectURL = _CpCaptivePortalRedirectURL_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 1, 2, 1, 1, 8),
    _CpCaptivePortalRedirectURL_Type()
)
cpCaptivePortalRedirectURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpCaptivePortalRedirectURL.setStatus("current")


class _CpCaptivePortalSessionTimeout_Type(Unsigned32):
    """Custom type cpCaptivePortalSessionTimeout based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_CpCaptivePortalSessionTimeout_Type.__name__ = "Unsigned32"
_CpCaptivePortalSessionTimeout_Object = MibTableColumn
cpCaptivePortalSessionTimeout = _CpCaptivePortalSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 1, 2, 1, 1, 9),
    _CpCaptivePortalSessionTimeout_Type()
)
cpCaptivePortalSessionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpCaptivePortalSessionTimeout.setStatus("current")


class _CpCaptivePortalIdleTimeout_Type(Unsigned32):
    """Custom type cpCaptivePortalIdleTimeout based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_CpCaptivePortalIdleTimeout_Type.__name__ = "Unsigned32"
_CpCaptivePortalIdleTimeout_Object = MibTableColumn
cpCaptivePortalIdleTimeout = _CpCaptivePortalIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 1, 2, 1, 1, 10),
    _CpCaptivePortalIdleTimeout_Type()
)
cpCaptivePortalIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpCaptivePortalIdleTimeout.setStatus("current")


class _CpCaptivePortalRadiusAuthServer_Type(DisplayString):
    """Custom type cpCaptivePortalRadiusAuthServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CpCaptivePortalRadiusAuthServer_Type.__name__ = "DisplayString"
_CpCaptivePortalRadiusAuthServer_Object = MibTableColumn
cpCaptivePortalRadiusAuthServer = _CpCaptivePortalRadiusAuthServer_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 1, 2, 1, 1, 11),
    _CpCaptivePortalRadiusAuthServer_Type()
)
cpCaptivePortalRadiusAuthServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpCaptivePortalRadiusAuthServer.setStatus("current")


class _CpCaptivePortalMaxBandwidthUp_Type(Unsigned32):
    """Custom type cpCaptivePortalMaxBandwidthUp based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 536870911),
    )


_CpCaptivePortalMaxBandwidthUp_Type.__name__ = "Unsigned32"
_CpCaptivePortalMaxBandwidthUp_Object = MibTableColumn
cpCaptivePortalMaxBandwidthUp = _CpCaptivePortalMaxBandwidthUp_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 1, 2, 1, 1, 12),
    _CpCaptivePortalMaxBandwidthUp_Type()
)
cpCaptivePortalMaxBandwidthUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpCaptivePortalMaxBandwidthUp.setStatus("current")


class _CpCaptivePortalMaxBandwidthDown_Type(Unsigned32):
    """Custom type cpCaptivePortalMaxBandwidthDown based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 536870911),
    )


_CpCaptivePortalMaxBandwidthDown_Type.__name__ = "Unsigned32"
_CpCaptivePortalMaxBandwidthDown_Object = MibTableColumn
cpCaptivePortalMaxBandwidthDown = _CpCaptivePortalMaxBandwidthDown_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 1, 2, 1, 1, 13),
    _CpCaptivePortalMaxBandwidthDown_Type()
)
cpCaptivePortalMaxBandwidthDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpCaptivePortalMaxBandwidthDown.setStatus("current")


class _CpCaptivePortalMaxInputOctets_Type(Unsigned32):
    """Custom type cpCaptivePortalMaxInputOctets based on Unsigned32"""
    defaultValue = 0


_CpCaptivePortalMaxInputOctets_Object = MibTableColumn
cpCaptivePortalMaxInputOctets = _CpCaptivePortalMaxInputOctets_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 1, 2, 1, 1, 14),
    _CpCaptivePortalMaxInputOctets_Type()
)
cpCaptivePortalMaxInputOctets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpCaptivePortalMaxInputOctets.setStatus("current")


class _CpCaptivePortalMaxOutputOctets_Type(Unsigned32):
    """Custom type cpCaptivePortalMaxOutputOctets based on Unsigned32"""
    defaultValue = 0


_CpCaptivePortalMaxOutputOctets_Object = MibTableColumn
cpCaptivePortalMaxOutputOctets = _CpCaptivePortalMaxOutputOctets_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 1, 2, 1, 1, 15),
    _CpCaptivePortalMaxOutputOctets_Type()
)
cpCaptivePortalMaxOutputOctets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpCaptivePortalMaxOutputOctets.setStatus("current")


class _CpCaptivePortalMaxTotalOctets_Type(Unsigned32):
    """Custom type cpCaptivePortalMaxTotalOctets based on Unsigned32"""
    defaultValue = 0


_CpCaptivePortalMaxTotalOctets_Object = MibTableColumn
cpCaptivePortalMaxTotalOctets = _CpCaptivePortalMaxTotalOctets_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 1, 2, 1, 1, 16),
    _CpCaptivePortalMaxTotalOctets_Type()
)
cpCaptivePortalMaxTotalOctets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpCaptivePortalMaxTotalOctets.setStatus("current")


class _CpCaptivePortalUserLogoutMode_Type(Integer32):
    """Custom type cpCaptivePortalUserLogoutMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_CpCaptivePortalUserLogoutMode_Type.__name__ = "Integer32"
_CpCaptivePortalUserLogoutMode_Object = MibTableColumn
cpCaptivePortalUserLogoutMode = _CpCaptivePortalUserLogoutMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 1, 2, 1, 1, 17),
    _CpCaptivePortalUserLogoutMode_Type()
)
cpCaptivePortalUserLogoutMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpCaptivePortalUserLogoutMode.setStatus("current")
_CpCaptivePortalRowStatus_Type = RowStatus
_CpCaptivePortalRowStatus_Object = MibTableColumn
cpCaptivePortalRowStatus = _CpCaptivePortalRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 1, 2, 1, 1, 18),
    _CpCaptivePortalRowStatus_Type()
)
cpCaptivePortalRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpCaptivePortalRowStatus.setStatus("current")
_CpLocalUserDatabaseGroup_ObjectIdentity = ObjectIdentity
cpLocalUserDatabaseGroup = _CpLocalUserDatabaseGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 1, 3)
)
_CpLocalUserGroupTable_Object = MibTable
cpLocalUserGroupTable = _CpLocalUserGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cpLocalUserGroupTable.setStatus("current")
_CpLocalUserGroupEntry_Object = MibTableRow
cpLocalUserGroupEntry = _CpLocalUserGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 1, 3, 1, 1)
)
cpLocalUserGroupEntry.setIndexNames(
    (0, "DNOS-CAPTIVE-PORTAL-MIB", "cpLocalUserGroupIndex"),
)
if mibBuilder.loadTexts:
    cpLocalUserGroupEntry.setStatus("current")


class _CpLocalUserGroupIndex_Type(Integer32):
    """Custom type cpLocalUserGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CpLocalUserGroupIndex_Type.__name__ = "Integer32"
_CpLocalUserGroupIndex_Object = MibTableColumn
cpLocalUserGroupIndex = _CpLocalUserGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 1, 3, 1, 1, 1),
    _CpLocalUserGroupIndex_Type()
)
cpLocalUserGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpLocalUserGroupIndex.setStatus("current")


class _CpLocalUserGroupName_Type(DisplayString):
    """Custom type cpLocalUserGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CpLocalUserGroupName_Type.__name__ = "DisplayString"
_CpLocalUserGroupName_Object = MibTableColumn
cpLocalUserGroupName = _CpLocalUserGroupName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 1, 3, 1, 1, 2),
    _CpLocalUserGroupName_Type()
)
cpLocalUserGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpLocalUserGroupName.setStatus("current")
_CpLocalUserGroupRowStatus_Type = RowStatus
_CpLocalUserGroupRowStatus_Object = MibTableColumn
cpLocalUserGroupRowStatus = _CpLocalUserGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 1, 3, 1, 1, 3),
    _CpLocalUserGroupRowStatus_Type()
)
cpLocalUserGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpLocalUserGroupRowStatus.setStatus("current")
_CpLocalUserTable_Object = MibTable
cpLocalUserTable = _CpLocalUserTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cpLocalUserTable.setStatus("current")
_CpLocalUserEntry_Object = MibTableRow
cpLocalUserEntry = _CpLocalUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 1, 3, 2, 1)
)
cpLocalUserEntry.setIndexNames(
    (0, "DNOS-CAPTIVE-PORTAL-MIB", "cpLocalUserIndex"),
)
if mibBuilder.loadTexts:
    cpLocalUserEntry.setStatus("current")


class _CpLocalUserIndex_Type(Integer32):
    """Custom type cpLocalUserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CpLocalUserIndex_Type.__name__ = "Integer32"
_CpLocalUserIndex_Object = MibTableColumn
cpLocalUserIndex = _CpLocalUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 1, 3, 2, 1, 1),
    _CpLocalUserIndex_Type()
)
cpLocalUserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpLocalUserIndex.setStatus("current")


class _CpLocalUserName_Type(DisplayString):
    """Custom type cpLocalUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CpLocalUserName_Type.__name__ = "DisplayString"
_CpLocalUserName_Object = MibTableColumn
cpLocalUserName = _CpLocalUserName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 1, 3, 2, 1, 2),
    _CpLocalUserName_Type()
)
cpLocalUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpLocalUserName.setStatus("current")


class _CpLocalUserPassword_Type(DisplayString):
    """Custom type cpLocalUserPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 64),
    )


_CpLocalUserPassword_Type.__name__ = "DisplayString"
_CpLocalUserPassword_Object = MibTableColumn
cpLocalUserPassword = _CpLocalUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 1, 3, 2, 1, 3),
    _CpLocalUserPassword_Type()
)
cpLocalUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpLocalUserPassword.setStatus("current")


class _CpLocalUserSessionTimeout_Type(Unsigned32):
    """Custom type cpLocalUserSessionTimeout based on Unsigned32"""
    defaultValue = 0


_CpLocalUserSessionTimeout_Object = MibTableColumn
cpLocalUserSessionTimeout = _CpLocalUserSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 1, 3, 2, 1, 4),
    _CpLocalUserSessionTimeout_Type()
)
cpLocalUserSessionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpLocalUserSessionTimeout.setStatus("current")


class _CpLocalUserIdleTimeout_Type(Unsigned32):
    """Custom type cpLocalUserIdleTimeout based on Unsigned32"""
    defaultValue = 0


_CpLocalUserIdleTimeout_Object = MibTableColumn
cpLocalUserIdleTimeout = _CpLocalUserIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 1, 3, 2, 1, 5),
    _CpLocalUserIdleTimeout_Type()
)
cpLocalUserIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpLocalUserIdleTimeout.setStatus("current")


class _CpLocalUserMaxBandwidthUp_Type(Unsigned32):
    """Custom type cpLocalUserMaxBandwidthUp based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 536870911),
    )


_CpLocalUserMaxBandwidthUp_Type.__name__ = "Unsigned32"
_CpLocalUserMaxBandwidthUp_Object = MibTableColumn
cpLocalUserMaxBandwidthUp = _CpLocalUserMaxBandwidthUp_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 1, 3, 2, 1, 6),
    _CpLocalUserMaxBandwidthUp_Type()
)
cpLocalUserMaxBandwidthUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpLocalUserMaxBandwidthUp.setStatus("current")


class _CpLocalUserMaxBandwidthDown_Type(Unsigned32):
    """Custom type cpLocalUserMaxBandwidthDown based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 536870911),
    )


_CpLocalUserMaxBandwidthDown_Type.__name__ = "Unsigned32"
_CpLocalUserMaxBandwidthDown_Object = MibTableColumn
cpLocalUserMaxBandwidthDown = _CpLocalUserMaxBandwidthDown_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 1, 3, 2, 1, 7),
    _CpLocalUserMaxBandwidthDown_Type()
)
cpLocalUserMaxBandwidthDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpLocalUserMaxBandwidthDown.setStatus("current")


class _CpLocalUserMaxInputOctets_Type(Unsigned32):
    """Custom type cpLocalUserMaxInputOctets based on Unsigned32"""
    defaultValue = 0


_CpLocalUserMaxInputOctets_Object = MibTableColumn
cpLocalUserMaxInputOctets = _CpLocalUserMaxInputOctets_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 1, 3, 2, 1, 8),
    _CpLocalUserMaxInputOctets_Type()
)
cpLocalUserMaxInputOctets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpLocalUserMaxInputOctets.setStatus("current")


class _CpLocalUserMaxOutputOctets_Type(Unsigned32):
    """Custom type cpLocalUserMaxOutputOctets based on Unsigned32"""
    defaultValue = 0


_CpLocalUserMaxOutputOctets_Object = MibTableColumn
cpLocalUserMaxOutputOctets = _CpLocalUserMaxOutputOctets_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 1, 3, 2, 1, 9),
    _CpLocalUserMaxOutputOctets_Type()
)
cpLocalUserMaxOutputOctets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpLocalUserMaxOutputOctets.setStatus("current")


class _CpLocalUserMaxTotalOctets_Type(Unsigned32):
    """Custom type cpLocalUserMaxTotalOctets based on Unsigned32"""
    defaultValue = 0


_CpLocalUserMaxTotalOctets_Object = MibTableColumn
cpLocalUserMaxTotalOctets = _CpLocalUserMaxTotalOctets_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 1, 3, 2, 1, 10),
    _CpLocalUserMaxTotalOctets_Type()
)
cpLocalUserMaxTotalOctets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpLocalUserMaxTotalOctets.setStatus("current")
_CpLocalUserRowStatus_Type = RowStatus
_CpLocalUserRowStatus_Object = MibTableColumn
cpLocalUserRowStatus = _CpLocalUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 1, 3, 2, 1, 11),
    _CpLocalUserRowStatus_Type()
)
cpLocalUserRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpLocalUserRowStatus.setStatus("current")
_CpLocalUserGroupAssociationTable_Object = MibTable
cpLocalUserGroupAssociationTable = _CpLocalUserGroupAssociationTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 1, 3, 3)
)
if mibBuilder.loadTexts:
    cpLocalUserGroupAssociationTable.setStatus("current")
_CpLocalUserGroupAssociationEntry_Object = MibTableRow
cpLocalUserGroupAssociationEntry = _CpLocalUserGroupAssociationEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 1, 3, 3, 1)
)
cpLocalUserGroupAssociationEntry.setIndexNames(
    (0, "DNOS-CAPTIVE-PORTAL-MIB", "cpLocalUserGroupAssociationUserIndex"),
    (0, "DNOS-CAPTIVE-PORTAL-MIB", "cpLocalUserGroupAssociationGroupIndex"),
)
if mibBuilder.loadTexts:
    cpLocalUserGroupAssociationEntry.setStatus("current")


class _CpLocalUserGroupAssociationUserIndex_Type(Integer32):
    """Custom type cpLocalUserGroupAssociationUserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CpLocalUserGroupAssociationUserIndex_Type.__name__ = "Integer32"
_CpLocalUserGroupAssociationUserIndex_Object = MibTableColumn
cpLocalUserGroupAssociationUserIndex = _CpLocalUserGroupAssociationUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 1, 3, 3, 1, 1),
    _CpLocalUserGroupAssociationUserIndex_Type()
)
cpLocalUserGroupAssociationUserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpLocalUserGroupAssociationUserIndex.setStatus("current")


class _CpLocalUserGroupAssociationGroupIndex_Type(Integer32):
    """Custom type cpLocalUserGroupAssociationGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CpLocalUserGroupAssociationGroupIndex_Type.__name__ = "Integer32"
_CpLocalUserGroupAssociationGroupIndex_Object = MibTableColumn
cpLocalUserGroupAssociationGroupIndex = _CpLocalUserGroupAssociationGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 1, 3, 3, 1, 2),
    _CpLocalUserGroupAssociationGroupIndex_Type()
)
cpLocalUserGroupAssociationGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpLocalUserGroupAssociationGroupIndex.setStatus("current")
_CpLocalUserGroupAssociationRowStatus_Type = RowStatus
_CpLocalUserGroupAssociationRowStatus_Object = MibTableColumn
cpLocalUserGroupAssociationRowStatus = _CpLocalUserGroupAssociationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 1, 3, 3, 1, 3),
    _CpLocalUserGroupAssociationRowStatus_Type()
)
cpLocalUserGroupAssociationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpLocalUserGroupAssociationRowStatus.setStatus("current")
_CpInterfaceAssociationGroup_ObjectIdentity = ObjectIdentity
cpInterfaceAssociationGroup = _CpInterfaceAssociationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 1, 4)
)
_CpInterfaceAssociationTable_Object = MibTable
cpInterfaceAssociationTable = _CpInterfaceAssociationTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cpInterfaceAssociationTable.setStatus("current")
_CpInterfaceAssociationEntry_Object = MibTableRow
cpInterfaceAssociationEntry = _CpInterfaceAssociationEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 1, 4, 1, 1)
)
cpInterfaceAssociationEntry.setIndexNames(
    (0, "DNOS-CAPTIVE-PORTAL-MIB", "cpIntfAssociationCPID"),
    (0, "DNOS-CAPTIVE-PORTAL-MIB", "cpIntfAssociationIfIndex"),
)
if mibBuilder.loadTexts:
    cpInterfaceAssociationEntry.setStatus("current")
_CpIntfAssociationCPID_Type = Unsigned32
_CpIntfAssociationCPID_Object = MibTableColumn
cpIntfAssociationCPID = _CpIntfAssociationCPID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 1, 4, 1, 1, 1),
    _CpIntfAssociationCPID_Type()
)
cpIntfAssociationCPID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpIntfAssociationCPID.setStatus("current")
_CpIntfAssociationIfIndex_Type = InterfaceIndex
_CpIntfAssociationIfIndex_Object = MibTableColumn
cpIntfAssociationIfIndex = _CpIntfAssociationIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 1, 4, 1, 1, 2),
    _CpIntfAssociationIfIndex_Type()
)
cpIntfAssociationIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpIntfAssociationIfIndex.setStatus("current")
_CpIntfAssociationRowStatus_Type = RowStatus
_CpIntfAssociationRowStatus_Object = MibTableColumn
cpIntfAssociationRowStatus = _CpIntfAssociationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 1, 4, 1, 1, 3),
    _CpIntfAssociationRowStatus_Type()
)
cpIntfAssociationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpIntfAssociationRowStatus.setStatus("current")
_CpStatusGroup_ObjectIdentity = ObjectIdentity
cpStatusGroup = _CpStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 2)
)
_CpCaptivePortalGlobalStatusGroup_ObjectIdentity = ObjectIdentity
cpCaptivePortalGlobalStatusGroup = _CpCaptivePortalGlobalStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 2, 1)
)


class _CpCaptivePortalOperStatus_Type(Integer32):
    """Custom type cpCaptivePortalOperStatus based on Integer32"""
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
        *(("disablePending", 2),
          ("disabled", 3),
          ("enablePending", 0),
          ("enabled", 1))
    )


_CpCaptivePortalOperStatus_Type.__name__ = "Integer32"
_CpCaptivePortalOperStatus_Object = MibScalar
cpCaptivePortalOperStatus = _CpCaptivePortalOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 2, 1, 1),
    _CpCaptivePortalOperStatus_Type()
)
cpCaptivePortalOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpCaptivePortalOperStatus.setStatus("current")


class _CpCaptivePortalOperDisabledReason_Type(Integer32):
    """Custom type cpCaptivePortalOperDisabledReason based on Integer32"""
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
        *(("adminDisabled", 1),
          ("noIPAddress", 2),
          ("noIPRoutingIntf", 3),
          ("none", 0),
          ("routingDisabled", 4))
    )


_CpCaptivePortalOperDisabledReason_Type.__name__ = "Integer32"
_CpCaptivePortalOperDisabledReason_Object = MibScalar
cpCaptivePortalOperDisabledReason = _CpCaptivePortalOperDisabledReason_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 2, 1, 2),
    _CpCaptivePortalOperDisabledReason_Type()
)
cpCaptivePortalOperDisabledReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpCaptivePortalOperDisabledReason.setStatus("current")
_CpCaptivePortalIpv4Address_Type = IpAddress
_CpCaptivePortalIpv4Address_Object = MibScalar
cpCaptivePortalIpv4Address = _CpCaptivePortalIpv4Address_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 2, 1, 3),
    _CpCaptivePortalIpv4Address_Type()
)
cpCaptivePortalIpv4Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpCaptivePortalIpv4Address.setStatus("current")


class _CpCaptivePortalInstanceMaxCount_Type(Integer32):
    """Custom type cpCaptivePortalInstanceMaxCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_CpCaptivePortalInstanceMaxCount_Type.__name__ = "Integer32"
_CpCaptivePortalInstanceMaxCount_Object = MibScalar
cpCaptivePortalInstanceMaxCount = _CpCaptivePortalInstanceMaxCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 2, 1, 4),
    _CpCaptivePortalInstanceMaxCount_Type()
)
cpCaptivePortalInstanceMaxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpCaptivePortalInstanceMaxCount.setStatus("current")
_CpCaptivePortalInstanceConfiguredCount_Type = Integer32
_CpCaptivePortalInstanceConfiguredCount_Object = MibScalar
cpCaptivePortalInstanceConfiguredCount = _CpCaptivePortalInstanceConfiguredCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 2, 1, 5),
    _CpCaptivePortalInstanceConfiguredCount_Type()
)
cpCaptivePortalInstanceConfiguredCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpCaptivePortalInstanceConfiguredCount.setStatus("current")
_CpCaptivePortalInstanceActiveCount_Type = Integer32
_CpCaptivePortalInstanceActiveCount_Object = MibScalar
cpCaptivePortalInstanceActiveCount = _CpCaptivePortalInstanceActiveCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 2, 1, 6),
    _CpCaptivePortalInstanceActiveCount_Type()
)
cpCaptivePortalInstanceActiveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpCaptivePortalInstanceActiveCount.setStatus("current")


class _CpCaptivePortalAuthenUserMaxCount_Type(Integer32):
    """Custom type cpCaptivePortalAuthenUserMaxCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_CpCaptivePortalAuthenUserMaxCount_Type.__name__ = "Integer32"
_CpCaptivePortalAuthenUserMaxCount_Object = MibScalar
cpCaptivePortalAuthenUserMaxCount = _CpCaptivePortalAuthenUserMaxCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 2, 1, 7),
    _CpCaptivePortalAuthenUserMaxCount_Type()
)
cpCaptivePortalAuthenUserMaxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpCaptivePortalAuthenUserMaxCount.setStatus("current")


class _CpCaptivePortalLocalUserMaxCount_Type(Integer32):
    """Custom type cpCaptivePortalLocalUserMaxCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_CpCaptivePortalLocalUserMaxCount_Type.__name__ = "Integer32"
_CpCaptivePortalLocalUserMaxCount_Object = MibScalar
cpCaptivePortalLocalUserMaxCount = _CpCaptivePortalLocalUserMaxCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 2, 1, 8),
    _CpCaptivePortalLocalUserMaxCount_Type()
)
cpCaptivePortalLocalUserMaxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpCaptivePortalLocalUserMaxCount.setStatus("current")
_CpCaptivePortalConfiguredLocalUserCount_Type = Integer32
_CpCaptivePortalConfiguredLocalUserCount_Object = MibScalar
cpCaptivePortalConfiguredLocalUserCount = _CpCaptivePortalConfiguredLocalUserCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 2, 1, 9),
    _CpCaptivePortalConfiguredLocalUserCount_Type()
)
cpCaptivePortalConfiguredLocalUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpCaptivePortalConfiguredLocalUserCount.setStatus("current")
_CpCaptivePortalAuthenUserCurrentCount_Type = Integer32
_CpCaptivePortalAuthenUserCurrentCount_Object = MibScalar
cpCaptivePortalAuthenUserCurrentCount = _CpCaptivePortalAuthenUserCurrentCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 2, 1, 10),
    _CpCaptivePortalAuthenUserCurrentCount_Type()
)
cpCaptivePortalAuthenUserCurrentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpCaptivePortalAuthenUserCurrentCount.setStatus("current")
_CpCaptivePortalInstanceStatusGroup_ObjectIdentity = ObjectIdentity
cpCaptivePortalInstanceStatusGroup = _CpCaptivePortalInstanceStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 2, 2)
)
_CpCaptivePortalInstanceStatusTable_Object = MibTable
cpCaptivePortalInstanceStatusTable = _CpCaptivePortalInstanceStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cpCaptivePortalInstanceStatusTable.setStatus("current")
_CpCaptivePortalInstanceStatusEntry_Object = MibTableRow
cpCaptivePortalInstanceStatusEntry = _CpCaptivePortalInstanceStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 2, 2, 1, 1)
)
cpCaptivePortalInstanceStatusEntry.setIndexNames(
    (0, "DNOS-CAPTIVE-PORTAL-MIB", "cpCaptivePortalInstanceId"),
)
if mibBuilder.loadTexts:
    cpCaptivePortalInstanceStatusEntry.setStatus("current")


class _CpCaptivePortalInstanceOperStatus_Type(Integer32):
    """Custom type cpCaptivePortalInstanceOperStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_CpCaptivePortalInstanceOperStatus_Type.__name__ = "Integer32"
_CpCaptivePortalInstanceOperStatus_Object = MibTableColumn
cpCaptivePortalInstanceOperStatus = _CpCaptivePortalInstanceOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 2, 2, 1, 1, 1),
    _CpCaptivePortalInstanceOperStatus_Type()
)
cpCaptivePortalInstanceOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpCaptivePortalInstanceOperStatus.setStatus("current")


class _CpCaptivePortalInstanceOperDisabledReason_Type(Integer32):
    """Custom type cpCaptivePortalInstanceOperDisabledReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("adminDisabled", 1),
          ("noAccountingServer", 3),
          ("noActiveIntf", 5),
          ("noIntfAssociation", 4),
          ("noRadiusServer", 2),
          ("noValidCert", 6),
          ("none", 0))
    )


_CpCaptivePortalInstanceOperDisabledReason_Type.__name__ = "Integer32"
_CpCaptivePortalInstanceOperDisabledReason_Object = MibTableColumn
cpCaptivePortalInstanceOperDisabledReason = _CpCaptivePortalInstanceOperDisabledReason_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 2, 2, 1, 1, 2),
    _CpCaptivePortalInstanceOperDisabledReason_Type()
)
cpCaptivePortalInstanceOperDisabledReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpCaptivePortalInstanceOperDisabledReason.setStatus("current")


class _CpCaptivePortalInstanceBlockStatus_Type(Integer32):
    """Custom type cpCaptivePortalInstanceBlockStatus based on Integer32"""
    defaultValue = 3

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
        *(("blockPending", 0),
          ("blocked", 1),
          ("notBlockPending", 2),
          ("notBlocked", 3))
    )


_CpCaptivePortalInstanceBlockStatus_Type.__name__ = "Integer32"
_CpCaptivePortalInstanceBlockStatus_Object = MibTableColumn
cpCaptivePortalInstanceBlockStatus = _CpCaptivePortalInstanceBlockStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 2, 2, 1, 1, 3),
    _CpCaptivePortalInstanceBlockStatus_Type()
)
cpCaptivePortalInstanceBlockStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpCaptivePortalInstanceBlockStatus.setStatus("current")
_CpCaptivePortalInstanceAuthUserCount_Type = Integer32
_CpCaptivePortalInstanceAuthUserCount_Object = MibTableColumn
cpCaptivePortalInstanceAuthUserCount = _CpCaptivePortalInstanceAuthUserCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 2, 2, 1, 1, 4),
    _CpCaptivePortalInstanceAuthUserCount_Type()
)
cpCaptivePortalInstanceAuthUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpCaptivePortalInstanceAuthUserCount.setStatus("current")
_CpCaptivePortalIntfStatusGroup_ObjectIdentity = ObjectIdentity
cpCaptivePortalIntfStatusGroup = _CpCaptivePortalIntfStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 2, 3)
)
_CpCaptivePortalIntfStatusTable_Object = MibTable
cpCaptivePortalIntfStatusTable = _CpCaptivePortalIntfStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 2, 3, 1)
)
if mibBuilder.loadTexts:
    cpCaptivePortalIntfStatusTable.setStatus("current")
_CpCaptivePortalIntfStatusEntry_Object = MibTableRow
cpCaptivePortalIntfStatusEntry = _CpCaptivePortalIntfStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 2, 3, 1, 1)
)
cpCaptivePortalIntfStatusEntry.setIndexNames(
    (0, "DNOS-CAPTIVE-PORTAL-MIB", "cpCaptivePortalInstanceId"),
    (0, "DNOS-CAPTIVE-PORTAL-MIB", "cpCaptivePortalIntfIfIndex"),
)
if mibBuilder.loadTexts:
    cpCaptivePortalIntfStatusEntry.setStatus("current")
_CpCaptivePortalIntfIfIndex_Type = InterfaceIndex
_CpCaptivePortalIntfIfIndex_Object = MibTableColumn
cpCaptivePortalIntfIfIndex = _CpCaptivePortalIntfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 2, 3, 1, 1, 1),
    _CpCaptivePortalIntfIfIndex_Type()
)
cpCaptivePortalIntfIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpCaptivePortalIntfIfIndex.setStatus("current")


class _CpCaptivePortalIntfActivationStatus_Type(Integer32):
    """Custom type cpCaptivePortalIntfActivationStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_CpCaptivePortalIntfActivationStatus_Type.__name__ = "Integer32"
_CpCaptivePortalIntfActivationStatus_Object = MibTableColumn
cpCaptivePortalIntfActivationStatus = _CpCaptivePortalIntfActivationStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 2, 3, 1, 1, 2),
    _CpCaptivePortalIntfActivationStatus_Type()
)
cpCaptivePortalIntfActivationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpCaptivePortalIntfActivationStatus.setStatus("current")


class _CpCaptivePortalIntfActivationDisabledReason_Type(Integer32):
    """Custom type cpCaptivePortalIntfActivationDisabledReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("adminDisabled", 2),
          ("intfNotAttached", 1),
          ("none", 0))
    )


_CpCaptivePortalIntfActivationDisabledReason_Type.__name__ = "Integer32"
_CpCaptivePortalIntfActivationDisabledReason_Object = MibTableColumn
cpCaptivePortalIntfActivationDisabledReason = _CpCaptivePortalIntfActivationDisabledReason_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 2, 3, 1, 1, 3),
    _CpCaptivePortalIntfActivationDisabledReason_Type()
)
cpCaptivePortalIntfActivationDisabledReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpCaptivePortalIntfActivationDisabledReason.setStatus("current")


class _CpCaptivePortalIntfBlockStatus_Type(Integer32):
    """Custom type cpCaptivePortalIntfBlockStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 0),
          ("notBlocked", 1))
    )


_CpCaptivePortalIntfBlockStatus_Type.__name__ = "Integer32"
_CpCaptivePortalIntfBlockStatus_Object = MibTableColumn
cpCaptivePortalIntfBlockStatus = _CpCaptivePortalIntfBlockStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 2, 3, 1, 1, 4),
    _CpCaptivePortalIntfBlockStatus_Type()
)
cpCaptivePortalIntfBlockStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpCaptivePortalIntfBlockStatus.setStatus("current")
_CpCaptivePortalIntfAuthUserCount_Type = Integer32
_CpCaptivePortalIntfAuthUserCount_Object = MibTableColumn
cpCaptivePortalIntfAuthUserCount = _CpCaptivePortalIntfAuthUserCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 2, 3, 1, 1, 5),
    _CpCaptivePortalIntfAuthUserCount_Type()
)
cpCaptivePortalIntfAuthUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpCaptivePortalIntfAuthUserCount.setStatus("current")
_CpCaptivePortalIntfDatabaseGroup_ObjectIdentity = ObjectIdentity
cpCaptivePortalIntfDatabaseGroup = _CpCaptivePortalIntfDatabaseGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 2, 4)
)
_CpCaptivePortalIntfDatabaseTable_Object = MibTable
cpCaptivePortalIntfDatabaseTable = _CpCaptivePortalIntfDatabaseTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 2, 4, 1)
)
if mibBuilder.loadTexts:
    cpCaptivePortalIntfDatabaseTable.setStatus("current")
_CpCaptivePortalIntfDatabaseEntry_Object = MibTableRow
cpCaptivePortalIntfDatabaseEntry = _CpCaptivePortalIntfDatabaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 2, 4, 1, 1)
)
cpCaptivePortalIntfDatabaseEntry.setIndexNames(
    (0, "DNOS-CAPTIVE-PORTAL-MIB", "cpCaptivePortalIntfIfIndex"),
)
if mibBuilder.loadTexts:
    cpCaptivePortalIntfDatabaseEntry.setStatus("current")
_CpCaptivePortalIntfCapabilities_Type = CpCaptivePortalIntfCapabilitiesMap
_CpCaptivePortalIntfCapabilities_Object = MibTableColumn
cpCaptivePortalIntfCapabilities = _CpCaptivePortalIntfCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 2, 4, 1, 1, 1),
    _CpCaptivePortalIntfCapabilities_Type()
)
cpCaptivePortalIntfCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpCaptivePortalIntfCapabilities.setStatus("current")
_CpCaptivePortalClientStatusGroup_ObjectIdentity = ObjectIdentity
cpCaptivePortalClientStatusGroup = _CpCaptivePortalClientStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 2, 5)
)
_CpCaptivePortalClientStatusTable_Object = MibTable
cpCaptivePortalClientStatusTable = _CpCaptivePortalClientStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 2, 5, 1)
)
if mibBuilder.loadTexts:
    cpCaptivePortalClientStatusTable.setStatus("current")
_CpCaptivePortalClientStatusEntry_Object = MibTableRow
cpCaptivePortalClientStatusEntry = _CpCaptivePortalClientStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 2, 5, 1, 1)
)
cpCaptivePortalClientStatusEntry.setIndexNames(
    (0, "DNOS-CAPTIVE-PORTAL-MIB", "cpCaptivePortalClientMacAddress"),
)
if mibBuilder.loadTexts:
    cpCaptivePortalClientStatusEntry.setStatus("current")
_CpCaptivePortalClientMacAddress_Type = MacAddress
_CpCaptivePortalClientMacAddress_Object = MibTableColumn
cpCaptivePortalClientMacAddress = _CpCaptivePortalClientMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 2, 5, 1, 1, 1),
    _CpCaptivePortalClientMacAddress_Type()
)
cpCaptivePortalClientMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpCaptivePortalClientMacAddress.setStatus("current")
_CpCaptivePortalClientIpAddress_Type = IpAddress
_CpCaptivePortalClientIpAddress_Object = MibTableColumn
cpCaptivePortalClientIpAddress = _CpCaptivePortalClientIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 2, 5, 1, 1, 2),
    _CpCaptivePortalClientIpAddress_Type()
)
cpCaptivePortalClientIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpCaptivePortalClientIpAddress.setStatus("current")


class _CpCaptivePortalClientUserName_Type(DisplayString):
    """Custom type cpCaptivePortalClientUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CpCaptivePortalClientUserName_Type.__name__ = "DisplayString"
_CpCaptivePortalClientUserName_Object = MibTableColumn
cpCaptivePortalClientUserName = _CpCaptivePortalClientUserName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 2, 5, 1, 1, 3),
    _CpCaptivePortalClientUserName_Type()
)
cpCaptivePortalClientUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpCaptivePortalClientUserName.setStatus("current")


class _CpCaptivePortalClientProtocolMode_Type(Integer32):
    """Custom type cpCaptivePortalClientProtocolMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("http", 1),
          ("https", 0))
    )


_CpCaptivePortalClientProtocolMode_Type.__name__ = "Integer32"
_CpCaptivePortalClientProtocolMode_Object = MibTableColumn
cpCaptivePortalClientProtocolMode = _CpCaptivePortalClientProtocolMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 2, 5, 1, 1, 4),
    _CpCaptivePortalClientProtocolMode_Type()
)
cpCaptivePortalClientProtocolMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpCaptivePortalClientProtocolMode.setStatus("current")


class _CpCaptivePortalClientVerificationMode_Type(Integer32):
    """Custom type cpCaptivePortalClientVerificationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("guest", 0),
          ("local", 1),
          ("radius", 2))
    )


_CpCaptivePortalClientVerificationMode_Type.__name__ = "Integer32"
_CpCaptivePortalClientVerificationMode_Object = MibTableColumn
cpCaptivePortalClientVerificationMode = _CpCaptivePortalClientVerificationMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 2, 5, 1, 1, 5),
    _CpCaptivePortalClientVerificationMode_Type()
)
cpCaptivePortalClientVerificationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpCaptivePortalClientVerificationMode.setStatus("current")
_CpCaptivePortalClientAssocIfIndex_Type = InterfaceIndex
_CpCaptivePortalClientAssocIfIndex_Object = MibTableColumn
cpCaptivePortalClientAssocIfIndex = _CpCaptivePortalClientAssocIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 2, 5, 1, 1, 6),
    _CpCaptivePortalClientAssocIfIndex_Type()
)
cpCaptivePortalClientAssocIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpCaptivePortalClientAssocIfIndex.setStatus("current")
_CpCaptivePortalClientCPID_Type = Integer32
_CpCaptivePortalClientCPID_Object = MibTableColumn
cpCaptivePortalClientCPID = _CpCaptivePortalClientCPID_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 2, 5, 1, 1, 7),
    _CpCaptivePortalClientCPID_Type()
)
cpCaptivePortalClientCPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpCaptivePortalClientCPID.setStatus("current")
_CpCaptivePortalClientSessionTime_Type = TimeTicks
_CpCaptivePortalClientSessionTime_Object = MibTableColumn
cpCaptivePortalClientSessionTime = _CpCaptivePortalClientSessionTime_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 2, 5, 1, 1, 8),
    _CpCaptivePortalClientSessionTime_Type()
)
cpCaptivePortalClientSessionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpCaptivePortalClientSessionTime.setStatus("current")
_CpCaptivePortalClientSwitchMacAddress_Type = MacAddress
_CpCaptivePortalClientSwitchMacAddress_Object = MibTableColumn
cpCaptivePortalClientSwitchMacAddress = _CpCaptivePortalClientSwitchMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 2, 5, 1, 1, 9),
    _CpCaptivePortalClientSwitchMacAddress_Type()
)
cpCaptivePortalClientSwitchMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpCaptivePortalClientSwitchMacAddress.setStatus("current")
_CpCaptivePortalClientSwitchIpAddress_Type = IpAddress
_CpCaptivePortalClientSwitchIpAddress_Object = MibTableColumn
cpCaptivePortalClientSwitchIpAddress = _CpCaptivePortalClientSwitchIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 2, 5, 1, 1, 10),
    _CpCaptivePortalClientSwitchIpAddress_Type()
)
cpCaptivePortalClientSwitchIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpCaptivePortalClientSwitchIpAddress.setStatus("current")


class _CpCaptivePortalClientSwitchType_Type(Integer32):
    """Custom type cpCaptivePortalClientSwitchType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 2),
          ("peer", 1))
    )


_CpCaptivePortalClientSwitchType_Type.__name__ = "Integer32"
_CpCaptivePortalClientSwitchType_Object = MibTableColumn
cpCaptivePortalClientSwitchType = _CpCaptivePortalClientSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 2, 5, 1, 1, 11),
    _CpCaptivePortalClientSwitchType_Type()
)
cpCaptivePortalClientSwitchType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpCaptivePortalClientSwitchType.setStatus("current")


class _CpCaptivePortalClientDeauthAction_Type(Integer32):
    """Custom type cpCaptivePortalClientDeauthAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("start", 2))
    )


_CpCaptivePortalClientDeauthAction_Type.__name__ = "Integer32"
_CpCaptivePortalClientDeauthAction_Object = MibTableColumn
cpCaptivePortalClientDeauthAction = _CpCaptivePortalClientDeauthAction_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 2, 5, 1, 1, 12),
    _CpCaptivePortalClientDeauthAction_Type()
)
cpCaptivePortalClientDeauthAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpCaptivePortalClientDeauthAction.setStatus("current")
_CpCaptivePortalClientStatisticsTable_Object = MibTable
cpCaptivePortalClientStatisticsTable = _CpCaptivePortalClientStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 2, 5, 2)
)
if mibBuilder.loadTexts:
    cpCaptivePortalClientStatisticsTable.setStatus("current")
_CpCaptivePortalClientStatisticsEntry_Object = MibTableRow
cpCaptivePortalClientStatisticsEntry = _CpCaptivePortalClientStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 2, 5, 2, 1)
)
if mibBuilder.loadTexts:
    cpCaptivePortalClientStatisticsEntry.setStatus("current")
_CpCaptivePortalClientBytesReceived_Type = Counter64
_CpCaptivePortalClientBytesReceived_Object = MibTableColumn
cpCaptivePortalClientBytesReceived = _CpCaptivePortalClientBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 2, 5, 2, 1, 1),
    _CpCaptivePortalClientBytesReceived_Type()
)
cpCaptivePortalClientBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpCaptivePortalClientBytesReceived.setStatus("current")
_CpCaptivePortalClientBytesTransmitted_Type = Counter64
_CpCaptivePortalClientBytesTransmitted_Object = MibTableColumn
cpCaptivePortalClientBytesTransmitted = _CpCaptivePortalClientBytesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 2, 5, 2, 1, 2),
    _CpCaptivePortalClientBytesTransmitted_Type()
)
cpCaptivePortalClientBytesTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpCaptivePortalClientBytesTransmitted.setStatus("current")
_CpCaptivePortalClientPacketsReceived_Type = Counter64
_CpCaptivePortalClientPacketsReceived_Object = MibTableColumn
cpCaptivePortalClientPacketsReceived = _CpCaptivePortalClientPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 2, 5, 2, 1, 3),
    _CpCaptivePortalClientPacketsReceived_Type()
)
cpCaptivePortalClientPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpCaptivePortalClientPacketsReceived.setStatus("current")
_CpCaptivePortalClientPacketsTransmitted_Type = Counter64
_CpCaptivePortalClientPacketsTransmitted_Object = MibTableColumn
cpCaptivePortalClientPacketsTransmitted = _CpCaptivePortalClientPacketsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 2, 5, 2, 1, 4),
    _CpCaptivePortalClientPacketsTransmitted_Type()
)
cpCaptivePortalClientPacketsTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpCaptivePortalClientPacketsTransmitted.setStatus("current")
_CpCaptivePortalIntfClientAssocGroup_ObjectIdentity = ObjectIdentity
cpCaptivePortalIntfClientAssocGroup = _CpCaptivePortalIntfClientAssocGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 2, 6)
)
_CpCaptivePortalIntfClientAssocTable_Object = MibTable
cpCaptivePortalIntfClientAssocTable = _CpCaptivePortalIntfClientAssocTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 2, 6, 1)
)
if mibBuilder.loadTexts:
    cpCaptivePortalIntfClientAssocTable.setStatus("current")
_CpCaptivePortalIntfClientAssocEntry_Object = MibTableRow
cpCaptivePortalIntfClientAssocEntry = _CpCaptivePortalIntfClientAssocEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 2, 6, 1, 1)
)
cpCaptivePortalIntfClientAssocEntry.setIndexNames(
    (0, "DNOS-CAPTIVE-PORTAL-MIB", "cpCaptivePortalIntfClientIfIndex"),
    (0, "DNOS-CAPTIVE-PORTAL-MIB", "cpCaptivePortalIntfClientAssocMacAddress"),
)
if mibBuilder.loadTexts:
    cpCaptivePortalIntfClientAssocEntry.setStatus("current")
_CpCaptivePortalIntfClientIfIndex_Type = InterfaceIndex
_CpCaptivePortalIntfClientIfIndex_Object = MibTableColumn
cpCaptivePortalIntfClientIfIndex = _CpCaptivePortalIntfClientIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 2, 6, 1, 1, 1),
    _CpCaptivePortalIntfClientIfIndex_Type()
)
cpCaptivePortalIntfClientIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpCaptivePortalIntfClientIfIndex.setStatus("current")
_CpCaptivePortalIntfClientAssocMacAddress_Type = MacAddress
_CpCaptivePortalIntfClientAssocMacAddress_Object = MibTableColumn
cpCaptivePortalIntfClientAssocMacAddress = _CpCaptivePortalIntfClientAssocMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 2, 6, 1, 1, 2),
    _CpCaptivePortalIntfClientAssocMacAddress_Type()
)
cpCaptivePortalIntfClientAssocMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpCaptivePortalIntfClientAssocMacAddress.setStatus("current")
_CpCaptivePortalIntfClientAssocRowStatus_Type = RowStatus
_CpCaptivePortalIntfClientAssocRowStatus_Object = MibTableColumn
cpCaptivePortalIntfClientAssocRowStatus = _CpCaptivePortalIntfClientAssocRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 2, 6, 1, 1, 3),
    _CpCaptivePortalIntfClientAssocRowStatus_Type()
)
cpCaptivePortalIntfClientAssocRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpCaptivePortalIntfClientAssocRowStatus.setStatus("current")
_CpCaptivePortalInstanceClientAssocGroup_ObjectIdentity = ObjectIdentity
cpCaptivePortalInstanceClientAssocGroup = _CpCaptivePortalInstanceClientAssocGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 2, 7)
)
_CpCaptivePortalInstanceClientAssocTable_Object = MibTable
cpCaptivePortalInstanceClientAssocTable = _CpCaptivePortalInstanceClientAssocTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 2, 7, 1)
)
if mibBuilder.loadTexts:
    cpCaptivePortalInstanceClientAssocTable.setStatus("current")
_CpCaptivePortalInstanceClientAssocEntry_Object = MibTableRow
cpCaptivePortalInstanceClientAssocEntry = _CpCaptivePortalInstanceClientAssocEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 2, 7, 1, 1)
)
cpCaptivePortalInstanceClientAssocEntry.setIndexNames(
    (0, "DNOS-CAPTIVE-PORTAL-MIB", "cpCaptivePortalInstanceClientAssocInstanceId"),
    (0, "DNOS-CAPTIVE-PORTAL-MIB", "cpCaptivePortalInstanceClientAssocMacAddress"),
)
if mibBuilder.loadTexts:
    cpCaptivePortalInstanceClientAssocEntry.setStatus("current")


class _CpCaptivePortalInstanceClientAssocInstanceId_Type(Integer32):
    """Custom type cpCaptivePortalInstanceClientAssocInstanceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CpCaptivePortalInstanceClientAssocInstanceId_Type.__name__ = "Integer32"
_CpCaptivePortalInstanceClientAssocInstanceId_Object = MibTableColumn
cpCaptivePortalInstanceClientAssocInstanceId = _CpCaptivePortalInstanceClientAssocInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 2, 7, 1, 1, 1),
    _CpCaptivePortalInstanceClientAssocInstanceId_Type()
)
cpCaptivePortalInstanceClientAssocInstanceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpCaptivePortalInstanceClientAssocInstanceId.setStatus("current")
_CpCaptivePortalInstanceClientAssocMacAddress_Type = MacAddress
_CpCaptivePortalInstanceClientAssocMacAddress_Object = MibTableColumn
cpCaptivePortalInstanceClientAssocMacAddress = _CpCaptivePortalInstanceClientAssocMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 2, 7, 1, 1, 2),
    _CpCaptivePortalInstanceClientAssocMacAddress_Type()
)
cpCaptivePortalInstanceClientAssocMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpCaptivePortalInstanceClientAssocMacAddress.setStatus("current")
_CpCaptivePortalInstanceClientAssocRowStatus_Type = RowStatus
_CpCaptivePortalInstanceClientAssocRowStatus_Object = MibTableColumn
cpCaptivePortalInstanceClientAssocRowStatus = _CpCaptivePortalInstanceClientAssocRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 2, 7, 1, 1, 3),
    _CpCaptivePortalInstanceClientAssocRowStatus_Type()
)
cpCaptivePortalInstanceClientAssocRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpCaptivePortalInstanceClientAssocRowStatus.setStatus("current")
_CpTrapsConfig_ObjectIdentity = ObjectIdentity
cpTrapsConfig = _CpTrapsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 3)
)


class _CpTrapMode_Type(Integer32):
    """Custom type cpTrapMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_CpTrapMode_Type.__name__ = "Integer32"
_CpTrapMode_Object = MibScalar
cpTrapMode = _CpTrapMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 3, 1),
    _CpTrapMode_Type()
)
cpTrapMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpTrapMode.setStatus("current")


class _CpClientAuthenticationFailureTrapMode_Type(Integer32):
    """Custom type cpClientAuthenticationFailureTrapMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_CpClientAuthenticationFailureTrapMode_Type.__name__ = "Integer32"
_CpClientAuthenticationFailureTrapMode_Object = MibScalar
cpClientAuthenticationFailureTrapMode = _CpClientAuthenticationFailureTrapMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 3, 2),
    _CpClientAuthenticationFailureTrapMode_Type()
)
cpClientAuthenticationFailureTrapMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpClientAuthenticationFailureTrapMode.setStatus("current")


class _CpClientConnectTrapMode_Type(Integer32):
    """Custom type cpClientConnectTrapMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_CpClientConnectTrapMode_Type.__name__ = "Integer32"
_CpClientConnectTrapMode_Object = MibScalar
cpClientConnectTrapMode = _CpClientConnectTrapMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 3, 3),
    _CpClientConnectTrapMode_Type()
)
cpClientConnectTrapMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpClientConnectTrapMode.setStatus("current")


class _CpClientDatabaseFullTrapMode_Type(Integer32):
    """Custom type cpClientDatabaseFullTrapMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_CpClientDatabaseFullTrapMode_Type.__name__ = "Integer32"
_CpClientDatabaseFullTrapMode_Object = MibScalar
cpClientDatabaseFullTrapMode = _CpClientDatabaseFullTrapMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 3, 4),
    _CpClientDatabaseFullTrapMode_Type()
)
cpClientDatabaseFullTrapMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpClientDatabaseFullTrapMode.setStatus("current")


class _CpClientDisconnectTrapMode_Type(Integer32):
    """Custom type cpClientDisconnectTrapMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_CpClientDisconnectTrapMode_Type.__name__ = "Integer32"
_CpClientDisconnectTrapMode_Object = MibScalar
cpClientDisconnectTrapMode = _CpClientDisconnectTrapMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 3, 5),
    _CpClientDisconnectTrapMode_Type()
)
cpClientDisconnectTrapMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpClientDisconnectTrapMode.setStatus("current")
_CpTraps_ObjectIdentity = ObjectIdentity
cpTraps = _CpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 4)
)
_CpCaptivePortalConfigWebGroup_ObjectIdentity = ObjectIdentity
cpCaptivePortalConfigWebGroup = _CpCaptivePortalConfigWebGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 5)
)
_CpCaptivePortalConfigWebTable_Object = MibTable
cpCaptivePortalConfigWebTable = _CpCaptivePortalConfigWebTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 5, 1)
)
if mibBuilder.loadTexts:
    cpCaptivePortalConfigWebTable.setStatus("current")
_CpCaptivePortalConfigWebEntry_Object = MibTableRow
cpCaptivePortalConfigWebEntry = _CpCaptivePortalConfigWebEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 5, 1, 1)
)
cpCaptivePortalConfigWebEntry.setIndexNames(
    (0, "DNOS-CAPTIVE-PORTAL-MIB", "cpCaptivePortalConfigWebInstanceId"),
    (0, "DNOS-CAPTIVE-PORTAL-MIB", "cpCaptivePortalConfigWebWebId"),
)
if mibBuilder.loadTexts:
    cpCaptivePortalConfigWebEntry.setStatus("current")
_CpCaptivePortalConfigWebInstanceId_Type = Unsigned32
_CpCaptivePortalConfigWebInstanceId_Object = MibTableColumn
cpCaptivePortalConfigWebInstanceId = _CpCaptivePortalConfigWebInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 5, 1, 1, 1),
    _CpCaptivePortalConfigWebInstanceId_Type()
)
cpCaptivePortalConfigWebInstanceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpCaptivePortalConfigWebInstanceId.setStatus("current")
_CpCaptivePortalConfigWebWebId_Type = Unsigned32
_CpCaptivePortalConfigWebWebId_Object = MibTableColumn
cpCaptivePortalConfigWebWebId = _CpCaptivePortalConfigWebWebId_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 5, 1, 1, 2),
    _CpCaptivePortalConfigWebWebId_Type()
)
cpCaptivePortalConfigWebWebId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpCaptivePortalConfigWebWebId.setStatus("current")
cpCaptivePortalClientStatusEntry.registerAugmentions(
    ("DNOS-CAPTIVE-PORTAL-MIB",
     "cpCaptivePortalClientStatisticsEntry")
)
cpCaptivePortalClientStatisticsEntry.setIndexNames(*cpCaptivePortalClientStatusEntry.getIndexNames())

# Managed Objects groups


# Notification objects

cpClientAuthenticationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 4, 1)
)
cpClientAuthenticationFailure.setObjects(
      *(("DNOS-CAPTIVE-PORTAL-MIB", "cpCaptivePortalClientMacAddress"),
        ("DNOS-CAPTIVE-PORTAL-MIB", "cpCaptivePortalClientIpAddress"),
        ("DNOS-CAPTIVE-PORTAL-MIB", "cpCaptivePortalClientCPID"),
        ("DNOS-CAPTIVE-PORTAL-MIB", "cpCaptivePortalClientAssocIfIndex"),
        ("DNOS-CAPTIVE-PORTAL-MIB", "cpCaptivePortalClientSwitchMacAddress"),
        ("DNOS-CAPTIVE-PORTAL-MIB", "cpCaptivePortalClientUserName"))
)
if mibBuilder.loadTexts:
    cpClientAuthenticationFailure.setStatus(
        "current"
    )

cpClientConnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 4, 2)
)
cpClientConnect.setObjects(
      *(("DNOS-CAPTIVE-PORTAL-MIB", "cpCaptivePortalClientMacAddress"),
        ("DNOS-CAPTIVE-PORTAL-MIB", "cpCaptivePortalClientAssocIfIndex"),
        ("DNOS-CAPTIVE-PORTAL-MIB", "cpCaptivePortalClientIpAddress"),
        ("DNOS-CAPTIVE-PORTAL-MIB", "cpCaptivePortalClientCPID"),
        ("DNOS-CAPTIVE-PORTAL-MIB", "cpCaptivePortalClientSwitchMacAddress"))
)
if mibBuilder.loadTexts:
    cpClientConnect.setStatus(
        "current"
    )

cpClientDatabaseFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 4, 3)
)
cpClientDatabaseFull.setObjects(
    ("DNOS-CAPTIVE-PORTAL-MIB", "cpCaptivePortalClientMacAddress")
)
if mibBuilder.loadTexts:
    cpClientDatabaseFull.setStatus(
        "current"
    )

cpClientDisconnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 38, 4, 4)
)
cpClientDisconnect.setObjects(
      *(("DNOS-CAPTIVE-PORTAL-MIB", "cpCaptivePortalClientMacAddress"),
        ("DNOS-CAPTIVE-PORTAL-MIB", "cpCaptivePortalClientAssocIfIndex"),
        ("DNOS-CAPTIVE-PORTAL-MIB", "cpCaptivePortalClientIpAddress"),
        ("DNOS-CAPTIVE-PORTAL-MIB", "cpCaptivePortalClientCPID"),
        ("DNOS-CAPTIVE-PORTAL-MIB", "cpCaptivePortalClientSwitchMacAddress"))
)
if mibBuilder.loadTexts:
    cpClientDisconnect.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DNOS-CAPTIVE-PORTAL-MIB",
    **{"CpCaptivePortalIntfCapabilitiesMap": CpCaptivePortalIntfCapabilitiesMap,
       "fastPathCaptivePortal": fastPathCaptivePortal,
       "cpConfigGroup": cpConfigGroup,
       "cpGlobalConfigGroup": cpGlobalConfigGroup,
       "cpAdminMode": cpAdminMode,
       "cpAdditionalHttpPort": cpAdditionalHttpPort,
       "cpAdditionalHttpSecurePort": cpAdditionalHttpSecurePort,
       "cpPeerStatsReportingInterval": cpPeerStatsReportingInterval,
       "cpAuthTimeout": cpAuthTimeout,
       "cpCaptivePortalConfigGroup": cpCaptivePortalConfigGroup,
       "cpCaptivePortalTable": cpCaptivePortalTable,
       "cpCaptivePortalEntry": cpCaptivePortalEntry,
       "cpCaptivePortalInstanceId": cpCaptivePortalInstanceId,
       "cpCaptivePortalConfigName": cpCaptivePortalConfigName,
       "cpCaptivePortalAdminMode": cpCaptivePortalAdminMode,
       "cpCaptivePortalProtocolMode": cpCaptivePortalProtocolMode,
       "cpCaptivePortalVerificationMode": cpCaptivePortalVerificationMode,
       "cpCaptivePortalUserGroup": cpCaptivePortalUserGroup,
       "cpCaptivePortalURLRedirectMode": cpCaptivePortalURLRedirectMode,
       "cpCaptivePortalRedirectURL": cpCaptivePortalRedirectURL,
       "cpCaptivePortalSessionTimeout": cpCaptivePortalSessionTimeout,
       "cpCaptivePortalIdleTimeout": cpCaptivePortalIdleTimeout,
       "cpCaptivePortalRadiusAuthServer": cpCaptivePortalRadiusAuthServer,
       "cpCaptivePortalMaxBandwidthUp": cpCaptivePortalMaxBandwidthUp,
       "cpCaptivePortalMaxBandwidthDown": cpCaptivePortalMaxBandwidthDown,
       "cpCaptivePortalMaxInputOctets": cpCaptivePortalMaxInputOctets,
       "cpCaptivePortalMaxOutputOctets": cpCaptivePortalMaxOutputOctets,
       "cpCaptivePortalMaxTotalOctets": cpCaptivePortalMaxTotalOctets,
       "cpCaptivePortalUserLogoutMode": cpCaptivePortalUserLogoutMode,
       "cpCaptivePortalRowStatus": cpCaptivePortalRowStatus,
       "cpLocalUserDatabaseGroup": cpLocalUserDatabaseGroup,
       "cpLocalUserGroupTable": cpLocalUserGroupTable,
       "cpLocalUserGroupEntry": cpLocalUserGroupEntry,
       "cpLocalUserGroupIndex": cpLocalUserGroupIndex,
       "cpLocalUserGroupName": cpLocalUserGroupName,
       "cpLocalUserGroupRowStatus": cpLocalUserGroupRowStatus,
       "cpLocalUserTable": cpLocalUserTable,
       "cpLocalUserEntry": cpLocalUserEntry,
       "cpLocalUserIndex": cpLocalUserIndex,
       "cpLocalUserName": cpLocalUserName,
       "cpLocalUserPassword": cpLocalUserPassword,
       "cpLocalUserSessionTimeout": cpLocalUserSessionTimeout,
       "cpLocalUserIdleTimeout": cpLocalUserIdleTimeout,
       "cpLocalUserMaxBandwidthUp": cpLocalUserMaxBandwidthUp,
       "cpLocalUserMaxBandwidthDown": cpLocalUserMaxBandwidthDown,
       "cpLocalUserMaxInputOctets": cpLocalUserMaxInputOctets,
       "cpLocalUserMaxOutputOctets": cpLocalUserMaxOutputOctets,
       "cpLocalUserMaxTotalOctets": cpLocalUserMaxTotalOctets,
       "cpLocalUserRowStatus": cpLocalUserRowStatus,
       "cpLocalUserGroupAssociationTable": cpLocalUserGroupAssociationTable,
       "cpLocalUserGroupAssociationEntry": cpLocalUserGroupAssociationEntry,
       "cpLocalUserGroupAssociationUserIndex": cpLocalUserGroupAssociationUserIndex,
       "cpLocalUserGroupAssociationGroupIndex": cpLocalUserGroupAssociationGroupIndex,
       "cpLocalUserGroupAssociationRowStatus": cpLocalUserGroupAssociationRowStatus,
       "cpInterfaceAssociationGroup": cpInterfaceAssociationGroup,
       "cpInterfaceAssociationTable": cpInterfaceAssociationTable,
       "cpInterfaceAssociationEntry": cpInterfaceAssociationEntry,
       "cpIntfAssociationCPID": cpIntfAssociationCPID,
       "cpIntfAssociationIfIndex": cpIntfAssociationIfIndex,
       "cpIntfAssociationRowStatus": cpIntfAssociationRowStatus,
       "cpStatusGroup": cpStatusGroup,
       "cpCaptivePortalGlobalStatusGroup": cpCaptivePortalGlobalStatusGroup,
       "cpCaptivePortalOperStatus": cpCaptivePortalOperStatus,
       "cpCaptivePortalOperDisabledReason": cpCaptivePortalOperDisabledReason,
       "cpCaptivePortalIpv4Address": cpCaptivePortalIpv4Address,
       "cpCaptivePortalInstanceMaxCount": cpCaptivePortalInstanceMaxCount,
       "cpCaptivePortalInstanceConfiguredCount": cpCaptivePortalInstanceConfiguredCount,
       "cpCaptivePortalInstanceActiveCount": cpCaptivePortalInstanceActiveCount,
       "cpCaptivePortalAuthenUserMaxCount": cpCaptivePortalAuthenUserMaxCount,
       "cpCaptivePortalLocalUserMaxCount": cpCaptivePortalLocalUserMaxCount,
       "cpCaptivePortalConfiguredLocalUserCount": cpCaptivePortalConfiguredLocalUserCount,
       "cpCaptivePortalAuthenUserCurrentCount": cpCaptivePortalAuthenUserCurrentCount,
       "cpCaptivePortalInstanceStatusGroup": cpCaptivePortalInstanceStatusGroup,
       "cpCaptivePortalInstanceStatusTable": cpCaptivePortalInstanceStatusTable,
       "cpCaptivePortalInstanceStatusEntry": cpCaptivePortalInstanceStatusEntry,
       "cpCaptivePortalInstanceOperStatus": cpCaptivePortalInstanceOperStatus,
       "cpCaptivePortalInstanceOperDisabledReason": cpCaptivePortalInstanceOperDisabledReason,
       "cpCaptivePortalInstanceBlockStatus": cpCaptivePortalInstanceBlockStatus,
       "cpCaptivePortalInstanceAuthUserCount": cpCaptivePortalInstanceAuthUserCount,
       "cpCaptivePortalIntfStatusGroup": cpCaptivePortalIntfStatusGroup,
       "cpCaptivePortalIntfStatusTable": cpCaptivePortalIntfStatusTable,
       "cpCaptivePortalIntfStatusEntry": cpCaptivePortalIntfStatusEntry,
       "cpCaptivePortalIntfIfIndex": cpCaptivePortalIntfIfIndex,
       "cpCaptivePortalIntfActivationStatus": cpCaptivePortalIntfActivationStatus,
       "cpCaptivePortalIntfActivationDisabledReason": cpCaptivePortalIntfActivationDisabledReason,
       "cpCaptivePortalIntfBlockStatus": cpCaptivePortalIntfBlockStatus,
       "cpCaptivePortalIntfAuthUserCount": cpCaptivePortalIntfAuthUserCount,
       "cpCaptivePortalIntfDatabaseGroup": cpCaptivePortalIntfDatabaseGroup,
       "cpCaptivePortalIntfDatabaseTable": cpCaptivePortalIntfDatabaseTable,
       "cpCaptivePortalIntfDatabaseEntry": cpCaptivePortalIntfDatabaseEntry,
       "cpCaptivePortalIntfCapabilities": cpCaptivePortalIntfCapabilities,
       "cpCaptivePortalClientStatusGroup": cpCaptivePortalClientStatusGroup,
       "cpCaptivePortalClientStatusTable": cpCaptivePortalClientStatusTable,
       "cpCaptivePortalClientStatusEntry": cpCaptivePortalClientStatusEntry,
       "cpCaptivePortalClientMacAddress": cpCaptivePortalClientMacAddress,
       "cpCaptivePortalClientIpAddress": cpCaptivePortalClientIpAddress,
       "cpCaptivePortalClientUserName": cpCaptivePortalClientUserName,
       "cpCaptivePortalClientProtocolMode": cpCaptivePortalClientProtocolMode,
       "cpCaptivePortalClientVerificationMode": cpCaptivePortalClientVerificationMode,
       "cpCaptivePortalClientAssocIfIndex": cpCaptivePortalClientAssocIfIndex,
       "cpCaptivePortalClientCPID": cpCaptivePortalClientCPID,
       "cpCaptivePortalClientSessionTime": cpCaptivePortalClientSessionTime,
       "cpCaptivePortalClientSwitchMacAddress": cpCaptivePortalClientSwitchMacAddress,
       "cpCaptivePortalClientSwitchIpAddress": cpCaptivePortalClientSwitchIpAddress,
       "cpCaptivePortalClientSwitchType": cpCaptivePortalClientSwitchType,
       "cpCaptivePortalClientDeauthAction": cpCaptivePortalClientDeauthAction,
       "cpCaptivePortalClientStatisticsTable": cpCaptivePortalClientStatisticsTable,
       "cpCaptivePortalClientStatisticsEntry": cpCaptivePortalClientStatisticsEntry,
       "cpCaptivePortalClientBytesReceived": cpCaptivePortalClientBytesReceived,
       "cpCaptivePortalClientBytesTransmitted": cpCaptivePortalClientBytesTransmitted,
       "cpCaptivePortalClientPacketsReceived": cpCaptivePortalClientPacketsReceived,
       "cpCaptivePortalClientPacketsTransmitted": cpCaptivePortalClientPacketsTransmitted,
       "cpCaptivePortalIntfClientAssocGroup": cpCaptivePortalIntfClientAssocGroup,
       "cpCaptivePortalIntfClientAssocTable": cpCaptivePortalIntfClientAssocTable,
       "cpCaptivePortalIntfClientAssocEntry": cpCaptivePortalIntfClientAssocEntry,
       "cpCaptivePortalIntfClientIfIndex": cpCaptivePortalIntfClientIfIndex,
       "cpCaptivePortalIntfClientAssocMacAddress": cpCaptivePortalIntfClientAssocMacAddress,
       "cpCaptivePortalIntfClientAssocRowStatus": cpCaptivePortalIntfClientAssocRowStatus,
       "cpCaptivePortalInstanceClientAssocGroup": cpCaptivePortalInstanceClientAssocGroup,
       "cpCaptivePortalInstanceClientAssocTable": cpCaptivePortalInstanceClientAssocTable,
       "cpCaptivePortalInstanceClientAssocEntry": cpCaptivePortalInstanceClientAssocEntry,
       "cpCaptivePortalInstanceClientAssocInstanceId": cpCaptivePortalInstanceClientAssocInstanceId,
       "cpCaptivePortalInstanceClientAssocMacAddress": cpCaptivePortalInstanceClientAssocMacAddress,
       "cpCaptivePortalInstanceClientAssocRowStatus": cpCaptivePortalInstanceClientAssocRowStatus,
       "cpTrapsConfig": cpTrapsConfig,
       "cpTrapMode": cpTrapMode,
       "cpClientAuthenticationFailureTrapMode": cpClientAuthenticationFailureTrapMode,
       "cpClientConnectTrapMode": cpClientConnectTrapMode,
       "cpClientDatabaseFullTrapMode": cpClientDatabaseFullTrapMode,
       "cpClientDisconnectTrapMode": cpClientDisconnectTrapMode,
       "cpTraps": cpTraps,
       "cpClientAuthenticationFailure": cpClientAuthenticationFailure,
       "cpClientConnect": cpClientConnect,
       "cpClientDatabaseFull": cpClientDatabaseFull,
       "cpClientDisconnect": cpClientDisconnect,
       "cpCaptivePortalConfigWebGroup": cpCaptivePortalConfigWebGroup,
       "cpCaptivePortalConfigWebTable": cpCaptivePortalConfigWebTable,
       "cpCaptivePortalConfigWebEntry": cpCaptivePortalConfigWebEntry,
       "cpCaptivePortalConfigWebInstanceId": cpCaptivePortalConfigWebInstanceId,
       "cpCaptivePortalConfigWebWebId": cpCaptivePortalConfigWebWebId}
)
