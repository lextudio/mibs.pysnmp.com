# SNMP MIB module (HPN-ICF-DHCP-SNOOP2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-DHCP-SNOOP2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:59:39 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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

hpnicfDhcpSnoop2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 124)
)
hpnicfDhcpSnoop2.setRevisions(
        ("2013-04-15 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfDhcpSnoop2ScalarObjects_ObjectIdentity = ObjectIdentity
hpnicfDhcpSnoop2ScalarObjects = _HpnicfDhcpSnoop2ScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 124, 1)
)
_HpnicfDhcpSnoop2ConfigGroup_ObjectIdentity = ObjectIdentity
hpnicfDhcpSnoop2ConfigGroup = _HpnicfDhcpSnoop2ConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 124, 1, 1)
)


class _HpnicfDhcpSnoop2Enabled_Type(TruthValue):
    """Custom type hpnicfDhcpSnoop2Enabled based on TruthValue"""


_HpnicfDhcpSnoop2Enabled_Object = MibScalar
hpnicfDhcpSnoop2Enabled = _HpnicfDhcpSnoop2Enabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 124, 1, 1, 1),
    _HpnicfDhcpSnoop2Enabled_Type()
)
hpnicfDhcpSnoop2Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDhcpSnoop2Enabled.setStatus("current")


class _HpnicfDhcpSnoop2BindDbName_Type(OctetString):
    """Custom type hpnicfDhcpSnoop2BindDbName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_HpnicfDhcpSnoop2BindDbName_Type.__name__ = "OctetString"
_HpnicfDhcpSnoop2BindDbName_Object = MibScalar
hpnicfDhcpSnoop2BindDbName = _HpnicfDhcpSnoop2BindDbName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 124, 1, 1, 2),
    _HpnicfDhcpSnoop2BindDbName_Type()
)
hpnicfDhcpSnoop2BindDbName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDhcpSnoop2BindDbName.setStatus("current")


class _HpnicfDhcpSnoop2BindRefreshIntvl_Type(Unsigned32):
    """Custom type hpnicfDhcpSnoop2BindRefreshIntvl based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 864000),
    )


_HpnicfDhcpSnoop2BindRefreshIntvl_Type.__name__ = "Unsigned32"
_HpnicfDhcpSnoop2BindRefreshIntvl_Object = MibScalar
hpnicfDhcpSnoop2BindRefreshIntvl = _HpnicfDhcpSnoop2BindRefreshIntvl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 124, 1, 1, 3),
    _HpnicfDhcpSnoop2BindRefreshIntvl_Type()
)
hpnicfDhcpSnoop2BindRefreshIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDhcpSnoop2BindRefreshIntvl.setStatus("current")


class _HpnicfDhcpSnoop2BindRefresh_Type(Integer32):
    """Custom type hpnicfDhcpSnoop2BindRefresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("on", 1)
    )


_HpnicfDhcpSnoop2BindRefresh_Type.__name__ = "Integer32"
_HpnicfDhcpSnoop2BindRefresh_Object = MibScalar
hpnicfDhcpSnoop2BindRefresh = _HpnicfDhcpSnoop2BindRefresh_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 124, 1, 1, 4),
    _HpnicfDhcpSnoop2BindRefresh_Type()
)
hpnicfDhcpSnoop2BindRefresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDhcpSnoop2BindRefresh.setStatus("current")
_HpnicfDhcpSnoop2StatisticsGroup_ObjectIdentity = ObjectIdentity
hpnicfDhcpSnoop2StatisticsGroup = _HpnicfDhcpSnoop2StatisticsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 124, 1, 2)
)
_HpnicfDhcpSnoop2PktSentNum_Type = Counter64
_HpnicfDhcpSnoop2PktSentNum_Object = MibScalar
hpnicfDhcpSnoop2PktSentNum = _HpnicfDhcpSnoop2PktSentNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 124, 1, 2, 1),
    _HpnicfDhcpSnoop2PktSentNum_Type()
)
hpnicfDhcpSnoop2PktSentNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDhcpSnoop2PktSentNum.setStatus("current")
_HpnicfDhcpSnoop2PktRcvNum_Type = Counter64
_HpnicfDhcpSnoop2PktRcvNum_Object = MibScalar
hpnicfDhcpSnoop2PktRcvNum = _HpnicfDhcpSnoop2PktRcvNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 124, 1, 2, 2),
    _HpnicfDhcpSnoop2PktRcvNum_Type()
)
hpnicfDhcpSnoop2PktRcvNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDhcpSnoop2PktRcvNum.setStatus("current")
_HpnicfDhcpSnoop2PktDropNum_Type = Counter64
_HpnicfDhcpSnoop2PktDropNum_Object = MibScalar
hpnicfDhcpSnoop2PktDropNum = _HpnicfDhcpSnoop2PktDropNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 124, 1, 2, 3),
    _HpnicfDhcpSnoop2PktDropNum_Type()
)
hpnicfDhcpSnoop2PktDropNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDhcpSnoop2PktDropNum.setStatus("current")
_HpnicfDhcpSnoop2Tables_ObjectIdentity = ObjectIdentity
hpnicfDhcpSnoop2Tables = _HpnicfDhcpSnoop2Tables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 124, 2)
)
_HpnicfDhcpSnoop2BindTable_Object = MibTable
hpnicfDhcpSnoop2BindTable = _HpnicfDhcpSnoop2BindTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 124, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfDhcpSnoop2BindTable.setStatus("current")
_HpnicfDhcpSnoop2BindEntry_Object = MibTableRow
hpnicfDhcpSnoop2BindEntry = _HpnicfDhcpSnoop2BindEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 124, 2, 1, 1)
)
hpnicfDhcpSnoop2BindEntry.setIndexNames(
    (0, "HPN-ICF-DHCP-SNOOP2-MIB", "hpnicfDhcpSnoop2BindIpAddr"),
    (0, "HPN-ICF-DHCP-SNOOP2-MIB", "hpnicfDhcpSnoop2BindVlanId"),
    (0, "HPN-ICF-DHCP-SNOOP2-MIB", "hpnicfDhcpSnoop2BindSecVlanId"),
)
if mibBuilder.loadTexts:
    hpnicfDhcpSnoop2BindEntry.setStatus("current")
_HpnicfDhcpSnoop2BindIpAddr_Type = InetAddressIPv4
_HpnicfDhcpSnoop2BindIpAddr_Object = MibTableColumn
hpnicfDhcpSnoop2BindIpAddr = _HpnicfDhcpSnoop2BindIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 124, 2, 1, 1, 1),
    _HpnicfDhcpSnoop2BindIpAddr_Type()
)
hpnicfDhcpSnoop2BindIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDhcpSnoop2BindIpAddr.setStatus("current")


class _HpnicfDhcpSnoop2BindVlanId_Type(Unsigned32):
    """Custom type hpnicfDhcpSnoop2BindVlanId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HpnicfDhcpSnoop2BindVlanId_Type.__name__ = "Unsigned32"
_HpnicfDhcpSnoop2BindVlanId_Object = MibTableColumn
hpnicfDhcpSnoop2BindVlanId = _HpnicfDhcpSnoop2BindVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 124, 2, 1, 1, 2),
    _HpnicfDhcpSnoop2BindVlanId_Type()
)
hpnicfDhcpSnoop2BindVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDhcpSnoop2BindVlanId.setStatus("current")


class _HpnicfDhcpSnoop2BindSecVlanId_Type(Unsigned32):
    """Custom type hpnicfDhcpSnoop2BindSecVlanId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
        ValueRangeConstraint(65535, 65535),
    )


_HpnicfDhcpSnoop2BindSecVlanId_Type.__name__ = "Unsigned32"
_HpnicfDhcpSnoop2BindSecVlanId_Object = MibTableColumn
hpnicfDhcpSnoop2BindSecVlanId = _HpnicfDhcpSnoop2BindSecVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 124, 2, 1, 1, 3),
    _HpnicfDhcpSnoop2BindSecVlanId_Type()
)
hpnicfDhcpSnoop2BindSecVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDhcpSnoop2BindSecVlanId.setStatus("current")
_HpnicfDhcpSnoop2BindMacAddr_Type = MacAddress
_HpnicfDhcpSnoop2BindMacAddr_Object = MibTableColumn
hpnicfDhcpSnoop2BindMacAddr = _HpnicfDhcpSnoop2BindMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 124, 2, 1, 1, 4),
    _HpnicfDhcpSnoop2BindMacAddr_Type()
)
hpnicfDhcpSnoop2BindMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDhcpSnoop2BindMacAddr.setStatus("current")
_HpnicfDhcpSnoop2BindLease_Type = Unsigned32
_HpnicfDhcpSnoop2BindLease_Object = MibTableColumn
hpnicfDhcpSnoop2BindLease = _HpnicfDhcpSnoop2BindLease_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 124, 2, 1, 1, 5),
    _HpnicfDhcpSnoop2BindLease_Type()
)
hpnicfDhcpSnoop2BindLease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDhcpSnoop2BindLease.setStatus("current")
_HpnicfDhcpSnoop2BindPortIndex_Type = InterfaceIndexOrZero
_HpnicfDhcpSnoop2BindPortIndex_Object = MibTableColumn
hpnicfDhcpSnoop2BindPortIndex = _HpnicfDhcpSnoop2BindPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 124, 2, 1, 1, 6),
    _HpnicfDhcpSnoop2BindPortIndex_Type()
)
hpnicfDhcpSnoop2BindPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDhcpSnoop2BindPortIndex.setStatus("current")
_HpnicfDhcpSnoop2BindRowStatus_Type = RowStatus
_HpnicfDhcpSnoop2BindRowStatus_Object = MibTableColumn
hpnicfDhcpSnoop2BindRowStatus = _HpnicfDhcpSnoop2BindRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 124, 2, 1, 1, 7),
    _HpnicfDhcpSnoop2BindRowStatus_Type()
)
hpnicfDhcpSnoop2BindRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpSnoop2BindRowStatus.setStatus("current")
_HpnicfDhcpSnoop2IfConfigTable_Object = MibTable
hpnicfDhcpSnoop2IfConfigTable = _HpnicfDhcpSnoop2IfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 124, 2, 2)
)
if mibBuilder.loadTexts:
    hpnicfDhcpSnoop2IfConfigTable.setStatus("current")
_HpnicfDhcpSnoop2IfConfigEntry_Object = MibTableRow
hpnicfDhcpSnoop2IfConfigEntry = _HpnicfDhcpSnoop2IfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 124, 2, 2, 1)
)
hpnicfDhcpSnoop2IfConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfDhcpSnoop2IfConfigEntry.setStatus("current")


class _HpnicfDhcpSnoop2IfTrustStatus_Type(Integer32):
    """Custom type hpnicfDhcpSnoop2IfTrustStatus based on Integer32"""
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


_HpnicfDhcpSnoop2IfTrustStatus_Type.__name__ = "Integer32"
_HpnicfDhcpSnoop2IfTrustStatus_Object = MibTableColumn
hpnicfDhcpSnoop2IfTrustStatus = _HpnicfDhcpSnoop2IfTrustStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 124, 2, 2, 1, 1),
    _HpnicfDhcpSnoop2IfTrustStatus_Type()
)
hpnicfDhcpSnoop2IfTrustStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDhcpSnoop2IfTrustStatus.setStatus("current")


class _HpnicfDhcpSnoop2IfCheckMac_Type(TruthValue):
    """Custom type hpnicfDhcpSnoop2IfCheckMac based on TruthValue"""


_HpnicfDhcpSnoop2IfCheckMac_Object = MibTableColumn
hpnicfDhcpSnoop2IfCheckMac = _HpnicfDhcpSnoop2IfCheckMac_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 124, 2, 2, 1, 2),
    _HpnicfDhcpSnoop2IfCheckMac_Type()
)
hpnicfDhcpSnoop2IfCheckMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDhcpSnoop2IfCheckMac.setStatus("current")


class _HpnicfDhcpSnoop2IfCheckRequest_Type(TruthValue):
    """Custom type hpnicfDhcpSnoop2IfCheckRequest based on TruthValue"""


_HpnicfDhcpSnoop2IfCheckRequest_Object = MibTableColumn
hpnicfDhcpSnoop2IfCheckRequest = _HpnicfDhcpSnoop2IfCheckRequest_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 124, 2, 2, 1, 3),
    _HpnicfDhcpSnoop2IfCheckRequest_Type()
)
hpnicfDhcpSnoop2IfCheckRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDhcpSnoop2IfCheckRequest.setStatus("current")


class _HpnicfDhcpSnoop2IfRateLimit_Type(Unsigned32):
    """Custom type hpnicfDhcpSnoop2IfRateLimit based on Unsigned32"""
    defaultValue = 0


_HpnicfDhcpSnoop2IfRateLimit_Object = MibTableColumn
hpnicfDhcpSnoop2IfRateLimit = _HpnicfDhcpSnoop2IfRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 124, 2, 2, 1, 4),
    _HpnicfDhcpSnoop2IfRateLimit_Type()
)
hpnicfDhcpSnoop2IfRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDhcpSnoop2IfRateLimit.setStatus("current")


class _HpnicfDhcpSnoop2IfRecordBind_Type(TruthValue):
    """Custom type hpnicfDhcpSnoop2IfRecordBind based on TruthValue"""


_HpnicfDhcpSnoop2IfRecordBind_Object = MibTableColumn
hpnicfDhcpSnoop2IfRecordBind = _HpnicfDhcpSnoop2IfRecordBind_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 124, 2, 2, 1, 5),
    _HpnicfDhcpSnoop2IfRecordBind_Type()
)
hpnicfDhcpSnoop2IfRecordBind.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDhcpSnoop2IfRecordBind.setStatus("current")


class _HpnicfDhcpSnoop2IfMaxLearnNum_Type(Unsigned32):
    """Custom type hpnicfDhcpSnoop2IfMaxLearnNum based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HpnicfDhcpSnoop2IfMaxLearnNum_Type.__name__ = "Unsigned32"
_HpnicfDhcpSnoop2IfMaxLearnNum_Object = MibTableColumn
hpnicfDhcpSnoop2IfMaxLearnNum = _HpnicfDhcpSnoop2IfMaxLearnNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 124, 2, 2, 1, 6),
    _HpnicfDhcpSnoop2IfMaxLearnNum_Type()
)
hpnicfDhcpSnoop2IfMaxLearnNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDhcpSnoop2IfMaxLearnNum.setStatus("current")


class _HpnicfDhcpSnoop2IfOpt82Enable_Type(TruthValue):
    """Custom type hpnicfDhcpSnoop2IfOpt82Enable based on TruthValue"""


_HpnicfDhcpSnoop2IfOpt82Enable_Object = MibTableColumn
hpnicfDhcpSnoop2IfOpt82Enable = _HpnicfDhcpSnoop2IfOpt82Enable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 124, 2, 2, 1, 7),
    _HpnicfDhcpSnoop2IfOpt82Enable_Type()
)
hpnicfDhcpSnoop2IfOpt82Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDhcpSnoop2IfOpt82Enable.setStatus("current")


class _HpnicfDhcpSnoop2IfOpt82Strategy_Type(Integer32):
    """Custom type hpnicfDhcpSnoop2IfOpt82Strategy based on Integer32"""
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


_HpnicfDhcpSnoop2IfOpt82Strategy_Type.__name__ = "Integer32"
_HpnicfDhcpSnoop2IfOpt82Strategy_Object = MibTableColumn
hpnicfDhcpSnoop2IfOpt82Strategy = _HpnicfDhcpSnoop2IfOpt82Strategy_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 124, 2, 2, 1, 8),
    _HpnicfDhcpSnoop2IfOpt82Strategy_Type()
)
hpnicfDhcpSnoop2IfOpt82Strategy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDhcpSnoop2IfOpt82Strategy.setStatus("current")


class _HpnicfDhcpSnoop2IfOpt82CIDMode_Type(Integer32):
    """Custom type hpnicfDhcpSnoop2IfOpt82CIDMode based on Integer32"""
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


_HpnicfDhcpSnoop2IfOpt82CIDMode_Type.__name__ = "Integer32"
_HpnicfDhcpSnoop2IfOpt82CIDMode_Object = MibTableColumn
hpnicfDhcpSnoop2IfOpt82CIDMode = _HpnicfDhcpSnoop2IfOpt82CIDMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 124, 2, 2, 1, 9),
    _HpnicfDhcpSnoop2IfOpt82CIDMode_Type()
)
hpnicfDhcpSnoop2IfOpt82CIDMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDhcpSnoop2IfOpt82CIDMode.setStatus("current")


class _HpnicfDhcpSnoop2IfOpt82CIDNodeType_Type(Integer32):
    """Custom type hpnicfDhcpSnoop2IfOpt82CIDNodeType based on Integer32"""
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


_HpnicfDhcpSnoop2IfOpt82CIDNodeType_Type.__name__ = "Integer32"
_HpnicfDhcpSnoop2IfOpt82CIDNodeType_Object = MibTableColumn
hpnicfDhcpSnoop2IfOpt82CIDNodeType = _HpnicfDhcpSnoop2IfOpt82CIDNodeType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 124, 2, 2, 1, 10),
    _HpnicfDhcpSnoop2IfOpt82CIDNodeType_Type()
)
hpnicfDhcpSnoop2IfOpt82CIDNodeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDhcpSnoop2IfOpt82CIDNodeType.setStatus("current")


class _HpnicfDhcpSnoop2IfOpt82CIDNodeStr_Type(OctetString):
    """Custom type hpnicfDhcpSnoop2IfOpt82CIDNodeStr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_HpnicfDhcpSnoop2IfOpt82CIDNodeStr_Type.__name__ = "OctetString"
_HpnicfDhcpSnoop2IfOpt82CIDNodeStr_Object = MibTableColumn
hpnicfDhcpSnoop2IfOpt82CIDNodeStr = _HpnicfDhcpSnoop2IfOpt82CIDNodeStr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 124, 2, 2, 1, 11),
    _HpnicfDhcpSnoop2IfOpt82CIDNodeStr_Type()
)
hpnicfDhcpSnoop2IfOpt82CIDNodeStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDhcpSnoop2IfOpt82CIDNodeStr.setStatus("current")


class _HpnicfDhcpSnoop2IfOpt82CIDStr_Type(OctetString):
    """Custom type hpnicfDhcpSnoop2IfOpt82CIDStr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(3, 63),
    )


_HpnicfDhcpSnoop2IfOpt82CIDStr_Type.__name__ = "OctetString"
_HpnicfDhcpSnoop2IfOpt82CIDStr_Object = MibTableColumn
hpnicfDhcpSnoop2IfOpt82CIDStr = _HpnicfDhcpSnoop2IfOpt82CIDStr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 124, 2, 2, 1, 12),
    _HpnicfDhcpSnoop2IfOpt82CIDStr_Type()
)
hpnicfDhcpSnoop2IfOpt82CIDStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDhcpSnoop2IfOpt82CIDStr.setStatus("current")


class _HpnicfDhcpSnoop2IfOpt82CIDFormat_Type(Integer32):
    """Custom type hpnicfDhcpSnoop2IfOpt82CIDFormat based on Integer32"""
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


_HpnicfDhcpSnoop2IfOpt82CIDFormat_Type.__name__ = "Integer32"
_HpnicfDhcpSnoop2IfOpt82CIDFormat_Object = MibTableColumn
hpnicfDhcpSnoop2IfOpt82CIDFormat = _HpnicfDhcpSnoop2IfOpt82CIDFormat_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 124, 2, 2, 1, 13),
    _HpnicfDhcpSnoop2IfOpt82CIDFormat_Type()
)
hpnicfDhcpSnoop2IfOpt82CIDFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDhcpSnoop2IfOpt82CIDFormat.setStatus("current")


class _HpnicfDhcpSnoop2IfOpt82RIDMode_Type(Integer32):
    """Custom type hpnicfDhcpSnoop2IfOpt82RIDMode based on Integer32"""
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


_HpnicfDhcpSnoop2IfOpt82RIDMode_Type.__name__ = "Integer32"
_HpnicfDhcpSnoop2IfOpt82RIDMode_Object = MibTableColumn
hpnicfDhcpSnoop2IfOpt82RIDMode = _HpnicfDhcpSnoop2IfOpt82RIDMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 124, 2, 2, 1, 14),
    _HpnicfDhcpSnoop2IfOpt82RIDMode_Type()
)
hpnicfDhcpSnoop2IfOpt82RIDMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDhcpSnoop2IfOpt82RIDMode.setStatus("current")


class _HpnicfDhcpSnoop2IfOpt82RIDStr_Type(OctetString):
    """Custom type hpnicfDhcpSnoop2IfOpt82RIDStr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_HpnicfDhcpSnoop2IfOpt82RIDStr_Type.__name__ = "OctetString"
_HpnicfDhcpSnoop2IfOpt82RIDStr_Object = MibTableColumn
hpnicfDhcpSnoop2IfOpt82RIDStr = _HpnicfDhcpSnoop2IfOpt82RIDStr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 124, 2, 2, 1, 15),
    _HpnicfDhcpSnoop2IfOpt82RIDStr_Type()
)
hpnicfDhcpSnoop2IfOpt82RIDStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDhcpSnoop2IfOpt82RIDStr.setStatus("current")


class _HpnicfDhcpSnoop2IfOpt82RIDFormat_Type(Integer32):
    """Custom type hpnicfDhcpSnoop2IfOpt82RIDFormat based on Integer32"""
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


_HpnicfDhcpSnoop2IfOpt82RIDFormat_Type.__name__ = "Integer32"
_HpnicfDhcpSnoop2IfOpt82RIDFormat_Object = MibTableColumn
hpnicfDhcpSnoop2IfOpt82RIDFormat = _HpnicfDhcpSnoop2IfOpt82RIDFormat_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 124, 2, 2, 1, 16),
    _HpnicfDhcpSnoop2IfOpt82RIDFormat_Type()
)
hpnicfDhcpSnoop2IfOpt82RIDFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDhcpSnoop2IfOpt82RIDFormat.setStatus("current")
_HpnicfDhcpSnoop2IfVlanCIDTable_Object = MibTable
hpnicfDhcpSnoop2IfVlanCIDTable = _HpnicfDhcpSnoop2IfVlanCIDTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 124, 2, 3)
)
if mibBuilder.loadTexts:
    hpnicfDhcpSnoop2IfVlanCIDTable.setStatus("current")
_HpnicfDhcpSnoop2IfVlanCIDEntry_Object = MibTableRow
hpnicfDhcpSnoop2IfVlanCIDEntry = _HpnicfDhcpSnoop2IfVlanCIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 124, 2, 3, 1)
)
hpnicfDhcpSnoop2IfVlanCIDEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-DHCP-SNOOP2-MIB", "hpnicfDhcpSnoop2IfVlanCIDVlanIndex"),
)
if mibBuilder.loadTexts:
    hpnicfDhcpSnoop2IfVlanCIDEntry.setStatus("current")


class _HpnicfDhcpSnoop2IfVlanCIDVlanIndex_Type(Unsigned32):
    """Custom type hpnicfDhcpSnoop2IfVlanCIDVlanIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HpnicfDhcpSnoop2IfVlanCIDVlanIndex_Type.__name__ = "Unsigned32"
_HpnicfDhcpSnoop2IfVlanCIDVlanIndex_Object = MibTableColumn
hpnicfDhcpSnoop2IfVlanCIDVlanIndex = _HpnicfDhcpSnoop2IfVlanCIDVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 124, 2, 3, 1, 1),
    _HpnicfDhcpSnoop2IfVlanCIDVlanIndex_Type()
)
hpnicfDhcpSnoop2IfVlanCIDVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDhcpSnoop2IfVlanCIDVlanIndex.setStatus("current")


class _HpnicfDhcpSnoop2IfVlanCIDStr_Type(OctetString):
    """Custom type hpnicfDhcpSnoop2IfVlanCIDStr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 63),
    )


_HpnicfDhcpSnoop2IfVlanCIDStr_Type.__name__ = "OctetString"
_HpnicfDhcpSnoop2IfVlanCIDStr_Object = MibTableColumn
hpnicfDhcpSnoop2IfVlanCIDStr = _HpnicfDhcpSnoop2IfVlanCIDStr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 124, 2, 3, 1, 2),
    _HpnicfDhcpSnoop2IfVlanCIDStr_Type()
)
hpnicfDhcpSnoop2IfVlanCIDStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpSnoop2IfVlanCIDStr.setStatus("current")
_HpnicfDhcpSnoop2IfVlanCIDRowStatus_Type = RowStatus
_HpnicfDhcpSnoop2IfVlanCIDRowStatus_Object = MibTableColumn
hpnicfDhcpSnoop2IfVlanCIDRowStatus = _HpnicfDhcpSnoop2IfVlanCIDRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 124, 2, 3, 1, 3),
    _HpnicfDhcpSnoop2IfVlanCIDRowStatus_Type()
)
hpnicfDhcpSnoop2IfVlanCIDRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpSnoop2IfVlanCIDRowStatus.setStatus("current")
_HpnicfDhcpSnoop2IfVlanRIDTable_Object = MibTable
hpnicfDhcpSnoop2IfVlanRIDTable = _HpnicfDhcpSnoop2IfVlanRIDTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 124, 2, 4)
)
if mibBuilder.loadTexts:
    hpnicfDhcpSnoop2IfVlanRIDTable.setStatus("current")
_HpnicfDhcpSnoop2IfVlanRIDEntry_Object = MibTableRow
hpnicfDhcpSnoop2IfVlanRIDEntry = _HpnicfDhcpSnoop2IfVlanRIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 124, 2, 4, 1)
)
hpnicfDhcpSnoop2IfVlanRIDEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-DHCP-SNOOP2-MIB", "hpnicfDhcpSnoop2IfVlanRIDVlanIndex"),
)
if mibBuilder.loadTexts:
    hpnicfDhcpSnoop2IfVlanRIDEntry.setStatus("current")


class _HpnicfDhcpSnoop2IfVlanRIDVlanIndex_Type(Unsigned32):
    """Custom type hpnicfDhcpSnoop2IfVlanRIDVlanIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HpnicfDhcpSnoop2IfVlanRIDVlanIndex_Type.__name__ = "Unsigned32"
_HpnicfDhcpSnoop2IfVlanRIDVlanIndex_Object = MibTableColumn
hpnicfDhcpSnoop2IfVlanRIDVlanIndex = _HpnicfDhcpSnoop2IfVlanRIDVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 124, 2, 4, 1, 1),
    _HpnicfDhcpSnoop2IfVlanRIDVlanIndex_Type()
)
hpnicfDhcpSnoop2IfVlanRIDVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDhcpSnoop2IfVlanRIDVlanIndex.setStatus("current")


class _HpnicfDhcpSnoop2IfVlanRIDMode_Type(Integer32):
    """Custom type hpnicfDhcpSnoop2IfVlanRIDMode based on Integer32"""
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


_HpnicfDhcpSnoop2IfVlanRIDMode_Type.__name__ = "Integer32"
_HpnicfDhcpSnoop2IfVlanRIDMode_Object = MibTableColumn
hpnicfDhcpSnoop2IfVlanRIDMode = _HpnicfDhcpSnoop2IfVlanRIDMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 124, 2, 4, 1, 2),
    _HpnicfDhcpSnoop2IfVlanRIDMode_Type()
)
hpnicfDhcpSnoop2IfVlanRIDMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpSnoop2IfVlanRIDMode.setStatus("current")


class _HpnicfDhcpSnoop2IfVlanRIDStr_Type(OctetString):
    """Custom type hpnicfDhcpSnoop2IfVlanRIDStr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_HpnicfDhcpSnoop2IfVlanRIDStr_Type.__name__ = "OctetString"
_HpnicfDhcpSnoop2IfVlanRIDStr_Object = MibTableColumn
hpnicfDhcpSnoop2IfVlanRIDStr = _HpnicfDhcpSnoop2IfVlanRIDStr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 124, 2, 4, 1, 3),
    _HpnicfDhcpSnoop2IfVlanRIDStr_Type()
)
hpnicfDhcpSnoop2IfVlanRIDStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpSnoop2IfVlanRIDStr.setStatus("current")
_HpnicfDhcpSnoop2IfVlanRIDRowStatus_Type = RowStatus
_HpnicfDhcpSnoop2IfVlanRIDRowStatus_Object = MibTableColumn
hpnicfDhcpSnoop2IfVlanRIDRowStatus = _HpnicfDhcpSnoop2IfVlanRIDRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 124, 2, 4, 1, 4),
    _HpnicfDhcpSnoop2IfVlanRIDRowStatus_Type()
)
hpnicfDhcpSnoop2IfVlanRIDRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDhcpSnoop2IfVlanRIDRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-DHCP-SNOOP2-MIB",
    **{"hpnicfDhcpSnoop2": hpnicfDhcpSnoop2,
       "hpnicfDhcpSnoop2ScalarObjects": hpnicfDhcpSnoop2ScalarObjects,
       "hpnicfDhcpSnoop2ConfigGroup": hpnicfDhcpSnoop2ConfigGroup,
       "hpnicfDhcpSnoop2Enabled": hpnicfDhcpSnoop2Enabled,
       "hpnicfDhcpSnoop2BindDbName": hpnicfDhcpSnoop2BindDbName,
       "hpnicfDhcpSnoop2BindRefreshIntvl": hpnicfDhcpSnoop2BindRefreshIntvl,
       "hpnicfDhcpSnoop2BindRefresh": hpnicfDhcpSnoop2BindRefresh,
       "hpnicfDhcpSnoop2StatisticsGroup": hpnicfDhcpSnoop2StatisticsGroup,
       "hpnicfDhcpSnoop2PktSentNum": hpnicfDhcpSnoop2PktSentNum,
       "hpnicfDhcpSnoop2PktRcvNum": hpnicfDhcpSnoop2PktRcvNum,
       "hpnicfDhcpSnoop2PktDropNum": hpnicfDhcpSnoop2PktDropNum,
       "hpnicfDhcpSnoop2Tables": hpnicfDhcpSnoop2Tables,
       "hpnicfDhcpSnoop2BindTable": hpnicfDhcpSnoop2BindTable,
       "hpnicfDhcpSnoop2BindEntry": hpnicfDhcpSnoop2BindEntry,
       "hpnicfDhcpSnoop2BindIpAddr": hpnicfDhcpSnoop2BindIpAddr,
       "hpnicfDhcpSnoop2BindVlanId": hpnicfDhcpSnoop2BindVlanId,
       "hpnicfDhcpSnoop2BindSecVlanId": hpnicfDhcpSnoop2BindSecVlanId,
       "hpnicfDhcpSnoop2BindMacAddr": hpnicfDhcpSnoop2BindMacAddr,
       "hpnicfDhcpSnoop2BindLease": hpnicfDhcpSnoop2BindLease,
       "hpnicfDhcpSnoop2BindPortIndex": hpnicfDhcpSnoop2BindPortIndex,
       "hpnicfDhcpSnoop2BindRowStatus": hpnicfDhcpSnoop2BindRowStatus,
       "hpnicfDhcpSnoop2IfConfigTable": hpnicfDhcpSnoop2IfConfigTable,
       "hpnicfDhcpSnoop2IfConfigEntry": hpnicfDhcpSnoop2IfConfigEntry,
       "hpnicfDhcpSnoop2IfTrustStatus": hpnicfDhcpSnoop2IfTrustStatus,
       "hpnicfDhcpSnoop2IfCheckMac": hpnicfDhcpSnoop2IfCheckMac,
       "hpnicfDhcpSnoop2IfCheckRequest": hpnicfDhcpSnoop2IfCheckRequest,
       "hpnicfDhcpSnoop2IfRateLimit": hpnicfDhcpSnoop2IfRateLimit,
       "hpnicfDhcpSnoop2IfRecordBind": hpnicfDhcpSnoop2IfRecordBind,
       "hpnicfDhcpSnoop2IfMaxLearnNum": hpnicfDhcpSnoop2IfMaxLearnNum,
       "hpnicfDhcpSnoop2IfOpt82Enable": hpnicfDhcpSnoop2IfOpt82Enable,
       "hpnicfDhcpSnoop2IfOpt82Strategy": hpnicfDhcpSnoop2IfOpt82Strategy,
       "hpnicfDhcpSnoop2IfOpt82CIDMode": hpnicfDhcpSnoop2IfOpt82CIDMode,
       "hpnicfDhcpSnoop2IfOpt82CIDNodeType": hpnicfDhcpSnoop2IfOpt82CIDNodeType,
       "hpnicfDhcpSnoop2IfOpt82CIDNodeStr": hpnicfDhcpSnoop2IfOpt82CIDNodeStr,
       "hpnicfDhcpSnoop2IfOpt82CIDStr": hpnicfDhcpSnoop2IfOpt82CIDStr,
       "hpnicfDhcpSnoop2IfOpt82CIDFormat": hpnicfDhcpSnoop2IfOpt82CIDFormat,
       "hpnicfDhcpSnoop2IfOpt82RIDMode": hpnicfDhcpSnoop2IfOpt82RIDMode,
       "hpnicfDhcpSnoop2IfOpt82RIDStr": hpnicfDhcpSnoop2IfOpt82RIDStr,
       "hpnicfDhcpSnoop2IfOpt82RIDFormat": hpnicfDhcpSnoop2IfOpt82RIDFormat,
       "hpnicfDhcpSnoop2IfVlanCIDTable": hpnicfDhcpSnoop2IfVlanCIDTable,
       "hpnicfDhcpSnoop2IfVlanCIDEntry": hpnicfDhcpSnoop2IfVlanCIDEntry,
       "hpnicfDhcpSnoop2IfVlanCIDVlanIndex": hpnicfDhcpSnoop2IfVlanCIDVlanIndex,
       "hpnicfDhcpSnoop2IfVlanCIDStr": hpnicfDhcpSnoop2IfVlanCIDStr,
       "hpnicfDhcpSnoop2IfVlanCIDRowStatus": hpnicfDhcpSnoop2IfVlanCIDRowStatus,
       "hpnicfDhcpSnoop2IfVlanRIDTable": hpnicfDhcpSnoop2IfVlanRIDTable,
       "hpnicfDhcpSnoop2IfVlanRIDEntry": hpnicfDhcpSnoop2IfVlanRIDEntry,
       "hpnicfDhcpSnoop2IfVlanRIDVlanIndex": hpnicfDhcpSnoop2IfVlanRIDVlanIndex,
       "hpnicfDhcpSnoop2IfVlanRIDMode": hpnicfDhcpSnoop2IfVlanRIDMode,
       "hpnicfDhcpSnoop2IfVlanRIDStr": hpnicfDhcpSnoop2IfVlanRIDStr,
       "hpnicfDhcpSnoop2IfVlanRIDRowStatus": hpnicfDhcpSnoop2IfVlanRIDRowStatus}
)
