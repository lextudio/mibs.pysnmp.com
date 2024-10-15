# SNMP MIB module (HP-ICF-BYOD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-BYOD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:57:09 2024
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

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hpicfByodMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106)
)
hpicfByodMIB.setRevisions(
        ("2014-05-19 09:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfByodNotifications_ObjectIdentity = ObjectIdentity
hpicfByodNotifications = _HpicfByodNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 0)
)
_HpicfByodObjects_ObjectIdentity = ObjectIdentity
hpicfByodObjects = _HpicfByodObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 1)
)
_HpicfByodConfigObjects_ObjectIdentity = ObjectIdentity
hpicfByodConfigObjects = _HpicfByodConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 1, 1)
)
_HpicfByodScalarConfig_ObjectIdentity = ObjectIdentity
hpicfByodScalarConfig = _HpicfByodScalarConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 1, 1, 1)
)
_HpicfByodPortalTable_Object = MibTable
hpicfByodPortalTable = _HpicfByodPortalTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hpicfByodPortalTable.setStatus("current")
_HpicfByodPortalEntry_Object = MibTableRow
hpicfByodPortalEntry = _HpicfByodPortalEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 1, 1, 2, 1)
)
hpicfByodPortalEntry.setIndexNames(
    (0, "HP-ICF-BYOD-MIB", "hpicfByodPortalName"),
)
if mibBuilder.loadTexts:
    hpicfByodPortalEntry.setStatus("current")


class _HpicfByodPortalName_Type(DisplayString):
    """Custom type hpicfByodPortalName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HpicfByodPortalName_Type.__name__ = "DisplayString"
_HpicfByodPortalName_Object = MibTableColumn
hpicfByodPortalName = _HpicfByodPortalName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 1, 1, 2, 1, 1),
    _HpicfByodPortalName_Type()
)
hpicfByodPortalName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfByodPortalName.setStatus("current")


class _HpicfByodPortalVlanId_Type(Unsigned32):
    """Custom type hpicfByodPortalVlanId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HpicfByodPortalVlanId_Type.__name__ = "Unsigned32"
_HpicfByodPortalVlanId_Object = MibTableColumn
hpicfByodPortalVlanId = _HpicfByodPortalVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 1, 1, 2, 1, 2),
    _HpicfByodPortalVlanId_Type()
)
hpicfByodPortalVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfByodPortalVlanId.setStatus("current")


class _HpicfByodPortalUrl_Type(DisplayString):
    """Custom type hpicfByodPortalUrl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_HpicfByodPortalUrl_Type.__name__ = "DisplayString"
_HpicfByodPortalUrl_Object = MibTableColumn
hpicfByodPortalUrl = _HpicfByodPortalUrl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 1, 1, 2, 1, 3),
    _HpicfByodPortalUrl_Type()
)
hpicfByodPortalUrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfByodPortalUrl.setStatus("current")
_HpicfByodPortalInetAddrType_Type = InetAddressType
_HpicfByodPortalInetAddrType_Object = MibTableColumn
hpicfByodPortalInetAddrType = _HpicfByodPortalInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 1, 1, 2, 1, 4),
    _HpicfByodPortalInetAddrType_Type()
)
hpicfByodPortalInetAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfByodPortalInetAddrType.setStatus("current")
_HpicfByodPortalInetAddr_Type = InetAddress
_HpicfByodPortalInetAddr_Object = MibTableColumn
hpicfByodPortalInetAddr = _HpicfByodPortalInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 1, 1, 2, 1, 5),
    _HpicfByodPortalInetAddr_Type()
)
hpicfByodPortalInetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfByodPortalInetAddr.setStatus("current")


class _HpicfByodPortalDnsCacheTime_Type(TimeTicks):
    """Custom type hpicfByodPortalDnsCacheTime based on TimeTicks"""
    defaultValue = 15


_HpicfByodPortalDnsCacheTime_Object = MibTableColumn
hpicfByodPortalDnsCacheTime = _HpicfByodPortalDnsCacheTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 1, 1, 2, 1, 6),
    _HpicfByodPortalDnsCacheTime_Type()
)
hpicfByodPortalDnsCacheTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfByodPortalDnsCacheTime.setStatus("current")
_HpicfByodPortalRowStatus_Type = RowStatus
_HpicfByodPortalRowStatus_Object = MibTableColumn
hpicfByodPortalRowStatus = _HpicfByodPortalRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 1, 1, 2, 1, 7),
    _HpicfByodPortalRowStatus_Type()
)
hpicfByodPortalRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfByodPortalRowStatus.setStatus("current")
_HpicfByodFreeRuleTable_Object = MibTable
hpicfByodFreeRuleTable = _HpicfByodFreeRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hpicfByodFreeRuleTable.setStatus("current")
_HpicfByodFreeRuleEntry_Object = MibTableRow
hpicfByodFreeRuleEntry = _HpicfByodFreeRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 1, 1, 3, 1)
)
hpicfByodFreeRuleEntry.setIndexNames(
    (0, "HP-ICF-BYOD-MIB", "hpicfByodFreeRuleNumber"),
)
if mibBuilder.loadTexts:
    hpicfByodFreeRuleEntry.setStatus("current")


class _HpicfByodFreeRuleNumber_Type(Unsigned32):
    """Custom type hpicfByodFreeRuleNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_HpicfByodFreeRuleNumber_Type.__name__ = "Unsigned32"
_HpicfByodFreeRuleNumber_Object = MibTableColumn
hpicfByodFreeRuleNumber = _HpicfByodFreeRuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 1, 1, 3, 1, 1),
    _HpicfByodFreeRuleNumber_Type()
)
hpicfByodFreeRuleNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfByodFreeRuleNumber.setStatus("current")


class _HpicfByodFreeRuleSourceProtocol_Type(Integer32):
    """Custom type hpicfByodFreeRuleSourceProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 1),
          ("udp", 2))
    )


_HpicfByodFreeRuleSourceProtocol_Type.__name__ = "Integer32"
_HpicfByodFreeRuleSourceProtocol_Object = MibTableColumn
hpicfByodFreeRuleSourceProtocol = _HpicfByodFreeRuleSourceProtocol_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 1, 1, 3, 1, 2),
    _HpicfByodFreeRuleSourceProtocol_Type()
)
hpicfByodFreeRuleSourceProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfByodFreeRuleSourceProtocol.setStatus("current")


class _HpicfByodFreeRuleSourcePort_Type(Unsigned32):
    """Custom type hpicfByodFreeRuleSourcePort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpicfByodFreeRuleSourcePort_Type.__name__ = "Unsigned32"
_HpicfByodFreeRuleSourcePort_Object = MibTableColumn
hpicfByodFreeRuleSourcePort = _HpicfByodFreeRuleSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 1, 1, 3, 1, 3),
    _HpicfByodFreeRuleSourcePort_Type()
)
hpicfByodFreeRuleSourcePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfByodFreeRuleSourcePort.setStatus("current")


class _HpicfByodFreeRuleSourceVlanId_Type(Unsigned32):
    """Custom type hpicfByodFreeRuleSourceVlanId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HpicfByodFreeRuleSourceVlanId_Type.__name__ = "Unsigned32"
_HpicfByodFreeRuleSourceVlanId_Object = MibTableColumn
hpicfByodFreeRuleSourceVlanId = _HpicfByodFreeRuleSourceVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 1, 1, 3, 1, 4),
    _HpicfByodFreeRuleSourceVlanId_Type()
)
hpicfByodFreeRuleSourceVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfByodFreeRuleSourceVlanId.setStatus("current")
_HpicfByodFreeRuleSourceInetAddrType_Type = InetAddressType
_HpicfByodFreeRuleSourceInetAddrType_Object = MibTableColumn
hpicfByodFreeRuleSourceInetAddrType = _HpicfByodFreeRuleSourceInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 1, 1, 3, 1, 5),
    _HpicfByodFreeRuleSourceInetAddrType_Type()
)
hpicfByodFreeRuleSourceInetAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfByodFreeRuleSourceInetAddrType.setStatus("current")
_HpicfByodFreeRuleSourceInetAddr_Type = InetAddress
_HpicfByodFreeRuleSourceInetAddr_Object = MibTableColumn
hpicfByodFreeRuleSourceInetAddr = _HpicfByodFreeRuleSourceInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 1, 1, 3, 1, 6),
    _HpicfByodFreeRuleSourceInetAddr_Type()
)
hpicfByodFreeRuleSourceInetAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfByodFreeRuleSourceInetAddr.setStatus("current")
_HpicfByodFreeRuleSourceInetAddrMask_Type = InetAddress
_HpicfByodFreeRuleSourceInetAddrMask_Object = MibTableColumn
hpicfByodFreeRuleSourceInetAddrMask = _HpicfByodFreeRuleSourceInetAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 1, 1, 3, 1, 7),
    _HpicfByodFreeRuleSourceInetAddrMask_Type()
)
hpicfByodFreeRuleSourceInetAddrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfByodFreeRuleSourceInetAddrMask.setStatus("current")


class _HpicfByodFreeRuleDestinationProtocol_Type(Integer32):
    """Custom type hpicfByodFreeRuleDestinationProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 1),
          ("udp", 2))
    )


_HpicfByodFreeRuleDestinationProtocol_Type.__name__ = "Integer32"
_HpicfByodFreeRuleDestinationProtocol_Object = MibTableColumn
hpicfByodFreeRuleDestinationProtocol = _HpicfByodFreeRuleDestinationProtocol_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 1, 1, 3, 1, 8),
    _HpicfByodFreeRuleDestinationProtocol_Type()
)
hpicfByodFreeRuleDestinationProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfByodFreeRuleDestinationProtocol.setStatus("current")


class _HpicfByodFreeRuleDestinationPort_Type(Unsigned32):
    """Custom type hpicfByodFreeRuleDestinationPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpicfByodFreeRuleDestinationPort_Type.__name__ = "Unsigned32"
_HpicfByodFreeRuleDestinationPort_Object = MibTableColumn
hpicfByodFreeRuleDestinationPort = _HpicfByodFreeRuleDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 1, 1, 3, 1, 9),
    _HpicfByodFreeRuleDestinationPort_Type()
)
hpicfByodFreeRuleDestinationPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfByodFreeRuleDestinationPort.setStatus("current")
_HpicfByodFreeRuleDestinationInetAddrType_Type = InetAddressType
_HpicfByodFreeRuleDestinationInetAddrType_Object = MibTableColumn
hpicfByodFreeRuleDestinationInetAddrType = _HpicfByodFreeRuleDestinationInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 1, 1, 3, 1, 10),
    _HpicfByodFreeRuleDestinationInetAddrType_Type()
)
hpicfByodFreeRuleDestinationInetAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfByodFreeRuleDestinationInetAddrType.setStatus("current")
_HpicfByodFreeRuleDestinationInetAddr_Type = InetAddress
_HpicfByodFreeRuleDestinationInetAddr_Object = MibTableColumn
hpicfByodFreeRuleDestinationInetAddr = _HpicfByodFreeRuleDestinationInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 1, 1, 3, 1, 11),
    _HpicfByodFreeRuleDestinationInetAddr_Type()
)
hpicfByodFreeRuleDestinationInetAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfByodFreeRuleDestinationInetAddr.setStatus("current")
_HpicfByodFreeRuleDestinationInetAddrMask_Type = InetAddress
_HpicfByodFreeRuleDestinationInetAddrMask_Object = MibTableColumn
hpicfByodFreeRuleDestinationInetAddrMask = _HpicfByodFreeRuleDestinationInetAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 1, 1, 3, 1, 12),
    _HpicfByodFreeRuleDestinationInetAddrMask_Type()
)
hpicfByodFreeRuleDestinationInetAddrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfByodFreeRuleDestinationInetAddrMask.setStatus("current")
_HpicfByodFreeRuleRowStatus_Type = RowStatus
_HpicfByodFreeRuleRowStatus_Object = MibTableColumn
hpicfByodFreeRuleRowStatus = _HpicfByodFreeRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 1, 1, 3, 1, 13),
    _HpicfByodFreeRuleRowStatus_Type()
)
hpicfByodFreeRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfByodFreeRuleRowStatus.setStatus("current")
_HpicfByodStatsObjects_ObjectIdentity = ObjectIdentity
hpicfByodStatsObjects = _HpicfByodStatsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 1, 2)
)
_HpicfByodScalarStats_ObjectIdentity = ObjectIdentity
hpicfByodScalarStats = _HpicfByodScalarStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 1, 2, 1)
)
_HpicfByodTcpStatsTotalOpen_Type = Counter32
_HpicfByodTcpStatsTotalOpen_Object = MibScalar
hpicfByodTcpStatsTotalOpen = _HpicfByodTcpStatsTotalOpen_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 1, 2, 1, 1),
    _HpicfByodTcpStatsTotalOpen_Type()
)
hpicfByodTcpStatsTotalOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfByodTcpStatsTotalOpen.setStatus("current")
_HpicfByodTcpStatsResetConn_Type = Counter32
_HpicfByodTcpStatsResetConn_Object = MibScalar
hpicfByodTcpStatsResetConn = _HpicfByodTcpStatsResetConn_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 1, 2, 1, 2),
    _HpicfByodTcpStatsResetConn_Type()
)
hpicfByodTcpStatsResetConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfByodTcpStatsResetConn.setStatus("current")
_HpicfByodTcpStatsCurrentOpen_Type = Counter32
_HpicfByodTcpStatsCurrentOpen_Object = MibScalar
hpicfByodTcpStatsCurrentOpen = _HpicfByodTcpStatsCurrentOpen_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 1, 2, 1, 3),
    _HpicfByodTcpStatsCurrentOpen_Type()
)
hpicfByodTcpStatsCurrentOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfByodTcpStatsCurrentOpen.setStatus("current")
_HpicfByodTcpStatsPktsReceived_Type = Counter32
_HpicfByodTcpStatsPktsReceived_Object = MibScalar
hpicfByodTcpStatsPktsReceived = _HpicfByodTcpStatsPktsReceived_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 1, 2, 1, 4),
    _HpicfByodTcpStatsPktsReceived_Type()
)
hpicfByodTcpStatsPktsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfByodTcpStatsPktsReceived.setStatus("current")
_HpicfByodTcpStatsPktsSent_Type = Counter32
_HpicfByodTcpStatsPktsSent_Object = MibScalar
hpicfByodTcpStatsPktsSent = _HpicfByodTcpStatsPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 1, 2, 1, 5),
    _HpicfByodTcpStatsPktsSent_Type()
)
hpicfByodTcpStatsPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfByodTcpStatsPktsSent.setStatus("current")
_HpicfByodTcpStatsHttpPktsSent_Type = Counter32
_HpicfByodTcpStatsHttpPktsSent_Object = MibScalar
hpicfByodTcpStatsHttpPktsSent = _HpicfByodTcpStatsHttpPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 1, 2, 1, 8),
    _HpicfByodTcpStatsHttpPktsSent_Type()
)
hpicfByodTcpStatsHttpPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfByodTcpStatsHttpPktsSent.setStatus("current")
_HpicfByodTcpStatsStateSynRcvd_Type = Counter32
_HpicfByodTcpStatsStateSynRcvd_Object = MibScalar
hpicfByodTcpStatsStateSynRcvd = _HpicfByodTcpStatsStateSynRcvd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 1, 2, 1, 9),
    _HpicfByodTcpStatsStateSynRcvd_Type()
)
hpicfByodTcpStatsStateSynRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfByodTcpStatsStateSynRcvd.setStatus("current")
_HpicfByodTcpStatsStateEstablished_Type = Counter32
_HpicfByodTcpStatsStateEstablished_Object = MibScalar
hpicfByodTcpStatsStateEstablished = _HpicfByodTcpStatsStateEstablished_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 1, 2, 1, 10),
    _HpicfByodTcpStatsStateEstablished_Type()
)
hpicfByodTcpStatsStateEstablished.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfByodTcpStatsStateEstablished.setStatus("current")
_HpicfByodConformance_ObjectIdentity = ObjectIdentity
hpicfByodConformance = _HpicfByodConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 2)
)
_HpicfByodCompliances_ObjectIdentity = ObjectIdentity
hpicfByodCompliances = _HpicfByodCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 2, 1)
)
_HpicfByodGroups_ObjectIdentity = ObjectIdentity
hpicfByodGroups = _HpicfByodGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 2, 2)
)

# Managed Objects groups

hpicfByodConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 2, 2, 1)
)
hpicfByodConfigGroup.setObjects(
      *(("HP-ICF-BYOD-MIB", "hpicfByodPortalVlanId"),
        ("HP-ICF-BYOD-MIB", "hpicfByodPortalUrl"),
        ("HP-ICF-BYOD-MIB", "hpicfByodPortalInetAddrType"),
        ("HP-ICF-BYOD-MIB", "hpicfByodPortalInetAddr"),
        ("HP-ICF-BYOD-MIB", "hpicfByodPortalDnsCacheTime"),
        ("HP-ICF-BYOD-MIB", "hpicfByodPortalRowStatus"),
        ("HP-ICF-BYOD-MIB", "hpicfByodFreeRuleSourceProtocol"),
        ("HP-ICF-BYOD-MIB", "hpicfByodFreeRuleSourcePort"),
        ("HP-ICF-BYOD-MIB", "hpicfByodFreeRuleSourceVlanId"),
        ("HP-ICF-BYOD-MIB", "hpicfByodFreeRuleSourceInetAddrType"),
        ("HP-ICF-BYOD-MIB", "hpicfByodFreeRuleSourceInetAddr"),
        ("HP-ICF-BYOD-MIB", "hpicfByodFreeRuleSourceInetAddrMask"),
        ("HP-ICF-BYOD-MIB", "hpicfByodFreeRuleDestinationProtocol"),
        ("HP-ICF-BYOD-MIB", "hpicfByodFreeRuleDestinationPort"),
        ("HP-ICF-BYOD-MIB", "hpicfByodFreeRuleDestinationInetAddrType"),
        ("HP-ICF-BYOD-MIB", "hpicfByodFreeRuleDestinationInetAddr"),
        ("HP-ICF-BYOD-MIB", "hpicfByodFreeRuleDestinationInetAddrMask"),
        ("HP-ICF-BYOD-MIB", "hpicfByodFreeRuleRowStatus"))
)
if mibBuilder.loadTexts:
    hpicfByodConfigGroup.setStatus("current")

hpicfByodStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 2, 2, 2)
)
hpicfByodStatsGroup.setObjects(
      *(("HP-ICF-BYOD-MIB", "hpicfByodTcpStatsTotalOpen"),
        ("HP-ICF-BYOD-MIB", "hpicfByodTcpStatsResetConn"),
        ("HP-ICF-BYOD-MIB", "hpicfByodTcpStatsCurrentOpen"),
        ("HP-ICF-BYOD-MIB", "hpicfByodTcpStatsPktsReceived"),
        ("HP-ICF-BYOD-MIB", "hpicfByodTcpStatsPktsSent"),
        ("HP-ICF-BYOD-MIB", "hpicfByodTcpStatsHttpPktsSent"),
        ("HP-ICF-BYOD-MIB", "hpicfByodTcpStatsStateSynRcvd"),
        ("HP-ICF-BYOD-MIB", "hpicfByodTcpStatsStateEstablished"))
)
if mibBuilder.loadTexts:
    hpicfByodStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpicfByodCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 106, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfByodCompliance1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-BYOD-MIB",
    **{"hpicfByodMIB": hpicfByodMIB,
       "hpicfByodNotifications": hpicfByodNotifications,
       "hpicfByodObjects": hpicfByodObjects,
       "hpicfByodConfigObjects": hpicfByodConfigObjects,
       "hpicfByodScalarConfig": hpicfByodScalarConfig,
       "hpicfByodPortalTable": hpicfByodPortalTable,
       "hpicfByodPortalEntry": hpicfByodPortalEntry,
       "hpicfByodPortalName": hpicfByodPortalName,
       "hpicfByodPortalVlanId": hpicfByodPortalVlanId,
       "hpicfByodPortalUrl": hpicfByodPortalUrl,
       "hpicfByodPortalInetAddrType": hpicfByodPortalInetAddrType,
       "hpicfByodPortalInetAddr": hpicfByodPortalInetAddr,
       "hpicfByodPortalDnsCacheTime": hpicfByodPortalDnsCacheTime,
       "hpicfByodPortalRowStatus": hpicfByodPortalRowStatus,
       "hpicfByodFreeRuleTable": hpicfByodFreeRuleTable,
       "hpicfByodFreeRuleEntry": hpicfByodFreeRuleEntry,
       "hpicfByodFreeRuleNumber": hpicfByodFreeRuleNumber,
       "hpicfByodFreeRuleSourceProtocol": hpicfByodFreeRuleSourceProtocol,
       "hpicfByodFreeRuleSourcePort": hpicfByodFreeRuleSourcePort,
       "hpicfByodFreeRuleSourceVlanId": hpicfByodFreeRuleSourceVlanId,
       "hpicfByodFreeRuleSourceInetAddrType": hpicfByodFreeRuleSourceInetAddrType,
       "hpicfByodFreeRuleSourceInetAddr": hpicfByodFreeRuleSourceInetAddr,
       "hpicfByodFreeRuleSourceInetAddrMask": hpicfByodFreeRuleSourceInetAddrMask,
       "hpicfByodFreeRuleDestinationProtocol": hpicfByodFreeRuleDestinationProtocol,
       "hpicfByodFreeRuleDestinationPort": hpicfByodFreeRuleDestinationPort,
       "hpicfByodFreeRuleDestinationInetAddrType": hpicfByodFreeRuleDestinationInetAddrType,
       "hpicfByodFreeRuleDestinationInetAddr": hpicfByodFreeRuleDestinationInetAddr,
       "hpicfByodFreeRuleDestinationInetAddrMask": hpicfByodFreeRuleDestinationInetAddrMask,
       "hpicfByodFreeRuleRowStatus": hpicfByodFreeRuleRowStatus,
       "hpicfByodStatsObjects": hpicfByodStatsObjects,
       "hpicfByodScalarStats": hpicfByodScalarStats,
       "hpicfByodTcpStatsTotalOpen": hpicfByodTcpStatsTotalOpen,
       "hpicfByodTcpStatsResetConn": hpicfByodTcpStatsResetConn,
       "hpicfByodTcpStatsCurrentOpen": hpicfByodTcpStatsCurrentOpen,
       "hpicfByodTcpStatsPktsReceived": hpicfByodTcpStatsPktsReceived,
       "hpicfByodTcpStatsPktsSent": hpicfByodTcpStatsPktsSent,
       "hpicfByodTcpStatsHttpPktsSent": hpicfByodTcpStatsHttpPktsSent,
       "hpicfByodTcpStatsStateSynRcvd": hpicfByodTcpStatsStateSynRcvd,
       "hpicfByodTcpStatsStateEstablished": hpicfByodTcpStatsStateEstablished,
       "hpicfByodConformance": hpicfByodConformance,
       "hpicfByodCompliances": hpicfByodCompliances,
       "hpicfByodCompliance1": hpicfByodCompliance1,
       "hpicfByodGroups": hpicfByodGroups,
       "hpicfByodConfigGroup": hpicfByodConfigGroup,
       "hpicfByodStatsGroup": hpicfByodStatsGroup}
)
