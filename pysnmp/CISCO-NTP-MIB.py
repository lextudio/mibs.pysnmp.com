# SNMP MIB module (CISCO-NTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-NTP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:06:19 2024
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

ciscoNtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 168)
)
ciscoNtpMIB.setRevisions(
        ("2006-07-31 00:00",
         "2004-07-23 00:00",
         "2003-07-29 00:00",
         "2003-07-07 00:00",
         "2002-02-20 00:00",
         "2000-06-16 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class NTPTimeStamp(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )



class NTPLeapIndicator(Integer32, TextualConvention):
    status = "current"
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
        *(("addSecond", 1),
          ("alarm", 3),
          ("noWarning", 0),
          ("subtractSecond", 2))
    )



class NTPSignedTimeValue(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )



class NTPUnsignedTimeValue(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )



class NTPStratum(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class NTPRefId(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )



class NTPPollInterval(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20, 20),
    )



class NTPAssocIdentifier(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoNtpMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoNtpMIBNotifs = _CiscoNtpMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 168, 0)
)
_CiscoNtpMIBObjects_ObjectIdentity = ObjectIdentity
ciscoNtpMIBObjects = _CiscoNtpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 168, 1)
)
_CntpSystem_ObjectIdentity = ObjectIdentity
cntpSystem = _CntpSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 1)
)
_CntpSysLeap_Type = NTPLeapIndicator
_CntpSysLeap_Object = MibScalar
cntpSysLeap = _CntpSysLeap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 1, 1),
    _CntpSysLeap_Type()
)
cntpSysLeap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cntpSysLeap.setStatus("current")
_CntpSysStratum_Type = NTPStratum
_CntpSysStratum_Object = MibScalar
cntpSysStratum = _CntpSysStratum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 1, 2),
    _CntpSysStratum_Type()
)
cntpSysStratum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cntpSysStratum.setStatus("current")


class _CntpSysPrecision_Type(Integer32):
    """Custom type cntpSysPrecision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20, 20),
    )


_CntpSysPrecision_Type.__name__ = "Integer32"
_CntpSysPrecision_Object = MibScalar
cntpSysPrecision = _CntpSysPrecision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 1, 3),
    _CntpSysPrecision_Type()
)
cntpSysPrecision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntpSysPrecision.setStatus("current")
_CntpSysRootDelay_Type = NTPSignedTimeValue
_CntpSysRootDelay_Object = MibScalar
cntpSysRootDelay = _CntpSysRootDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 1, 4),
    _CntpSysRootDelay_Type()
)
cntpSysRootDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntpSysRootDelay.setStatus("current")
if mibBuilder.loadTexts:
    cntpSysRootDelay.setUnits("seconds")
_CntpSysRootDispersion_Type = NTPUnsignedTimeValue
_CntpSysRootDispersion_Object = MibScalar
cntpSysRootDispersion = _CntpSysRootDispersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 1, 5),
    _CntpSysRootDispersion_Type()
)
cntpSysRootDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntpSysRootDispersion.setStatus("current")
if mibBuilder.loadTexts:
    cntpSysRootDispersion.setUnits("seconds")
_CntpSysRefId_Type = NTPRefId
_CntpSysRefId_Object = MibScalar
cntpSysRefId = _CntpSysRefId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 1, 6),
    _CntpSysRefId_Type()
)
cntpSysRefId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntpSysRefId.setStatus("current")
_CntpSysRefTime_Type = NTPTimeStamp
_CntpSysRefTime_Object = MibScalar
cntpSysRefTime = _CntpSysRefTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 1, 7),
    _CntpSysRefTime_Type()
)
cntpSysRefTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntpSysRefTime.setStatus("current")
_CntpSysPoll_Type = NTPPollInterval
_CntpSysPoll_Object = MibScalar
cntpSysPoll = _CntpSysPoll_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 1, 8),
    _CntpSysPoll_Type()
)
cntpSysPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntpSysPoll.setStatus("current")
_CntpSysPeer_Type = NTPAssocIdentifier
_CntpSysPeer_Object = MibScalar
cntpSysPeer = _CntpSysPeer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 1, 9),
    _CntpSysPeer_Type()
)
cntpSysPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntpSysPeer.setStatus("current")
_CntpSysClock_Type = NTPTimeStamp
_CntpSysClock_Object = MibScalar
cntpSysClock = _CntpSysClock_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 1, 10),
    _CntpSysClock_Type()
)
cntpSysClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntpSysClock.setStatus("current")


class _CntpSysSrvStatus_Type(Integer32):
    """Custom type cntpSysSrvStatus based on Integer32"""
    defaultValue = 1

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
        *(("notRunning", 2),
          ("notSynchronized", 3),
          ("syncToLocal", 4),
          ("syncToRefclock", 5),
          ("syncToRemoteServer", 6),
          ("unknown", 1))
    )


_CntpSysSrvStatus_Type.__name__ = "Integer32"
_CntpSysSrvStatus_Object = MibScalar
cntpSysSrvStatus = _CntpSysSrvStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 1, 11),
    _CntpSysSrvStatus_Type()
)
cntpSysSrvStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntpSysSrvStatus.setStatus("current")
_CntpPeers_ObjectIdentity = ObjectIdentity
cntpPeers = _CntpPeers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2)
)
_CntpPeersVarTable_Object = MibTable
cntpPeersVarTable = _CntpPeersVarTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cntpPeersVarTable.setStatus("current")
_CntpPeersVarEntry_Object = MibTableRow
cntpPeersVarEntry = _CntpPeersVarEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1)
)
cntpPeersVarEntry.setIndexNames(
    (0, "CISCO-NTP-MIB", "cntpPeersAssocId"),
)
if mibBuilder.loadTexts:
    cntpPeersVarEntry.setStatus("current")
_CntpPeersAssocId_Type = NTPAssocIdentifier
_CntpPeersAssocId_Object = MibTableColumn
cntpPeersAssocId = _CntpPeersAssocId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 1),
    _CntpPeersAssocId_Type()
)
cntpPeersAssocId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cntpPeersAssocId.setStatus("current")
_CntpPeersConfigured_Type = TruthValue
_CntpPeersConfigured_Object = MibTableColumn
cntpPeersConfigured = _CntpPeersConfigured_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 2),
    _CntpPeersConfigured_Type()
)
cntpPeersConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntpPeersConfigured.setStatus("current")
_CntpPeersPeerAddress_Type = IpAddress
_CntpPeersPeerAddress_Object = MibTableColumn
cntpPeersPeerAddress = _CntpPeersPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 3),
    _CntpPeersPeerAddress_Type()
)
cntpPeersPeerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cntpPeersPeerAddress.setStatus("current")


class _CntpPeersPeerPort_Type(Integer32):
    """Custom type cntpPeersPeerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CntpPeersPeerPort_Type.__name__ = "Integer32"
_CntpPeersPeerPort_Object = MibTableColumn
cntpPeersPeerPort = _CntpPeersPeerPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 4),
    _CntpPeersPeerPort_Type()
)
cntpPeersPeerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntpPeersPeerPort.setStatus("current")
_CntpPeersHostAddress_Type = IpAddress
_CntpPeersHostAddress_Object = MibTableColumn
cntpPeersHostAddress = _CntpPeersHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 5),
    _CntpPeersHostAddress_Type()
)
cntpPeersHostAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cntpPeersHostAddress.setStatus("current")


class _CntpPeersHostPort_Type(Integer32):
    """Custom type cntpPeersHostPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CntpPeersHostPort_Type.__name__ = "Integer32"
_CntpPeersHostPort_Object = MibTableColumn
cntpPeersHostPort = _CntpPeersHostPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 6),
    _CntpPeersHostPort_Type()
)
cntpPeersHostPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntpPeersHostPort.setStatus("current")
_CntpPeersLeap_Type = NTPLeapIndicator
_CntpPeersLeap_Object = MibTableColumn
cntpPeersLeap = _CntpPeersLeap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 7),
    _CntpPeersLeap_Type()
)
cntpPeersLeap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntpPeersLeap.setStatus("current")


class _CntpPeersMode_Type(Integer32):
    """Custom type cntpPeersMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 5),
          ("client", 3),
          ("reservedControl", 6),
          ("reservedPrivate", 7),
          ("server", 4),
          ("symmetricActive", 1),
          ("symmetricPassive", 2),
          ("unspecified", 0))
    )


_CntpPeersMode_Type.__name__ = "Integer32"
_CntpPeersMode_Object = MibTableColumn
cntpPeersMode = _CntpPeersMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 8),
    _CntpPeersMode_Type()
)
cntpPeersMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cntpPeersMode.setStatus("current")
_CntpPeersStratum_Type = NTPStratum
_CntpPeersStratum_Object = MibTableColumn
cntpPeersStratum = _CntpPeersStratum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 9),
    _CntpPeersStratum_Type()
)
cntpPeersStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntpPeersStratum.setStatus("current")
_CntpPeersPeerPoll_Type = NTPPollInterval
_CntpPeersPeerPoll_Object = MibTableColumn
cntpPeersPeerPoll = _CntpPeersPeerPoll_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 10),
    _CntpPeersPeerPoll_Type()
)
cntpPeersPeerPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntpPeersPeerPoll.setStatus("current")
_CntpPeersHostPoll_Type = NTPPollInterval
_CntpPeersHostPoll_Object = MibTableColumn
cntpPeersHostPoll = _CntpPeersHostPoll_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 11),
    _CntpPeersHostPoll_Type()
)
cntpPeersHostPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntpPeersHostPoll.setStatus("current")


class _CntpPeersPrecision_Type(Integer32):
    """Custom type cntpPeersPrecision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20, 20),
    )


_CntpPeersPrecision_Type.__name__ = "Integer32"
_CntpPeersPrecision_Object = MibTableColumn
cntpPeersPrecision = _CntpPeersPrecision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 12),
    _CntpPeersPrecision_Type()
)
cntpPeersPrecision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntpPeersPrecision.setStatus("current")
_CntpPeersRootDelay_Type = NTPSignedTimeValue
_CntpPeersRootDelay_Object = MibTableColumn
cntpPeersRootDelay = _CntpPeersRootDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 13),
    _CntpPeersRootDelay_Type()
)
cntpPeersRootDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntpPeersRootDelay.setStatus("current")
if mibBuilder.loadTexts:
    cntpPeersRootDelay.setUnits("seconds")
_CntpPeersRootDispersion_Type = NTPUnsignedTimeValue
_CntpPeersRootDispersion_Object = MibTableColumn
cntpPeersRootDispersion = _CntpPeersRootDispersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 14),
    _CntpPeersRootDispersion_Type()
)
cntpPeersRootDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntpPeersRootDispersion.setStatus("current")
if mibBuilder.loadTexts:
    cntpPeersRootDispersion.setUnits("seconds")
_CntpPeersRefId_Type = NTPRefId
_CntpPeersRefId_Object = MibTableColumn
cntpPeersRefId = _CntpPeersRefId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 15),
    _CntpPeersRefId_Type()
)
cntpPeersRefId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntpPeersRefId.setStatus("current")
_CntpPeersRefTime_Type = NTPTimeStamp
_CntpPeersRefTime_Object = MibTableColumn
cntpPeersRefTime = _CntpPeersRefTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 16),
    _CntpPeersRefTime_Type()
)
cntpPeersRefTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntpPeersRefTime.setStatus("current")
_CntpPeersOrgTime_Type = NTPTimeStamp
_CntpPeersOrgTime_Object = MibTableColumn
cntpPeersOrgTime = _CntpPeersOrgTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 17),
    _CntpPeersOrgTime_Type()
)
cntpPeersOrgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntpPeersOrgTime.setStatus("current")
_CntpPeersReceiveTime_Type = NTPTimeStamp
_CntpPeersReceiveTime_Object = MibTableColumn
cntpPeersReceiveTime = _CntpPeersReceiveTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 18),
    _CntpPeersReceiveTime_Type()
)
cntpPeersReceiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntpPeersReceiveTime.setStatus("current")
_CntpPeersTransmitTime_Type = NTPTimeStamp
_CntpPeersTransmitTime_Object = MibTableColumn
cntpPeersTransmitTime = _CntpPeersTransmitTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 19),
    _CntpPeersTransmitTime_Type()
)
cntpPeersTransmitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntpPeersTransmitTime.setStatus("current")


class _CntpPeersUpdateTime_Type(Integer32):
    """Custom type cntpPeersUpdateTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CntpPeersUpdateTime_Type.__name__ = "Integer32"
_CntpPeersUpdateTime_Object = MibTableColumn
cntpPeersUpdateTime = _CntpPeersUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 20),
    _CntpPeersUpdateTime_Type()
)
cntpPeersUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntpPeersUpdateTime.setStatus("deprecated")


class _CntpPeersReach_Type(Integer32):
    """Custom type cntpPeersReach based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CntpPeersReach_Type.__name__ = "Integer32"
_CntpPeersReach_Object = MibTableColumn
cntpPeersReach = _CntpPeersReach_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 21),
    _CntpPeersReach_Type()
)
cntpPeersReach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntpPeersReach.setStatus("current")


class _CntpPeersTimer_Type(Integer32):
    """Custom type cntpPeersTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CntpPeersTimer_Type.__name__ = "Integer32"
_CntpPeersTimer_Object = MibTableColumn
cntpPeersTimer = _CntpPeersTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 22),
    _CntpPeersTimer_Type()
)
cntpPeersTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntpPeersTimer.setStatus("current")
if mibBuilder.loadTexts:
    cntpPeersTimer.setUnits("seconds")
_CntpPeersOffset_Type = NTPSignedTimeValue
_CntpPeersOffset_Object = MibTableColumn
cntpPeersOffset = _CntpPeersOffset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 23),
    _CntpPeersOffset_Type()
)
cntpPeersOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntpPeersOffset.setStatus("current")
if mibBuilder.loadTexts:
    cntpPeersOffset.setUnits("seconds")
_CntpPeersDelay_Type = NTPSignedTimeValue
_CntpPeersDelay_Object = MibTableColumn
cntpPeersDelay = _CntpPeersDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 24),
    _CntpPeersDelay_Type()
)
cntpPeersDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntpPeersDelay.setStatus("current")
if mibBuilder.loadTexts:
    cntpPeersDelay.setUnits("seconds")
_CntpPeersDispersion_Type = NTPUnsignedTimeValue
_CntpPeersDispersion_Object = MibTableColumn
cntpPeersDispersion = _CntpPeersDispersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 25),
    _CntpPeersDispersion_Type()
)
cntpPeersDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntpPeersDispersion.setStatus("current")
if mibBuilder.loadTexts:
    cntpPeersDispersion.setUnits("seconds")
_CntpPeersFilterValidEntries_Type = Gauge32
_CntpPeersFilterValidEntries_Object = MibTableColumn
cntpPeersFilterValidEntries = _CntpPeersFilterValidEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 26),
    _CntpPeersFilterValidEntries_Type()
)
cntpPeersFilterValidEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntpPeersFilterValidEntries.setStatus("current")
_CntpPeersEntryStatus_Type = RowStatus
_CntpPeersEntryStatus_Object = MibTableColumn
cntpPeersEntryStatus = _CntpPeersEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 27),
    _CntpPeersEntryStatus_Type()
)
cntpPeersEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cntpPeersEntryStatus.setStatus("current")
_CntpPeersUpdateTimeRev1_Type = Unsigned32
_CntpPeersUpdateTimeRev1_Object = MibTableColumn
cntpPeersUpdateTimeRev1 = _CntpPeersUpdateTimeRev1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 28),
    _CntpPeersUpdateTimeRev1_Type()
)
cntpPeersUpdateTimeRev1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntpPeersUpdateTimeRev1.setStatus("current")


class _CntpPeersPrefPeer_Type(TruthValue):
    """Custom type cntpPeersPrefPeer based on TruthValue"""


_CntpPeersPrefPeer_Object = MibTableColumn
cntpPeersPrefPeer = _CntpPeersPrefPeer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 29),
    _CntpPeersPrefPeer_Type()
)
cntpPeersPrefPeer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cntpPeersPrefPeer.setStatus("current")


class _CntpPeersPeerType_Type(InetAddressType):
    """Custom type cntpPeersPeerType based on InetAddressType"""


_CntpPeersPeerType_Object = MibTableColumn
cntpPeersPeerType = _CntpPeersPeerType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 30),
    _CntpPeersPeerType_Type()
)
cntpPeersPeerType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cntpPeersPeerType.setStatus("current")
_CntpPeersPeerName_Type = InetAddress
_CntpPeersPeerName_Object = MibTableColumn
cntpPeersPeerName = _CntpPeersPeerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 2, 1, 1, 31),
    _CntpPeersPeerName_Type()
)
cntpPeersPeerName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cntpPeersPeerName.setStatus("current")
_CntpFilter_ObjectIdentity = ObjectIdentity
cntpFilter = _CntpFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 3)
)
_CntpFilterRegisterTable_Object = MibTable
cntpFilterRegisterTable = _CntpFilterRegisterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cntpFilterRegisterTable.setStatus("current")
_CntpFilterRegisterEntry_Object = MibTableRow
cntpFilterRegisterEntry = _CntpFilterRegisterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 3, 2, 1)
)
cntpFilterRegisterEntry.setIndexNames(
    (0, "CISCO-NTP-MIB", "cntpPeersAssocId"),
    (0, "CISCO-NTP-MIB", "cntpFilterIndex"),
)
if mibBuilder.loadTexts:
    cntpFilterRegisterEntry.setStatus("current")


class _CntpFilterIndex_Type(Integer32):
    """Custom type cntpFilterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CntpFilterIndex_Type.__name__ = "Integer32"
_CntpFilterIndex_Object = MibTableColumn
cntpFilterIndex = _CntpFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 3, 2, 1, 1),
    _CntpFilterIndex_Type()
)
cntpFilterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cntpFilterIndex.setStatus("current")
_CntpFilterPeersOffset_Type = NTPSignedTimeValue
_CntpFilterPeersOffset_Object = MibTableColumn
cntpFilterPeersOffset = _CntpFilterPeersOffset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 3, 2, 1, 2),
    _CntpFilterPeersOffset_Type()
)
cntpFilterPeersOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntpFilterPeersOffset.setStatus("current")
if mibBuilder.loadTexts:
    cntpFilterPeersOffset.setUnits("seconds")
_CntpFilterPeersDelay_Type = NTPSignedTimeValue
_CntpFilterPeersDelay_Object = MibTableColumn
cntpFilterPeersDelay = _CntpFilterPeersDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 3, 2, 1, 3),
    _CntpFilterPeersDelay_Type()
)
cntpFilterPeersDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntpFilterPeersDelay.setStatus("current")
if mibBuilder.loadTexts:
    cntpFilterPeersDelay.setUnits("seconds")
_CntpFilterPeersDispersion_Type = NTPUnsignedTimeValue
_CntpFilterPeersDispersion_Object = MibTableColumn
cntpFilterPeersDispersion = _CntpFilterPeersDispersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 168, 1, 3, 2, 1, 4),
    _CntpFilterPeersDispersion_Type()
)
cntpFilterPeersDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntpFilterPeersDispersion.setStatus("current")
if mibBuilder.loadTexts:
    cntpFilterPeersDispersion.setUnits("seconds")
_CiscoNtpMIBConformance_ObjectIdentity = ObjectIdentity
ciscoNtpMIBConformance = _CiscoNtpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 168, 2)
)
_CiscoNtpMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoNtpMIBCompliances = _CiscoNtpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 168, 2, 1)
)
_CiscoNtpMIBGroups_ObjectIdentity = ObjectIdentity
ciscoNtpMIBGroups = _CiscoNtpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 168, 2, 2)
)

# Managed Objects groups

ciscoNtpSysGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 168, 2, 2, 1)
)
ciscoNtpSysGroup.setObjects(
      *(("CISCO-NTP-MIB", "cntpSysLeap"),
        ("CISCO-NTP-MIB", "cntpSysStratum"),
        ("CISCO-NTP-MIB", "cntpSysPrecision"),
        ("CISCO-NTP-MIB", "cntpSysRootDelay"),
        ("CISCO-NTP-MIB", "cntpSysRootDispersion"),
        ("CISCO-NTP-MIB", "cntpSysRefId"),
        ("CISCO-NTP-MIB", "cntpSysRefTime"),
        ("CISCO-NTP-MIB", "cntpSysPoll"),
        ("CISCO-NTP-MIB", "cntpSysPeer"),
        ("CISCO-NTP-MIB", "cntpSysClock"))
)
if mibBuilder.loadTexts:
    ciscoNtpSysGroup.setStatus("current")

ciscoNtpPeersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 168, 2, 2, 2)
)
ciscoNtpPeersGroup.setObjects(
      *(("CISCO-NTP-MIB", "cntpPeersConfigured"),
        ("CISCO-NTP-MIB", "cntpPeersPeerAddress"),
        ("CISCO-NTP-MIB", "cntpPeersPeerPort"),
        ("CISCO-NTP-MIB", "cntpPeersHostAddress"),
        ("CISCO-NTP-MIB", "cntpPeersHostPort"),
        ("CISCO-NTP-MIB", "cntpPeersLeap"),
        ("CISCO-NTP-MIB", "cntpPeersMode"),
        ("CISCO-NTP-MIB", "cntpPeersStratum"),
        ("CISCO-NTP-MIB", "cntpPeersPeerPoll"),
        ("CISCO-NTP-MIB", "cntpPeersHostPoll"),
        ("CISCO-NTP-MIB", "cntpPeersPrecision"),
        ("CISCO-NTP-MIB", "cntpPeersRootDelay"),
        ("CISCO-NTP-MIB", "cntpPeersRootDispersion"),
        ("CISCO-NTP-MIB", "cntpPeersRefId"),
        ("CISCO-NTP-MIB", "cntpPeersRefTime"),
        ("CISCO-NTP-MIB", "cntpPeersOrgTime"),
        ("CISCO-NTP-MIB", "cntpPeersReceiveTime"),
        ("CISCO-NTP-MIB", "cntpPeersTransmitTime"),
        ("CISCO-NTP-MIB", "cntpPeersUpdateTime"),
        ("CISCO-NTP-MIB", "cntpPeersReach"),
        ("CISCO-NTP-MIB", "cntpPeersTimer"),
        ("CISCO-NTP-MIB", "cntpPeersOffset"),
        ("CISCO-NTP-MIB", "cntpPeersDelay"),
        ("CISCO-NTP-MIB", "cntpPeersDispersion"),
        ("CISCO-NTP-MIB", "cntpPeersFilterValidEntries"),
        ("CISCO-NTP-MIB", "cntpPeersEntryStatus"))
)
if mibBuilder.loadTexts:
    ciscoNtpPeersGroup.setStatus("deprecated")

ciscoNtpFilterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 168, 2, 2, 3)
)
ciscoNtpFilterGroup.setObjects(
      *(("CISCO-NTP-MIB", "cntpFilterPeersOffset"),
        ("CISCO-NTP-MIB", "cntpFilterPeersDelay"),
        ("CISCO-NTP-MIB", "cntpFilterPeersDispersion"))
)
if mibBuilder.loadTexts:
    ciscoNtpFilterGroup.setStatus("current")

ciscoNtpPeersGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 168, 2, 2, 4)
)
ciscoNtpPeersGroupRev1.setObjects(
      *(("CISCO-NTP-MIB", "cntpPeersConfigured"),
        ("CISCO-NTP-MIB", "cntpPeersPeerAddress"),
        ("CISCO-NTP-MIB", "cntpPeersPeerPort"),
        ("CISCO-NTP-MIB", "cntpPeersHostAddress"),
        ("CISCO-NTP-MIB", "cntpPeersHostPort"),
        ("CISCO-NTP-MIB", "cntpPeersLeap"),
        ("CISCO-NTP-MIB", "cntpPeersMode"),
        ("CISCO-NTP-MIB", "cntpPeersStratum"),
        ("CISCO-NTP-MIB", "cntpPeersPeerPoll"),
        ("CISCO-NTP-MIB", "cntpPeersHostPoll"),
        ("CISCO-NTP-MIB", "cntpPeersPrecision"),
        ("CISCO-NTP-MIB", "cntpPeersRootDelay"),
        ("CISCO-NTP-MIB", "cntpPeersRootDispersion"),
        ("CISCO-NTP-MIB", "cntpPeersRefId"),
        ("CISCO-NTP-MIB", "cntpPeersRefTime"),
        ("CISCO-NTP-MIB", "cntpPeersOrgTime"),
        ("CISCO-NTP-MIB", "cntpPeersReceiveTime"),
        ("CISCO-NTP-MIB", "cntpPeersTransmitTime"),
        ("CISCO-NTP-MIB", "cntpPeersUpdateTimeRev1"),
        ("CISCO-NTP-MIB", "cntpPeersReach"),
        ("CISCO-NTP-MIB", "cntpPeersTimer"),
        ("CISCO-NTP-MIB", "cntpPeersOffset"),
        ("CISCO-NTP-MIB", "cntpPeersDelay"),
        ("CISCO-NTP-MIB", "cntpPeersDispersion"),
        ("CISCO-NTP-MIB", "cntpPeersFilterValidEntries"),
        ("CISCO-NTP-MIB", "cntpPeersEntryStatus"))
)
if mibBuilder.loadTexts:
    ciscoNtpPeersGroupRev1.setStatus("deprecated")

ciscoNtpPeerExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 168, 2, 2, 5)
)
ciscoNtpPeerExtGroup.setObjects(
    ("CISCO-NTP-MIB", "cntpPeersPrefPeer")
)
if mibBuilder.loadTexts:
    ciscoNtpPeerExtGroup.setStatus("current")

ciscoNtpPeersGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 168, 2, 2, 6)
)
ciscoNtpPeersGroupRev2.setObjects(
      *(("CISCO-NTP-MIB", "cntpPeersConfigured"),
        ("CISCO-NTP-MIB", "cntpPeersPeerAddress"),
        ("CISCO-NTP-MIB", "cntpPeersPeerPort"),
        ("CISCO-NTP-MIB", "cntpPeersHostAddress"),
        ("CISCO-NTP-MIB", "cntpPeersHostPort"),
        ("CISCO-NTP-MIB", "cntpPeersLeap"),
        ("CISCO-NTP-MIB", "cntpPeersMode"),
        ("CISCO-NTP-MIB", "cntpPeersStratum"),
        ("CISCO-NTP-MIB", "cntpPeersPeerPoll"),
        ("CISCO-NTP-MIB", "cntpPeersHostPoll"),
        ("CISCO-NTP-MIB", "cntpPeersPrecision"),
        ("CISCO-NTP-MIB", "cntpPeersRootDelay"),
        ("CISCO-NTP-MIB", "cntpPeersRootDispersion"),
        ("CISCO-NTP-MIB", "cntpPeersRefId"),
        ("CISCO-NTP-MIB", "cntpPeersRefTime"),
        ("CISCO-NTP-MIB", "cntpPeersOrgTime"),
        ("CISCO-NTP-MIB", "cntpPeersReceiveTime"),
        ("CISCO-NTP-MIB", "cntpPeersTransmitTime"),
        ("CISCO-NTP-MIB", "cntpPeersUpdateTimeRev1"),
        ("CISCO-NTP-MIB", "cntpPeersReach"),
        ("CISCO-NTP-MIB", "cntpPeersTimer"),
        ("CISCO-NTP-MIB", "cntpPeersOffset"),
        ("CISCO-NTP-MIB", "cntpPeersDelay"),
        ("CISCO-NTP-MIB", "cntpPeersDispersion"),
        ("CISCO-NTP-MIB", "cntpPeersFilterValidEntries"),
        ("CISCO-NTP-MIB", "cntpPeersEntryStatus"),
        ("CISCO-NTP-MIB", "cntpPeersPeerName"),
        ("CISCO-NTP-MIB", "cntpPeersPeerType"))
)
if mibBuilder.loadTexts:
    ciscoNtpPeersGroupRev2.setStatus("current")

ciscoNtpSysExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 168, 2, 2, 7)
)
ciscoNtpSysExtGroup.setObjects(
    ("CISCO-NTP-MIB", "cntpSysSrvStatus")
)
if mibBuilder.loadTexts:
    ciscoNtpSysExtGroup.setStatus("current")


# Notification objects

ciscoNtpSrvStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 168, 0, 1)
)
ciscoNtpSrvStatusChange.setObjects(
    ("CISCO-NTP-MIB", "cntpSysSrvStatus")
)
if mibBuilder.loadTexts:
    ciscoNtpSrvStatusChange.setStatus(
        "current"
    )

ciscoNtpHighPriorityConnFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 168, 0, 2)
)
ciscoNtpHighPriorityConnFailure.setObjects(
    ("CISCO-NTP-MIB", "cntpPeersPeerAddress")
)
if mibBuilder.loadTexts:
    ciscoNtpHighPriorityConnFailure.setStatus(
        "current"
    )

ciscoNtpHighPriorityConnRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 168, 0, 3)
)
ciscoNtpHighPriorityConnRestore.setObjects(
    ("CISCO-NTP-MIB", "cntpPeersPeerAddress")
)
if mibBuilder.loadTexts:
    ciscoNtpHighPriorityConnRestore.setStatus(
        "current"
    )

ciscoNtpGeneralConnFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 168, 0, 4)
)
if mibBuilder.loadTexts:
    ciscoNtpGeneralConnFailure.setStatus(
        "current"
    )

ciscoNtpGeneralConnRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 168, 0, 5)
)
ciscoNtpGeneralConnRestore.setObjects(
    ("CISCO-NTP-MIB", "cntpPeersPeerAddress")
)
if mibBuilder.loadTexts:
    ciscoNtpGeneralConnRestore.setStatus(
        "current"
    )


# Notifications groups

ciscoNtpSrvNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 168, 2, 2, 8)
)
ciscoNtpSrvNotifGroup.setObjects(
      *(("CISCO-NTP-MIB", "ciscoNtpSrvStatusChange"),
        ("CISCO-NTP-MIB", "ciscoNtpHighPriorityConnFailure"),
        ("CISCO-NTP-MIB", "ciscoNtpHighPriorityConnRestore"),
        ("CISCO-NTP-MIB", "ciscoNtpGeneralConnFailure"),
        ("CISCO-NTP-MIB", "ciscoNtpGeneralConnRestore"))
)
if mibBuilder.loadTexts:
    ciscoNtpSrvNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoNtpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 168, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoNtpMIBCompliance.setStatus(
        "deprecated"
    )

ciscoNtpMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 168, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoNtpMIBComplianceRev1.setStatus(
        "deprecated"
    )

ciscoNtpMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 168, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoNtpMIBComplianceRev2.setStatus(
        "deprecated"
    )

ciscoNtpMIBComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 168, 2, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoNtpMIBComplianceRev3.setStatus(
        "deprecated"
    )

ciscoNtpMIBComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 168, 2, 1, 5)
)
if mibBuilder.loadTexts:
    ciscoNtpMIBComplianceRev4.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-NTP-MIB",
    **{"NTPTimeStamp": NTPTimeStamp,
       "NTPLeapIndicator": NTPLeapIndicator,
       "NTPSignedTimeValue": NTPSignedTimeValue,
       "NTPUnsignedTimeValue": NTPUnsignedTimeValue,
       "NTPStratum": NTPStratum,
       "NTPRefId": NTPRefId,
       "NTPPollInterval": NTPPollInterval,
       "NTPAssocIdentifier": NTPAssocIdentifier,
       "ciscoNtpMIB": ciscoNtpMIB,
       "ciscoNtpMIBNotifs": ciscoNtpMIBNotifs,
       "ciscoNtpSrvStatusChange": ciscoNtpSrvStatusChange,
       "ciscoNtpHighPriorityConnFailure": ciscoNtpHighPriorityConnFailure,
       "ciscoNtpHighPriorityConnRestore": ciscoNtpHighPriorityConnRestore,
       "ciscoNtpGeneralConnFailure": ciscoNtpGeneralConnFailure,
       "ciscoNtpGeneralConnRestore": ciscoNtpGeneralConnRestore,
       "ciscoNtpMIBObjects": ciscoNtpMIBObjects,
       "cntpSystem": cntpSystem,
       "cntpSysLeap": cntpSysLeap,
       "cntpSysStratum": cntpSysStratum,
       "cntpSysPrecision": cntpSysPrecision,
       "cntpSysRootDelay": cntpSysRootDelay,
       "cntpSysRootDispersion": cntpSysRootDispersion,
       "cntpSysRefId": cntpSysRefId,
       "cntpSysRefTime": cntpSysRefTime,
       "cntpSysPoll": cntpSysPoll,
       "cntpSysPeer": cntpSysPeer,
       "cntpSysClock": cntpSysClock,
       "cntpSysSrvStatus": cntpSysSrvStatus,
       "cntpPeers": cntpPeers,
       "cntpPeersVarTable": cntpPeersVarTable,
       "cntpPeersVarEntry": cntpPeersVarEntry,
       "cntpPeersAssocId": cntpPeersAssocId,
       "cntpPeersConfigured": cntpPeersConfigured,
       "cntpPeersPeerAddress": cntpPeersPeerAddress,
       "cntpPeersPeerPort": cntpPeersPeerPort,
       "cntpPeersHostAddress": cntpPeersHostAddress,
       "cntpPeersHostPort": cntpPeersHostPort,
       "cntpPeersLeap": cntpPeersLeap,
       "cntpPeersMode": cntpPeersMode,
       "cntpPeersStratum": cntpPeersStratum,
       "cntpPeersPeerPoll": cntpPeersPeerPoll,
       "cntpPeersHostPoll": cntpPeersHostPoll,
       "cntpPeersPrecision": cntpPeersPrecision,
       "cntpPeersRootDelay": cntpPeersRootDelay,
       "cntpPeersRootDispersion": cntpPeersRootDispersion,
       "cntpPeersRefId": cntpPeersRefId,
       "cntpPeersRefTime": cntpPeersRefTime,
       "cntpPeersOrgTime": cntpPeersOrgTime,
       "cntpPeersReceiveTime": cntpPeersReceiveTime,
       "cntpPeersTransmitTime": cntpPeersTransmitTime,
       "cntpPeersUpdateTime": cntpPeersUpdateTime,
       "cntpPeersReach": cntpPeersReach,
       "cntpPeersTimer": cntpPeersTimer,
       "cntpPeersOffset": cntpPeersOffset,
       "cntpPeersDelay": cntpPeersDelay,
       "cntpPeersDispersion": cntpPeersDispersion,
       "cntpPeersFilterValidEntries": cntpPeersFilterValidEntries,
       "cntpPeersEntryStatus": cntpPeersEntryStatus,
       "cntpPeersUpdateTimeRev1": cntpPeersUpdateTimeRev1,
       "cntpPeersPrefPeer": cntpPeersPrefPeer,
       "cntpPeersPeerType": cntpPeersPeerType,
       "cntpPeersPeerName": cntpPeersPeerName,
       "cntpFilter": cntpFilter,
       "cntpFilterRegisterTable": cntpFilterRegisterTable,
       "cntpFilterRegisterEntry": cntpFilterRegisterEntry,
       "cntpFilterIndex": cntpFilterIndex,
       "cntpFilterPeersOffset": cntpFilterPeersOffset,
       "cntpFilterPeersDelay": cntpFilterPeersDelay,
       "cntpFilterPeersDispersion": cntpFilterPeersDispersion,
       "ciscoNtpMIBConformance": ciscoNtpMIBConformance,
       "ciscoNtpMIBCompliances": ciscoNtpMIBCompliances,
       "ciscoNtpMIBCompliance": ciscoNtpMIBCompliance,
       "ciscoNtpMIBComplianceRev1": ciscoNtpMIBComplianceRev1,
       "ciscoNtpMIBComplianceRev2": ciscoNtpMIBComplianceRev2,
       "ciscoNtpMIBComplianceRev3": ciscoNtpMIBComplianceRev3,
       "ciscoNtpMIBComplianceRev4": ciscoNtpMIBComplianceRev4,
       "ciscoNtpMIBGroups": ciscoNtpMIBGroups,
       "ciscoNtpSysGroup": ciscoNtpSysGroup,
       "ciscoNtpPeersGroup": ciscoNtpPeersGroup,
       "ciscoNtpFilterGroup": ciscoNtpFilterGroup,
       "ciscoNtpPeersGroupRev1": ciscoNtpPeersGroupRev1,
       "ciscoNtpPeerExtGroup": ciscoNtpPeerExtGroup,
       "ciscoNtpPeersGroupRev2": ciscoNtpPeersGroupRev2,
       "ciscoNtpSysExtGroup": ciscoNtpSysExtGroup,
       "ciscoNtpSrvNotifGroup": ciscoNtpSrvNotifGroup}
)
