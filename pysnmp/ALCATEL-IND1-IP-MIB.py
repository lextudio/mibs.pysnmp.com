# SNMP MIB module (ALCATEL-IND1-IP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-IP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:36:13 2024
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

(softentIND1Ip,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1Ip")

(InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(ipCidrRouteEntry,) = mibBuilder.importSymbols(
    "IP-FORWARD-MIB",
    "ipCidrRouteEntry")

(ipNetToMediaEntry,
 ipNetToMediaIfIndex,
 ipNetToMediaNetAddress) = mibBuilder.importSymbols(
    "IP-MIB",
    "ipNetToMediaEntry",
    "ipNetToMediaIfIndex",
    "ipNetToMediaNetAddress")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

alcatelIND1IPMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1)
)
alcatelIND1IPMIB.setRevisions(
        ("2012-03-23 00:00",
         "2011-03-07 00:00",
         "2011-01-25 00:00",
         "2010-05-13 00:00",
         "2009-05-19 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1IPMIBNotifications_ObjectIdentity = ObjectIdentity
alcatelIND1IPMIBNotifications = _AlcatelIND1IPMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 0)
)
if mibBuilder.loadTexts:
    alcatelIND1IPMIBNotifications.setStatus("current")
_AlcatelIND1IPMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1IPMIBObjects = _AlcatelIND1IPMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1)
)
_AlaIpConfig_ObjectIdentity = ObjectIdentity
alaIpConfig = _AlaIpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 1)
)


class _AlaIpClearArpCache_Type(Integer32):
    """Custom type alaIpClearArpCache based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_AlaIpClearArpCache_Type.__name__ = "Integer32"
_AlaIpClearArpCache_Object = MibScalar
alaIpClearArpCache = _AlaIpClearArpCache_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 1, 1),
    _AlaIpClearArpCache_Type()
)
alaIpClearArpCache.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpClearArpCache.setStatus("current")


class _AlaIpDirectedBroadcast_Type(Integer32):
    """Custom type alaIpDirectedBroadcast based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_AlaIpDirectedBroadcast_Type.__name__ = "Integer32"
_AlaIpDirectedBroadcast_Object = MibScalar
alaIpDirectedBroadcast = _AlaIpDirectedBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 1, 2),
    _AlaIpDirectedBroadcast_Type()
)
alaIpDirectedBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpDirectedBroadcast.setStatus("current")


class _AlaIpClearArpFilter_Type(Integer32):
    """Custom type alaIpClearArpFilter based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_AlaIpClearArpFilter_Type.__name__ = "Integer32"
_AlaIpClearArpFilter_Object = MibScalar
alaIpClearArpFilter = _AlaIpClearArpFilter_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 1, 3),
    _AlaIpClearArpFilter_Type()
)
alaIpClearArpFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpClearArpFilter.setStatus("current")
_AlaIpNetToMediaTable_Object = MibTable
alaIpNetToMediaTable = _AlaIpNetToMediaTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 2)
)
if mibBuilder.loadTexts:
    alaIpNetToMediaTable.setStatus("current")
_AlaIpNetToMediaEntry_Object = MibTableRow
alaIpNetToMediaEntry = _AlaIpNetToMediaEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 2, 1)
)
alaIpNetToMediaEntry.setIndexNames(
    (0, "IP-MIB", "ipNetToMediaIfIndex"),
    (0, "IP-MIB", "ipNetToMediaNetAddress"),
)
if mibBuilder.loadTexts:
    alaIpNetToMediaEntry.setStatus("current")
_AlaIpNetToMediaPhysAddress_Type = PhysAddress
_AlaIpNetToMediaPhysAddress_Object = MibTableColumn
alaIpNetToMediaPhysAddress = _AlaIpNetToMediaPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 2, 1, 1),
    _AlaIpNetToMediaPhysAddress_Type()
)
alaIpNetToMediaPhysAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpNetToMediaPhysAddress.setStatus("current")


class _AlaIpNetToMediaProxy_Type(Integer32):
    """Custom type alaIpNetToMediaProxy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_AlaIpNetToMediaProxy_Type.__name__ = "Integer32"
_AlaIpNetToMediaProxy_Object = MibTableColumn
alaIpNetToMediaProxy = _AlaIpNetToMediaProxy_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 2, 1, 2),
    _AlaIpNetToMediaProxy_Type()
)
alaIpNetToMediaProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpNetToMediaProxy.setStatus("current")


class _AlaIpNetToMediaVrrp_Type(Integer32):
    """Custom type alaIpNetToMediaVrrp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_AlaIpNetToMediaVrrp_Type.__name__ = "Integer32"
_AlaIpNetToMediaVrrp_Object = MibTableColumn
alaIpNetToMediaVrrp = _AlaIpNetToMediaVrrp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 2, 1, 3),
    _AlaIpNetToMediaVrrp_Type()
)
alaIpNetToMediaVrrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpNetToMediaVrrp.setStatus("current")


class _AlaIpNetToMediaAuth_Type(Integer32):
    """Custom type alaIpNetToMediaAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_AlaIpNetToMediaAuth_Type.__name__ = "Integer32"
_AlaIpNetToMediaAuth_Object = MibTableColumn
alaIpNetToMediaAuth = _AlaIpNetToMediaAuth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 2, 1, 4),
    _AlaIpNetToMediaAuth_Type()
)
alaIpNetToMediaAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpNetToMediaAuth.setStatus("current")


class _AlaIpNetToMediaName_Type(SnmpAdminString):
    """Custom type alaIpNetToMediaName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaIpNetToMediaName_Type.__name__ = "SnmpAdminString"
_AlaIpNetToMediaName_Object = MibTableColumn
alaIpNetToMediaName = _AlaIpNetToMediaName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 2, 1, 5),
    _AlaIpNetToMediaName_Type()
)
alaIpNetToMediaName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpNetToMediaName.setStatus("current")
_AlaDoSConfig_ObjectIdentity = ObjectIdentity
alaDoSConfig = _AlaDoSConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 3)
)
_AlaDoSTable_Object = MibTable
alaDoSTable = _AlaDoSTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    alaDoSTable.setStatus("current")
_AlaDoSEntry_Object = MibTableRow
alaDoSEntry = _AlaDoSEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 3, 1, 1)
)
alaDoSEntry.setIndexNames(
    (0, "ALCATEL-IND1-IP-MIB", "alaDoSType"),
)
if mibBuilder.loadTexts:
    alaDoSEntry.setStatus("current")


class _AlaDoSType_Type(Integer32):
    """Custom type alaDoSType based on Integer32"""
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
              7,
              8,
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("arpattack", 12),
          ("arppoison", 13),
          ("invalidip", 8),
          ("land", 5),
          ("loopbacksrcip", 7),
          ("mcastmismatch", 9),
          ("pepsi", 4),
          ("pingattack", 11),
          ("pingofdeath", 2),
          ("portscan", 0),
          ("smurf", 3),
          ("tcpsyn", 1),
          ("teardropBonkBoink", 6),
          ("ucastipmcastmac", 10))
    )


_AlaDoSType_Type.__name__ = "Integer32"
_AlaDoSType_Object = MibTableColumn
alaDoSType = _AlaDoSType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 3, 1, 1, 1),
    _AlaDoSType_Type()
)
alaDoSType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDoSType.setStatus("current")
_AlaDoSDetected_Type = Counter32
_AlaDoSDetected_Object = MibTableColumn
alaDoSDetected = _AlaDoSDetected_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 3, 1, 1, 2),
    _AlaDoSDetected_Type()
)
alaDoSDetected.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDoSDetected.setStatus("current")
_AlaDoSIp_Type = IpAddress
_AlaDoSIp_Object = MibTableColumn
alaDoSIp = _AlaDoSIp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 3, 1, 1, 3),
    _AlaDoSIp_Type()
)
alaDoSIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDoSIp.setStatus("current")
_AlaDoSMac_Type = MacAddress
_AlaDoSMac_Object = MibTableColumn
alaDoSMac = _AlaDoSMac_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 3, 1, 1, 4),
    _AlaDoSMac_Type()
)
alaDoSMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDoSMac.setStatus("current")
_AlaDoSSlot_Type = Integer32
_AlaDoSSlot_Object = MibTableColumn
alaDoSSlot = _AlaDoSSlot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 3, 1, 1, 5),
    _AlaDoSSlot_Type()
)
alaDoSSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDoSSlot.setStatus("current")
_AlaDoSPort_Type = Integer32
_AlaDoSPort_Object = MibTableColumn
alaDoSPort = _AlaDoSPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 3, 1, 1, 6),
    _AlaDoSPort_Type()
)
alaDoSPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDoSPort.setStatus("current")


class _AlaDoSStatus_Type(Integer32):
    """Custom type alaDoSStatus based on Integer32"""
    defaultValue = 1

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


_AlaDoSStatus_Type.__name__ = "Integer32"
_AlaDoSStatus_Object = MibTableColumn
alaDoSStatus = _AlaDoSStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 3, 1, 1, 7),
    _AlaDoSStatus_Type()
)
alaDoSStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDoSStatus.setStatus("current")
_AlaDoSChassisId_Type = Integer32
_AlaDoSChassisId_Object = MibTableColumn
alaDoSChassisId = _AlaDoSChassisId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 3, 1, 1, 8),
    _AlaDoSChassisId_Type()
)
alaDoSChassisId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDoSChassisId.setStatus("current")


class _AlaDoSPortScanClosePortPenalty_Type(Integer32):
    """Custom type alaDoSPortScanClosePortPenalty based on Integer32"""
    defaultValue = 10


_AlaDoSPortScanClosePortPenalty_Object = MibScalar
alaDoSPortScanClosePortPenalty = _AlaDoSPortScanClosePortPenalty_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 3, 2),
    _AlaDoSPortScanClosePortPenalty_Type()
)
alaDoSPortScanClosePortPenalty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDoSPortScanClosePortPenalty.setStatus("current")


class _AlaDoSPortScanTcpOpenPortPenalty_Type(Integer32):
    """Custom type alaDoSPortScanTcpOpenPortPenalty based on Integer32"""
    defaultValue = 0


_AlaDoSPortScanTcpOpenPortPenalty_Object = MibScalar
alaDoSPortScanTcpOpenPortPenalty = _AlaDoSPortScanTcpOpenPortPenalty_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 3, 3),
    _AlaDoSPortScanTcpOpenPortPenalty_Type()
)
alaDoSPortScanTcpOpenPortPenalty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDoSPortScanTcpOpenPortPenalty.setStatus("current")


class _AlaDoSPortScanUdpOpenPortPenalty_Type(Integer32):
    """Custom type alaDoSPortScanUdpOpenPortPenalty based on Integer32"""
    defaultValue = 0


_AlaDoSPortScanUdpOpenPortPenalty_Object = MibScalar
alaDoSPortScanUdpOpenPortPenalty = _AlaDoSPortScanUdpOpenPortPenalty_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 3, 4),
    _AlaDoSPortScanUdpOpenPortPenalty_Type()
)
alaDoSPortScanUdpOpenPortPenalty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDoSPortScanUdpOpenPortPenalty.setStatus("current")
_AlaDoSPortScanTotalPenalty_Type = Integer32
_AlaDoSPortScanTotalPenalty_Object = MibScalar
alaDoSPortScanTotalPenalty = _AlaDoSPortScanTotalPenalty_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 3, 5),
    _AlaDoSPortScanTotalPenalty_Type()
)
alaDoSPortScanTotalPenalty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDoSPortScanTotalPenalty.setStatus("current")


class _AlaDoSPortScanThreshold_Type(Integer32):
    """Custom type alaDoSPortScanThreshold based on Integer32"""
    defaultValue = 1000


_AlaDoSPortScanThreshold_Object = MibScalar
alaDoSPortScanThreshold = _AlaDoSPortScanThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 3, 6),
    _AlaDoSPortScanThreshold_Type()
)
alaDoSPortScanThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDoSPortScanThreshold.setStatus("current")


class _AlaDoSPortScanDecay_Type(Integer32):
    """Custom type alaDoSPortScanDecay based on Integer32"""
    defaultValue = 2


_AlaDoSPortScanDecay_Object = MibScalar
alaDoSPortScanDecay = _AlaDoSPortScanDecay_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 3, 7),
    _AlaDoSPortScanDecay_Type()
)
alaDoSPortScanDecay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDoSPortScanDecay.setStatus("current")


class _AlaDoSTrapCntl_Type(Integer32):
    """Custom type alaDoSTrapCntl based on Integer32"""
    defaultValue = 1

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


_AlaDoSTrapCntl_Type.__name__ = "Integer32"
_AlaDoSTrapCntl_Object = MibScalar
alaDoSTrapCntl = _AlaDoSTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 3, 8),
    _AlaDoSTrapCntl_Type()
)
alaDoSTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDoSTrapCntl.setStatus("current")


class _AlaDoSARPRate_Type(Integer32):
    """Custom type alaDoSARPRate based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500),
    )


_AlaDoSARPRate_Type.__name__ = "Integer32"
_AlaDoSARPRate_Object = MibScalar
alaDoSARPRate = _AlaDoSARPRate_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 3, 9),
    _AlaDoSARPRate_Type()
)
alaDoSARPRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDoSARPRate.setStatus("current")


class _AlaDoSPingRate_Type(Integer32):
    """Custom type alaDoSPingRate based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_AlaDoSPingRate_Type.__name__ = "Integer32"
_AlaDoSPingRate_Object = MibScalar
alaDoSPingRate = _AlaDoSPingRate_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 3, 10),
    _AlaDoSPingRate_Type()
)
alaDoSPingRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDoSPingRate.setStatus("current")
_AlaDoSArpPoisonTable_Object = MibTable
alaDoSArpPoisonTable = _AlaDoSArpPoisonTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 3, 11)
)
if mibBuilder.loadTexts:
    alaDoSArpPoisonTable.setStatus("current")
_AlaDoSArpPoisonEntry_Object = MibTableRow
alaDoSArpPoisonEntry = _AlaDoSArpPoisonEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 3, 11, 1)
)
alaDoSArpPoisonEntry.setIndexNames(
    (0, "ALCATEL-IND1-IP-MIB", "alaDoSArpPoisonIpAddr"),
)
if mibBuilder.loadTexts:
    alaDoSArpPoisonEntry.setStatus("current")
_AlaDoSArpPoisonIpAddr_Type = IpAddress
_AlaDoSArpPoisonIpAddr_Object = MibTableColumn
alaDoSArpPoisonIpAddr = _AlaDoSArpPoisonIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 3, 11, 1, 1),
    _AlaDoSArpPoisonIpAddr_Type()
)
alaDoSArpPoisonIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDoSArpPoisonIpAddr.setStatus("current")
_AlaDoSArpPoisonDetected_Type = Counter32
_AlaDoSArpPoisonDetected_Object = MibTableColumn
alaDoSArpPoisonDetected = _AlaDoSArpPoisonDetected_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 3, 11, 1, 2),
    _AlaDoSArpPoisonDetected_Type()
)
alaDoSArpPoisonDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDoSArpPoisonDetected.setStatus("current")
_AlaDoSArpPoisonRowStatus_Type = RowStatus
_AlaDoSArpPoisonRowStatus_Object = MibTableColumn
alaDoSArpPoisonRowStatus = _AlaDoSArpPoisonRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 3, 11, 1, 3),
    _AlaDoSArpPoisonRowStatus_Type()
)
alaDoSArpPoisonRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDoSArpPoisonRowStatus.setStatus("current")
_IpNetToMediaAugTable_Object = MibTable
ipNetToMediaAugTable = _IpNetToMediaAugTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 4)
)
if mibBuilder.loadTexts:
    ipNetToMediaAugTable.setStatus("current")
_IpNetToMediaAugEntry_Object = MibTableRow
ipNetToMediaAugEntry = _IpNetToMediaAugEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ipNetToMediaAugEntry.setStatus("current")
_IpNetToMediaSlot_Type = Integer32
_IpNetToMediaSlot_Object = MibTableColumn
ipNetToMediaSlot = _IpNetToMediaSlot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 4, 1, 1),
    _IpNetToMediaSlot_Type()
)
ipNetToMediaSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNetToMediaSlot.setStatus("current")
_IpNetToMediaPort_Type = Integer32
_IpNetToMediaPort_Object = MibTableColumn
ipNetToMediaPort = _IpNetToMediaPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 4, 1, 2),
    _IpNetToMediaPort_Type()
)
ipNetToMediaPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNetToMediaPort.setStatus("current")


class _IpNetToMediaName_Type(SnmpAdminString):
    """Custom type ipNetToMediaName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_IpNetToMediaName_Type.__name__ = "SnmpAdminString"
_IpNetToMediaName_Object = MibTableColumn
ipNetToMediaName = _IpNetToMediaName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 4, 1, 3),
    _IpNetToMediaName_Type()
)
ipNetToMediaName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNetToMediaName.setStatus("current")
_IpNetToMediaChassisId_Type = Integer32
_IpNetToMediaChassisId_Object = MibTableColumn
ipNetToMediaChassisId = _IpNetToMediaChassisId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 4, 1, 4),
    _IpNetToMediaChassisId_Type()
)
ipNetToMediaChassisId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNetToMediaChassisId.setStatus("current")
_TrafficEventTrapObjs_ObjectIdentity = ObjectIdentity
trafficEventTrapObjs = _TrafficEventTrapObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 5)
)


class _PktDropType_Type(Integer32):
    """Custom type pktDropType based on Integer32"""
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
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("bgpTriggeredUserPortDisable", 5),
          ("bpduTriggeredUserPortDisable", 4),
          ("ospfTriggeredUserPortDisable", 6),
          ("ripTriggeredUserPortDisable", 7),
          ("rulematchTriggeredPortDisable", 2),
          ("spoofTriggeredUserPortDisable", 3),
          ("spoofedIp", 0),
          ("toBlockedPort", 1),
          ("vrrpTriggeredUserPortDisable", 8))
    )


_PktDropType_Type.__name__ = "Integer32"
_PktDropType_Object = MibScalar
pktDropType = _PktDropType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 5, 1),
    _PktDropType_Type()
)
pktDropType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pktDropType.setStatus("current")
_PktDropIfIndex_Type = InterfaceIndexOrZero
_PktDropIfIndex_Object = MibScalar
pktDropIfIndex = _PktDropIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 5, 2),
    _PktDropIfIndex_Type()
)
pktDropIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pktDropIfIndex.setStatus("current")
_PktDropCount_Type = Integer32
_PktDropCount_Object = MibScalar
pktDropCount = _PktDropCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 5, 3),
    _PktDropCount_Type()
)
pktDropCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pktDropCount.setStatus("current")


class _PktDropFrag_Type(OctetString):
    """Custom type pktDropFrag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_PktDropFrag_Type.__name__ = "OctetString"
_PktDropFrag_Object = MibScalar
pktDropFrag = _PktDropFrag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 5, 4),
    _PktDropFrag_Type()
)
pktDropFrag.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pktDropFrag.setStatus("current")
_IpCidrRouteAugTable_Object = MibTable
ipCidrRouteAugTable = _IpCidrRouteAugTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 6)
)
if mibBuilder.loadTexts:
    ipCidrRouteAugTable.setStatus("current")
_IpCidrRouteAugEntry_Object = MibTableRow
ipCidrRouteAugEntry = _IpCidrRouteAugEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 6, 1)
)
if mibBuilder.loadTexts:
    ipCidrRouteAugEntry.setStatus("current")


class _IpCidrRouteScope_Type(Integer32):
    """Custom type ipCidrRouteScope based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("emproute", 2),
          ("niroute", 1))
    )


_IpCidrRouteScope_Type.__name__ = "Integer32"
_IpCidrRouteScope_Object = MibTableColumn
ipCidrRouteScope = _IpCidrRouteScope_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 6, 1, 1),
    _IpCidrRouteScope_Type()
)
ipCidrRouteScope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCidrRouteScope.setStatus("current")
_AlaIcmpCtrlTable_Object = MibTable
alaIcmpCtrlTable = _AlaIcmpCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 7)
)
if mibBuilder.loadTexts:
    alaIcmpCtrlTable.setStatus("current")
_AlaIcmpCtrlEntry_Object = MibTableRow
alaIcmpCtrlEntry = _AlaIcmpCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 7, 1)
)
alaIcmpCtrlEntry.setIndexNames(
    (0, "ALCATEL-IND1-IP-MIB", "alaIcmpCtrlType"),
    (0, "ALCATEL-IND1-IP-MIB", "alaIcmpCtrlCode"),
)
if mibBuilder.loadTexts:
    alaIcmpCtrlEntry.setStatus("current")


class _AlaIcmpCtrlType_Type(Integer32):
    """Custom type alaIcmpCtrlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 18),
    )


_AlaIcmpCtrlType_Type.__name__ = "Integer32"
_AlaIcmpCtrlType_Object = MibTableColumn
alaIcmpCtrlType = _AlaIcmpCtrlType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 7, 1, 1),
    _AlaIcmpCtrlType_Type()
)
alaIcmpCtrlType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIcmpCtrlType.setStatus("current")


class _AlaIcmpCtrlCode_Type(Integer32):
    """Custom type alaIcmpCtrlCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AlaIcmpCtrlCode_Type.__name__ = "Integer32"
_AlaIcmpCtrlCode_Object = MibTableColumn
alaIcmpCtrlCode = _AlaIcmpCtrlCode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 7, 1, 2),
    _AlaIcmpCtrlCode_Type()
)
alaIcmpCtrlCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIcmpCtrlCode.setStatus("current")


class _AlaIcmpCtrlStatus_Type(Integer32):
    """Custom type alaIcmpCtrlStatus based on Integer32"""
    defaultValue = 1

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


_AlaIcmpCtrlStatus_Type.__name__ = "Integer32"
_AlaIcmpCtrlStatus_Object = MibTableColumn
alaIcmpCtrlStatus = _AlaIcmpCtrlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 7, 1, 3),
    _AlaIcmpCtrlStatus_Type()
)
alaIcmpCtrlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIcmpCtrlStatus.setStatus("current")


class _AlaIcmpCtrlPktGap_Type(Integer32):
    """Custom type alaIcmpCtrlPktGap based on Integer32"""
    defaultValue = 0


_AlaIcmpCtrlPktGap_Object = MibTableColumn
alaIcmpCtrlPktGap = _AlaIcmpCtrlPktGap_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 7, 1, 4),
    _AlaIcmpCtrlPktGap_Type()
)
alaIcmpCtrlPktGap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIcmpCtrlPktGap.setStatus("current")
_AlaIpRouteSumTable_Object = MibTable
alaIpRouteSumTable = _AlaIpRouteSumTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 9)
)
if mibBuilder.loadTexts:
    alaIpRouteSumTable.setStatus("current")
_AlaIpRouteSumEntry_Object = MibTableRow
alaIpRouteSumEntry = _AlaIpRouteSumEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 9, 1)
)
alaIpRouteSumEntry.setIndexNames(
    (0, "ALCATEL-IND1-IP-MIB", "alaIpRouteProtocol"),
)
if mibBuilder.loadTexts:
    alaIpRouteSumEntry.setStatus("current")


class _AlaIpRouteProtocol_Type(Integer32):
    """Custom type alaIpRouteProtocol based on Integer32"""
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
        *(("bgp", 7),
          ("isis", 5),
          ("local", 2),
          ("netmgmt", 3),
          ("ospf", 6),
          ("other", 8),
          ("rip", 4),
          ("total", 1))
    )


_AlaIpRouteProtocol_Type.__name__ = "Integer32"
_AlaIpRouteProtocol_Object = MibTableColumn
alaIpRouteProtocol = _AlaIpRouteProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 9, 1, 1),
    _AlaIpRouteProtocol_Type()
)
alaIpRouteProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpRouteProtocol.setStatus("current")
_AlaIpRouteCount_Type = Integer32
_AlaIpRouteCount_Object = MibTableColumn
alaIpRouteCount = _AlaIpRouteCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 9, 1, 2),
    _AlaIpRouteCount_Type()
)
alaIpRouteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpRouteCount.setStatus("current")
_AlaIcmpCtrl_ObjectIdentity = ObjectIdentity
alaIcmpCtrl = _AlaIcmpCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 10)
)


class _AlaIcmpAllMsgStatus_Type(Integer32):
    """Custom type alaIcmpAllMsgStatus based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 1),
          ("other", 3))
    )


_AlaIcmpAllMsgStatus_Type.__name__ = "Integer32"
_AlaIcmpAllMsgStatus_Object = MibScalar
alaIcmpAllMsgStatus = _AlaIcmpAllMsgStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 10, 1),
    _AlaIcmpAllMsgStatus_Type()
)
alaIcmpAllMsgStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIcmpAllMsgStatus.setStatus("current")
_AlaIpArpFilterTable_Object = MibTable
alaIpArpFilterTable = _AlaIpArpFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 11)
)
if mibBuilder.loadTexts:
    alaIpArpFilterTable.setStatus("current")
_AlaIpArpFilterEntry_Object = MibTableRow
alaIpArpFilterEntry = _AlaIpArpFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 11, 1)
)
alaIpArpFilterEntry.setIndexNames(
    (0, "ALCATEL-IND1-IP-MIB", "alaIpArpFilterIpAddr"),
    (0, "ALCATEL-IND1-IP-MIB", "alaIpArpFilterIpMask"),
    (0, "ALCATEL-IND1-IP-MIB", "alaIpArpFilterVlan"),
    (0, "ALCATEL-IND1-IP-MIB", "alaIpArpFilterType"),
)
if mibBuilder.loadTexts:
    alaIpArpFilterEntry.setStatus("current")
_AlaIpArpFilterIpAddr_Type = IpAddress
_AlaIpArpFilterIpAddr_Object = MibTableColumn
alaIpArpFilterIpAddr = _AlaIpArpFilterIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 11, 1, 1),
    _AlaIpArpFilterIpAddr_Type()
)
alaIpArpFilterIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpArpFilterIpAddr.setStatus("current")
_AlaIpArpFilterIpMask_Type = IpAddress
_AlaIpArpFilterIpMask_Object = MibTableColumn
alaIpArpFilterIpMask = _AlaIpArpFilterIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 11, 1, 2),
    _AlaIpArpFilterIpMask_Type()
)
alaIpArpFilterIpMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpArpFilterIpMask.setStatus("current")


class _AlaIpArpFilterVlan_Type(Integer32):
    """Custom type alaIpArpFilterVlan based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AlaIpArpFilterVlan_Type.__name__ = "Integer32"
_AlaIpArpFilterVlan_Object = MibTableColumn
alaIpArpFilterVlan = _AlaIpArpFilterVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 11, 1, 3),
    _AlaIpArpFilterVlan_Type()
)
alaIpArpFilterVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpArpFilterVlan.setStatus("current")


class _AlaIpArpFilterType_Type(Integer32):
    """Custom type alaIpArpFilterType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sender", 2),
          ("target", 1))
    )


_AlaIpArpFilterType_Type.__name__ = "Integer32"
_AlaIpArpFilterType_Object = MibTableColumn
alaIpArpFilterType = _AlaIpArpFilterType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 11, 1, 4),
    _AlaIpArpFilterType_Type()
)
alaIpArpFilterType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpArpFilterType.setStatus("current")


class _AlaIpArpFilterMode_Type(Integer32):
    """Custom type alaIpArpFilterMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("block", 2))
    )


_AlaIpArpFilterMode_Type.__name__ = "Integer32"
_AlaIpArpFilterMode_Object = MibTableColumn
alaIpArpFilterMode = _AlaIpArpFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 11, 1, 5),
    _AlaIpArpFilterMode_Type()
)
alaIpArpFilterMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIpArpFilterMode.setStatus("current")
_AlaIpArpFilterRowStatus_Type = RowStatus
_AlaIpArpFilterRowStatus_Object = MibTableColumn
alaIpArpFilterRowStatus = _AlaIpArpFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 11, 1, 6),
    _AlaIpArpFilterRowStatus_Type()
)
alaIpArpFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIpArpFilterRowStatus.setStatus("current")
_AlaIpServiceTable_Object = MibTable
alaIpServiceTable = _AlaIpServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 12)
)
if mibBuilder.loadTexts:
    alaIpServiceTable.setStatus("current")
_AlaIpServiceEntry_Object = MibTableRow
alaIpServiceEntry = _AlaIpServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 12, 1)
)
alaIpServiceEntry.setIndexNames(
    (0, "ALCATEL-IND1-IP-MIB", "alaIpServiceType"),
)
if mibBuilder.loadTexts:
    alaIpServiceEntry.setStatus("current")


class _AlaIpServiceType_Type(Integer32):
    """Custom type alaIpServiceType based on Integer32"""
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
        *(("ftp", 1),
          ("http", 4),
          ("https", 7),
          ("ntp", 5),
          ("snmp", 6),
          ("ssh", 2),
          ("telnet", 3))
    )


_AlaIpServiceType_Type.__name__ = "Integer32"
_AlaIpServiceType_Object = MibTableColumn
alaIpServiceType = _AlaIpServiceType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 12, 1, 1),
    _AlaIpServiceType_Type()
)
alaIpServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpServiceType.setStatus("current")


class _AlaIpServicePort_Type(Integer32):
    """Custom type alaIpServicePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AlaIpServicePort_Type.__name__ = "Integer32"
_AlaIpServicePort_Object = MibTableColumn
alaIpServicePort = _AlaIpServicePort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 12, 1, 2),
    _AlaIpServicePort_Type()
)
alaIpServicePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpServicePort.setStatus("current")


class _AlaIpServiceStatus_Type(Integer32):
    """Custom type alaIpServiceStatus based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 1),
          ("other", 3))
    )


_AlaIpServiceStatus_Type.__name__ = "Integer32"
_AlaIpServiceStatus_Object = MibTableColumn
alaIpServiceStatus = _AlaIpServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 12, 1, 3),
    _AlaIpServiceStatus_Type()
)
alaIpServiceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpServiceStatus.setStatus("current")
_AlaIpPortServiceTable_Object = MibTable
alaIpPortServiceTable = _AlaIpPortServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 13)
)
if mibBuilder.loadTexts:
    alaIpPortServiceTable.setStatus("current")
_AlaIpPortServiceEntry_Object = MibTableRow
alaIpPortServiceEntry = _AlaIpPortServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 13, 1)
)
alaIpPortServiceEntry.setIndexNames(
    (0, "ALCATEL-IND1-IP-MIB", "alaIpPortServicePort"),
)
if mibBuilder.loadTexts:
    alaIpPortServiceEntry.setStatus("current")


class _AlaIpPortServicePort_Type(Integer32):
    """Custom type alaIpPortServicePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AlaIpPortServicePort_Type.__name__ = "Integer32"
_AlaIpPortServicePort_Object = MibTableColumn
alaIpPortServicePort = _AlaIpPortServicePort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 13, 1, 1),
    _AlaIpPortServicePort_Type()
)
alaIpPortServicePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpPortServicePort.setStatus("current")


class _AlaIpPortServiceStatus_Type(Integer32):
    """Custom type alaIpPortServiceStatus based on Integer32"""
    defaultValue = 1

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


_AlaIpPortServiceStatus_Type.__name__ = "Integer32"
_AlaIpPortServiceStatus_Object = MibTableColumn
alaIpPortServiceStatus = _AlaIpPortServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 13, 1, 2),
    _AlaIpPortServiceStatus_Type()
)
alaIpPortServiceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpPortServiceStatus.setStatus("current")
_AlaIpInterfaceTable_Object = MibTable
alaIpInterfaceTable = _AlaIpInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 14)
)
if mibBuilder.loadTexts:
    alaIpInterfaceTable.setStatus("current")
_AlaIpInterfaceEntry_Object = MibTableRow
alaIpInterfaceEntry = _AlaIpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 14, 1)
)
alaIpInterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    alaIpInterfaceEntry.setStatus("current")


class _AlaIpInterfaceName_Type(SnmpAdminString):
    """Custom type alaIpInterfaceName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaIpInterfaceName_Type.__name__ = "SnmpAdminString"
_AlaIpInterfaceName_Object = MibTableColumn
alaIpInterfaceName = _AlaIpInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 14, 1, 1),
    _AlaIpInterfaceName_Type()
)
alaIpInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpInterfaceName.setStatus("current")


class _AlaIpInterfaceAddress_Type(IpAddress):
    """Custom type alaIpInterfaceAddress based on IpAddress"""
    defaultHexValue = "00000000"


_AlaIpInterfaceAddress_Object = MibTableColumn
alaIpInterfaceAddress = _AlaIpInterfaceAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 14, 1, 2),
    _AlaIpInterfaceAddress_Type()
)
alaIpInterfaceAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpInterfaceAddress.setStatus("current")


class _AlaIpInterfaceMask_Type(IpAddress):
    """Custom type alaIpInterfaceMask based on IpAddress"""
    defaultHexValue = "00000000"


_AlaIpInterfaceMask_Object = MibTableColumn
alaIpInterfaceMask = _AlaIpInterfaceMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 14, 1, 3),
    _AlaIpInterfaceMask_Type()
)
alaIpInterfaceMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpInterfaceMask.setStatus("current")


class _AlaIpInterfaceAdminState_Type(Integer32):
    """Custom type alaIpInterfaceAdminState based on Integer32"""
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


_AlaIpInterfaceAdminState_Type.__name__ = "Integer32"
_AlaIpInterfaceAdminState_Object = MibTableColumn
alaIpInterfaceAdminState = _AlaIpInterfaceAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 14, 1, 4),
    _AlaIpInterfaceAdminState_Type()
)
alaIpInterfaceAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpInterfaceAdminState.setStatus("current")


class _AlaIpInterfaceDeviceType_Type(Integer32):
    """Custom type alaIpInterfaceDeviceType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("emp", 2),
          ("greTunnel", 4),
          ("ipipTunnel", 5),
          ("loopback", 3),
          ("unbound", 0),
          ("vlan", 1))
    )


_AlaIpInterfaceDeviceType_Type.__name__ = "Integer32"
_AlaIpInterfaceDeviceType_Object = MibTableColumn
alaIpInterfaceDeviceType = _AlaIpInterfaceDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 14, 1, 5),
    _AlaIpInterfaceDeviceType_Type()
)
alaIpInterfaceDeviceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpInterfaceDeviceType.setStatus("current")


class _AlaIpInterfaceVlanID_Type(Integer32):
    """Custom type alaIpInterfaceVlanID based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AlaIpInterfaceVlanID_Type.__name__ = "Integer32"
_AlaIpInterfaceVlanID_Object = MibTableColumn
alaIpInterfaceVlanID = _AlaIpInterfaceVlanID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 14, 1, 6),
    _AlaIpInterfaceVlanID_Type()
)
alaIpInterfaceVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpInterfaceVlanID.setStatus("current")


class _AlaIpInterfaceIpForward_Type(Integer32):
    """Custom type alaIpInterfaceIpForward based on Integer32"""
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


_AlaIpInterfaceIpForward_Type.__name__ = "Integer32"
_AlaIpInterfaceIpForward_Object = MibTableColumn
alaIpInterfaceIpForward = _AlaIpInterfaceIpForward_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 14, 1, 7),
    _AlaIpInterfaceIpForward_Type()
)
alaIpInterfaceIpForward.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpInterfaceIpForward.setStatus("current")


class _AlaIpInterfaceEncap_Type(Integer32):
    """Custom type alaIpInterfaceEncap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernet2", 1),
          ("snap", 2))
    )


_AlaIpInterfaceEncap_Type.__name__ = "Integer32"
_AlaIpInterfaceEncap_Object = MibTableColumn
alaIpInterfaceEncap = _AlaIpInterfaceEncap_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 14, 1, 8),
    _AlaIpInterfaceEncap_Type()
)
alaIpInterfaceEncap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpInterfaceEncap.setStatus("current")


class _AlaIpInterfaceMtu_Type(Unsigned32):
    """Custom type alaIpInterfaceMtu based on Unsigned32"""
    defaultValue = 0


_AlaIpInterfaceMtu_Object = MibTableColumn
alaIpInterfaceMtu = _AlaIpInterfaceMtu_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 14, 1, 9),
    _AlaIpInterfaceMtu_Type()
)
alaIpInterfaceMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpInterfaceMtu.setStatus("current")


class _AlaIpInterfaceLocalProxyArp_Type(Integer32):
    """Custom type alaIpInterfaceLocalProxyArp based on Integer32"""
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


_AlaIpInterfaceLocalProxyArp_Type.__name__ = "Integer32"
_AlaIpInterfaceLocalProxyArp_Object = MibTableColumn
alaIpInterfaceLocalProxyArp = _AlaIpInterfaceLocalProxyArp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 14, 1, 10),
    _AlaIpInterfaceLocalProxyArp_Type()
)
alaIpInterfaceLocalProxyArp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpInterfaceLocalProxyArp.setStatus("current")


class _AlaIpInterfacePrimCfg_Type(Integer32):
    """Custom type alaIpInterfacePrimCfg based on Integer32"""
    defaultValue = 0

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


_AlaIpInterfacePrimCfg_Type.__name__ = "Integer32"
_AlaIpInterfacePrimCfg_Object = MibTableColumn
alaIpInterfacePrimCfg = _AlaIpInterfacePrimCfg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 14, 1, 11),
    _AlaIpInterfacePrimCfg_Type()
)
alaIpInterfacePrimCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpInterfacePrimCfg.setStatus("current")


class _AlaIpInterfaceOperState_Type(Integer32):
    """Custom type alaIpInterfaceOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_AlaIpInterfaceOperState_Type.__name__ = "Integer32"
_AlaIpInterfaceOperState_Object = MibTableColumn
alaIpInterfaceOperState = _AlaIpInterfaceOperState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 14, 1, 12),
    _AlaIpInterfaceOperState_Type()
)
alaIpInterfaceOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpInterfaceOperState.setStatus("current")


class _AlaIpInterfaceOperReason_Type(Integer32):
    """Custom type alaIpInterfaceOperReason based on Integer32"""
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
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("adminDown", 1),
          ("deviceDown", 3),
          ("interfaceUp", 0),
          ("noRouterMac", 5),
          ("noSuchDevice", 4),
          ("noVipAddress", 8),
          ("tunnelDstUnreachable", 7),
          ("tunnelSrcInvalid", 6),
          ("unbound", 2))
    )


_AlaIpInterfaceOperReason_Type.__name__ = "Integer32"
_AlaIpInterfaceOperReason_Object = MibTableColumn
alaIpInterfaceOperReason = _AlaIpInterfaceOperReason_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 14, 1, 13),
    _AlaIpInterfaceOperReason_Type()
)
alaIpInterfaceOperReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpInterfaceOperReason.setStatus("current")
_AlaIpInterfaceRouterMac_Type = MacAddress
_AlaIpInterfaceRouterMac_Object = MibTableColumn
alaIpInterfaceRouterMac = _AlaIpInterfaceRouterMac_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 14, 1, 14),
    _AlaIpInterfaceRouterMac_Type()
)
alaIpInterfaceRouterMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpInterfaceRouterMac.setStatus("current")
_AlaIpInterfaceBcastAddr_Type = IpAddress
_AlaIpInterfaceBcastAddr_Object = MibTableColumn
alaIpInterfaceBcastAddr = _AlaIpInterfaceBcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 14, 1, 15),
    _AlaIpInterfaceBcastAddr_Type()
)
alaIpInterfaceBcastAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpInterfaceBcastAddr.setStatus("current")


class _AlaIpInterfacePrimAct_Type(Integer32):
    """Custom type alaIpInterfacePrimAct based on Integer32"""
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


_AlaIpInterfacePrimAct_Type.__name__ = "Integer32"
_AlaIpInterfacePrimAct_Object = MibTableColumn
alaIpInterfacePrimAct = _AlaIpInterfacePrimAct_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 14, 1, 16),
    _AlaIpInterfacePrimAct_Type()
)
alaIpInterfacePrimAct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpInterfacePrimAct.setStatus("current")
_AlaIpInterfaceRemoteAddr_Type = IpAddress
_AlaIpInterfaceRemoteAddr_Object = MibTableColumn
alaIpInterfaceRemoteAddr = _AlaIpInterfaceRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 14, 1, 17),
    _AlaIpInterfaceRemoteAddr_Type()
)
alaIpInterfaceRemoteAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpInterfaceRemoteAddr.setStatus("current")
_AlaIpInterfaceTunnelSrcAddressType_Type = InetAddressType
_AlaIpInterfaceTunnelSrcAddressType_Object = MibTableColumn
alaIpInterfaceTunnelSrcAddressType = _AlaIpInterfaceTunnelSrcAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 14, 1, 18),
    _AlaIpInterfaceTunnelSrcAddressType_Type()
)
alaIpInterfaceTunnelSrcAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpInterfaceTunnelSrcAddressType.setStatus("current")
_AlaIpInterfaceTunnelSrc_Type = InetAddress
_AlaIpInterfaceTunnelSrc_Object = MibTableColumn
alaIpInterfaceTunnelSrc = _AlaIpInterfaceTunnelSrc_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 14, 1, 19),
    _AlaIpInterfaceTunnelSrc_Type()
)
alaIpInterfaceTunnelSrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpInterfaceTunnelSrc.setStatus("current")
_AlaIpInterfaceTunnelDstAddressType_Type = InetAddressType
_AlaIpInterfaceTunnelDstAddressType_Object = MibTableColumn
alaIpInterfaceTunnelDstAddressType = _AlaIpInterfaceTunnelDstAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 14, 1, 20),
    _AlaIpInterfaceTunnelDstAddressType_Type()
)
alaIpInterfaceTunnelDstAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpInterfaceTunnelDstAddressType.setStatus("current")
_AlaIpInterfaceTunnelDst_Type = InetAddress
_AlaIpInterfaceTunnelDst_Object = MibTableColumn
alaIpInterfaceTunnelDst = _AlaIpInterfaceTunnelDst_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 14, 1, 21),
    _AlaIpInterfaceTunnelDst_Type()
)
alaIpInterfaceTunnelDst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpInterfaceTunnelDst.setStatus("current")


class _AlaIpInterfaceVipAddress_Type(IpAddress):
    """Custom type alaIpInterfaceVipAddress based on IpAddress"""
    defaultHexValue = "00000000"


_AlaIpInterfaceVipAddress_Object = MibTableColumn
alaIpInterfaceVipAddress = _AlaIpInterfaceVipAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 14, 1, 22),
    _AlaIpInterfaceVipAddress_Type()
)
alaIpInterfaceVipAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpInterfaceVipAddress.setStatus("current")


class _AlaIpInterfaceDhcpStatus_Type(Integer32):
    """Custom type alaIpInterfaceDhcpStatus based on Integer32"""
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
        *(("active", 2),
          ("discovery", 1),
          ("timeout", 3))
    )


_AlaIpInterfaceDhcpStatus_Type.__name__ = "Integer32"
_AlaIpInterfaceDhcpStatus_Object = MibTableColumn
alaIpInterfaceDhcpStatus = _AlaIpInterfaceDhcpStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 14, 1, 23),
    _AlaIpInterfaceDhcpStatus_Type()
)
alaIpInterfaceDhcpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpInterfaceDhcpStatus.setStatus("current")


class _AlaIpInterfaceDhcpIpRelease_Type(Integer32):
    """Custom type alaIpInterfaceDhcpIpRelease based on Integer32"""
    defaultValue = 2

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


_AlaIpInterfaceDhcpIpRelease_Type.__name__ = "Integer32"
_AlaIpInterfaceDhcpIpRelease_Object = MibTableColumn
alaIpInterfaceDhcpIpRelease = _AlaIpInterfaceDhcpIpRelease_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 14, 1, 24),
    _AlaIpInterfaceDhcpIpRelease_Type()
)
alaIpInterfaceDhcpIpRelease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpInterfaceDhcpIpRelease.setStatus("current")


class _AlaIpInterfaceDhcpIpRenew_Type(Integer32):
    """Custom type alaIpInterfaceDhcpIpRenew based on Integer32"""
    defaultValue = 2

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


_AlaIpInterfaceDhcpIpRenew_Type.__name__ = "Integer32"
_AlaIpInterfaceDhcpIpRenew_Object = MibTableColumn
alaIpInterfaceDhcpIpRenew = _AlaIpInterfaceDhcpIpRenew_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 14, 1, 25),
    _AlaIpInterfaceDhcpIpRenew_Type()
)
alaIpInterfaceDhcpIpRenew.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpInterfaceDhcpIpRenew.setStatus("current")


class _AlaIpInterfaceDhcpOption60String_Type(SnmpAdminString):
    """Custom type alaIpInterfaceDhcpOption60String based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_AlaIpInterfaceDhcpOption60String_Type.__name__ = "SnmpAdminString"
_AlaIpInterfaceDhcpOption60String_Object = MibTableColumn
alaIpInterfaceDhcpOption60String = _AlaIpInterfaceDhcpOption60String_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 14, 1, 26),
    _AlaIpInterfaceDhcpOption60String_Type()
)
alaIpInterfaceDhcpOption60String.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpInterfaceDhcpOption60String.setStatus("current")
_AlaIpItfConfigTable_Object = MibTable
alaIpItfConfigTable = _AlaIpItfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 15)
)
if mibBuilder.loadTexts:
    alaIpItfConfigTable.setStatus("current")
_AlaIpItfConfigEntry_Object = MibTableRow
alaIpItfConfigEntry = _AlaIpItfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 15, 1)
)
alaIpItfConfigEntry.setIndexNames(
    (0, "ALCATEL-IND1-IP-MIB", "alaIpItfConfigName"),
)
if mibBuilder.loadTexts:
    alaIpItfConfigEntry.setStatus("current")


class _AlaIpItfConfigName_Type(SnmpAdminString):
    """Custom type alaIpItfConfigName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaIpItfConfigName_Type.__name__ = "SnmpAdminString"
_AlaIpItfConfigName_Object = MibTableColumn
alaIpItfConfigName = _AlaIpItfConfigName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 15, 1, 1),
    _AlaIpItfConfigName_Type()
)
alaIpItfConfigName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpItfConfigName.setStatus("current")
_AlaIpItfConfigIfIndex_Type = InterfaceIndexOrZero
_AlaIpItfConfigIfIndex_Object = MibTableColumn
alaIpItfConfigIfIndex = _AlaIpItfConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 15, 1, 2),
    _AlaIpItfConfigIfIndex_Type()
)
alaIpItfConfigIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIpItfConfigIfIndex.setStatus("current")
_AlaIpItfConfigRowStatus_Type = RowStatus
_AlaIpItfConfigRowStatus_Object = MibTableColumn
alaIpItfConfigRowStatus = _AlaIpItfConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 15, 1, 3),
    _AlaIpItfConfigRowStatus_Type()
)
alaIpItfConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIpItfConfigRowStatus.setStatus("current")
_AlaIpFtpConfig_ObjectIdentity = ObjectIdentity
alaIpFtpConfig = _AlaIpFtpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 16)
)


class _AlaIpFtpAdminStatus_Type(Integer32):
    """Custom type alaIpFtpAdminStatus based on Integer32"""
    defaultValue = 1

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


_AlaIpFtpAdminStatus_Type.__name__ = "Integer32"
_AlaIpFtpAdminStatus_Object = MibScalar
alaIpFtpAdminStatus = _AlaIpFtpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 16, 1),
    _AlaIpFtpAdminStatus_Type()
)
alaIpFtpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpFtpAdminStatus.setStatus("current")


class _AlaIpFtpPort_Type(Integer32):
    """Custom type alaIpFtpPort based on Integer32"""
    defaultValue = 21

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(21, 21),
        ValueRangeConstraint(1024, 65535),
    )


_AlaIpFtpPort_Type.__name__ = "Integer32"
_AlaIpFtpPort_Object = MibScalar
alaIpFtpPort = _AlaIpFtpPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 16, 2),
    _AlaIpFtpPort_Type()
)
alaIpFtpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpFtpPort.setStatus("current")
_AlaIpSshConfig_ObjectIdentity = ObjectIdentity
alaIpSshConfig = _AlaIpSshConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 17)
)


class _AlaIpSshAdminStatus_Type(Integer32):
    """Custom type alaIpSshAdminStatus based on Integer32"""
    defaultValue = 1

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


_AlaIpSshAdminStatus_Type.__name__ = "Integer32"
_AlaIpSshAdminStatus_Object = MibScalar
alaIpSshAdminStatus = _AlaIpSshAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 17, 1),
    _AlaIpSshAdminStatus_Type()
)
alaIpSshAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpSshAdminStatus.setStatus("current")


class _AlaIpSshPort_Type(Integer32):
    """Custom type alaIpSshPort based on Integer32"""
    defaultValue = 22

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(22, 22),
        ValueRangeConstraint(1024, 65535),
    )


_AlaIpSshPort_Type.__name__ = "Integer32"
_AlaIpSshPort_Object = MibScalar
alaIpSshPort = _AlaIpSshPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 17, 2),
    _AlaIpSshPort_Type()
)
alaIpSshPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpSshPort.setStatus("current")


class _AlaIpSshPubKeyEnforceAdminStatus_Type(Integer32):
    """Custom type alaIpSshPubKeyEnforceAdminStatus based on Integer32"""
    defaultValue = 2

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


_AlaIpSshPubKeyEnforceAdminStatus_Type.__name__ = "Integer32"
_AlaIpSshPubKeyEnforceAdminStatus_Object = MibScalar
alaIpSshPubKeyEnforceAdminStatus = _AlaIpSshPubKeyEnforceAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 17, 3),
    _AlaIpSshPubKeyEnforceAdminStatus_Type()
)
alaIpSshPubKeyEnforceAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpSshPubKeyEnforceAdminStatus.setStatus("current")
_AlaIpTelnetConfig_ObjectIdentity = ObjectIdentity
alaIpTelnetConfig = _AlaIpTelnetConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 18)
)


class _AlaIpTelnetAdminStatus_Type(Integer32):
    """Custom type alaIpTelnetAdminStatus based on Integer32"""
    defaultValue = 1

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


_AlaIpTelnetAdminStatus_Type.__name__ = "Integer32"
_AlaIpTelnetAdminStatus_Object = MibScalar
alaIpTelnetAdminStatus = _AlaIpTelnetAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 18, 1),
    _AlaIpTelnetAdminStatus_Type()
)
alaIpTelnetAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpTelnetAdminStatus.setStatus("current")


class _AlaIpTelnetPort_Type(Integer32):
    """Custom type alaIpTelnetPort based on Integer32"""
    defaultValue = 23

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(23, 23),
        ValueRangeConstraint(1024, 65535),
    )


_AlaIpTelnetPort_Type.__name__ = "Integer32"
_AlaIpTelnetPort_Object = MibScalar
alaIpTelnetPort = _AlaIpTelnetPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 18, 2),
    _AlaIpTelnetPort_Type()
)
alaIpTelnetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpTelnetPort.setStatus("current")
_AlaIpDhcpHostIdentifierObjects_ObjectIdentity = ObjectIdentity
alaIpDhcpHostIdentifierObjects = _AlaIpDhcpHostIdentifierObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 19)
)
_AlaIpDhcpServerAddressType_Type = InetAddressType
_AlaIpDhcpServerAddressType_Object = MibScalar
alaIpDhcpServerAddressType = _AlaIpDhcpServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 19, 1),
    _AlaIpDhcpServerAddressType_Type()
)
alaIpDhcpServerAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpDhcpServerAddressType.setStatus("current")
_AlaIpDhcpServerAddress_Type = InetAddress
_AlaIpDhcpServerAddress_Object = MibScalar
alaIpDhcpServerAddress = _AlaIpDhcpServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 19, 2),
    _AlaIpDhcpServerAddress_Type()
)
alaIpDhcpServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpDhcpServerAddress.setStatus("current")
_AlaIpDhcpRouterAddressType_Type = InetAddressType
_AlaIpDhcpRouterAddressType_Object = MibScalar
alaIpDhcpRouterAddressType = _AlaIpDhcpRouterAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 19, 3),
    _AlaIpDhcpRouterAddressType_Type()
)
alaIpDhcpRouterAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpDhcpRouterAddressType.setStatus("current")
_AlaIpDhcpRouterAddress_Type = InetAddress
_AlaIpDhcpRouterAddress_Object = MibScalar
alaIpDhcpRouterAddress = _AlaIpDhcpRouterAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 19, 4),
    _AlaIpDhcpRouterAddress_Type()
)
alaIpDhcpRouterAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpDhcpRouterAddress.setStatus("current")


class _AlaIpDhcpHostName_Type(SnmpAdminString):
    """Custom type alaIpDhcpHostName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_AlaIpDhcpHostName_Type.__name__ = "SnmpAdminString"
_AlaIpDhcpHostName_Object = MibScalar
alaIpDhcpHostName = _AlaIpDhcpHostName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 19, 5),
    _AlaIpDhcpHostName_Type()
)
alaIpDhcpHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpDhcpHostName.setStatus("current")
_AlaIpDhcpClientLeaseObtained_Type = TimeStamp
_AlaIpDhcpClientLeaseObtained_Object = MibScalar
alaIpDhcpClientLeaseObtained = _AlaIpDhcpClientLeaseObtained_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 19, 6),
    _AlaIpDhcpClientLeaseObtained_Type()
)
alaIpDhcpClientLeaseObtained.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpDhcpClientLeaseObtained.setStatus("current")
_AlaIpDhcpClientLeaseExpires_Type = TimeStamp
_AlaIpDhcpClientLeaseExpires_Object = MibScalar
alaIpDhcpClientLeaseExpires = _AlaIpDhcpClientLeaseExpires_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 19, 7),
    _AlaIpDhcpClientLeaseExpires_Type()
)
alaIpDhcpClientLeaseExpires.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpDhcpClientLeaseExpires.setStatus("current")
_AlaIpNtpConfig_ObjectIdentity = ObjectIdentity
alaIpNtpConfig = _AlaIpNtpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 20)
)


class _AlaIpNtpVrfName_Type(SnmpAdminString):
    """Custom type alaIpNtpVrfName based on SnmpAdminString"""
    defaultValue = OctetString("default")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AlaIpNtpVrfName_Type.__name__ = "SnmpAdminString"
_AlaIpNtpVrfName_Object = MibScalar
alaIpNtpVrfName = _AlaIpNtpVrfName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 20, 1),
    _AlaIpNtpVrfName_Type()
)
alaIpNtpVrfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpNtpVrfName.setStatus("current")
_AlcatelIND1IPMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1IPMIBConformance = _AlcatelIND1IPMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 2)
)
_AlcatelIND1IPMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1IPMIBCompliances = _AlcatelIND1IPMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 2, 1)
)
_AlcatelIND1IPMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1IPMIBGroups = _AlcatelIND1IPMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 2, 2)
)
ipNetToMediaEntry.registerAugmentions(
    ("ALCATEL-IND1-IP-MIB",
     "ipNetToMediaAugEntry")
)
ipNetToMediaAugEntry.setIndexNames(*ipNetToMediaEntry.getIndexNames())
ipCidrRouteEntry.registerAugmentions(
    ("ALCATEL-IND1-IP-MIB",
     "ipCidrRouteAugEntry")
)
ipCidrRouteAugEntry.setIndexNames(*ipCidrRouteEntry.getIndexNames())

# Managed Objects groups

alaIpConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 2, 2, 1)
)
alaIpConfigGroup.setObjects(
      *(("ALCATEL-IND1-IP-MIB", "alaIpClearArpCache"),
        ("ALCATEL-IND1-IP-MIB", "alaIpDirectedBroadcast"),
        ("ALCATEL-IND1-IP-MIB", "alaIpClearArpFilter"))
)
if mibBuilder.loadTexts:
    alaIpConfigGroup.setStatus("current")

alaIpNetToMediaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 2, 2, 2)
)
alaIpNetToMediaGroup.setObjects(
      *(("ALCATEL-IND1-IP-MIB", "alaIpNetToMediaPhysAddress"),
        ("ALCATEL-IND1-IP-MIB", "alaIpNetToMediaProxy"),
        ("ALCATEL-IND1-IP-MIB", "alaIpNetToMediaVrrp"),
        ("ALCATEL-IND1-IP-MIB", "alaIpNetToMediaAuth"),
        ("ALCATEL-IND1-IP-MIB", "alaIpNetToMediaName"))
)
if mibBuilder.loadTexts:
    alaIpNetToMediaGroup.setStatus("current")

alaDoSGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 2, 2, 3)
)
alaDoSGroup.setObjects(
      *(("ALCATEL-IND1-IP-MIB", "alaDoSType"),
        ("ALCATEL-IND1-IP-MIB", "alaDoSDetected"),
        ("ALCATEL-IND1-IP-MIB", "alaDoSIp"),
        ("ALCATEL-IND1-IP-MIB", "alaDoSMac"),
        ("ALCATEL-IND1-IP-MIB", "alaDoSSlot"),
        ("ALCATEL-IND1-IP-MIB", "alaDoSPort"),
        ("ALCATEL-IND1-IP-MIB", "alaDoSStatus"),
        ("ALCATEL-IND1-IP-MIB", "alaDoSChassisId"))
)
if mibBuilder.loadTexts:
    alaDoSGroup.setStatus("current")

alaPortScanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 2, 2, 4)
)
alaPortScanGroup.setObjects(
      *(("ALCATEL-IND1-IP-MIB", "alaDoSPortScanClosePortPenalty"),
        ("ALCATEL-IND1-IP-MIB", "alaDoSPortScanTcpOpenPortPenalty"),
        ("ALCATEL-IND1-IP-MIB", "alaDoSPortScanUdpOpenPortPenalty"),
        ("ALCATEL-IND1-IP-MIB", "alaDoSPortScanTotalPenalty"),
        ("ALCATEL-IND1-IP-MIB", "alaDoSPortScanThreshold"),
        ("ALCATEL-IND1-IP-MIB", "alaDoSPortScanDecay"),
        ("ALCATEL-IND1-IP-MIB", "alaDoSTrapCntl"))
)
if mibBuilder.loadTexts:
    alaPortScanGroup.setStatus("current")

alaArpPingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 2, 2, 5)
)
alaArpPingGroup.setObjects(
      *(("ALCATEL-IND1-IP-MIB", "alaDoSARPRate"),
        ("ALCATEL-IND1-IP-MIB", "alaDoSPingRate"))
)
if mibBuilder.loadTexts:
    alaArpPingGroup.setStatus("current")

alaArpPoisonGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 2, 2, 6)
)
alaArpPoisonGroup.setObjects(
      *(("ALCATEL-IND1-IP-MIB", "alaDoSArpPoisonDetected"),
        ("ALCATEL-IND1-IP-MIB", "alaDoSArpPoisonRowStatus"))
)
if mibBuilder.loadTexts:
    alaArpPoisonGroup.setStatus("current")

alaIpNetToMediaAugGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 2, 2, 7)
)
alaIpNetToMediaAugGroup.setObjects(
      *(("ALCATEL-IND1-IP-MIB", "ipNetToMediaSlot"),
        ("ALCATEL-IND1-IP-MIB", "ipNetToMediaPort"),
        ("ALCATEL-IND1-IP-MIB", "ipNetToMediaName"),
        ("ALCATEL-IND1-IP-MIB", "ipNetToMediaChassisId"))
)
if mibBuilder.loadTexts:
    alaIpNetToMediaAugGroup.setStatus("current")

alaPktDropGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 2, 2, 8)
)
alaPktDropGroup.setObjects(
      *(("ALCATEL-IND1-IP-MIB", "pktDropType"),
        ("ALCATEL-IND1-IP-MIB", "pktDropIfIndex"),
        ("ALCATEL-IND1-IP-MIB", "pktDropCount"),
        ("ALCATEL-IND1-IP-MIB", "pktDropFrag"))
)
if mibBuilder.loadTexts:
    alaPktDropGroup.setStatus("current")

alaIpCidrAugGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 2, 2, 9)
)
alaIpCidrAugGroup.setObjects(
    ("ALCATEL-IND1-IP-MIB", "ipCidrRouteScope")
)
if mibBuilder.loadTexts:
    alaIpCidrAugGroup.setStatus("current")

alaIcmpCtrlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 2, 2, 10)
)
alaIcmpCtrlGroup.setObjects(
      *(("ALCATEL-IND1-IP-MIB", "alaIcmpCtrlType"),
        ("ALCATEL-IND1-IP-MIB", "alaIcmpCtrlCode"),
        ("ALCATEL-IND1-IP-MIB", "alaIcmpCtrlStatus"),
        ("ALCATEL-IND1-IP-MIB", "alaIcmpCtrlPktGap"),
        ("ALCATEL-IND1-IP-MIB", "alaIcmpAllMsgStatus"))
)
if mibBuilder.loadTexts:
    alaIcmpCtrlGroup.setStatus("current")

alaIpRouteSumGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 2, 2, 11)
)
alaIpRouteSumGroup.setObjects(
      *(("ALCATEL-IND1-IP-MIB", "alaIpRouteProtocol"),
        ("ALCATEL-IND1-IP-MIB", "alaIpRouteCount"))
)
if mibBuilder.loadTexts:
    alaIpRouteSumGroup.setStatus("current")

alaIpArpFilterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 2, 2, 12)
)
alaIpArpFilterGroup.setObjects(
      *(("ALCATEL-IND1-IP-MIB", "alaIpArpFilterMode"),
        ("ALCATEL-IND1-IP-MIB", "alaIpArpFilterRowStatus"))
)
if mibBuilder.loadTexts:
    alaIpArpFilterGroup.setStatus("current")

alaIpServiceTypeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 2, 2, 13)
)
alaIpServiceTypeGroup.setObjects(
      *(("ALCATEL-IND1-IP-MIB", "alaIpServiceType"),
        ("ALCATEL-IND1-IP-MIB", "alaIpServicePort"),
        ("ALCATEL-IND1-IP-MIB", "alaIpServiceStatus"))
)
if mibBuilder.loadTexts:
    alaIpServiceTypeGroup.setStatus("current")

alaIpPortServiceTypeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 2, 2, 14)
)
alaIpPortServiceTypeGroup.setObjects(
      *(("ALCATEL-IND1-IP-MIB", "alaIpPortServicePort"),
        ("ALCATEL-IND1-IP-MIB", "alaIpPortServiceStatus"))
)
if mibBuilder.loadTexts:
    alaIpPortServiceTypeGroup.setStatus("current")

alaIpInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 2, 2, 15)
)
alaIpInterfaceGroup.setObjects(
      *(("ALCATEL-IND1-IP-MIB", "alaIpInterfaceName"),
        ("ALCATEL-IND1-IP-MIB", "alaIpInterfaceAddress"),
        ("ALCATEL-IND1-IP-MIB", "alaIpInterfaceMask"),
        ("ALCATEL-IND1-IP-MIB", "alaIpInterfaceAdminState"),
        ("ALCATEL-IND1-IP-MIB", "alaIpInterfaceDeviceType"),
        ("ALCATEL-IND1-IP-MIB", "alaIpInterfaceVlanID"),
        ("ALCATEL-IND1-IP-MIB", "alaIpInterfaceIpForward"),
        ("ALCATEL-IND1-IP-MIB", "alaIpInterfaceEncap"),
        ("ALCATEL-IND1-IP-MIB", "alaIpInterfaceMtu"),
        ("ALCATEL-IND1-IP-MIB", "alaIpInterfaceLocalProxyArp"),
        ("ALCATEL-IND1-IP-MIB", "alaIpInterfacePrimCfg"),
        ("ALCATEL-IND1-IP-MIB", "alaIpInterfaceOperState"),
        ("ALCATEL-IND1-IP-MIB", "alaIpInterfaceOperReason"),
        ("ALCATEL-IND1-IP-MIB", "alaIpInterfaceRouterMac"),
        ("ALCATEL-IND1-IP-MIB", "alaIpInterfaceBcastAddr"),
        ("ALCATEL-IND1-IP-MIB", "alaIpInterfacePrimAct"),
        ("ALCATEL-IND1-IP-MIB", "alaIpInterfaceRemoteAddr"),
        ("ALCATEL-IND1-IP-MIB", "alaIpInterfaceTunnelSrcAddressType"),
        ("ALCATEL-IND1-IP-MIB", "alaIpInterfaceTunnelSrc"),
        ("ALCATEL-IND1-IP-MIB", "alaIpInterfaceTunnelDstAddressType"),
        ("ALCATEL-IND1-IP-MIB", "alaIpInterfaceTunnelDst"),
        ("ALCATEL-IND1-IP-MIB", "alaIpInterfaceVipAddress"),
        ("ALCATEL-IND1-IP-MIB", "alaIpInterfaceDhcpStatus"),
        ("ALCATEL-IND1-IP-MIB", "alaIpInterfaceDhcpIpRelease"),
        ("ALCATEL-IND1-IP-MIB", "alaIpInterfaceDhcpIpRenew"),
        ("ALCATEL-IND1-IP-MIB", "alaIpInterfaceDhcpOption60String"))
)
if mibBuilder.loadTexts:
    alaIpInterfaceGroup.setStatus("current")

alaIpItfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 2, 2, 16)
)
alaIpItfGroup.setObjects(
      *(("ALCATEL-IND1-IP-MIB", "alaIpItfConfigName"),
        ("ALCATEL-IND1-IP-MIB", "alaIpItfConfigIfIndex"),
        ("ALCATEL-IND1-IP-MIB", "alaIpItfConfigRowStatus"))
)
if mibBuilder.loadTexts:
    alaIpItfGroup.setStatus("current")

alaIpFtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 2, 2, 17)
)
alaIpFtpGroup.setObjects(
      *(("ALCATEL-IND1-IP-MIB", "alaIpFtpAdminStatus"),
        ("ALCATEL-IND1-IP-MIB", "alaIpFtpPort"))
)
if mibBuilder.loadTexts:
    alaIpFtpGroup.setStatus("current")

alaIpSshGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 2, 2, 18)
)
alaIpSshGroup.setObjects(
      *(("ALCATEL-IND1-IP-MIB", "alaIpSshAdminStatus"),
        ("ALCATEL-IND1-IP-MIB", "alaIpSshPort"),
        ("ALCATEL-IND1-IP-MIB", "alaIpSshPubKeyEnforceAdminStatus"))
)
if mibBuilder.loadTexts:
    alaIpSshGroup.setStatus("current")

alaIpTelnetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 2, 2, 19)
)
alaIpTelnetGroup.setObjects(
      *(("ALCATEL-IND1-IP-MIB", "alaIpTelnetAdminStatus"),
        ("ALCATEL-IND1-IP-MIB", "alaIpTelnetPort"))
)
if mibBuilder.loadTexts:
    alaIpTelnetGroup.setStatus("current")

alaIpDhcpHostIdentifierGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 2, 2, 21)
)
alaIpDhcpHostIdentifierGroup.setObjects(
      *(("ALCATEL-IND1-IP-MIB", "alaIpDhcpServerAddressType"),
        ("ALCATEL-IND1-IP-MIB", "alaIpDhcpServerAddress"),
        ("ALCATEL-IND1-IP-MIB", "alaIpDhcpRouterAddressType"),
        ("ALCATEL-IND1-IP-MIB", "alaIpDhcpRouterAddress"),
        ("ALCATEL-IND1-IP-MIB", "alaIpDhcpHostName"),
        ("ALCATEL-IND1-IP-MIB", "alaIpDhcpClientLeaseObtained"),
        ("ALCATEL-IND1-IP-MIB", "alaIpDhcpClientLeaseExpires"))
)
if mibBuilder.loadTexts:
    alaIpDhcpHostIdentifierGroup.setStatus("current")

alaIpNtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 2, 2, 22)
)
alaIpNtpGroup.setObjects(
    ("ALCATEL-IND1-IP-MIB", "alaIpNtpVrfName")
)
if mibBuilder.loadTexts:
    alaIpNtpGroup.setStatus("current")


# Notification objects

alaDoSTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 0, 1)
)
alaDoSTrap.setObjects(
      *(("ALCATEL-IND1-IP-MIB", "alaDoSType"),
        ("ALCATEL-IND1-IP-MIB", "alaDoSDetected"),
        ("ALCATEL-IND1-IP-MIB", "alaDoSIp"),
        ("ALCATEL-IND1-IP-MIB", "alaDoSMac"),
        ("ALCATEL-IND1-IP-MIB", "alaDoSSlot"),
        ("ALCATEL-IND1-IP-MIB", "alaDoSPort"),
        ("ALCATEL-IND1-IP-MIB", "alaDoSChassisId"))
)
if mibBuilder.loadTexts:
    alaDoSTrap.setStatus(
        "current"
    )

pktDrop = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 0, 2)
)
pktDrop.setObjects(
      *(("ALCATEL-IND1-IP-MIB", "pktDropType"),
        ("ALCATEL-IND1-IP-MIB", "pktDropIfIndex"),
        ("ALCATEL-IND1-IP-MIB", "pktDropCount"),
        ("ALCATEL-IND1-IP-MIB", "pktDropFrag"))
)
if mibBuilder.loadTexts:
    pktDrop.setStatus(
        "current"
    )


# Notifications groups

alaIpNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 2, 2, 20)
)
alaIpNotificationGroup.setObjects(
      *(("ALCATEL-IND1-IP-MIB", "alaDoSTrap"),
        ("ALCATEL-IND1-IP-MIB", "pktDrop"))
)
if mibBuilder.loadTexts:
    alaIpNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alaIpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    alaIpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-IP-MIB",
    **{"alcatelIND1IPMIB": alcatelIND1IPMIB,
       "alcatelIND1IPMIBNotifications": alcatelIND1IPMIBNotifications,
       "alaDoSTrap": alaDoSTrap,
       "pktDrop": pktDrop,
       "alcatelIND1IPMIBObjects": alcatelIND1IPMIBObjects,
       "alaIpConfig": alaIpConfig,
       "alaIpClearArpCache": alaIpClearArpCache,
       "alaIpDirectedBroadcast": alaIpDirectedBroadcast,
       "alaIpClearArpFilter": alaIpClearArpFilter,
       "alaIpNetToMediaTable": alaIpNetToMediaTable,
       "alaIpNetToMediaEntry": alaIpNetToMediaEntry,
       "alaIpNetToMediaPhysAddress": alaIpNetToMediaPhysAddress,
       "alaIpNetToMediaProxy": alaIpNetToMediaProxy,
       "alaIpNetToMediaVrrp": alaIpNetToMediaVrrp,
       "alaIpNetToMediaAuth": alaIpNetToMediaAuth,
       "alaIpNetToMediaName": alaIpNetToMediaName,
       "alaDoSConfig": alaDoSConfig,
       "alaDoSTable": alaDoSTable,
       "alaDoSEntry": alaDoSEntry,
       "alaDoSType": alaDoSType,
       "alaDoSDetected": alaDoSDetected,
       "alaDoSIp": alaDoSIp,
       "alaDoSMac": alaDoSMac,
       "alaDoSSlot": alaDoSSlot,
       "alaDoSPort": alaDoSPort,
       "alaDoSStatus": alaDoSStatus,
       "alaDoSChassisId": alaDoSChassisId,
       "alaDoSPortScanClosePortPenalty": alaDoSPortScanClosePortPenalty,
       "alaDoSPortScanTcpOpenPortPenalty": alaDoSPortScanTcpOpenPortPenalty,
       "alaDoSPortScanUdpOpenPortPenalty": alaDoSPortScanUdpOpenPortPenalty,
       "alaDoSPortScanTotalPenalty": alaDoSPortScanTotalPenalty,
       "alaDoSPortScanThreshold": alaDoSPortScanThreshold,
       "alaDoSPortScanDecay": alaDoSPortScanDecay,
       "alaDoSTrapCntl": alaDoSTrapCntl,
       "alaDoSARPRate": alaDoSARPRate,
       "alaDoSPingRate": alaDoSPingRate,
       "alaDoSArpPoisonTable": alaDoSArpPoisonTable,
       "alaDoSArpPoisonEntry": alaDoSArpPoisonEntry,
       "alaDoSArpPoisonIpAddr": alaDoSArpPoisonIpAddr,
       "alaDoSArpPoisonDetected": alaDoSArpPoisonDetected,
       "alaDoSArpPoisonRowStatus": alaDoSArpPoisonRowStatus,
       "ipNetToMediaAugTable": ipNetToMediaAugTable,
       "ipNetToMediaAugEntry": ipNetToMediaAugEntry,
       "ipNetToMediaSlot": ipNetToMediaSlot,
       "ipNetToMediaPort": ipNetToMediaPort,
       "ipNetToMediaName": ipNetToMediaName,
       "ipNetToMediaChassisId": ipNetToMediaChassisId,
       "trafficEventTrapObjs": trafficEventTrapObjs,
       "pktDropType": pktDropType,
       "pktDropIfIndex": pktDropIfIndex,
       "pktDropCount": pktDropCount,
       "pktDropFrag": pktDropFrag,
       "ipCidrRouteAugTable": ipCidrRouteAugTable,
       "ipCidrRouteAugEntry": ipCidrRouteAugEntry,
       "ipCidrRouteScope": ipCidrRouteScope,
       "alaIcmpCtrlTable": alaIcmpCtrlTable,
       "alaIcmpCtrlEntry": alaIcmpCtrlEntry,
       "alaIcmpCtrlType": alaIcmpCtrlType,
       "alaIcmpCtrlCode": alaIcmpCtrlCode,
       "alaIcmpCtrlStatus": alaIcmpCtrlStatus,
       "alaIcmpCtrlPktGap": alaIcmpCtrlPktGap,
       "alaIpRouteSumTable": alaIpRouteSumTable,
       "alaIpRouteSumEntry": alaIpRouteSumEntry,
       "alaIpRouteProtocol": alaIpRouteProtocol,
       "alaIpRouteCount": alaIpRouteCount,
       "alaIcmpCtrl": alaIcmpCtrl,
       "alaIcmpAllMsgStatus": alaIcmpAllMsgStatus,
       "alaIpArpFilterTable": alaIpArpFilterTable,
       "alaIpArpFilterEntry": alaIpArpFilterEntry,
       "alaIpArpFilterIpAddr": alaIpArpFilterIpAddr,
       "alaIpArpFilterIpMask": alaIpArpFilterIpMask,
       "alaIpArpFilterVlan": alaIpArpFilterVlan,
       "alaIpArpFilterType": alaIpArpFilterType,
       "alaIpArpFilterMode": alaIpArpFilterMode,
       "alaIpArpFilterRowStatus": alaIpArpFilterRowStatus,
       "alaIpServiceTable": alaIpServiceTable,
       "alaIpServiceEntry": alaIpServiceEntry,
       "alaIpServiceType": alaIpServiceType,
       "alaIpServicePort": alaIpServicePort,
       "alaIpServiceStatus": alaIpServiceStatus,
       "alaIpPortServiceTable": alaIpPortServiceTable,
       "alaIpPortServiceEntry": alaIpPortServiceEntry,
       "alaIpPortServicePort": alaIpPortServicePort,
       "alaIpPortServiceStatus": alaIpPortServiceStatus,
       "alaIpInterfaceTable": alaIpInterfaceTable,
       "alaIpInterfaceEntry": alaIpInterfaceEntry,
       "alaIpInterfaceName": alaIpInterfaceName,
       "alaIpInterfaceAddress": alaIpInterfaceAddress,
       "alaIpInterfaceMask": alaIpInterfaceMask,
       "alaIpInterfaceAdminState": alaIpInterfaceAdminState,
       "alaIpInterfaceDeviceType": alaIpInterfaceDeviceType,
       "alaIpInterfaceVlanID": alaIpInterfaceVlanID,
       "alaIpInterfaceIpForward": alaIpInterfaceIpForward,
       "alaIpInterfaceEncap": alaIpInterfaceEncap,
       "alaIpInterfaceMtu": alaIpInterfaceMtu,
       "alaIpInterfaceLocalProxyArp": alaIpInterfaceLocalProxyArp,
       "alaIpInterfacePrimCfg": alaIpInterfacePrimCfg,
       "alaIpInterfaceOperState": alaIpInterfaceOperState,
       "alaIpInterfaceOperReason": alaIpInterfaceOperReason,
       "alaIpInterfaceRouterMac": alaIpInterfaceRouterMac,
       "alaIpInterfaceBcastAddr": alaIpInterfaceBcastAddr,
       "alaIpInterfacePrimAct": alaIpInterfacePrimAct,
       "alaIpInterfaceRemoteAddr": alaIpInterfaceRemoteAddr,
       "alaIpInterfaceTunnelSrcAddressType": alaIpInterfaceTunnelSrcAddressType,
       "alaIpInterfaceTunnelSrc": alaIpInterfaceTunnelSrc,
       "alaIpInterfaceTunnelDstAddressType": alaIpInterfaceTunnelDstAddressType,
       "alaIpInterfaceTunnelDst": alaIpInterfaceTunnelDst,
       "alaIpInterfaceVipAddress": alaIpInterfaceVipAddress,
       "alaIpInterfaceDhcpStatus": alaIpInterfaceDhcpStatus,
       "alaIpInterfaceDhcpIpRelease": alaIpInterfaceDhcpIpRelease,
       "alaIpInterfaceDhcpIpRenew": alaIpInterfaceDhcpIpRenew,
       "alaIpInterfaceDhcpOption60String": alaIpInterfaceDhcpOption60String,
       "alaIpItfConfigTable": alaIpItfConfigTable,
       "alaIpItfConfigEntry": alaIpItfConfigEntry,
       "alaIpItfConfigName": alaIpItfConfigName,
       "alaIpItfConfigIfIndex": alaIpItfConfigIfIndex,
       "alaIpItfConfigRowStatus": alaIpItfConfigRowStatus,
       "alaIpFtpConfig": alaIpFtpConfig,
       "alaIpFtpAdminStatus": alaIpFtpAdminStatus,
       "alaIpFtpPort": alaIpFtpPort,
       "alaIpSshConfig": alaIpSshConfig,
       "alaIpSshAdminStatus": alaIpSshAdminStatus,
       "alaIpSshPort": alaIpSshPort,
       "alaIpSshPubKeyEnforceAdminStatus": alaIpSshPubKeyEnforceAdminStatus,
       "alaIpTelnetConfig": alaIpTelnetConfig,
       "alaIpTelnetAdminStatus": alaIpTelnetAdminStatus,
       "alaIpTelnetPort": alaIpTelnetPort,
       "alaIpDhcpHostIdentifierObjects": alaIpDhcpHostIdentifierObjects,
       "alaIpDhcpServerAddressType": alaIpDhcpServerAddressType,
       "alaIpDhcpServerAddress": alaIpDhcpServerAddress,
       "alaIpDhcpRouterAddressType": alaIpDhcpRouterAddressType,
       "alaIpDhcpRouterAddress": alaIpDhcpRouterAddress,
       "alaIpDhcpHostName": alaIpDhcpHostName,
       "alaIpDhcpClientLeaseObtained": alaIpDhcpClientLeaseObtained,
       "alaIpDhcpClientLeaseExpires": alaIpDhcpClientLeaseExpires,
       "alaIpNtpConfig": alaIpNtpConfig,
       "alaIpNtpVrfName": alaIpNtpVrfName,
       "alcatelIND1IPMIBConformance": alcatelIND1IPMIBConformance,
       "alcatelIND1IPMIBCompliances": alcatelIND1IPMIBCompliances,
       "alaIpCompliance": alaIpCompliance,
       "alcatelIND1IPMIBGroups": alcatelIND1IPMIBGroups,
       "alaIpConfigGroup": alaIpConfigGroup,
       "alaIpNetToMediaGroup": alaIpNetToMediaGroup,
       "alaDoSGroup": alaDoSGroup,
       "alaPortScanGroup": alaPortScanGroup,
       "alaArpPingGroup": alaArpPingGroup,
       "alaArpPoisonGroup": alaArpPoisonGroup,
       "alaIpNetToMediaAugGroup": alaIpNetToMediaAugGroup,
       "alaPktDropGroup": alaPktDropGroup,
       "alaIpCidrAugGroup": alaIpCidrAugGroup,
       "alaIcmpCtrlGroup": alaIcmpCtrlGroup,
       "alaIpRouteSumGroup": alaIpRouteSumGroup,
       "alaIpArpFilterGroup": alaIpArpFilterGroup,
       "alaIpServiceTypeGroup": alaIpServiceTypeGroup,
       "alaIpPortServiceTypeGroup": alaIpPortServiceTypeGroup,
       "alaIpInterfaceGroup": alaIpInterfaceGroup,
       "alaIpItfGroup": alaIpItfGroup,
       "alaIpFtpGroup": alaIpFtpGroup,
       "alaIpSshGroup": alaIpSshGroup,
       "alaIpTelnetGroup": alaIpTelnetGroup,
       "alaIpNotificationGroup": alaIpNotificationGroup,
       "alaIpDhcpHostIdentifierGroup": alaIpDhcpHostIdentifierGroup,
       "alaIpNtpGroup": alaIpNtpGroup}
)
