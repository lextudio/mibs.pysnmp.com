# SNMP MIB module (HUAWEI-ISIS-CONF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-ISIS-CONF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:04:13 2024
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

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

(ifName,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifName")

(isisAdjState,
 isisCircIfIndex,
 isisPduLspId,
 isisSysInstance,
 isisSysLevelIndex) = mibBuilder.importSymbols(
    "ISIS-MIB",
    "isisAdjState",
    "isisCircIfIndex",
    "isisPduLspId",
    "isisSysInstance",
    "isisSysLevelIndex")

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

hwISIS = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24)
)
hwISIS.setRevisions(
        ("2015-10-15 11:00",
         "2015-08-27 19:00",
         "2015-04-08 11:47",
         "2015-03-13 09:00",
         "2014-11-06 15:18",
         "2014-01-15 17:10",
         "2013-08-08 11:31",
         "2013-04-01 11:53",
         "2003-08-11 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SystemID(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )



class InetAddress(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class InetAddressType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              16)
        )
    )
    namedValues = NamedValues(
        *(("dns", 16),
          ("ipv4", 1),
          ("ipv4z", 3),
          ("ipv6", 2),
          ("ipv6z", 4),
          ("unknown", 0))
    )



class InetAddressPrefixLength(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2040),
    )



# MIB Managed Objects in the order of their OIDs

_HwIsisConf_ObjectIdentity = ObjectIdentity
hwIsisConf = _HwIsisConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2)
)
_HwIsisMIBObjects_ObjectIdentity = ObjectIdentity
hwIsisMIBObjects = _HwIsisMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1)
)
_HwIsisProcBaseTable_Object = MibTable
hwIsisProcBaseTable = _HwIsisProcBaseTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hwIsisProcBaseTable.setStatus("current")
_HwIsisProcBaseEntry_Object = MibTableRow
hwIsisProcBaseEntry = _HwIsisProcBaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 1, 1)
)
hwIsisProcBaseEntry.setIndexNames(
    (0, "HUAWEI-ISIS-CONF-MIB", "hwIsisProcIdIndex"),
)
if mibBuilder.loadTexts:
    hwIsisProcBaseEntry.setStatus("current")


class _HwIsisProcIdIndex_Type(Integer32):
    """Custom type hwIsisProcIdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwIsisProcIdIndex_Type.__name__ = "Integer32"
_HwIsisProcIdIndex_Object = MibTableColumn
hwIsisProcIdIndex = _HwIsisProcIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 1, 1, 1),
    _HwIsisProcIdIndex_Type()
)
hwIsisProcIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIsisProcIdIndex.setStatus("current")


class _HwIsisProcVpnName_Type(OctetString):
    """Custom type hwIsisProcVpnName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwIsisProcVpnName_Type.__name__ = "OctetString"
_HwIsisProcVpnName_Object = MibTableColumn
hwIsisProcVpnName = _HwIsisProcVpnName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 1, 1, 2),
    _HwIsisProcVpnName_Type()
)
hwIsisProcVpnName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisProcVpnName.setStatus("current")


class _HwIsisProcVpn6Name_Type(OctetString):
    """Custom type hwIsisProcVpn6Name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwIsisProcVpn6Name_Type.__name__ = "OctetString"
_HwIsisProcVpn6Name_Object = MibTableColumn
hwIsisProcVpn6Name = _HwIsisProcVpn6Name_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 1, 1, 3),
    _HwIsisProcVpn6Name_Type()
)
hwIsisProcVpn6Name.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisProcVpn6Name.setStatus("obsolete")


class _HwIsisProcAreaAuthType_Type(Integer32):
    """Custom type hwIsisProcAreaAuthType based on Integer32"""
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
        *(("keychain", 3),
          ("md5", 1),
          ("null", 0),
          ("simple", 2))
    )


_HwIsisProcAreaAuthType_Type.__name__ = "Integer32"
_HwIsisProcAreaAuthType_Object = MibTableColumn
hwIsisProcAreaAuthType = _HwIsisProcAreaAuthType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 1, 1, 4),
    _HwIsisProcAreaAuthType_Type()
)
hwIsisProcAreaAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisProcAreaAuthType.setStatus("current")


class _HwIsisProcAreaAuthPasswordName_Type(OctetString):
    """Custom type hwIsisProcAreaAuthPasswordName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 392),
    )


_HwIsisProcAreaAuthPasswordName_Type.__name__ = "OctetString"
_HwIsisProcAreaAuthPasswordName_Object = MibTableColumn
hwIsisProcAreaAuthPasswordName = _HwIsisProcAreaAuthPasswordName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 1, 1, 5),
    _HwIsisProcAreaAuthPasswordName_Type()
)
hwIsisProcAreaAuthPasswordName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisProcAreaAuthPasswordName.setStatus("current")


class _HwIsisProcAreaAuthPacketAuthMode_Type(Integer32):
    """Custom type hwIsisProcAreaAuthPacketAuthMode based on Integer32"""
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
        *(("allsendonly", 2),
          ("authenticateall", 1),
          ("none", 0),
          ("snppacketauthenticationavoid", 3),
          ("snppacketsendonly", 4))
    )


_HwIsisProcAreaAuthPacketAuthMode_Type.__name__ = "Integer32"
_HwIsisProcAreaAuthPacketAuthMode_Object = MibTableColumn
hwIsisProcAreaAuthPacketAuthMode = _HwIsisProcAreaAuthPacketAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 1, 1, 6),
    _HwIsisProcAreaAuthPacketAuthMode_Type()
)
hwIsisProcAreaAuthPacketAuthMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisProcAreaAuthPacketAuthMode.setStatus("current")


class _HwIsisProcAreaAuthCode_Type(Integer32):
    """Custom type hwIsisProcAreaAuthCode based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              10,
              133)
        )
    )
    namedValues = NamedValues(
        *(("ip", 133),
          ("none", 0),
          ("osi", 10))
    )


_HwIsisProcAreaAuthCode_Type.__name__ = "Integer32"
_HwIsisProcAreaAuthCode_Object = MibTableColumn
hwIsisProcAreaAuthCode = _HwIsisProcAreaAuthCode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 1, 1, 7),
    _HwIsisProcAreaAuthCode_Type()
)
hwIsisProcAreaAuthCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisProcAreaAuthCode.setStatus("current")


class _HwIsisProcDomainAuthType_Type(Integer32):
    """Custom type hwIsisProcDomainAuthType based on Integer32"""
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
        *(("keychain", 3),
          ("md5", 1),
          ("null", 0),
          ("simple", 2))
    )


_HwIsisProcDomainAuthType_Type.__name__ = "Integer32"
_HwIsisProcDomainAuthType_Object = MibTableColumn
hwIsisProcDomainAuthType = _HwIsisProcDomainAuthType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 1, 1, 8),
    _HwIsisProcDomainAuthType_Type()
)
hwIsisProcDomainAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisProcDomainAuthType.setStatus("current")


class _HwIsisProcDomainAuthPasswordName_Type(OctetString):
    """Custom type hwIsisProcDomainAuthPasswordName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 392),
    )


_HwIsisProcDomainAuthPasswordName_Type.__name__ = "OctetString"
_HwIsisProcDomainAuthPasswordName_Object = MibTableColumn
hwIsisProcDomainAuthPasswordName = _HwIsisProcDomainAuthPasswordName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 1, 1, 9),
    _HwIsisProcDomainAuthPasswordName_Type()
)
hwIsisProcDomainAuthPasswordName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisProcDomainAuthPasswordName.setStatus("current")


class _HwIsisProcDomainAuthPacketAuthMode_Type(Integer32):
    """Custom type hwIsisProcDomainAuthPacketAuthMode based on Integer32"""
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
        *(("allsendonly", 2),
          ("authenticateall", 1),
          ("none", 0),
          ("snppacketauthenticationavoid", 3),
          ("snppacketsendonly", 4))
    )


_HwIsisProcDomainAuthPacketAuthMode_Type.__name__ = "Integer32"
_HwIsisProcDomainAuthPacketAuthMode_Object = MibTableColumn
hwIsisProcDomainAuthPacketAuthMode = _HwIsisProcDomainAuthPacketAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 1, 1, 10),
    _HwIsisProcDomainAuthPacketAuthMode_Type()
)
hwIsisProcDomainAuthPacketAuthMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisProcDomainAuthPacketAuthMode.setStatus("current")


class _HwIsisProcDomainAuthCode_Type(Integer32):
    """Custom type hwIsisProcDomainAuthCode based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              10,
              133)
        )
    )
    namedValues = NamedValues(
        *(("ip", 133),
          ("none", 0),
          ("osi", 10))
    )


_HwIsisProcDomainAuthCode_Type.__name__ = "Integer32"
_HwIsisProcDomainAuthCode_Object = MibTableColumn
hwIsisProcDomainAuthCode = _HwIsisProcDomainAuthCode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 1, 1, 11),
    _HwIsisProcDomainAuthCode_Type()
)
hwIsisProcDomainAuthCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisProcDomainAuthCode.setStatus("current")


class _HwIsisProcLevel_Type(Integer32):
    """Custom type hwIsisProcLevel based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("level1", 1),
          ("level12", 3),
          ("level2", 2))
    )


_HwIsisProcLevel_Type.__name__ = "Integer32"
_HwIsisProcLevel_Object = MibTableColumn
hwIsisProcLevel = _HwIsisProcLevel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 1, 1, 12),
    _HwIsisProcLevel_Type()
)
hwIsisProcLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisProcLevel.setStatus("current")


class _HwIsisProcL1FlashFloodCount_Type(Integer32):
    """Custom type hwIsisProcL1FlashFloodCount based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_HwIsisProcL1FlashFloodCount_Type.__name__ = "Integer32"
_HwIsisProcL1FlashFloodCount_Object = MibTableColumn
hwIsisProcL1FlashFloodCount = _HwIsisProcL1FlashFloodCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 1, 1, 13),
    _HwIsisProcL1FlashFloodCount_Type()
)
hwIsisProcL1FlashFloodCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisProcL1FlashFloodCount.setStatus("current")


class _HwIsisProcL1FlashFloodInterval_Type(Integer32):
    """Custom type hwIsisProcL1FlashFloodInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 50000),
    )


_HwIsisProcL1FlashFloodInterval_Type.__name__ = "Integer32"
_HwIsisProcL1FlashFloodInterval_Object = MibTableColumn
hwIsisProcL1FlashFloodInterval = _HwIsisProcL1FlashFloodInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 1, 1, 14),
    _HwIsisProcL1FlashFloodInterval_Type()
)
hwIsisProcL1FlashFloodInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisProcL1FlashFloodInterval.setStatus("current")
if mibBuilder.loadTexts:
    hwIsisProcL1FlashFloodInterval.setUnits("millionseconds")


class _HwIsisProcL2FlashFloodCount_Type(Integer32):
    """Custom type hwIsisProcL2FlashFloodCount based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_HwIsisProcL2FlashFloodCount_Type.__name__ = "Integer32"
_HwIsisProcL2FlashFloodCount_Object = MibTableColumn
hwIsisProcL2FlashFloodCount = _HwIsisProcL2FlashFloodCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 1, 1, 15),
    _HwIsisProcL2FlashFloodCount_Type()
)
hwIsisProcL2FlashFloodCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisProcL2FlashFloodCount.setStatus("current")


class _HwIsisProcL2FlashFloodInterval_Type(Integer32):
    """Custom type hwIsisProcL2FlashFloodInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 50000),
    )


_HwIsisProcL2FlashFloodInterval_Type.__name__ = "Integer32"
_HwIsisProcL2FlashFloodInterval_Object = MibTableColumn
hwIsisProcL2FlashFloodInterval = _HwIsisProcL2FlashFloodInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 1, 1, 16),
    _HwIsisProcL2FlashFloodInterval_Type()
)
hwIsisProcL2FlashFloodInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisProcL2FlashFloodInterval.setStatus("current")
if mibBuilder.loadTexts:
    hwIsisProcL2FlashFloodInterval.setUnits("millionseconds")


class _HwIsisProcLogPeerChange_Type(Integer32):
    """Custom type hwIsisProcLogPeerChange based on Integer32"""
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
        *(("enabledwithouttopology", 1),
          ("enabledwithtopology", 2),
          ("null", 0))
    )


_HwIsisProcLogPeerChange_Type.__name__ = "Integer32"
_HwIsisProcLogPeerChange_Object = MibTableColumn
hwIsisProcLogPeerChange = _HwIsisProcLogPeerChange_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 1, 1, 17),
    _HwIsisProcLogPeerChange_Type()
)
hwIsisProcLogPeerChange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisProcLogPeerChange.setStatus("current")


class _HwIsisProcTimerRefresh_Type(Integer32):
    """Custom type hwIsisProcTimerRefresh based on Integer32"""
    defaultValue = 900

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65534),
    )


_HwIsisProcTimerRefresh_Type.__name__ = "Integer32"
_HwIsisProcTimerRefresh_Object = MibTableColumn
hwIsisProcTimerRefresh = _HwIsisProcTimerRefresh_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 1, 1, 18),
    _HwIsisProcTimerRefresh_Type()
)
hwIsisProcTimerRefresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisProcTimerRefresh.setStatus("current")
if mibBuilder.loadTexts:
    hwIsisProcTimerRefresh.setUnits("seconds")


class _HwIsisProcTimerMaxAge_Type(Integer32):
    """Custom type hwIsisProcTimerMaxAge based on Integer32"""
    defaultValue = 1200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 65535),
    )


_HwIsisProcTimerMaxAge_Type.__name__ = "Integer32"
_HwIsisProcTimerMaxAge_Object = MibTableColumn
hwIsisProcTimerMaxAge = _HwIsisProcTimerMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 1, 1, 19),
    _HwIsisProcTimerMaxAge_Type()
)
hwIsisProcTimerMaxAge.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisProcTimerMaxAge.setStatus("current")
if mibBuilder.loadTexts:
    hwIsisProcTimerMaxAge.setUnits("seconds")


class _HwIsisProcL1TimerLspGenMaxInterval_Type(Integer32):
    """Custom type hwIsisProcL1TimerLspGenMaxInterval based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_HwIsisProcL1TimerLspGenMaxInterval_Type.__name__ = "Integer32"
_HwIsisProcL1TimerLspGenMaxInterval_Object = MibTableColumn
hwIsisProcL1TimerLspGenMaxInterval = _HwIsisProcL1TimerLspGenMaxInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 1, 1, 20),
    _HwIsisProcL1TimerLspGenMaxInterval_Type()
)
hwIsisProcL1TimerLspGenMaxInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisProcL1TimerLspGenMaxInterval.setStatus("current")
if mibBuilder.loadTexts:
    hwIsisProcL1TimerLspGenMaxInterval.setUnits("seconds")


class _HwIsisProcL1TimerLspGenInitInterval_Type(Integer32):
    """Custom type hwIsisProcL1TimerLspGenInitInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_HwIsisProcL1TimerLspGenInitInterval_Type.__name__ = "Integer32"
_HwIsisProcL1TimerLspGenInitInterval_Object = MibTableColumn
hwIsisProcL1TimerLspGenInitInterval = _HwIsisProcL1TimerLspGenInitInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 1, 1, 21),
    _HwIsisProcL1TimerLspGenInitInterval_Type()
)
hwIsisProcL1TimerLspGenInitInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisProcL1TimerLspGenInitInterval.setStatus("current")
if mibBuilder.loadTexts:
    hwIsisProcL1TimerLspGenInitInterval.setUnits("millionseconds")


class _HwIsisProcL1TimerLspGenIncrInterval_Type(Integer32):
    """Custom type hwIsisProcL1TimerLspGenIncrInterval based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_HwIsisProcL1TimerLspGenIncrInterval_Type.__name__ = "Integer32"
_HwIsisProcL1TimerLspGenIncrInterval_Object = MibTableColumn
hwIsisProcL1TimerLspGenIncrInterval = _HwIsisProcL1TimerLspGenIncrInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 1, 1, 22),
    _HwIsisProcL1TimerLspGenIncrInterval_Type()
)
hwIsisProcL1TimerLspGenIncrInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisProcL1TimerLspGenIncrInterval.setStatus("current")
if mibBuilder.loadTexts:
    hwIsisProcL1TimerLspGenIncrInterval.setUnits("millionseconds")


class _HwIsisProcL2TimerLspGenMaxInterval_Type(Integer32):
    """Custom type hwIsisProcL2TimerLspGenMaxInterval based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_HwIsisProcL2TimerLspGenMaxInterval_Type.__name__ = "Integer32"
_HwIsisProcL2TimerLspGenMaxInterval_Object = MibTableColumn
hwIsisProcL2TimerLspGenMaxInterval = _HwIsisProcL2TimerLspGenMaxInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 1, 1, 23),
    _HwIsisProcL2TimerLspGenMaxInterval_Type()
)
hwIsisProcL2TimerLspGenMaxInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisProcL2TimerLspGenMaxInterval.setStatus("current")
if mibBuilder.loadTexts:
    hwIsisProcL2TimerLspGenMaxInterval.setUnits("seconds")


class _HwIsisProcL2TimerLspGenInitInterval_Type(Integer32):
    """Custom type hwIsisProcL2TimerLspGenInitInterval based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_HwIsisProcL2TimerLspGenInitInterval_Type.__name__ = "Integer32"
_HwIsisProcL2TimerLspGenInitInterval_Object = MibTableColumn
hwIsisProcL2TimerLspGenInitInterval = _HwIsisProcL2TimerLspGenInitInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 1, 1, 24),
    _HwIsisProcL2TimerLspGenInitInterval_Type()
)
hwIsisProcL2TimerLspGenInitInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisProcL2TimerLspGenInitInterval.setStatus("current")
if mibBuilder.loadTexts:
    hwIsisProcL2TimerLspGenInitInterval.setUnits("millionseconds")


class _HwIsisProcL2TimerLspGenIncrInterval_Type(Integer32):
    """Custom type hwIsisProcL2TimerLspGenIncrInterval based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_HwIsisProcL2TimerLspGenIncrInterval_Type.__name__ = "Integer32"
_HwIsisProcL2TimerLspGenIncrInterval_Object = MibTableColumn
hwIsisProcL2TimerLspGenIncrInterval = _HwIsisProcL2TimerLspGenIncrInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 1, 1, 25),
    _HwIsisProcL2TimerLspGenIncrInterval_Type()
)
hwIsisProcL2TimerLspGenIncrInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisProcL2TimerLspGenIncrInterval.setStatus("current")
if mibBuilder.loadTexts:
    hwIsisProcL2TimerLspGenIncrInterval.setUnits("millionseconds")


class _HwIsisProcTimerSPFMaxInterval_Type(Integer32):
    """Custom type hwIsisProcTimerSPFMaxInterval based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_HwIsisProcTimerSPFMaxInterval_Type.__name__ = "Integer32"
_HwIsisProcTimerSPFMaxInterval_Object = MibTableColumn
hwIsisProcTimerSPFMaxInterval = _HwIsisProcTimerSPFMaxInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 1, 1, 26),
    _HwIsisProcTimerSPFMaxInterval_Type()
)
hwIsisProcTimerSPFMaxInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisProcTimerSPFMaxInterval.setStatus("current")
if mibBuilder.loadTexts:
    hwIsisProcTimerSPFMaxInterval.setUnits("seconds")


class _HwIsisProcTimerSPFInitInterval_Type(Integer32):
    """Custom type hwIsisProcTimerSPFInitInterval based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_HwIsisProcTimerSPFInitInterval_Type.__name__ = "Integer32"
_HwIsisProcTimerSPFInitInterval_Object = MibTableColumn
hwIsisProcTimerSPFInitInterval = _HwIsisProcTimerSPFInitInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 1, 1, 27),
    _HwIsisProcTimerSPFInitInterval_Type()
)
hwIsisProcTimerSPFInitInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisProcTimerSPFInitInterval.setStatus("current")
if mibBuilder.loadTexts:
    hwIsisProcTimerSPFInitInterval.setUnits("millionseconds")


class _HwIsisProcTimerSPFIncrInterval_Type(Integer32):
    """Custom type hwIsisProcTimerSPFIncrInterval based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_HwIsisProcTimerSPFIncrInterval_Type.__name__ = "Integer32"
_HwIsisProcTimerSPFIncrInterval_Object = MibTableColumn
hwIsisProcTimerSPFIncrInterval = _HwIsisProcTimerSPFIncrInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 1, 1, 28),
    _HwIsisProcTimerSPFIncrInterval_Type()
)
hwIsisProcTimerSPFIncrInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisProcTimerSPFIncrInterval.setStatus("current")
if mibBuilder.loadTexts:
    hwIsisProcTimerSPFIncrInterval.setUnits("millionseconds")


class _HwIsisProcCostStyle_Type(Integer32):
    """Custom type hwIsisProcCostStyle based on Integer32"""
    defaultValue = 1

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
        *(("compatible", 3),
          ("compatiblerelax", 7),
          ("narrow", 1),
          ("narrowcompatible", 2),
          ("narrowcompatiblerelax", 6),
          ("wide", 4),
          ("widecompatible", 5))
    )


_HwIsisProcCostStyle_Type.__name__ = "Integer32"
_HwIsisProcCostStyle_Object = MibTableColumn
hwIsisProcCostStyle = _HwIsisProcCostStyle_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 1, 1, 29),
    _HwIsisProcCostStyle_Type()
)
hwIsisProcCostStyle.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisProcCostStyle.setStatus("current")


class _HwIsisProcDynamicName_Type(OctetString):
    """Custom type hwIsisProcDynamicName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwIsisProcDynamicName_Type.__name__ = "OctetString"
_HwIsisProcDynamicName_Object = MibTableColumn
hwIsisProcDynamicName = _HwIsisProcDynamicName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 1, 1, 30),
    _HwIsisProcDynamicName_Type()
)
hwIsisProcDynamicName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisProcDynamicName.setStatus("current")
_HwIsisProcGREnabled_Type = TruthValue
_HwIsisProcGREnabled_Object = MibTableColumn
hwIsisProcGREnabled = _HwIsisProcGREnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 1, 1, 31),
    _HwIsisProcGREnabled_Type()
)
hwIsisProcGREnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisProcGREnabled.setStatus("current")


class _HwIsisProcGRInterval_Type(Integer32):
    """Custom type hwIsisProcGRInterval based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(30, 1800),
    )


_HwIsisProcGRInterval_Type.__name__ = "Integer32"
_HwIsisProcGRInterval_Object = MibTableColumn
hwIsisProcGRInterval = _HwIsisProcGRInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 1, 1, 32),
    _HwIsisProcGRInterval_Type()
)
hwIsisProcGRInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisProcGRInterval.setStatus("current")
if mibBuilder.loadTexts:
    hwIsisProcGRInterval.setUnits("seconds")


class _HwIsisProcGRSuppresSAEnabled_Type(TruthValue):
    """Custom type hwIsisProcGRSuppresSAEnabled based on TruthValue"""


_HwIsisProcGRSuppresSAEnabled_Object = MibTableColumn
hwIsisProcGRSuppresSAEnabled = _HwIsisProcGRSuppresSAEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 1, 1, 33),
    _HwIsisProcGRSuppresSAEnabled_Type()
)
hwIsisProcGRSuppresSAEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisProcGRSuppresSAEnabled.setStatus("current")


class _HwIsisProcTEEnableLevel_Type(Integer32):
    """Custom type hwIsisProcTEEnableLevel based on Integer32"""
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
        *(("level1", 1),
          ("level12", 3),
          ("level2", 2),
          ("none", 0))
    )


_HwIsisProcTEEnableLevel_Type.__name__ = "Integer32"
_HwIsisProcTEEnableLevel_Object = MibTableColumn
hwIsisProcTEEnableLevel = _HwIsisProcTEEnableLevel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 1, 1, 34),
    _HwIsisProcTEEnableLevel_Type()
)
hwIsisProcTEEnableLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisProcTEEnableLevel.setStatus("current")


class _HwIsisProcBFDEnabled_Type(TruthValue):
    """Custom type hwIsisProcBFDEnabled based on TruthValue"""


_HwIsisProcBFDEnabled_Object = MibTableColumn
hwIsisProcBFDEnabled = _HwIsisProcBFDEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 1, 1, 35),
    _HwIsisProcBFDEnabled_Type()
)
hwIsisProcBFDEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisProcBFDEnabled.setStatus("current")


class _HwIsisProcBFDFrrBindEnabled_Type(TruthValue):
    """Custom type hwIsisProcBFDFrrBindEnabled based on TruthValue"""


_HwIsisProcBFDFrrBindEnabled_Object = MibTableColumn
hwIsisProcBFDFrrBindEnabled = _HwIsisProcBFDFrrBindEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 1, 1, 36),
    _HwIsisProcBFDFrrBindEnabled_Type()
)
hwIsisProcBFDFrrBindEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisProcBFDFrrBindEnabled.setStatus("current")


class _HwIsisProcBFDMinTxInterval_Type(Integer32):
    """Custom type hwIsisProcBFDMinTxInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwIsisProcBFDMinTxInterval_Type.__name__ = "Integer32"
_HwIsisProcBFDMinTxInterval_Object = MibTableColumn
hwIsisProcBFDMinTxInterval = _HwIsisProcBFDMinTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 1, 1, 37),
    _HwIsisProcBFDMinTxInterval_Type()
)
hwIsisProcBFDMinTxInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisProcBFDMinTxInterval.setStatus("current")
if mibBuilder.loadTexts:
    hwIsisProcBFDMinTxInterval.setUnits("seconds")


class _HwIsisProcBFDMinRecvInteval_Type(Integer32):
    """Custom type hwIsisProcBFDMinRecvInteval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwIsisProcBFDMinRecvInteval_Type.__name__ = "Integer32"
_HwIsisProcBFDMinRecvInteval_Object = MibTableColumn
hwIsisProcBFDMinRecvInteval = _HwIsisProcBFDMinRecvInteval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 1, 1, 38),
    _HwIsisProcBFDMinRecvInteval_Type()
)
hwIsisProcBFDMinRecvInteval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisProcBFDMinRecvInteval.setStatus("current")
if mibBuilder.loadTexts:
    hwIsisProcBFDMinRecvInteval.setUnits("seconds")


class _HwIsisProcBFDMultiplier_Type(Integer32):
    """Custom type hwIsisProcBFDMultiplier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwIsisProcBFDMultiplier_Type.__name__ = "Integer32"
_HwIsisProcBFDMultiplier_Object = MibTableColumn
hwIsisProcBFDMultiplier = _HwIsisProcBFDMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 1, 1, 39),
    _HwIsisProcBFDMultiplier_Type()
)
hwIsisProcBFDMultiplier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisProcBFDMultiplier.setStatus("current")


class _HwIsisProcIPv6EnableTopologyType_Type(Integer32):
    """Custom type hwIsisProcIPv6EnableTopologyType based on Integer32"""

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
        *(("compatible", 3),
          ("compatibleenablemtspf", 4),
          ("disable", 0),
          ("ipv6", 2),
          ("standard", 1))
    )


_HwIsisProcIPv6EnableTopologyType_Type.__name__ = "Integer32"
_HwIsisProcIPv6EnableTopologyType_Object = MibTableColumn
hwIsisProcIPv6EnableTopologyType = _HwIsisProcIPv6EnableTopologyType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 1, 1, 40),
    _HwIsisProcIPv6EnableTopologyType_Type()
)
hwIsisProcIPv6EnableTopologyType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisProcIPv6EnableTopologyType.setStatus("current")
_HwIsisProcRowStatus_Type = RowStatus
_HwIsisProcRowStatus_Object = MibTableColumn
hwIsisProcRowStatus = _HwIsisProcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 1, 1, 41),
    _HwIsisProcRowStatus_Type()
)
hwIsisProcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisProcRowStatus.setStatus("current")


class _HwIsisProcOptionalChecksumEnabled_Type(TruthValue):
    """Custom type hwIsisProcOptionalChecksumEnabled based on TruthValue"""


_HwIsisProcOptionalChecksumEnabled_Object = MibTableColumn
hwIsisProcOptionalChecksumEnabled = _HwIsisProcOptionalChecksumEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 1, 1, 42),
    _HwIsisProcOptionalChecksumEnabled_Type()
)
hwIsisProcOptionalChecksumEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisProcOptionalChecksumEnabled.setStatus("current")


class _HwisisProcLsdbMaxLimit_Type(Unsigned32):
    """Custom type hwisisProcLsdbMaxLimit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500000),
    )


_HwisisProcLsdbMaxLimit_Type.__name__ = "Unsigned32"
_HwisisProcLsdbMaxLimit_Object = MibTableColumn
hwisisProcLsdbMaxLimit = _HwisisProcLsdbMaxLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 1, 1, 43),
    _HwisisProcLsdbMaxLimit_Type()
)
hwisisProcLsdbMaxLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwisisProcLsdbMaxLimit.setStatus("current")


class _HwIsisProcLsdbUpperThreshold_Type(Unsigned32):
    """Custom type hwIsisProcLsdbUpperThreshold based on Unsigned32"""
    defaultValue = 80

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HwIsisProcLsdbUpperThreshold_Type.__name__ = "Unsigned32"
_HwIsisProcLsdbUpperThreshold_Object = MibTableColumn
hwIsisProcLsdbUpperThreshold = _HwIsisProcLsdbUpperThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 1, 1, 44),
    _HwIsisProcLsdbUpperThreshold_Type()
)
hwIsisProcLsdbUpperThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisProcLsdbUpperThreshold.setStatus("current")


class _HwIsisProcLsdbLowerThreshold_Type(Unsigned32):
    """Custom type hwIsisProcLsdbLowerThreshold based on Unsigned32"""
    defaultValue = 70

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HwIsisProcLsdbLowerThreshold_Type.__name__ = "Unsigned32"
_HwIsisProcLsdbLowerThreshold_Object = MibTableColumn
hwIsisProcLsdbLowerThreshold = _HwIsisProcLsdbLowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 1, 1, 45),
    _HwIsisProcLsdbLowerThreshold_Type()
)
hwIsisProcLsdbLowerThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisProcLsdbLowerThreshold.setStatus("current")


class _HwIsisProcLsdbTotal_Type(Unsigned32):
    """Custom type hwIsisProcLsdbTotal based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwIsisProcLsdbTotal_Type.__name__ = "Unsigned32"
_HwIsisProcLsdbTotal_Object = MibTableColumn
hwIsisProcLsdbTotal = _HwIsisProcLsdbTotal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 1, 1, 46),
    _HwIsisProcLsdbTotal_Type()
)
hwIsisProcLsdbTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIsisProcLsdbTotal.setStatus("current")


class _HwIsisProcAreaAuthKeychainName_Type(OctetString):
    """Custom type hwIsisProcAreaAuthKeychainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_HwIsisProcAreaAuthKeychainName_Type.__name__ = "OctetString"
_HwIsisProcAreaAuthKeychainName_Object = MibTableColumn
hwIsisProcAreaAuthKeychainName = _HwIsisProcAreaAuthKeychainName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 1, 1, 47),
    _HwIsisProcAreaAuthKeychainName_Type()
)
hwIsisProcAreaAuthKeychainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisProcAreaAuthKeychainName.setStatus("current")


class _HwIsisProcDomainAuthKeychainName_Type(OctetString):
    """Custom type hwIsisProcDomainAuthKeychainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_HwIsisProcDomainAuthKeychainName_Type.__name__ = "OctetString"
_HwIsisProcDomainAuthKeychainName_Object = MibTableColumn
hwIsisProcDomainAuthKeychainName = _HwIsisProcDomainAuthKeychainName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 1, 1, 48),
    _HwIsisProcDomainAuthKeychainName_Type()
)
hwIsisProcDomainAuthKeychainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisProcDomainAuthKeychainName.setStatus("current")
_HwIsisNETTable_Object = MibTable
hwIsisNETTable = _HwIsisNETTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 2)
)
if mibBuilder.loadTexts:
    hwIsisNETTable.setStatus("current")
_HwIsisNETEntry_Object = MibTableRow
hwIsisNETEntry = _HwIsisNETEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 2, 1)
)
hwIsisNETEntry.setIndexNames(
    (0, "HUAWEI-ISIS-CONF-MIB", "hwIsisProcIdIndex"),
    (0, "HUAWEI-ISIS-CONF-MIB", "hwIsisNETIndex"),
)
if mibBuilder.loadTexts:
    hwIsisNETEntry.setStatus("current")


class _HwIsisNETIndex_Type(OctetString):
    """Custom type hwIsisNETIndex based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 20),
    )


_HwIsisNETIndex_Type.__name__ = "OctetString"
_HwIsisNETIndex_Object = MibTableColumn
hwIsisNETIndex = _HwIsisNETIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 2, 1, 1),
    _HwIsisNETIndex_Type()
)
hwIsisNETIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIsisNETIndex.setStatus("current")
_HwIsisNETStatus_Type = RowStatus
_HwIsisNETStatus_Object = MibTableColumn
hwIsisNETStatus = _HwIsisNETStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 2, 1, 2),
    _HwIsisNETStatus_Type()
)
hwIsisNETStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisNETStatus.setStatus("current")
_HwIsisProcMTExtTable_Object = MibTable
hwIsisProcMTExtTable = _HwIsisProcMTExtTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 3)
)
if mibBuilder.loadTexts:
    hwIsisProcMTExtTable.setStatus("current")
_HwIsisProcMTExtEntry_Object = MibTableRow
hwIsisProcMTExtEntry = _HwIsisProcMTExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 3, 1)
)
hwIsisProcMTExtEntry.setIndexNames(
    (0, "HUAWEI-ISIS-CONF-MIB", "hwIsisProcIdIndex"),
    (0, "HUAWEI-ISIS-CONF-MIB", "hwIsisIpTypeIndex"),
    (0, "HUAWEI-ISIS-CONF-MIB", "hwIsisMTIdIndex"),
)
if mibBuilder.loadTexts:
    hwIsisProcMTExtEntry.setStatus("current")
_HwIsisIpTypeIndex_Type = InetAddressType
_HwIsisIpTypeIndex_Object = MibTableColumn
hwIsisIpTypeIndex = _HwIsisIpTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 3, 1, 1),
    _HwIsisIpTypeIndex_Type()
)
hwIsisIpTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIsisIpTypeIndex.setStatus("current")


class _HwIsisMTIdIndex_Type(Integer32):
    """Custom type hwIsisMTIdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_HwIsisMTIdIndex_Type.__name__ = "Integer32"
_HwIsisMTIdIndex_Object = MibTableColumn
hwIsisMTIdIndex = _HwIsisMTIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 3, 1, 2),
    _HwIsisMTIdIndex_Type()
)
hwIsisMTIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIsisMTIdIndex.setStatus("current")


class _HwIsisMTName_Type(OctetString):
    """Custom type hwIsisMTName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwIsisMTName_Type.__name__ = "OctetString"
_HwIsisMTName_Object = MibTableColumn
hwIsisMTName = _HwIsisMTName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 3, 1, 3),
    _HwIsisMTName_Type()
)
hwIsisMTName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisMTName.setStatus("current")


class _HwIsisProcDefRoutAdvType_Type(Integer32):
    """Custom type hwIsisProcDefRoutAdvType based on Integer32"""
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
        *(("always", 1),
          ("matchdefault", 2),
          ("null", 0),
          ("routepolicy", 3))
    )


_HwIsisProcDefRoutAdvType_Type.__name__ = "Integer32"
_HwIsisProcDefRoutAdvType_Object = MibTableColumn
hwIsisProcDefRoutAdvType = _HwIsisProcDefRoutAdvType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 3, 1, 4),
    _HwIsisProcDefRoutAdvType_Type()
)
hwIsisProcDefRoutAdvType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisProcDefRoutAdvType.setStatus("current")


class _HwIsisProcDefRoutAdvPolicyName_Type(OctetString):
    """Custom type hwIsisProcDefRoutAdvPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_HwIsisProcDefRoutAdvPolicyName_Type.__name__ = "OctetString"
_HwIsisProcDefRoutAdvPolicyName_Object = MibTableColumn
hwIsisProcDefRoutAdvPolicyName = _HwIsisProcDefRoutAdvPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 3, 1, 5),
    _HwIsisProcDefRoutAdvPolicyName_Type()
)
hwIsisProcDefRoutAdvPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisProcDefRoutAdvPolicyName.setStatus("current")


class _HwIsisProcDefRoutAdvCost_Type(Unsigned32):
    """Custom type hwIsisProcDefRoutAdvCost based on Unsigned32"""
    defaultValue = 0


_HwIsisProcDefRoutAdvCost_Object = MibTableColumn
hwIsisProcDefRoutAdvCost = _HwIsisProcDefRoutAdvCost_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 3, 1, 6),
    _HwIsisProcDefRoutAdvCost_Type()
)
hwIsisProcDefRoutAdvCost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisProcDefRoutAdvCost.setStatus("current")
_HwIsisProcDefRoutAdvTag_Type = Unsigned32
_HwIsisProcDefRoutAdvTag_Object = MibTableColumn
hwIsisProcDefRoutAdvTag = _HwIsisProcDefRoutAdvTag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 3, 1, 7),
    _HwIsisProcDefRoutAdvTag_Type()
)
hwIsisProcDefRoutAdvTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisProcDefRoutAdvTag.setStatus("current")


class _HwIsisProcDefRoutAdvLevel_Type(Integer32):
    """Custom type hwIsisProcDefRoutAdvLevel based on Integer32"""
    defaultValue = 2

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
        *(("level1", 1),
          ("level12", 3),
          ("level2", 2),
          ("null", 0))
    )


_HwIsisProcDefRoutAdvLevel_Type.__name__ = "Integer32"
_HwIsisProcDefRoutAdvLevel_Object = MibTableColumn
hwIsisProcDefRoutAdvLevel = _HwIsisProcDefRoutAdvLevel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 3, 1, 8),
    _HwIsisProcDefRoutAdvLevel_Type()
)
hwIsisProcDefRoutAdvLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisProcDefRoutAdvLevel.setStatus("current")


class _HwIsisProcDefRoutAdvAvoidLearnEnabled_Type(TruthValue):
    """Custom type hwIsisProcDefRoutAdvAvoidLearnEnabled based on TruthValue"""


_HwIsisProcDefRoutAdvAvoidLearnEnabled_Object = MibTableColumn
hwIsisProcDefRoutAdvAvoidLearnEnabled = _HwIsisProcDefRoutAdvAvoidLearnEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 3, 1, 9),
    _HwIsisProcDefRoutAdvAvoidLearnEnabled_Type()
)
hwIsisProcDefRoutAdvAvoidLearnEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisProcDefRoutAdvAvoidLearnEnabled.setStatus("current")


class _HwIsisProcL1CircuitCost_Type(Integer32):
    """Custom type hwIsisProcL1CircuitCost based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_HwIsisProcL1CircuitCost_Type.__name__ = "Integer32"
_HwIsisProcL1CircuitCost_Object = MibTableColumn
hwIsisProcL1CircuitCost = _HwIsisProcL1CircuitCost_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 3, 1, 10),
    _HwIsisProcL1CircuitCost_Type()
)
hwIsisProcL1CircuitCost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisProcL1CircuitCost.setStatus("current")


class _HwIsisProcL2CircuitCost_Type(Integer32):
    """Custom type hwIsisProcL2CircuitCost based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_HwIsisProcL2CircuitCost_Type.__name__ = "Integer32"
_HwIsisProcL2CircuitCost_Object = MibTableColumn
hwIsisProcL2CircuitCost = _HwIsisProcL2CircuitCost_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 3, 1, 11),
    _HwIsisProcL2CircuitCost_Type()
)
hwIsisProcL2CircuitCost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisProcL2CircuitCost.setStatus("current")


class _HwIsisProcPrefValue_Type(Integer32):
    """Custom type hwIsisProcPrefValue based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwIsisProcPrefValue_Type.__name__ = "Integer32"
_HwIsisProcPrefValue_Object = MibTableColumn
hwIsisProcPrefValue = _HwIsisProcPrefValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 3, 1, 12),
    _HwIsisProcPrefValue_Type()
)
hwIsisProcPrefValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisProcPrefValue.setStatus("current")


class _HwIsisProcPrefPolicyName_Type(OctetString):
    """Custom type hwIsisProcPrefPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_HwIsisProcPrefPolicyName_Type.__name__ = "OctetString"
_HwIsisProcPrefPolicyName_Object = MibTableColumn
hwIsisProcPrefPolicyName = _HwIsisProcPrefPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 3, 1, 13),
    _HwIsisProcPrefPolicyName_Type()
)
hwIsisProcPrefPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisProcPrefPolicyName.setStatus("current")


class _HwIsisProcMaxLoadBalance_Type(Integer32):
    """Custom type hwIsisProcMaxLoadBalance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_HwIsisProcMaxLoadBalance_Type.__name__ = "Integer32"
_HwIsisProcMaxLoadBalance_Object = MibTableColumn
hwIsisProcMaxLoadBalance = _HwIsisProcMaxLoadBalance_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 3, 1, 14),
    _HwIsisProcMaxLoadBalance_Type()
)
hwIsisProcMaxLoadBalance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisProcMaxLoadBalance.setStatus("current")
_HwIsisProcL1CircuitDefaultTag_Type = Unsigned32
_HwIsisProcL1CircuitDefaultTag_Object = MibTableColumn
hwIsisProcL1CircuitDefaultTag = _HwIsisProcL1CircuitDefaultTag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 3, 1, 15),
    _HwIsisProcL1CircuitDefaultTag_Type()
)
hwIsisProcL1CircuitDefaultTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisProcL1CircuitDefaultTag.setStatus("current")
_HwIsisProcL2CircuitDefaultTag_Type = Unsigned32
_HwIsisProcL2CircuitDefaultTag_Object = MibTableColumn
hwIsisProcL2CircuitDefaultTag = _HwIsisProcL2CircuitDefaultTag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 3, 1, 16),
    _HwIsisProcL2CircuitDefaultTag_Type()
)
hwIsisProcL2CircuitDefaultTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisProcL2CircuitDefaultTag.setStatus("current")


class _HwIsisProcBandWidthReference_Type(Unsigned32):
    """Custom type hwIsisProcBandWidthReference based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483648),
    )


_HwIsisProcBandWidthReference_Type.__name__ = "Unsigned32"
_HwIsisProcBandWidthReference_Object = MibTableColumn
hwIsisProcBandWidthReference = _HwIsisProcBandWidthReference_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 3, 1, 17),
    _HwIsisProcBandWidthReference_Type()
)
hwIsisProcBandWidthReference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisProcBandWidthReference.setStatus("current")


class _HwIsisProcAutoCostEnabled_Type(TruthValue):
    """Custom type hwIsisProcAutoCostEnabled based on TruthValue"""


_HwIsisProcAutoCostEnabled_Object = MibTableColumn
hwIsisProcAutoCostEnabled = _HwIsisProcAutoCostEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 3, 1, 18),
    _HwIsisProcAutoCostEnabled_Type()
)
hwIsisProcAutoCostEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisProcAutoCostEnabled.setStatus("current")


class _HwIsisProcSetOverLoad_Type(Integer32):
    """Custom type hwIsisProcSetOverLoad based on Integer32"""
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
        *(("disable", 0),
          ("enable", 1),
          ("onstartup", 2))
    )


_HwIsisProcSetOverLoad_Type.__name__ = "Integer32"
_HwIsisProcSetOverLoad_Object = MibTableColumn
hwIsisProcSetOverLoad = _HwIsisProcSetOverLoad_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 3, 1, 19),
    _HwIsisProcSetOverLoad_Type()
)
hwIsisProcSetOverLoad.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisProcSetOverLoad.setStatus("current")


class _HwIsisProcSetOverLoadAllowRoute_Type(Integer32):
    """Custom type hwIsisProcSetOverLoadAllowRoute based on Integer32"""
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
        *(("external", 1),
          ("externalandinterlevel", 3),
          ("interlevel", 2),
          ("null", 0))
    )


_HwIsisProcSetOverLoadAllowRoute_Type.__name__ = "Integer32"
_HwIsisProcSetOverLoadAllowRoute_Object = MibTableColumn
hwIsisProcSetOverLoadAllowRoute = _HwIsisProcSetOverLoadAllowRoute_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 3, 1, 20),
    _HwIsisProcSetOverLoadAllowRoute_Type()
)
hwIsisProcSetOverLoadAllowRoute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisProcSetOverLoadAllowRoute.setStatus("current")


class _HwIsisProcOnStartInterval_Type(Integer32):
    """Custom type hwIsisProcOnStartInterval based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5, 86400),
    )


_HwIsisProcOnStartInterval_Type.__name__ = "Integer32"
_HwIsisProcOnStartInterval_Object = MibTableColumn
hwIsisProcOnStartInterval = _HwIsisProcOnStartInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 3, 1, 21),
    _HwIsisProcOnStartInterval_Type()
)
hwIsisProcOnStartInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisProcOnStartInterval.setStatus("current")
if mibBuilder.loadTexts:
    hwIsisProcOnStartInterval.setUnits("seconds")


class _HwIsisProcOnStartStartFromPeer_Type(OctetString):
    """Custom type hwIsisProcOnStartStartFromPeer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(12, 14),
    )


_HwIsisProcOnStartStartFromPeer_Type.__name__ = "OctetString"
_HwIsisProcOnStartStartFromPeer_Object = MibTableColumn
hwIsisProcOnStartStartFromPeer = _HwIsisProcOnStartStartFromPeer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 3, 1, 22),
    _HwIsisProcOnStartStartFromPeer_Type()
)
hwIsisProcOnStartStartFromPeer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisProcOnStartStartFromPeer.setStatus("current")


class _HwIsisProcOnStartFromPeerInterval_Type(Integer32):
    """Custom type hwIsisProcOnStartFromPeerInterval based on Integer32"""
    defaultValue = 1200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5, 86400),
    )


_HwIsisProcOnStartFromPeerInterval_Type.__name__ = "Integer32"
_HwIsisProcOnStartFromPeerInterval_Object = MibTableColumn
hwIsisProcOnStartFromPeerInterval = _HwIsisProcOnStartFromPeerInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 3, 1, 23),
    _HwIsisProcOnStartFromPeerInterval_Type()
)
hwIsisProcOnStartFromPeerInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisProcOnStartFromPeerInterval.setStatus("current")
if mibBuilder.loadTexts:
    hwIsisProcOnStartFromPeerInterval.setUnits("seconds")


class _HwIsisProcOnStartWaitForBgpEnabled_Type(TruthValue):
    """Custom type hwIsisProcOnStartWaitForBgpEnabled based on TruthValue"""


_HwIsisProcOnStartWaitForBgpEnabled_Object = MibTableColumn
hwIsisProcOnStartWaitForBgpEnabled = _HwIsisProcOnStartWaitForBgpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 3, 1, 24),
    _HwIsisProcOnStartWaitForBgpEnabled_Type()
)
hwIsisProcOnStartWaitForBgpEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisProcOnStartWaitForBgpEnabled.setStatus("current")
_HwIsisProcMTStatus_Type = RowStatus
_HwIsisProcMTStatus_Object = MibTableColumn
hwIsisProcMTStatus = _HwIsisProcMTStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 3, 1, 25),
    _HwIsisProcMTStatus_Type()
)
hwIsisProcMTStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisProcMTStatus.setStatus("current")


class _HwIsisProcL1RedistMaxLimit_Type(Unsigned32):
    """Custom type hwIsisProcL1RedistMaxLimit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_HwIsisProcL1RedistMaxLimit_Type.__name__ = "Unsigned32"
_HwIsisProcL1RedistMaxLimit_Object = MibTableColumn
hwIsisProcL1RedistMaxLimit = _HwIsisProcL1RedistMaxLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 3, 1, 26),
    _HwIsisProcL1RedistMaxLimit_Type()
)
hwIsisProcL1RedistMaxLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisProcL1RedistMaxLimit.setStatus("current")


class _HwIsisProcL2RedistMaxLimit_Type(Unsigned32):
    """Custom type hwIsisProcL2RedistMaxLimit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_HwIsisProcL2RedistMaxLimit_Type.__name__ = "Unsigned32"
_HwIsisProcL2RedistMaxLimit_Object = MibTableColumn
hwIsisProcL2RedistMaxLimit = _HwIsisProcL2RedistMaxLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 3, 1, 27),
    _HwIsisProcL2RedistMaxLimit_Type()
)
hwIsisProcL2RedistMaxLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisProcL2RedistMaxLimit.setStatus("current")


class _HwIsisProcL1UpperRedistThreshold_Type(Unsigned32):
    """Custom type hwIsisProcL1UpperRedistThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HwIsisProcL1UpperRedistThreshold_Type.__name__ = "Unsigned32"
_HwIsisProcL1UpperRedistThreshold_Object = MibTableColumn
hwIsisProcL1UpperRedistThreshold = _HwIsisProcL1UpperRedistThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 3, 1, 28),
    _HwIsisProcL1UpperRedistThreshold_Type()
)
hwIsisProcL1UpperRedistThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisProcL1UpperRedistThreshold.setStatus("current")


class _HwIsisProcL2UpperRedistThreshold_Type(Unsigned32):
    """Custom type hwIsisProcL2UpperRedistThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HwIsisProcL2UpperRedistThreshold_Type.__name__ = "Unsigned32"
_HwIsisProcL2UpperRedistThreshold_Object = MibTableColumn
hwIsisProcL2UpperRedistThreshold = _HwIsisProcL2UpperRedistThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 3, 1, 29),
    _HwIsisProcL2UpperRedistThreshold_Type()
)
hwIsisProcL2UpperRedistThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisProcL2UpperRedistThreshold.setStatus("current")


class _HwIsisProcL1LowerRedistThreshold_Type(Unsigned32):
    """Custom type hwIsisProcL1LowerRedistThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HwIsisProcL1LowerRedistThreshold_Type.__name__ = "Unsigned32"
_HwIsisProcL1LowerRedistThreshold_Object = MibTableColumn
hwIsisProcL1LowerRedistThreshold = _HwIsisProcL1LowerRedistThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 3, 1, 30),
    _HwIsisProcL1LowerRedistThreshold_Type()
)
hwIsisProcL1LowerRedistThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisProcL1LowerRedistThreshold.setStatus("current")


class _HwIsisProcL2LowerRedistThreshold_Type(Unsigned32):
    """Custom type hwIsisProcL2LowerRedistThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HwIsisProcL2LowerRedistThreshold_Type.__name__ = "Unsigned32"
_HwIsisProcL2LowerRedistThreshold_Object = MibTableColumn
hwIsisProcL2LowerRedistThreshold = _HwIsisProcL2LowerRedistThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 3, 1, 31),
    _HwIsisProcL2LowerRedistThreshold_Type()
)
hwIsisProcL2LowerRedistThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisProcL2LowerRedistThreshold.setStatus("current")


class _HwIsisProcL1TotalRedist_Type(Unsigned32):
    """Custom type hwIsisProcL1TotalRedist based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwIsisProcL1TotalRedist_Type.__name__ = "Unsigned32"
_HwIsisProcL1TotalRedist_Object = MibTableColumn
hwIsisProcL1TotalRedist = _HwIsisProcL1TotalRedist_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 3, 1, 32),
    _HwIsisProcL1TotalRedist_Type()
)
hwIsisProcL1TotalRedist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIsisProcL1TotalRedist.setStatus("current")


class _HwIsisProcL2TotalRedist_Type(Unsigned32):
    """Custom type hwIsisProcL2TotalRedist based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwIsisProcL2TotalRedist_Type.__name__ = "Unsigned32"
_HwIsisProcL2TotalRedist_Object = MibTableColumn
hwIsisProcL2TotalRedist = _HwIsisProcL2TotalRedist_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 3, 1, 33),
    _HwIsisProcL2TotalRedist_Type()
)
hwIsisProcL2TotalRedist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIsisProcL2TotalRedist.setStatus("current")
_HwIsisPrefixPriorityTable_Object = MibTable
hwIsisPrefixPriorityTable = _HwIsisPrefixPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 4)
)
if mibBuilder.loadTexts:
    hwIsisPrefixPriorityTable.setStatus("current")
_HwIsisPrefixPriorityEntry_Object = MibTableRow
hwIsisPrefixPriorityEntry = _HwIsisPrefixPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 4, 1)
)
hwIsisPrefixPriorityEntry.setIndexNames(
    (0, "HUAWEI-ISIS-CONF-MIB", "hwIsisProcIdIndex"),
    (0, "HUAWEI-ISIS-CONF-MIB", "hwIsisIpTypeIndex"),
    (0, "HUAWEI-ISIS-CONF-MIB", "hwIsisMTIdIndex"),
    (0, "HUAWEI-ISIS-CONF-MIB", "hwIsisPrefixPriorityTypeIndex"),
)
if mibBuilder.loadTexts:
    hwIsisPrefixPriorityEntry.setStatus("current")


class _HwIsisPrefixPriorityTypeIndex_Type(Integer32):
    """Custom type hwIsisPrefixPriorityTypeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("critical", 3),
          ("high", 2),
          ("medium", 1))
    )


_HwIsisPrefixPriorityTypeIndex_Type.__name__ = "Integer32"
_HwIsisPrefixPriorityTypeIndex_Object = MibTableColumn
hwIsisPrefixPriorityTypeIndex = _HwIsisPrefixPriorityTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 4, 1, 1),
    _HwIsisPrefixPriorityTypeIndex_Type()
)
hwIsisPrefixPriorityTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIsisPrefixPriorityTypeIndex.setStatus("current")


class _HwIsisPrefixPriorityL1PolicyType_Type(Integer32):
    """Custom type hwIsisPrefixPriorityL1PolicyType based on Integer32"""
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
        *(("none", 0),
          ("prefix", 1),
          ("tag", 2))
    )


_HwIsisPrefixPriorityL1PolicyType_Type.__name__ = "Integer32"
_HwIsisPrefixPriorityL1PolicyType_Object = MibTableColumn
hwIsisPrefixPriorityL1PolicyType = _HwIsisPrefixPriorityL1PolicyType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 4, 1, 2),
    _HwIsisPrefixPriorityL1PolicyType_Type()
)
hwIsisPrefixPriorityL1PolicyType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisPrefixPriorityL1PolicyType.setStatus("current")


class _HwIsisPrefixPriorityL2PolicyType_Type(Integer32):
    """Custom type hwIsisPrefixPriorityL2PolicyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("prefix", 1),
          ("tag", 2))
    )


_HwIsisPrefixPriorityL2PolicyType_Type.__name__ = "Integer32"
_HwIsisPrefixPriorityL2PolicyType_Object = MibTableColumn
hwIsisPrefixPriorityL2PolicyType = _HwIsisPrefixPriorityL2PolicyType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 4, 1, 3),
    _HwIsisPrefixPriorityL2PolicyType_Type()
)
hwIsisPrefixPriorityL2PolicyType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisPrefixPriorityL2PolicyType.setStatus("current")


class _HwIsisPrefixPriorityL1IpPrefixName_Type(OctetString):
    """Custom type hwIsisPrefixPriorityL1IpPrefixName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 169),
    )


_HwIsisPrefixPriorityL1IpPrefixName_Type.__name__ = "OctetString"
_HwIsisPrefixPriorityL1IpPrefixName_Object = MibTableColumn
hwIsisPrefixPriorityL1IpPrefixName = _HwIsisPrefixPriorityL1IpPrefixName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 4, 1, 4),
    _HwIsisPrefixPriorityL1IpPrefixName_Type()
)
hwIsisPrefixPriorityL1IpPrefixName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisPrefixPriorityL1IpPrefixName.setStatus("current")


class _HwIsisPrefixPriorityL2IpPrefixName_Type(OctetString):
    """Custom type hwIsisPrefixPriorityL2IpPrefixName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 169),
    )


_HwIsisPrefixPriorityL2IpPrefixName_Type.__name__ = "OctetString"
_HwIsisPrefixPriorityL2IpPrefixName_Object = MibTableColumn
hwIsisPrefixPriorityL2IpPrefixName = _HwIsisPrefixPriorityL2IpPrefixName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 4, 1, 5),
    _HwIsisPrefixPriorityL2IpPrefixName_Type()
)
hwIsisPrefixPriorityL2IpPrefixName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisPrefixPriorityL2IpPrefixName.setStatus("current")
_HwIsisPrefixPriorityL1TagValue_Type = Unsigned32
_HwIsisPrefixPriorityL1TagValue_Object = MibTableColumn
hwIsisPrefixPriorityL1TagValue = _HwIsisPrefixPriorityL1TagValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 4, 1, 6),
    _HwIsisPrefixPriorityL1TagValue_Type()
)
hwIsisPrefixPriorityL1TagValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisPrefixPriorityL1TagValue.setStatus("current")
_HwIsisPrefixPriorityL2TagValue_Type = Unsigned32
_HwIsisPrefixPriorityL2TagValue_Object = MibTableColumn
hwIsisPrefixPriorityL2TagValue = _HwIsisPrefixPriorityL2TagValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 4, 1, 7),
    _HwIsisPrefixPriorityL2TagValue_Type()
)
hwIsisPrefixPriorityL2TagValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisPrefixPriorityL2TagValue.setStatus("current")
_HwIsisSummaryTable_Object = MibTable
hwIsisSummaryTable = _HwIsisSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 5)
)
if mibBuilder.loadTexts:
    hwIsisSummaryTable.setStatus("current")
_HwIsisSummaryEntry_Object = MibTableRow
hwIsisSummaryEntry = _HwIsisSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 5, 1)
)
hwIsisSummaryEntry.setIndexNames(
    (0, "HUAWEI-ISIS-CONF-MIB", "hwIsisProcIdIndex"),
    (0, "HUAWEI-ISIS-CONF-MIB", "hwIsisIpTypeIndex"),
    (0, "HUAWEI-ISIS-CONF-MIB", "hwIsisMTIdIndex"),
    (0, "HUAWEI-ISIS-CONF-MIB", "hwIsisSummaryIPIndex"),
    (0, "HUAWEI-ISIS-CONF-MIB", "hwIsisSummaryMaskIndex"),
)
if mibBuilder.loadTexts:
    hwIsisSummaryEntry.setStatus("current")


class _HwIsisSummaryIPIndex_Type(InetAddress):
    """Custom type hwIsisSummaryIPIndex based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_HwIsisSummaryIPIndex_Type.__name__ = "InetAddress"
_HwIsisSummaryIPIndex_Object = MibTableColumn
hwIsisSummaryIPIndex = _HwIsisSummaryIPIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 5, 1, 1),
    _HwIsisSummaryIPIndex_Type()
)
hwIsisSummaryIPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIsisSummaryIPIndex.setStatus("current")


class _HwIsisSummaryMaskIndex_Type(InetAddressPrefixLength):
    """Custom type hwIsisSummaryMaskIndex based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_HwIsisSummaryMaskIndex_Type.__name__ = "InetAddressPrefixLength"
_HwIsisSummaryMaskIndex_Object = MibTableColumn
hwIsisSummaryMaskIndex = _HwIsisSummaryMaskIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 5, 1, 2),
    _HwIsisSummaryMaskIndex_Type()
)
hwIsisSummaryMaskIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIsisSummaryMaskIndex.setStatus("current")


class _HwIsisSummaryAvoidFeedBackEnabled_Type(TruthValue):
    """Custom type hwIsisSummaryAvoidFeedBackEnabled based on TruthValue"""


_HwIsisSummaryAvoidFeedBackEnabled_Object = MibTableColumn
hwIsisSummaryAvoidFeedBackEnabled = _HwIsisSummaryAvoidFeedBackEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 5, 1, 3),
    _HwIsisSummaryAvoidFeedBackEnabled_Type()
)
hwIsisSummaryAvoidFeedBackEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisSummaryAvoidFeedBackEnabled.setStatus("current")


class _HwIsisSummaryGenNull0RouteEnabled_Type(TruthValue):
    """Custom type hwIsisSummaryGenNull0RouteEnabled based on TruthValue"""


_HwIsisSummaryGenNull0RouteEnabled_Object = MibTableColumn
hwIsisSummaryGenNull0RouteEnabled = _HwIsisSummaryGenNull0RouteEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 5, 1, 4),
    _HwIsisSummaryGenNull0RouteEnabled_Type()
)
hwIsisSummaryGenNull0RouteEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisSummaryGenNull0RouteEnabled.setStatus("current")


class _HwIsisSummaryLevel_Type(Integer32):
    """Custom type hwIsisSummaryLevel based on Integer32"""
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
        *(("level1", 1),
          ("level12", 3),
          ("level2", 2))
    )


_HwIsisSummaryLevel_Type.__name__ = "Integer32"
_HwIsisSummaryLevel_Object = MibTableColumn
hwIsisSummaryLevel = _HwIsisSummaryLevel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 5, 1, 5),
    _HwIsisSummaryLevel_Type()
)
hwIsisSummaryLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisSummaryLevel.setStatus("current")
_HwIsisSummaryTag_Type = Unsigned32
_HwIsisSummaryTag_Object = MibTableColumn
hwIsisSummaryTag = _HwIsisSummaryTag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 5, 1, 6),
    _HwIsisSummaryTag_Type()
)
hwIsisSummaryTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisSummaryTag.setStatus("current")
_HwIsisSummaryStatus_Type = RowStatus
_HwIsisSummaryStatus_Object = MibTableColumn
hwIsisSummaryStatus = _HwIsisSummaryStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 5, 1, 7),
    _HwIsisSummaryStatus_Type()
)
hwIsisSummaryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisSummaryStatus.setStatus("current")
_HwIsisImportRouteTable_Object = MibTable
hwIsisImportRouteTable = _HwIsisImportRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 6)
)
if mibBuilder.loadTexts:
    hwIsisImportRouteTable.setStatus("current")
_HwIsisImportRouteEntry_Object = MibTableRow
hwIsisImportRouteEntry = _HwIsisImportRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 6, 1)
)
hwIsisImportRouteEntry.setIndexNames(
    (0, "HUAWEI-ISIS-CONF-MIB", "hwIsisProcIdIndex"),
    (0, "HUAWEI-ISIS-CONF-MIB", "hwIsisIpTypeIndex"),
    (0, "HUAWEI-ISIS-CONF-MIB", "hwIsisMTIdIndex"),
    (0, "HUAWEI-ISIS-CONF-MIB", "hwIsisImportProtocolIndex"),
    (0, "HUAWEI-ISIS-CONF-MIB", "hwIsisImportProcessIdIndex"),
)
if mibBuilder.loadTexts:
    hwIsisImportRouteEntry.setStatus("current")


class _HwIsisImportProtocolIndex_Type(Integer32):
    """Custom type hwIsisImportProtocolIndex based on Integer32"""
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
        *(("bgp", 6),
          ("bgpIbgp", 9),
          ("direct", 1),
          ("isis", 5),
          ("ospf", 4),
          ("ospfv3", 7),
          ("rip", 3),
          ("ripng", 8),
          ("static", 2))
    )


_HwIsisImportProtocolIndex_Type.__name__ = "Integer32"
_HwIsisImportProtocolIndex_Object = MibTableColumn
hwIsisImportProtocolIndex = _HwIsisImportProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 6, 1, 1),
    _HwIsisImportProtocolIndex_Type()
)
hwIsisImportProtocolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIsisImportProtocolIndex.setStatus("current")


class _HwIsisImportProcessIdIndex_Type(Integer32):
    """Custom type hwIsisImportProcessIdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwIsisImportProcessIdIndex_Type.__name__ = "Integer32"
_HwIsisImportProcessIdIndex_Object = MibTableColumn
hwIsisImportProcessIdIndex = _HwIsisImportProcessIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 6, 1, 2),
    _HwIsisImportProcessIdIndex_Type()
)
hwIsisImportProcessIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIsisImportProcessIdIndex.setStatus("current")


class _HwIsisImportInheritCostEnabled_Type(TruthValue):
    """Custom type hwIsisImportInheritCostEnabled based on TruthValue"""


_HwIsisImportInheritCostEnabled_Object = MibTableColumn
hwIsisImportInheritCostEnabled = _HwIsisImportInheritCostEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 6, 1, 3),
    _HwIsisImportInheritCostEnabled_Type()
)
hwIsisImportInheritCostEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisImportInheritCostEnabled.setStatus("current")


class _HwIsisImportCost_Type(Unsigned32):
    """Custom type hwIsisImportCost based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4261412864),
    )


_HwIsisImportCost_Type.__name__ = "Unsigned32"
_HwIsisImportCost_Object = MibTableColumn
hwIsisImportCost = _HwIsisImportCost_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 6, 1, 4),
    _HwIsisImportCost_Type()
)
hwIsisImportCost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisImportCost.setStatus("current")


class _HwIsisImportCostType_Type(Integer32):
    """Custom type hwIsisImportCostType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("internal", 1))
    )


_HwIsisImportCostType_Type.__name__ = "Integer32"
_HwIsisImportCostType_Object = MibTableColumn
hwIsisImportCostType = _HwIsisImportCostType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 6, 1, 5),
    _HwIsisImportCostType_Type()
)
hwIsisImportCostType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisImportCostType.setStatus("current")


class _HwIsisImportLevel_Type(Integer32):
    """Custom type hwIsisImportLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("level1", 1),
          ("level12", 3),
          ("level2", 2))
    )


_HwIsisImportLevel_Type.__name__ = "Integer32"
_HwIsisImportLevel_Object = MibTableColumn
hwIsisImportLevel = _HwIsisImportLevel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 6, 1, 6),
    _HwIsisImportLevel_Type()
)
hwIsisImportLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisImportLevel.setStatus("current")


class _HwIsisImportTag_Type(Unsigned32):
    """Custom type hwIsisImportTag based on Unsigned32"""
    defaultValue = 0


_HwIsisImportTag_Object = MibTableColumn
hwIsisImportTag = _HwIsisImportTag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 6, 1, 7),
    _HwIsisImportTag_Type()
)
hwIsisImportTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisImportTag.setStatus("current")


class _HwIsisImportPolicyName_Type(OctetString):
    """Custom type hwIsisImportPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_HwIsisImportPolicyName_Type.__name__ = "OctetString"
_HwIsisImportPolicyName_Object = MibTableColumn
hwIsisImportPolicyName = _HwIsisImportPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 6, 1, 8),
    _HwIsisImportPolicyName_Type()
)
hwIsisImportPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisImportPolicyName.setStatus("current")
_HwIsisImportRouteStatus_Type = RowStatus
_HwIsisImportRouteStatus_Object = MibTableColumn
hwIsisImportRouteStatus = _HwIsisImportRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 6, 1, 9),
    _HwIsisImportRouteStatus_Type()
)
hwIsisImportRouteStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisImportRouteStatus.setStatus("current")
_HwIsisRouteLeakTable_Object = MibTable
hwIsisRouteLeakTable = _HwIsisRouteLeakTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 7)
)
if mibBuilder.loadTexts:
    hwIsisRouteLeakTable.setStatus("current")
_HwIsisRouteLeakEntry_Object = MibTableRow
hwIsisRouteLeakEntry = _HwIsisRouteLeakEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 7, 1)
)
hwIsisRouteLeakEntry.setIndexNames(
    (0, "HUAWEI-ISIS-CONF-MIB", "hwIsisProcIdIndex"),
    (0, "HUAWEI-ISIS-CONF-MIB", "hwIsisIpTypeIndex"),
    (0, "HUAWEI-ISIS-CONF-MIB", "hwIsisMTIdIndex"),
    (0, "HUAWEI-ISIS-CONF-MIB", "hwIsisRouteLeakTypeIndex"),
)
if mibBuilder.loadTexts:
    hwIsisRouteLeakEntry.setStatus("current")


class _HwIsisRouteLeakTypeIndex_Type(Integer32):
    """Custom type hwIsisRouteLeakTypeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("level1intolevel2", 1),
          ("level2intolevel1", 2))
    )


_HwIsisRouteLeakTypeIndex_Type.__name__ = "Integer32"
_HwIsisRouteLeakTypeIndex_Object = MibTableColumn
hwIsisRouteLeakTypeIndex = _HwIsisRouteLeakTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 7, 1, 1),
    _HwIsisRouteLeakTypeIndex_Type()
)
hwIsisRouteLeakTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIsisRouteLeakTypeIndex.setStatus("current")
_HwIsisRouteLeakTag_Type = Unsigned32
_HwIsisRouteLeakTag_Object = MibTableColumn
hwIsisRouteLeakTag = _HwIsisRouteLeakTag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 7, 1, 2),
    _HwIsisRouteLeakTag_Type()
)
hwIsisRouteLeakTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisRouteLeakTag.setStatus("current")


class _HwIsisRouteLeakFilterPolicyType_Type(Integer32):
    """Custom type hwIsisRouteLeakFilterPolicyType based on Integer32"""
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
        *(("aclName", 2),
          ("basicAcl", 1),
          ("ipPrefix", 3),
          ("none", 0),
          ("routePolicy", 4))
    )


_HwIsisRouteLeakFilterPolicyType_Type.__name__ = "Integer32"
_HwIsisRouteLeakFilterPolicyType_Object = MibTableColumn
hwIsisRouteLeakFilterPolicyType = _HwIsisRouteLeakFilterPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 7, 1, 3),
    _HwIsisRouteLeakFilterPolicyType_Type()
)
hwIsisRouteLeakFilterPolicyType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisRouteLeakFilterPolicyType.setStatus("current")


class _HwIsisRouteLeakFilterPolicyBasicAcl_Type(Integer32):
    """Custom type hwIsisRouteLeakFilterPolicyBasicAcl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 2999),
    )


_HwIsisRouteLeakFilterPolicyBasicAcl_Type.__name__ = "Integer32"
_HwIsisRouteLeakFilterPolicyBasicAcl_Object = MibTableColumn
hwIsisRouteLeakFilterPolicyBasicAcl = _HwIsisRouteLeakFilterPolicyBasicAcl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 7, 1, 4),
    _HwIsisRouteLeakFilterPolicyBasicAcl_Type()
)
hwIsisRouteLeakFilterPolicyBasicAcl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisRouteLeakFilterPolicyBasicAcl.setStatus("current")


class _HwIsisRouteLeakFilterPolicyPolicyName_Type(OctetString):
    """Custom type hwIsisRouteLeakFilterPolicyPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 169),
    )


_HwIsisRouteLeakFilterPolicyPolicyName_Type.__name__ = "OctetString"
_HwIsisRouteLeakFilterPolicyPolicyName_Object = MibTableColumn
hwIsisRouteLeakFilterPolicyPolicyName = _HwIsisRouteLeakFilterPolicyPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 7, 1, 5),
    _HwIsisRouteLeakFilterPolicyPolicyName_Type()
)
hwIsisRouteLeakFilterPolicyPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisRouteLeakFilterPolicyPolicyName.setStatus("current")
_HwIsisRouteLeakStatus_Type = RowStatus
_HwIsisRouteLeakStatus_Object = MibTableColumn
hwIsisRouteLeakStatus = _HwIsisRouteLeakStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 7, 1, 6),
    _HwIsisRouteLeakStatus_Type()
)
hwIsisRouteLeakStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisRouteLeakStatus.setStatus("current")
_HwIsisFrrTable_Object = MibTable
hwIsisFrrTable = _HwIsisFrrTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 8)
)
if mibBuilder.loadTexts:
    hwIsisFrrTable.setStatus("current")
_HwIsisFrrEntry_Object = MibTableRow
hwIsisFrrEntry = _HwIsisFrrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 8, 1)
)
hwIsisFrrEntry.setIndexNames(
    (0, "HUAWEI-ISIS-CONF-MIB", "hwIsisProcIdIndex"),
    (0, "HUAWEI-ISIS-CONF-MIB", "hwIsisIpTypeIndex"),
    (0, "HUAWEI-ISIS-CONF-MIB", "hwIsisMTIdIndex"),
)
if mibBuilder.loadTexts:
    hwIsisFrrEntry.setStatus("current")


class _HwIsisFrrPolicyName_Type(OctetString):
    """Custom type hwIsisFrrPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_HwIsisFrrPolicyName_Type.__name__ = "OctetString"
_HwIsisFrrPolicyName_Object = MibTableColumn
hwIsisFrrPolicyName = _HwIsisFrrPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 8, 1, 1),
    _HwIsisFrrPolicyName_Type()
)
hwIsisFrrPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisFrrPolicyName.setStatus("current")


class _HwIsisFrrLoopFreeAltLevel_Type(Integer32):
    """Custom type hwIsisFrrLoopFreeAltLevel based on Integer32"""
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
        *(("level1", 1),
          ("level12", 3),
          ("level2", 2),
          ("null", 0))
    )


_HwIsisFrrLoopFreeAltLevel_Type.__name__ = "Integer32"
_HwIsisFrrLoopFreeAltLevel_Object = MibTableColumn
hwIsisFrrLoopFreeAltLevel = _HwIsisFrrLoopFreeAltLevel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 8, 1, 2),
    _HwIsisFrrLoopFreeAltLevel_Type()
)
hwIsisFrrLoopFreeAltLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisFrrLoopFreeAltLevel.setStatus("current")
_HwIsisFrrEnabled_Type = TruthValue
_HwIsisFrrEnabled_Object = MibTableColumn
hwIsisFrrEnabled = _HwIsisFrrEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 8, 1, 3),
    _HwIsisFrrEnabled_Type()
)
hwIsisFrrEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisFrrEnabled.setStatus("current")
_HwIsisIntfBaseTable_Object = MibTable
hwIsisIntfBaseTable = _HwIsisIntfBaseTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 21)
)
if mibBuilder.loadTexts:
    hwIsisIntfBaseTable.setStatus("current")
_HwIsisIntfBaseEntry_Object = MibTableRow
hwIsisIntfBaseEntry = _HwIsisIntfBaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 21, 1)
)
hwIsisIntfBaseEntry.setIndexNames(
    (0, "HUAWEI-ISIS-CONF-MIB", "hwIsisProcIdIndex"),
    (0, "HUAWEI-ISIS-CONF-MIB", "hwIsisInterfaceIndex"),
)
if mibBuilder.loadTexts:
    hwIsisIntfBaseEntry.setStatus("current")
_HwIsisInterfaceIndex_Type = Unsigned32
_HwIsisInterfaceIndex_Object = MibTableColumn
hwIsisInterfaceIndex = _HwIsisInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 21, 1, 1),
    _HwIsisInterfaceIndex_Type()
)
hwIsisInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIsisInterfaceIndex.setStatus("current")


class _HwIsisEnableIPProtocol_Type(Integer32):
    """Custom type hwIsisEnableIPProtocol based on Integer32"""
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


_HwIsisEnableIPProtocol_Type.__name__ = "Integer32"
_HwIsisEnableIPProtocol_Object = MibTableColumn
hwIsisEnableIPProtocol = _HwIsisEnableIPProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 21, 1, 2),
    _HwIsisEnableIPProtocol_Type()
)
hwIsisEnableIPProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisEnableIPProtocol.setStatus("current")


class _HwIsisEnableIPv6Protocol_Type(Integer32):
    """Custom type hwIsisEnableIPv6Protocol based on Integer32"""
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


_HwIsisEnableIPv6Protocol_Type.__name__ = "Integer32"
_HwIsisEnableIPv6Protocol_Object = MibTableColumn
hwIsisEnableIPv6Protocol = _HwIsisEnableIPv6Protocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 21, 1, 3),
    _HwIsisEnableIPv6Protocol_Type()
)
hwIsisEnableIPv6Protocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisEnableIPv6Protocol.setStatus("current")


class _HwIsisCircLevel_Type(Integer32):
    """Custom type hwIsisCircLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("level1", 1),
          ("level12", 3),
          ("level2", 2))
    )


_HwIsisCircLevel_Type.__name__ = "Integer32"
_HwIsisCircLevel_Object = MibTableColumn
hwIsisCircLevel = _HwIsisCircLevel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 21, 1, 4),
    _HwIsisCircLevel_Type()
)
hwIsisCircLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisCircLevel.setStatus("current")


class _HwIsisCircSimulation_Type(Integer32):
    """Custom type hwIsisCircSimulation based on Integer32"""
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


_HwIsisCircSimulation_Type.__name__ = "Integer32"
_HwIsisCircSimulation_Object = MibTableColumn
hwIsisCircSimulation = _HwIsisCircSimulation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 21, 1, 5),
    _HwIsisCircSimulation_Type()
)
hwIsisCircSimulation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisCircSimulation.setStatus("current")


class _HwIsisCircL1HelloInterval_Type(Integer32):
    """Custom type hwIsisCircL1HelloInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 255),
    )


_HwIsisCircL1HelloInterval_Type.__name__ = "Integer32"
_HwIsisCircL1HelloInterval_Object = MibTableColumn
hwIsisCircL1HelloInterval = _HwIsisCircL1HelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 21, 1, 6),
    _HwIsisCircL1HelloInterval_Type()
)
hwIsisCircL1HelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisCircL1HelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    hwIsisCircL1HelloInterval.setUnits("seconds")


class _HwIsisCircL2HelloInterval_Type(Integer32):
    """Custom type hwIsisCircL2HelloInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 255),
    )


_HwIsisCircL2HelloInterval_Type.__name__ = "Integer32"
_HwIsisCircL2HelloInterval_Object = MibTableColumn
hwIsisCircL2HelloInterval = _HwIsisCircL2HelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 21, 1, 7),
    _HwIsisCircL2HelloInterval_Type()
)
hwIsisCircL2HelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisCircL2HelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    hwIsisCircL2HelloInterval.setUnits("seconds")


class _HwIsisCircL1HelloMultiplier_Type(Integer32):
    """Custom type hwIsisCircL1HelloMultiplier based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 1000),
    )


_HwIsisCircL1HelloMultiplier_Type.__name__ = "Integer32"
_HwIsisCircL1HelloMultiplier_Object = MibTableColumn
hwIsisCircL1HelloMultiplier = _HwIsisCircL1HelloMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 21, 1, 8),
    _HwIsisCircL1HelloMultiplier_Type()
)
hwIsisCircL1HelloMultiplier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisCircL1HelloMultiplier.setStatus("current")


class _HwIsisCircL2HelloMultiplier_Type(Integer32):
    """Custom type hwIsisCircL2HelloMultiplier based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 1000),
    )


_HwIsisCircL2HelloMultiplier_Type.__name__ = "Integer32"
_HwIsisCircL2HelloMultiplier_Object = MibTableColumn
hwIsisCircL2HelloMultiplier = _HwIsisCircL2HelloMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 21, 1, 9),
    _HwIsisCircL2HelloMultiplier_Type()
)
hwIsisCircL2HelloMultiplier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisCircL2HelloMultiplier.setStatus("current")


class _HwIsisCircL1AuthMode_Type(Integer32):
    """Custom type hwIsisCircL1AuthMode based on Integer32"""
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
        *(("keychain", 3),
          ("md5", 1),
          ("null", 0),
          ("simple", 2))
    )


_HwIsisCircL1AuthMode_Type.__name__ = "Integer32"
_HwIsisCircL1AuthMode_Object = MibTableColumn
hwIsisCircL1AuthMode = _HwIsisCircL1AuthMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 21, 1, 10),
    _HwIsisCircL1AuthMode_Type()
)
hwIsisCircL1AuthMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisCircL1AuthMode.setStatus("current")


class _HwIsisCircL1AuthText_Type(OctetString):
    """Custom type hwIsisCircL1AuthText based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 392),
    )


_HwIsisCircL1AuthText_Type.__name__ = "OctetString"
_HwIsisCircL1AuthText_Object = MibTableColumn
hwIsisCircL1AuthText = _HwIsisCircL1AuthText_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 21, 1, 11),
    _HwIsisCircL1AuthText_Type()
)
hwIsisCircL1AuthText.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisCircL1AuthText.setStatus("current")


class _HwIsisCircL1AuthSendOnly_Type(Integer32):
    """Custom type hwIsisCircL1AuthSendOnly based on Integer32"""
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


_HwIsisCircL1AuthSendOnly_Type.__name__ = "Integer32"
_HwIsisCircL1AuthSendOnly_Object = MibTableColumn
hwIsisCircL1AuthSendOnly = _HwIsisCircL1AuthSendOnly_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 21, 1, 12),
    _HwIsisCircL1AuthSendOnly_Type()
)
hwIsisCircL1AuthSendOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisCircL1AuthSendOnly.setStatus("current")


class _HwIsisCircL1AuthCode_Type(Integer32):
    """Custom type hwIsisCircL1AuthCode based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              10,
              133)
        )
    )
    namedValues = NamedValues(
        *(("ip", 133),
          ("none", 0),
          ("osi", 10))
    )


_HwIsisCircL1AuthCode_Type.__name__ = "Integer32"
_HwIsisCircL1AuthCode_Object = MibTableColumn
hwIsisCircL1AuthCode = _HwIsisCircL1AuthCode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 21, 1, 13),
    _HwIsisCircL1AuthCode_Type()
)
hwIsisCircL1AuthCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisCircL1AuthCode.setStatus("current")


class _HwIsisCircL2AuthMode_Type(Integer32):
    """Custom type hwIsisCircL2AuthMode based on Integer32"""
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
        *(("keychain", 3),
          ("md5", 1),
          ("null", 0),
          ("simple", 2))
    )


_HwIsisCircL2AuthMode_Type.__name__ = "Integer32"
_HwIsisCircL2AuthMode_Object = MibTableColumn
hwIsisCircL2AuthMode = _HwIsisCircL2AuthMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 21, 1, 14),
    _HwIsisCircL2AuthMode_Type()
)
hwIsisCircL2AuthMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisCircL2AuthMode.setStatus("current")


class _HwIsisCircL2AuthText_Type(OctetString):
    """Custom type hwIsisCircL2AuthText based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 392),
    )


_HwIsisCircL2AuthText_Type.__name__ = "OctetString"
_HwIsisCircL2AuthText_Object = MibTableColumn
hwIsisCircL2AuthText = _HwIsisCircL2AuthText_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 21, 1, 15),
    _HwIsisCircL2AuthText_Type()
)
hwIsisCircL2AuthText.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisCircL2AuthText.setStatus("current")


class _HwIsisCircL2AuthSendOnly_Type(Integer32):
    """Custom type hwIsisCircL2AuthSendOnly based on Integer32"""
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


_HwIsisCircL2AuthSendOnly_Type.__name__ = "Integer32"
_HwIsisCircL2AuthSendOnly_Object = MibTableColumn
hwIsisCircL2AuthSendOnly = _HwIsisCircL2AuthSendOnly_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 21, 1, 16),
    _HwIsisCircL2AuthSendOnly_Type()
)
hwIsisCircL2AuthSendOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisCircL2AuthSendOnly.setStatus("current")


class _HwIsisCircL2AuthCode_Type(Integer32):
    """Custom type hwIsisCircL2AuthCode based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              10,
              133)
        )
    )
    namedValues = NamedValues(
        *(("ip", 133),
          ("none", 0),
          ("osi", 10))
    )


_HwIsisCircL2AuthCode_Type.__name__ = "Integer32"
_HwIsisCircL2AuthCode_Object = MibTableColumn
hwIsisCircL2AuthCode = _HwIsisCircL2AuthCode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 21, 1, 17),
    _HwIsisCircL2AuthCode_Type()
)
hwIsisCircL2AuthCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisCircL2AuthCode.setStatus("current")


class _HwIsisCircLdpSync_Type(Integer32):
    """Custom type hwIsisCircLdpSync based on Integer32"""
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


_HwIsisCircLdpSync_Type.__name__ = "Integer32"
_HwIsisCircLdpSync_Object = MibTableColumn
hwIsisCircLdpSync = _HwIsisCircLdpSync_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 21, 1, 18),
    _HwIsisCircLdpSync_Type()
)
hwIsisCircLdpSync.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisCircLdpSync.setStatus("current")


class _HwIsisCircLdpSyncHoldDown_Type(Integer32):
    """Custom type hwIsisCircLdpSyncHoldDown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_HwIsisCircLdpSyncHoldDown_Type.__name__ = "Integer32"
_HwIsisCircLdpSyncHoldDown_Object = MibTableColumn
hwIsisCircLdpSyncHoldDown = _HwIsisCircLdpSyncHoldDown_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 21, 1, 19),
    _HwIsisCircLdpSyncHoldDown_Type()
)
hwIsisCircLdpSyncHoldDown.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisCircLdpSyncHoldDown.setStatus("current")


class _HwIsisCircLdpHldMaxCost_Type(Integer32):
    """Custom type hwIsisCircLdpHldMaxCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65536),
    )


_HwIsisCircLdpHldMaxCost_Type.__name__ = "Integer32"
_HwIsisCircLdpHldMaxCost_Object = MibTableColumn
hwIsisCircLdpHldMaxCost = _HwIsisCircLdpHldMaxCost_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 21, 1, 20),
    _HwIsisCircLdpHldMaxCost_Type()
)
hwIsisCircLdpHldMaxCost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisCircLdpHldMaxCost.setStatus("current")


class _HwIsisCircSmallHello_Type(Integer32):
    """Custom type hwIsisCircSmallHello based on Integer32"""
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


_HwIsisCircSmallHello_Type.__name__ = "Integer32"
_HwIsisCircSmallHello_Object = MibTableColumn
hwIsisCircSmallHello = _HwIsisCircSmallHello_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 21, 1, 21),
    _HwIsisCircSmallHello_Type()
)
hwIsisCircSmallHello.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisCircSmallHello.setStatus("current")


class _HwIsisCircIpIgnore_Type(Integer32):
    """Custom type hwIsisCircIpIgnore based on Integer32"""
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


_HwIsisCircIpIgnore_Type.__name__ = "Integer32"
_HwIsisCircIpIgnore_Object = MibTableColumn
hwIsisCircIpIgnore = _HwIsisCircIpIgnore_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 21, 1, 22),
    _HwIsisCircIpIgnore_Type()
)
hwIsisCircIpIgnore.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisCircIpIgnore.setStatus("current")


class _HwIsisCircSenseRpr_Type(Integer32):
    """Custom type hwIsisCircSenseRpr based on Integer32"""
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


_HwIsisCircSenseRpr_Type.__name__ = "Integer32"
_HwIsisCircSenseRpr_Object = MibTableColumn
hwIsisCircSenseRpr = _HwIsisCircSenseRpr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 21, 1, 23),
    _HwIsisCircSenseRpr_Type()
)
hwIsisCircSenseRpr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisCircSenseRpr.setStatus("current")


class _HwIsisCircPadHello_Type(Integer32):
    """Custom type hwIsisCircPadHello based on Integer32"""
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


_HwIsisCircPadHello_Type.__name__ = "Integer32"
_HwIsisCircPadHello_Object = MibTableColumn
hwIsisCircPadHello = _HwIsisCircPadHello_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 21, 1, 24),
    _HwIsisCircPadHello_Type()
)
hwIsisCircPadHello.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisCircPadHello.setStatus("current")


class _HwIsisCircLspRetransInterval_Type(Integer32):
    """Custom type hwIsisCircLspRetransInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_HwIsisCircLspRetransInterval_Type.__name__ = "Integer32"
_HwIsisCircLspRetransInterval_Object = MibTableColumn
hwIsisCircLspRetransInterval = _HwIsisCircLspRetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 21, 1, 25),
    _HwIsisCircLspRetransInterval_Type()
)
hwIsisCircLspRetransInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisCircLspRetransInterval.setStatus("current")
if mibBuilder.loadTexts:
    hwIsisCircLspRetransInterval.setUnits("seconds")


class _HwIsisL1CsnpTimerValue_Type(Integer32):
    """Custom type hwIsisL1CsnpTimerValue based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwIsisL1CsnpTimerValue_Type.__name__ = "Integer32"
_HwIsisL1CsnpTimerValue_Object = MibTableColumn
hwIsisL1CsnpTimerValue = _HwIsisL1CsnpTimerValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 21, 1, 26),
    _HwIsisL1CsnpTimerValue_Type()
)
hwIsisL1CsnpTimerValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisL1CsnpTimerValue.setStatus("current")
if mibBuilder.loadTexts:
    hwIsisL1CsnpTimerValue.setUnits("seconds")


class _HwIsisL2CsnpTimerValue_Type(Integer32):
    """Custom type hwIsisL2CsnpTimerValue based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwIsisL2CsnpTimerValue_Type.__name__ = "Integer32"
_HwIsisL2CsnpTimerValue_Object = MibTableColumn
hwIsisL2CsnpTimerValue = _HwIsisL2CsnpTimerValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 21, 1, 27),
    _HwIsisL2CsnpTimerValue_Type()
)
hwIsisL2CsnpTimerValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisL2CsnpTimerValue.setStatus("current")
if mibBuilder.loadTexts:
    hwIsisL2CsnpTimerValue.setUnits("seconds")


class _HwIsisLspThrottleInterval_Type(Integer32):
    """Custom type hwIsisLspThrottleInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_HwIsisLspThrottleInterval_Type.__name__ = "Integer32"
_HwIsisLspThrottleInterval_Object = MibTableColumn
hwIsisLspThrottleInterval = _HwIsisLspThrottleInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 21, 1, 28),
    _HwIsisLspThrottleInterval_Type()
)
hwIsisLspThrottleInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisLspThrottleInterval.setStatus("current")
if mibBuilder.loadTexts:
    hwIsisLspThrottleInterval.setUnits("milliseconds.")


class _HwIsisLspThrottleCount_Type(Integer32):
    """Custom type hwIsisLspThrottleCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_HwIsisLspThrottleCount_Type.__name__ = "Integer32"
_HwIsisLspThrottleCount_Object = MibTableColumn
hwIsisLspThrottleCount = _HwIsisLspThrottleCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 21, 1, 29),
    _HwIsisLspThrottleCount_Type()
)
hwIsisLspThrottleCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisLspThrottleCount.setStatus("current")


class _HwIsisCircL1DisPriority_Type(Integer32):
    """Custom type hwIsisCircL1DisPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_HwIsisCircL1DisPriority_Type.__name__ = "Integer32"
_HwIsisCircL1DisPriority_Object = MibTableColumn
hwIsisCircL1DisPriority = _HwIsisCircL1DisPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 21, 1, 30),
    _HwIsisCircL1DisPriority_Type()
)
hwIsisCircL1DisPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisCircL1DisPriority.setStatus("current")


class _HwIsisCircL2DisPriority_Type(Integer32):
    """Custom type hwIsisCircL2DisPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_HwIsisCircL2DisPriority_Type.__name__ = "Integer32"
_HwIsisCircL2DisPriority_Object = MibTableColumn
hwIsisCircL2DisPriority = _HwIsisCircL2DisPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 21, 1, 31),
    _HwIsisCircL2DisPriority_Type()
)
hwIsisCircL2DisPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisCircL2DisPriority.setStatus("current")


class _HwIsisCircSilent_Type(Integer32):
    """Custom type hwIsisCircSilent based on Integer32"""
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


_HwIsisCircSilent_Type.__name__ = "Integer32"
_HwIsisCircSilent_Object = MibTableColumn
hwIsisCircSilent = _HwIsisCircSilent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 21, 1, 32),
    _HwIsisCircSilent_Type()
)
hwIsisCircSilent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisCircSilent.setStatus("current")
_HwIsisCircMeshGroup_Type = Unsigned32
_HwIsisCircMeshGroup_Object = MibTableColumn
hwIsisCircMeshGroup = _HwIsisCircMeshGroup_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 21, 1, 33),
    _HwIsisCircMeshGroup_Type()
)
hwIsisCircMeshGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisCircMeshGroup.setStatus("current")


class _HwIsisCircMeshBlock_Type(Integer32):
    """Custom type hwIsisCircMeshBlock based on Integer32"""
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


_HwIsisCircMeshBlock_Type.__name__ = "Integer32"
_HwIsisCircMeshBlock_Object = MibTableColumn
hwIsisCircMeshBlock = _HwIsisCircMeshBlock_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 21, 1, 34),
    _HwIsisCircMeshBlock_Type()
)
hwIsisCircMeshBlock.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisCircMeshBlock.setStatus("current")


class _HwIsisCircDisName_Type(OctetString):
    """Custom type hwIsisCircDisName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwIsisCircDisName_Type.__name__ = "OctetString"
_HwIsisCircDisName_Object = MibTableColumn
hwIsisCircDisName = _HwIsisCircDisName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 21, 1, 35),
    _HwIsisCircDisName_Type()
)
hwIsisCircDisName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisCircDisName.setStatus("current")


class _HwIsisCircPppNego_Type(Integer32):
    """Custom type hwIsisCircPppNego based on Integer32"""

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
        *(("none", 0),
          ("threeWay", 2),
          ("threeWayOnly", 3),
          ("twoWay", 1))
    )


_HwIsisCircPppNego_Type.__name__ = "Integer32"
_HwIsisCircPppNego_Object = MibTableColumn
hwIsisCircPppNego = _HwIsisCircPppNego_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 21, 1, 36),
    _HwIsisCircPppNego_Type()
)
hwIsisCircPppNego.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisCircPppNego.setStatus("current")


class _HwIsisCircPppOsicpCheck_Type(Integer32):
    """Custom type hwIsisCircPppOsicpCheck based on Integer32"""
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


_HwIsisCircPppOsicpCheck_Type.__name__ = "Integer32"
_HwIsisCircPppOsicpCheck_Object = MibTableColumn
hwIsisCircPppOsicpCheck = _HwIsisCircPppOsicpCheck_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 21, 1, 37),
    _HwIsisCircPppOsicpCheck_Type()
)
hwIsisCircPppOsicpCheck.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisCircPppOsicpCheck.setStatus("current")
_HwIsisIntfRowStatus_Type = RowStatus
_HwIsisIntfRowStatus_Object = MibTableColumn
hwIsisIntfRowStatus = _HwIsisIntfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 21, 1, 38),
    _HwIsisIntfRowStatus_Type()
)
hwIsisIntfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisIntfRowStatus.setStatus("current")


class _HwIsisCircL1AuthKeychainName_Type(OctetString):
    """Custom type hwIsisCircL1AuthKeychainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_HwIsisCircL1AuthKeychainName_Type.__name__ = "OctetString"
_HwIsisCircL1AuthKeychainName_Object = MibTableColumn
hwIsisCircL1AuthKeychainName = _HwIsisCircL1AuthKeychainName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 21, 1, 39),
    _HwIsisCircL1AuthKeychainName_Type()
)
hwIsisCircL1AuthKeychainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisCircL1AuthKeychainName.setStatus("current")


class _HwIsisCircL2AuthKeychainName_Type(OctetString):
    """Custom type hwIsisCircL2AuthKeychainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_HwIsisCircL2AuthKeychainName_Type.__name__ = "OctetString"
_HwIsisCircL2AuthKeychainName_Object = MibTableColumn
hwIsisCircL2AuthKeychainName = _HwIsisCircL2AuthKeychainName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 21, 1, 40),
    _HwIsisCircL2AuthKeychainName_Type()
)
hwIsisCircL2AuthKeychainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisCircL2AuthKeychainName.setStatus("current")


class _HwIsisCircStrictSnpaCheckEnable_Type(Integer32):
    """Custom type hwIsisCircStrictSnpaCheckEnable based on Integer32"""
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


_HwIsisCircStrictSnpaCheckEnable_Type.__name__ = "Integer32"
_HwIsisCircStrictSnpaCheckEnable_Object = MibTableColumn
hwIsisCircStrictSnpaCheckEnable = _HwIsisCircStrictSnpaCheckEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 21, 1, 41),
    _HwIsisCircStrictSnpaCheckEnable_Type()
)
hwIsisCircStrictSnpaCheckEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisCircStrictSnpaCheckEnable.setStatus("current")
_HwIsisIntfExtTable_Object = MibTable
hwIsisIntfExtTable = _HwIsisIntfExtTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 22)
)
if mibBuilder.loadTexts:
    hwIsisIntfExtTable.setStatus("current")
_HwIsisIntfExtEntry_Object = MibTableRow
hwIsisIntfExtEntry = _HwIsisIntfExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 22, 1)
)
hwIsisIntfExtEntry.setIndexNames(
    (0, "HUAWEI-ISIS-CONF-MIB", "hwIsisProcIdIndex"),
    (0, "HUAWEI-ISIS-CONF-MIB", "hwIsisInterfaceIndex"),
    (0, "HUAWEI-ISIS-CONF-MIB", "hwIsisIpTypeIndex"),
    (0, "HUAWEI-ISIS-CONF-MIB", "hwIsisMTIdIndex"),
)
if mibBuilder.loadTexts:
    hwIsisIntfExtEntry.setStatus("current")


class _HwIsisCircL1Cost_Type(Integer32):
    """Custom type hwIsisCircL1Cost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_HwIsisCircL1Cost_Type.__name__ = "Integer32"
_HwIsisCircL1Cost_Object = MibTableColumn
hwIsisCircL1Cost = _HwIsisCircL1Cost_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 22, 1, 1),
    _HwIsisCircL1Cost_Type()
)
hwIsisCircL1Cost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisCircL1Cost.setStatus("current")


class _HwIsisCircL2Cost_Type(Integer32):
    """Custom type hwIsisCircL2Cost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_HwIsisCircL2Cost_Type.__name__ = "Integer32"
_HwIsisCircL2Cost_Object = MibTableColumn
hwIsisCircL2Cost = _HwIsisCircL2Cost_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 22, 1, 2),
    _HwIsisCircL2Cost_Type()
)
hwIsisCircL2Cost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisCircL2Cost.setStatus("current")
_HwIsisL1TagValue_Type = Unsigned32
_HwIsisL1TagValue_Object = MibTableColumn
hwIsisL1TagValue = _HwIsisL1TagValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 22, 1, 3),
    _HwIsisL1TagValue_Type()
)
hwIsisL1TagValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisL1TagValue.setStatus("current")
_HwIsisL2TagValue_Type = Unsigned32
_HwIsisL2TagValue_Object = MibTableColumn
hwIsisL2TagValue = _HwIsisL2TagValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 22, 1, 4),
    _HwIsisL2TagValue_Type()
)
hwIsisL2TagValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisL2TagValue.setStatus("current")


class _HwIsisCircSuppReachablity_Type(Integer32):
    """Custom type hwIsisCircSuppReachablity based on Integer32"""
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
        *(("level1", 1),
          ("level12", 3),
          ("level2", 2),
          ("null", 0))
    )


_HwIsisCircSuppReachablity_Type.__name__ = "Integer32"
_HwIsisCircSuppReachablity_Object = MibTableColumn
hwIsisCircSuppReachablity = _HwIsisCircSuppReachablity_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 22, 1, 5),
    _HwIsisCircSuppReachablity_Type()
)
hwIsisCircSuppReachablity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisCircSuppReachablity.setStatus("current")


class _HwIsisCircFrrBackup_Type(Integer32):
    """Custom type hwIsisCircFrrBackup based on Integer32"""
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
        *(("level1", 1),
          ("level12", 3),
          ("level2", 2),
          ("null", 0))
    )


_HwIsisCircFrrBackup_Type.__name__ = "Integer32"
_HwIsisCircFrrBackup_Object = MibTableColumn
hwIsisCircFrrBackup = _HwIsisCircFrrBackup_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 22, 1, 6),
    _HwIsisCircFrrBackup_Type()
)
hwIsisCircFrrBackup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisCircFrrBackup.setStatus("current")
_HwIsisCircMTRowStatus_Type = RowStatus
_HwIsisCircMTRowStatus_Object = MibTableColumn
hwIsisCircMTRowStatus = _HwIsisCircMTRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 22, 1, 7),
    _HwIsisCircMTRowStatus_Type()
)
hwIsisCircMTRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisCircMTRowStatus.setStatus("current")
_HwIsisIntfBfdTable_Object = MibTable
hwIsisIntfBfdTable = _HwIsisIntfBfdTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 23)
)
if mibBuilder.loadTexts:
    hwIsisIntfBfdTable.setStatus("current")
_HwIsisIntfBfdEntry_Object = MibTableRow
hwIsisIntfBfdEntry = _HwIsisIntfBfdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 23, 1)
)
hwIsisIntfBfdEntry.setIndexNames(
    (0, "HUAWEI-ISIS-CONF-MIB", "hwIsisProcIdIndex"),
    (0, "HUAWEI-ISIS-CONF-MIB", "hwIsisInterfaceIndex"),
    (0, "HUAWEI-ISIS-CONF-MIB", "hwIsisIpTypeIndex"),
)
if mibBuilder.loadTexts:
    hwIsisIntfBfdEntry.setStatus("current")


class _HwIsisCircBfdState_Type(Integer32):
    """Custom type hwIsisCircBfdState based on Integer32"""
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
        *(("block", 4),
          ("disable", 2),
          ("enable", 1),
          ("static", 3))
    )


_HwIsisCircBfdState_Type.__name__ = "Integer32"
_HwIsisCircBfdState_Object = MibTableColumn
hwIsisCircBfdState = _HwIsisCircBfdState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 23, 1, 1),
    _HwIsisCircBfdState_Type()
)
hwIsisCircBfdState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisCircBfdState.setStatus("current")


class _HwIsisCircBfdMinTxInterval_Type(Integer32):
    """Custom type hwIsisCircBfdMinTxInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwIsisCircBfdMinTxInterval_Type.__name__ = "Integer32"
_HwIsisCircBfdMinTxInterval_Object = MibTableColumn
hwIsisCircBfdMinTxInterval = _HwIsisCircBfdMinTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 23, 1, 2),
    _HwIsisCircBfdMinTxInterval_Type()
)
hwIsisCircBfdMinTxInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisCircBfdMinTxInterval.setStatus("current")


class _HwIsisCircBfdMinRxInterval_Type(Integer32):
    """Custom type hwIsisCircBfdMinRxInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwIsisCircBfdMinRxInterval_Type.__name__ = "Integer32"
_HwIsisCircBfdMinRxInterval_Object = MibTableColumn
hwIsisCircBfdMinRxInterval = _HwIsisCircBfdMinRxInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 23, 1, 3),
    _HwIsisCircBfdMinRxInterval_Type()
)
hwIsisCircBfdMinRxInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisCircBfdMinRxInterval.setStatus("current")


class _HwIsisCircBfdMultiplier_Type(Integer32):
    """Custom type hwIsisCircBfdMultiplier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HwIsisCircBfdMultiplier_Type.__name__ = "Integer32"
_HwIsisCircBfdMultiplier_Object = MibTableColumn
hwIsisCircBfdMultiplier = _HwIsisCircBfdMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 23, 1, 4),
    _HwIsisCircBfdMultiplier_Type()
)
hwIsisCircBfdMultiplier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisCircBfdMultiplier.setStatus("current")


class _HwIsisCircBfdFrrBinding_Type(Integer32):
    """Custom type hwIsisCircBfdFrrBinding based on Integer32"""
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


_HwIsisCircBfdFrrBinding_Type.__name__ = "Integer32"
_HwIsisCircBfdFrrBinding_Object = MibTableColumn
hwIsisCircBfdFrrBinding = _HwIsisCircBfdFrrBinding_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 1, 23, 1, 5),
    _HwIsisCircBfdFrrBinding_Type()
)
hwIsisCircBfdFrrBinding.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsisCircBfdFrrBinding.setStatus("current")
_HwIsisTrapsObjects_ObjectIdentity = ObjectIdentity
hwIsisTrapsObjects = _HwIsisTrapsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 2)
)


class _HwIsisAdjChangeReason_Type(Integer32):
    """Custom type hwIsisAdjChangeReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              100)
        )
    )
    namedValues = NamedValues(
        *(("isNbrBfdSessionDown", 4),
          ("isNbrClear", 100),
          ("isNbrConfigurationChange", 5),
          ("isNbrHoldTimerExpired", 1),
          ("isNbrPeerRouterReason", 6),
          ("isNbrPhysicalInterfaceChange", 2),
          ("isNbrProtocolReason", 3))
    )


_HwIsisAdjChangeReason_Type.__name__ = "Integer32"
_HwIsisAdjChangeReason_Object = MibScalar
hwIsisAdjChangeReason = _HwIsisAdjChangeReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 2, 1),
    _HwIsisAdjChangeReason_Type()
)
hwIsisAdjChangeReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIsisAdjChangeReason.setStatus("current")


class _HwisisSysInstance_Type(Integer32):
    """Custom type hwisisSysInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwisisSysInstance_Type.__name__ = "Integer32"
_HwisisSysInstance_Object = MibScalar
hwisisSysInstance = _HwisisSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 2, 2),
    _HwisisSysInstance_Type()
)
hwisisSysInstance.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwisisSysInstance.setStatus("current")


class _HwisisSysLevelIndex_Type(Integer32):
    """Custom type hwisisSysLevelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("level1IS", 1),
          ("level2IS", 2))
    )


_HwisisSysLevelIndex_Type.__name__ = "Integer32"
_HwisisSysLevelIndex_Object = MibScalar
hwisisSysLevelIndex = _HwisisSysLevelIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 2, 3),
    _HwisisSysLevelIndex_Type()
)
hwisisSysLevelIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwisisSysLevelIndex.setStatus("current")
_HwIsisOwnSysID_Type = SystemID
_HwIsisOwnSysID_Object = MibScalar
hwIsisOwnSysID = _HwIsisOwnSysID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 2, 4),
    _HwIsisOwnSysID_Type()
)
hwIsisOwnSysID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIsisOwnSysID.setStatus("current")
_HwIsisAdjSysID_Type = SystemID
_HwIsisAdjSysID_Object = MibScalar
hwIsisAdjSysID = _HwIsisAdjSysID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 2, 5),
    _HwIsisAdjSysID_Type()
)
hwIsisAdjSysID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIsisAdjSysID.setStatus("current")


class _HwIsisAdjSysName_Type(OctetString):
    """Custom type hwIsisAdjSysName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwIsisAdjSysName_Type.__name__ = "OctetString"
_HwIsisAdjSysName_Object = MibScalar
hwIsisAdjSysName = _HwIsisAdjSysName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 2, 6),
    _HwIsisAdjSysName_Type()
)
hwIsisAdjSysName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIsisAdjSysName.setStatus("current")
_HwIsisConflictSystemID_Type = SystemID
_HwIsisConflictSystemID_Object = MibScalar
hwIsisConflictSystemID = _HwIsisConflictSystemID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 2, 7),
    _HwIsisConflictSystemID_Type()
)
hwIsisConflictSystemID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIsisConflictSystemID.setStatus("current")
_HwIsisAutoSysId_Type = SystemID
_HwIsisAutoSysId_Object = MibScalar
hwIsisAutoSysId = _HwIsisAutoSysId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 2, 8),
    _HwIsisAutoSysId_Type()
)
hwIsisAutoSysId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIsisAutoSysId.setStatus("current")
_HwIsisLocalIP_Type = InetAddress
_HwIsisLocalIP_Object = MibScalar
hwIsisLocalIP = _HwIsisLocalIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 2, 9),
    _HwIsisLocalIP_Type()
)
hwIsisLocalIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIsisLocalIP.setStatus("current")
_HwIsisRemoteIP_Type = InetAddress
_HwIsisRemoteIP_Object = MibScalar
hwIsisRemoteIP = _HwIsisRemoteIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 2, 10),
    _HwIsisRemoteIP_Type()
)
hwIsisRemoteIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIsisRemoteIP.setStatus("current")
_HwIsisAdjIP_Type = InetAddress
_HwIsisAdjIP_Object = MibScalar
hwIsisAdjIP = _HwIsisAdjIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 2, 11),
    _HwIsisAdjIP_Type()
)
hwIsisAdjIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIsisAdjIP.setStatus("current")
_HwIsisConfConformance_ObjectIdentity = ObjectIdentity
hwIsisConfConformance = _HwIsisConfConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 3)
)
_HwIsisCompliances_ObjectIdentity = ObjectIdentity
hwIsisCompliances = _HwIsisCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 3, 1)
)
_HwIsisConfGroups_ObjectIdentity = ObjectIdentity
hwIsisConfGroups = _HwIsisConfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 3, 2)
)
_HwIsisTraps_ObjectIdentity = ObjectIdentity
hwIsisTraps = _HwIsisTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 4)
)

# Managed Objects groups

hwIsisProcBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 3, 2, 1)
)
hwIsisProcBaseGroup.setObjects(
      *(("HUAWEI-ISIS-CONF-MIB", "hwIsisProcVpnName"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcVpn6Name"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcAreaAuthType"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcAreaAuthPasswordName"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcAreaAuthPacketAuthMode"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcAreaAuthCode"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcDomainAuthType"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcDomainAuthPasswordName"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcDomainAuthPacketAuthMode"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcDomainAuthCode"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcLevel"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcL1FlashFloodCount"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcL1FlashFloodInterval"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcL2FlashFloodCount"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcL2FlashFloodInterval"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcLogPeerChange"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcTimerRefresh"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcTimerMaxAge"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcL1TimerLspGenMaxInterval"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcL1TimerLspGenInitInterval"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcL1TimerLspGenIncrInterval"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcL2TimerLspGenMaxInterval"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcL2TimerLspGenInitInterval"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcL2TimerLspGenIncrInterval"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcTimerSPFMaxInterval"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcTimerSPFInitInterval"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcTimerSPFIncrInterval"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcCostStyle"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcDynamicName"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcGREnabled"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcGRInterval"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcGRSuppresSAEnabled"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcTEEnableLevel"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcBFDEnabled"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcBFDMinTxInterval"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcBFDMinRecvInteval"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcBFDMultiplier"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcBFDFrrBindEnabled"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcIPv6EnableTopologyType"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcRowStatus"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcOptionalChecksumEnabled"),
        ("HUAWEI-ISIS-CONF-MIB", "hwisisProcLsdbMaxLimit"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcLsdbUpperThreshold"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcLsdbLowerThreshold"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcLsdbTotal"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcAreaAuthKeychainName"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcDomainAuthKeychainName"))
)
if mibBuilder.loadTexts:
    hwIsisProcBaseGroup.setStatus("current")

hwIsisProcMTExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 3, 2, 2)
)
hwIsisProcMTExtGroup.setObjects(
      *(("HUAWEI-ISIS-CONF-MIB", "hwIsisProcDefRoutAdvType"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcDefRoutAdvPolicyName"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcDefRoutAdvCost"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcDefRoutAdvTag"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcDefRoutAdvLevel"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcDefRoutAdvAvoidLearnEnabled"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcL1CircuitCost"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcL2CircuitCost"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcPrefValue"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcPrefPolicyName"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcMaxLoadBalance"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcL1CircuitDefaultTag"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcL2CircuitDefaultTag"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcAutoCostEnabled"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcSetOverLoad"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcSetOverLoadAllowRoute"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcOnStartInterval"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcOnStartStartFromPeer"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcOnStartFromPeerInterval"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisMTName"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcMTStatus"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcL2RedistMaxLimit"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcL1RedistMaxLimit"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcOnStartWaitForBgpEnabled"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcBandWidthReference"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcL1UpperRedistThreshold"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcL2UpperRedistThreshold"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcL1LowerRedistThreshold"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcL2LowerRedistThreshold"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcL1TotalRedist"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcL2TotalRedist"))
)
if mibBuilder.loadTexts:
    hwIsisProcMTExtGroup.setStatus("current")

hwIsisPrefixPriorityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 3, 2, 3)
)
hwIsisPrefixPriorityGroup.setObjects(
      *(("HUAWEI-ISIS-CONF-MIB", "hwIsisPrefixPriorityL1PolicyType"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisPrefixPriorityL2PolicyType"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisPrefixPriorityL1IpPrefixName"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisPrefixPriorityL2IpPrefixName"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisPrefixPriorityL1TagValue"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisPrefixPriorityL2TagValue"))
)
if mibBuilder.loadTexts:
    hwIsisPrefixPriorityGroup.setStatus("current")

hwIsisSummaryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 3, 2, 4)
)
hwIsisSummaryGroup.setObjects(
      *(("HUAWEI-ISIS-CONF-MIB", "hwIsisSummaryAvoidFeedBackEnabled"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisSummaryGenNull0RouteEnabled"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisSummaryLevel"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisSummaryTag"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisSummaryStatus"))
)
if mibBuilder.loadTexts:
    hwIsisSummaryGroup.setStatus("current")

hwIsisNETGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 3, 2, 5)
)
hwIsisNETGroup.setObjects(
    ("HUAWEI-ISIS-CONF-MIB", "hwIsisNETStatus")
)
if mibBuilder.loadTexts:
    hwIsisNETGroup.setStatus("current")

hwIsisImportRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 3, 2, 6)
)
hwIsisImportRouteGroup.setObjects(
      *(("HUAWEI-ISIS-CONF-MIB", "hwIsisImportInheritCostEnabled"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisImportCost"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisImportCostType"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisImportLevel"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisImportTag"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisImportPolicyName"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisImportRouteStatus"))
)
if mibBuilder.loadTexts:
    hwIsisImportRouteGroup.setStatus("current")

hwIsisRouteLeakGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 3, 2, 7)
)
hwIsisRouteLeakGroup.setObjects(
      *(("HUAWEI-ISIS-CONF-MIB", "hwIsisRouteLeakTag"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisRouteLeakFilterPolicyType"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisRouteLeakFilterPolicyBasicAcl"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisRouteLeakFilterPolicyPolicyName"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisRouteLeakStatus"))
)
if mibBuilder.loadTexts:
    hwIsisRouteLeakGroup.setStatus("current")

hwIsisFrrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 3, 2, 8)
)
hwIsisFrrGroup.setObjects(
      *(("HUAWEI-ISIS-CONF-MIB", "hwIsisFrrPolicyName"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisFrrLoopFreeAltLevel"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisFrrEnabled"))
)
if mibBuilder.loadTexts:
    hwIsisFrrGroup.setStatus("current")

hwIsisIntfBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 3, 2, 21)
)
hwIsisIntfBaseGroup.setObjects(
      *(("HUAWEI-ISIS-CONF-MIB", "hwIsisEnableIPProtocol"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisEnableIPv6Protocol"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisCircLevel"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisCircSimulation"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisCircL1HelloInterval"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisCircL2HelloInterval"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisCircL1HelloMultiplier"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisCircL2HelloMultiplier"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisCircL1AuthMode"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisCircL1AuthText"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisCircL1AuthSendOnly"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisCircL2AuthMode"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisCircL2AuthText"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisCircL2AuthSendOnly"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisCircLdpSync"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisCircLdpSyncHoldDown"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisCircLdpHldMaxCost"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisCircSmallHello"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisCircIpIgnore"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisCircSenseRpr"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisCircPadHello"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisCircLspRetransInterval"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisL1CsnpTimerValue"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisL2CsnpTimerValue"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisLspThrottleInterval"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisLspThrottleCount"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisCircL1DisPriority"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisCircL2DisPriority"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisCircSilent"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisCircMeshGroup"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisCircMeshBlock"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisCircDisName"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisCircPppNego"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisCircPppOsicpCheck"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisIntfRowStatus"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisCircL1AuthCode"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisCircL2AuthCode"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisCircL1AuthKeychainName"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisCircL2AuthKeychainName"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisCircStrictSnpaCheckEnable"))
)
if mibBuilder.loadTexts:
    hwIsisIntfBaseGroup.setStatus("current")

hwIsisIntfExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 3, 2, 22)
)
hwIsisIntfExtGroup.setObjects(
      *(("HUAWEI-ISIS-CONF-MIB", "hwIsisCircL1Cost"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisCircL2Cost"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisL1TagValue"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisL2TagValue"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisCircSuppReachablity"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisCircFrrBackup"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisCircMTRowStatus"))
)
if mibBuilder.loadTexts:
    hwIsisIntfExtGroup.setStatus("current")

hwIsisIntfBfdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 3, 2, 23)
)
hwIsisIntfBfdGroup.setObjects(
      *(("HUAWEI-ISIS-CONF-MIB", "hwIsisCircBfdMinTxInterval"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisCircBfdMinRxInterval"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisCircBfdMultiplier"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisCircBfdFrrBinding"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisCircBfdState"))
)
if mibBuilder.loadTexts:
    hwIsisIntfBfdGroup.setStatus("current")

hwIsisTrapsObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 3, 2, 24)
)
hwIsisTrapsObjectsGroup.setObjects(
      *(("HUAWEI-ISIS-CONF-MIB", "hwIsisAdjChangeReason"),
        ("HUAWEI-ISIS-CONF-MIB", "hwisisSysInstance"),
        ("HUAWEI-ISIS-CONF-MIB", "hwisisSysLevelIndex"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisOwnSysID"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisAdjSysID"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisAdjSysName"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisConflictSystemID"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisAutoSysId"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisLocalIP"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisAdjIP"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisRemoteIP"))
)
if mibBuilder.loadTexts:
    hwIsisTrapsObjectsGroup.setStatus("current")


# Notification objects

hwIsisSystemIdConflict = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 4, 1)
)
hwIsisSystemIdConflict.setObjects(
      *(("HUAWEI-ISIS-CONF-MIB", "hwisisSysInstance"),
        ("HUAWEI-ISIS-CONF-MIB", "hwisisSysLevelIndex"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisOwnSysID"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcDynamicName"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisAdjSysID"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisAdjSysName"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisLocalIP"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisAdjIP"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisRemoteIP"))
)
if mibBuilder.loadTexts:
    hwIsisSystemIdConflict.setStatus(
        "current"
    )

hwIsisL1ImportRouteExceedLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 4, 2)
)
hwIsisL1ImportRouteExceedLimit.setObjects(
      *(("HUAWEI-ISIS-CONF-MIB", "hwIsisProcL1RedistMaxLimit"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcL1TotalRedist"))
)
if mibBuilder.loadTexts:
    hwIsisL1ImportRouteExceedLimit.setStatus(
        "current"
    )

hwIsisL1ImportRouteRestoreToLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 4, 3)
)
hwIsisL1ImportRouteRestoreToLimit.setObjects(
      *(("HUAWEI-ISIS-CONF-MIB", "hwIsisProcL1RedistMaxLimit"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcL1TotalRedist"))
)
if mibBuilder.loadTexts:
    hwIsisL1ImportRouteRestoreToLimit.setStatus(
        "current"
    )

hwIsisL2ImportRouteExceedLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 4, 4)
)
hwIsisL2ImportRouteExceedLimit.setObjects(
      *(("HUAWEI-ISIS-CONF-MIB", "hwIsisProcL2RedistMaxLimit"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcL2TotalRedist"))
)
if mibBuilder.loadTexts:
    hwIsisL2ImportRouteExceedLimit.setStatus(
        "current"
    )

hwIsisL2ImportRouteRestoreToLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 4, 5)
)
hwIsisL2ImportRouteRestoreToLimit.setObjects(
      *(("HUAWEI-ISIS-CONF-MIB", "hwIsisProcL2RedistMaxLimit"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcL2TotalRedist"))
)
if mibBuilder.loadTexts:
    hwIsisL2ImportRouteRestoreToLimit.setStatus(
        "current"
    )

hwIsisL1ImportRouteThresholdReach = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 4, 6)
)
hwIsisL1ImportRouteThresholdReach.setObjects(
      *(("HUAWEI-ISIS-CONF-MIB", "hwIsisProcL1RedistMaxLimit"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcL1UpperRedistThreshold"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcL1LowerRedistThreshold"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcL1TotalRedist"))
)
if mibBuilder.loadTexts:
    hwIsisL1ImportRouteThresholdReach.setStatus(
        "current"
    )

hwIsisL1ImportRouteThresholdReachClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 4, 7)
)
hwIsisL1ImportRouteThresholdReachClear.setObjects(
      *(("HUAWEI-ISIS-CONF-MIB", "hwIsisProcL1RedistMaxLimit"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcL1UpperRedistThreshold"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcL1LowerRedistThreshold"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcL1TotalRedist"))
)
if mibBuilder.loadTexts:
    hwIsisL1ImportRouteThresholdReachClear.setStatus(
        "current"
    )

hwIsisL2ImportRouteThresholdReach = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 4, 8)
)
hwIsisL2ImportRouteThresholdReach.setObjects(
      *(("HUAWEI-ISIS-CONF-MIB", "hwIsisProcL2RedistMaxLimit"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcL2UpperRedistThreshold"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcL2LowerRedistThreshold"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcL2TotalRedist"))
)
if mibBuilder.loadTexts:
    hwIsisL2ImportRouteThresholdReach.setStatus(
        "current"
    )

hwIsisL2ImportRouteThresholdReachClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 4, 9)
)
hwIsisL2ImportRouteThresholdReachClear.setObjects(
      *(("HUAWEI-ISIS-CONF-MIB", "hwIsisProcL2RedistMaxLimit"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcL2UpperRedistThreshold"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcL2LowerRedistThreshold"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcL2TotalRedist"))
)
if mibBuilder.loadTexts:
    hwIsisL2ImportRouteThresholdReachClear.setStatus(
        "current"
    )

hwIsisLsdbThresholdReach = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 4, 10)
)
hwIsisLsdbThresholdReach.setObjects(
      *(("HUAWEI-ISIS-CONF-MIB", "hwisisProcLsdbMaxLimit"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcLsdbUpperThreshold"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcLsdbLowerThreshold"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcLsdbTotal"))
)
if mibBuilder.loadTexts:
    hwIsisLsdbThresholdReach.setStatus(
        "current"
    )

hwIsisLsdbThresholdReachClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 4, 11)
)
hwIsisLsdbThresholdReachClear.setObjects(
      *(("HUAWEI-ISIS-CONF-MIB", "hwisisProcLsdbMaxLimit"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcLsdbUpperThreshold"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcLsdbLowerThreshold"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisProcLsdbTotal"))
)
if mibBuilder.loadTexts:
    hwIsisLsdbThresholdReachClear.setStatus(
        "current"
    )

hwIsisSystemIdAutoRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 4, 12)
)
hwIsisSystemIdAutoRecover.setObjects(
      *(("HUAWEI-ISIS-CONF-MIB", "hwisisSysInstance"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisConflictSystemID"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisAutoSysId"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisLocalIP"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisRemoteIP"))
)
if mibBuilder.loadTexts:
    hwIsisSystemIdAutoRecover.setStatus(
        "current"
    )

hwIsisAdjacencyChangeClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 4, 13)
)
hwIsisAdjacencyChangeClear.setObjects(
      *(("ISIS-MIB", "isisSysInstance"),
        ("ISIS-MIB", "isisSysLevelIndex"),
        ("ISIS-MIB", "isisCircIfIndex"),
        ("ISIS-MIB", "isisPduLspId"),
        ("ISIS-MIB", "isisAdjState"),
        ("IF-MIB", "ifName"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisAdjChangeReason"))
)
if mibBuilder.loadTexts:
    hwIsisAdjacencyChangeClear.setStatus(
        "current"
    )

hwIsisSeqNumExceedThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 4, 14)
)
hwIsisSeqNumExceedThreshold.setObjects(
      *(("ISIS-MIB", "isisSysInstance"),
        ("ISIS-MIB", "isisSysLevelIndex"),
        ("ISIS-MIB", "isisPduLspId"))
)
if mibBuilder.loadTexts:
    hwIsisSeqNumExceedThreshold.setStatus(
        "current"
    )


# Notifications groups

hwIsisTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 3, 2, 25)
)
hwIsisTrapsGroup.setObjects(
      *(("HUAWEI-ISIS-CONF-MIB", "hwIsisSystemIdConflict"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisL1ImportRouteExceedLimit"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisL1ImportRouteRestoreToLimit"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisL2ImportRouteExceedLimit"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisL2ImportRouteRestoreToLimit"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisL1ImportRouteThresholdReach"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisL1ImportRouteThresholdReachClear"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisL2ImportRouteThresholdReach"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisL2ImportRouteThresholdReachClear"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisLsdbThresholdReach"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisLsdbThresholdReachClear"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisSystemIdAutoRecover"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisAdjacencyChangeClear"),
        ("HUAWEI-ISIS-CONF-MIB", "hwIsisSeqNumExceedThreshold"))
)
if mibBuilder.loadTexts:
    hwIsisTrapsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwIsisModuleFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 24, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hwIsisModuleFullCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-ISIS-CONF-MIB",
    **{"SystemID": SystemID,
       "InetAddress": InetAddress,
       "InetAddressType": InetAddressType,
       "InetAddressPrefixLength": InetAddressPrefixLength,
       "hwISIS": hwISIS,
       "hwIsisConf": hwIsisConf,
       "hwIsisMIBObjects": hwIsisMIBObjects,
       "hwIsisProcBaseTable": hwIsisProcBaseTable,
       "hwIsisProcBaseEntry": hwIsisProcBaseEntry,
       "hwIsisProcIdIndex": hwIsisProcIdIndex,
       "hwIsisProcVpnName": hwIsisProcVpnName,
       "hwIsisProcVpn6Name": hwIsisProcVpn6Name,
       "hwIsisProcAreaAuthType": hwIsisProcAreaAuthType,
       "hwIsisProcAreaAuthPasswordName": hwIsisProcAreaAuthPasswordName,
       "hwIsisProcAreaAuthPacketAuthMode": hwIsisProcAreaAuthPacketAuthMode,
       "hwIsisProcAreaAuthCode": hwIsisProcAreaAuthCode,
       "hwIsisProcDomainAuthType": hwIsisProcDomainAuthType,
       "hwIsisProcDomainAuthPasswordName": hwIsisProcDomainAuthPasswordName,
       "hwIsisProcDomainAuthPacketAuthMode": hwIsisProcDomainAuthPacketAuthMode,
       "hwIsisProcDomainAuthCode": hwIsisProcDomainAuthCode,
       "hwIsisProcLevel": hwIsisProcLevel,
       "hwIsisProcL1FlashFloodCount": hwIsisProcL1FlashFloodCount,
       "hwIsisProcL1FlashFloodInterval": hwIsisProcL1FlashFloodInterval,
       "hwIsisProcL2FlashFloodCount": hwIsisProcL2FlashFloodCount,
       "hwIsisProcL2FlashFloodInterval": hwIsisProcL2FlashFloodInterval,
       "hwIsisProcLogPeerChange": hwIsisProcLogPeerChange,
       "hwIsisProcTimerRefresh": hwIsisProcTimerRefresh,
       "hwIsisProcTimerMaxAge": hwIsisProcTimerMaxAge,
       "hwIsisProcL1TimerLspGenMaxInterval": hwIsisProcL1TimerLspGenMaxInterval,
       "hwIsisProcL1TimerLspGenInitInterval": hwIsisProcL1TimerLspGenInitInterval,
       "hwIsisProcL1TimerLspGenIncrInterval": hwIsisProcL1TimerLspGenIncrInterval,
       "hwIsisProcL2TimerLspGenMaxInterval": hwIsisProcL2TimerLspGenMaxInterval,
       "hwIsisProcL2TimerLspGenInitInterval": hwIsisProcL2TimerLspGenInitInterval,
       "hwIsisProcL2TimerLspGenIncrInterval": hwIsisProcL2TimerLspGenIncrInterval,
       "hwIsisProcTimerSPFMaxInterval": hwIsisProcTimerSPFMaxInterval,
       "hwIsisProcTimerSPFInitInterval": hwIsisProcTimerSPFInitInterval,
       "hwIsisProcTimerSPFIncrInterval": hwIsisProcTimerSPFIncrInterval,
       "hwIsisProcCostStyle": hwIsisProcCostStyle,
       "hwIsisProcDynamicName": hwIsisProcDynamicName,
       "hwIsisProcGREnabled": hwIsisProcGREnabled,
       "hwIsisProcGRInterval": hwIsisProcGRInterval,
       "hwIsisProcGRSuppresSAEnabled": hwIsisProcGRSuppresSAEnabled,
       "hwIsisProcTEEnableLevel": hwIsisProcTEEnableLevel,
       "hwIsisProcBFDEnabled": hwIsisProcBFDEnabled,
       "hwIsisProcBFDFrrBindEnabled": hwIsisProcBFDFrrBindEnabled,
       "hwIsisProcBFDMinTxInterval": hwIsisProcBFDMinTxInterval,
       "hwIsisProcBFDMinRecvInteval": hwIsisProcBFDMinRecvInteval,
       "hwIsisProcBFDMultiplier": hwIsisProcBFDMultiplier,
       "hwIsisProcIPv6EnableTopologyType": hwIsisProcIPv6EnableTopologyType,
       "hwIsisProcRowStatus": hwIsisProcRowStatus,
       "hwIsisProcOptionalChecksumEnabled": hwIsisProcOptionalChecksumEnabled,
       "hwisisProcLsdbMaxLimit": hwisisProcLsdbMaxLimit,
       "hwIsisProcLsdbUpperThreshold": hwIsisProcLsdbUpperThreshold,
       "hwIsisProcLsdbLowerThreshold": hwIsisProcLsdbLowerThreshold,
       "hwIsisProcLsdbTotal": hwIsisProcLsdbTotal,
       "hwIsisProcAreaAuthKeychainName": hwIsisProcAreaAuthKeychainName,
       "hwIsisProcDomainAuthKeychainName": hwIsisProcDomainAuthKeychainName,
       "hwIsisNETTable": hwIsisNETTable,
       "hwIsisNETEntry": hwIsisNETEntry,
       "hwIsisNETIndex": hwIsisNETIndex,
       "hwIsisNETStatus": hwIsisNETStatus,
       "hwIsisProcMTExtTable": hwIsisProcMTExtTable,
       "hwIsisProcMTExtEntry": hwIsisProcMTExtEntry,
       "hwIsisIpTypeIndex": hwIsisIpTypeIndex,
       "hwIsisMTIdIndex": hwIsisMTIdIndex,
       "hwIsisMTName": hwIsisMTName,
       "hwIsisProcDefRoutAdvType": hwIsisProcDefRoutAdvType,
       "hwIsisProcDefRoutAdvPolicyName": hwIsisProcDefRoutAdvPolicyName,
       "hwIsisProcDefRoutAdvCost": hwIsisProcDefRoutAdvCost,
       "hwIsisProcDefRoutAdvTag": hwIsisProcDefRoutAdvTag,
       "hwIsisProcDefRoutAdvLevel": hwIsisProcDefRoutAdvLevel,
       "hwIsisProcDefRoutAdvAvoidLearnEnabled": hwIsisProcDefRoutAdvAvoidLearnEnabled,
       "hwIsisProcL1CircuitCost": hwIsisProcL1CircuitCost,
       "hwIsisProcL2CircuitCost": hwIsisProcL2CircuitCost,
       "hwIsisProcPrefValue": hwIsisProcPrefValue,
       "hwIsisProcPrefPolicyName": hwIsisProcPrefPolicyName,
       "hwIsisProcMaxLoadBalance": hwIsisProcMaxLoadBalance,
       "hwIsisProcL1CircuitDefaultTag": hwIsisProcL1CircuitDefaultTag,
       "hwIsisProcL2CircuitDefaultTag": hwIsisProcL2CircuitDefaultTag,
       "hwIsisProcBandWidthReference": hwIsisProcBandWidthReference,
       "hwIsisProcAutoCostEnabled": hwIsisProcAutoCostEnabled,
       "hwIsisProcSetOverLoad": hwIsisProcSetOverLoad,
       "hwIsisProcSetOverLoadAllowRoute": hwIsisProcSetOverLoadAllowRoute,
       "hwIsisProcOnStartInterval": hwIsisProcOnStartInterval,
       "hwIsisProcOnStartStartFromPeer": hwIsisProcOnStartStartFromPeer,
       "hwIsisProcOnStartFromPeerInterval": hwIsisProcOnStartFromPeerInterval,
       "hwIsisProcOnStartWaitForBgpEnabled": hwIsisProcOnStartWaitForBgpEnabled,
       "hwIsisProcMTStatus": hwIsisProcMTStatus,
       "hwIsisProcL1RedistMaxLimit": hwIsisProcL1RedistMaxLimit,
       "hwIsisProcL2RedistMaxLimit": hwIsisProcL2RedistMaxLimit,
       "hwIsisProcL1UpperRedistThreshold": hwIsisProcL1UpperRedistThreshold,
       "hwIsisProcL2UpperRedistThreshold": hwIsisProcL2UpperRedistThreshold,
       "hwIsisProcL1LowerRedistThreshold": hwIsisProcL1LowerRedistThreshold,
       "hwIsisProcL2LowerRedistThreshold": hwIsisProcL2LowerRedistThreshold,
       "hwIsisProcL1TotalRedist": hwIsisProcL1TotalRedist,
       "hwIsisProcL2TotalRedist": hwIsisProcL2TotalRedist,
       "hwIsisPrefixPriorityTable": hwIsisPrefixPriorityTable,
       "hwIsisPrefixPriorityEntry": hwIsisPrefixPriorityEntry,
       "hwIsisPrefixPriorityTypeIndex": hwIsisPrefixPriorityTypeIndex,
       "hwIsisPrefixPriorityL1PolicyType": hwIsisPrefixPriorityL1PolicyType,
       "hwIsisPrefixPriorityL2PolicyType": hwIsisPrefixPriorityL2PolicyType,
       "hwIsisPrefixPriorityL1IpPrefixName": hwIsisPrefixPriorityL1IpPrefixName,
       "hwIsisPrefixPriorityL2IpPrefixName": hwIsisPrefixPriorityL2IpPrefixName,
       "hwIsisPrefixPriorityL1TagValue": hwIsisPrefixPriorityL1TagValue,
       "hwIsisPrefixPriorityL2TagValue": hwIsisPrefixPriorityL2TagValue,
       "hwIsisSummaryTable": hwIsisSummaryTable,
       "hwIsisSummaryEntry": hwIsisSummaryEntry,
       "hwIsisSummaryIPIndex": hwIsisSummaryIPIndex,
       "hwIsisSummaryMaskIndex": hwIsisSummaryMaskIndex,
       "hwIsisSummaryAvoidFeedBackEnabled": hwIsisSummaryAvoidFeedBackEnabled,
       "hwIsisSummaryGenNull0RouteEnabled": hwIsisSummaryGenNull0RouteEnabled,
       "hwIsisSummaryLevel": hwIsisSummaryLevel,
       "hwIsisSummaryTag": hwIsisSummaryTag,
       "hwIsisSummaryStatus": hwIsisSummaryStatus,
       "hwIsisImportRouteTable": hwIsisImportRouteTable,
       "hwIsisImportRouteEntry": hwIsisImportRouteEntry,
       "hwIsisImportProtocolIndex": hwIsisImportProtocolIndex,
       "hwIsisImportProcessIdIndex": hwIsisImportProcessIdIndex,
       "hwIsisImportInheritCostEnabled": hwIsisImportInheritCostEnabled,
       "hwIsisImportCost": hwIsisImportCost,
       "hwIsisImportCostType": hwIsisImportCostType,
       "hwIsisImportLevel": hwIsisImportLevel,
       "hwIsisImportTag": hwIsisImportTag,
       "hwIsisImportPolicyName": hwIsisImportPolicyName,
       "hwIsisImportRouteStatus": hwIsisImportRouteStatus,
       "hwIsisRouteLeakTable": hwIsisRouteLeakTable,
       "hwIsisRouteLeakEntry": hwIsisRouteLeakEntry,
       "hwIsisRouteLeakTypeIndex": hwIsisRouteLeakTypeIndex,
       "hwIsisRouteLeakTag": hwIsisRouteLeakTag,
       "hwIsisRouteLeakFilterPolicyType": hwIsisRouteLeakFilterPolicyType,
       "hwIsisRouteLeakFilterPolicyBasicAcl": hwIsisRouteLeakFilterPolicyBasicAcl,
       "hwIsisRouteLeakFilterPolicyPolicyName": hwIsisRouteLeakFilterPolicyPolicyName,
       "hwIsisRouteLeakStatus": hwIsisRouteLeakStatus,
       "hwIsisFrrTable": hwIsisFrrTable,
       "hwIsisFrrEntry": hwIsisFrrEntry,
       "hwIsisFrrPolicyName": hwIsisFrrPolicyName,
       "hwIsisFrrLoopFreeAltLevel": hwIsisFrrLoopFreeAltLevel,
       "hwIsisFrrEnabled": hwIsisFrrEnabled,
       "hwIsisIntfBaseTable": hwIsisIntfBaseTable,
       "hwIsisIntfBaseEntry": hwIsisIntfBaseEntry,
       "hwIsisInterfaceIndex": hwIsisInterfaceIndex,
       "hwIsisEnableIPProtocol": hwIsisEnableIPProtocol,
       "hwIsisEnableIPv6Protocol": hwIsisEnableIPv6Protocol,
       "hwIsisCircLevel": hwIsisCircLevel,
       "hwIsisCircSimulation": hwIsisCircSimulation,
       "hwIsisCircL1HelloInterval": hwIsisCircL1HelloInterval,
       "hwIsisCircL2HelloInterval": hwIsisCircL2HelloInterval,
       "hwIsisCircL1HelloMultiplier": hwIsisCircL1HelloMultiplier,
       "hwIsisCircL2HelloMultiplier": hwIsisCircL2HelloMultiplier,
       "hwIsisCircL1AuthMode": hwIsisCircL1AuthMode,
       "hwIsisCircL1AuthText": hwIsisCircL1AuthText,
       "hwIsisCircL1AuthSendOnly": hwIsisCircL1AuthSendOnly,
       "hwIsisCircL1AuthCode": hwIsisCircL1AuthCode,
       "hwIsisCircL2AuthMode": hwIsisCircL2AuthMode,
       "hwIsisCircL2AuthText": hwIsisCircL2AuthText,
       "hwIsisCircL2AuthSendOnly": hwIsisCircL2AuthSendOnly,
       "hwIsisCircL2AuthCode": hwIsisCircL2AuthCode,
       "hwIsisCircLdpSync": hwIsisCircLdpSync,
       "hwIsisCircLdpSyncHoldDown": hwIsisCircLdpSyncHoldDown,
       "hwIsisCircLdpHldMaxCost": hwIsisCircLdpHldMaxCost,
       "hwIsisCircSmallHello": hwIsisCircSmallHello,
       "hwIsisCircIpIgnore": hwIsisCircIpIgnore,
       "hwIsisCircSenseRpr": hwIsisCircSenseRpr,
       "hwIsisCircPadHello": hwIsisCircPadHello,
       "hwIsisCircLspRetransInterval": hwIsisCircLspRetransInterval,
       "hwIsisL1CsnpTimerValue": hwIsisL1CsnpTimerValue,
       "hwIsisL2CsnpTimerValue": hwIsisL2CsnpTimerValue,
       "hwIsisLspThrottleInterval": hwIsisLspThrottleInterval,
       "hwIsisLspThrottleCount": hwIsisLspThrottleCount,
       "hwIsisCircL1DisPriority": hwIsisCircL1DisPriority,
       "hwIsisCircL2DisPriority": hwIsisCircL2DisPriority,
       "hwIsisCircSilent": hwIsisCircSilent,
       "hwIsisCircMeshGroup": hwIsisCircMeshGroup,
       "hwIsisCircMeshBlock": hwIsisCircMeshBlock,
       "hwIsisCircDisName": hwIsisCircDisName,
       "hwIsisCircPppNego": hwIsisCircPppNego,
       "hwIsisCircPppOsicpCheck": hwIsisCircPppOsicpCheck,
       "hwIsisIntfRowStatus": hwIsisIntfRowStatus,
       "hwIsisCircL1AuthKeychainName": hwIsisCircL1AuthKeychainName,
       "hwIsisCircL2AuthKeychainName": hwIsisCircL2AuthKeychainName,
       "hwIsisCircStrictSnpaCheckEnable": hwIsisCircStrictSnpaCheckEnable,
       "hwIsisIntfExtTable": hwIsisIntfExtTable,
       "hwIsisIntfExtEntry": hwIsisIntfExtEntry,
       "hwIsisCircL1Cost": hwIsisCircL1Cost,
       "hwIsisCircL2Cost": hwIsisCircL2Cost,
       "hwIsisL1TagValue": hwIsisL1TagValue,
       "hwIsisL2TagValue": hwIsisL2TagValue,
       "hwIsisCircSuppReachablity": hwIsisCircSuppReachablity,
       "hwIsisCircFrrBackup": hwIsisCircFrrBackup,
       "hwIsisCircMTRowStatus": hwIsisCircMTRowStatus,
       "hwIsisIntfBfdTable": hwIsisIntfBfdTable,
       "hwIsisIntfBfdEntry": hwIsisIntfBfdEntry,
       "hwIsisCircBfdState": hwIsisCircBfdState,
       "hwIsisCircBfdMinTxInterval": hwIsisCircBfdMinTxInterval,
       "hwIsisCircBfdMinRxInterval": hwIsisCircBfdMinRxInterval,
       "hwIsisCircBfdMultiplier": hwIsisCircBfdMultiplier,
       "hwIsisCircBfdFrrBinding": hwIsisCircBfdFrrBinding,
       "hwIsisTrapsObjects": hwIsisTrapsObjects,
       "hwIsisAdjChangeReason": hwIsisAdjChangeReason,
       "hwisisSysInstance": hwisisSysInstance,
       "hwisisSysLevelIndex": hwisisSysLevelIndex,
       "hwIsisOwnSysID": hwIsisOwnSysID,
       "hwIsisAdjSysID": hwIsisAdjSysID,
       "hwIsisAdjSysName": hwIsisAdjSysName,
       "hwIsisConflictSystemID": hwIsisConflictSystemID,
       "hwIsisAutoSysId": hwIsisAutoSysId,
       "hwIsisLocalIP": hwIsisLocalIP,
       "hwIsisRemoteIP": hwIsisRemoteIP,
       "hwIsisAdjIP": hwIsisAdjIP,
       "hwIsisConfConformance": hwIsisConfConformance,
       "hwIsisCompliances": hwIsisCompliances,
       "hwIsisModuleFullCompliance": hwIsisModuleFullCompliance,
       "hwIsisConfGroups": hwIsisConfGroups,
       "hwIsisProcBaseGroup": hwIsisProcBaseGroup,
       "hwIsisProcMTExtGroup": hwIsisProcMTExtGroup,
       "hwIsisPrefixPriorityGroup": hwIsisPrefixPriorityGroup,
       "hwIsisSummaryGroup": hwIsisSummaryGroup,
       "hwIsisNETGroup": hwIsisNETGroup,
       "hwIsisImportRouteGroup": hwIsisImportRouteGroup,
       "hwIsisRouteLeakGroup": hwIsisRouteLeakGroup,
       "hwIsisFrrGroup": hwIsisFrrGroup,
       "hwIsisIntfBaseGroup": hwIsisIntfBaseGroup,
       "hwIsisIntfExtGroup": hwIsisIntfExtGroup,
       "hwIsisIntfBfdGroup": hwIsisIntfBfdGroup,
       "hwIsisTrapsObjectsGroup": hwIsisTrapsObjectsGroup,
       "hwIsisTrapsGroup": hwIsisTrapsGroup,
       "hwIsisTraps": hwIsisTraps,
       "hwIsisSystemIdConflict": hwIsisSystemIdConflict,
       "hwIsisL1ImportRouteExceedLimit": hwIsisL1ImportRouteExceedLimit,
       "hwIsisL1ImportRouteRestoreToLimit": hwIsisL1ImportRouteRestoreToLimit,
       "hwIsisL2ImportRouteExceedLimit": hwIsisL2ImportRouteExceedLimit,
       "hwIsisL2ImportRouteRestoreToLimit": hwIsisL2ImportRouteRestoreToLimit,
       "hwIsisL1ImportRouteThresholdReach": hwIsisL1ImportRouteThresholdReach,
       "hwIsisL1ImportRouteThresholdReachClear": hwIsisL1ImportRouteThresholdReachClear,
       "hwIsisL2ImportRouteThresholdReach": hwIsisL2ImportRouteThresholdReach,
       "hwIsisL2ImportRouteThresholdReachClear": hwIsisL2ImportRouteThresholdReachClear,
       "hwIsisLsdbThresholdReach": hwIsisLsdbThresholdReach,
       "hwIsisLsdbThresholdReachClear": hwIsisLsdbThresholdReachClear,
       "hwIsisSystemIdAutoRecover": hwIsisSystemIdAutoRecover,
       "hwIsisAdjacencyChangeClear": hwIsisAdjacencyChangeClear,
       "hwIsisSeqNumExceedThreshold": hwIsisSeqNumExceedThreshold}
)
