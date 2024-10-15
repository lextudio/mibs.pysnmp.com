# SNMP MIB module (CISCO-REMOTE-ACCESS-MONITOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-REMOTE-ACCESS-MONITOR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:07:28 2024
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
 iso,
 zeroDotZero) = mibBuilder.importSymbols(
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
    "zeroDotZero")

(DisplayString,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoRemoteAccessMonitorMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 392)
)
ciscoRemoteAccessMonitorMIB.setRevisions(
        ("2008-08-28 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RasProtocol(Integer32, TextualConvention):
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
        *(("ipsec", 2),
          ("l2f", 6),
          ("l2tp", 3),
          ("l2tpoveripsec", 4),
          ("other", 1),
          ("pptp", 5),
          ("ssl", 7))
    )



class UserAuthenMethod(Integer32, TextualConvention):
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
        *(("kerberos", 5),
          ("ldap", 7),
          ("local", 6),
          ("none", 1),
          ("ntlm", 8),
          ("other", 2),
          ("radius", 3),
          ("sdi", 9),
          ("tacacsplus", 4))
    )



class UserAuthorMethod(Integer32, TextualConvention):
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
        *(("kerberos", 5),
          ("ldap", 7),
          ("local", 6),
          ("none", 1),
          ("other", 2),
          ("radius", 3),
          ("tacacsplus", 4))
    )



class SessionEncrAlgo(Integer32, TextualConvention):
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
        *(("aes", 9),
          ("blowfish", 8),
          ("cast", 7),
          ("des", 2),
          ("des3", 3),
          ("idea", 6),
          ("none", 1),
          ("rc4", 4),
          ("rc5", 5))
    )



class SessionAuthAlgo(Integer32, TextualConvention):
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
        *(("hmacMd5", 3),
          ("hmacSha", 4),
          ("none", 1),
          ("other", 2))
    )



class SessionCompressionAlgo(Integer32, TextualConvention):
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
        *(("lzs", 3),
          ("none", 1),
          ("other", 2))
    )



class SessionStatus(Integer32, TextualConvention):
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
        *(("established", 2),
          ("initializing", 1),
          ("terminating", 3))
    )



class SessionIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class FailureRecordIndex(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoRasMonitorMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoRasMonitorMIBNotifs = _CiscoRasMonitorMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 0)
)
_CiscoRasMonitorMIBObjects_ObjectIdentity = ObjectIdentity
ciscoRasMonitorMIBObjects = _CiscoRasMonitorMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1)
)
_CrasCapacity_ObjectIdentity = ObjectIdentity
crasCapacity = _CrasCapacity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 1)
)


class _CrasMaxSessionsSupportable_Type(Integer32):
    """Custom type crasMaxSessionsSupportable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CrasMaxSessionsSupportable_Type.__name__ = "Integer32"
_CrasMaxSessionsSupportable_Object = MibScalar
crasMaxSessionsSupportable = _CrasMaxSessionsSupportable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 1, 1),
    _CrasMaxSessionsSupportable_Type()
)
crasMaxSessionsSupportable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasMaxSessionsSupportable.setStatus("current")
if mibBuilder.loadTexts:
    crasMaxSessionsSupportable.setUnits("Sessions")


class _CrasMaxUsersSupportable_Type(Integer32):
    """Custom type crasMaxUsersSupportable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CrasMaxUsersSupportable_Type.__name__ = "Integer32"
_CrasMaxUsersSupportable_Object = MibScalar
crasMaxUsersSupportable = _CrasMaxUsersSupportable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 1, 2),
    _CrasMaxUsersSupportable_Type()
)
crasMaxUsersSupportable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasMaxUsersSupportable.setStatus("current")
if mibBuilder.loadTexts:
    crasMaxUsersSupportable.setUnits("Users")


class _CrasMaxGroupsSupportable_Type(Integer32):
    """Custom type crasMaxGroupsSupportable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CrasMaxGroupsSupportable_Type.__name__ = "Integer32"
_CrasMaxGroupsSupportable_Object = MibScalar
crasMaxGroupsSupportable = _CrasMaxGroupsSupportable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 1, 3),
    _CrasMaxGroupsSupportable_Type()
)
crasMaxGroupsSupportable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasMaxGroupsSupportable.setStatus("current")
if mibBuilder.loadTexts:
    crasMaxGroupsSupportable.setUnits("Groups")


class _CrasNumCryptoAccelerators_Type(Integer32):
    """Custom type crasNumCryptoAccelerators based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CrasNumCryptoAccelerators_Type.__name__ = "Integer32"
_CrasNumCryptoAccelerators_Object = MibScalar
crasNumCryptoAccelerators = _CrasNumCryptoAccelerators_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 1, 4),
    _CrasNumCryptoAccelerators_Type()
)
crasNumCryptoAccelerators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasNumCryptoAccelerators.setStatus("current")
if mibBuilder.loadTexts:
    crasNumCryptoAccelerators.setUnits("Users")
_CrasResourceUsage_ObjectIdentity = ObjectIdentity
crasResourceUsage = _CrasResourceUsage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 2)
)
_CrasGlobalBwUsage_Type = Gauge32
_CrasGlobalBwUsage_Object = MibScalar
crasGlobalBwUsage = _CrasGlobalBwUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 2, 1),
    _CrasGlobalBwUsage_Type()
)
crasGlobalBwUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasGlobalBwUsage.setStatus("current")
if mibBuilder.loadTexts:
    crasGlobalBwUsage.setUnits("MBytes/second")
_CrasActivity_ObjectIdentity = ObjectIdentity
crasActivity = _CrasActivity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3)
)
_CrasNumSessions_Type = Gauge32
_CrasNumSessions_Object = MibScalar
crasNumSessions = _CrasNumSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 1),
    _CrasNumSessions_Type()
)
crasNumSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasNumSessions.setStatus("current")
if mibBuilder.loadTexts:
    crasNumSessions.setUnits("Sessions")
_CrasNumPrevSessions_Type = Counter32
_CrasNumPrevSessions_Object = MibScalar
crasNumPrevSessions = _CrasNumPrevSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 2),
    _CrasNumPrevSessions_Type()
)
crasNumPrevSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasNumPrevSessions.setStatus("current")
if mibBuilder.loadTexts:
    crasNumPrevSessions.setUnits("Sessions")
_CrasNumUsers_Type = Gauge32
_CrasNumUsers_Object = MibScalar
crasNumUsers = _CrasNumUsers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 3),
    _CrasNumUsers_Type()
)
crasNumUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasNumUsers.setStatus("current")
if mibBuilder.loadTexts:
    crasNumUsers.setUnits("Users")
_CrasNumGroups_Type = Gauge32
_CrasNumGroups_Object = MibScalar
crasNumGroups = _CrasNumGroups_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 4),
    _CrasNumGroups_Type()
)
crasNumGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasNumGroups.setStatus("current")
if mibBuilder.loadTexts:
    crasNumGroups.setUnits("Groups")
_CrasGlobalInPkts_Type = Counter64
_CrasGlobalInPkts_Object = MibScalar
crasGlobalInPkts = _CrasGlobalInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 5),
    _CrasGlobalInPkts_Type()
)
crasGlobalInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasGlobalInPkts.setStatus("current")
if mibBuilder.loadTexts:
    crasGlobalInPkts.setUnits("Packets")
_CrasGlobalOutPkts_Type = Counter64
_CrasGlobalOutPkts_Object = MibScalar
crasGlobalOutPkts = _CrasGlobalOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 6),
    _CrasGlobalOutPkts_Type()
)
crasGlobalOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasGlobalOutPkts.setStatus("current")
if mibBuilder.loadTexts:
    crasGlobalOutPkts.setUnits("Packets")
_CrasGlobalInOctets_Type = Counter64
_CrasGlobalInOctets_Object = MibScalar
crasGlobalInOctets = _CrasGlobalInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 7),
    _CrasGlobalInOctets_Type()
)
crasGlobalInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasGlobalInOctets.setStatus("current")
if mibBuilder.loadTexts:
    crasGlobalInOctets.setUnits("Octets")
_CrasGlobalInDecompOctets_Type = Counter64
_CrasGlobalInDecompOctets_Object = MibScalar
crasGlobalInDecompOctets = _CrasGlobalInDecompOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 8),
    _CrasGlobalInDecompOctets_Type()
)
crasGlobalInDecompOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasGlobalInDecompOctets.setStatus("current")
if mibBuilder.loadTexts:
    crasGlobalInDecompOctets.setUnits("Octets")
_CrasGlobalOutOctets_Type = Counter64
_CrasGlobalOutOctets_Object = MibScalar
crasGlobalOutOctets = _CrasGlobalOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 9),
    _CrasGlobalOutOctets_Type()
)
crasGlobalOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasGlobalOutOctets.setStatus("current")
if mibBuilder.loadTexts:
    crasGlobalOutOctets.setUnits("Octets")
_CrasGlobalOutUncompOctets_Type = Counter64
_CrasGlobalOutUncompOctets_Object = MibScalar
crasGlobalOutUncompOctets = _CrasGlobalOutUncompOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 10),
    _CrasGlobalOutUncompOctets_Type()
)
crasGlobalOutUncompOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasGlobalOutUncompOctets.setStatus("current")
if mibBuilder.loadTexts:
    crasGlobalOutUncompOctets.setUnits("Octets")
_CrasGlobalInDropPkts_Type = Counter64
_CrasGlobalInDropPkts_Object = MibScalar
crasGlobalInDropPkts = _CrasGlobalInDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 11),
    _CrasGlobalInDropPkts_Type()
)
crasGlobalInDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasGlobalInDropPkts.setStatus("current")
if mibBuilder.loadTexts:
    crasGlobalInDropPkts.setUnits("Packets")
_CrasGlobalOutDropPkts_Type = Counter64
_CrasGlobalOutDropPkts_Object = MibScalar
crasGlobalOutDropPkts = _CrasGlobalOutDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 12),
    _CrasGlobalOutDropPkts_Type()
)
crasGlobalOutDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasGlobalOutDropPkts.setStatus("current")
if mibBuilder.loadTexts:
    crasGlobalOutDropPkts.setUnits("Packets")
_CrasSessionTable_Object = MibTable
crasSessionTable = _CrasSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 21)
)
if mibBuilder.loadTexts:
    crasSessionTable.setStatus("current")
_CrasSessionEntry_Object = MibTableRow
crasSessionEntry = _CrasSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 21, 1)
)
crasSessionEntry.setIndexNames(
    (0, "CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasUsername"),
    (0, "CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasSessionIndex"),
)
if mibBuilder.loadTexts:
    crasSessionEntry.setStatus("current")


class _CrasUsername_Type(SnmpAdminString):
    """Custom type crasUsername based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CrasUsername_Type.__name__ = "SnmpAdminString"
_CrasUsername_Object = MibTableColumn
crasUsername = _CrasUsername_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 21, 1, 1),
    _CrasUsername_Type()
)
crasUsername.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crasUsername.setStatus("current")
_CrasGroup_Type = SnmpAdminString
_CrasGroup_Object = MibTableColumn
crasGroup = _CrasGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 21, 1, 2),
    _CrasGroup_Type()
)
crasGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasGroup.setStatus("current")
_CrasSessionIndex_Type = SessionIndex
_CrasSessionIndex_Object = MibTableColumn
crasSessionIndex = _CrasSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 21, 1, 3),
    _CrasSessionIndex_Type()
)
crasSessionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crasSessionIndex.setStatus("current")
_CrasAuthenMethod_Type = UserAuthenMethod
_CrasAuthenMethod_Object = MibTableColumn
crasAuthenMethod = _CrasAuthenMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 21, 1, 4),
    _CrasAuthenMethod_Type()
)
crasAuthenMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasAuthenMethod.setStatus("current")
_CrasAuthorMethod_Type = UserAuthorMethod
_CrasAuthorMethod_Object = MibTableColumn
crasAuthorMethod = _CrasAuthorMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 21, 1, 5),
    _CrasAuthorMethod_Type()
)
crasAuthorMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasAuthorMethod.setStatus("current")
_CrasSessionDuration_Type = Counter32
_CrasSessionDuration_Object = MibTableColumn
crasSessionDuration = _CrasSessionDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 21, 1, 6),
    _CrasSessionDuration_Type()
)
crasSessionDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasSessionDuration.setStatus("current")
_CrasLocalAddressType_Type = InetAddressType
_CrasLocalAddressType_Object = MibTableColumn
crasLocalAddressType = _CrasLocalAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 21, 1, 7),
    _CrasLocalAddressType_Type()
)
crasLocalAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasLocalAddressType.setStatus("current")
_CrasLocalAddress_Type = InetAddress
_CrasLocalAddress_Object = MibTableColumn
crasLocalAddress = _CrasLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 21, 1, 8),
    _CrasLocalAddress_Type()
)
crasLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasLocalAddress.setStatus("current")
_CrasISPAddressType_Type = InetAddressType
_CrasISPAddressType_Object = MibTableColumn
crasISPAddressType = _CrasISPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 21, 1, 9),
    _CrasISPAddressType_Type()
)
crasISPAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasISPAddressType.setStatus("current")
_CrasISPAddress_Type = InetAddress
_CrasISPAddress_Object = MibTableColumn
crasISPAddress = _CrasISPAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 21, 1, 10),
    _CrasISPAddress_Type()
)
crasISPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasISPAddress.setStatus("current")
_CrasSessionProtocol_Type = RasProtocol
_CrasSessionProtocol_Object = MibTableColumn
crasSessionProtocol = _CrasSessionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 21, 1, 11),
    _CrasSessionProtocol_Type()
)
crasSessionProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasSessionProtocol.setStatus("current")


class _CrasProtocolElement_Type(ObjectIdentifier):
    """Custom type crasProtocolElement based on ObjectIdentifier"""
    defaultValue = (0, 0)


_CrasProtocolElement_Object = MibTableColumn
crasProtocolElement = _CrasProtocolElement_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 21, 1, 12),
    _CrasProtocolElement_Type()
)
crasProtocolElement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasProtocolElement.setStatus("current")
_CrasSessionEncryptionAlgo_Type = SessionEncrAlgo
_CrasSessionEncryptionAlgo_Object = MibTableColumn
crasSessionEncryptionAlgo = _CrasSessionEncryptionAlgo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 21, 1, 13),
    _CrasSessionEncryptionAlgo_Type()
)
crasSessionEncryptionAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasSessionEncryptionAlgo.setStatus("current")
_CrasSessionPktAuthenAlgo_Type = SessionAuthAlgo
_CrasSessionPktAuthenAlgo_Object = MibTableColumn
crasSessionPktAuthenAlgo = _CrasSessionPktAuthenAlgo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 21, 1, 14),
    _CrasSessionPktAuthenAlgo_Type()
)
crasSessionPktAuthenAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasSessionPktAuthenAlgo.setStatus("current")
_CrasSessionCompressionAlgo_Type = SessionCompressionAlgo
_CrasSessionCompressionAlgo_Object = MibTableColumn
crasSessionCompressionAlgo = _CrasSessionCompressionAlgo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 21, 1, 15),
    _CrasSessionCompressionAlgo_Type()
)
crasSessionCompressionAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasSessionCompressionAlgo.setStatus("current")


class _CrasHeartbeatInterval_Type(Unsigned32):
    """Custom type crasHeartbeatInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CrasHeartbeatInterval_Type.__name__ = "Unsigned32"
_CrasHeartbeatInterval_Object = MibTableColumn
crasHeartbeatInterval = _CrasHeartbeatInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 21, 1, 16),
    _CrasHeartbeatInterval_Type()
)
crasHeartbeatInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasHeartbeatInterval.setStatus("current")
if mibBuilder.loadTexts:
    crasHeartbeatInterval.setUnits("Seconds")
_CrasClientVendorString_Type = SnmpAdminString
_CrasClientVendorString_Object = MibTableColumn
crasClientVendorString = _CrasClientVendorString_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 21, 1, 17),
    _CrasClientVendorString_Type()
)
crasClientVendorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasClientVendorString.setStatus("current")
_CrasClientVersionString_Type = SnmpAdminString
_CrasClientVersionString_Object = MibTableColumn
crasClientVersionString = _CrasClientVersionString_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 21, 1, 18),
    _CrasClientVersionString_Type()
)
crasClientVersionString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasClientVersionString.setStatus("current")
_CrasClientOSVendorString_Type = SnmpAdminString
_CrasClientOSVendorString_Object = MibTableColumn
crasClientOSVendorString = _CrasClientOSVendorString_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 21, 1, 19),
    _CrasClientOSVendorString_Type()
)
crasClientOSVendorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasClientOSVendorString.setStatus("current")
_CrasClientOSVersionString_Type = SnmpAdminString
_CrasClientOSVersionString_Object = MibTableColumn
crasClientOSVersionString = _CrasClientOSVersionString_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 21, 1, 20),
    _CrasClientOSVersionString_Type()
)
crasClientOSVersionString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasClientOSVersionString.setStatus("current")
_CrasPrimWINSServerAddrType_Type = InetAddressType
_CrasPrimWINSServerAddrType_Object = MibTableColumn
crasPrimWINSServerAddrType = _CrasPrimWINSServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 21, 1, 21),
    _CrasPrimWINSServerAddrType_Type()
)
crasPrimWINSServerAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasPrimWINSServerAddrType.setStatus("current")
_CrasPrimWINSServer_Type = InetAddress
_CrasPrimWINSServer_Object = MibTableColumn
crasPrimWINSServer = _CrasPrimWINSServer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 21, 1, 22),
    _CrasPrimWINSServer_Type()
)
crasPrimWINSServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasPrimWINSServer.setStatus("current")
_CrasSecWINSServerAddrType_Type = InetAddressType
_CrasSecWINSServerAddrType_Object = MibTableColumn
crasSecWINSServerAddrType = _CrasSecWINSServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 21, 1, 23),
    _CrasSecWINSServerAddrType_Type()
)
crasSecWINSServerAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasSecWINSServerAddrType.setStatus("current")
_CrasSecWINSServer_Type = InetAddress
_CrasSecWINSServer_Object = MibTableColumn
crasSecWINSServer = _CrasSecWINSServer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 21, 1, 24),
    _CrasSecWINSServer_Type()
)
crasSecWINSServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasSecWINSServer.setStatus("current")
_CrasPrimDNSServerAddrType_Type = InetAddressType
_CrasPrimDNSServerAddrType_Object = MibTableColumn
crasPrimDNSServerAddrType = _CrasPrimDNSServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 21, 1, 25),
    _CrasPrimDNSServerAddrType_Type()
)
crasPrimDNSServerAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasPrimDNSServerAddrType.setStatus("current")
_CrasPrimDNSServer_Type = InetAddress
_CrasPrimDNSServer_Object = MibTableColumn
crasPrimDNSServer = _CrasPrimDNSServer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 21, 1, 26),
    _CrasPrimDNSServer_Type()
)
crasPrimDNSServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasPrimDNSServer.setStatus("current")
_CrasSecDNSServerAddrType_Type = InetAddressType
_CrasSecDNSServerAddrType_Object = MibTableColumn
crasSecDNSServerAddrType = _CrasSecDNSServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 21, 1, 27),
    _CrasSecDNSServerAddrType_Type()
)
crasSecDNSServerAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasSecDNSServerAddrType.setStatus("current")
_CrasSecDNSServer_Type = InetAddress
_CrasSecDNSServer_Object = MibTableColumn
crasSecDNSServer = _CrasSecDNSServer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 21, 1, 28),
    _CrasSecDNSServer_Type()
)
crasSecDNSServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasSecDNSServer.setStatus("current")
_CrasDHCPServerAddrType_Type = InetAddressType
_CrasDHCPServerAddrType_Object = MibTableColumn
crasDHCPServerAddrType = _CrasDHCPServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 21, 1, 29),
    _CrasDHCPServerAddrType_Type()
)
crasDHCPServerAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasDHCPServerAddrType.setStatus("current")
_CrasDHCPServer_Type = InetAddress
_CrasDHCPServer_Object = MibTableColumn
crasDHCPServer = _CrasDHCPServer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 21, 1, 30),
    _CrasDHCPServer_Type()
)
crasDHCPServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasDHCPServer.setStatus("current")
_CrasSessionInPkts_Type = Counter64
_CrasSessionInPkts_Object = MibTableColumn
crasSessionInPkts = _CrasSessionInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 21, 1, 31),
    _CrasSessionInPkts_Type()
)
crasSessionInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasSessionInPkts.setStatus("current")
if mibBuilder.loadTexts:
    crasSessionInPkts.setUnits("Packets")
_CrasSessionOutPkts_Type = Counter64
_CrasSessionOutPkts_Object = MibTableColumn
crasSessionOutPkts = _CrasSessionOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 21, 1, 32),
    _CrasSessionOutPkts_Type()
)
crasSessionOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasSessionOutPkts.setStatus("current")
if mibBuilder.loadTexts:
    crasSessionOutPkts.setUnits("Packets")
_CrasSessionInDropPkts_Type = Counter64
_CrasSessionInDropPkts_Object = MibTableColumn
crasSessionInDropPkts = _CrasSessionInDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 21, 1, 33),
    _CrasSessionInDropPkts_Type()
)
crasSessionInDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasSessionInDropPkts.setStatus("current")
if mibBuilder.loadTexts:
    crasSessionInDropPkts.setUnits("Packets")
_CrasSessionOutDropPkts_Type = Counter64
_CrasSessionOutDropPkts_Object = MibTableColumn
crasSessionOutDropPkts = _CrasSessionOutDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 21, 1, 34),
    _CrasSessionOutDropPkts_Type()
)
crasSessionOutDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasSessionOutDropPkts.setStatus("current")
if mibBuilder.loadTexts:
    crasSessionOutDropPkts.setUnits("Packets")
_CrasSessionInOctets_Type = Counter64
_CrasSessionInOctets_Object = MibTableColumn
crasSessionInOctets = _CrasSessionInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 21, 1, 35),
    _CrasSessionInOctets_Type()
)
crasSessionInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasSessionInOctets.setStatus("current")
if mibBuilder.loadTexts:
    crasSessionInOctets.setUnits("Octets")
_CrasSessionOutOctets_Type = Counter64
_CrasSessionOutOctets_Object = MibTableColumn
crasSessionOutOctets = _CrasSessionOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 21, 1, 36),
    _CrasSessionOutOctets_Type()
)
crasSessionOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasSessionOutOctets.setStatus("current")
if mibBuilder.loadTexts:
    crasSessionOutOctets.setUnits("Octets")
_CrasSessionState_Type = SessionStatus
_CrasSessionState_Object = MibTableColumn
crasSessionState = _CrasSessionState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 21, 1, 37),
    _CrasSessionState_Type()
)
crasSessionState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crasSessionState.setStatus("current")
_CrasActGroupTable_Object = MibTable
crasActGroupTable = _CrasActGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 22)
)
if mibBuilder.loadTexts:
    crasActGroupTable.setStatus("current")
_CrasActGroupEntry_Object = MibTableRow
crasActGroupEntry = _CrasActGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 22, 1)
)
crasActGroupEntry.setIndexNames(
    (0, "CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasActGrpName"),
)
if mibBuilder.loadTexts:
    crasActGroupEntry.setStatus("current")


class _CrasActGrpName_Type(SnmpAdminString):
    """Custom type crasActGrpName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CrasActGrpName_Type.__name__ = "SnmpAdminString"
_CrasActGrpName_Object = MibTableColumn
crasActGrpName = _CrasActGrpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 22, 1, 1),
    _CrasActGrpName_Type()
)
crasActGrpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crasActGrpName.setStatus("current")


class _CrasActGrNumUsers_Type(Integer32):
    """Custom type crasActGrNumUsers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CrasActGrNumUsers_Type.__name__ = "Integer32"
_CrasActGrNumUsers_Object = MibTableColumn
crasActGrNumUsers = _CrasActGrNumUsers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 22, 1, 2),
    _CrasActGrNumUsers_Type()
)
crasActGrNumUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasActGrNumUsers.setStatus("current")
_CrasActGrpInPkts_Type = Counter64
_CrasActGrpInPkts_Object = MibTableColumn
crasActGrpInPkts = _CrasActGrpInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 22, 1, 3),
    _CrasActGrpInPkts_Type()
)
crasActGrpInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasActGrpInPkts.setStatus("current")
if mibBuilder.loadTexts:
    crasActGrpInPkts.setUnits("Packets")
_CrasActGrpOutPkts_Type = Counter64
_CrasActGrpOutPkts_Object = MibTableColumn
crasActGrpOutPkts = _CrasActGrpOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 22, 1, 4),
    _CrasActGrpOutPkts_Type()
)
crasActGrpOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasActGrpOutPkts.setStatus("current")
if mibBuilder.loadTexts:
    crasActGrpOutPkts.setUnits("Packets")
_CrasActGrpInDropPkts_Type = Counter64
_CrasActGrpInDropPkts_Object = MibTableColumn
crasActGrpInDropPkts = _CrasActGrpInDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 22, 1, 5),
    _CrasActGrpInDropPkts_Type()
)
crasActGrpInDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasActGrpInDropPkts.setStatus("current")
if mibBuilder.loadTexts:
    crasActGrpInDropPkts.setUnits("Packets")
_CrasActGrpOutDropPkts_Type = Counter64
_CrasActGrpOutDropPkts_Object = MibTableColumn
crasActGrpOutDropPkts = _CrasActGrpOutDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 22, 1, 6),
    _CrasActGrpOutDropPkts_Type()
)
crasActGrpOutDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasActGrpOutDropPkts.setStatus("current")
if mibBuilder.loadTexts:
    crasActGrpOutDropPkts.setUnits("Packets")
_CrasActGrpInOctets_Type = Counter64
_CrasActGrpInOctets_Object = MibTableColumn
crasActGrpInOctets = _CrasActGrpInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 22, 1, 7),
    _CrasActGrpInOctets_Type()
)
crasActGrpInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasActGrpInOctets.setStatus("current")
if mibBuilder.loadTexts:
    crasActGrpInOctets.setUnits("Octets")
_CrasActGrpOutOctets_Type = Counter64
_CrasActGrpOutOctets_Object = MibTableColumn
crasActGrpOutOctets = _CrasActGrpOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 22, 1, 8),
    _CrasActGrpOutOctets_Type()
)
crasActGrpOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasActGrpOutOctets.setStatus("current")
if mibBuilder.loadTexts:
    crasActGrpOutOctets.setUnits("Octets")
_CrasEmailNumSessions_Type = Gauge32
_CrasEmailNumSessions_Object = MibScalar
crasEmailNumSessions = _CrasEmailNumSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 23),
    _CrasEmailNumSessions_Type()
)
crasEmailNumSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasEmailNumSessions.setStatus("current")
if mibBuilder.loadTexts:
    crasEmailNumSessions.setUnits("Sessions")
_CrasEmailCumulateSessions_Type = Counter32
_CrasEmailCumulateSessions_Object = MibScalar
crasEmailCumulateSessions = _CrasEmailCumulateSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 24),
    _CrasEmailCumulateSessions_Type()
)
crasEmailCumulateSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasEmailCumulateSessions.setStatus("current")
if mibBuilder.loadTexts:
    crasEmailCumulateSessions.setUnits("Sessions")
_CrasEmailPeakConcurrentSessions_Type = Unsigned32
_CrasEmailPeakConcurrentSessions_Object = MibScalar
crasEmailPeakConcurrentSessions = _CrasEmailPeakConcurrentSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 25),
    _CrasEmailPeakConcurrentSessions_Type()
)
crasEmailPeakConcurrentSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasEmailPeakConcurrentSessions.setStatus("current")
if mibBuilder.loadTexts:
    crasEmailPeakConcurrentSessions.setUnits("Sessions")
_CrasIPSecNumSessions_Type = Gauge32
_CrasIPSecNumSessions_Object = MibScalar
crasIPSecNumSessions = _CrasIPSecNumSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 26),
    _CrasIPSecNumSessions_Type()
)
crasIPSecNumSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasIPSecNumSessions.setStatus("current")
if mibBuilder.loadTexts:
    crasIPSecNumSessions.setUnits("Sessions")
_CrasIPSecCumulateSessions_Type = Counter32
_CrasIPSecCumulateSessions_Object = MibScalar
crasIPSecCumulateSessions = _CrasIPSecCumulateSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 27),
    _CrasIPSecCumulateSessions_Type()
)
crasIPSecCumulateSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasIPSecCumulateSessions.setStatus("current")
if mibBuilder.loadTexts:
    crasIPSecCumulateSessions.setUnits("Sessions")
_CrasIPSecPeakConcurrentSessions_Type = Unsigned32
_CrasIPSecPeakConcurrentSessions_Object = MibScalar
crasIPSecPeakConcurrentSessions = _CrasIPSecPeakConcurrentSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 28),
    _CrasIPSecPeakConcurrentSessions_Type()
)
crasIPSecPeakConcurrentSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasIPSecPeakConcurrentSessions.setStatus("current")
if mibBuilder.loadTexts:
    crasIPSecPeakConcurrentSessions.setUnits("Sessions")
_CrasL2LNumSessions_Type = Gauge32
_CrasL2LNumSessions_Object = MibScalar
crasL2LNumSessions = _CrasL2LNumSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 29),
    _CrasL2LNumSessions_Type()
)
crasL2LNumSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasL2LNumSessions.setStatus("current")
if mibBuilder.loadTexts:
    crasL2LNumSessions.setUnits("Sessions")
_CrasL2LCumulateSessions_Type = Counter32
_CrasL2LCumulateSessions_Object = MibScalar
crasL2LCumulateSessions = _CrasL2LCumulateSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 30),
    _CrasL2LCumulateSessions_Type()
)
crasL2LCumulateSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasL2LCumulateSessions.setStatus("current")
if mibBuilder.loadTexts:
    crasL2LCumulateSessions.setUnits("Sessions")
_CrasL2LPeakConcurrentSessions_Type = Unsigned32
_CrasL2LPeakConcurrentSessions_Object = MibScalar
crasL2LPeakConcurrentSessions = _CrasL2LPeakConcurrentSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 31),
    _CrasL2LPeakConcurrentSessions_Type()
)
crasL2LPeakConcurrentSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasL2LPeakConcurrentSessions.setStatus("current")
if mibBuilder.loadTexts:
    crasL2LPeakConcurrentSessions.setUnits("Sessions")
_CrasLBNumSessions_Type = Gauge32
_CrasLBNumSessions_Object = MibScalar
crasLBNumSessions = _CrasLBNumSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 32),
    _CrasLBNumSessions_Type()
)
crasLBNumSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasLBNumSessions.setStatus("current")
if mibBuilder.loadTexts:
    crasLBNumSessions.setUnits("Sessions")
_CrasLBCumulateSessions_Type = Counter32
_CrasLBCumulateSessions_Object = MibScalar
crasLBCumulateSessions = _CrasLBCumulateSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 33),
    _CrasLBCumulateSessions_Type()
)
crasLBCumulateSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasLBCumulateSessions.setStatus("current")
if mibBuilder.loadTexts:
    crasLBCumulateSessions.setUnits("Sessions")
_CrasLBPeakConcurrentSessions_Type = Unsigned32
_CrasLBPeakConcurrentSessions_Object = MibScalar
crasLBPeakConcurrentSessions = _CrasLBPeakConcurrentSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 34),
    _CrasLBPeakConcurrentSessions_Type()
)
crasLBPeakConcurrentSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasLBPeakConcurrentSessions.setStatus("current")
if mibBuilder.loadTexts:
    crasLBPeakConcurrentSessions.setUnits("Sessions")
_CrasSVCNumSessions_Type = Gauge32
_CrasSVCNumSessions_Object = MibScalar
crasSVCNumSessions = _CrasSVCNumSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 35),
    _CrasSVCNumSessions_Type()
)
crasSVCNumSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasSVCNumSessions.setStatus("current")
if mibBuilder.loadTexts:
    crasSVCNumSessions.setUnits("Sessions")
_CrasSVCCumulateSessions_Type = Counter32
_CrasSVCCumulateSessions_Object = MibScalar
crasSVCCumulateSessions = _CrasSVCCumulateSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 36),
    _CrasSVCCumulateSessions_Type()
)
crasSVCCumulateSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasSVCCumulateSessions.setStatus("current")
if mibBuilder.loadTexts:
    crasSVCCumulateSessions.setUnits("Sessions")
_CrasSVCPeakConcurrentSessions_Type = Unsigned32
_CrasSVCPeakConcurrentSessions_Object = MibScalar
crasSVCPeakConcurrentSessions = _CrasSVCPeakConcurrentSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 37),
    _CrasSVCPeakConcurrentSessions_Type()
)
crasSVCPeakConcurrentSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasSVCPeakConcurrentSessions.setStatus("current")
if mibBuilder.loadTexts:
    crasSVCPeakConcurrentSessions.setUnits("Sessions")
_CrasWebvpnNumSessions_Type = Gauge32
_CrasWebvpnNumSessions_Object = MibScalar
crasWebvpnNumSessions = _CrasWebvpnNumSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 38),
    _CrasWebvpnNumSessions_Type()
)
crasWebvpnNumSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasWebvpnNumSessions.setStatus("current")
if mibBuilder.loadTexts:
    crasWebvpnNumSessions.setUnits("Sessions")
_CrasWebvpnCumulateSessions_Type = Counter32
_CrasWebvpnCumulateSessions_Object = MibScalar
crasWebvpnCumulateSessions = _CrasWebvpnCumulateSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 39),
    _CrasWebvpnCumulateSessions_Type()
)
crasWebvpnCumulateSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasWebvpnCumulateSessions.setStatus("current")
if mibBuilder.loadTexts:
    crasWebvpnCumulateSessions.setUnits("Sessions")
_CrasWebvpnPeakConcurrentSessions_Type = Unsigned32
_CrasWebvpnPeakConcurrentSessions_Object = MibScalar
crasWebvpnPeakConcurrentSessions = _CrasWebvpnPeakConcurrentSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 3, 40),
    _CrasWebvpnPeakConcurrentSessions_Type()
)
crasWebvpnPeakConcurrentSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasWebvpnPeakConcurrentSessions.setStatus("current")
if mibBuilder.loadTexts:
    crasWebvpnPeakConcurrentSessions.setUnits("Sessions")
_CrasFailures_ObjectIdentity = ObjectIdentity
crasFailures = _CrasFailures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 4)
)
_CrasFailuresGlobals_ObjectIdentity = ObjectIdentity
crasFailuresGlobals = _CrasFailuresGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 4, 1)
)
_CrasNumTotalFailures_Type = Counter64
_CrasNumTotalFailures_Object = MibScalar
crasNumTotalFailures = _CrasNumTotalFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 4, 1, 1),
    _CrasNumTotalFailures_Type()
)
crasNumTotalFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasNumTotalFailures.setStatus("current")


class _CrasNumDeclinedSessions_Type(Unsigned32):
    """Custom type crasNumDeclinedSessions based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CrasNumDeclinedSessions_Type.__name__ = "Unsigned32"
_CrasNumDeclinedSessions_Object = MibScalar
crasNumDeclinedSessions = _CrasNumDeclinedSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 4, 1, 2),
    _CrasNumDeclinedSessions_Type()
)
crasNumDeclinedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasNumDeclinedSessions.setStatus("current")
if mibBuilder.loadTexts:
    crasNumDeclinedSessions.setUnits("Sessions")
_CrasNumSetupFailInsufResources_Type = Counter64
_CrasNumSetupFailInsufResources_Object = MibScalar
crasNumSetupFailInsufResources = _CrasNumSetupFailInsufResources_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 4, 1, 3),
    _CrasNumSetupFailInsufResources_Type()
)
crasNumSetupFailInsufResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasNumSetupFailInsufResources.setStatus("current")
if mibBuilder.loadTexts:
    crasNumSetupFailInsufResources.setUnits("Sessions")
_CrasNumAbortedSessions_Type = Counter64
_CrasNumAbortedSessions_Object = MibScalar
crasNumAbortedSessions = _CrasNumAbortedSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 4, 1, 4),
    _CrasNumAbortedSessions_Type()
)
crasNumAbortedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasNumAbortedSessions.setStatus("current")
if mibBuilder.loadTexts:
    crasNumAbortedSessions.setUnits("Sessions")
_CrasFailGlobalCntl_ObjectIdentity = ObjectIdentity
crasFailGlobalCntl = _CrasFailGlobalCntl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 4, 2)
)


class _CrasFailTableSize_Type(Unsigned32):
    """Custom type crasFailTableSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CrasFailTableSize_Type.__name__ = "Unsigned32"
_CrasFailTableSize_Object = MibScalar
crasFailTableSize = _CrasFailTableSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 4, 2, 1),
    _CrasFailTableSize_Type()
)
crasFailTableSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crasFailTableSize.setStatus("current")
_CrasSessFailures_ObjectIdentity = ObjectIdentity
crasSessFailures = _CrasSessFailures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 4, 3)
)
_CrasSessFailTable_Object = MibTable
crasSessFailTable = _CrasSessFailTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 4, 3, 1)
)
if mibBuilder.loadTexts:
    crasSessFailTable.setStatus("current")
_CrasSessFailEntry_Object = MibTableRow
crasSessFailEntry = _CrasSessFailEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 4, 3, 1, 1)
)
crasSessFailEntry.setIndexNames(
    (0, "CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasSessFailIndex"),
)
if mibBuilder.loadTexts:
    crasSessFailEntry.setStatus("current")
_CrasSessFailIndex_Type = FailureRecordIndex
_CrasSessFailIndex_Object = MibTableColumn
crasSessFailIndex = _CrasSessFailIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 4, 3, 1, 1, 1),
    _CrasSessFailIndex_Type()
)
crasSessFailIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crasSessFailIndex.setStatus("current")
_CrasSessFailUsername_Type = SnmpAdminString
_CrasSessFailUsername_Object = MibTableColumn
crasSessFailUsername = _CrasSessFailUsername_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 4, 3, 1, 1, 2),
    _CrasSessFailUsername_Type()
)
crasSessFailUsername.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasSessFailUsername.setStatus("current")
_CrasSessFailGroupname_Type = SnmpAdminString
_CrasSessFailGroupname_Object = MibTableColumn
crasSessFailGroupname = _CrasSessFailGroupname_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 4, 3, 1, 1, 3),
    _CrasSessFailGroupname_Type()
)
crasSessFailGroupname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasSessFailGroupname.setStatus("current")


class _CrasSessFailType_Type(Integer32):
    """Custom type crasSessFailType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("operationalFailure", 2),
          ("setupFailure", 1))
    )


_CrasSessFailType_Type.__name__ = "Integer32"
_CrasSessFailType_Object = MibTableColumn
crasSessFailType = _CrasSessFailType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 4, 3, 1, 1, 4),
    _CrasSessFailType_Type()
)
crasSessFailType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasSessFailType.setStatus("current")


class _CrasSessFailReason_Type(Integer32):
    """Custom type crasSessFailReason based on Integer32"""
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
        *(("authenticationFailure", 3),
          ("authorizationFailure", 4),
          ("internalError", 2),
          ("operRequest", 8),
          ("other", 1),
          ("peerAbortRequest", 6),
          ("peerLost", 7),
          ("sysCapExceeded", 5))
    )


_CrasSessFailReason_Type.__name__ = "Integer32"
_CrasSessFailReason_Object = MibTableColumn
crasSessFailReason = _CrasSessFailReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 4, 3, 1, 1, 5),
    _CrasSessFailReason_Type()
)
crasSessFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasSessFailReason.setStatus("current")
_CrasSessFailTime_Type = TimeStamp
_CrasSessFailTime_Object = MibTableColumn
crasSessFailTime = _CrasSessFailTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 4, 3, 1, 1, 6),
    _CrasSessFailTime_Type()
)
crasSessFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasSessFailTime.setStatus("current")
_CrasSessFailSessionIndex_Type = SessionIndex
_CrasSessFailSessionIndex_Object = MibTableColumn
crasSessFailSessionIndex = _CrasSessFailSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 4, 3, 1, 1, 7),
    _CrasSessFailSessionIndex_Type()
)
crasSessFailSessionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasSessFailSessionIndex.setStatus("current")
_CrasSessFailISPAddrType_Type = InetAddressType
_CrasSessFailISPAddrType_Object = MibTableColumn
crasSessFailISPAddrType = _CrasSessFailISPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 4, 3, 1, 1, 8),
    _CrasSessFailISPAddrType_Type()
)
crasSessFailISPAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasSessFailISPAddrType.setStatus("current")
_CrasSessFailISPAddr_Type = InetAddress
_CrasSessFailISPAddr_Object = MibTableColumn
crasSessFailISPAddr = _CrasSessFailISPAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 4, 3, 1, 1, 9),
    _CrasSessFailISPAddr_Type()
)
crasSessFailISPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasSessFailISPAddr.setStatus("current")
_CrasSessFailLocalAddrType_Type = InetAddressType
_CrasSessFailLocalAddrType_Object = MibTableColumn
crasSessFailLocalAddrType = _CrasSessFailLocalAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 4, 3, 1, 1, 10),
    _CrasSessFailLocalAddrType_Type()
)
crasSessFailLocalAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasSessFailLocalAddrType.setStatus("current")
_CrasSessFailLocalAddr_Type = InetAddress
_CrasSessFailLocalAddr_Object = MibTableColumn
crasSessFailLocalAddr = _CrasSessFailLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 4, 3, 1, 1, 11),
    _CrasSessFailLocalAddr_Type()
)
crasSessFailLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasSessFailLocalAddr.setStatus("current")
_CrasFailLastFailIndex_Type = FailureRecordIndex
_CrasFailLastFailIndex_Object = MibScalar
crasFailLastFailIndex = _CrasFailLastFailIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 4, 3, 2),
    _CrasFailLastFailIndex_Type()
)
crasFailLastFailIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasFailLastFailIndex.setStatus("current")
_CrasGroupFailures_ObjectIdentity = ObjectIdentity
crasGroupFailures = _CrasGroupFailures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 4, 4)
)
_CrasGrpFailTable_Object = MibTable
crasGrpFailTable = _CrasGrpFailTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 4, 4, 1)
)
if mibBuilder.loadTexts:
    crasGrpFailTable.setStatus("current")
_CrasGrpFailEntry_Object = MibTableRow
crasGrpFailEntry = _CrasGrpFailEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 4, 4, 1, 1)
)
crasGrpFailEntry.setIndexNames(
    (0, "CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasGrpFailGroupname"),
)
if mibBuilder.loadTexts:
    crasGrpFailEntry.setStatus("current")


class _CrasGrpFailGroupname_Type(SnmpAdminString):
    """Custom type crasGrpFailGroupname based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CrasGrpFailGroupname_Type.__name__ = "SnmpAdminString"
_CrasGrpFailGroupname_Object = MibTableColumn
crasGrpFailGroupname = _CrasGrpFailGroupname_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 4, 4, 1, 1, 1),
    _CrasGrpFailGroupname_Type()
)
crasGrpFailGroupname.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crasGrpFailGroupname.setStatus("current")
_CrasGrpFailNumFailAuths_Type = Counter64
_CrasGrpFailNumFailAuths_Object = MibTableColumn
crasGrpFailNumFailAuths = _CrasGrpFailNumFailAuths_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 4, 4, 1, 1, 2),
    _CrasGrpFailNumFailAuths_Type()
)
crasGrpFailNumFailAuths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasGrpFailNumFailAuths.setStatus("current")
_CrasGrpFailNumResourceFailures_Type = Counter64
_CrasGrpFailNumResourceFailures_Object = MibTableColumn
crasGrpFailNumResourceFailures = _CrasGrpFailNumResourceFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 4, 4, 1, 1, 3),
    _CrasGrpFailNumResourceFailures_Type()
)
crasGrpFailNumResourceFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasGrpFailNumResourceFailures.setStatus("current")
_CrasGrpFailNumDeclined_Type = Counter64
_CrasGrpFailNumDeclined_Object = MibTableColumn
crasGrpFailNumDeclined = _CrasGrpFailNumDeclined_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 4, 4, 1, 1, 4),
    _CrasGrpFailNumDeclined_Type()
)
crasGrpFailNumDeclined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasGrpFailNumDeclined.setStatus("current")
_CrasGrpFailNumTerminatedMgmt_Type = Counter64
_CrasGrpFailNumTerminatedMgmt_Object = MibTableColumn
crasGrpFailNumTerminatedMgmt = _CrasGrpFailNumTerminatedMgmt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 4, 4, 1, 1, 5),
    _CrasGrpFailNumTerminatedMgmt_Type()
)
crasGrpFailNumTerminatedMgmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasGrpFailNumTerminatedMgmt.setStatus("current")
_CrasGrpFailNumTerminatedOther_Type = Counter64
_CrasGrpFailNumTerminatedOther_Object = MibTableColumn
crasGrpFailNumTerminatedOther = _CrasGrpFailNumTerminatedOther_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 4, 4, 1, 1, 6),
    _CrasGrpFailNumTerminatedOther_Type()
)
crasGrpFailNumTerminatedOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasGrpFailNumTerminatedOther.setStatus("current")
_CrasSecurity_ObjectIdentity = ObjectIdentity
crasSecurity = _CrasSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 5)
)
_CrasSecurityGlobals_ObjectIdentity = ObjectIdentity
crasSecurityGlobals = _CrasSecurityGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 5, 1)
)
_CrasNumDisabledAccounts_Type = Counter64
_CrasNumDisabledAccounts_Object = MibScalar
crasNumDisabledAccounts = _CrasNumDisabledAccounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 5, 1, 1),
    _CrasNumDisabledAccounts_Type()
)
crasNumDisabledAccounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasNumDisabledAccounts.setStatus("current")
if mibBuilder.loadTexts:
    crasNumDisabledAccounts.setUnits("Users")
_CrasThresholds_ObjectIdentity = ObjectIdentity
crasThresholds = _CrasThresholds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 6)
)


class _CrasThrMaxSessions_Type(Integer32):
    """Custom type crasThrMaxSessions based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CrasThrMaxSessions_Type.__name__ = "Integer32"
_CrasThrMaxSessions_Object = MibScalar
crasThrMaxSessions = _CrasThrMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 6, 1),
    _CrasThrMaxSessions_Type()
)
crasThrMaxSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasThrMaxSessions.setStatus("current")
if mibBuilder.loadTexts:
    crasThrMaxSessions.setUnits("Sessions")


class _CrasThrMaxFailedAuths_Type(Unsigned32):
    """Custom type crasThrMaxFailedAuths based on Unsigned32"""
    defaultValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CrasThrMaxFailedAuths_Type.__name__ = "Unsigned32"
_CrasThrMaxFailedAuths_Object = MibScalar
crasThrMaxFailedAuths = _CrasThrMaxFailedAuths_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 6, 2),
    _CrasThrMaxFailedAuths_Type()
)
crasThrMaxFailedAuths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasThrMaxFailedAuths.setStatus("current")


class _CrasThrMaxThroughput_Type(Integer32):
    """Custom type crasThrMaxThroughput based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CrasThrMaxThroughput_Type.__name__ = "Integer32"
_CrasThrMaxThroughput_Object = MibScalar
crasThrMaxThroughput = _CrasThrMaxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 6, 3),
    _CrasThrMaxThroughput_Type()
)
crasThrMaxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crasThrMaxThroughput.setStatus("current")
if mibBuilder.loadTexts:
    crasThrMaxThroughput.setUnits("Octets Per Second")
_CrasNotifCntl_ObjectIdentity = ObjectIdentity
crasNotifCntl = _CrasNotifCntl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 7)
)


class _CrasCntlTooManySessions_Type(TruthValue):
    """Custom type crasCntlTooManySessions based on TruthValue"""


_CrasCntlTooManySessions_Object = MibScalar
crasCntlTooManySessions = _CrasCntlTooManySessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 7, 1),
    _CrasCntlTooManySessions_Type()
)
crasCntlTooManySessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crasCntlTooManySessions.setStatus("current")


class _CrasCntlTooManyFailedAuths_Type(TruthValue):
    """Custom type crasCntlTooManyFailedAuths based on TruthValue"""


_CrasCntlTooManyFailedAuths_Object = MibScalar
crasCntlTooManyFailedAuths = _CrasCntlTooManyFailedAuths_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 7, 2),
    _CrasCntlTooManyFailedAuths_Type()
)
crasCntlTooManyFailedAuths.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crasCntlTooManyFailedAuths.setStatus("current")


class _CrasCntlTooHighThroughput_Type(TruthValue):
    """Custom type crasCntlTooHighThroughput based on TruthValue"""


_CrasCntlTooHighThroughput_Object = MibScalar
crasCntlTooHighThroughput = _CrasCntlTooHighThroughput_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 1, 7, 3),
    _CrasCntlTooHighThroughput_Type()
)
crasCntlTooHighThroughput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crasCntlTooHighThroughput.setStatus("current")
_CiscoRasMonitorMIBConform_ObjectIdentity = ObjectIdentity
ciscoRasMonitorMIBConform = _CiscoRasMonitorMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 2)
)
_CiscoRasMonitorMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoRasMonitorMIBCompliances = _CiscoRasMonitorMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 2, 1)
)
_CiscoRasMonitorMIBGroups_ObjectIdentity = ObjectIdentity
ciscoRasMonitorMIBGroups = _CiscoRasMonitorMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 2, 2)
)

# Managed Objects groups

ciscoRasCapacityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 2, 2, 1)
)
ciscoRasCapacityGroup.setObjects(
      *(("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasMaxSessionsSupportable"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasMaxUsersSupportable"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasMaxGroupsSupportable"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasNumCryptoAccelerators"))
)
if mibBuilder.loadTexts:
    ciscoRasCapacityGroup.setStatus("current")

ciscoRasResourceUsageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 2, 2, 2)
)
ciscoRasResourceUsageGroup.setObjects(
    ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasGlobalBwUsage")
)
if mibBuilder.loadTexts:
    ciscoRasResourceUsageGroup.setStatus("current")

ciscoRasActivityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 2, 2, 3)
)
ciscoRasActivityGroup.setObjects(
      *(("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasNumSessions"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasNumPrevSessions"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasNumUsers"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasGlobalInPkts"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasGlobalOutPkts"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasGlobalInOctets"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasGlobalOutOctets"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasGlobalInDecompOctets"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasGlobalOutUncompOctets"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasGlobalInDropPkts"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasGlobalOutDropPkts"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasGroup"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasAuthenMethod"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasAuthorMethod"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasSessionDuration"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasLocalAddressType"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasLocalAddress"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasISPAddressType"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasISPAddress"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasSessionProtocol"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasProtocolElement"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasSessionEncryptionAlgo"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasSessionPktAuthenAlgo"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasSessionCompressionAlgo"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasHeartbeatInterval"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasClientVendorString"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasClientVersionString"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasClientOSVendorString"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasClientOSVersionString"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasPrimWINSServerAddrType"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasPrimWINSServer"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasSecWINSServerAddrType"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasSecWINSServer"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasPrimDNSServerAddrType"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasPrimDNSServer"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasSecDNSServerAddrType"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasSecDNSServer"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasDHCPServerAddrType"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasDHCPServer"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasSessionInPkts"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasSessionOutPkts"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasSessionInDropPkts"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasSessionOutDropPkts"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasSessionInOctets"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasSessionOutOctets"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasSessionState"))
)
if mibBuilder.loadTexts:
    ciscoRasActivityGroup.setStatus("current")

ciscoRasGrpActivityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 2, 2, 4)
)
ciscoRasGrpActivityGroup.setObjects(
      *(("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasNumGroups"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasActGrNumUsers"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasActGrpInPkts"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasActGrpOutPkts"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasActGrpInDropPkts"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasActGrpOutDropPkts"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasActGrpInOctets"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasActGrpOutOctets"))
)
if mibBuilder.loadTexts:
    ciscoRasGrpActivityGroup.setStatus("current")

ciscoRasMandatoryFailureGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 2, 2, 5)
)
ciscoRasMandatoryFailureGroup.setObjects(
      *(("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasNumTotalFailures"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasNumDeclinedSessions"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasNumAbortedSessions"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasFailTableSize"))
)
if mibBuilder.loadTexts:
    ciscoRasMandatoryFailureGroup.setStatus("current")

ciscoRasOptionalFailureGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 2, 2, 6)
)
ciscoRasOptionalFailureGroup.setObjects(
      *(("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasNumSetupFailInsufResources"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasSessFailUsername"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasSessFailGroupname"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasSessFailType"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasSessFailReason"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasSessFailTime"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasSessFailSessionIndex"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasSessFailISPAddr"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasSessFailLocalAddr"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasSessFailISPAddrType"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasSessFailLocalAddrType"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasFailLastFailIndex"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasGrpFailNumFailAuths"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasGrpFailNumResourceFailures"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasGrpFailNumDeclined"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasGrpFailNumTerminatedMgmt"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasGrpFailNumTerminatedOther"))
)
if mibBuilder.loadTexts:
    ciscoRasOptionalFailureGroup.setStatus("current")

ciscoRasSecurityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 2, 2, 7)
)
ciscoRasSecurityGroup.setObjects(
    ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasNumDisabledAccounts")
)
if mibBuilder.loadTexts:
    ciscoRasSecurityGroup.setStatus("current")

ciscoRasThresholdsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 2, 2, 8)
)
ciscoRasThresholdsGroup.setObjects(
      *(("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasThrMaxSessions"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasThrMaxFailedAuths"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasThrMaxThroughput"))
)
if mibBuilder.loadTexts:
    ciscoRasThresholdsGroup.setStatus("current")

ciscoRasNotificationCntlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 2, 2, 9)
)
ciscoRasNotificationCntlGroup.setObjects(
      *(("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasCntlTooManySessions"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasCntlTooManyFailedAuths"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasCntlTooHighThroughput"))
)
if mibBuilder.loadTexts:
    ciscoRasNotificationCntlGroup.setStatus("current")

ciscoRasActivityGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 2, 2, 11)
)
ciscoRasActivityGroupRev1.setObjects(
      *(("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasEmailNumSessions"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasEmailCumulateSessions"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasEmailPeakConcurrentSessions"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasIPSecNumSessions"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasIPSecCumulateSessions"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasIPSecPeakConcurrentSessions"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasL2LNumSessions"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasL2LCumulateSessions"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasL2LPeakConcurrentSessions"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasLBNumSessions"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasLBCumulateSessions"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasLBPeakConcurrentSessions"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasSVCNumSessions"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasSVCCumulateSessions"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasSVCPeakConcurrentSessions"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasWebvpnNumSessions"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasWebvpnCumulateSessions"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasWebvpnPeakConcurrentSessions"))
)
if mibBuilder.loadTexts:
    ciscoRasActivityGroupRev1.setStatus("current")


# Notification objects

ciscoRasTooManySessions = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 0, 1)
)
ciscoRasTooManySessions.setObjects(
      *(("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasNumSessions"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasNumUsers"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasMaxSessionsSupportable"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasMaxUsersSupportable"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasThrMaxSessions"))
)
if mibBuilder.loadTexts:
    ciscoRasTooManySessions.setStatus(
        "current"
    )

ciscoRasTooManyFailedAuths = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 0, 2)
)
ciscoRasTooManyFailedAuths.setObjects(
      *(("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasNumDeclinedSessions"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasThrMaxFailedAuths"))
)
if mibBuilder.loadTexts:
    ciscoRasTooManyFailedAuths.setStatus(
        "current"
    )

ciscoRasTooHighThroughput = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 0, 3)
)
ciscoRasTooHighThroughput.setObjects(
      *(("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasGlobalInOctets"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasGlobalOutOctets"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "crasThrMaxThroughput"))
)
if mibBuilder.loadTexts:
    ciscoRasTooHighThroughput.setStatus(
        "current"
    )


# Notifications groups

ciscoRasNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 2, 2, 10)
)
ciscoRasNotificationsGroup.setObjects(
      *(("CISCO-REMOTE-ACCESS-MONITOR-MIB", "ciscoRasTooHighThroughput"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "ciscoRasTooManyFailedAuths"),
        ("CISCO-REMOTE-ACCESS-MONITOR-MIB", "ciscoRasTooManySessions"))
)
if mibBuilder.loadTexts:
    ciscoRasNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoRasMonitorMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoRasMonitorMIBCompliance.setStatus(
        "deprecated"
    )

ciscoRasMonitorMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 392, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoRasMonitorMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-REMOTE-ACCESS-MONITOR-MIB",
    **{"RasProtocol": RasProtocol,
       "UserAuthenMethod": UserAuthenMethod,
       "UserAuthorMethod": UserAuthorMethod,
       "SessionEncrAlgo": SessionEncrAlgo,
       "SessionAuthAlgo": SessionAuthAlgo,
       "SessionCompressionAlgo": SessionCompressionAlgo,
       "SessionStatus": SessionStatus,
       "SessionIndex": SessionIndex,
       "FailureRecordIndex": FailureRecordIndex,
       "ciscoRemoteAccessMonitorMIB": ciscoRemoteAccessMonitorMIB,
       "ciscoRasMonitorMIBNotifs": ciscoRasMonitorMIBNotifs,
       "ciscoRasTooManySessions": ciscoRasTooManySessions,
       "ciscoRasTooManyFailedAuths": ciscoRasTooManyFailedAuths,
       "ciscoRasTooHighThroughput": ciscoRasTooHighThroughput,
       "ciscoRasMonitorMIBObjects": ciscoRasMonitorMIBObjects,
       "crasCapacity": crasCapacity,
       "crasMaxSessionsSupportable": crasMaxSessionsSupportable,
       "crasMaxUsersSupportable": crasMaxUsersSupportable,
       "crasMaxGroupsSupportable": crasMaxGroupsSupportable,
       "crasNumCryptoAccelerators": crasNumCryptoAccelerators,
       "crasResourceUsage": crasResourceUsage,
       "crasGlobalBwUsage": crasGlobalBwUsage,
       "crasActivity": crasActivity,
       "crasNumSessions": crasNumSessions,
       "crasNumPrevSessions": crasNumPrevSessions,
       "crasNumUsers": crasNumUsers,
       "crasNumGroups": crasNumGroups,
       "crasGlobalInPkts": crasGlobalInPkts,
       "crasGlobalOutPkts": crasGlobalOutPkts,
       "crasGlobalInOctets": crasGlobalInOctets,
       "crasGlobalInDecompOctets": crasGlobalInDecompOctets,
       "crasGlobalOutOctets": crasGlobalOutOctets,
       "crasGlobalOutUncompOctets": crasGlobalOutUncompOctets,
       "crasGlobalInDropPkts": crasGlobalInDropPkts,
       "crasGlobalOutDropPkts": crasGlobalOutDropPkts,
       "crasSessionTable": crasSessionTable,
       "crasSessionEntry": crasSessionEntry,
       "crasUsername": crasUsername,
       "crasGroup": crasGroup,
       "crasSessionIndex": crasSessionIndex,
       "crasAuthenMethod": crasAuthenMethod,
       "crasAuthorMethod": crasAuthorMethod,
       "crasSessionDuration": crasSessionDuration,
       "crasLocalAddressType": crasLocalAddressType,
       "crasLocalAddress": crasLocalAddress,
       "crasISPAddressType": crasISPAddressType,
       "crasISPAddress": crasISPAddress,
       "crasSessionProtocol": crasSessionProtocol,
       "crasProtocolElement": crasProtocolElement,
       "crasSessionEncryptionAlgo": crasSessionEncryptionAlgo,
       "crasSessionPktAuthenAlgo": crasSessionPktAuthenAlgo,
       "crasSessionCompressionAlgo": crasSessionCompressionAlgo,
       "crasHeartbeatInterval": crasHeartbeatInterval,
       "crasClientVendorString": crasClientVendorString,
       "crasClientVersionString": crasClientVersionString,
       "crasClientOSVendorString": crasClientOSVendorString,
       "crasClientOSVersionString": crasClientOSVersionString,
       "crasPrimWINSServerAddrType": crasPrimWINSServerAddrType,
       "crasPrimWINSServer": crasPrimWINSServer,
       "crasSecWINSServerAddrType": crasSecWINSServerAddrType,
       "crasSecWINSServer": crasSecWINSServer,
       "crasPrimDNSServerAddrType": crasPrimDNSServerAddrType,
       "crasPrimDNSServer": crasPrimDNSServer,
       "crasSecDNSServerAddrType": crasSecDNSServerAddrType,
       "crasSecDNSServer": crasSecDNSServer,
       "crasDHCPServerAddrType": crasDHCPServerAddrType,
       "crasDHCPServer": crasDHCPServer,
       "crasSessionInPkts": crasSessionInPkts,
       "crasSessionOutPkts": crasSessionOutPkts,
       "crasSessionInDropPkts": crasSessionInDropPkts,
       "crasSessionOutDropPkts": crasSessionOutDropPkts,
       "crasSessionInOctets": crasSessionInOctets,
       "crasSessionOutOctets": crasSessionOutOctets,
       "crasSessionState": crasSessionState,
       "crasActGroupTable": crasActGroupTable,
       "crasActGroupEntry": crasActGroupEntry,
       "crasActGrpName": crasActGrpName,
       "crasActGrNumUsers": crasActGrNumUsers,
       "crasActGrpInPkts": crasActGrpInPkts,
       "crasActGrpOutPkts": crasActGrpOutPkts,
       "crasActGrpInDropPkts": crasActGrpInDropPkts,
       "crasActGrpOutDropPkts": crasActGrpOutDropPkts,
       "crasActGrpInOctets": crasActGrpInOctets,
       "crasActGrpOutOctets": crasActGrpOutOctets,
       "crasEmailNumSessions": crasEmailNumSessions,
       "crasEmailCumulateSessions": crasEmailCumulateSessions,
       "crasEmailPeakConcurrentSessions": crasEmailPeakConcurrentSessions,
       "crasIPSecNumSessions": crasIPSecNumSessions,
       "crasIPSecCumulateSessions": crasIPSecCumulateSessions,
       "crasIPSecPeakConcurrentSessions": crasIPSecPeakConcurrentSessions,
       "crasL2LNumSessions": crasL2LNumSessions,
       "crasL2LCumulateSessions": crasL2LCumulateSessions,
       "crasL2LPeakConcurrentSessions": crasL2LPeakConcurrentSessions,
       "crasLBNumSessions": crasLBNumSessions,
       "crasLBCumulateSessions": crasLBCumulateSessions,
       "crasLBPeakConcurrentSessions": crasLBPeakConcurrentSessions,
       "crasSVCNumSessions": crasSVCNumSessions,
       "crasSVCCumulateSessions": crasSVCCumulateSessions,
       "crasSVCPeakConcurrentSessions": crasSVCPeakConcurrentSessions,
       "crasWebvpnNumSessions": crasWebvpnNumSessions,
       "crasWebvpnCumulateSessions": crasWebvpnCumulateSessions,
       "crasWebvpnPeakConcurrentSessions": crasWebvpnPeakConcurrentSessions,
       "crasFailures": crasFailures,
       "crasFailuresGlobals": crasFailuresGlobals,
       "crasNumTotalFailures": crasNumTotalFailures,
       "crasNumDeclinedSessions": crasNumDeclinedSessions,
       "crasNumSetupFailInsufResources": crasNumSetupFailInsufResources,
       "crasNumAbortedSessions": crasNumAbortedSessions,
       "crasFailGlobalCntl": crasFailGlobalCntl,
       "crasFailTableSize": crasFailTableSize,
       "crasSessFailures": crasSessFailures,
       "crasSessFailTable": crasSessFailTable,
       "crasSessFailEntry": crasSessFailEntry,
       "crasSessFailIndex": crasSessFailIndex,
       "crasSessFailUsername": crasSessFailUsername,
       "crasSessFailGroupname": crasSessFailGroupname,
       "crasSessFailType": crasSessFailType,
       "crasSessFailReason": crasSessFailReason,
       "crasSessFailTime": crasSessFailTime,
       "crasSessFailSessionIndex": crasSessFailSessionIndex,
       "crasSessFailISPAddrType": crasSessFailISPAddrType,
       "crasSessFailISPAddr": crasSessFailISPAddr,
       "crasSessFailLocalAddrType": crasSessFailLocalAddrType,
       "crasSessFailLocalAddr": crasSessFailLocalAddr,
       "crasFailLastFailIndex": crasFailLastFailIndex,
       "crasGroupFailures": crasGroupFailures,
       "crasGrpFailTable": crasGrpFailTable,
       "crasGrpFailEntry": crasGrpFailEntry,
       "crasGrpFailGroupname": crasGrpFailGroupname,
       "crasGrpFailNumFailAuths": crasGrpFailNumFailAuths,
       "crasGrpFailNumResourceFailures": crasGrpFailNumResourceFailures,
       "crasGrpFailNumDeclined": crasGrpFailNumDeclined,
       "crasGrpFailNumTerminatedMgmt": crasGrpFailNumTerminatedMgmt,
       "crasGrpFailNumTerminatedOther": crasGrpFailNumTerminatedOther,
       "crasSecurity": crasSecurity,
       "crasSecurityGlobals": crasSecurityGlobals,
       "crasNumDisabledAccounts": crasNumDisabledAccounts,
       "crasThresholds": crasThresholds,
       "crasThrMaxSessions": crasThrMaxSessions,
       "crasThrMaxFailedAuths": crasThrMaxFailedAuths,
       "crasThrMaxThroughput": crasThrMaxThroughput,
       "crasNotifCntl": crasNotifCntl,
       "crasCntlTooManySessions": crasCntlTooManySessions,
       "crasCntlTooManyFailedAuths": crasCntlTooManyFailedAuths,
       "crasCntlTooHighThroughput": crasCntlTooHighThroughput,
       "ciscoRasMonitorMIBConform": ciscoRasMonitorMIBConform,
       "ciscoRasMonitorMIBCompliances": ciscoRasMonitorMIBCompliances,
       "ciscoRasMonitorMIBCompliance": ciscoRasMonitorMIBCompliance,
       "ciscoRasMonitorMIBComplianceRev1": ciscoRasMonitorMIBComplianceRev1,
       "ciscoRasMonitorMIBGroups": ciscoRasMonitorMIBGroups,
       "ciscoRasCapacityGroup": ciscoRasCapacityGroup,
       "ciscoRasResourceUsageGroup": ciscoRasResourceUsageGroup,
       "ciscoRasActivityGroup": ciscoRasActivityGroup,
       "ciscoRasGrpActivityGroup": ciscoRasGrpActivityGroup,
       "ciscoRasMandatoryFailureGroup": ciscoRasMandatoryFailureGroup,
       "ciscoRasOptionalFailureGroup": ciscoRasOptionalFailureGroup,
       "ciscoRasSecurityGroup": ciscoRasSecurityGroup,
       "ciscoRasThresholdsGroup": ciscoRasThresholdsGroup,
       "ciscoRasNotificationCntlGroup": ciscoRasNotificationCntlGroup,
       "ciscoRasNotificationsGroup": ciscoRasNotificationsGroup,
       "ciscoRasActivityGroupRev1": ciscoRasActivityGroupRev1}
)
