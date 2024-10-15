# SNMP MIB module (HP-ICF-DHCPV4-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-DHCPV4-SERVER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:57:19 2024
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

(VidList,) = mibBuilder.importSymbols(
    "HP-ICF-FTRCO",
    "VidList")

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

(ifName,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifName")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpicfDhcpv4ServerMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99)
)
hpicfDhcpv4ServerMIB.setRevisions(
        ("2015-10-15 00:00",
         "2015-01-28 00:00",
         "2014-03-07 00:00",
         "2013-04-05 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class InetAddressIPv4(OctetString, TextualConvention):
    status = "current"
    displayHint = "1d.1d.1d.1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )



# MIB Managed Objects in the order of their OIDs

_HpicfDhcpv4ServerNotifs_ObjectIdentity = ObjectIdentity
hpicfDhcpv4ServerNotifs = _HpicfDhcpv4ServerNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 0)
)
_HpicfDhcpv4ServerNotifyDuplicateIpAddr_Type = InetAddressIPv4
_HpicfDhcpv4ServerNotifyDuplicateIpAddr_Object = MibScalar
hpicfDhcpv4ServerNotifyDuplicateIpAddr = _HpicfDhcpv4ServerNotifyDuplicateIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 0, 1),
    _HpicfDhcpv4ServerNotifyDuplicateIpAddr_Type()
)
hpicfDhcpv4ServerNotifyDuplicateIpAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfDhcpv4ServerNotifyDuplicateIpAddr.setStatus("current")
_HpicfDhcpv4ServerNotifyDuplicateMac_Type = MacAddress
_HpicfDhcpv4ServerNotifyDuplicateMac_Object = MibScalar
hpicfDhcpv4ServerNotifyDuplicateMac = _HpicfDhcpv4ServerNotifyDuplicateMac_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 0, 2),
    _HpicfDhcpv4ServerNotifyDuplicateMac_Type()
)
hpicfDhcpv4ServerNotifyDuplicateMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfDhcpv4ServerNotifyDuplicateMac.setStatus("current")


class _HpicfDhcpv4ServerNotifyClientOrServerDetected_Type(Integer32):
    """Custom type hpicfDhcpv4ServerNotifyClientOrServerDetected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("client", 1),
          ("server", 2))
    )


_HpicfDhcpv4ServerNotifyClientOrServerDetected_Type.__name__ = "Integer32"
_HpicfDhcpv4ServerNotifyClientOrServerDetected_Object = MibScalar
hpicfDhcpv4ServerNotifyClientOrServerDetected = _HpicfDhcpv4ServerNotifyClientOrServerDetected_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 0, 3),
    _HpicfDhcpv4ServerNotifyClientOrServerDetected_Type()
)
hpicfDhcpv4ServerNotifyClientOrServerDetected.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfDhcpv4ServerNotifyClientOrServerDetected.setStatus("current")
_HpicfDhcpv4ServerClientPhysicalAddress_Type = MacAddress
_HpicfDhcpv4ServerClientPhysicalAddress_Object = MibScalar
hpicfDhcpv4ServerClientPhysicalAddress = _HpicfDhcpv4ServerClientPhysicalAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 0, 4),
    _HpicfDhcpv4ServerClientPhysicalAddress_Type()
)
hpicfDhcpv4ServerClientPhysicalAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfDhcpv4ServerClientPhysicalAddress.setStatus("current")
_HpicfDhcpv4ServerObjects_ObjectIdentity = ObjectIdentity
hpicfDhcpv4ServerObjects = _HpicfDhcpv4ServerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1)
)
_HpicfDhcpv4LeaseDataBase_ObjectIdentity = ObjectIdentity
hpicfDhcpv4LeaseDataBase = _HpicfDhcpv4LeaseDataBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 1)
)


class _HpicfDhcpv4ServerDBFile_Type(SnmpAdminString):
    """Custom type hpicfDhcpv4ServerDBFile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpicfDhcpv4ServerDBFile_Type.__name__ = "SnmpAdminString"
_HpicfDhcpv4ServerDBFile_Object = MibScalar
hpicfDhcpv4ServerDBFile = _HpicfDhcpv4ServerDBFile_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 1, 1),
    _HpicfDhcpv4ServerDBFile_Type()
)
hpicfDhcpv4ServerDBFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDhcpv4ServerDBFile.setStatus("current")


class _HpicfDhcpv4ServerDBWriteDelay_Type(Unsigned32):
    """Custom type hpicfDhcpv4ServerDBWriteDelay based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 86400),
    )


_HpicfDhcpv4ServerDBWriteDelay_Type.__name__ = "Unsigned32"
_HpicfDhcpv4ServerDBWriteDelay_Object = MibScalar
hpicfDhcpv4ServerDBWriteDelay = _HpicfDhcpv4ServerDBWriteDelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 1, 2),
    _HpicfDhcpv4ServerDBWriteDelay_Type()
)
hpicfDhcpv4ServerDBWriteDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDhcpv4ServerDBWriteDelay.setStatus("current")
if mibBuilder.loadTexts:
    hpicfDhcpv4ServerDBWriteDelay.setUnits("seconds")


class _HpicfDhcpv4ServerDBWriteTimeout_Type(Unsigned32):
    """Custom type hpicfDhcpv4ServerDBWriteTimeout based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_HpicfDhcpv4ServerDBWriteTimeout_Type.__name__ = "Unsigned32"
_HpicfDhcpv4ServerDBWriteTimeout_Object = MibScalar
hpicfDhcpv4ServerDBWriteTimeout = _HpicfDhcpv4ServerDBWriteTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 1, 3),
    _HpicfDhcpv4ServerDBWriteTimeout_Type()
)
hpicfDhcpv4ServerDBWriteTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDhcpv4ServerDBWriteTimeout.setStatus("current")
if mibBuilder.loadTexts:
    hpicfDhcpv4ServerDBWriteTimeout.setUnits("seconds")
_HpicfDhcpServerDBFileWriteAttempts_Type = Counter32
_HpicfDhcpServerDBFileWriteAttempts_Object = MibScalar
hpicfDhcpServerDBFileWriteAttempts = _HpicfDhcpServerDBFileWriteAttempts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 1, 4),
    _HpicfDhcpServerDBFileWriteAttempts_Type()
)
hpicfDhcpServerDBFileWriteAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpServerDBFileWriteAttempts.setStatus("current")
_HpicfDhcpServerDBFileWriteFailures_Type = Counter32
_HpicfDhcpServerDBFileWriteFailures_Object = MibScalar
hpicfDhcpServerDBFileWriteFailures = _HpicfDhcpServerDBFileWriteFailures_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 1, 5),
    _HpicfDhcpServerDBFileWriteFailures_Type()
)
hpicfDhcpServerDBFileWriteFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpServerDBFileWriteFailures.setStatus("current")


class _HpicfDhcpServerDBFileReadStatus_Type(Integer32):
    """Custom type hpicfDhcpServerDBFileReadStatus based on Integer32"""
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
        *(("failed", 4),
          ("inProgress", 2),
          ("notConfigured", 1),
          ("succeeded", 3))
    )


_HpicfDhcpServerDBFileReadStatus_Type.__name__ = "Integer32"
_HpicfDhcpServerDBFileReadStatus_Object = MibScalar
hpicfDhcpServerDBFileReadStatus = _HpicfDhcpServerDBFileReadStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 1, 6),
    _HpicfDhcpServerDBFileReadStatus_Type()
)
hpicfDhcpServerDBFileReadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpServerDBFileReadStatus.setStatus("current")


class _HpicfDhcpServerDBFileWriteStatus_Type(Integer32):
    """Custom type hpicfDhcpServerDBFileWriteStatus based on Integer32"""
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
        *(("delaying", 2),
          ("failed", 5),
          ("inProgress", 3),
          ("notConfigured", 1),
          ("succeeded", 4))
    )


_HpicfDhcpServerDBFileWriteStatus_Type.__name__ = "Integer32"
_HpicfDhcpServerDBFileWriteStatus_Object = MibScalar
hpicfDhcpServerDBFileWriteStatus = _HpicfDhcpServerDBFileWriteStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 1, 7),
    _HpicfDhcpServerDBFileWriteStatus_Type()
)
hpicfDhcpServerDBFileWriteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpServerDBFileWriteStatus.setStatus("current")
_HpicfDhcpServerDBFileLastWriteTime_Type = DateAndTime
_HpicfDhcpServerDBFileLastWriteTime_Object = MibScalar
hpicfDhcpServerDBFileLastWriteTime = _HpicfDhcpServerDBFileLastWriteTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 1, 8),
    _HpicfDhcpServerDBFileLastWriteTime_Type()
)
hpicfDhcpServerDBFileLastWriteTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpServerDBFileLastWriteTime.setStatus("current")


class _HpicfDhcpv4ServerDBFTPort_Type(Unsigned32):
    """Custom type hpicfDhcpv4ServerDBFTPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpicfDhcpv4ServerDBFTPort_Type.__name__ = "Unsigned32"
_HpicfDhcpv4ServerDBFTPort_Object = MibScalar
hpicfDhcpv4ServerDBFTPort = _HpicfDhcpv4ServerDBFTPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 1, 9),
    _HpicfDhcpv4ServerDBFTPort_Type()
)
hpicfDhcpv4ServerDBFTPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDhcpv4ServerDBFTPort.setStatus("current")


class _HpicfDhcpv4ServerDBSFTPUsername_Type(SnmpAdminString):
    """Custom type hpicfDhcpv4ServerDBSFTPUsername based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpicfDhcpv4ServerDBSFTPUsername_Type.__name__ = "SnmpAdminString"
_HpicfDhcpv4ServerDBSFTPUsername_Object = MibScalar
hpicfDhcpv4ServerDBSFTPUsername = _HpicfDhcpv4ServerDBSFTPUsername_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 1, 10),
    _HpicfDhcpv4ServerDBSFTPUsername_Type()
)
hpicfDhcpv4ServerDBSFTPUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDhcpv4ServerDBSFTPUsername.setStatus("current")


class _HpicfDhcpv4ServerDBSFTPPassword_Type(SnmpAdminString):
    """Custom type hpicfDhcpv4ServerDBSFTPPassword based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpicfDhcpv4ServerDBSFTPPassword_Type.__name__ = "SnmpAdminString"
_HpicfDhcpv4ServerDBSFTPPassword_Object = MibScalar
hpicfDhcpv4ServerDBSFTPPassword = _HpicfDhcpv4ServerDBSFTPPassword_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 1, 11),
    _HpicfDhcpv4ServerDBSFTPPassword_Type()
)
hpicfDhcpv4ServerDBSFTPPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDhcpv4ServerDBSFTPPassword.setStatus("current")


class _HpicfDhcpv4ServerDBValidateSFTPServer_Type(Integer32):
    """Custom type hpicfDhcpv4ServerDBValidateSFTPServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_HpicfDhcpv4ServerDBValidateSFTPServer_Type.__name__ = "Integer32"
_HpicfDhcpv4ServerDBValidateSFTPServer_Object = MibScalar
hpicfDhcpv4ServerDBValidateSFTPServer = _HpicfDhcpv4ServerDBValidateSFTPServer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 1, 12),
    _HpicfDhcpv4ServerDBValidateSFTPServer_Type()
)
hpicfDhcpv4ServerDBValidateSFTPServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDhcpv4ServerDBValidateSFTPServer.setStatus("current")
_HpicfDhcpv4BootpCounters_ObjectIdentity = ObjectIdentity
hpicfDhcpv4BootpCounters = _HpicfDhcpv4BootpCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 2)
)
_HpicfBootpCountRequests_Type = Counter32
_HpicfBootpCountRequests_Object = MibScalar
hpicfBootpCountRequests = _HpicfBootpCountRequests_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 2, 1),
    _HpicfBootpCountRequests_Type()
)
hpicfBootpCountRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfBootpCountRequests.setStatus("current")
_HpicfBootpCountReplies_Type = Counter32
_HpicfBootpCountReplies_Object = MibScalar
hpicfBootpCountReplies = _HpicfBootpCountReplies_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 2, 2),
    _HpicfBootpCountReplies_Type()
)
hpicfBootpCountReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfBootpCountReplies.setStatus("current")
_HpicfDhcpv4Counters_ObjectIdentity = ObjectIdentity
hpicfDhcpv4Counters = _HpicfDhcpv4Counters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 3)
)
_HpicfDhcpv4CountDiscovers_Type = Counter32
_HpicfDhcpv4CountDiscovers_Object = MibScalar
hpicfDhcpv4CountDiscovers = _HpicfDhcpv4CountDiscovers_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 3, 1),
    _HpicfDhcpv4CountDiscovers_Type()
)
hpicfDhcpv4CountDiscovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpv4CountDiscovers.setStatus("current")
_HpicfDhcpv4CountOffers_Type = Counter32
_HpicfDhcpv4CountOffers_Object = MibScalar
hpicfDhcpv4CountOffers = _HpicfDhcpv4CountOffers_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 3, 2),
    _HpicfDhcpv4CountOffers_Type()
)
hpicfDhcpv4CountOffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpv4CountOffers.setStatus("current")
_HpicfDhcpv4CountRequests_Type = Counter32
_HpicfDhcpv4CountRequests_Object = MibScalar
hpicfDhcpv4CountRequests = _HpicfDhcpv4CountRequests_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 3, 3),
    _HpicfDhcpv4CountRequests_Type()
)
hpicfDhcpv4CountRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpv4CountRequests.setStatus("current")
_HpicfDhcpv4CountDeclines_Type = Counter32
_HpicfDhcpv4CountDeclines_Object = MibScalar
hpicfDhcpv4CountDeclines = _HpicfDhcpv4CountDeclines_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 3, 4),
    _HpicfDhcpv4CountDeclines_Type()
)
hpicfDhcpv4CountDeclines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpv4CountDeclines.setStatus("current")
_HpicfDhcpv4CountAcks_Type = Counter32
_HpicfDhcpv4CountAcks_Object = MibScalar
hpicfDhcpv4CountAcks = _HpicfDhcpv4CountAcks_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 3, 5),
    _HpicfDhcpv4CountAcks_Type()
)
hpicfDhcpv4CountAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpv4CountAcks.setStatus("current")
_HpicfDhcpv4CountNaks_Type = Counter32
_HpicfDhcpv4CountNaks_Object = MibScalar
hpicfDhcpv4CountNaks = _HpicfDhcpv4CountNaks_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 3, 6),
    _HpicfDhcpv4CountNaks_Type()
)
hpicfDhcpv4CountNaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpv4CountNaks.setStatus("current")
_HpicfDhcpv4CountReleases_Type = Counter32
_HpicfDhcpv4CountReleases_Object = MibScalar
hpicfDhcpv4CountReleases = _HpicfDhcpv4CountReleases_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 3, 7),
    _HpicfDhcpv4CountReleases_Type()
)
hpicfDhcpv4CountReleases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpv4CountReleases.setStatus("current")
_HpicfDhcpv4CountInforms_Type = Counter32
_HpicfDhcpv4CountInforms_Object = MibScalar
hpicfDhcpv4CountInforms = _HpicfDhcpv4CountInforms_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 3, 8),
    _HpicfDhcpv4CountInforms_Type()
)
hpicfDhcpv4CountInforms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpv4CountInforms.setStatus("current")
_HpicfDhcpv4CountBadMsgs_Type = Counter32
_HpicfDhcpv4CountBadMsgs_Object = MibScalar
hpicfDhcpv4CountBadMsgs = _HpicfDhcpv4CountBadMsgs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 3, 9),
    _HpicfDhcpv4CountBadMsgs_Type()
)
hpicfDhcpv4CountBadMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpv4CountBadMsgs.setStatus("current")
_HpicfDhcpv4CountPools_Type = Counter32
_HpicfDhcpv4CountPools_Object = MibScalar
hpicfDhcpv4CountPools = _HpicfDhcpv4CountPools_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 3, 10),
    _HpicfDhcpv4CountPools_Type()
)
hpicfDhcpv4CountPools.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpv4CountPools.setStatus("current")
_HpicfDhcpv4CountAutoBindings_Type = Counter32
_HpicfDhcpv4CountAutoBindings_Object = MibScalar
hpicfDhcpv4CountAutoBindings = _HpicfDhcpv4CountAutoBindings_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 3, 11),
    _HpicfDhcpv4CountAutoBindings_Type()
)
hpicfDhcpv4CountAutoBindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpv4CountAutoBindings.setStatus("current")
_HpicfDhcpv4CountStaticBindings_Type = Counter32
_HpicfDhcpv4CountStaticBindings_Object = MibScalar
hpicfDhcpv4CountStaticBindings = _HpicfDhcpv4CountStaticBindings_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 3, 12),
    _HpicfDhcpv4CountStaticBindings_Type()
)
hpicfDhcpv4CountStaticBindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpv4CountStaticBindings.setStatus("current")
_HpicfDhcpv4CountExpiredOrFreeBindings_Type = Counter32
_HpicfDhcpv4CountExpiredOrFreeBindings_Object = MibScalar
hpicfDhcpv4CountExpiredOrFreeBindings = _HpicfDhcpv4CountExpiredOrFreeBindings_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 3, 13),
    _HpicfDhcpv4CountExpiredOrFreeBindings_Type()
)
hpicfDhcpv4CountExpiredOrFreeBindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpv4CountExpiredOrFreeBindings.setStatus("current")
_HpicfDhcpv4IpPool_ObjectIdentity = ObjectIdentity
hpicfDhcpv4IpPool = _HpicfDhcpv4IpPool_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 4)
)
_HpicfDhcpv4ServerPoolTable_Object = MibTable
hpicfDhcpv4ServerPoolTable = _HpicfDhcpv4ServerPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 4, 1)
)
if mibBuilder.loadTexts:
    hpicfDhcpv4ServerPoolTable.setStatus("current")
_HpicfDhcpv4ServerPoolEntry_Object = MibTableRow
hpicfDhcpv4ServerPoolEntry = _HpicfDhcpv4ServerPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 4, 1, 1)
)
hpicfDhcpv4ServerPoolEntry.setIndexNames(
    (0, "HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4ServerPoolName"),
)
if mibBuilder.loadTexts:
    hpicfDhcpv4ServerPoolEntry.setStatus("current")


class _HpicfDhcpv4ServerPoolName_Type(DisplayString):
    """Custom type hpicfDhcpv4ServerPoolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpicfDhcpv4ServerPoolName_Type.__name__ = "DisplayString"
_HpicfDhcpv4ServerPoolName_Object = MibTableColumn
hpicfDhcpv4ServerPoolName = _HpicfDhcpv4ServerPoolName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 4, 1, 1, 1),
    _HpicfDhcpv4ServerPoolName_Type()
)
hpicfDhcpv4ServerPoolName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfDhcpv4ServerPoolName.setStatus("current")
_HpicfDhcpv4ServerPoolNetworkAddress_Type = InetAddressIPv4
_HpicfDhcpv4ServerPoolNetworkAddress_Object = MibTableColumn
hpicfDhcpv4ServerPoolNetworkAddress = _HpicfDhcpv4ServerPoolNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 4, 1, 1, 2),
    _HpicfDhcpv4ServerPoolNetworkAddress_Type()
)
hpicfDhcpv4ServerPoolNetworkAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfDhcpv4ServerPoolNetworkAddress.setStatus("current")
_HpicfDhcpv4ServerPoolNetworkAddressMask_Type = InetAddressIPv4
_HpicfDhcpv4ServerPoolNetworkAddressMask_Object = MibTableColumn
hpicfDhcpv4ServerPoolNetworkAddressMask = _HpicfDhcpv4ServerPoolNetworkAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 4, 1, 1, 3),
    _HpicfDhcpv4ServerPoolNetworkAddressMask_Type()
)
hpicfDhcpv4ServerPoolNetworkAddressMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfDhcpv4ServerPoolNetworkAddressMask.setStatus("current")


class _HpicfDhcpv4ServerPoolDomainName_Type(DisplayString):
    """Custom type hpicfDhcpv4ServerPoolDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpicfDhcpv4ServerPoolDomainName_Type.__name__ = "DisplayString"
_HpicfDhcpv4ServerPoolDomainName_Object = MibTableColumn
hpicfDhcpv4ServerPoolDomainName = _HpicfDhcpv4ServerPoolDomainName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 4, 1, 1, 4),
    _HpicfDhcpv4ServerPoolDomainName_Type()
)
hpicfDhcpv4ServerPoolDomainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfDhcpv4ServerPoolDomainName.setStatus("current")


class _HpicfDhcpv4ServerPoolNetBIOSNodeType_Type(Integer32):
    """Custom type hpicfDhcpv4ServerPoolNetBIOSNodeType based on Integer32"""
    defaultValue = 0

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
        *(("broadcast", 1),
          ("hybrid", 4),
          ("mixed", 3),
          ("none", 0),
          ("peerTopeer", 2))
    )


_HpicfDhcpv4ServerPoolNetBIOSNodeType_Type.__name__ = "Integer32"
_HpicfDhcpv4ServerPoolNetBIOSNodeType_Object = MibTableColumn
hpicfDhcpv4ServerPoolNetBIOSNodeType = _HpicfDhcpv4ServerPoolNetBIOSNodeType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 4, 1, 1, 5),
    _HpicfDhcpv4ServerPoolNetBIOSNodeType_Type()
)
hpicfDhcpv4ServerPoolNetBIOSNodeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfDhcpv4ServerPoolNetBIOSNodeType.setStatus("current")


class _HpicfDhcpv4ServerPoolLeaseTime_Type(Unsigned32):
    """Custom type hpicfDhcpv4ServerPoolLeaseTime based on Unsigned32"""
    defaultValue = 86400


_HpicfDhcpv4ServerPoolLeaseTime_Object = MibTableColumn
hpicfDhcpv4ServerPoolLeaseTime = _HpicfDhcpv4ServerPoolLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 4, 1, 1, 6),
    _HpicfDhcpv4ServerPoolLeaseTime_Type()
)
hpicfDhcpv4ServerPoolLeaseTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfDhcpv4ServerPoolLeaseTime.setStatus("current")
if mibBuilder.loadTexts:
    hpicfDhcpv4ServerPoolLeaseTime.setUnits("seconds")


class _HpicfDhcpv4ServerPoolBootFile_Type(DisplayString):
    """Custom type hpicfDhcpv4ServerPoolBootFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HpicfDhcpv4ServerPoolBootFile_Type.__name__ = "DisplayString"
_HpicfDhcpv4ServerPoolBootFile_Object = MibTableColumn
hpicfDhcpv4ServerPoolBootFile = _HpicfDhcpv4ServerPoolBootFile_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 4, 1, 1, 7),
    _HpicfDhcpv4ServerPoolBootFile_Type()
)
hpicfDhcpv4ServerPoolBootFile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfDhcpv4ServerPoolBootFile.setStatus("current")
_HpicfDhcpv4ServerPoolLowThreshold_Type = Unsigned32
_HpicfDhcpv4ServerPoolLowThreshold_Object = MibTableColumn
hpicfDhcpv4ServerPoolLowThreshold = _HpicfDhcpv4ServerPoolLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 4, 1, 1, 8),
    _HpicfDhcpv4ServerPoolLowThreshold_Type()
)
hpicfDhcpv4ServerPoolLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpv4ServerPoolLowThreshold.setStatus("current")
_HpicfDhcpv4ServerPoolHighThreshold_Type = Unsigned32
_HpicfDhcpv4ServerPoolHighThreshold_Object = MibTableColumn
hpicfDhcpv4ServerPoolHighThreshold = _HpicfDhcpv4ServerPoolHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 4, 1, 1, 9),
    _HpicfDhcpv4ServerPoolHighThreshold_Type()
)
hpicfDhcpv4ServerPoolHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpv4ServerPoolHighThreshold.setStatus("current")
_HpicfDhcpv4ServerPoolFreeAddresses_Type = Unsigned32
_HpicfDhcpv4ServerPoolFreeAddresses_Object = MibTableColumn
hpicfDhcpv4ServerPoolFreeAddresses = _HpicfDhcpv4ServerPoolFreeAddresses_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 4, 1, 1, 10),
    _HpicfDhcpv4ServerPoolFreeAddresses_Type()
)
hpicfDhcpv4ServerPoolFreeAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpv4ServerPoolFreeAddresses.setStatus("current")


class _HpicfDhcpv4ServerDNSServerAddress_Type(DisplayString):
    """Custom type hpicfDhcpv4ServerDNSServerAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HpicfDhcpv4ServerDNSServerAddress_Type.__name__ = "DisplayString"
_HpicfDhcpv4ServerDNSServerAddress_Object = MibTableColumn
hpicfDhcpv4ServerDNSServerAddress = _HpicfDhcpv4ServerDNSServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 4, 1, 1, 11),
    _HpicfDhcpv4ServerDNSServerAddress_Type()
)
hpicfDhcpv4ServerDNSServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfDhcpv4ServerDNSServerAddress.setStatus("current")


class _HpicfDhcpv4ServerNetBIOSNameServer_Type(DisplayString):
    """Custom type hpicfDhcpv4ServerNetBIOSNameServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HpicfDhcpv4ServerNetBIOSNameServer_Type.__name__ = "DisplayString"
_HpicfDhcpv4ServerNetBIOSNameServer_Object = MibTableColumn
hpicfDhcpv4ServerNetBIOSNameServer = _HpicfDhcpv4ServerNetBIOSNameServer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 4, 1, 1, 12),
    _HpicfDhcpv4ServerNetBIOSNameServer_Type()
)
hpicfDhcpv4ServerNetBIOSNameServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDhcpv4ServerNetBIOSNameServer.setStatus("current")


class _HpicfDhcpv4ServerDefaultRouter_Type(DisplayString):
    """Custom type hpicfDhcpv4ServerDefaultRouter based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HpicfDhcpv4ServerDefaultRouter_Type.__name__ = "DisplayString"
_HpicfDhcpv4ServerDefaultRouter_Object = MibTableColumn
hpicfDhcpv4ServerDefaultRouter = _HpicfDhcpv4ServerDefaultRouter_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 4, 1, 1, 13),
    _HpicfDhcpv4ServerDefaultRouter_Type()
)
hpicfDhcpv4ServerDefaultRouter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfDhcpv4ServerDefaultRouter.setStatus("current")


class _HpicfDhcpv4ServerTFTPServerName_Type(DisplayString):
    """Custom type hpicfDhcpv4ServerTFTPServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpicfDhcpv4ServerTFTPServerName_Type.__name__ = "DisplayString"
_HpicfDhcpv4ServerTFTPServerName_Object = MibTableColumn
hpicfDhcpv4ServerTFTPServerName = _HpicfDhcpv4ServerTFTPServerName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 4, 1, 1, 14),
    _HpicfDhcpv4ServerTFTPServerName_Type()
)
hpicfDhcpv4ServerTFTPServerName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfDhcpv4ServerTFTPServerName.setStatus("current")
_HpicfDhcpv4ServerTFTPServerIpAddress_Type = InetAddressIPv4
_HpicfDhcpv4ServerTFTPServerIpAddress_Object = MibTableColumn
hpicfDhcpv4ServerTFTPServerIpAddress = _HpicfDhcpv4ServerTFTPServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 4, 1, 1, 15),
    _HpicfDhcpv4ServerTFTPServerIpAddress_Type()
)
hpicfDhcpv4ServerTFTPServerIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfDhcpv4ServerTFTPServerIpAddress.setStatus("current")
_HpicfDhcpv4ServerStaticIpAddress_Type = InetAddressIPv4
_HpicfDhcpv4ServerStaticIpAddress_Object = MibTableColumn
hpicfDhcpv4ServerStaticIpAddress = _HpicfDhcpv4ServerStaticIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 4, 1, 1, 16),
    _HpicfDhcpv4ServerStaticIpAddress_Type()
)
hpicfDhcpv4ServerStaticIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfDhcpv4ServerStaticIpAddress.setStatus("current")
_HpicfDhcpv4ServerStaticIpAddressMask_Type = InetAddressIPv4
_HpicfDhcpv4ServerStaticIpAddressMask_Object = MibTableColumn
hpicfDhcpv4ServerStaticIpAddressMask = _HpicfDhcpv4ServerStaticIpAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 4, 1, 1, 17),
    _HpicfDhcpv4ServerStaticIpAddressMask_Type()
)
hpicfDhcpv4ServerStaticIpAddressMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfDhcpv4ServerStaticIpAddressMask.setStatus("current")
_HpicfDhcpv4ServerStaticHardwareAddress_Type = MacAddress
_HpicfDhcpv4ServerStaticHardwareAddress_Object = MibTableColumn
hpicfDhcpv4ServerStaticHardwareAddress = _HpicfDhcpv4ServerStaticHardwareAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 4, 1, 1, 18),
    _HpicfDhcpv4ServerStaticHardwareAddress_Type()
)
hpicfDhcpv4ServerStaticHardwareAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfDhcpv4ServerStaticHardwareAddress.setStatus("current")
_HpicfDhcpv4ServerPoolIsAuthoritative_Type = TruthValue
_HpicfDhcpv4ServerPoolIsAuthoritative_Object = MibTableColumn
hpicfDhcpv4ServerPoolIsAuthoritative = _HpicfDhcpv4ServerPoolIsAuthoritative_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 4, 1, 1, 19),
    _HpicfDhcpv4ServerPoolIsAuthoritative_Type()
)
hpicfDhcpv4ServerPoolIsAuthoritative.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfDhcpv4ServerPoolIsAuthoritative.setStatus("current")
_HpicfDhcpv4ServerPoolStatus_Type = RowStatus
_HpicfDhcpv4ServerPoolStatus_Object = MibTableColumn
hpicfDhcpv4ServerPoolStatus = _HpicfDhcpv4ServerPoolStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 4, 1, 1, 20),
    _HpicfDhcpv4ServerPoolStatus_Type()
)
hpicfDhcpv4ServerPoolStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfDhcpv4ServerPoolStatus.setStatus("current")
_HpicfDhcpv4PoolIpRange_ObjectIdentity = ObjectIdentity
hpicfDhcpv4PoolIpRange = _HpicfDhcpv4PoolIpRange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 5)
)
_HpicfDhcpv4ServerRangeTable_Object = MibTable
hpicfDhcpv4ServerRangeTable = _HpicfDhcpv4ServerRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 5, 1)
)
if mibBuilder.loadTexts:
    hpicfDhcpv4ServerRangeTable.setStatus("current")
_HpicfDhcpv4ServerRangeEntry_Object = MibTableRow
hpicfDhcpv4ServerRangeEntry = _HpicfDhcpv4ServerRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 5, 1, 1)
)
hpicfDhcpv4ServerRangeEntry.setIndexNames(
    (0, "HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4ServerPoolName"),
    (0, "HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4ServerRangeStartAddress"),
)
if mibBuilder.loadTexts:
    hpicfDhcpv4ServerRangeEntry.setStatus("current")
_HpicfDhcpv4ServerRangeStartAddress_Type = InetAddressIPv4
_HpicfDhcpv4ServerRangeStartAddress_Object = MibTableColumn
hpicfDhcpv4ServerRangeStartAddress = _HpicfDhcpv4ServerRangeStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 5, 1, 1, 1),
    _HpicfDhcpv4ServerRangeStartAddress_Type()
)
hpicfDhcpv4ServerRangeStartAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfDhcpv4ServerRangeStartAddress.setStatus("current")
_HpicfDhcpv4ServerRangeEndAddress_Type = InetAddressIPv4
_HpicfDhcpv4ServerRangeEndAddress_Object = MibTableColumn
hpicfDhcpv4ServerRangeEndAddress = _HpicfDhcpv4ServerRangeEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 5, 1, 1, 2),
    _HpicfDhcpv4ServerRangeEndAddress_Type()
)
hpicfDhcpv4ServerRangeEndAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfDhcpv4ServerRangeEndAddress.setStatus("current")
_HpicfDhcpv4ServerRangeStatus_Type = RowStatus
_HpicfDhcpv4ServerRangeStatus_Object = MibTableColumn
hpicfDhcpv4ServerRangeStatus = _HpicfDhcpv4ServerRangeStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 5, 1, 1, 3),
    _HpicfDhcpv4ServerRangeStatus_Type()
)
hpicfDhcpv4ServerRangeStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfDhcpv4ServerRangeStatus.setStatus("current")
_HpicfDhcpv4PoolOption_ObjectIdentity = ObjectIdentity
hpicfDhcpv4PoolOption = _HpicfDhcpv4PoolOption_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 6)
)
_HpicfDhcpv4ServerPoolOptionTable_Object = MibTable
hpicfDhcpv4ServerPoolOptionTable = _HpicfDhcpv4ServerPoolOptionTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 6, 1)
)
if mibBuilder.loadTexts:
    hpicfDhcpv4ServerPoolOptionTable.setStatus("current")
_HpicfDhcpv4ServerPoolOptionEntry_Object = MibTableRow
hpicfDhcpv4ServerPoolOptionEntry = _HpicfDhcpv4ServerPoolOptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 6, 1, 1)
)
hpicfDhcpv4ServerPoolOptionEntry.setIndexNames(
    (0, "HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4ServerPoolName"),
    (0, "HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4ServerPoolOptionCode"),
)
if mibBuilder.loadTexts:
    hpicfDhcpv4ServerPoolOptionEntry.setStatus("current")


class _HpicfDhcpv4ServerPoolOptionCode_Type(Unsigned32):
    """Custom type hpicfDhcpv4ServerPoolOptionCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 254),
    )


_HpicfDhcpv4ServerPoolOptionCode_Type.__name__ = "Unsigned32"
_HpicfDhcpv4ServerPoolOptionCode_Object = MibTableColumn
hpicfDhcpv4ServerPoolOptionCode = _HpicfDhcpv4ServerPoolOptionCode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 6, 1, 1, 1),
    _HpicfDhcpv4ServerPoolOptionCode_Type()
)
hpicfDhcpv4ServerPoolOptionCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfDhcpv4ServerPoolOptionCode.setStatus("current")


class _HpicfDhcpv4ServerPoolOptionType_Type(Integer32):
    """Custom type hpicfDhcpv4ServerPoolOptionType based on Integer32"""
    defaultValue = 0

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
        *(("asciiString", 2),
          ("hexString", 1),
          ("ipAddresses", 3),
          ("none", 0))
    )


_HpicfDhcpv4ServerPoolOptionType_Type.__name__ = "Integer32"
_HpicfDhcpv4ServerPoolOptionType_Object = MibTableColumn
hpicfDhcpv4ServerPoolOptionType = _HpicfDhcpv4ServerPoolOptionType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 6, 1, 1, 2),
    _HpicfDhcpv4ServerPoolOptionType_Type()
)
hpicfDhcpv4ServerPoolOptionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDhcpv4ServerPoolOptionType.setStatus("current")


class _HpicfDhcpv4ServerPoolOptionData_Type(DisplayString):
    """Custom type hpicfDhcpv4ServerPoolOptionData based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpicfDhcpv4ServerPoolOptionData_Type.__name__ = "DisplayString"
_HpicfDhcpv4ServerPoolOptionData_Object = MibTableColumn
hpicfDhcpv4ServerPoolOptionData = _HpicfDhcpv4ServerPoolOptionData_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 6, 1, 1, 3),
    _HpicfDhcpv4ServerPoolOptionData_Type()
)
hpicfDhcpv4ServerPoolOptionData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDhcpv4ServerPoolOptionData.setStatus("current")
_HpicfDhcpv4ServerPoolOptionStatus_Type = RowStatus
_HpicfDhcpv4ServerPoolOptionStatus_Object = MibTableColumn
hpicfDhcpv4ServerPoolOptionStatus = _HpicfDhcpv4ServerPoolOptionStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 6, 1, 1, 4),
    _HpicfDhcpv4ServerPoolOptionStatus_Type()
)
hpicfDhcpv4ServerPoolOptionStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfDhcpv4ServerPoolOptionStatus.setStatus("current")
_HpicfDhcpv4PoolDynamicBind_ObjectIdentity = ObjectIdentity
hpicfDhcpv4PoolDynamicBind = _HpicfDhcpv4PoolDynamicBind_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 7)
)
_HpicfDhcpv4BindingTable_Object = MibTable
hpicfDhcpv4BindingTable = _HpicfDhcpv4BindingTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 7, 1)
)
if mibBuilder.loadTexts:
    hpicfDhcpv4BindingTable.setStatus("current")
_HpicfDhcpv4BindingEntry_Object = MibTableRow
hpicfDhcpv4BindingEntry = _HpicfDhcpv4BindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 7, 1, 1)
)
hpicfDhcpv4BindingEntry.setIndexNames(
    (0, "HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4ServerPoolName"),
    (0, "HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4BindingIpAddress"),
)
if mibBuilder.loadTexts:
    hpicfDhcpv4BindingEntry.setStatus("current")
_HpicfDhcpv4BindingIpAddress_Type = InetAddressIPv4
_HpicfDhcpv4BindingIpAddress_Object = MibTableColumn
hpicfDhcpv4BindingIpAddress = _HpicfDhcpv4BindingIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 7, 1, 1, 1),
    _HpicfDhcpv4BindingIpAddress_Type()
)
hpicfDhcpv4BindingIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfDhcpv4BindingIpAddress.setStatus("current")
_HpicfDhcpv4BindingHardwareAddress_Type = MacAddress
_HpicfDhcpv4BindingHardwareAddress_Object = MibTableColumn
hpicfDhcpv4BindingHardwareAddress = _HpicfDhcpv4BindingHardwareAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 7, 1, 1, 2),
    _HpicfDhcpv4BindingHardwareAddress_Type()
)
hpicfDhcpv4BindingHardwareAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpv4BindingHardwareAddress.setStatus("current")


class _HpicfDhcpv4BindingType_Type(Integer32):
    """Custom type hpicfDhcpv4BindingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 2),
          ("dynamic", 3),
          ("manual", 1))
    )


_HpicfDhcpv4BindingType_Type.__name__ = "Integer32"
_HpicfDhcpv4BindingType_Object = MibTableColumn
hpicfDhcpv4BindingType = _HpicfDhcpv4BindingType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 7, 1, 1, 3),
    _HpicfDhcpv4BindingType_Type()
)
hpicfDhcpv4BindingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpv4BindingType.setStatus("current")
_HpicfDhcpv4BindingLifeTime_Type = Unsigned32
_HpicfDhcpv4BindingLifeTime_Object = MibTableColumn
hpicfDhcpv4BindingLifeTime = _HpicfDhcpv4BindingLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 7, 1, 1, 4),
    _HpicfDhcpv4BindingLifeTime_Type()
)
hpicfDhcpv4BindingLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpv4BindingLifeTime.setStatus("current")
if mibBuilder.loadTexts:
    hpicfDhcpv4BindingLifeTime.setUnits("seconds")
_HpicfDhcpv4ServerConflicts_ObjectIdentity = ObjectIdentity
hpicfDhcpv4ServerConflicts = _HpicfDhcpv4ServerConflicts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 8)
)
_HpicfDhcpv4ConflictIPTable_Object = MibTable
hpicfDhcpv4ConflictIPTable = _HpicfDhcpv4ConflictIPTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 8, 1)
)
if mibBuilder.loadTexts:
    hpicfDhcpv4ConflictIPTable.setStatus("current")
_HpicfDhcpv4ConflictIPEntry_Object = MibTableRow
hpicfDhcpv4ConflictIPEntry = _HpicfDhcpv4ConflictIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 8, 1, 1)
)
hpicfDhcpv4ConflictIPEntry.setIndexNames(
    (0, "HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4ConflictIPAddress"),
)
if mibBuilder.loadTexts:
    hpicfDhcpv4ConflictIPEntry.setStatus("current")
_HpicfDhcpv4ConflictIPAddress_Type = InetAddressIPv4
_HpicfDhcpv4ConflictIPAddress_Object = MibTableColumn
hpicfDhcpv4ConflictIPAddress = _HpicfDhcpv4ConflictIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 8, 1, 1, 1),
    _HpicfDhcpv4ConflictIPAddress_Type()
)
hpicfDhcpv4ConflictIPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfDhcpv4ConflictIPAddress.setStatus("current")


class _HpicfDhcpv4ConflictIPDetectionMethod_Type(Integer32):
    """Custom type hpicfDhcpv4ConflictIPDetectionMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gratuitousArp", 2),
          ("ping", 1))
    )


_HpicfDhcpv4ConflictIPDetectionMethod_Type.__name__ = "Integer32"
_HpicfDhcpv4ConflictIPDetectionMethod_Object = MibTableColumn
hpicfDhcpv4ConflictIPDetectionMethod = _HpicfDhcpv4ConflictIPDetectionMethod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 8, 1, 1, 2),
    _HpicfDhcpv4ConflictIPDetectionMethod_Type()
)
hpicfDhcpv4ConflictIPDetectionMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpv4ConflictIPDetectionMethod.setStatus("current")
_HpicfDhcpv4ConflictIPDetectionTime_Type = DateAndTime
_HpicfDhcpv4ConflictIPDetectionTime_Object = MibTableColumn
hpicfDhcpv4ConflictIPDetectionTime = _HpicfDhcpv4ConflictIPDetectionTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 8, 1, 1, 3),
    _HpicfDhcpv4ConflictIPDetectionTime_Type()
)
hpicfDhcpv4ConflictIPDetectionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpv4ConflictIPDetectionTime.setStatus("current")


class _HpicfDhcpv4ServerEnable_Type(Integer32):
    """Custom type hpicfDhcpv4ServerEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("disableWithClearConfig", 3),
          ("enable", 1))
    )


_HpicfDhcpv4ServerEnable_Type.__name__ = "Integer32"
_HpicfDhcpv4ServerEnable_Object = MibScalar
hpicfDhcpv4ServerEnable = _HpicfDhcpv4ServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 10),
    _HpicfDhcpv4ServerEnable_Type()
)
hpicfDhcpv4ServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDhcpv4ServerEnable.setStatus("current")


class _HpicfDhcpv4PingPktNumber_Type(Integer32):
    """Custom type hpicfDhcpv4PingPktNumber based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_HpicfDhcpv4PingPktNumber_Type.__name__ = "Integer32"
_HpicfDhcpv4PingPktNumber_Object = MibScalar
hpicfDhcpv4PingPktNumber = _HpicfDhcpv4PingPktNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 11),
    _HpicfDhcpv4PingPktNumber_Type()
)
hpicfDhcpv4PingPktNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDhcpv4PingPktNumber.setStatus("current")


class _HpicfDhcpv4PingTimeOut_Type(Integer32):
    """Custom type hpicfDhcpv4PingTimeOut based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_HpicfDhcpv4PingTimeOut_Type.__name__ = "Integer32"
_HpicfDhcpv4PingTimeOut_Object = MibScalar
hpicfDhcpv4PingTimeOut = _HpicfDhcpv4PingTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 12),
    _HpicfDhcpv4PingTimeOut_Type()
)
hpicfDhcpv4PingTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDhcpv4PingTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    hpicfDhcpv4PingTimeOut.setUnits("seconds")
_HpicfDhcpv4ClearStatistics_Type = TruthValue
_HpicfDhcpv4ClearStatistics_Object = MibScalar
hpicfDhcpv4ClearStatistics = _HpicfDhcpv4ClearStatistics_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 13),
    _HpicfDhcpv4ClearStatistics_Type()
)
hpicfDhcpv4ClearStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDhcpv4ClearStatistics.setStatus("current")
_HpicfDhcpv4ClearBindings_Type = InetAddressIPv4
_HpicfDhcpv4ClearBindings_Object = MibScalar
hpicfDhcpv4ClearBindings = _HpicfDhcpv4ClearBindings_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 14),
    _HpicfDhcpv4ClearBindings_Type()
)
hpicfDhcpv4ClearBindings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDhcpv4ClearBindings.setStatus("current")
_HpicfDhcpv4ClearConflictIP_Type = InetAddressIPv4
_HpicfDhcpv4ClearConflictIP_Object = MibScalar
hpicfDhcpv4ClearConflictIP = _HpicfDhcpv4ClearConflictIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 15),
    _HpicfDhcpv4ClearConflictIP_Type()
)
hpicfDhcpv4ClearConflictIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDhcpv4ClearConflictIP.setStatus("current")


class _HpicfDhcpv4ConflictsLog_Type(TruthValue):
    """Custom type hpicfDhcpv4ConflictsLog based on TruthValue"""


_HpicfDhcpv4ConflictsLog_Object = MibScalar
hpicfDhcpv4ConflictsLog = _HpicfDhcpv4ConflictsLog_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 16),
    _HpicfDhcpv4ConflictsLog_Type()
)
hpicfDhcpv4ConflictsLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDhcpv4ConflictsLog.setStatus("current")


class _HpicfDhcpv4TrapEnable_Type(TruthValue):
    """Custom type hpicfDhcpv4TrapEnable based on TruthValue"""


_HpicfDhcpv4TrapEnable_Object = MibScalar
hpicfDhcpv4TrapEnable = _HpicfDhcpv4TrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 17),
    _HpicfDhcpv4TrapEnable_Type()
)
hpicfDhcpv4TrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDhcpv4TrapEnable.setStatus("current")
_HpicfDhcpv4ServerVlanEnable_Type = VidList
_HpicfDhcpv4ServerVlanEnable_Object = MibScalar
hpicfDhcpv4ServerVlanEnable = _HpicfDhcpv4ServerVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 18),
    _HpicfDhcpv4ServerVlanEnable_Type()
)
hpicfDhcpv4ServerVlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDhcpv4ServerVlanEnable.setStatus("current")


class _HpicfDhcpv4ServerOperStatus_Type(Integer32):
    """Custom type hpicfDhcpv4ServerOperStatus based on Integer32"""
    defaultValue = 0

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
        *(("disabled", 0),
          ("enabled", 1),
          ("inprogress", 3),
          ("paused", 2),
          ("shuttingdown", 4))
    )


_HpicfDhcpv4ServerOperStatus_Type.__name__ = "Integer32"
_HpicfDhcpv4ServerOperStatus_Object = MibScalar
hpicfDhcpv4ServerOperStatus = _HpicfDhcpv4ServerOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 1, 19),
    _HpicfDhcpv4ServerOperStatus_Type()
)
hpicfDhcpv4ServerOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpv4ServerOperStatus.setStatus("current")
_HpicfDhcpv4ServerConform_ObjectIdentity = ObjectIdentity
hpicfDhcpv4ServerConform = _HpicfDhcpv4ServerConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 2)
)
_HpicfDhcpv4ServerCompliances_ObjectIdentity = ObjectIdentity
hpicfDhcpv4ServerCompliances = _HpicfDhcpv4ServerCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 2, 1)
)
_HpicfDhcpv4ServerGroups_ObjectIdentity = ObjectIdentity
hpicfDhcpv4ServerGroups = _HpicfDhcpv4ServerGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 2, 2)
)
_HpicfDhcpv4ServerCompliances1_ObjectIdentity = ObjectIdentity
hpicfDhcpv4ServerCompliances1 = _HpicfDhcpv4ServerCompliances1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 2, 3)
)

# Managed Objects groups

hpicfDhcpv4ServerBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 2, 2, 1)
)
hpicfDhcpv4ServerBaseGroup.setObjects(
      *(("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4ServerEnable"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4PingPktNumber"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4PingTimeOut"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4ConflictsLog"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4ClearStatistics"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4ClearBindings"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4ClearConflictIP"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4TrapEnable"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4ServerVlanEnable"))
)
if mibBuilder.loadTexts:
    hpicfDhcpv4ServerBaseGroup.setStatus("deprecated")

hpicfDhcpv4ServerLeaseDataBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 2, 2, 2)
)
hpicfDhcpv4ServerLeaseDataBaseGroup.setObjects(
      *(("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4ServerDBFile"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4ServerDBWriteDelay"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4ServerDBWriteTimeout"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpServerDBFileWriteAttempts"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpServerDBFileWriteFailures"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpServerDBFileReadStatus"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpServerDBFileWriteStatus"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpServerDBFileLastWriteTime"))
)
if mibBuilder.loadTexts:
    hpicfDhcpv4ServerLeaseDataBaseGroup.setStatus("deprecated")

hpicfDhcpv4ServerBootpCountersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 2, 2, 3)
)
hpicfDhcpv4ServerBootpCountersGroup.setObjects(
      *(("HP-ICF-DHCPV4-SERVER-MIB", "hpicfBootpCountRequests"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfBootpCountReplies"))
)
if mibBuilder.loadTexts:
    hpicfDhcpv4ServerBootpCountersGroup.setStatus("current")

hpicfDhcpv4ServerCounterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 2, 2, 4)
)
hpicfDhcpv4ServerCounterGroup.setObjects(
      *(("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4CountDiscovers"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4CountOffers"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4CountRequests"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4CountDeclines"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4CountAcks"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4CountNaks"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4CountReleases"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4CountInforms"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4CountBadMsgs"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4CountPools"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4CountAutoBindings"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4CountStaticBindings"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4CountExpiredOrFreeBindings"))
)
if mibBuilder.loadTexts:
    hpicfDhcpv4ServerCounterGroup.setStatus("current")

hpicfDhcpv4ServerPoolGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 2, 2, 5)
)
hpicfDhcpv4ServerPoolGroup.setObjects(
      *(("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4ServerPoolNetworkAddress"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4ServerPoolNetworkAddressMask"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4ServerPoolDomainName"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4ServerPoolNetBIOSNodeType"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4ServerPoolLeaseTime"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4ServerPoolBootFile"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4ServerPoolLowThreshold"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4ServerPoolHighThreshold"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4ServerPoolFreeAddresses"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4ServerDNSServerAddress"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4ServerNetBIOSNameServer"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4ServerDefaultRouter"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4ServerTFTPServerName"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4ServerTFTPServerIpAddress"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4ServerStaticIpAddress"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4ServerStaticIpAddressMask"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4ServerStaticHardwareAddress"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4ServerPoolIsAuthoritative"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4ServerPoolStatus"))
)
if mibBuilder.loadTexts:
    hpicfDhcpv4ServerPoolGroup.setStatus("current")

hpicfDhcpv4ServerRangeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 2, 2, 6)
)
hpicfDhcpv4ServerRangeGroup.setObjects(
      *(("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4ServerRangeEndAddress"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4ServerRangeStatus"))
)
if mibBuilder.loadTexts:
    hpicfDhcpv4ServerRangeGroup.setStatus("current")

hpicfDhcpv4ServerOptionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 2, 2, 7)
)
hpicfDhcpv4ServerOptionGroup.setObjects(
      *(("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4ServerPoolOptionType"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4ServerPoolOptionData"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4ServerPoolOptionStatus"))
)
if mibBuilder.loadTexts:
    hpicfDhcpv4ServerOptionGroup.setStatus("current")

hpicfDhcpv4ServerBindingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 2, 2, 8)
)
hpicfDhcpv4ServerBindingGroup.setObjects(
      *(("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4BindingHardwareAddress"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4BindingType"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4BindingLifeTime"))
)
if mibBuilder.loadTexts:
    hpicfDhcpv4ServerBindingGroup.setStatus("current")

hpicfDhcpv4ServerConflictGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 2, 2, 9)
)
hpicfDhcpv4ServerConflictGroup.setObjects(
      *(("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4ConflictIPDetectionMethod"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4ConflictIPDetectionTime"))
)
if mibBuilder.loadTexts:
    hpicfDhcpv4ServerConflictGroup.setStatus("current")

hpicfDhcpv4ServerNotifyObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 2, 2, 10)
)
hpicfDhcpv4ServerNotifyObjectsGroup.setObjects(
      *(("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4ServerPoolLowThreshold"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4ServerPoolFreeAddresses"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4ServerPoolHighThreshold"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4ServerNotifyDuplicateIpAddr"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4ServerNotifyDuplicateMac"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4ServerNotifyClientOrServerDetected"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4ServerClientPhysicalAddress"))
)
if mibBuilder.loadTexts:
    hpicfDhcpv4ServerNotifyObjectsGroup.setStatus("current")

hpicfDhcpv4ServerLeaseDataBaseGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 2, 2, 12)
)
hpicfDhcpv4ServerLeaseDataBaseGroup1.setObjects(
      *(("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4ServerDBFile"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4ServerDBWriteDelay"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4ServerDBWriteTimeout"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpServerDBFileWriteAttempts"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpServerDBFileWriteFailures"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpServerDBFileReadStatus"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpServerDBFileWriteStatus"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpServerDBFileLastWriteTime"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4ServerDBFTPort"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4ServerDBSFTPUsername"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4ServerDBSFTPPassword"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4ServerDBValidateSFTPServer"))
)
if mibBuilder.loadTexts:
    hpicfDhcpv4ServerLeaseDataBaseGroup1.setStatus("current")

hpicfDhcpv4ServerBaseGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 2, 2, 13)
)
hpicfDhcpv4ServerBaseGroup1.setObjects(
      *(("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4ServerEnable"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4PingPktNumber"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4PingTimeOut"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4ConflictsLog"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4ClearStatistics"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4ClearBindings"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4ClearConflictIP"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4TrapEnable"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4ServerVlanEnable"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4ServerOperStatus"))
)
if mibBuilder.loadTexts:
    hpicfDhcpv4ServerBaseGroup1.setStatus("current")


# Notification objects

hpicfDhcpv4ServerFreeAddressLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 0, 5)
)
hpicfDhcpv4ServerFreeAddressLow.setObjects(
      *(("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4ServerPoolLowThreshold"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4ServerPoolFreeAddresses"))
)
if mibBuilder.loadTexts:
    hpicfDhcpv4ServerFreeAddressLow.setStatus(
        "current"
    )

hpicfDhcpv4ServerFreeAddressHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 0, 6)
)
hpicfDhcpv4ServerFreeAddressHigh.setObjects(
      *(("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4ServerPoolHighThreshold"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4ServerPoolFreeAddresses"))
)
if mibBuilder.loadTexts:
    hpicfDhcpv4ServerFreeAddressHigh.setStatus(
        "current"
    )

hpicfDhcpv4ServerDuplicateAddress = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 0, 7)
)
hpicfDhcpv4ServerDuplicateAddress.setObjects(
      *(("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4ServerNotifyDuplicateIpAddr"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4ServerNotifyDuplicateMac"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4ServerNotifyClientOrServerDetected"))
)
if mibBuilder.loadTexts:
    hpicfDhcpv4ServerDuplicateAddress.setStatus(
        "current"
    )

hpicfDhcpv4ServerIfLeaseLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 0, 8)
)
hpicfDhcpv4ServerIfLeaseLimitExceeded.setObjects(
      *(("IF-MIB", "ifName"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4ServerClientPhysicalAddress"))
)
if mibBuilder.loadTexts:
    hpicfDhcpv4ServerIfLeaseLimitExceeded.setStatus(
        "current"
    )


# Notifications groups

hpicfDhcpv4ServerNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 2, 2, 11)
)
hpicfDhcpv4ServerNotificationsGroup.setObjects(
      *(("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4ServerFreeAddressLow"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4ServerFreeAddressHigh"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4ServerDuplicateAddress"),
        ("HP-ICF-DHCPV4-SERVER-MIB", "hpicfDhcpv4ServerIfLeaseLimitExceeded"))
)
if mibBuilder.loadTexts:
    hpicfDhcpv4ServerNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hpicfDhcpv4ServerCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfDhcpv4ServerCompliance.setStatus(
        "deprecated"
    )

hpicfDhcpv4ServerCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 2, 1, 2)
)
if mibBuilder.loadTexts:
    hpicfDhcpv4ServerCompliance1.setStatus(
        "deprecated"
    )

hpicfDhcpv4ServerCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 99, 2, 1, 3)
)
if mibBuilder.loadTexts:
    hpicfDhcpv4ServerCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-DHCPV4-SERVER-MIB",
    **{"InetAddressIPv4": InetAddressIPv4,
       "hpicfDhcpv4ServerMIB": hpicfDhcpv4ServerMIB,
       "hpicfDhcpv4ServerNotifs": hpicfDhcpv4ServerNotifs,
       "hpicfDhcpv4ServerNotifyDuplicateIpAddr": hpicfDhcpv4ServerNotifyDuplicateIpAddr,
       "hpicfDhcpv4ServerNotifyDuplicateMac": hpicfDhcpv4ServerNotifyDuplicateMac,
       "hpicfDhcpv4ServerNotifyClientOrServerDetected": hpicfDhcpv4ServerNotifyClientOrServerDetected,
       "hpicfDhcpv4ServerClientPhysicalAddress": hpicfDhcpv4ServerClientPhysicalAddress,
       "hpicfDhcpv4ServerFreeAddressLow": hpicfDhcpv4ServerFreeAddressLow,
       "hpicfDhcpv4ServerFreeAddressHigh": hpicfDhcpv4ServerFreeAddressHigh,
       "hpicfDhcpv4ServerDuplicateAddress": hpicfDhcpv4ServerDuplicateAddress,
       "hpicfDhcpv4ServerIfLeaseLimitExceeded": hpicfDhcpv4ServerIfLeaseLimitExceeded,
       "hpicfDhcpv4ServerObjects": hpicfDhcpv4ServerObjects,
       "hpicfDhcpv4LeaseDataBase": hpicfDhcpv4LeaseDataBase,
       "hpicfDhcpv4ServerDBFile": hpicfDhcpv4ServerDBFile,
       "hpicfDhcpv4ServerDBWriteDelay": hpicfDhcpv4ServerDBWriteDelay,
       "hpicfDhcpv4ServerDBWriteTimeout": hpicfDhcpv4ServerDBWriteTimeout,
       "hpicfDhcpServerDBFileWriteAttempts": hpicfDhcpServerDBFileWriteAttempts,
       "hpicfDhcpServerDBFileWriteFailures": hpicfDhcpServerDBFileWriteFailures,
       "hpicfDhcpServerDBFileReadStatus": hpicfDhcpServerDBFileReadStatus,
       "hpicfDhcpServerDBFileWriteStatus": hpicfDhcpServerDBFileWriteStatus,
       "hpicfDhcpServerDBFileLastWriteTime": hpicfDhcpServerDBFileLastWriteTime,
       "hpicfDhcpv4ServerDBFTPort": hpicfDhcpv4ServerDBFTPort,
       "hpicfDhcpv4ServerDBSFTPUsername": hpicfDhcpv4ServerDBSFTPUsername,
       "hpicfDhcpv4ServerDBSFTPPassword": hpicfDhcpv4ServerDBSFTPPassword,
       "hpicfDhcpv4ServerDBValidateSFTPServer": hpicfDhcpv4ServerDBValidateSFTPServer,
       "hpicfDhcpv4BootpCounters": hpicfDhcpv4BootpCounters,
       "hpicfBootpCountRequests": hpicfBootpCountRequests,
       "hpicfBootpCountReplies": hpicfBootpCountReplies,
       "hpicfDhcpv4Counters": hpicfDhcpv4Counters,
       "hpicfDhcpv4CountDiscovers": hpicfDhcpv4CountDiscovers,
       "hpicfDhcpv4CountOffers": hpicfDhcpv4CountOffers,
       "hpicfDhcpv4CountRequests": hpicfDhcpv4CountRequests,
       "hpicfDhcpv4CountDeclines": hpicfDhcpv4CountDeclines,
       "hpicfDhcpv4CountAcks": hpicfDhcpv4CountAcks,
       "hpicfDhcpv4CountNaks": hpicfDhcpv4CountNaks,
       "hpicfDhcpv4CountReleases": hpicfDhcpv4CountReleases,
       "hpicfDhcpv4CountInforms": hpicfDhcpv4CountInforms,
       "hpicfDhcpv4CountBadMsgs": hpicfDhcpv4CountBadMsgs,
       "hpicfDhcpv4CountPools": hpicfDhcpv4CountPools,
       "hpicfDhcpv4CountAutoBindings": hpicfDhcpv4CountAutoBindings,
       "hpicfDhcpv4CountStaticBindings": hpicfDhcpv4CountStaticBindings,
       "hpicfDhcpv4CountExpiredOrFreeBindings": hpicfDhcpv4CountExpiredOrFreeBindings,
       "hpicfDhcpv4IpPool": hpicfDhcpv4IpPool,
       "hpicfDhcpv4ServerPoolTable": hpicfDhcpv4ServerPoolTable,
       "hpicfDhcpv4ServerPoolEntry": hpicfDhcpv4ServerPoolEntry,
       "hpicfDhcpv4ServerPoolName": hpicfDhcpv4ServerPoolName,
       "hpicfDhcpv4ServerPoolNetworkAddress": hpicfDhcpv4ServerPoolNetworkAddress,
       "hpicfDhcpv4ServerPoolNetworkAddressMask": hpicfDhcpv4ServerPoolNetworkAddressMask,
       "hpicfDhcpv4ServerPoolDomainName": hpicfDhcpv4ServerPoolDomainName,
       "hpicfDhcpv4ServerPoolNetBIOSNodeType": hpicfDhcpv4ServerPoolNetBIOSNodeType,
       "hpicfDhcpv4ServerPoolLeaseTime": hpicfDhcpv4ServerPoolLeaseTime,
       "hpicfDhcpv4ServerPoolBootFile": hpicfDhcpv4ServerPoolBootFile,
       "hpicfDhcpv4ServerPoolLowThreshold": hpicfDhcpv4ServerPoolLowThreshold,
       "hpicfDhcpv4ServerPoolHighThreshold": hpicfDhcpv4ServerPoolHighThreshold,
       "hpicfDhcpv4ServerPoolFreeAddresses": hpicfDhcpv4ServerPoolFreeAddresses,
       "hpicfDhcpv4ServerDNSServerAddress": hpicfDhcpv4ServerDNSServerAddress,
       "hpicfDhcpv4ServerNetBIOSNameServer": hpicfDhcpv4ServerNetBIOSNameServer,
       "hpicfDhcpv4ServerDefaultRouter": hpicfDhcpv4ServerDefaultRouter,
       "hpicfDhcpv4ServerTFTPServerName": hpicfDhcpv4ServerTFTPServerName,
       "hpicfDhcpv4ServerTFTPServerIpAddress": hpicfDhcpv4ServerTFTPServerIpAddress,
       "hpicfDhcpv4ServerStaticIpAddress": hpicfDhcpv4ServerStaticIpAddress,
       "hpicfDhcpv4ServerStaticIpAddressMask": hpicfDhcpv4ServerStaticIpAddressMask,
       "hpicfDhcpv4ServerStaticHardwareAddress": hpicfDhcpv4ServerStaticHardwareAddress,
       "hpicfDhcpv4ServerPoolIsAuthoritative": hpicfDhcpv4ServerPoolIsAuthoritative,
       "hpicfDhcpv4ServerPoolStatus": hpicfDhcpv4ServerPoolStatus,
       "hpicfDhcpv4PoolIpRange": hpicfDhcpv4PoolIpRange,
       "hpicfDhcpv4ServerRangeTable": hpicfDhcpv4ServerRangeTable,
       "hpicfDhcpv4ServerRangeEntry": hpicfDhcpv4ServerRangeEntry,
       "hpicfDhcpv4ServerRangeStartAddress": hpicfDhcpv4ServerRangeStartAddress,
       "hpicfDhcpv4ServerRangeEndAddress": hpicfDhcpv4ServerRangeEndAddress,
       "hpicfDhcpv4ServerRangeStatus": hpicfDhcpv4ServerRangeStatus,
       "hpicfDhcpv4PoolOption": hpicfDhcpv4PoolOption,
       "hpicfDhcpv4ServerPoolOptionTable": hpicfDhcpv4ServerPoolOptionTable,
       "hpicfDhcpv4ServerPoolOptionEntry": hpicfDhcpv4ServerPoolOptionEntry,
       "hpicfDhcpv4ServerPoolOptionCode": hpicfDhcpv4ServerPoolOptionCode,
       "hpicfDhcpv4ServerPoolOptionType": hpicfDhcpv4ServerPoolOptionType,
       "hpicfDhcpv4ServerPoolOptionData": hpicfDhcpv4ServerPoolOptionData,
       "hpicfDhcpv4ServerPoolOptionStatus": hpicfDhcpv4ServerPoolOptionStatus,
       "hpicfDhcpv4PoolDynamicBind": hpicfDhcpv4PoolDynamicBind,
       "hpicfDhcpv4BindingTable": hpicfDhcpv4BindingTable,
       "hpicfDhcpv4BindingEntry": hpicfDhcpv4BindingEntry,
       "hpicfDhcpv4BindingIpAddress": hpicfDhcpv4BindingIpAddress,
       "hpicfDhcpv4BindingHardwareAddress": hpicfDhcpv4BindingHardwareAddress,
       "hpicfDhcpv4BindingType": hpicfDhcpv4BindingType,
       "hpicfDhcpv4BindingLifeTime": hpicfDhcpv4BindingLifeTime,
       "hpicfDhcpv4ServerConflicts": hpicfDhcpv4ServerConflicts,
       "hpicfDhcpv4ConflictIPTable": hpicfDhcpv4ConflictIPTable,
       "hpicfDhcpv4ConflictIPEntry": hpicfDhcpv4ConflictIPEntry,
       "hpicfDhcpv4ConflictIPAddress": hpicfDhcpv4ConflictIPAddress,
       "hpicfDhcpv4ConflictIPDetectionMethod": hpicfDhcpv4ConflictIPDetectionMethod,
       "hpicfDhcpv4ConflictIPDetectionTime": hpicfDhcpv4ConflictIPDetectionTime,
       "hpicfDhcpv4ServerEnable": hpicfDhcpv4ServerEnable,
       "hpicfDhcpv4PingPktNumber": hpicfDhcpv4PingPktNumber,
       "hpicfDhcpv4PingTimeOut": hpicfDhcpv4PingTimeOut,
       "hpicfDhcpv4ClearStatistics": hpicfDhcpv4ClearStatistics,
       "hpicfDhcpv4ClearBindings": hpicfDhcpv4ClearBindings,
       "hpicfDhcpv4ClearConflictIP": hpicfDhcpv4ClearConflictIP,
       "hpicfDhcpv4ConflictsLog": hpicfDhcpv4ConflictsLog,
       "hpicfDhcpv4TrapEnable": hpicfDhcpv4TrapEnable,
       "hpicfDhcpv4ServerVlanEnable": hpicfDhcpv4ServerVlanEnable,
       "hpicfDhcpv4ServerOperStatus": hpicfDhcpv4ServerOperStatus,
       "hpicfDhcpv4ServerConform": hpicfDhcpv4ServerConform,
       "hpicfDhcpv4ServerCompliances": hpicfDhcpv4ServerCompliances,
       "hpicfDhcpv4ServerCompliance": hpicfDhcpv4ServerCompliance,
       "hpicfDhcpv4ServerCompliance1": hpicfDhcpv4ServerCompliance1,
       "hpicfDhcpv4ServerCompliance2": hpicfDhcpv4ServerCompliance2,
       "hpicfDhcpv4ServerGroups": hpicfDhcpv4ServerGroups,
       "hpicfDhcpv4ServerBaseGroup": hpicfDhcpv4ServerBaseGroup,
       "hpicfDhcpv4ServerLeaseDataBaseGroup": hpicfDhcpv4ServerLeaseDataBaseGroup,
       "hpicfDhcpv4ServerBootpCountersGroup": hpicfDhcpv4ServerBootpCountersGroup,
       "hpicfDhcpv4ServerCounterGroup": hpicfDhcpv4ServerCounterGroup,
       "hpicfDhcpv4ServerPoolGroup": hpicfDhcpv4ServerPoolGroup,
       "hpicfDhcpv4ServerRangeGroup": hpicfDhcpv4ServerRangeGroup,
       "hpicfDhcpv4ServerOptionGroup": hpicfDhcpv4ServerOptionGroup,
       "hpicfDhcpv4ServerBindingGroup": hpicfDhcpv4ServerBindingGroup,
       "hpicfDhcpv4ServerConflictGroup": hpicfDhcpv4ServerConflictGroup,
       "hpicfDhcpv4ServerNotifyObjectsGroup": hpicfDhcpv4ServerNotifyObjectsGroup,
       "hpicfDhcpv4ServerNotificationsGroup": hpicfDhcpv4ServerNotificationsGroup,
       "hpicfDhcpv4ServerLeaseDataBaseGroup1": hpicfDhcpv4ServerLeaseDataBaseGroup1,
       "hpicfDhcpv4ServerBaseGroup1": hpicfDhcpv4ServerBaseGroup1,
       "hpicfDhcpv4ServerCompliances1": hpicfDhcpv4ServerCompliances1}
)
