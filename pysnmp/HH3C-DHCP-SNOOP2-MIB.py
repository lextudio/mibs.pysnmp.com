# SNMP MIB module (HH3C-DHCP-SNOOP2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-DHCP-SNOOP2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:52:39 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

(InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifIndex")

(InetAddressIPv4,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv4")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hh3cDhcpSnoop2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 124)
)
hh3cDhcpSnoop2.setRevisions(
        ("2013-04-15 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cDhcpSnoop2ScalarObjects_ObjectIdentity = ObjectIdentity
hh3cDhcpSnoop2ScalarObjects = _Hh3cDhcpSnoop2ScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 124, 1)
)
_Hh3cDhcpSnoop2ConfigGroup_ObjectIdentity = ObjectIdentity
hh3cDhcpSnoop2ConfigGroup = _Hh3cDhcpSnoop2ConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 124, 1, 1)
)


class _Hh3cDhcpSnoop2Enabled_Type(TruthValue):
    """Custom type hh3cDhcpSnoop2Enabled based on TruthValue"""


_Hh3cDhcpSnoop2Enabled_Object = MibScalar
hh3cDhcpSnoop2Enabled = _Hh3cDhcpSnoop2Enabled_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 124, 1, 1, 1),
    _Hh3cDhcpSnoop2Enabled_Type()
)
hh3cDhcpSnoop2Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDhcpSnoop2Enabled.setStatus("current")


class _Hh3cDhcpSnoop2BindDbName_Type(OctetString):
    """Custom type hh3cDhcpSnoop2BindDbName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_Hh3cDhcpSnoop2BindDbName_Type.__name__ = "OctetString"
_Hh3cDhcpSnoop2BindDbName_Object = MibScalar
hh3cDhcpSnoop2BindDbName = _Hh3cDhcpSnoop2BindDbName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 124, 1, 1, 2),
    _Hh3cDhcpSnoop2BindDbName_Type()
)
hh3cDhcpSnoop2BindDbName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDhcpSnoop2BindDbName.setStatus("current")


class _Hh3cDhcpSnoop2BindRefreshIntvl_Type(Unsigned32):
    """Custom type hh3cDhcpSnoop2BindRefreshIntvl based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 864000),
    )


_Hh3cDhcpSnoop2BindRefreshIntvl_Type.__name__ = "Unsigned32"
_Hh3cDhcpSnoop2BindRefreshIntvl_Object = MibScalar
hh3cDhcpSnoop2BindRefreshIntvl = _Hh3cDhcpSnoop2BindRefreshIntvl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 124, 1, 1, 3),
    _Hh3cDhcpSnoop2BindRefreshIntvl_Type()
)
hh3cDhcpSnoop2BindRefreshIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDhcpSnoop2BindRefreshIntvl.setStatus("current")


class _Hh3cDhcpSnoop2BindRefresh_Type(Integer32):
    """Custom type hh3cDhcpSnoop2BindRefresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("on", 1)
    )


_Hh3cDhcpSnoop2BindRefresh_Type.__name__ = "Integer32"
_Hh3cDhcpSnoop2BindRefresh_Object = MibScalar
hh3cDhcpSnoop2BindRefresh = _Hh3cDhcpSnoop2BindRefresh_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 124, 1, 1, 4),
    _Hh3cDhcpSnoop2BindRefresh_Type()
)
hh3cDhcpSnoop2BindRefresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDhcpSnoop2BindRefresh.setStatus("current")
_Hh3cDhcpSnoop2StatisticsGroup_ObjectIdentity = ObjectIdentity
hh3cDhcpSnoop2StatisticsGroup = _Hh3cDhcpSnoop2StatisticsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 124, 1, 2)
)
_Hh3cDhcpSnoop2PktSentNum_Type = Counter64
_Hh3cDhcpSnoop2PktSentNum_Object = MibScalar
hh3cDhcpSnoop2PktSentNum = _Hh3cDhcpSnoop2PktSentNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 124, 1, 2, 1),
    _Hh3cDhcpSnoop2PktSentNum_Type()
)
hh3cDhcpSnoop2PktSentNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcpSnoop2PktSentNum.setStatus("current")
_Hh3cDhcpSnoop2PktRcvNum_Type = Counter64
_Hh3cDhcpSnoop2PktRcvNum_Object = MibScalar
hh3cDhcpSnoop2PktRcvNum = _Hh3cDhcpSnoop2PktRcvNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 124, 1, 2, 2),
    _Hh3cDhcpSnoop2PktRcvNum_Type()
)
hh3cDhcpSnoop2PktRcvNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcpSnoop2PktRcvNum.setStatus("current")
_Hh3cDhcpSnoop2PktDropNum_Type = Counter64
_Hh3cDhcpSnoop2PktDropNum_Object = MibScalar
hh3cDhcpSnoop2PktDropNum = _Hh3cDhcpSnoop2PktDropNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 124, 1, 2, 3),
    _Hh3cDhcpSnoop2PktDropNum_Type()
)
hh3cDhcpSnoop2PktDropNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcpSnoop2PktDropNum.setStatus("current")
_Hh3cDhcpSnoop2Tables_ObjectIdentity = ObjectIdentity
hh3cDhcpSnoop2Tables = _Hh3cDhcpSnoop2Tables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 124, 2)
)
_Hh3cDhcpSnoop2BindTable_Object = MibTable
hh3cDhcpSnoop2BindTable = _Hh3cDhcpSnoop2BindTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 124, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cDhcpSnoop2BindTable.setStatus("current")
_Hh3cDhcpSnoop2BindEntry_Object = MibTableRow
hh3cDhcpSnoop2BindEntry = _Hh3cDhcpSnoop2BindEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 124, 2, 1, 1)
)
hh3cDhcpSnoop2BindEntry.setIndexNames(
    (0, "HH3C-DHCP-SNOOP2-MIB", "hh3cDhcpSnoop2BindIpAddr"),
    (0, "HH3C-DHCP-SNOOP2-MIB", "hh3cDhcpSnoop2BindVlanId"),
    (0, "HH3C-DHCP-SNOOP2-MIB", "hh3cDhcpSnoop2BindSecVlanId"),
)
if mibBuilder.loadTexts:
    hh3cDhcpSnoop2BindEntry.setStatus("current")
_Hh3cDhcpSnoop2BindIpAddr_Type = InetAddressIPv4
_Hh3cDhcpSnoop2BindIpAddr_Object = MibTableColumn
hh3cDhcpSnoop2BindIpAddr = _Hh3cDhcpSnoop2BindIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 124, 2, 1, 1, 1),
    _Hh3cDhcpSnoop2BindIpAddr_Type()
)
hh3cDhcpSnoop2BindIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDhcpSnoop2BindIpAddr.setStatus("current")


class _Hh3cDhcpSnoop2BindVlanId_Type(Unsigned32):
    """Custom type hh3cDhcpSnoop2BindVlanId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Hh3cDhcpSnoop2BindVlanId_Type.__name__ = "Unsigned32"
_Hh3cDhcpSnoop2BindVlanId_Object = MibTableColumn
hh3cDhcpSnoop2BindVlanId = _Hh3cDhcpSnoop2BindVlanId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 124, 2, 1, 1, 2),
    _Hh3cDhcpSnoop2BindVlanId_Type()
)
hh3cDhcpSnoop2BindVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDhcpSnoop2BindVlanId.setStatus("current")


class _Hh3cDhcpSnoop2BindSecVlanId_Type(Unsigned32):
    """Custom type hh3cDhcpSnoop2BindSecVlanId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
        ValueRangeConstraint(65535, 65535),
    )


_Hh3cDhcpSnoop2BindSecVlanId_Type.__name__ = "Unsigned32"
_Hh3cDhcpSnoop2BindSecVlanId_Object = MibTableColumn
hh3cDhcpSnoop2BindSecVlanId = _Hh3cDhcpSnoop2BindSecVlanId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 124, 2, 1, 1, 3),
    _Hh3cDhcpSnoop2BindSecVlanId_Type()
)
hh3cDhcpSnoop2BindSecVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDhcpSnoop2BindSecVlanId.setStatus("current")
_Hh3cDhcpSnoop2BindMacAddr_Type = MacAddress
_Hh3cDhcpSnoop2BindMacAddr_Object = MibTableColumn
hh3cDhcpSnoop2BindMacAddr = _Hh3cDhcpSnoop2BindMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 124, 2, 1, 1, 4),
    _Hh3cDhcpSnoop2BindMacAddr_Type()
)
hh3cDhcpSnoop2BindMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcpSnoop2BindMacAddr.setStatus("current")
_Hh3cDhcpSnoop2BindLease_Type = Unsigned32
_Hh3cDhcpSnoop2BindLease_Object = MibTableColumn
hh3cDhcpSnoop2BindLease = _Hh3cDhcpSnoop2BindLease_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 124, 2, 1, 1, 5),
    _Hh3cDhcpSnoop2BindLease_Type()
)
hh3cDhcpSnoop2BindLease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcpSnoop2BindLease.setStatus("current")
_Hh3cDhcpSnoop2BindPortIndex_Type = InterfaceIndexOrZero
_Hh3cDhcpSnoop2BindPortIndex_Object = MibTableColumn
hh3cDhcpSnoop2BindPortIndex = _Hh3cDhcpSnoop2BindPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 124, 2, 1, 1, 6),
    _Hh3cDhcpSnoop2BindPortIndex_Type()
)
hh3cDhcpSnoop2BindPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDhcpSnoop2BindPortIndex.setStatus("current")
_Hh3cDhcpSnoop2BindRowStatus_Type = RowStatus
_Hh3cDhcpSnoop2BindRowStatus_Object = MibTableColumn
hh3cDhcpSnoop2BindRowStatus = _Hh3cDhcpSnoop2BindRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 124, 2, 1, 1, 7),
    _Hh3cDhcpSnoop2BindRowStatus_Type()
)
hh3cDhcpSnoop2BindRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpSnoop2BindRowStatus.setStatus("current")
_Hh3cDhcpSnoop2IfConfigTable_Object = MibTable
hh3cDhcpSnoop2IfConfigTable = _Hh3cDhcpSnoop2IfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 124, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cDhcpSnoop2IfConfigTable.setStatus("current")
_Hh3cDhcpSnoop2IfConfigEntry_Object = MibTableRow
hh3cDhcpSnoop2IfConfigEntry = _Hh3cDhcpSnoop2IfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 124, 2, 2, 1)
)
hh3cDhcpSnoop2IfConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cDhcpSnoop2IfConfigEntry.setStatus("current")


class _Hh3cDhcpSnoop2IfTrustStatus_Type(Integer32):
    """Custom type hh3cDhcpSnoop2IfTrustStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("trusted", 1),
          ("untrusted", 0))
    )


_Hh3cDhcpSnoop2IfTrustStatus_Type.__name__ = "Integer32"
_Hh3cDhcpSnoop2IfTrustStatus_Object = MibTableColumn
hh3cDhcpSnoop2IfTrustStatus = _Hh3cDhcpSnoop2IfTrustStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 124, 2, 2, 1, 1),
    _Hh3cDhcpSnoop2IfTrustStatus_Type()
)
hh3cDhcpSnoop2IfTrustStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDhcpSnoop2IfTrustStatus.setStatus("current")


class _Hh3cDhcpSnoop2IfCheckMac_Type(TruthValue):
    """Custom type hh3cDhcpSnoop2IfCheckMac based on TruthValue"""


_Hh3cDhcpSnoop2IfCheckMac_Object = MibTableColumn
hh3cDhcpSnoop2IfCheckMac = _Hh3cDhcpSnoop2IfCheckMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 124, 2, 2, 1, 2),
    _Hh3cDhcpSnoop2IfCheckMac_Type()
)
hh3cDhcpSnoop2IfCheckMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDhcpSnoop2IfCheckMac.setStatus("current")


class _Hh3cDhcpSnoop2IfCheckRequest_Type(TruthValue):
    """Custom type hh3cDhcpSnoop2IfCheckRequest based on TruthValue"""


_Hh3cDhcpSnoop2IfCheckRequest_Object = MibTableColumn
hh3cDhcpSnoop2IfCheckRequest = _Hh3cDhcpSnoop2IfCheckRequest_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 124, 2, 2, 1, 3),
    _Hh3cDhcpSnoop2IfCheckRequest_Type()
)
hh3cDhcpSnoop2IfCheckRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDhcpSnoop2IfCheckRequest.setStatus("current")


class _Hh3cDhcpSnoop2IfRateLimit_Type(Unsigned32):
    """Custom type hh3cDhcpSnoop2IfRateLimit based on Unsigned32"""
    defaultValue = 0


_Hh3cDhcpSnoop2IfRateLimit_Object = MibTableColumn
hh3cDhcpSnoop2IfRateLimit = _Hh3cDhcpSnoop2IfRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 124, 2, 2, 1, 4),
    _Hh3cDhcpSnoop2IfRateLimit_Type()
)
hh3cDhcpSnoop2IfRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDhcpSnoop2IfRateLimit.setStatus("current")


class _Hh3cDhcpSnoop2IfRecordBind_Type(TruthValue):
    """Custom type hh3cDhcpSnoop2IfRecordBind based on TruthValue"""


_Hh3cDhcpSnoop2IfRecordBind_Object = MibTableColumn
hh3cDhcpSnoop2IfRecordBind = _Hh3cDhcpSnoop2IfRecordBind_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 124, 2, 2, 1, 5),
    _Hh3cDhcpSnoop2IfRecordBind_Type()
)
hh3cDhcpSnoop2IfRecordBind.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDhcpSnoop2IfRecordBind.setStatus("current")


class _Hh3cDhcpSnoop2IfMaxLearnNum_Type(Unsigned32):
    """Custom type hh3cDhcpSnoop2IfMaxLearnNum based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Hh3cDhcpSnoop2IfMaxLearnNum_Type.__name__ = "Unsigned32"
_Hh3cDhcpSnoop2IfMaxLearnNum_Object = MibTableColumn
hh3cDhcpSnoop2IfMaxLearnNum = _Hh3cDhcpSnoop2IfMaxLearnNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 124, 2, 2, 1, 6),
    _Hh3cDhcpSnoop2IfMaxLearnNum_Type()
)
hh3cDhcpSnoop2IfMaxLearnNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDhcpSnoop2IfMaxLearnNum.setStatus("current")


class _Hh3cDhcpSnoop2IfOpt82Enable_Type(TruthValue):
    """Custom type hh3cDhcpSnoop2IfOpt82Enable based on TruthValue"""


_Hh3cDhcpSnoop2IfOpt82Enable_Object = MibTableColumn
hh3cDhcpSnoop2IfOpt82Enable = _Hh3cDhcpSnoop2IfOpt82Enable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 124, 2, 2, 1, 7),
    _Hh3cDhcpSnoop2IfOpt82Enable_Type()
)
hh3cDhcpSnoop2IfOpt82Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDhcpSnoop2IfOpt82Enable.setStatus("current")


class _Hh3cDhcpSnoop2IfOpt82Strategy_Type(Integer32):
    """Custom type hh3cDhcpSnoop2IfOpt82Strategy based on Integer32"""
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
        *(("drop", 1),
          ("keep", 2),
          ("replace", 3))
    )


_Hh3cDhcpSnoop2IfOpt82Strategy_Type.__name__ = "Integer32"
_Hh3cDhcpSnoop2IfOpt82Strategy_Object = MibTableColumn
hh3cDhcpSnoop2IfOpt82Strategy = _Hh3cDhcpSnoop2IfOpt82Strategy_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 124, 2, 2, 1, 8),
    _Hh3cDhcpSnoop2IfOpt82Strategy_Type()
)
hh3cDhcpSnoop2IfOpt82Strategy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDhcpSnoop2IfOpt82Strategy.setStatus("current")


class _Hh3cDhcpSnoop2IfOpt82CIDMode_Type(Integer32):
    """Custom type hh3cDhcpSnoop2IfOpt82CIDMode based on Integer32"""
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
        *(("normal", 1),
          ("userDefine", 3),
          ("verbose", 2))
    )


_Hh3cDhcpSnoop2IfOpt82CIDMode_Type.__name__ = "Integer32"
_Hh3cDhcpSnoop2IfOpt82CIDMode_Object = MibTableColumn
hh3cDhcpSnoop2IfOpt82CIDMode = _Hh3cDhcpSnoop2IfOpt82CIDMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 124, 2, 2, 1, 9),
    _Hh3cDhcpSnoop2IfOpt82CIDMode_Type()
)
hh3cDhcpSnoop2IfOpt82CIDMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDhcpSnoop2IfOpt82CIDMode.setStatus("current")


class _Hh3cDhcpSnoop2IfOpt82CIDNodeType_Type(Integer32):
    """Custom type hh3cDhcpSnoop2IfOpt82CIDNodeType based on Integer32"""
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
        *(("invalid", 1),
          ("mac", 2),
          ("sysname", 3),
          ("userDefine", 4))
    )


_Hh3cDhcpSnoop2IfOpt82CIDNodeType_Type.__name__ = "Integer32"
_Hh3cDhcpSnoop2IfOpt82CIDNodeType_Object = MibTableColumn
hh3cDhcpSnoop2IfOpt82CIDNodeType = _Hh3cDhcpSnoop2IfOpt82CIDNodeType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 124, 2, 2, 1, 10),
    _Hh3cDhcpSnoop2IfOpt82CIDNodeType_Type()
)
hh3cDhcpSnoop2IfOpt82CIDNodeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDhcpSnoop2IfOpt82CIDNodeType.setStatus("current")


class _Hh3cDhcpSnoop2IfOpt82CIDNodeStr_Type(OctetString):
    """Custom type hh3cDhcpSnoop2IfOpt82CIDNodeStr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_Hh3cDhcpSnoop2IfOpt82CIDNodeStr_Type.__name__ = "OctetString"
_Hh3cDhcpSnoop2IfOpt82CIDNodeStr_Object = MibTableColumn
hh3cDhcpSnoop2IfOpt82CIDNodeStr = _Hh3cDhcpSnoop2IfOpt82CIDNodeStr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 124, 2, 2, 1, 11),
    _Hh3cDhcpSnoop2IfOpt82CIDNodeStr_Type()
)
hh3cDhcpSnoop2IfOpt82CIDNodeStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDhcpSnoop2IfOpt82CIDNodeStr.setStatus("current")


class _Hh3cDhcpSnoop2IfOpt82CIDStr_Type(OctetString):
    """Custom type hh3cDhcpSnoop2IfOpt82CIDStr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(3, 63),
    )


_Hh3cDhcpSnoop2IfOpt82CIDStr_Type.__name__ = "OctetString"
_Hh3cDhcpSnoop2IfOpt82CIDStr_Object = MibTableColumn
hh3cDhcpSnoop2IfOpt82CIDStr = _Hh3cDhcpSnoop2IfOpt82CIDStr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 124, 2, 2, 1, 12),
    _Hh3cDhcpSnoop2IfOpt82CIDStr_Type()
)
hh3cDhcpSnoop2IfOpt82CIDStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDhcpSnoop2IfOpt82CIDStr.setStatus("current")


class _Hh3cDhcpSnoop2IfOpt82CIDFormat_Type(Integer32):
    """Custom type hh3cDhcpSnoop2IfOpt82CIDFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 2),
          ("hex", 1),
          ("undefine", 3))
    )


_Hh3cDhcpSnoop2IfOpt82CIDFormat_Type.__name__ = "Integer32"
_Hh3cDhcpSnoop2IfOpt82CIDFormat_Object = MibTableColumn
hh3cDhcpSnoop2IfOpt82CIDFormat = _Hh3cDhcpSnoop2IfOpt82CIDFormat_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 124, 2, 2, 1, 13),
    _Hh3cDhcpSnoop2IfOpt82CIDFormat_Type()
)
hh3cDhcpSnoop2IfOpt82CIDFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDhcpSnoop2IfOpt82CIDFormat.setStatus("current")


class _Hh3cDhcpSnoop2IfOpt82RIDMode_Type(Integer32):
    """Custom type hh3cDhcpSnoop2IfOpt82RIDMode based on Integer32"""
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
        *(("normal", 1),
          ("sysname", 2),
          ("userDefine", 3))
    )


_Hh3cDhcpSnoop2IfOpt82RIDMode_Type.__name__ = "Integer32"
_Hh3cDhcpSnoop2IfOpt82RIDMode_Object = MibTableColumn
hh3cDhcpSnoop2IfOpt82RIDMode = _Hh3cDhcpSnoop2IfOpt82RIDMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 124, 2, 2, 1, 14),
    _Hh3cDhcpSnoop2IfOpt82RIDMode_Type()
)
hh3cDhcpSnoop2IfOpt82RIDMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDhcpSnoop2IfOpt82RIDMode.setStatus("current")


class _Hh3cDhcpSnoop2IfOpt82RIDStr_Type(OctetString):
    """Custom type hh3cDhcpSnoop2IfOpt82RIDStr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Hh3cDhcpSnoop2IfOpt82RIDStr_Type.__name__ = "OctetString"
_Hh3cDhcpSnoop2IfOpt82RIDStr_Object = MibTableColumn
hh3cDhcpSnoop2IfOpt82RIDStr = _Hh3cDhcpSnoop2IfOpt82RIDStr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 124, 2, 2, 1, 15),
    _Hh3cDhcpSnoop2IfOpt82RIDStr_Type()
)
hh3cDhcpSnoop2IfOpt82RIDStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDhcpSnoop2IfOpt82RIDStr.setStatus("current")


class _Hh3cDhcpSnoop2IfOpt82RIDFormat_Type(Integer32):
    """Custom type hh3cDhcpSnoop2IfOpt82RIDFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 2),
          ("hex", 1))
    )


_Hh3cDhcpSnoop2IfOpt82RIDFormat_Type.__name__ = "Integer32"
_Hh3cDhcpSnoop2IfOpt82RIDFormat_Object = MibTableColumn
hh3cDhcpSnoop2IfOpt82RIDFormat = _Hh3cDhcpSnoop2IfOpt82RIDFormat_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 124, 2, 2, 1, 16),
    _Hh3cDhcpSnoop2IfOpt82RIDFormat_Type()
)
hh3cDhcpSnoop2IfOpt82RIDFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDhcpSnoop2IfOpt82RIDFormat.setStatus("current")
_Hh3cDhcpSnoop2IfVlanCIDTable_Object = MibTable
hh3cDhcpSnoop2IfVlanCIDTable = _Hh3cDhcpSnoop2IfVlanCIDTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 124, 2, 3)
)
if mibBuilder.loadTexts:
    hh3cDhcpSnoop2IfVlanCIDTable.setStatus("current")
_Hh3cDhcpSnoop2IfVlanCIDEntry_Object = MibTableRow
hh3cDhcpSnoop2IfVlanCIDEntry = _Hh3cDhcpSnoop2IfVlanCIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 124, 2, 3, 1)
)
hh3cDhcpSnoop2IfVlanCIDEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-DHCP-SNOOP2-MIB", "hh3cDhcpSnoop2IfVlanCIDVlanIndex"),
)
if mibBuilder.loadTexts:
    hh3cDhcpSnoop2IfVlanCIDEntry.setStatus("current")


class _Hh3cDhcpSnoop2IfVlanCIDVlanIndex_Type(Unsigned32):
    """Custom type hh3cDhcpSnoop2IfVlanCIDVlanIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Hh3cDhcpSnoop2IfVlanCIDVlanIndex_Type.__name__ = "Unsigned32"
_Hh3cDhcpSnoop2IfVlanCIDVlanIndex_Object = MibTableColumn
hh3cDhcpSnoop2IfVlanCIDVlanIndex = _Hh3cDhcpSnoop2IfVlanCIDVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 124, 2, 3, 1, 1),
    _Hh3cDhcpSnoop2IfVlanCIDVlanIndex_Type()
)
hh3cDhcpSnoop2IfVlanCIDVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDhcpSnoop2IfVlanCIDVlanIndex.setStatus("current")


class _Hh3cDhcpSnoop2IfVlanCIDStr_Type(OctetString):
    """Custom type hh3cDhcpSnoop2IfVlanCIDStr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 63),
    )


_Hh3cDhcpSnoop2IfVlanCIDStr_Type.__name__ = "OctetString"
_Hh3cDhcpSnoop2IfVlanCIDStr_Object = MibTableColumn
hh3cDhcpSnoop2IfVlanCIDStr = _Hh3cDhcpSnoop2IfVlanCIDStr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 124, 2, 3, 1, 2),
    _Hh3cDhcpSnoop2IfVlanCIDStr_Type()
)
hh3cDhcpSnoop2IfVlanCIDStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpSnoop2IfVlanCIDStr.setStatus("current")
_Hh3cDhcpSnoop2IfVlanCIDRowStatus_Type = RowStatus
_Hh3cDhcpSnoop2IfVlanCIDRowStatus_Object = MibTableColumn
hh3cDhcpSnoop2IfVlanCIDRowStatus = _Hh3cDhcpSnoop2IfVlanCIDRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 124, 2, 3, 1, 3),
    _Hh3cDhcpSnoop2IfVlanCIDRowStatus_Type()
)
hh3cDhcpSnoop2IfVlanCIDRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpSnoop2IfVlanCIDRowStatus.setStatus("current")
_Hh3cDhcpSnoop2IfVlanRIDTable_Object = MibTable
hh3cDhcpSnoop2IfVlanRIDTable = _Hh3cDhcpSnoop2IfVlanRIDTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 124, 2, 4)
)
if mibBuilder.loadTexts:
    hh3cDhcpSnoop2IfVlanRIDTable.setStatus("current")
_Hh3cDhcpSnoop2IfVlanRIDEntry_Object = MibTableRow
hh3cDhcpSnoop2IfVlanRIDEntry = _Hh3cDhcpSnoop2IfVlanRIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 124, 2, 4, 1)
)
hh3cDhcpSnoop2IfVlanRIDEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-DHCP-SNOOP2-MIB", "hh3cDhcpSnoop2IfVlanRIDVlanIndex"),
)
if mibBuilder.loadTexts:
    hh3cDhcpSnoop2IfVlanRIDEntry.setStatus("current")


class _Hh3cDhcpSnoop2IfVlanRIDVlanIndex_Type(Unsigned32):
    """Custom type hh3cDhcpSnoop2IfVlanRIDVlanIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Hh3cDhcpSnoop2IfVlanRIDVlanIndex_Type.__name__ = "Unsigned32"
_Hh3cDhcpSnoop2IfVlanRIDVlanIndex_Object = MibTableColumn
hh3cDhcpSnoop2IfVlanRIDVlanIndex = _Hh3cDhcpSnoop2IfVlanRIDVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 124, 2, 4, 1, 1),
    _Hh3cDhcpSnoop2IfVlanRIDVlanIndex_Type()
)
hh3cDhcpSnoop2IfVlanRIDVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDhcpSnoop2IfVlanRIDVlanIndex.setStatus("current")


class _Hh3cDhcpSnoop2IfVlanRIDMode_Type(Integer32):
    """Custom type hh3cDhcpSnoop2IfVlanRIDMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sysname", 1),
          ("userDefine", 2))
    )


_Hh3cDhcpSnoop2IfVlanRIDMode_Type.__name__ = "Integer32"
_Hh3cDhcpSnoop2IfVlanRIDMode_Object = MibTableColumn
hh3cDhcpSnoop2IfVlanRIDMode = _Hh3cDhcpSnoop2IfVlanRIDMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 124, 2, 4, 1, 2),
    _Hh3cDhcpSnoop2IfVlanRIDMode_Type()
)
hh3cDhcpSnoop2IfVlanRIDMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpSnoop2IfVlanRIDMode.setStatus("current")


class _Hh3cDhcpSnoop2IfVlanRIDStr_Type(OctetString):
    """Custom type hh3cDhcpSnoop2IfVlanRIDStr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Hh3cDhcpSnoop2IfVlanRIDStr_Type.__name__ = "OctetString"
_Hh3cDhcpSnoop2IfVlanRIDStr_Object = MibTableColumn
hh3cDhcpSnoop2IfVlanRIDStr = _Hh3cDhcpSnoop2IfVlanRIDStr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 124, 2, 4, 1, 3),
    _Hh3cDhcpSnoop2IfVlanRIDStr_Type()
)
hh3cDhcpSnoop2IfVlanRIDStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpSnoop2IfVlanRIDStr.setStatus("current")
_Hh3cDhcpSnoop2IfVlanRIDRowStatus_Type = RowStatus
_Hh3cDhcpSnoop2IfVlanRIDRowStatus_Object = MibTableColumn
hh3cDhcpSnoop2IfVlanRIDRowStatus = _Hh3cDhcpSnoop2IfVlanRIDRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 124, 2, 4, 1, 4),
    _Hh3cDhcpSnoop2IfVlanRIDRowStatus_Type()
)
hh3cDhcpSnoop2IfVlanRIDRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDhcpSnoop2IfVlanRIDRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-DHCP-SNOOP2-MIB",
    **{"hh3cDhcpSnoop2": hh3cDhcpSnoop2,
       "hh3cDhcpSnoop2ScalarObjects": hh3cDhcpSnoop2ScalarObjects,
       "hh3cDhcpSnoop2ConfigGroup": hh3cDhcpSnoop2ConfigGroup,
       "hh3cDhcpSnoop2Enabled": hh3cDhcpSnoop2Enabled,
       "hh3cDhcpSnoop2BindDbName": hh3cDhcpSnoop2BindDbName,
       "hh3cDhcpSnoop2BindRefreshIntvl": hh3cDhcpSnoop2BindRefreshIntvl,
       "hh3cDhcpSnoop2BindRefresh": hh3cDhcpSnoop2BindRefresh,
       "hh3cDhcpSnoop2StatisticsGroup": hh3cDhcpSnoop2StatisticsGroup,
       "hh3cDhcpSnoop2PktSentNum": hh3cDhcpSnoop2PktSentNum,
       "hh3cDhcpSnoop2PktRcvNum": hh3cDhcpSnoop2PktRcvNum,
       "hh3cDhcpSnoop2PktDropNum": hh3cDhcpSnoop2PktDropNum,
       "hh3cDhcpSnoop2Tables": hh3cDhcpSnoop2Tables,
       "hh3cDhcpSnoop2BindTable": hh3cDhcpSnoop2BindTable,
       "hh3cDhcpSnoop2BindEntry": hh3cDhcpSnoop2BindEntry,
       "hh3cDhcpSnoop2BindIpAddr": hh3cDhcpSnoop2BindIpAddr,
       "hh3cDhcpSnoop2BindVlanId": hh3cDhcpSnoop2BindVlanId,
       "hh3cDhcpSnoop2BindSecVlanId": hh3cDhcpSnoop2BindSecVlanId,
       "hh3cDhcpSnoop2BindMacAddr": hh3cDhcpSnoop2BindMacAddr,
       "hh3cDhcpSnoop2BindLease": hh3cDhcpSnoop2BindLease,
       "hh3cDhcpSnoop2BindPortIndex": hh3cDhcpSnoop2BindPortIndex,
       "hh3cDhcpSnoop2BindRowStatus": hh3cDhcpSnoop2BindRowStatus,
       "hh3cDhcpSnoop2IfConfigTable": hh3cDhcpSnoop2IfConfigTable,
       "hh3cDhcpSnoop2IfConfigEntry": hh3cDhcpSnoop2IfConfigEntry,
       "hh3cDhcpSnoop2IfTrustStatus": hh3cDhcpSnoop2IfTrustStatus,
       "hh3cDhcpSnoop2IfCheckMac": hh3cDhcpSnoop2IfCheckMac,
       "hh3cDhcpSnoop2IfCheckRequest": hh3cDhcpSnoop2IfCheckRequest,
       "hh3cDhcpSnoop2IfRateLimit": hh3cDhcpSnoop2IfRateLimit,
       "hh3cDhcpSnoop2IfRecordBind": hh3cDhcpSnoop2IfRecordBind,
       "hh3cDhcpSnoop2IfMaxLearnNum": hh3cDhcpSnoop2IfMaxLearnNum,
       "hh3cDhcpSnoop2IfOpt82Enable": hh3cDhcpSnoop2IfOpt82Enable,
       "hh3cDhcpSnoop2IfOpt82Strategy": hh3cDhcpSnoop2IfOpt82Strategy,
       "hh3cDhcpSnoop2IfOpt82CIDMode": hh3cDhcpSnoop2IfOpt82CIDMode,
       "hh3cDhcpSnoop2IfOpt82CIDNodeType": hh3cDhcpSnoop2IfOpt82CIDNodeType,
       "hh3cDhcpSnoop2IfOpt82CIDNodeStr": hh3cDhcpSnoop2IfOpt82CIDNodeStr,
       "hh3cDhcpSnoop2IfOpt82CIDStr": hh3cDhcpSnoop2IfOpt82CIDStr,
       "hh3cDhcpSnoop2IfOpt82CIDFormat": hh3cDhcpSnoop2IfOpt82CIDFormat,
       "hh3cDhcpSnoop2IfOpt82RIDMode": hh3cDhcpSnoop2IfOpt82RIDMode,
       "hh3cDhcpSnoop2IfOpt82RIDStr": hh3cDhcpSnoop2IfOpt82RIDStr,
       "hh3cDhcpSnoop2IfOpt82RIDFormat": hh3cDhcpSnoop2IfOpt82RIDFormat,
       "hh3cDhcpSnoop2IfVlanCIDTable": hh3cDhcpSnoop2IfVlanCIDTable,
       "hh3cDhcpSnoop2IfVlanCIDEntry": hh3cDhcpSnoop2IfVlanCIDEntry,
       "hh3cDhcpSnoop2IfVlanCIDVlanIndex": hh3cDhcpSnoop2IfVlanCIDVlanIndex,
       "hh3cDhcpSnoop2IfVlanCIDStr": hh3cDhcpSnoop2IfVlanCIDStr,
       "hh3cDhcpSnoop2IfVlanCIDRowStatus": hh3cDhcpSnoop2IfVlanCIDRowStatus,
       "hh3cDhcpSnoop2IfVlanRIDTable": hh3cDhcpSnoop2IfVlanRIDTable,
       "hh3cDhcpSnoop2IfVlanRIDEntry": hh3cDhcpSnoop2IfVlanRIDEntry,
       "hh3cDhcpSnoop2IfVlanRIDVlanIndex": hh3cDhcpSnoop2IfVlanRIDVlanIndex,
       "hh3cDhcpSnoop2IfVlanRIDMode": hh3cDhcpSnoop2IfVlanRIDMode,
       "hh3cDhcpSnoop2IfVlanRIDStr": hh3cDhcpSnoop2IfVlanRIDStr,
       "hh3cDhcpSnoop2IfVlanRIDRowStatus": hh3cDhcpSnoop2IfVlanRIDRowStatus}
)
