# SNMP MIB module (SONUS-NTP-SERVICES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SONUS-NTP-SERVICES-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:57:05 2024
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(sonusEventClass,
 sonusEventDescription,
 sonusEventLevel,
 sonusShelfIndex,
 sonusSlotIndex) = mibBuilder.importSymbols(
    "SONUS-COMMON-MIB",
    "sonusEventClass",
    "sonusEventDescription",
    "sonusEventLevel",
    "sonusShelfIndex",
    "sonusSlotIndex")

(sonusServicesMIBs,) = mibBuilder.importSymbols(
    "SONUS-SMI",
    "sonusServicesMIBs")

(SonusName,
 SonusNameReference) = mibBuilder.importSymbols(
    "SONUS-TC",
    "SonusName",
    "SonusNameReference")


# MODULE-IDENTITY

sonusNtpServicesMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SonusNtpServicesMIBObjects_ObjectIdentity = ObjectIdentity
sonusNtpServicesMIBObjects = _SonusNtpServicesMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 2, 1)
)
_SonusTimeZoneObjects_ObjectIdentity = ObjectIdentity
sonusTimeZoneObjects = _SonusTimeZoneObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 2, 1, 1)
)


class _SonusTimeZone_Type(Integer32):
    """Custom type sonusTimeZone based on Integer32"""
    defaultValue = 12

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
              35)
        )
    )
    namedValues = NamedValues(
        *(("gmt", 19),
          ("gmtMinus01-Azores", 18),
          ("gmtMinus02-MidAtlantic", 17),
          ("gmtMinus03-BuenosAires", 16),
          ("gmtMinus04-Atlantic-Canada", 14),
          ("gmtMinus04-Caracas", 15),
          ("gmtMinus05-Bojota", 11),
          ("gmtMinus05-Eastern-US", 12),
          ("gmtMinus05-Indiana", 13),
          ("gmtMinus06-Central-US", 8),
          ("gmtMinus06-Mexico", 9),
          ("gmtMinus06-Saskatchewan", 10),
          ("gmtMinus07-Arizona", 6),
          ("gmtMinus07-Mountain", 7),
          ("gmtMinus08-Pacific-US", 5),
          ("gmtMinus09-Alaska", 4),
          ("gmtMinus10-Hawaii", 3),
          ("gmtMinus11-MidwayIsland", 2),
          ("gmtMinus12-Eniuetok", 1),
          ("gmtPlus01-Berlin", 20),
          ("gmtPlus02-Athens", 21),
          ("gmtPlus03-Moscow", 22),
          ("gmtPlus0330-Tehran", 23),
          ("gmtPlus04-AbuDhabi", 24),
          ("gmtPlus0430-Kabul", 25),
          ("gmtPlus05-Islamabad", 26),
          ("gmtPlus0530-NewDelhi", 27),
          ("gmtPlus06-Dhaka", 28),
          ("gmtPlus07-Bangkok", 29),
          ("gmtPlus08-Beijing", 30),
          ("gmtPlus09-Tokyo", 31),
          ("gmtPlus0930-Adelaide", 32),
          ("gmtPlus10-Guam", 33),
          ("gmtPlus11-Magadan", 34),
          ("gmtPlus12-Fiji", 35))
    )


_SonusTimeZone_Type.__name__ = "Integer32"
_SonusTimeZone_Object = MibScalar
sonusTimeZone = _SonusTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 2, 1, 1, 1),
    _SonusTimeZone_Type()
)
sonusTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusTimeZone.setStatus("current")
_SonusNtpPeer_ObjectIdentity = ObjectIdentity
sonusNtpPeer = _SonusNtpPeer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 2, 1, 2)
)
_SonusNtpPeerNextIndex_Type = Integer32
_SonusNtpPeerNextIndex_Object = MibScalar
sonusNtpPeerNextIndex = _SonusNtpPeerNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 2, 1, 2, 1),
    _SonusNtpPeerNextIndex_Type()
)
sonusNtpPeerNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNtpPeerNextIndex.setStatus("current")
_SonusNtpPeerTable_Object = MibTable
sonusNtpPeerTable = _SonusNtpPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    sonusNtpPeerTable.setStatus("current")
_SonusNtpAdmnEntry_Object = MibTableRow
sonusNtpAdmnEntry = _SonusNtpAdmnEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 2, 1, 2, 2, 1)
)
sonusNtpAdmnEntry.setIndexNames(
    (0, "SONUS-NTP-SERVICES-MIB", "sonusNtpPeerIndex"),
)
if mibBuilder.loadTexts:
    sonusNtpAdmnEntry.setStatus("current")


class _SonusNtpPeerIndex_Type(Integer32):
    """Custom type sonusNtpPeerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_SonusNtpPeerIndex_Type.__name__ = "Integer32"
_SonusNtpPeerIndex_Object = MibTableColumn
sonusNtpPeerIndex = _SonusNtpPeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 2, 1, 2, 2, 1, 1),
    _SonusNtpPeerIndex_Type()
)
sonusNtpPeerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNtpPeerIndex.setStatus("current")
_SonusNtpServerName_Type = SonusName
_SonusNtpServerName_Object = MibTableColumn
sonusNtpServerName = _SonusNtpServerName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 2, 1, 2, 2, 1, 2),
    _SonusNtpServerName_Type()
)
sonusNtpServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNtpServerName.setStatus("current")
_SonusNtpPeerIpaddr_Type = IpAddress
_SonusNtpPeerIpaddr_Object = MibTableColumn
sonusNtpPeerIpaddr = _SonusNtpPeerIpaddr_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 2, 1, 2, 2, 1, 3),
    _SonusNtpPeerIpaddr_Type()
)
sonusNtpPeerIpaddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNtpPeerIpaddr.setStatus("current")


class _SonusNtpPeerMode_Type(Integer32):
    """Custom type sonusNtpPeerMode based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              8)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 8),
          ("poll", 3))
    )


_SonusNtpPeerMode_Type.__name__ = "Integer32"
_SonusNtpPeerMode_Object = MibTableColumn
sonusNtpPeerMode = _SonusNtpPeerMode_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 2, 1, 2, 2, 1, 4),
    _SonusNtpPeerMode_Type()
)
sonusNtpPeerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNtpPeerMode.setStatus("current")


class _SonusNtpPeerVersion_Type(Integer32):
    """Custom type sonusNtpPeerVersion based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("version3", 3),
          ("version4", 4))
    )


_SonusNtpPeerVersion_Type.__name__ = "Integer32"
_SonusNtpPeerVersion_Object = MibTableColumn
sonusNtpPeerVersion = _SonusNtpPeerVersion_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 2, 1, 2, 2, 1, 5),
    _SonusNtpPeerVersion_Type()
)
sonusNtpPeerVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNtpPeerVersion.setStatus("current")


class _SonusNtpPeerMinPoll_Type(Integer32):
    """Custom type sonusNtpPeerMinPoll based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_SonusNtpPeerMinPoll_Type.__name__ = "Integer32"
_SonusNtpPeerMinPoll_Object = MibTableColumn
sonusNtpPeerMinPoll = _SonusNtpPeerMinPoll_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 2, 1, 2, 2, 1, 6),
    _SonusNtpPeerMinPoll_Type()
)
sonusNtpPeerMinPoll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNtpPeerMinPoll.setStatus("current")


class _SonusNtpPeerMaxPoll_Type(Integer32):
    """Custom type sonusNtpPeerMaxPoll based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_SonusNtpPeerMaxPoll_Type.__name__ = "Integer32"
_SonusNtpPeerMaxPoll_Object = MibTableColumn
sonusNtpPeerMaxPoll = _SonusNtpPeerMaxPoll_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 2, 1, 2, 2, 1, 7),
    _SonusNtpPeerMaxPoll_Type()
)
sonusNtpPeerMaxPoll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNtpPeerMaxPoll.setStatus("current")


class _SonusNtpPeerAdmnState_Type(Integer32):
    """Custom type sonusNtpPeerAdmnState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SonusNtpPeerAdmnState_Type.__name__ = "Integer32"
_SonusNtpPeerAdmnState_Object = MibTableColumn
sonusNtpPeerAdmnState = _SonusNtpPeerAdmnState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 2, 1, 2, 2, 1, 8),
    _SonusNtpPeerAdmnState_Type()
)
sonusNtpPeerAdmnState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNtpPeerAdmnState.setStatus("current")
_SonusNtpPeerAdmnRowStatus_Type = RowStatus
_SonusNtpPeerAdmnRowStatus_Object = MibTableColumn
sonusNtpPeerAdmnRowStatus = _SonusNtpPeerAdmnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 2, 1, 2, 2, 1, 9),
    _SonusNtpPeerAdmnRowStatus_Type()
)
sonusNtpPeerAdmnRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNtpPeerAdmnRowStatus.setStatus("current")
_SonusNtpPeerStatTable_Object = MibTable
sonusNtpPeerStatTable = _SonusNtpPeerStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 2, 1, 3)
)
if mibBuilder.loadTexts:
    sonusNtpPeerStatTable.setStatus("current")
_SonusNtpPeerStatEntry_Object = MibTableRow
sonusNtpPeerStatEntry = _SonusNtpPeerStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 2, 1, 3, 1)
)
sonusNtpPeerStatEntry.setIndexNames(
    (0, "SONUS-NTP-SERVICES-MIB", "sonusNtpPeerStatShelfIndex"),
    (0, "SONUS-NTP-SERVICES-MIB", "sonusNtpPeerStatIndex"),
)
if mibBuilder.loadTexts:
    sonusNtpPeerStatEntry.setStatus("current")
_SonusNtpPeerStatShelfIndex_Type = Integer32
_SonusNtpPeerStatShelfIndex_Object = MibTableColumn
sonusNtpPeerStatShelfIndex = _SonusNtpPeerStatShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 2, 1, 3, 1, 1),
    _SonusNtpPeerStatShelfIndex_Type()
)
sonusNtpPeerStatShelfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNtpPeerStatShelfIndex.setStatus("current")
_SonusNtpPeerStatIndex_Type = Integer32
_SonusNtpPeerStatIndex_Object = MibTableColumn
sonusNtpPeerStatIndex = _SonusNtpPeerStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 2, 1, 3, 1, 2),
    _SonusNtpPeerStatIndex_Type()
)
sonusNtpPeerStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNtpPeerStatIndex.setStatus("current")


class _SonusNtpPeerState_Type(Integer32):
    """Custom type sonusNtpPeerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("insync", 2),
          ("outofsync", 1))
    )


_SonusNtpPeerState_Type.__name__ = "Integer32"
_SonusNtpPeerState_Object = MibTableColumn
sonusNtpPeerState = _SonusNtpPeerState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 2, 1, 3, 1, 3),
    _SonusNtpPeerState_Type()
)
sonusNtpPeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNtpPeerState.setStatus("current")
_SonusNtpPeerStratum_Type = Integer32
_SonusNtpPeerStratum_Object = MibTableColumn
sonusNtpPeerStratum = _SonusNtpPeerStratum_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 2, 1, 3, 1, 4),
    _SonusNtpPeerStratum_Type()
)
sonusNtpPeerStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNtpPeerStratum.setStatus("current")


class _SonusNtpPeerRefTime_Type(DisplayString):
    """Custom type sonusNtpPeerRefTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_SonusNtpPeerRefTime_Type.__name__ = "DisplayString"
_SonusNtpPeerRefTime_Object = MibTableColumn
sonusNtpPeerRefTime = _SonusNtpPeerRefTime_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 2, 1, 3, 1, 5),
    _SonusNtpPeerRefTime_Type()
)
sonusNtpPeerRefTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNtpPeerRefTime.setStatus("current")
_SonusNtpSysStatTable_Object = MibTable
sonusNtpSysStatTable = _SonusNtpSysStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 2, 1, 4)
)
if mibBuilder.loadTexts:
    sonusNtpSysStatTable.setStatus("current")
_SonusNtpSysStatEntry_Object = MibTableRow
sonusNtpSysStatEntry = _SonusNtpSysStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 2, 1, 4, 1)
)
sonusNtpSysStatEntry.setIndexNames(
    (0, "SONUS-NTP-SERVICES-MIB", "sonusNtpSysShelfIndex"),
)
if mibBuilder.loadTexts:
    sonusNtpSysStatEntry.setStatus("current")
_SonusNtpSysShelfIndex_Type = Integer32
_SonusNtpSysShelfIndex_Object = MibTableColumn
sonusNtpSysShelfIndex = _SonusNtpSysShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 2, 1, 4, 1, 1),
    _SonusNtpSysShelfIndex_Type()
)
sonusNtpSysShelfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNtpSysShelfIndex.setStatus("current")


class _SonusNtpSysClock_Type(DisplayString):
    """Custom type sonusNtpSysClock based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_SonusNtpSysClock_Type.__name__ = "DisplayString"
_SonusNtpSysClock_Object = MibTableColumn
sonusNtpSysClock = _SonusNtpSysClock_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 2, 1, 4, 1, 2),
    _SonusNtpSysClock_Type()
)
sonusNtpSysClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNtpSysClock.setStatus("current")


class _SonusNtpSysRefTime_Type(DisplayString):
    """Custom type sonusNtpSysRefTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_SonusNtpSysRefTime_Type.__name__ = "DisplayString"
_SonusNtpSysRefTime_Object = MibTableColumn
sonusNtpSysRefTime = _SonusNtpSysRefTime_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 2, 1, 4, 1, 3),
    _SonusNtpSysRefTime_Type()
)
sonusNtpSysRefTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNtpSysRefTime.setStatus("current")


class _SonusNtpSysLastSelect_Type(DisplayString):
    """Custom type sonusNtpSysLastSelect based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_SonusNtpSysLastSelect_Type.__name__ = "DisplayString"
_SonusNtpSysLastSelect_Object = MibTableColumn
sonusNtpSysLastSelect = _SonusNtpSysLastSelect_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 2, 1, 4, 1, 4),
    _SonusNtpSysLastSelect_Type()
)
sonusNtpSysLastSelect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNtpSysLastSelect.setStatus("current")
_SonusNtpSysPeer_Type = SonusNameReference
_SonusNtpSysPeer_Object = MibTableColumn
sonusNtpSysPeer = _SonusNtpSysPeer_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 2, 1, 4, 1, 5),
    _SonusNtpSysPeer_Type()
)
sonusNtpSysPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNtpSysPeer.setStatus("current")
_SonusNtpServicesMIBNotifications_ObjectIdentity = ObjectIdentity
sonusNtpServicesMIBNotifications = _SonusNtpServicesMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 2, 2)
)
_SonusNtpServicesMIBNotificationsPrefix_ObjectIdentity = ObjectIdentity
sonusNtpServicesMIBNotificationsPrefix = _SonusNtpServicesMIBNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 2, 2, 0)
)
_SonusNtpServicesMIBNotificationsObjects_ObjectIdentity = ObjectIdentity
sonusNtpServicesMIBNotificationsObjects = _SonusNtpServicesMIBNotificationsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 2, 2, 1)
)


class _SonusNtpServerOutOfServiceReason_Type(Integer32):
    """Custom type sonusNtpServerOutOfServiceReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ntpServerDisabled", 1),
          ("ntpServerOutOfSync", 2))
    )


_SonusNtpServerOutOfServiceReason_Type.__name__ = "Integer32"
_SonusNtpServerOutOfServiceReason_Object = MibScalar
sonusNtpServerOutOfServiceReason = _SonusNtpServerOutOfServiceReason_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 2, 2, 1, 1),
    _SonusNtpServerOutOfServiceReason_Type()
)
sonusNtpServerOutOfServiceReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNtpServerOutOfServiceReason.setStatus("current")


class _SonusNtpDownReason_Type(Integer32):
    """Custom type sonusNtpDownReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allNtpServersOutOfSync", 2),
          ("noNtpServerConfigured", 1))
    )


_SonusNtpDownReason_Type.__name__ = "Integer32"
_SonusNtpDownReason_Object = MibScalar
sonusNtpDownReason = _SonusNtpDownReason_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 2, 2, 1, 2),
    _SonusNtpDownReason_Type()
)
sonusNtpDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNtpDownReason.setStatus("current")

# Managed Objects groups


# Notification objects

sonusNtpServerInServiceNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 2, 2, 0, 1)
)
sonusNtpServerInServiceNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusSlotIndex"),
        ("SONUS-NTP-SERVICES-MIB", "sonusNtpServerName"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusNtpServerInServiceNotification.setStatus(
        "current"
    )

sonusNtpServerOutOfServiceNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 2, 2, 0, 2)
)
sonusNtpServerOutOfServiceNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusSlotIndex"),
        ("SONUS-NTP-SERVICES-MIB", "sonusNtpServerName"),
        ("SONUS-NTP-SERVICES-MIB", "sonusNtpServerOutOfServiceReason"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusNtpServerOutOfServiceNotification.setStatus(
        "current"
    )

sonusNtpUpNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 2, 2, 0, 3)
)
sonusNtpUpNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusSlotIndex"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusNtpUpNotification.setStatus(
        "current"
    )

sonusNtpDownNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 5, 2, 2, 0, 4)
)
sonusNtpDownNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusSlotIndex"),
        ("SONUS-NTP-SERVICES-MIB", "sonusNtpDownReason"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusNtpDownNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SONUS-NTP-SERVICES-MIB",
    **{"sonusNtpServicesMIB": sonusNtpServicesMIB,
       "sonusNtpServicesMIBObjects": sonusNtpServicesMIBObjects,
       "sonusTimeZoneObjects": sonusTimeZoneObjects,
       "sonusTimeZone": sonusTimeZone,
       "sonusNtpPeer": sonusNtpPeer,
       "sonusNtpPeerNextIndex": sonusNtpPeerNextIndex,
       "sonusNtpPeerTable": sonusNtpPeerTable,
       "sonusNtpAdmnEntry": sonusNtpAdmnEntry,
       "sonusNtpPeerIndex": sonusNtpPeerIndex,
       "sonusNtpServerName": sonusNtpServerName,
       "sonusNtpPeerIpaddr": sonusNtpPeerIpaddr,
       "sonusNtpPeerMode": sonusNtpPeerMode,
       "sonusNtpPeerVersion": sonusNtpPeerVersion,
       "sonusNtpPeerMinPoll": sonusNtpPeerMinPoll,
       "sonusNtpPeerMaxPoll": sonusNtpPeerMaxPoll,
       "sonusNtpPeerAdmnState": sonusNtpPeerAdmnState,
       "sonusNtpPeerAdmnRowStatus": sonusNtpPeerAdmnRowStatus,
       "sonusNtpPeerStatTable": sonusNtpPeerStatTable,
       "sonusNtpPeerStatEntry": sonusNtpPeerStatEntry,
       "sonusNtpPeerStatShelfIndex": sonusNtpPeerStatShelfIndex,
       "sonusNtpPeerStatIndex": sonusNtpPeerStatIndex,
       "sonusNtpPeerState": sonusNtpPeerState,
       "sonusNtpPeerStratum": sonusNtpPeerStratum,
       "sonusNtpPeerRefTime": sonusNtpPeerRefTime,
       "sonusNtpSysStatTable": sonusNtpSysStatTable,
       "sonusNtpSysStatEntry": sonusNtpSysStatEntry,
       "sonusNtpSysShelfIndex": sonusNtpSysShelfIndex,
       "sonusNtpSysClock": sonusNtpSysClock,
       "sonusNtpSysRefTime": sonusNtpSysRefTime,
       "sonusNtpSysLastSelect": sonusNtpSysLastSelect,
       "sonusNtpSysPeer": sonusNtpSysPeer,
       "sonusNtpServicesMIBNotifications": sonusNtpServicesMIBNotifications,
       "sonusNtpServicesMIBNotificationsPrefix": sonusNtpServicesMIBNotificationsPrefix,
       "sonusNtpServerInServiceNotification": sonusNtpServerInServiceNotification,
       "sonusNtpServerOutOfServiceNotification": sonusNtpServerOutOfServiceNotification,
       "sonusNtpUpNotification": sonusNtpUpNotification,
       "sonusNtpDownNotification": sonusNtpDownNotification,
       "sonusNtpServicesMIBNotificationsObjects": sonusNtpServicesMIBNotificationsObjects,
       "sonusNtpServerOutOfServiceReason": sonusNtpServerOutOfServiceReason,
       "sonusNtpDownReason": sonusNtpDownReason}
)
