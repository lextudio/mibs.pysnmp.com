# SNMP MIB module (ALCATEL-IND1-NTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-NTP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:36:38 2024
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

(softentIND1Ntp,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1Ntp")

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

(DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

alcatelIND1NTPMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1)
)
alcatelIND1NTPMIB.setRevisions(
        ("2010-05-13 00:00",
         "2007-04-03 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1NTPMIBNotifications_ObjectIdentity = ObjectIdentity
alcatelIND1NTPMIBNotifications = _AlcatelIND1NTPMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 0)
)
if mibBuilder.loadTexts:
    alcatelIND1NTPMIBNotifications.setStatus("current")
_AlcatelIND1NTPMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1NTPMIBObjects = _AlcatelIND1NTPMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1NTPMIBObjects.setStatus("current")
_AlaNtpConfig_ObjectIdentity = ObjectIdentity
alaNtpConfig = _AlaNtpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 1)
)


class _AlaNtpEnable_Type(Integer32):
    """Custom type alaNtpEnable based on Integer32"""
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


_AlaNtpEnable_Type.__name__ = "Integer32"
_AlaNtpEnable_Object = MibScalar
alaNtpEnable = _AlaNtpEnable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 1, 1),
    _AlaNtpEnable_Type()
)
alaNtpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaNtpEnable.setStatus("current")


class _AlaNtpMonitorEnable_Type(Integer32):
    """Custom type alaNtpMonitorEnable based on Integer32"""
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


_AlaNtpMonitorEnable_Type.__name__ = "Integer32"
_AlaNtpMonitorEnable_Object = MibScalar
alaNtpMonitorEnable = _AlaNtpMonitorEnable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 1, 2),
    _AlaNtpMonitorEnable_Type()
)
alaNtpMonitorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaNtpMonitorEnable.setStatus("current")


class _AlaNtpBroadcastEnable_Type(Integer32):
    """Custom type alaNtpBroadcastEnable based on Integer32"""
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


_AlaNtpBroadcastEnable_Type.__name__ = "Integer32"
_AlaNtpBroadcastEnable_Object = MibScalar
alaNtpBroadcastEnable = _AlaNtpBroadcastEnable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 1, 3),
    _AlaNtpBroadcastEnable_Type()
)
alaNtpBroadcastEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaNtpBroadcastEnable.setStatus("current")
_AlaNtpPeerTable_Object = MibTable
alaNtpPeerTable = _AlaNtpPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 1, 4)
)
if mibBuilder.loadTexts:
    alaNtpPeerTable.setStatus("current")
_AlaNtpPeerEntry_Object = MibTableRow
alaNtpPeerEntry = _AlaNtpPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 1, 4, 1)
)
alaNtpPeerEntry.setIndexNames(
    (0, "ALCATEL-IND1-NTP-MIB", "alaNtpPeerAddressType"),
    (0, "ALCATEL-IND1-NTP-MIB", "alaNtpPeerAddress"),
)
if mibBuilder.loadTexts:
    alaNtpPeerEntry.setStatus("current")
_AlaNtpPeerAddressType_Type = InetAddressType
_AlaNtpPeerAddressType_Object = MibTableColumn
alaNtpPeerAddressType = _AlaNtpPeerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 1, 4, 1, 1),
    _AlaNtpPeerAddressType_Type()
)
alaNtpPeerAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaNtpPeerAddressType.setStatus("current")
_AlaNtpPeerAddress_Type = InetAddress
_AlaNtpPeerAddress_Object = MibTableColumn
alaNtpPeerAddress = _AlaNtpPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 1, 4, 1, 2),
    _AlaNtpPeerAddress_Type()
)
alaNtpPeerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaNtpPeerAddress.setStatus("current")
_AlaNtpPeerIpAddress_Type = IpAddress
_AlaNtpPeerIpAddress_Object = MibTableColumn
alaNtpPeerIpAddress = _AlaNtpPeerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 1, 4, 1, 3),
    _AlaNtpPeerIpAddress_Type()
)
alaNtpPeerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpPeerIpAddress.setStatus("current")


class _AlaNtpPeerType_Type(Integer32):
    """Custom type alaNtpPeerType based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              8)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("bclient", 8),
          ("broadcast", 5),
          ("client", 3),
          ("passive", 2),
          ("server", 4))
    )


_AlaNtpPeerType_Type.__name__ = "Integer32"
_AlaNtpPeerType_Object = MibTableColumn
alaNtpPeerType = _AlaNtpPeerType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 1, 4, 1, 4),
    _AlaNtpPeerType_Type()
)
alaNtpPeerType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaNtpPeerType.setStatus("current")


class _AlaNtpPeerAuth_Type(Integer32):
    """Custom type alaNtpPeerAuth based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaNtpPeerAuth_Type.__name__ = "Integer32"
_AlaNtpPeerAuth_Object = MibTableColumn
alaNtpPeerAuth = _AlaNtpPeerAuth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 1, 4, 1, 5),
    _AlaNtpPeerAuth_Type()
)
alaNtpPeerAuth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaNtpPeerAuth.setStatus("current")


class _AlaNtpPeerVersion_Type(Integer32):
    """Custom type alaNtpPeerVersion based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AlaNtpPeerVersion_Type.__name__ = "Integer32"
_AlaNtpPeerVersion_Object = MibTableColumn
alaNtpPeerVersion = _AlaNtpPeerVersion_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 1, 4, 1, 6),
    _AlaNtpPeerVersion_Type()
)
alaNtpPeerVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaNtpPeerVersion.setStatus("current")


class _AlaNtpPeerMinpoll_Type(Integer32):
    """Custom type alaNtpPeerMinpoll based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 10),
    )


_AlaNtpPeerMinpoll_Type.__name__ = "Integer32"
_AlaNtpPeerMinpoll_Object = MibTableColumn
alaNtpPeerMinpoll = _AlaNtpPeerMinpoll_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 1, 4, 1, 7),
    _AlaNtpPeerMinpoll_Type()
)
alaNtpPeerMinpoll.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaNtpPeerMinpoll.setStatus("current")


class _AlaNtpPeerPrefer_Type(Integer32):
    """Custom type alaNtpPeerPrefer based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noPrefer", 2),
          ("prefer", 1))
    )


_AlaNtpPeerPrefer_Type.__name__ = "Integer32"
_AlaNtpPeerPrefer_Object = MibTableColumn
alaNtpPeerPrefer = _AlaNtpPeerPrefer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 1, 4, 1, 8),
    _AlaNtpPeerPrefer_Type()
)
alaNtpPeerPrefer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaNtpPeerPrefer.setStatus("current")
_AlaNtpPeerAdmin_Type = RowStatus
_AlaNtpPeerAdmin_Object = MibTableColumn
alaNtpPeerAdmin = _AlaNtpPeerAdmin_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 1, 4, 1, 9),
    _AlaNtpPeerAdmin_Type()
)
alaNtpPeerAdmin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaNtpPeerAdmin.setStatus("current")
_AlaNtpPeerName_Type = SnmpAdminString
_AlaNtpPeerName_Object = MibTableColumn
alaNtpPeerName = _AlaNtpPeerName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 1, 4, 1, 10),
    _AlaNtpPeerName_Type()
)
alaNtpPeerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpPeerName.setStatus("current")


class _AlaNtpPeerStratum_Type(Integer32):
    """Custom type alaNtpPeerStratum based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AlaNtpPeerStratum_Type.__name__ = "Integer32"
_AlaNtpPeerStratum_Object = MibTableColumn
alaNtpPeerStratum = _AlaNtpPeerStratum_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 1, 4, 1, 11),
    _AlaNtpPeerStratum_Type()
)
alaNtpPeerStratum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaNtpPeerStratum.setStatus("current")


class _AlaNtpAuthDelay_Type(Integer32):
    """Custom type alaNtpAuthDelay based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaNtpAuthDelay_Type.__name__ = "Integer32"
_AlaNtpAuthDelay_Object = MibScalar
alaNtpAuthDelay = _AlaNtpAuthDelay_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 1, 5),
    _AlaNtpAuthDelay_Type()
)
alaNtpAuthDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaNtpAuthDelay.setStatus("current")


class _AlaNtpBroadcastDelay_Type(Integer32):
    """Custom type alaNtpBroadcastDelay based on Integer32"""
    defaultValue = 4000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaNtpBroadcastDelay_Type.__name__ = "Integer32"
_AlaNtpBroadcastDelay_Object = MibScalar
alaNtpBroadcastDelay = _AlaNtpBroadcastDelay_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 1, 6),
    _AlaNtpBroadcastDelay_Type()
)
alaNtpBroadcastDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaNtpBroadcastDelay.setStatus("current")
_AlaNtpKeysFile_Type = SnmpAdminString
_AlaNtpKeysFile_Object = MibScalar
alaNtpKeysFile = _AlaNtpKeysFile_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 1, 7),
    _AlaNtpKeysFile_Type()
)
alaNtpKeysFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpKeysFile.setStatus("current")


class _AlaNtpConfigReqKeyId_Type(Integer32):
    """Custom type alaNtpConfigReqKeyId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaNtpConfigReqKeyId_Type.__name__ = "Integer32"
_AlaNtpConfigReqKeyId_Object = MibScalar
alaNtpConfigReqKeyId = _AlaNtpConfigReqKeyId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 1, 8),
    _AlaNtpConfigReqKeyId_Type()
)
alaNtpConfigReqKeyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaNtpConfigReqKeyId.setStatus("current")


class _AlaNtpConfigCtlKeyId_Type(Integer32):
    """Custom type alaNtpConfigCtlKeyId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaNtpConfigCtlKeyId_Type.__name__ = "Integer32"
_AlaNtpConfigCtlKeyId_Object = MibScalar
alaNtpConfigCtlKeyId = _AlaNtpConfigCtlKeyId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 1, 9),
    _AlaNtpConfigCtlKeyId_Type()
)
alaNtpConfigCtlKeyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaNtpConfigCtlKeyId.setStatus("current")


class _AlaNtpConfigCfgKeyId_Type(Integer32):
    """Custom type alaNtpConfigCfgKeyId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaNtpConfigCfgKeyId_Type.__name__ = "Integer32"
_AlaNtpConfigCfgKeyId_Object = MibScalar
alaNtpConfigCfgKeyId = _AlaNtpConfigCfgKeyId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 1, 10),
    _AlaNtpConfigCfgKeyId_Type()
)
alaNtpConfigCfgKeyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaNtpConfigCfgKeyId.setStatus("current")


class _AlaNtpPrecision_Type(Integer32):
    """Custom type alaNtpPrecision based on Integer32"""
    defaultValue = -6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20, -1),
    )


_AlaNtpPrecision_Type.__name__ = "Integer32"
_AlaNtpPrecision_Object = MibScalar
alaNtpPrecision = _AlaNtpPrecision_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 1, 11),
    _AlaNtpPrecision_Type()
)
alaNtpPrecision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaNtpPrecision.setStatus("current")


class _AlaNtpPeerTests_Type(Integer32):
    """Custom type alaNtpPeerTests based on Integer32"""
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


_AlaNtpPeerTests_Type.__name__ = "Integer32"
_AlaNtpPeerTests_Object = MibScalar
alaNtpPeerTests = _AlaNtpPeerTests_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 1, 12),
    _AlaNtpPeerTests_Type()
)
alaNtpPeerTests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaNtpPeerTests.setStatus("current")


class _AlaNtpSysStratum_Type(Integer32):
    """Custom type alaNtpSysStratum based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 16),
    )


_AlaNtpSysStratum_Type.__name__ = "Integer32"
_AlaNtpSysStratum_Object = MibScalar
alaNtpSysStratum = _AlaNtpSysStratum_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 1, 13),
    _AlaNtpSysStratum_Type()
)
alaNtpSysStratum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaNtpSysStratum.setStatus("current")


class _AlaNtpMaxAssociation_Type(Integer32):
    """Custom type alaNtpMaxAssociation based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_AlaNtpMaxAssociation_Type.__name__ = "Integer32"
_AlaNtpMaxAssociation_Object = MibScalar
alaNtpMaxAssociation = _AlaNtpMaxAssociation_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 1, 14),
    _AlaNtpMaxAssociation_Type()
)
alaNtpMaxAssociation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaNtpMaxAssociation.setStatus("current")


class _AlaNtpAuthenticate_Type(Integer32):
    """Custom type alaNtpAuthenticate based on Integer32"""
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


_AlaNtpAuthenticate_Type.__name__ = "Integer32"
_AlaNtpAuthenticate_Object = MibScalar
alaNtpAuthenticate = _AlaNtpAuthenticate_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 1, 15),
    _AlaNtpAuthenticate_Type()
)
alaNtpAuthenticate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaNtpAuthenticate.setStatus("current")
_AlaNtpInfo_ObjectIdentity = ObjectIdentity
alaNtpInfo = _AlaNtpInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 2)
)
_AlaNtpPeerListTable_Object = MibTable
alaNtpPeerListTable = _AlaNtpPeerListTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alaNtpPeerListTable.setStatus("current")
_AlaNtpPeerListEntry_Object = MibTableRow
alaNtpPeerListEntry = _AlaNtpPeerListEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 2, 1, 1)
)
alaNtpPeerListEntry.setIndexNames(
    (0, "ALCATEL-IND1-NTP-MIB", "alaNtpPeerListAddressType"),
    (0, "ALCATEL-IND1-NTP-MIB", "alaNtpPeerListAddress"),
)
if mibBuilder.loadTexts:
    alaNtpPeerListEntry.setStatus("current")
_AlaNtpPeerListAddressType_Type = InetAddressType
_AlaNtpPeerListAddressType_Object = MibTableColumn
alaNtpPeerListAddressType = _AlaNtpPeerListAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 2, 1, 1, 1),
    _AlaNtpPeerListAddressType_Type()
)
alaNtpPeerListAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaNtpPeerListAddressType.setStatus("current")
_AlaNtpPeerListAddress_Type = InetAddress
_AlaNtpPeerListAddress_Object = MibTableColumn
alaNtpPeerListAddress = _AlaNtpPeerListAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 2, 1, 1, 2),
    _AlaNtpPeerListAddress_Type()
)
alaNtpPeerListAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaNtpPeerListAddress.setStatus("current")
_AlaNtpPeerListIpAddress_Type = IpAddress
_AlaNtpPeerListIpAddress_Object = MibTableColumn
alaNtpPeerListIpAddress = _AlaNtpPeerListIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 2, 1, 1, 3),
    _AlaNtpPeerListIpAddress_Type()
)
alaNtpPeerListIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpPeerListIpAddress.setStatus("current")
_AlaNtpPeerListLocal_Type = IpAddress
_AlaNtpPeerListLocal_Object = MibTableColumn
alaNtpPeerListLocal = _AlaNtpPeerListLocal_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 2, 1, 1, 4),
    _AlaNtpPeerListLocal_Type()
)
alaNtpPeerListLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpPeerListLocal.setStatus("current")


class _AlaNtpPeerListStratum_Type(Integer32):
    """Custom type alaNtpPeerListStratum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AlaNtpPeerListStratum_Type.__name__ = "Integer32"
_AlaNtpPeerListStratum_Object = MibTableColumn
alaNtpPeerListStratum = _AlaNtpPeerListStratum_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 2, 1, 1, 5),
    _AlaNtpPeerListStratum_Type()
)
alaNtpPeerListStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpPeerListStratum.setStatus("current")


class _AlaNtpPeerListPoll_Type(Integer32):
    """Custom type alaNtpPeerListPoll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AlaNtpPeerListPoll_Type.__name__ = "Integer32"
_AlaNtpPeerListPoll_Object = MibTableColumn
alaNtpPeerListPoll = _AlaNtpPeerListPoll_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 2, 1, 1, 6),
    _AlaNtpPeerListPoll_Type()
)
alaNtpPeerListPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpPeerListPoll.setStatus("current")


class _AlaNtpPeerListReach_Type(Integer32):
    """Custom type alaNtpPeerListReach based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AlaNtpPeerListReach_Type.__name__ = "Integer32"
_AlaNtpPeerListReach_Object = MibTableColumn
alaNtpPeerListReach = _AlaNtpPeerListReach_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 2, 1, 1, 7),
    _AlaNtpPeerListReach_Type()
)
alaNtpPeerListReach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpPeerListReach.setStatus("current")
_AlaNtpPeerListDelay_Type = SnmpAdminString
_AlaNtpPeerListDelay_Object = MibTableColumn
alaNtpPeerListDelay = _AlaNtpPeerListDelay_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 2, 1, 1, 8),
    _AlaNtpPeerListDelay_Type()
)
alaNtpPeerListDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpPeerListDelay.setStatus("current")
_AlaNtpPeerListOffset_Type = SnmpAdminString
_AlaNtpPeerListOffset_Object = MibTableColumn
alaNtpPeerListOffset = _AlaNtpPeerListOffset_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 2, 1, 1, 9),
    _AlaNtpPeerListOffset_Type()
)
alaNtpPeerListOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpPeerListOffset.setStatus("current")
_AlaNtpPeerListDispersion_Type = SnmpAdminString
_AlaNtpPeerListDispersion_Object = MibTableColumn
alaNtpPeerListDispersion = _AlaNtpPeerListDispersion_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 2, 1, 1, 10),
    _AlaNtpPeerListDispersion_Type()
)
alaNtpPeerListDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpPeerListDispersion.setStatus("current")


class _AlaNtpPeerListSynced_Type(Integer32):
    """Custom type alaNtpPeerListSynced based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSynchronized", 2),
          ("synchronized", 1))
    )


_AlaNtpPeerListSynced_Type.__name__ = "Integer32"
_AlaNtpPeerListSynced_Object = MibTableColumn
alaNtpPeerListSynced = _AlaNtpPeerListSynced_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 2, 1, 1, 11),
    _AlaNtpPeerListSynced_Type()
)
alaNtpPeerListSynced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpPeerListSynced.setStatus("current")
_AlaNtpPeerListName_Type = SnmpAdminString
_AlaNtpPeerListName_Object = MibTableColumn
alaNtpPeerListName = _AlaNtpPeerListName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 2, 1, 1, 12),
    _AlaNtpPeerListName_Type()
)
alaNtpPeerListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpPeerListName.setStatus("current")
_AlaNtpPeerShowTable_Object = MibTable
alaNtpPeerShowTable = _AlaNtpPeerShowTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    alaNtpPeerShowTable.setStatus("current")
_AlaNtpPeerShowEntry_Object = MibTableRow
alaNtpPeerShowEntry = _AlaNtpPeerShowEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 2, 3, 1)
)
alaNtpPeerShowEntry.setIndexNames(
    (0, "ALCATEL-IND1-NTP-MIB", "alaNtpPeerShowRemoteAddressType"),
    (0, "ALCATEL-IND1-NTP-MIB", "alaNtpPeerShowRemoteAddress"),
)
if mibBuilder.loadTexts:
    alaNtpPeerShowEntry.setStatus("current")
_AlaNtpPeerShowRemoteAddressType_Type = InetAddressType
_AlaNtpPeerShowRemoteAddressType_Object = MibTableColumn
alaNtpPeerShowRemoteAddressType = _AlaNtpPeerShowRemoteAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 2, 3, 1, 1),
    _AlaNtpPeerShowRemoteAddressType_Type()
)
alaNtpPeerShowRemoteAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaNtpPeerShowRemoteAddressType.setStatus("current")
_AlaNtpPeerShowRemoteAddress_Type = InetAddress
_AlaNtpPeerShowRemoteAddress_Object = MibTableColumn
alaNtpPeerShowRemoteAddress = _AlaNtpPeerShowRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 2, 3, 1, 2),
    _AlaNtpPeerShowRemoteAddress_Type()
)
alaNtpPeerShowRemoteAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaNtpPeerShowRemoteAddress.setStatus("current")
_AlaNtpPeerShowRemoteIpAddress_Type = IpAddress
_AlaNtpPeerShowRemoteIpAddress_Object = MibTableColumn
alaNtpPeerShowRemoteIpAddress = _AlaNtpPeerShowRemoteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 2, 3, 1, 3),
    _AlaNtpPeerShowRemoteIpAddress_Type()
)
alaNtpPeerShowRemoteIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpPeerShowRemoteIpAddress.setStatus("current")
_AlaNtpPeerShowLocal_Type = IpAddress
_AlaNtpPeerShowLocal_Object = MibTableColumn
alaNtpPeerShowLocal = _AlaNtpPeerShowLocal_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 2, 3, 1, 4),
    _AlaNtpPeerShowLocal_Type()
)
alaNtpPeerShowLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpPeerShowLocal.setStatus("current")
_AlaNtpPeerShowHmode_Type = SnmpAdminString
_AlaNtpPeerShowHmode_Object = MibTableColumn
alaNtpPeerShowHmode = _AlaNtpPeerShowHmode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 2, 3, 1, 5),
    _AlaNtpPeerShowHmode_Type()
)
alaNtpPeerShowHmode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpPeerShowHmode.setStatus("current")
_AlaNtpPeerShowPmode_Type = SnmpAdminString
_AlaNtpPeerShowPmode_Object = MibTableColumn
alaNtpPeerShowPmode = _AlaNtpPeerShowPmode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 2, 3, 1, 6),
    _AlaNtpPeerShowPmode_Type()
)
alaNtpPeerShowPmode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpPeerShowPmode.setStatus("current")


class _AlaNtpPeerShowStratum_Type(Integer32):
    """Custom type alaNtpPeerShowStratum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AlaNtpPeerShowStratum_Type.__name__ = "Integer32"
_AlaNtpPeerShowStratum_Object = MibTableColumn
alaNtpPeerShowStratum = _AlaNtpPeerShowStratum_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 2, 3, 1, 7),
    _AlaNtpPeerShowStratum_Type()
)
alaNtpPeerShowStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpPeerShowStratum.setStatus("current")


class _AlaNtpPeerShowPrecision_Type(Integer32):
    """Custom type alaNtpPeerShowPrecision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20, -4),
    )


_AlaNtpPeerShowPrecision_Type.__name__ = "Integer32"
_AlaNtpPeerShowPrecision_Object = MibTableColumn
alaNtpPeerShowPrecision = _AlaNtpPeerShowPrecision_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 2, 3, 1, 8),
    _AlaNtpPeerShowPrecision_Type()
)
alaNtpPeerShowPrecision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpPeerShowPrecision.setStatus("current")


class _AlaNtpPeerShowLeapIndicator_Type(Integer32):
    """Custom type alaNtpPeerShowLeapIndicator based on Integer32"""
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
        *(("leapAddSecond", 1),
          ("leapDeleteSecond", 2),
          ("leapNotInSync", 3),
          ("noLeapWarning", 0))
    )


_AlaNtpPeerShowLeapIndicator_Type.__name__ = "Integer32"
_AlaNtpPeerShowLeapIndicator_Object = MibTableColumn
alaNtpPeerShowLeapIndicator = _AlaNtpPeerShowLeapIndicator_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 2, 3, 1, 9),
    _AlaNtpPeerShowLeapIndicator_Type()
)
alaNtpPeerShowLeapIndicator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpPeerShowLeapIndicator.setStatus("current")
_AlaNtpPeerShowReferenceId_Type = SnmpAdminString
_AlaNtpPeerShowReferenceId_Object = MibTableColumn
alaNtpPeerShowReferenceId = _AlaNtpPeerShowReferenceId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 2, 3, 1, 10),
    _AlaNtpPeerShowReferenceId_Type()
)
alaNtpPeerShowReferenceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpPeerShowReferenceId.setStatus("current")
_AlaNtpPeerShowRootDistance_Type = SnmpAdminString
_AlaNtpPeerShowRootDistance_Object = MibTableColumn
alaNtpPeerShowRootDistance = _AlaNtpPeerShowRootDistance_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 2, 3, 1, 11),
    _AlaNtpPeerShowRootDistance_Type()
)
alaNtpPeerShowRootDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpPeerShowRootDistance.setStatus("current")
_AlaNtpPeerShowRootDispersion_Type = SnmpAdminString
_AlaNtpPeerShowRootDispersion_Object = MibTableColumn
alaNtpPeerShowRootDispersion = _AlaNtpPeerShowRootDispersion_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 2, 3, 1, 12),
    _AlaNtpPeerShowRootDispersion_Type()
)
alaNtpPeerShowRootDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpPeerShowRootDispersion.setStatus("current")


class _AlaNtpPeerShowPpoll_Type(Integer32):
    """Custom type alaNtpPeerShowPpoll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaNtpPeerShowPpoll_Type.__name__ = "Integer32"
_AlaNtpPeerShowPpoll_Object = MibTableColumn
alaNtpPeerShowPpoll = _AlaNtpPeerShowPpoll_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 2, 3, 1, 13),
    _AlaNtpPeerShowPpoll_Type()
)
alaNtpPeerShowPpoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpPeerShowPpoll.setStatus("current")


class _AlaNtpPeerShowHpoll_Type(Integer32):
    """Custom type alaNtpPeerShowHpoll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaNtpPeerShowHpoll_Type.__name__ = "Integer32"
_AlaNtpPeerShowHpoll_Object = MibTableColumn
alaNtpPeerShowHpoll = _AlaNtpPeerShowHpoll_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 2, 3, 1, 14),
    _AlaNtpPeerShowHpoll_Type()
)
alaNtpPeerShowHpoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpPeerShowHpoll.setStatus("current")


class _AlaNtpPeerShowKeyid_Type(Integer32):
    """Custom type alaNtpPeerShowKeyid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaNtpPeerShowKeyid_Type.__name__ = "Integer32"
_AlaNtpPeerShowKeyid_Object = MibTableColumn
alaNtpPeerShowKeyid = _AlaNtpPeerShowKeyid_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 2, 3, 1, 15),
    _AlaNtpPeerShowKeyid_Type()
)
alaNtpPeerShowKeyid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpPeerShowKeyid.setStatus("current")


class _AlaNtpPeerShowVersion_Type(Integer32):
    """Custom type alaNtpPeerShowVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AlaNtpPeerShowVersion_Type.__name__ = "Integer32"
_AlaNtpPeerShowVersion_Object = MibTableColumn
alaNtpPeerShowVersion = _AlaNtpPeerShowVersion_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 2, 3, 1, 16),
    _AlaNtpPeerShowVersion_Type()
)
alaNtpPeerShowVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpPeerShowVersion.setStatus("current")


class _AlaNtpPeerShowAssociation_Type(Integer32):
    """Custom type alaNtpPeerShowAssociation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaNtpPeerShowAssociation_Type.__name__ = "Integer32"
_AlaNtpPeerShowAssociation_Object = MibTableColumn
alaNtpPeerShowAssociation = _AlaNtpPeerShowAssociation_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 2, 3, 1, 17),
    _AlaNtpPeerShowAssociation_Type()
)
alaNtpPeerShowAssociation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpPeerShowAssociation.setStatus("current")


class _AlaNtpPeerShowValid_Type(Integer32):
    """Custom type alaNtpPeerShowValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_AlaNtpPeerShowValid_Type.__name__ = "Integer32"
_AlaNtpPeerShowValid_Object = MibTableColumn
alaNtpPeerShowValid = _AlaNtpPeerShowValid_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 2, 3, 1, 18),
    _AlaNtpPeerShowValid_Type()
)
alaNtpPeerShowValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpPeerShowValid.setStatus("current")


class _AlaNtpPeerShowReach_Type(Integer32):
    """Custom type alaNtpPeerShowReach based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaNtpPeerShowReach_Type.__name__ = "Integer32"
_AlaNtpPeerShowReach_Object = MibTableColumn
alaNtpPeerShowReach = _AlaNtpPeerShowReach_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 2, 3, 1, 19),
    _AlaNtpPeerShowReach_Type()
)
alaNtpPeerShowReach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpPeerShowReach.setStatus("current")


class _AlaNtpPeerShowUnreach_Type(Integer32):
    """Custom type alaNtpPeerShowUnreach based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AlaNtpPeerShowUnreach_Type.__name__ = "Integer32"
_AlaNtpPeerShowUnreach_Object = MibTableColumn
alaNtpPeerShowUnreach = _AlaNtpPeerShowUnreach_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 2, 3, 1, 20),
    _AlaNtpPeerShowUnreach_Type()
)
alaNtpPeerShowUnreach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpPeerShowUnreach.setStatus("current")


class _AlaNtpPeerShowFlash_Type(Integer32):
    """Custom type alaNtpPeerShowFlash based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_AlaNtpPeerShowFlash_Type.__name__ = "Integer32"
_AlaNtpPeerShowFlash_Object = MibTableColumn
alaNtpPeerShowFlash = _AlaNtpPeerShowFlash_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 2, 3, 1, 21),
    _AlaNtpPeerShowFlash_Type()
)
alaNtpPeerShowFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpPeerShowFlash.setStatus("current")
_AlaNtpPeerShowBroadcastOffset_Type = SnmpAdminString
_AlaNtpPeerShowBroadcastOffset_Object = MibTableColumn
alaNtpPeerShowBroadcastOffset = _AlaNtpPeerShowBroadcastOffset_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 2, 3, 1, 22),
    _AlaNtpPeerShowBroadcastOffset_Type()
)
alaNtpPeerShowBroadcastOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpPeerShowBroadcastOffset.setStatus("current")


class _AlaNtpPeerShowTTL_Type(Integer32):
    """Custom type alaNtpPeerShowTTL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaNtpPeerShowTTL_Type.__name__ = "Integer32"
_AlaNtpPeerShowTTL_Object = MibTableColumn
alaNtpPeerShowTTL = _AlaNtpPeerShowTTL_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 2, 3, 1, 23),
    _AlaNtpPeerShowTTL_Type()
)
alaNtpPeerShowTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpPeerShowTTL.setStatus("current")


class _AlaNtpPeerShowTimer_Type(Integer32):
    """Custom type alaNtpPeerShowTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlaNtpPeerShowTimer_Type.__name__ = "Integer32"
_AlaNtpPeerShowTimer_Object = MibTableColumn
alaNtpPeerShowTimer = _AlaNtpPeerShowTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 2, 3, 1, 24),
    _AlaNtpPeerShowTimer_Type()
)
alaNtpPeerShowTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpPeerShowTimer.setStatus("current")


class _AlaNtpPeerShowFlags_Type(Integer32):
    """Custom type alaNtpPeerShowFlags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaNtpPeerShowFlags_Type.__name__ = "Integer32"
_AlaNtpPeerShowFlags_Object = MibTableColumn
alaNtpPeerShowFlags = _AlaNtpPeerShowFlags_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 2, 3, 1, 25),
    _AlaNtpPeerShowFlags_Type()
)
alaNtpPeerShowFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpPeerShowFlags.setStatus("current")
_AlaNtpPeerShowReferenceTime_Type = SnmpAdminString
_AlaNtpPeerShowReferenceTime_Object = MibTableColumn
alaNtpPeerShowReferenceTime = _AlaNtpPeerShowReferenceTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 2, 3, 1, 26),
    _AlaNtpPeerShowReferenceTime_Type()
)
alaNtpPeerShowReferenceTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpPeerShowReferenceTime.setStatus("current")
_AlaNtpPeerShowOriginateTime_Type = SnmpAdminString
_AlaNtpPeerShowOriginateTime_Object = MibTableColumn
alaNtpPeerShowOriginateTime = _AlaNtpPeerShowOriginateTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 2, 3, 1, 27),
    _AlaNtpPeerShowOriginateTime_Type()
)
alaNtpPeerShowOriginateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpPeerShowOriginateTime.setStatus("current")
_AlaNtpPeerShowReceiveTime_Type = SnmpAdminString
_AlaNtpPeerShowReceiveTime_Object = MibTableColumn
alaNtpPeerShowReceiveTime = _AlaNtpPeerShowReceiveTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 2, 3, 1, 28),
    _AlaNtpPeerShowReceiveTime_Type()
)
alaNtpPeerShowReceiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpPeerShowReceiveTime.setStatus("current")
_AlaNtpPeerShowTransmitTime_Type = SnmpAdminString
_AlaNtpPeerShowTransmitTime_Object = MibTableColumn
alaNtpPeerShowTransmitTime = _AlaNtpPeerShowTransmitTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 2, 3, 1, 29),
    _AlaNtpPeerShowTransmitTime_Type()
)
alaNtpPeerShowTransmitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpPeerShowTransmitTime.setStatus("current")
_AlaNtpPeerShowOffset_Type = SnmpAdminString
_AlaNtpPeerShowOffset_Object = MibTableColumn
alaNtpPeerShowOffset = _AlaNtpPeerShowOffset_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 2, 3, 1, 30),
    _AlaNtpPeerShowOffset_Type()
)
alaNtpPeerShowOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpPeerShowOffset.setStatus("current")
_AlaNtpPeerShowDelay_Type = SnmpAdminString
_AlaNtpPeerShowDelay_Object = MibTableColumn
alaNtpPeerShowDelay = _AlaNtpPeerShowDelay_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 2, 3, 1, 31),
    _AlaNtpPeerShowDelay_Type()
)
alaNtpPeerShowDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpPeerShowDelay.setStatus("current")
_AlaNtpPeerShowDispersion_Type = SnmpAdminString
_AlaNtpPeerShowDispersion_Object = MibTableColumn
alaNtpPeerShowDispersion = _AlaNtpPeerShowDispersion_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 2, 3, 1, 32),
    _AlaNtpPeerShowDispersion_Type()
)
alaNtpPeerShowDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpPeerShowDispersion.setStatus("current")
_AlaNtpPeerShowName_Type = SnmpAdminString
_AlaNtpPeerShowName_Object = MibTableColumn
alaNtpPeerShowName = _AlaNtpPeerShowName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 2, 3, 1, 33),
    _AlaNtpPeerShowName_Type()
)
alaNtpPeerShowName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpPeerShowName.setStatus("current")


class _AlaNtpPeerShowStatus_Type(Bits):
    """Custom type alaNtpPeerShowStatus based on Bits"""
    namedValues = NamedValues(
        *(("authenticated", 9),
          ("authenticationRequired", 10),
          ("candidate", 4),
          ("configured", 11),
          ("exceedsMaxDistance", 5),
          ("excess", 2),
          ("falsticker", 1),
          ("outlyer", 3),
          ("reachable", 8),
          ("rejected", 0),
          ("selected", 6),
          ("selectedPPS", 7))
    )

_AlaNtpPeerShowStatus_Type.__name__ = "Bits"
_AlaNtpPeerShowStatus_Object = MibTableColumn
alaNtpPeerShowStatus = _AlaNtpPeerShowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 2, 3, 1, 34),
    _AlaNtpPeerShowStatus_Type()
)
alaNtpPeerShowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpPeerShowStatus.setStatus("current")
_AlaNtpClientListTable_Object = MibTable
alaNtpClientListTable = _AlaNtpClientListTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 2, 4)
)
if mibBuilder.loadTexts:
    alaNtpClientListTable.setStatus("current")
_AlaNtpClientListEntry_Object = MibTableRow
alaNtpClientListEntry = _AlaNtpClientListEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 2, 4, 1)
)
alaNtpClientListEntry.setIndexNames(
    (0, "ALCATEL-IND1-NTP-MIB", "alaNtpClientListAddressType"),
    (0, "ALCATEL-IND1-NTP-MIB", "alaNtpClientListAddress"),
)
if mibBuilder.loadTexts:
    alaNtpClientListEntry.setStatus("current")


class _AlaNtpClientListAddressType_Type(InetAddressType):
    """Custom type alaNtpClientListAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_AlaNtpClientListAddressType_Type.__name__ = "InetAddressType"
_AlaNtpClientListAddressType_Object = MibTableColumn
alaNtpClientListAddressType = _AlaNtpClientListAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 2, 4, 1, 1),
    _AlaNtpClientListAddressType_Type()
)
alaNtpClientListAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaNtpClientListAddressType.setStatus("current")
_AlaNtpClientListAddress_Type = InetAddress
_AlaNtpClientListAddress_Object = MibTableColumn
alaNtpClientListAddress = _AlaNtpClientListAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 2, 4, 1, 2),
    _AlaNtpClientListAddress_Type()
)
alaNtpClientListAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaNtpClientListAddress.setStatus("current")


class _AlaNtpClientListVersion_Type(Integer32):
    """Custom type alaNtpClientListVersion based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 4),
    )


_AlaNtpClientListVersion_Type.__name__ = "Integer32"
_AlaNtpClientListVersion_Object = MibTableColumn
alaNtpClientListVersion = _AlaNtpClientListVersion_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 2, 4, 1, 3),
    _AlaNtpClientListVersion_Type()
)
alaNtpClientListVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpClientListVersion.setStatus("current")


class _AlaNtpClientKey_Type(Integer32):
    """Custom type alaNtpClientKey based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaNtpClientKey_Type.__name__ = "Integer32"
_AlaNtpClientKey_Object = MibTableColumn
alaNtpClientKey = _AlaNtpClientKey_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 2, 4, 1, 4),
    _AlaNtpClientKey_Type()
)
alaNtpClientKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpClientKey.setStatus("current")
_AlaNtpStats_ObjectIdentity = ObjectIdentity
alaNtpStats = _AlaNtpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 3)
)
_AlaNtpStatsPeerTable_Object = MibTable
alaNtpStatsPeerTable = _AlaNtpStatsPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    alaNtpStatsPeerTable.setStatus("current")
_AlaNtpStatsPeerEntry_Object = MibTableRow
alaNtpStatsPeerEntry = _AlaNtpStatsPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 3, 2, 1)
)
alaNtpStatsPeerEntry.setIndexNames(
    (0, "ALCATEL-IND1-NTP-MIB", "alaNtpStatsPeerAddressType"),
    (0, "ALCATEL-IND1-NTP-MIB", "alaNtpStatsPeerAddress"),
)
if mibBuilder.loadTexts:
    alaNtpStatsPeerEntry.setStatus("current")
_AlaNtpStatsPeerAddressType_Type = InetAddressType
_AlaNtpStatsPeerAddressType_Object = MibTableColumn
alaNtpStatsPeerAddressType = _AlaNtpStatsPeerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 3, 2, 1, 1),
    _AlaNtpStatsPeerAddressType_Type()
)
alaNtpStatsPeerAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaNtpStatsPeerAddressType.setStatus("current")
_AlaNtpStatsPeerAddress_Type = InetAddress
_AlaNtpStatsPeerAddress_Object = MibTableColumn
alaNtpStatsPeerAddress = _AlaNtpStatsPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 3, 2, 1, 2),
    _AlaNtpStatsPeerAddress_Type()
)
alaNtpStatsPeerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaNtpStatsPeerAddress.setStatus("current")
_AlaNtpStatsPeerIpAddress_Type = IpAddress
_AlaNtpStatsPeerIpAddress_Object = MibTableColumn
alaNtpStatsPeerIpAddress = _AlaNtpStatsPeerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 3, 2, 1, 3),
    _AlaNtpStatsPeerIpAddress_Type()
)
alaNtpStatsPeerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpStatsPeerIpAddress.setStatus("current")
_AlaNtpStatsPeerLocal_Type = IpAddress
_AlaNtpStatsPeerLocal_Object = MibTableColumn
alaNtpStatsPeerLocal = _AlaNtpStatsPeerLocal_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 3, 2, 1, 4),
    _AlaNtpStatsPeerLocal_Type()
)
alaNtpStatsPeerLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpStatsPeerLocal.setStatus("current")
_AlaNtpStatsPeerLastRcv_Type = Counter32
_AlaNtpStatsPeerLastRcv_Object = MibTableColumn
alaNtpStatsPeerLastRcv = _AlaNtpStatsPeerLastRcv_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 3, 2, 1, 5),
    _AlaNtpStatsPeerLastRcv_Type()
)
alaNtpStatsPeerLastRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpStatsPeerLastRcv.setStatus("current")
_AlaNtpStatsPeerNextSend_Type = Counter32
_AlaNtpStatsPeerNextSend_Object = MibTableColumn
alaNtpStatsPeerNextSend = _AlaNtpStatsPeerNextSend_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 3, 2, 1, 6),
    _AlaNtpStatsPeerNextSend_Type()
)
alaNtpStatsPeerNextSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpStatsPeerNextSend.setStatus("current")
_AlaNtpStatsPeerReachChange_Type = Counter32
_AlaNtpStatsPeerReachChange_Object = MibTableColumn
alaNtpStatsPeerReachChange = _AlaNtpStatsPeerReachChange_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 3, 2, 1, 7),
    _AlaNtpStatsPeerReachChange_Type()
)
alaNtpStatsPeerReachChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpStatsPeerReachChange.setStatus("current")
_AlaNtpStatsPeerPacketsSent_Type = Counter32
_AlaNtpStatsPeerPacketsSent_Object = MibTableColumn
alaNtpStatsPeerPacketsSent = _AlaNtpStatsPeerPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 3, 2, 1, 8),
    _AlaNtpStatsPeerPacketsSent_Type()
)
alaNtpStatsPeerPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpStatsPeerPacketsSent.setStatus("current")
_AlaNtpStatsPeerPacketsRcvd_Type = Counter32
_AlaNtpStatsPeerPacketsRcvd_Object = MibTableColumn
alaNtpStatsPeerPacketsRcvd = _AlaNtpStatsPeerPacketsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 3, 2, 1, 9),
    _AlaNtpStatsPeerPacketsRcvd_Type()
)
alaNtpStatsPeerPacketsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpStatsPeerPacketsRcvd.setStatus("current")
_AlaNtpStatsPeerBadAuth_Type = Counter32
_AlaNtpStatsPeerBadAuth_Object = MibTableColumn
alaNtpStatsPeerBadAuth = _AlaNtpStatsPeerBadAuth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 3, 2, 1, 10),
    _AlaNtpStatsPeerBadAuth_Type()
)
alaNtpStatsPeerBadAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpStatsPeerBadAuth.setStatus("current")
_AlaNtpStatsPeerBogusOrigin_Type = Counter32
_AlaNtpStatsPeerBogusOrigin_Object = MibTableColumn
alaNtpStatsPeerBogusOrigin = _AlaNtpStatsPeerBogusOrigin_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 3, 2, 1, 11),
    _AlaNtpStatsPeerBogusOrigin_Type()
)
alaNtpStatsPeerBogusOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpStatsPeerBogusOrigin.setStatus("current")
_AlaNtpStatsPeerDuplicate_Type = Counter32
_AlaNtpStatsPeerDuplicate_Object = MibTableColumn
alaNtpStatsPeerDuplicate = _AlaNtpStatsPeerDuplicate_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 3, 2, 1, 12),
    _AlaNtpStatsPeerDuplicate_Type()
)
alaNtpStatsPeerDuplicate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpStatsPeerDuplicate.setStatus("current")
_AlaNtpStatsPeerBadDispersion_Type = Counter32
_AlaNtpStatsPeerBadDispersion_Object = MibTableColumn
alaNtpStatsPeerBadDispersion = _AlaNtpStatsPeerBadDispersion_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 3, 2, 1, 13),
    _AlaNtpStatsPeerBadDispersion_Type()
)
alaNtpStatsPeerBadDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpStatsPeerBadDispersion.setStatus("current")
_AlaNtpStatsPeerBadRefTime_Type = Counter32
_AlaNtpStatsPeerBadRefTime_Object = MibTableColumn
alaNtpStatsPeerBadRefTime = _AlaNtpStatsPeerBadRefTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 3, 2, 1, 14),
    _AlaNtpStatsPeerBadRefTime_Type()
)
alaNtpStatsPeerBadRefTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpStatsPeerBadRefTime.setStatus("deprecated")
_AlaNtpStatsPeerCandidateOrder_Type = Counter32
_AlaNtpStatsPeerCandidateOrder_Object = MibTableColumn
alaNtpStatsPeerCandidateOrder = _AlaNtpStatsPeerCandidateOrder_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 3, 2, 1, 15),
    _AlaNtpStatsPeerCandidateOrder_Type()
)
alaNtpStatsPeerCandidateOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpStatsPeerCandidateOrder.setStatus("current")


class _AlaNtpStatsPeerReset_Type(Integer32):
    """Custom type alaNtpStatsPeerReset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlaNtpStatsPeerReset_Type.__name__ = "Integer32"
_AlaNtpStatsPeerReset_Object = MibTableColumn
alaNtpStatsPeerReset = _AlaNtpStatsPeerReset_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 3, 2, 1, 16),
    _AlaNtpStatsPeerReset_Type()
)
alaNtpStatsPeerReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaNtpStatsPeerReset.setStatus("current")
_AlaNtpStatsPeerName_Type = SnmpAdminString
_AlaNtpStatsPeerName_Object = MibTableColumn
alaNtpStatsPeerName = _AlaNtpStatsPeerName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 3, 2, 1, 17),
    _AlaNtpStatsPeerName_Type()
)
alaNtpStatsPeerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpStatsPeerName.setStatus("current")


class _AlaNtpStatsReset_Type(Integer32):
    """Custom type alaNtpStatsReset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_AlaNtpStatsReset_Type.__name__ = "Integer32"
_AlaNtpStatsReset_Object = MibScalar
alaNtpStatsReset = _AlaNtpStatsReset_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 3, 5),
    _AlaNtpStatsReset_Type()
)
alaNtpStatsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaNtpStatsReset.setStatus("current")
_AlaNtpStatsMonitorTable_Object = MibTable
alaNtpStatsMonitorTable = _AlaNtpStatsMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 3, 6)
)
if mibBuilder.loadTexts:
    alaNtpStatsMonitorTable.setStatus("current")
_AlaNtpStatsMonitorEntry_Object = MibTableRow
alaNtpStatsMonitorEntry = _AlaNtpStatsMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 3, 6, 1)
)
alaNtpStatsMonitorEntry.setIndexNames(
    (0, "ALCATEL-IND1-NTP-MIB", "alaNtpStatsMonitorIndex"),
)
if mibBuilder.loadTexts:
    alaNtpStatsMonitorEntry.setStatus("current")


class _AlaNtpStatsMonitorIndex_Type(Unsigned32):
    """Custom type alaNtpStatsMonitorIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AlaNtpStatsMonitorIndex_Type.__name__ = "Unsigned32"
_AlaNtpStatsMonitorIndex_Object = MibTableColumn
alaNtpStatsMonitorIndex = _AlaNtpStatsMonitorIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 3, 6, 1, 1),
    _AlaNtpStatsMonitorIndex_Type()
)
alaNtpStatsMonitorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaNtpStatsMonitorIndex.setStatus("current")
_AlaNtpStatsMonitorAddress_Type = IpAddress
_AlaNtpStatsMonitorAddress_Object = MibTableColumn
alaNtpStatsMonitorAddress = _AlaNtpStatsMonitorAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 3, 6, 1, 2),
    _AlaNtpStatsMonitorAddress_Type()
)
alaNtpStatsMonitorAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpStatsMonitorAddress.setStatus("current")


class _AlaNtpStatsMonitorPort_Type(Integer32):
    """Custom type alaNtpStatsMonitorPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaNtpStatsMonitorPort_Type.__name__ = "Integer32"
_AlaNtpStatsMonitorPort_Object = MibTableColumn
alaNtpStatsMonitorPort = _AlaNtpStatsMonitorPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 3, 6, 1, 3),
    _AlaNtpStatsMonitorPort_Type()
)
alaNtpStatsMonitorPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpStatsMonitorPort.setStatus("current")
_AlaNtpStatsMonitorLocalAddress_Type = IpAddress
_AlaNtpStatsMonitorLocalAddress_Object = MibTableColumn
alaNtpStatsMonitorLocalAddress = _AlaNtpStatsMonitorLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 3, 6, 1, 4),
    _AlaNtpStatsMonitorLocalAddress_Type()
)
alaNtpStatsMonitorLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpStatsMonitorLocalAddress.setStatus("current")
_AlaNtpStatsMonitorCount_Type = Counter32
_AlaNtpStatsMonitorCount_Object = MibTableColumn
alaNtpStatsMonitorCount = _AlaNtpStatsMonitorCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 3, 6, 1, 5),
    _AlaNtpStatsMonitorCount_Type()
)
alaNtpStatsMonitorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpStatsMonitorCount.setStatus("current")
_AlaNtpStatsMonitorMode_Type = SnmpAdminString
_AlaNtpStatsMonitorMode_Object = MibTableColumn
alaNtpStatsMonitorMode = _AlaNtpStatsMonitorMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 3, 6, 1, 6),
    _AlaNtpStatsMonitorMode_Type()
)
alaNtpStatsMonitorMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpStatsMonitorMode.setStatus("current")


class _AlaNtpStatsMonitorVersion_Type(Integer32):
    """Custom type alaNtpStatsMonitorVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AlaNtpStatsMonitorVersion_Type.__name__ = "Integer32"
_AlaNtpStatsMonitorVersion_Object = MibTableColumn
alaNtpStatsMonitorVersion = _AlaNtpStatsMonitorVersion_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 3, 6, 1, 7),
    _AlaNtpStatsMonitorVersion_Type()
)
alaNtpStatsMonitorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpStatsMonitorVersion.setStatus("current")
_AlaNtpStatsMonitorDrop_Type = Counter32
_AlaNtpStatsMonitorDrop_Object = MibTableColumn
alaNtpStatsMonitorDrop = _AlaNtpStatsMonitorDrop_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 3, 6, 1, 8),
    _AlaNtpStatsMonitorDrop_Type()
)
alaNtpStatsMonitorDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpStatsMonitorDrop.setStatus("current")
_AlaNtpStatsMonitorLast_Type = Counter32
_AlaNtpStatsMonitorLast_Object = MibTableColumn
alaNtpStatsMonitorLast = _AlaNtpStatsMonitorLast_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 3, 6, 1, 9),
    _AlaNtpStatsMonitorLast_Type()
)
alaNtpStatsMonitorLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpStatsMonitorLast.setStatus("current")
_AlaNtpStatsMonitorFirst_Type = Counter32
_AlaNtpStatsMonitorFirst_Object = MibTableColumn
alaNtpStatsMonitorFirst = _AlaNtpStatsMonitorFirst_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 3, 6, 1, 10),
    _AlaNtpStatsMonitorFirst_Type()
)
alaNtpStatsMonitorFirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpStatsMonitorFirst.setStatus("current")
_AlaNtpStatsMonitorName_Type = SnmpAdminString
_AlaNtpStatsMonitorName_Object = MibTableColumn
alaNtpStatsMonitorName = _AlaNtpStatsMonitorName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 3, 6, 1, 11),
    _AlaNtpStatsMonitorName_Type()
)
alaNtpStatsMonitorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpStatsMonitorName.setStatus("current")
_AlaNtpStatsStat_ObjectIdentity = ObjectIdentity
alaNtpStatsStat = _AlaNtpStatsStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 4)
)
_AlaNtpStatsStatUptime_Type = Counter32
_AlaNtpStatsStatUptime_Object = MibScalar
alaNtpStatsStatUptime = _AlaNtpStatsStatUptime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 4, 1),
    _AlaNtpStatsStatUptime_Type()
)
alaNtpStatsStatUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpStatsStatUptime.setStatus("current")
_AlaNtpStatsStatReset_Type = Counter32
_AlaNtpStatsStatReset_Object = MibScalar
alaNtpStatsStatReset = _AlaNtpStatsStatReset_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 4, 2),
    _AlaNtpStatsStatReset_Type()
)
alaNtpStatsStatReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpStatsStatReset.setStatus("current")
_AlaNtpStatsStatBadStratum_Type = Counter32
_AlaNtpStatsStatBadStratum_Object = MibScalar
alaNtpStatsStatBadStratum = _AlaNtpStatsStatBadStratum_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 4, 3),
    _AlaNtpStatsStatBadStratum_Type()
)
alaNtpStatsStatBadStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpStatsStatBadStratum.setStatus("current")
_AlaNtpStatsStatOldVersion_Type = Counter32
_AlaNtpStatsStatOldVersion_Object = MibScalar
alaNtpStatsStatOldVersion = _AlaNtpStatsStatOldVersion_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 4, 4),
    _AlaNtpStatsStatOldVersion_Type()
)
alaNtpStatsStatOldVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpStatsStatOldVersion.setStatus("current")
_AlaNtpStatsStatNewVersion_Type = Counter32
_AlaNtpStatsStatNewVersion_Object = MibScalar
alaNtpStatsStatNewVersion = _AlaNtpStatsStatNewVersion_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 4, 5),
    _AlaNtpStatsStatNewVersion_Type()
)
alaNtpStatsStatNewVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpStatsStatNewVersion.setStatus("current")
_AlaNtpStatsStatUnknownVersion_Type = Counter32
_AlaNtpStatsStatUnknownVersion_Object = MibScalar
alaNtpStatsStatUnknownVersion = _AlaNtpStatsStatUnknownVersion_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 4, 6),
    _AlaNtpStatsStatUnknownVersion_Type()
)
alaNtpStatsStatUnknownVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpStatsStatUnknownVersion.setStatus("current")
_AlaNtpStatsStatBadLength_Type = Counter32
_AlaNtpStatsStatBadLength_Object = MibScalar
alaNtpStatsStatBadLength = _AlaNtpStatsStatBadLength_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 4, 7),
    _AlaNtpStatsStatBadLength_Type()
)
alaNtpStatsStatBadLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpStatsStatBadLength.setStatus("current")
_AlaNtpStatsStatProcessed_Type = Counter32
_AlaNtpStatsStatProcessed_Object = MibScalar
alaNtpStatsStatProcessed = _AlaNtpStatsStatProcessed_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 4, 8),
    _AlaNtpStatsStatProcessed_Type()
)
alaNtpStatsStatProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpStatsStatProcessed.setStatus("current")
_AlaNtpStatsStatBadAuth_Type = Counter32
_AlaNtpStatsStatBadAuth_Object = MibScalar
alaNtpStatsStatBadAuth = _AlaNtpStatsStatBadAuth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 4, 9),
    _AlaNtpStatsStatBadAuth_Type()
)
alaNtpStatsStatBadAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpStatsStatBadAuth.setStatus("current")
_AlaNtpStatsStatLimitRejects_Type = Counter32
_AlaNtpStatsStatLimitRejects_Object = MibScalar
alaNtpStatsStatLimitRejects = _AlaNtpStatsStatLimitRejects_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 4, 10),
    _AlaNtpStatsStatLimitRejects_Type()
)
alaNtpStatsStatLimitRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpStatsStatLimitRejects.setStatus("current")
_AlaNtpStatsLoop_ObjectIdentity = ObjectIdentity
alaNtpStatsLoop = _AlaNtpStatsLoop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 5)
)
_AlaNtpStatsLoopOffset_Type = SnmpAdminString
_AlaNtpStatsLoopOffset_Object = MibScalar
alaNtpStatsLoopOffset = _AlaNtpStatsLoopOffset_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 5, 1),
    _AlaNtpStatsLoopOffset_Type()
)
alaNtpStatsLoopOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpStatsLoopOffset.setStatus("current")
_AlaNtpStatsLoopFrequency_Type = SnmpAdminString
_AlaNtpStatsLoopFrequency_Object = MibScalar
alaNtpStatsLoopFrequency = _AlaNtpStatsLoopFrequency_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 5, 2),
    _AlaNtpStatsLoopFrequency_Type()
)
alaNtpStatsLoopFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpStatsLoopFrequency.setStatus("current")


class _AlaNtpStatsLoopPollAdjust_Type(Integer32):
    """Custom type alaNtpStatsLoopPollAdjust based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-30, 30),
    )


_AlaNtpStatsLoopPollAdjust_Type.__name__ = "Integer32"
_AlaNtpStatsLoopPollAdjust_Object = MibScalar
alaNtpStatsLoopPollAdjust = _AlaNtpStatsLoopPollAdjust_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 5, 3),
    _AlaNtpStatsLoopPollAdjust_Type()
)
alaNtpStatsLoopPollAdjust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpStatsLoopPollAdjust.setStatus("current")
_AlaNtpStatsLoopWatchdog_Type = Counter32
_AlaNtpStatsLoopWatchdog_Object = MibScalar
alaNtpStatsLoopWatchdog = _AlaNtpStatsLoopWatchdog_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 5, 4),
    _AlaNtpStatsLoopWatchdog_Type()
)
alaNtpStatsLoopWatchdog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpStatsLoopWatchdog.setStatus("current")
_AlaNtpStatsIo_ObjectIdentity = ObjectIdentity
alaNtpStatsIo = _AlaNtpStatsIo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 6)
)
_AlaNtpStatsIoReset_Type = Counter32
_AlaNtpStatsIoReset_Object = MibScalar
alaNtpStatsIoReset = _AlaNtpStatsIoReset_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 6, 1),
    _AlaNtpStatsIoReset_Type()
)
alaNtpStatsIoReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpStatsIoReset.setStatus("current")
_AlaNtpStatsIoRcvBuffers_Type = Counter32
_AlaNtpStatsIoRcvBuffers_Object = MibScalar
alaNtpStatsIoRcvBuffers = _AlaNtpStatsIoRcvBuffers_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 6, 2),
    _AlaNtpStatsIoRcvBuffers_Type()
)
alaNtpStatsIoRcvBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpStatsIoRcvBuffers.setStatus("current")
_AlaNtpStatsIoFreeRcvBuffers_Type = Counter32
_AlaNtpStatsIoFreeRcvBuffers_Object = MibScalar
alaNtpStatsIoFreeRcvBuffers = _AlaNtpStatsIoFreeRcvBuffers_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 6, 3),
    _AlaNtpStatsIoFreeRcvBuffers_Type()
)
alaNtpStatsIoFreeRcvBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpStatsIoFreeRcvBuffers.setStatus("current")
_AlaNtpStatsIoUsedRcvBuffers_Type = Counter32
_AlaNtpStatsIoUsedRcvBuffers_Object = MibScalar
alaNtpStatsIoUsedRcvBuffers = _AlaNtpStatsIoUsedRcvBuffers_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 6, 4),
    _AlaNtpStatsIoUsedRcvBuffers_Type()
)
alaNtpStatsIoUsedRcvBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpStatsIoUsedRcvBuffers.setStatus("current")
_AlaNtpStatsIoRefills_Type = Counter32
_AlaNtpStatsIoRefills_Object = MibScalar
alaNtpStatsIoRefills = _AlaNtpStatsIoRefills_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 6, 5),
    _AlaNtpStatsIoRefills_Type()
)
alaNtpStatsIoRefills.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpStatsIoRefills.setStatus("current")
_AlaNtpStatsIoDroppedPackets_Type = Counter32
_AlaNtpStatsIoDroppedPackets_Object = MibScalar
alaNtpStatsIoDroppedPackets = _AlaNtpStatsIoDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 6, 6),
    _AlaNtpStatsIoDroppedPackets_Type()
)
alaNtpStatsIoDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpStatsIoDroppedPackets.setStatus("current")
_AlaNtpStatsIoIgnoredPackets_Type = Counter32
_AlaNtpStatsIoIgnoredPackets_Object = MibScalar
alaNtpStatsIoIgnoredPackets = _AlaNtpStatsIoIgnoredPackets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 6, 7),
    _AlaNtpStatsIoIgnoredPackets_Type()
)
alaNtpStatsIoIgnoredPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpStatsIoIgnoredPackets.setStatus("current")
_AlaNtpStatsIoRcvPackets_Type = Counter32
_AlaNtpStatsIoRcvPackets_Object = MibScalar
alaNtpStatsIoRcvPackets = _AlaNtpStatsIoRcvPackets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 6, 8),
    _AlaNtpStatsIoRcvPackets_Type()
)
alaNtpStatsIoRcvPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpStatsIoRcvPackets.setStatus("current")
_AlaNtpStatsIoSentPackets_Type = Counter32
_AlaNtpStatsIoSentPackets_Object = MibScalar
alaNtpStatsIoSentPackets = _AlaNtpStatsIoSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 6, 9),
    _AlaNtpStatsIoSentPackets_Type()
)
alaNtpStatsIoSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpStatsIoSentPackets.setStatus("current")
_AlaNtpStatsIoNotSentPackets_Type = Counter32
_AlaNtpStatsIoNotSentPackets_Object = MibScalar
alaNtpStatsIoNotSentPackets = _AlaNtpStatsIoNotSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 6, 10),
    _AlaNtpStatsIoNotSentPackets_Type()
)
alaNtpStatsIoNotSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpStatsIoNotSentPackets.setStatus("current")
_AlaNtpStatsIoInterrupts_Type = Counter32
_AlaNtpStatsIoInterrupts_Object = MibScalar
alaNtpStatsIoInterrupts = _AlaNtpStatsIoInterrupts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 6, 11),
    _AlaNtpStatsIoInterrupts_Type()
)
alaNtpStatsIoInterrupts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpStatsIoInterrupts.setStatus("current")
_AlaNtpStatsIoInterruptsRcv_Type = Counter32
_AlaNtpStatsIoInterruptsRcv_Object = MibScalar
alaNtpStatsIoInterruptsRcv = _AlaNtpStatsIoInterruptsRcv_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 6, 12),
    _AlaNtpStatsIoInterruptsRcv_Type()
)
alaNtpStatsIoInterruptsRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpStatsIoInterruptsRcv.setStatus("current")
_AlaNtpAccess_ObjectIdentity = ObjectIdentity
alaNtpAccess = _AlaNtpAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 7)
)
_AlaNtpAccessKeyIdTable_Object = MibTable
alaNtpAccessKeyIdTable = _AlaNtpAccessKeyIdTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 7, 1)
)
if mibBuilder.loadTexts:
    alaNtpAccessKeyIdTable.setStatus("current")
_AlaNtpAccessKeyIdEntry_Object = MibTableRow
alaNtpAccessKeyIdEntry = _AlaNtpAccessKeyIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 7, 1, 1)
)
alaNtpAccessKeyIdEntry.setIndexNames(
    (0, "ALCATEL-IND1-NTP-MIB", "alaNtpAccessKeyIdKeyId"),
)
if mibBuilder.loadTexts:
    alaNtpAccessKeyIdEntry.setStatus("current")


class _AlaNtpAccessKeyIdKeyId_Type(Integer32):
    """Custom type alaNtpAccessKeyIdKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaNtpAccessKeyIdKeyId_Type.__name__ = "Integer32"
_AlaNtpAccessKeyIdKeyId_Object = MibTableColumn
alaNtpAccessKeyIdKeyId = _AlaNtpAccessKeyIdKeyId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 7, 1, 1, 1),
    _AlaNtpAccessKeyIdKeyId_Type()
)
alaNtpAccessKeyIdKeyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaNtpAccessKeyIdKeyId.setStatus("current")


class _AlaNtpAccessKeyIdTrust_Type(Integer32):
    """Custom type alaNtpAccessKeyIdTrust based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("trusted", 1),
          ("untrusted", 2))
    )


_AlaNtpAccessKeyIdTrust_Type.__name__ = "Integer32"
_AlaNtpAccessKeyIdTrust_Object = MibTableColumn
alaNtpAccessKeyIdTrust = _AlaNtpAccessKeyIdTrust_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 7, 1, 1, 2),
    _AlaNtpAccessKeyIdTrust_Type()
)
alaNtpAccessKeyIdTrust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaNtpAccessKeyIdTrust.setStatus("current")
_AlaNtpAccessRestrictedTable_Object = MibTable
alaNtpAccessRestrictedTable = _AlaNtpAccessRestrictedTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 7, 2)
)
if mibBuilder.loadTexts:
    alaNtpAccessRestrictedTable.setStatus("current")
_AlaNtpAccessRestrictedEntry_Object = MibTableRow
alaNtpAccessRestrictedEntry = _AlaNtpAccessRestrictedEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 7, 2, 1)
)
alaNtpAccessRestrictedEntry.setIndexNames(
    (0, "ALCATEL-IND1-NTP-MIB", "alaNtpAccessRestrictedIpAddress"),
    (0, "ALCATEL-IND1-NTP-MIB", "alaNtpAccessRestrictedMask"),
)
if mibBuilder.loadTexts:
    alaNtpAccessRestrictedEntry.setStatus("current")
_AlaNtpAccessRestrictedIpAddress_Type = IpAddress
_AlaNtpAccessRestrictedIpAddress_Object = MibTableColumn
alaNtpAccessRestrictedIpAddress = _AlaNtpAccessRestrictedIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 7, 2, 1, 1),
    _AlaNtpAccessRestrictedIpAddress_Type()
)
alaNtpAccessRestrictedIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaNtpAccessRestrictedIpAddress.setStatus("current")
_AlaNtpAccessRestrictedMask_Type = IpAddress
_AlaNtpAccessRestrictedMask_Object = MibTableColumn
alaNtpAccessRestrictedMask = _AlaNtpAccessRestrictedMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 7, 2, 1, 2),
    _AlaNtpAccessRestrictedMask_Type()
)
alaNtpAccessRestrictedMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaNtpAccessRestrictedMask.setStatus("current")


class _AlaNtpAccessRestrictedRestrictions_Type(Integer32):
    """Custom type alaNtpAccessRestrictedRestrictions based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_AlaNtpAccessRestrictedRestrictions_Type.__name__ = "Integer32"
_AlaNtpAccessRestrictedRestrictions_Object = MibTableColumn
alaNtpAccessRestrictedRestrictions = _AlaNtpAccessRestrictedRestrictions_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 7, 2, 1, 3),
    _AlaNtpAccessRestrictedRestrictions_Type()
)
alaNtpAccessRestrictedRestrictions.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaNtpAccessRestrictedRestrictions.setStatus("current")
_AlaNtpAccessRestrictedCount_Type = Counter32
_AlaNtpAccessRestrictedCount_Object = MibTableColumn
alaNtpAccessRestrictedCount = _AlaNtpAccessRestrictedCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 7, 2, 1, 4),
    _AlaNtpAccessRestrictedCount_Type()
)
alaNtpAccessRestrictedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpAccessRestrictedCount.setStatus("current")
_AlaNtpAccessRestrictedRowStatus_Type = RowStatus
_AlaNtpAccessRestrictedRowStatus_Object = MibTableColumn
alaNtpAccessRestrictedRowStatus = _AlaNtpAccessRestrictedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 7, 2, 1, 5),
    _AlaNtpAccessRestrictedRowStatus_Type()
)
alaNtpAccessRestrictedRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaNtpAccessRestrictedRowStatus.setStatus("current")


class _AlaNtpAccessRereadKeyFile_Type(Integer32):
    """Custom type alaNtpAccessRereadKeyFile based on Integer32"""
    defaultValue = 3

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
        *(("error", 4),
          ("inProgress", 2),
          ("reload", 1),
          ("successful", 3))
    )


_AlaNtpAccessRereadKeyFile_Type.__name__ = "Integer32"
_AlaNtpAccessRereadKeyFile_Object = MibScalar
alaNtpAccessRereadKeyFile = _AlaNtpAccessRereadKeyFile_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 7, 3),
    _AlaNtpAccessRereadKeyFile_Type()
)
alaNtpAccessRereadKeyFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaNtpAccessRereadKeyFile.setStatus("current")
_AlaNtpLocalInfo_ObjectIdentity = ObjectIdentity
alaNtpLocalInfo = _AlaNtpLocalInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 8)
)
_AlaNtpInfoPeer_Type = IpAddress
_AlaNtpInfoPeer_Object = MibScalar
alaNtpInfoPeer = _AlaNtpInfoPeer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 8, 1),
    _AlaNtpInfoPeer_Type()
)
alaNtpInfoPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpInfoPeer.setStatus("current")
_AlaNtpInfoMode_Type = SnmpAdminString
_AlaNtpInfoMode_Object = MibScalar
alaNtpInfoMode = _AlaNtpInfoMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 8, 2),
    _AlaNtpInfoMode_Type()
)
alaNtpInfoMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpInfoMode.setStatus("current")


class _AlaNtpInfoLeapIndicator_Type(Integer32):
    """Custom type alaNtpInfoLeapIndicator based on Integer32"""
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
        *(("leapAddSecond", 1),
          ("leapDeleteSecond", 2),
          ("leapNotInSync", 3),
          ("noLeapWarning", 0))
    )


_AlaNtpInfoLeapIndicator_Type.__name__ = "Integer32"
_AlaNtpInfoLeapIndicator_Object = MibScalar
alaNtpInfoLeapIndicator = _AlaNtpInfoLeapIndicator_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 8, 3),
    _AlaNtpInfoLeapIndicator_Type()
)
alaNtpInfoLeapIndicator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpInfoLeapIndicator.setStatus("current")


class _AlaNtpInfoStratum_Type(Integer32):
    """Custom type alaNtpInfoStratum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AlaNtpInfoStratum_Type.__name__ = "Integer32"
_AlaNtpInfoStratum_Object = MibScalar
alaNtpInfoStratum = _AlaNtpInfoStratum_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 8, 4),
    _AlaNtpInfoStratum_Type()
)
alaNtpInfoStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpInfoStratum.setStatus("current")


class _AlaNtpInfoPrecision_Type(Integer32):
    """Custom type alaNtpInfoPrecision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20, -4),
    )


_AlaNtpInfoPrecision_Type.__name__ = "Integer32"
_AlaNtpInfoPrecision_Object = MibScalar
alaNtpInfoPrecision = _AlaNtpInfoPrecision_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 8, 5),
    _AlaNtpInfoPrecision_Type()
)
alaNtpInfoPrecision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpInfoPrecision.setStatus("current")
_AlaNtpInfoDistance_Type = SnmpAdminString
_AlaNtpInfoDistance_Object = MibScalar
alaNtpInfoDistance = _AlaNtpInfoDistance_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 8, 6),
    _AlaNtpInfoDistance_Type()
)
alaNtpInfoDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpInfoDistance.setStatus("current")
_AlaNtpInfoDispersion_Type = SnmpAdminString
_AlaNtpInfoDispersion_Object = MibScalar
alaNtpInfoDispersion = _AlaNtpInfoDispersion_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 8, 7),
    _AlaNtpInfoDispersion_Type()
)
alaNtpInfoDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpInfoDispersion.setStatus("current")
_AlaNtpInfoReferenceId_Type = SnmpAdminString
_AlaNtpInfoReferenceId_Object = MibScalar
alaNtpInfoReferenceId = _AlaNtpInfoReferenceId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 8, 8),
    _AlaNtpInfoReferenceId_Type()
)
alaNtpInfoReferenceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpInfoReferenceId.setStatus("current")
_AlaNtpInfoReferenceTime_Type = SnmpAdminString
_AlaNtpInfoReferenceTime_Object = MibScalar
alaNtpInfoReferenceTime = _AlaNtpInfoReferenceTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 8, 9),
    _AlaNtpInfoReferenceTime_Type()
)
alaNtpInfoReferenceTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpInfoReferenceTime.setStatus("current")
_AlaNtpInfoFrequency_Type = SnmpAdminString
_AlaNtpInfoFrequency_Object = MibScalar
alaNtpInfoFrequency = _AlaNtpInfoFrequency_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 8, 10),
    _AlaNtpInfoFrequency_Type()
)
alaNtpInfoFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpInfoFrequency.setStatus("current")
_AlaNtpInfoStability_Type = SnmpAdminString
_AlaNtpInfoStability_Object = MibScalar
alaNtpInfoStability = _AlaNtpInfoStability_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 8, 11),
    _AlaNtpInfoStability_Type()
)
alaNtpInfoStability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpInfoStability.setStatus("current")
_AlaNtpInfoBroadcastDelay_Type = SnmpAdminString
_AlaNtpInfoBroadcastDelay_Object = MibScalar
alaNtpInfoBroadcastDelay = _AlaNtpInfoBroadcastDelay_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 8, 12),
    _AlaNtpInfoBroadcastDelay_Type()
)
alaNtpInfoBroadcastDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpInfoBroadcastDelay.setStatus("current")
_AlaNtpInfoAuthDelay_Type = SnmpAdminString
_AlaNtpInfoAuthDelay_Object = MibScalar
alaNtpInfoAuthDelay = _AlaNtpInfoAuthDelay_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 8, 13),
    _AlaNtpInfoAuthDelay_Type()
)
alaNtpInfoAuthDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaNtpInfoAuthDelay.setStatus("current")


class _NtpClientConfig_Type(Integer32):
    """Custom type ntpClientConfig based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("nonLoopback0", 2),
          ("userIp", 3))
    )


_NtpClientConfig_Type.__name__ = "Integer32"
_NtpClientConfig_Object = MibScalar
ntpClientConfig = _NtpClientConfig_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 9),
    _NtpClientConfig_Type()
)
ntpClientConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpClientConfig.setStatus("deprecated")
_NtpClientIP_Type = IpAddress
_NtpClientIP_Object = MibScalar
ntpClientIP = _NtpClientIP_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 10),
    _NtpClientIP_Type()
)
ntpClientIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpClientIP.setStatus("deprecated")


class _AlaNtpSrcIpConfig_Type(Integer32):
    """Custom type alaNtpSrcIpConfig based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("nonLoopback0", 2),
          ("userIp", 3))
    )


_AlaNtpSrcIpConfig_Type.__name__ = "Integer32"
_AlaNtpSrcIpConfig_Object = MibScalar
alaNtpSrcIpConfig = _AlaNtpSrcIpConfig_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 11),
    _AlaNtpSrcIpConfig_Type()
)
alaNtpSrcIpConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaNtpSrcIpConfig.setStatus("current")
_AlaNtpSrcIp_Type = IpAddress
_AlaNtpSrcIp_Object = MibScalar
alaNtpSrcIp = _AlaNtpSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 1, 12),
    _AlaNtpSrcIp_Type()
)
alaNtpSrcIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaNtpSrcIp.setStatus("current")
_AlaIND1NtpMIBConformance_ObjectIdentity = ObjectIdentity
alaIND1NtpMIBConformance = _AlaIND1NtpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 2)
)
if mibBuilder.loadTexts:
    alaIND1NtpMIBConformance.setStatus("current")
_AlaIND1NtpMIBGroups_ObjectIdentity = ObjectIdentity
alaIND1NtpMIBGroups = _AlaIND1NtpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alaIND1NtpMIBGroups.setStatus("current")
_AlaIND1NtpMIBCompliances_ObjectIdentity = ObjectIdentity
alaIND1NtpMIBCompliances = _AlaIND1NtpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alaIND1NtpMIBCompliances.setStatus("current")

# Managed Objects groups

alaNtpConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 2, 1, 1)
)
alaNtpConfigGroup.setObjects(
      *(("ALCATEL-IND1-NTP-MIB", "alaNtpEnable"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpMonitorEnable"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpBroadcastEnable"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpPeerIpAddress"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpPeerType"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpPeerAuth"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpPeerVersion"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpPeerMinpoll"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpPeerPrefer"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpPeerAdmin"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpPeerName"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpPeerStratum"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpAuthDelay"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpBroadcastDelay"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpKeysFile"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpConfigReqKeyId"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpConfigCtlKeyId"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpConfigCfgKeyId"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpPrecision"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpPeerTests"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpSysStratum"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpMaxAssociation"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpAuthenticate"))
)
if mibBuilder.loadTexts:
    alaNtpConfigGroup.setStatus("current")

alaNtpInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 2, 1, 2)
)
alaNtpInfoGroup.setObjects(
      *(("ALCATEL-IND1-NTP-MIB", "alaNtpPeerListIpAddress"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpPeerListLocal"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpPeerListStratum"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpPeerListPoll"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpPeerListReach"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpPeerListDelay"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpPeerListOffset"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpPeerListDispersion"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpPeerListSynced"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpPeerListName"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpPeerShowRemoteIpAddress"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpPeerShowLocal"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpPeerShowHmode"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpPeerShowPmode"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpPeerShowStratum"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpPeerShowPrecision"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpPeerShowLeapIndicator"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpPeerShowReferenceId"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpPeerShowRootDistance"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpPeerShowRootDispersion"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpPeerShowPpoll"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpPeerShowHpoll"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpPeerShowKeyid"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpPeerShowVersion"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpPeerShowAssociation"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpPeerShowValid"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpPeerShowReach"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpPeerShowUnreach"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpPeerShowFlash"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpPeerShowBroadcastOffset"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpPeerShowTTL"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpPeerShowTimer"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpPeerShowFlags"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpPeerShowReferenceTime"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpPeerShowOriginateTime"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpPeerShowReceiveTime"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpPeerShowTransmitTime"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpPeerShowOffset"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpPeerShowDelay"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpPeerShowDispersion"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpPeerShowName"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpPeerShowStatus"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpClientListVersion"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpClientKey"))
)
if mibBuilder.loadTexts:
    alaNtpInfoGroup.setStatus("current")

alaNtpStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 2, 1, 3)
)
alaNtpStatsGroup.setObjects(
      *(("ALCATEL-IND1-NTP-MIB", "alaNtpStatsPeerIpAddress"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpStatsPeerLocal"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpStatsPeerLastRcv"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpStatsPeerNextSend"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpStatsPeerReachChange"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpStatsPeerPacketsSent"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpStatsPeerPacketsRcvd"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpStatsPeerBadAuth"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpStatsPeerBogusOrigin"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpStatsPeerDuplicate"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpStatsPeerBadDispersion"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpStatsPeerBadRefTime"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpStatsPeerCandidateOrder"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpStatsPeerReset"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpStatsPeerName"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpStatsReset"))
)
if mibBuilder.loadTexts:
    alaNtpStatsGroup.setStatus("current")

alaNtpStatsStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 2, 1, 4)
)
alaNtpStatsStatGroup.setObjects(
      *(("ALCATEL-IND1-NTP-MIB", "alaNtpStatsStatUptime"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpStatsStatReset"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpStatsStatBadStratum"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpStatsStatOldVersion"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpStatsStatNewVersion"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpStatsStatUnknownVersion"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpStatsStatBadLength"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpStatsStatProcessed"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpStatsStatBadAuth"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpStatsStatLimitRejects"))
)
if mibBuilder.loadTexts:
    alaNtpStatsStatGroup.setStatus("current")

alaNtpStatsLoopGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 2, 1, 5)
)
alaNtpStatsLoopGroup.setObjects(
      *(("ALCATEL-IND1-NTP-MIB", "alaNtpStatsLoopOffset"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpStatsLoopFrequency"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpStatsLoopPollAdjust"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpStatsLoopWatchdog"))
)
if mibBuilder.loadTexts:
    alaNtpStatsLoopGroup.setStatus("current")

alaNtpStatsIoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 2, 1, 6)
)
alaNtpStatsIoGroup.setObjects(
      *(("ALCATEL-IND1-NTP-MIB", "alaNtpStatsIoReset"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpStatsIoRcvBuffers"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpStatsIoFreeRcvBuffers"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpStatsIoUsedRcvBuffers"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpStatsIoRefills"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpStatsIoDroppedPackets"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpStatsIoIgnoredPackets"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpStatsIoRcvPackets"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpStatsIoSentPackets"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpStatsIoNotSentPackets"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpStatsIoInterrupts"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpStatsIoInterruptsRcv"))
)
if mibBuilder.loadTexts:
    alaNtpStatsIoGroup.setStatus("current")

alaNtpAccessGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 2, 1, 7)
)
alaNtpAccessGroup.setObjects(
      *(("ALCATEL-IND1-NTP-MIB", "alaNtpAccessKeyIdTrust"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpAccessRestrictedRestrictions"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpAccessRestrictedCount"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpAccessRestrictedRowStatus"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpAccessRereadKeyFile"))
)
if mibBuilder.loadTexts:
    alaNtpAccessGroup.setStatus("current")

alaNtpLocalInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 2, 1, 8)
)
alaNtpLocalInfoGroup.setObjects(
      *(("ALCATEL-IND1-NTP-MIB", "alaNtpInfoPeer"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpInfoMode"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpInfoLeapIndicator"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpInfoStratum"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpInfoPrecision"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpInfoDistance"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpInfoDispersion"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpInfoReferenceId"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpInfoReferenceTime"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpInfoFrequency"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpInfoStability"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpInfoBroadcastDelay"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpInfoAuthDelay"))
)
if mibBuilder.loadTexts:
    alaNtpLocalInfoGroup.setStatus("current")

alaNtpSrcIpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 2, 1, 10)
)
alaNtpSrcIpGroup.setObjects(
      *(("ALCATEL-IND1-NTP-MIB", "alaNtpSrcIpConfig"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpSrcIp"),
        ("ALCATEL-IND1-NTP-MIB", "ntpClientConfig"),
        ("ALCATEL-IND1-NTP-MIB", "ntpClientIP"))
)
if mibBuilder.loadTexts:
    alaNtpSrcIpGroup.setStatus("current")

alaNtpStatsMonitorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 2, 1, 11)
)
alaNtpStatsMonitorGroup.setObjects(
      *(("ALCATEL-IND1-NTP-MIB", "alaNtpStatsMonitorAddress"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpStatsMonitorPort"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpStatsMonitorLocalAddress"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpStatsMonitorCount"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpStatsMonitorMode"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpStatsMonitorVersion"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpStatsMonitorDrop"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpStatsMonitorLast"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpStatsMonitorFirst"),
        ("ALCATEL-IND1-NTP-MIB", "alaNtpStatsMonitorName"))
)
if mibBuilder.loadTexts:
    alaNtpStatsMonitorGroup.setStatus("current")


# Notification objects

alaNtpMaxAssocTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 0, 1)
)
alaNtpMaxAssocTrap.setObjects(
    ("ALCATEL-IND1-NTP-MIB", "alaNtpMaxAssociation")
)
if mibBuilder.loadTexts:
    alaNtpMaxAssocTrap.setStatus(
        "current"
    )


# Notifications groups

alaNtpEventsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 2, 1, 9)
)
alaNtpEventsGroup.setObjects(
    ("ALCATEL-IND1-NTP-MIB", "alaNtpMaxAssocTrap")
)
if mibBuilder.loadTexts:
    alaNtpEventsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alaIND1NtpMonitorMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 26, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    alaIND1NtpMonitorMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-NTP-MIB",
    **{"alcatelIND1NTPMIB": alcatelIND1NTPMIB,
       "alcatelIND1NTPMIBNotifications": alcatelIND1NTPMIBNotifications,
       "alaNtpMaxAssocTrap": alaNtpMaxAssocTrap,
       "alcatelIND1NTPMIBObjects": alcatelIND1NTPMIBObjects,
       "alaNtpConfig": alaNtpConfig,
       "alaNtpEnable": alaNtpEnable,
       "alaNtpMonitorEnable": alaNtpMonitorEnable,
       "alaNtpBroadcastEnable": alaNtpBroadcastEnable,
       "alaNtpPeerTable": alaNtpPeerTable,
       "alaNtpPeerEntry": alaNtpPeerEntry,
       "alaNtpPeerAddressType": alaNtpPeerAddressType,
       "alaNtpPeerAddress": alaNtpPeerAddress,
       "alaNtpPeerIpAddress": alaNtpPeerIpAddress,
       "alaNtpPeerType": alaNtpPeerType,
       "alaNtpPeerAuth": alaNtpPeerAuth,
       "alaNtpPeerVersion": alaNtpPeerVersion,
       "alaNtpPeerMinpoll": alaNtpPeerMinpoll,
       "alaNtpPeerPrefer": alaNtpPeerPrefer,
       "alaNtpPeerAdmin": alaNtpPeerAdmin,
       "alaNtpPeerName": alaNtpPeerName,
       "alaNtpPeerStratum": alaNtpPeerStratum,
       "alaNtpAuthDelay": alaNtpAuthDelay,
       "alaNtpBroadcastDelay": alaNtpBroadcastDelay,
       "alaNtpKeysFile": alaNtpKeysFile,
       "alaNtpConfigReqKeyId": alaNtpConfigReqKeyId,
       "alaNtpConfigCtlKeyId": alaNtpConfigCtlKeyId,
       "alaNtpConfigCfgKeyId": alaNtpConfigCfgKeyId,
       "alaNtpPrecision": alaNtpPrecision,
       "alaNtpPeerTests": alaNtpPeerTests,
       "alaNtpSysStratum": alaNtpSysStratum,
       "alaNtpMaxAssociation": alaNtpMaxAssociation,
       "alaNtpAuthenticate": alaNtpAuthenticate,
       "alaNtpInfo": alaNtpInfo,
       "alaNtpPeerListTable": alaNtpPeerListTable,
       "alaNtpPeerListEntry": alaNtpPeerListEntry,
       "alaNtpPeerListAddressType": alaNtpPeerListAddressType,
       "alaNtpPeerListAddress": alaNtpPeerListAddress,
       "alaNtpPeerListIpAddress": alaNtpPeerListIpAddress,
       "alaNtpPeerListLocal": alaNtpPeerListLocal,
       "alaNtpPeerListStratum": alaNtpPeerListStratum,
       "alaNtpPeerListPoll": alaNtpPeerListPoll,
       "alaNtpPeerListReach": alaNtpPeerListReach,
       "alaNtpPeerListDelay": alaNtpPeerListDelay,
       "alaNtpPeerListOffset": alaNtpPeerListOffset,
       "alaNtpPeerListDispersion": alaNtpPeerListDispersion,
       "alaNtpPeerListSynced": alaNtpPeerListSynced,
       "alaNtpPeerListName": alaNtpPeerListName,
       "alaNtpPeerShowTable": alaNtpPeerShowTable,
       "alaNtpPeerShowEntry": alaNtpPeerShowEntry,
       "alaNtpPeerShowRemoteAddressType": alaNtpPeerShowRemoteAddressType,
       "alaNtpPeerShowRemoteAddress": alaNtpPeerShowRemoteAddress,
       "alaNtpPeerShowRemoteIpAddress": alaNtpPeerShowRemoteIpAddress,
       "alaNtpPeerShowLocal": alaNtpPeerShowLocal,
       "alaNtpPeerShowHmode": alaNtpPeerShowHmode,
       "alaNtpPeerShowPmode": alaNtpPeerShowPmode,
       "alaNtpPeerShowStratum": alaNtpPeerShowStratum,
       "alaNtpPeerShowPrecision": alaNtpPeerShowPrecision,
       "alaNtpPeerShowLeapIndicator": alaNtpPeerShowLeapIndicator,
       "alaNtpPeerShowReferenceId": alaNtpPeerShowReferenceId,
       "alaNtpPeerShowRootDistance": alaNtpPeerShowRootDistance,
       "alaNtpPeerShowRootDispersion": alaNtpPeerShowRootDispersion,
       "alaNtpPeerShowPpoll": alaNtpPeerShowPpoll,
       "alaNtpPeerShowHpoll": alaNtpPeerShowHpoll,
       "alaNtpPeerShowKeyid": alaNtpPeerShowKeyid,
       "alaNtpPeerShowVersion": alaNtpPeerShowVersion,
       "alaNtpPeerShowAssociation": alaNtpPeerShowAssociation,
       "alaNtpPeerShowValid": alaNtpPeerShowValid,
       "alaNtpPeerShowReach": alaNtpPeerShowReach,
       "alaNtpPeerShowUnreach": alaNtpPeerShowUnreach,
       "alaNtpPeerShowFlash": alaNtpPeerShowFlash,
       "alaNtpPeerShowBroadcastOffset": alaNtpPeerShowBroadcastOffset,
       "alaNtpPeerShowTTL": alaNtpPeerShowTTL,
       "alaNtpPeerShowTimer": alaNtpPeerShowTimer,
       "alaNtpPeerShowFlags": alaNtpPeerShowFlags,
       "alaNtpPeerShowReferenceTime": alaNtpPeerShowReferenceTime,
       "alaNtpPeerShowOriginateTime": alaNtpPeerShowOriginateTime,
       "alaNtpPeerShowReceiveTime": alaNtpPeerShowReceiveTime,
       "alaNtpPeerShowTransmitTime": alaNtpPeerShowTransmitTime,
       "alaNtpPeerShowOffset": alaNtpPeerShowOffset,
       "alaNtpPeerShowDelay": alaNtpPeerShowDelay,
       "alaNtpPeerShowDispersion": alaNtpPeerShowDispersion,
       "alaNtpPeerShowName": alaNtpPeerShowName,
       "alaNtpPeerShowStatus": alaNtpPeerShowStatus,
       "alaNtpClientListTable": alaNtpClientListTable,
       "alaNtpClientListEntry": alaNtpClientListEntry,
       "alaNtpClientListAddressType": alaNtpClientListAddressType,
       "alaNtpClientListAddress": alaNtpClientListAddress,
       "alaNtpClientListVersion": alaNtpClientListVersion,
       "alaNtpClientKey": alaNtpClientKey,
       "alaNtpStats": alaNtpStats,
       "alaNtpStatsPeerTable": alaNtpStatsPeerTable,
       "alaNtpStatsPeerEntry": alaNtpStatsPeerEntry,
       "alaNtpStatsPeerAddressType": alaNtpStatsPeerAddressType,
       "alaNtpStatsPeerAddress": alaNtpStatsPeerAddress,
       "alaNtpStatsPeerIpAddress": alaNtpStatsPeerIpAddress,
       "alaNtpStatsPeerLocal": alaNtpStatsPeerLocal,
       "alaNtpStatsPeerLastRcv": alaNtpStatsPeerLastRcv,
       "alaNtpStatsPeerNextSend": alaNtpStatsPeerNextSend,
       "alaNtpStatsPeerReachChange": alaNtpStatsPeerReachChange,
       "alaNtpStatsPeerPacketsSent": alaNtpStatsPeerPacketsSent,
       "alaNtpStatsPeerPacketsRcvd": alaNtpStatsPeerPacketsRcvd,
       "alaNtpStatsPeerBadAuth": alaNtpStatsPeerBadAuth,
       "alaNtpStatsPeerBogusOrigin": alaNtpStatsPeerBogusOrigin,
       "alaNtpStatsPeerDuplicate": alaNtpStatsPeerDuplicate,
       "alaNtpStatsPeerBadDispersion": alaNtpStatsPeerBadDispersion,
       "alaNtpStatsPeerBadRefTime": alaNtpStatsPeerBadRefTime,
       "alaNtpStatsPeerCandidateOrder": alaNtpStatsPeerCandidateOrder,
       "alaNtpStatsPeerReset": alaNtpStatsPeerReset,
       "alaNtpStatsPeerName": alaNtpStatsPeerName,
       "alaNtpStatsReset": alaNtpStatsReset,
       "alaNtpStatsMonitorTable": alaNtpStatsMonitorTable,
       "alaNtpStatsMonitorEntry": alaNtpStatsMonitorEntry,
       "alaNtpStatsMonitorIndex": alaNtpStatsMonitorIndex,
       "alaNtpStatsMonitorAddress": alaNtpStatsMonitorAddress,
       "alaNtpStatsMonitorPort": alaNtpStatsMonitorPort,
       "alaNtpStatsMonitorLocalAddress": alaNtpStatsMonitorLocalAddress,
       "alaNtpStatsMonitorCount": alaNtpStatsMonitorCount,
       "alaNtpStatsMonitorMode": alaNtpStatsMonitorMode,
       "alaNtpStatsMonitorVersion": alaNtpStatsMonitorVersion,
       "alaNtpStatsMonitorDrop": alaNtpStatsMonitorDrop,
       "alaNtpStatsMonitorLast": alaNtpStatsMonitorLast,
       "alaNtpStatsMonitorFirst": alaNtpStatsMonitorFirst,
       "alaNtpStatsMonitorName": alaNtpStatsMonitorName,
       "alaNtpStatsStat": alaNtpStatsStat,
       "alaNtpStatsStatUptime": alaNtpStatsStatUptime,
       "alaNtpStatsStatReset": alaNtpStatsStatReset,
       "alaNtpStatsStatBadStratum": alaNtpStatsStatBadStratum,
       "alaNtpStatsStatOldVersion": alaNtpStatsStatOldVersion,
       "alaNtpStatsStatNewVersion": alaNtpStatsStatNewVersion,
       "alaNtpStatsStatUnknownVersion": alaNtpStatsStatUnknownVersion,
       "alaNtpStatsStatBadLength": alaNtpStatsStatBadLength,
       "alaNtpStatsStatProcessed": alaNtpStatsStatProcessed,
       "alaNtpStatsStatBadAuth": alaNtpStatsStatBadAuth,
       "alaNtpStatsStatLimitRejects": alaNtpStatsStatLimitRejects,
       "alaNtpStatsLoop": alaNtpStatsLoop,
       "alaNtpStatsLoopOffset": alaNtpStatsLoopOffset,
       "alaNtpStatsLoopFrequency": alaNtpStatsLoopFrequency,
       "alaNtpStatsLoopPollAdjust": alaNtpStatsLoopPollAdjust,
       "alaNtpStatsLoopWatchdog": alaNtpStatsLoopWatchdog,
       "alaNtpStatsIo": alaNtpStatsIo,
       "alaNtpStatsIoReset": alaNtpStatsIoReset,
       "alaNtpStatsIoRcvBuffers": alaNtpStatsIoRcvBuffers,
       "alaNtpStatsIoFreeRcvBuffers": alaNtpStatsIoFreeRcvBuffers,
       "alaNtpStatsIoUsedRcvBuffers": alaNtpStatsIoUsedRcvBuffers,
       "alaNtpStatsIoRefills": alaNtpStatsIoRefills,
       "alaNtpStatsIoDroppedPackets": alaNtpStatsIoDroppedPackets,
       "alaNtpStatsIoIgnoredPackets": alaNtpStatsIoIgnoredPackets,
       "alaNtpStatsIoRcvPackets": alaNtpStatsIoRcvPackets,
       "alaNtpStatsIoSentPackets": alaNtpStatsIoSentPackets,
       "alaNtpStatsIoNotSentPackets": alaNtpStatsIoNotSentPackets,
       "alaNtpStatsIoInterrupts": alaNtpStatsIoInterrupts,
       "alaNtpStatsIoInterruptsRcv": alaNtpStatsIoInterruptsRcv,
       "alaNtpAccess": alaNtpAccess,
       "alaNtpAccessKeyIdTable": alaNtpAccessKeyIdTable,
       "alaNtpAccessKeyIdEntry": alaNtpAccessKeyIdEntry,
       "alaNtpAccessKeyIdKeyId": alaNtpAccessKeyIdKeyId,
       "alaNtpAccessKeyIdTrust": alaNtpAccessKeyIdTrust,
       "alaNtpAccessRestrictedTable": alaNtpAccessRestrictedTable,
       "alaNtpAccessRestrictedEntry": alaNtpAccessRestrictedEntry,
       "alaNtpAccessRestrictedIpAddress": alaNtpAccessRestrictedIpAddress,
       "alaNtpAccessRestrictedMask": alaNtpAccessRestrictedMask,
       "alaNtpAccessRestrictedRestrictions": alaNtpAccessRestrictedRestrictions,
       "alaNtpAccessRestrictedCount": alaNtpAccessRestrictedCount,
       "alaNtpAccessRestrictedRowStatus": alaNtpAccessRestrictedRowStatus,
       "alaNtpAccessRereadKeyFile": alaNtpAccessRereadKeyFile,
       "alaNtpLocalInfo": alaNtpLocalInfo,
       "alaNtpInfoPeer": alaNtpInfoPeer,
       "alaNtpInfoMode": alaNtpInfoMode,
       "alaNtpInfoLeapIndicator": alaNtpInfoLeapIndicator,
       "alaNtpInfoStratum": alaNtpInfoStratum,
       "alaNtpInfoPrecision": alaNtpInfoPrecision,
       "alaNtpInfoDistance": alaNtpInfoDistance,
       "alaNtpInfoDispersion": alaNtpInfoDispersion,
       "alaNtpInfoReferenceId": alaNtpInfoReferenceId,
       "alaNtpInfoReferenceTime": alaNtpInfoReferenceTime,
       "alaNtpInfoFrequency": alaNtpInfoFrequency,
       "alaNtpInfoStability": alaNtpInfoStability,
       "alaNtpInfoBroadcastDelay": alaNtpInfoBroadcastDelay,
       "alaNtpInfoAuthDelay": alaNtpInfoAuthDelay,
       "ntpClientConfig": ntpClientConfig,
       "ntpClientIP": ntpClientIP,
       "alaNtpSrcIpConfig": alaNtpSrcIpConfig,
       "alaNtpSrcIp": alaNtpSrcIp,
       "alaIND1NtpMIBConformance": alaIND1NtpMIBConformance,
       "alaIND1NtpMIBGroups": alaIND1NtpMIBGroups,
       "alaNtpConfigGroup": alaNtpConfigGroup,
       "alaNtpInfoGroup": alaNtpInfoGroup,
       "alaNtpStatsGroup": alaNtpStatsGroup,
       "alaNtpStatsStatGroup": alaNtpStatsStatGroup,
       "alaNtpStatsLoopGroup": alaNtpStatsLoopGroup,
       "alaNtpStatsIoGroup": alaNtpStatsIoGroup,
       "alaNtpAccessGroup": alaNtpAccessGroup,
       "alaNtpLocalInfoGroup": alaNtpLocalInfoGroup,
       "alaNtpEventsGroup": alaNtpEventsGroup,
       "alaNtpSrcIpGroup": alaNtpSrcIpGroup,
       "alaNtpStatsMonitorGroup": alaNtpStatsMonitorGroup,
       "alaIND1NtpMIBCompliances": alaIND1NtpMIBCompliances,
       "alaIND1NtpMonitorMIBCompliance": alaIND1NtpMonitorMIBCompliance}
)
