# SNMP MIB module (HUAWEI-SECURITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-SECURITY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:05:52 2024
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

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

hwSecurityMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165)
)
hwSecurityMIB.setRevisions(
        ("2015-10-14 14:20",
         "2015-09-29 16:48",
         "2015-05-26 20:23",
         "2015-04-07 11:02",
         "2015-03-24 10:12",
         "2014-09-18 20:20",
         "2014-09-18 20:20",
         "2013-10-24 15:29",
         "2013-10-18 11:23",
         "2013-06-05 17:56",
         "2013-05-20 14:04",
         "2013-04-17 11:11",
         "2013-04-08 16:53",
         "2013-03-06 14:43",
         "2014-04-04 13:01",
         "2015-03-24 10:12")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwBaseSecurityMIBObjects_ObjectIdentity = ObjectIdentity
hwBaseSecurityMIBObjects = _HwBaseSecurityMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1)
)
_HwLocalUrpf_ObjectIdentity = ObjectIdentity
hwLocalUrpf = _HwLocalUrpf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 2)
)
_HwLocalUrpfTable_Object = MibTable
hwLocalUrpfTable = _HwLocalUrpfTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hwLocalUrpfTable.setStatus("current")
_HwLocalUrpfEntry_Object = MibTableRow
hwLocalUrpfEntry = _HwLocalUrpfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 2, 1, 1)
)
hwLocalUrpfEntry.setIndexNames(
    (0, "HUAWEI-SECURITY-MIB", "hwLocalUrpfChassisId"),
    (0, "HUAWEI-SECURITY-MIB", "hwLocalUrpfSlotId"),
)
if mibBuilder.loadTexts:
    hwLocalUrpfEntry.setStatus("current")


class _HwLocalUrpfChassisId_Type(Integer32):
    """Custom type hwLocalUrpfChassisId based on Integer32"""
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
        *(("clc1", 1),
          ("clc2", 2),
          ("clc3", 3),
          ("clc4", 4),
          ("clc5", 5),
          ("clc6", 6),
          ("clc7", 7),
          ("clc8", 8))
    )


_HwLocalUrpfChassisId_Type.__name__ = "Integer32"
_HwLocalUrpfChassisId_Object = MibTableColumn
hwLocalUrpfChassisId = _HwLocalUrpfChassisId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 2, 1, 1, 1),
    _HwLocalUrpfChassisId_Type()
)
hwLocalUrpfChassisId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwLocalUrpfChassisId.setStatus("current")


class _HwLocalUrpfSlotId_Type(Integer32):
    """Custom type hwLocalUrpfSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HwLocalUrpfSlotId_Type.__name__ = "Integer32"
_HwLocalUrpfSlotId_Object = MibTableColumn
hwLocalUrpfSlotId = _HwLocalUrpfSlotId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 2, 1, 1, 2),
    _HwLocalUrpfSlotId_Type()
)
hwLocalUrpfSlotId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwLocalUrpfSlotId.setStatus("current")
_HwLocalUrpfCurrentRateLow_Type = Integer32
_HwLocalUrpfCurrentRateLow_Object = MibTableColumn
hwLocalUrpfCurrentRateLow = _HwLocalUrpfCurrentRateLow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 2, 1, 1, 11),
    _HwLocalUrpfCurrentRateLow_Type()
)
hwLocalUrpfCurrentRateLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLocalUrpfCurrentRateLow.setStatus("current")
_HwLocalUrpfCurrentRateHigh_Type = Integer32
_HwLocalUrpfCurrentRateHigh_Object = MibTableColumn
hwLocalUrpfCurrentRateHigh = _HwLocalUrpfCurrentRateHigh_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 2, 1, 1, 12),
    _HwLocalUrpfCurrentRateHigh_Type()
)
hwLocalUrpfCurrentRateHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLocalUrpfCurrentRateHigh.setStatus("current")
_HwLocalUrpfNotifyEnabledStatus_Type = EnabledStatus
_HwLocalUrpfNotifyEnabledStatus_Object = MibTableColumn
hwLocalUrpfNotifyEnabledStatus = _HwLocalUrpfNotifyEnabledStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 2, 1, 1, 13),
    _HwLocalUrpfNotifyEnabledStatus_Type()
)
hwLocalUrpfNotifyEnabledStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLocalUrpfNotifyEnabledStatus.setStatus("current")
_HwLocalUrpfRateThreshold_Type = Integer32
_HwLocalUrpfRateThreshold_Object = MibTableColumn
hwLocalUrpfRateThreshold = _HwLocalUrpfRateThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 2, 1, 1, 14),
    _HwLocalUrpfRateThreshold_Type()
)
hwLocalUrpfRateThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLocalUrpfRateThreshold.setStatus("current")
_HwLocalUrpfRateInterval_Type = Integer32
_HwLocalUrpfRateInterval_Object = MibTableColumn
hwLocalUrpfRateInterval = _HwLocalUrpfRateInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 2, 1, 1, 15),
    _HwLocalUrpfRateInterval_Type()
)
hwLocalUrpfRateInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLocalUrpfRateInterval.setStatus("current")
_HwTcpIpDefend_ObjectIdentity = ObjectIdentity
hwTcpIpDefend = _HwTcpIpDefend_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 3)
)
_HwTcpIpDefendTable_Object = MibTable
hwTcpIpDefendTable = _HwTcpIpDefendTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hwTcpIpDefendTable.setStatus("current")
_HwTcpIpDefendEntry_Object = MibTableRow
hwTcpIpDefendEntry = _HwTcpIpDefendEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 3, 1, 1)
)
hwTcpIpDefendEntry.setIndexNames(
    (0, "HUAWEI-SECURITY-MIB", "hwTcpIpDefendChassisId"),
    (0, "HUAWEI-SECURITY-MIB", "hwTcpIpDefendSlotId"),
    (0, "HUAWEI-SECURITY-MIB", "hwTcpIpDefendType"),
)
if mibBuilder.loadTexts:
    hwTcpIpDefendEntry.setStatus("current")


class _HwTcpIpDefendChassisId_Type(Integer32):
    """Custom type hwTcpIpDefendChassisId based on Integer32"""
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
        *(("clc1", 1),
          ("clc2", 2),
          ("clc3", 3),
          ("clc4", 4),
          ("clc5", 5),
          ("clc6", 6),
          ("clc7", 7),
          ("clc8", 8))
    )


_HwTcpIpDefendChassisId_Type.__name__ = "Integer32"
_HwTcpIpDefendChassisId_Object = MibTableColumn
hwTcpIpDefendChassisId = _HwTcpIpDefendChassisId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 3, 1, 1, 1),
    _HwTcpIpDefendChassisId_Type()
)
hwTcpIpDefendChassisId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwTcpIpDefendChassisId.setStatus("current")


class _HwTcpIpDefendSlotId_Type(Integer32):
    """Custom type hwTcpIpDefendSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HwTcpIpDefendSlotId_Type.__name__ = "Integer32"
_HwTcpIpDefendSlotId_Object = MibTableColumn
hwTcpIpDefendSlotId = _HwTcpIpDefendSlotId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 3, 1, 1, 2),
    _HwTcpIpDefendSlotId_Type()
)
hwTcpIpDefendSlotId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwTcpIpDefendSlotId.setStatus("current")


class _HwTcpIpDefendType_Type(Integer32):
    """Custom type hwTcpIpDefendType based on Integer32"""
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
        *(("abnormalPacket", 1),
          ("ipFragmentation", 4),
          ("tcpSyn", 3),
          ("udpPacket", 2))
    )


_HwTcpIpDefendType_Type.__name__ = "Integer32"
_HwTcpIpDefendType_Object = MibTableColumn
hwTcpIpDefendType = _HwTcpIpDefendType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 3, 1, 1, 3),
    _HwTcpIpDefendType_Type()
)
hwTcpIpDefendType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwTcpIpDefendType.setStatus("current")
_HwTcpIpDefendCurrentRateLow_Type = Integer32
_HwTcpIpDefendCurrentRateLow_Object = MibTableColumn
hwTcpIpDefendCurrentRateLow = _HwTcpIpDefendCurrentRateLow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 3, 1, 1, 11),
    _HwTcpIpDefendCurrentRateLow_Type()
)
hwTcpIpDefendCurrentRateLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTcpIpDefendCurrentRateLow.setStatus("current")
_HwTcpIpDefendCurrentRateHigh_Type = Integer32
_HwTcpIpDefendCurrentRateHigh_Object = MibTableColumn
hwTcpIpDefendCurrentRateHigh = _HwTcpIpDefendCurrentRateHigh_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 3, 1, 1, 12),
    _HwTcpIpDefendCurrentRateHigh_Type()
)
hwTcpIpDefendCurrentRateHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTcpIpDefendCurrentRateHigh.setStatus("current")
_HwTcpIpDefendNotifyEnabledStatus_Type = EnabledStatus
_HwTcpIpDefendNotifyEnabledStatus_Object = MibTableColumn
hwTcpIpDefendNotifyEnabledStatus = _HwTcpIpDefendNotifyEnabledStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 3, 1, 1, 13),
    _HwTcpIpDefendNotifyEnabledStatus_Type()
)
hwTcpIpDefendNotifyEnabledStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTcpIpDefendNotifyEnabledStatus.setStatus("current")
_HwTcpIpDefendRateThreshold_Type = Integer32
_HwTcpIpDefendRateThreshold_Object = MibTableColumn
hwTcpIpDefendRateThreshold = _HwTcpIpDefendRateThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 3, 1, 1, 14),
    _HwTcpIpDefendRateThreshold_Type()
)
hwTcpIpDefendRateThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTcpIpDefendRateThreshold.setStatus("current")
_HwTcpIpDefendRateInterval_Type = Integer32
_HwTcpIpDefendRateInterval_Object = MibTableColumn
hwTcpIpDefendRateInterval = _HwTcpIpDefendRateInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 3, 1, 1, 15),
    _HwTcpIpDefendRateInterval_Type()
)
hwTcpIpDefendRateInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTcpIpDefendRateInterval.setStatus("current")
_HwTcpIpDefendProtocolDescirption_Type = OctetString
_HwTcpIpDefendProtocolDescirption_Object = MibTableColumn
hwTcpIpDefendProtocolDescirption = _HwTcpIpDefendProtocolDescirption_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 3, 1, 1, 16),
    _HwTcpIpDefendProtocolDescirption_Type()
)
hwTcpIpDefendProtocolDescirption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTcpIpDefendProtocolDescirption.setStatus("current")
_HwMaDefend_ObjectIdentity = ObjectIdentity
hwMaDefend = _HwMaDefend_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 4)
)
_HwMaDefendTable_Object = MibTable
hwMaDefendTable = _HwMaDefendTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 4, 1)
)
if mibBuilder.loadTexts:
    hwMaDefendTable.setStatus("current")
_HwMaDefendEntry_Object = MibTableRow
hwMaDefendEntry = _HwMaDefendEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 4, 1, 1)
)
hwMaDefendEntry.setIndexNames(
    (0, "HUAWEI-SECURITY-MIB", "hwMaDefendChassisId"),
    (0, "HUAWEI-SECURITY-MIB", "hwMaDefendSlotId"),
    (0, "HUAWEI-SECURITY-MIB", "hwMaDefendProtocol"),
)
if mibBuilder.loadTexts:
    hwMaDefendEntry.setStatus("current")


class _HwMaDefendChassisId_Type(Integer32):
    """Custom type hwMaDefendChassisId based on Integer32"""
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
        *(("clc1", 1),
          ("clc2", 2),
          ("clc3", 3),
          ("clc4", 4),
          ("clc5", 5),
          ("clc6", 6),
          ("clc7", 7),
          ("clc8", 8))
    )


_HwMaDefendChassisId_Type.__name__ = "Integer32"
_HwMaDefendChassisId_Object = MibTableColumn
hwMaDefendChassisId = _HwMaDefendChassisId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 4, 1, 1, 1),
    _HwMaDefendChassisId_Type()
)
hwMaDefendChassisId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMaDefendChassisId.setStatus("current")


class _HwMaDefendSlotId_Type(Integer32):
    """Custom type hwMaDefendSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HwMaDefendSlotId_Type.__name__ = "Integer32"
_HwMaDefendSlotId_Object = MibTableColumn
hwMaDefendSlotId = _HwMaDefendSlotId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 4, 1, 1, 2),
    _HwMaDefendSlotId_Type()
)
hwMaDefendSlotId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMaDefendSlotId.setStatus("current")


class _HwMaDefendProtocol_Type(Integer32):
    """Custom type hwMaDefendProtocol based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("bgp", 6),
          ("dhcpc", 15),
          ("dhcpr", 16),
          ("ftp", 1),
          ("ipprotocol", 19),
          ("isis", 11),
          ("ldp", 7),
          ("lspping", 14),
          ("ntp", 13),
          ("ospf", 9),
          ("pim", 12),
          ("rip", 10),
          ("rsvp", 8),
          ("snmp", 3),
          ("ssh", 2),
          ("tcp", 17),
          ("telnet", 4),
          ("tftp", 5),
          ("udp", 18))
    )


_HwMaDefendProtocol_Type.__name__ = "Integer32"
_HwMaDefendProtocol_Object = MibTableColumn
hwMaDefendProtocol = _HwMaDefendProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 4, 1, 1, 3),
    _HwMaDefendProtocol_Type()
)
hwMaDefendProtocol.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMaDefendProtocol.setStatus("current")
_HwMaDefendCurrentRateLow_Type = Integer32
_HwMaDefendCurrentRateLow_Object = MibTableColumn
hwMaDefendCurrentRateLow = _HwMaDefendCurrentRateLow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 4, 1, 1, 11),
    _HwMaDefendCurrentRateLow_Type()
)
hwMaDefendCurrentRateLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMaDefendCurrentRateLow.setStatus("current")
_HwMaDefendCurrentRateHigh_Type = Integer32
_HwMaDefendCurrentRateHigh_Object = MibTableColumn
hwMaDefendCurrentRateHigh = _HwMaDefendCurrentRateHigh_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 4, 1, 1, 12),
    _HwMaDefendCurrentRateHigh_Type()
)
hwMaDefendCurrentRateHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMaDefendCurrentRateHigh.setStatus("current")
_HwMaDefendNotifyEnabledStatus_Type = EnabledStatus
_HwMaDefendNotifyEnabledStatus_Object = MibTableColumn
hwMaDefendNotifyEnabledStatus = _HwMaDefendNotifyEnabledStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 4, 1, 1, 13),
    _HwMaDefendNotifyEnabledStatus_Type()
)
hwMaDefendNotifyEnabledStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMaDefendNotifyEnabledStatus.setStatus("current")
_HwMaDefendRateThreshold_Type = Integer32
_HwMaDefendRateThreshold_Object = MibTableColumn
hwMaDefendRateThreshold = _HwMaDefendRateThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 4, 1, 1, 14),
    _HwMaDefendRateThreshold_Type()
)
hwMaDefendRateThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMaDefendRateThreshold.setStatus("current")
_HwMaDefendRateInterval_Type = Integer32
_HwMaDefendRateInterval_Object = MibTableColumn
hwMaDefendRateInterval = _HwMaDefendRateInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 4, 1, 1, 15),
    _HwMaDefendRateInterval_Type()
)
hwMaDefendRateInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMaDefendRateInterval.setStatus("current")
_HwApplicationApperceive_ObjectIdentity = ObjectIdentity
hwApplicationApperceive = _HwApplicationApperceive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 5)
)
_HwApplicationApperceiveTable_Object = MibTable
hwApplicationApperceiveTable = _HwApplicationApperceiveTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 5, 1)
)
if mibBuilder.loadTexts:
    hwApplicationApperceiveTable.setStatus("current")
_HwApplicationApperceiveEntry_Object = MibTableRow
hwApplicationApperceiveEntry = _HwApplicationApperceiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 5, 1, 1)
)
hwApplicationApperceiveEntry.setIndexNames(
    (0, "HUAWEI-SECURITY-MIB", "hwAppliApperChassisId"),
    (0, "HUAWEI-SECURITY-MIB", "hwAppliApperSlotId"),
    (0, "HUAWEI-SECURITY-MIB", "hwAppliApperProtocol"),
)
if mibBuilder.loadTexts:
    hwApplicationApperceiveEntry.setStatus("current")


class _HwAppliApperChassisId_Type(Integer32):
    """Custom type hwAppliApperChassisId based on Integer32"""
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
        *(("clc1", 1),
          ("clc2", 2),
          ("clc3", 3),
          ("clc4", 4),
          ("clc5", 5),
          ("clc6", 6),
          ("clc7", 7),
          ("clc8", 8))
    )


_HwAppliApperChassisId_Type.__name__ = "Integer32"
_HwAppliApperChassisId_Object = MibTableColumn
hwAppliApperChassisId = _HwAppliApperChassisId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 5, 1, 1, 1),
    _HwAppliApperChassisId_Type()
)
hwAppliApperChassisId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwAppliApperChassisId.setStatus("current")


class _HwAppliApperSlotId_Type(Integer32):
    """Custom type hwAppliApperSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HwAppliApperSlotId_Type.__name__ = "Integer32"
_HwAppliApperSlotId_Object = MibTableColumn
hwAppliApperSlotId = _HwAppliApperSlotId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 5, 1, 1, 2),
    _HwAppliApperSlotId_Type()
)
hwAppliApperSlotId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwAppliApperSlotId.setStatus("current")


class _HwAppliApperProtocol_Type(Integer32):
    """Custom type hwAppliApperProtocol based on Integer32"""
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
              35,
              36,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74)
        )
    )
    namedValues = NamedValues(
        *(("bfd", 28),
          ("bgp", 6),
          ("bgpv6", 72),
          ("bpdu", 17),
          ("dhcp", 18),
          ("dnsClient", 35),
          ("dnsv6", 68),
          ("eth8021ag", 30),
          ("ftpClient", 31),
          ("ftpServer", 1),
          ("ftpv6Client", 73),
          ("ftpv6Server", 74),
          ("hwTacacs", 22),
          ("icmp", 13),
          ("icmpv6", 67),
          ("igmp", 24),
          ("ipv4Arp", 16),
          ("isis", 11),
          ("lacp", 19),
          ("ldp", 7),
          ("lspPing", 23),
          ("mplsOam", 29),
          ("msdp", 14),
          ("ntp", 20),
          ("ospf", 9),
          ("ospfv3", 71),
          ("pim", 15),
          ("pimv6", 69),
          ("radius", 21),
          ("rip", 10),
          ("rrpp", 26),
          ("rsvp", 8),
          ("sftpClient", 34),
          ("sftpSever", 12),
          ("snmp", 3),
          ("sshClient", 33),
          ("sshServer", 2),
          ("sshv6Server", 70),
          ("telnetClient", 32),
          ("telnetServer", 4),
          ("telnetv6Client", 65),
          ("telnetv6Server", 64),
          ("tftp", 5),
          ("tftpv6Client", 66),
          ("vgmp", 25),
          ("vrrp", 27),
          ("webAuthServer", 36))
    )


_HwAppliApperProtocol_Type.__name__ = "Integer32"
_HwAppliApperProtocol_Object = MibTableColumn
hwAppliApperProtocol = _HwAppliApperProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 5, 1, 1, 3),
    _HwAppliApperProtocol_Type()
)
hwAppliApperProtocol.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwAppliApperProtocol.setStatus("current")
_HwAppliApperCurrentRateLow_Type = Integer32
_HwAppliApperCurrentRateLow_Object = MibTableColumn
hwAppliApperCurrentRateLow = _HwAppliApperCurrentRateLow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 5, 1, 1, 11),
    _HwAppliApperCurrentRateLow_Type()
)
hwAppliApperCurrentRateLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAppliApperCurrentRateLow.setStatus("current")
_HwAppliApperCurrentRateHigh_Type = Integer32
_HwAppliApperCurrentRateHigh_Object = MibTableColumn
hwAppliApperCurrentRateHigh = _HwAppliApperCurrentRateHigh_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 5, 1, 1, 12),
    _HwAppliApperCurrentRateHigh_Type()
)
hwAppliApperCurrentRateHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAppliApperCurrentRateHigh.setStatus("current")
_HwAppliApperNotifyEnabledStatus_Type = EnabledStatus
_HwAppliApperNotifyEnabledStatus_Object = MibTableColumn
hwAppliApperNotifyEnabledStatus = _HwAppliApperNotifyEnabledStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 5, 1, 1, 13),
    _HwAppliApperNotifyEnabledStatus_Type()
)
hwAppliApperNotifyEnabledStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAppliApperNotifyEnabledStatus.setStatus("current")
_HwAppliApperRateThreshold_Type = Integer32
_HwAppliApperRateThreshold_Object = MibTableColumn
hwAppliApperRateThreshold = _HwAppliApperRateThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 5, 1, 1, 14),
    _HwAppliApperRateThreshold_Type()
)
hwAppliApperRateThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAppliApperRateThreshold.setStatus("current")
_HwAppliApperRateInterval_Type = Integer32
_HwAppliApperRateInterval_Object = MibTableColumn
hwAppliApperRateInterval = _HwAppliApperRateInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 5, 1, 1, 15),
    _HwAppliApperRateInterval_Type()
)
hwAppliApperRateInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAppliApperRateInterval.setStatus("current")
_HwAppliApperProtocolDescirption_Type = OctetString
_HwAppliApperProtocolDescirption_Object = MibTableColumn
hwAppliApperProtocolDescirption = _HwAppliApperProtocolDescirption_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 5, 1, 1, 16),
    _HwAppliApperProtocolDescirption_Type()
)
hwAppliApperProtocolDescirption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAppliApperProtocolDescirption.setStatus("current")
_HwDefdPortVlan_ObjectIdentity = ObjectIdentity
hwDefdPortVlan = _HwDefdPortVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 6)
)
_HwDefdPortVlanTable_Object = MibTable
hwDefdPortVlanTable = _HwDefdPortVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 6, 1)
)
if mibBuilder.loadTexts:
    hwDefdPortVlanTable.setStatus("current")
_HwDefdPortVlanEntry_Object = MibTableRow
hwDefdPortVlanEntry = _HwDefdPortVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 6, 1, 1)
)
hwDefdPortVlanEntry.setIndexNames(
    (0, "HUAWEI-SECURITY-MIB", "hwDefdPortVlanIfIndex"),
)
if mibBuilder.loadTexts:
    hwDefdPortVlanEntry.setStatus("current")


class _HwDefdPortVlanIfIndex_Type(Integer32):
    """Custom type hwDefdPortVlanIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwDefdPortVlanIfIndex_Type.__name__ = "Integer32"
_HwDefdPortVlanIfIndex_Object = MibTableColumn
hwDefdPortVlanIfIndex = _HwDefdPortVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 6, 1, 1, 1),
    _HwDefdPortVlanIfIndex_Type()
)
hwDefdPortVlanIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwDefdPortVlanIfIndex.setStatus("current")


class _HwDefdPortVlanIfName_Type(OctetString):
    """Custom type hwDefdPortVlanIfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_HwDefdPortVlanIfName_Type.__name__ = "OctetString"
_HwDefdPortVlanIfName_Object = MibTableColumn
hwDefdPortVlanIfName = _HwDefdPortVlanIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 6, 1, 1, 2),
    _HwDefdPortVlanIfName_Type()
)
hwDefdPortVlanIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDefdPortVlanIfName.setStatus("current")


class _HwDefdPortVlanId_Type(Integer32):
    """Custom type hwDefdPortVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_HwDefdPortVlanId_Type.__name__ = "Integer32"
_HwDefdPortVlanId_Object = MibTableColumn
hwDefdPortVlanId = _HwDefdPortVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 6, 1, 1, 3),
    _HwDefdPortVlanId_Type()
)
hwDefdPortVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDefdPortVlanId.setStatus("current")


class _HwDefdPortVlanCheckProtocol_Type(OctetString):
    """Custom type hwDefdPortVlanCheckProtocol based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_HwDefdPortVlanCheckProtocol_Type.__name__ = "OctetString"
_HwDefdPortVlanCheckProtocol_Object = MibTableColumn
hwDefdPortVlanCheckProtocol = _HwDefdPortVlanCheckProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 6, 1, 1, 4),
    _HwDefdPortVlanCheckProtocol_Type()
)
hwDefdPortVlanCheckProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDefdPortVlanCheckProtocol.setStatus("current")
_HwSocAttackTrapObject_ObjectIdentity = ObjectIdentity
hwSocAttackTrapObject = _HwSocAttackTrapObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 7)
)
_HwSocAttackInfoTable_Object = MibTable
hwSocAttackInfoTable = _HwSocAttackInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 7, 1)
)
if mibBuilder.loadTexts:
    hwSocAttackInfoTable.setStatus("current")
_HwSocAttackInfoEntry_Object = MibTableRow
hwSocAttackInfoEntry = _HwSocAttackInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 7, 1, 1)
)
hwSocAttackInfoEntry.setIndexNames(
    (0, "HUAWEI-SECURITY-MIB", "hwSocAttackSeqNo"),
)
if mibBuilder.loadTexts:
    hwSocAttackInfoEntry.setStatus("current")


class _HwSocAttackSeqNo_Type(Integer32):
    """Custom type hwSocAttackSeqNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_HwSocAttackSeqNo_Type.__name__ = "Integer32"
_HwSocAttackSeqNo_Object = MibTableColumn
hwSocAttackSeqNo = _HwSocAttackSeqNo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 7, 1, 1, 1),
    _HwSocAttackSeqNo_Type()
)
hwSocAttackSeqNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSocAttackSeqNo.setStatus("current")


class _HwSocAttackPossib_Type(OctetString):
    """Custom type hwSocAttackPossib based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwSocAttackPossib_Type.__name__ = "OctetString"
_HwSocAttackPossib_Object = MibTableColumn
hwSocAttackPossib = _HwSocAttackPossib_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 7, 1, 1, 2),
    _HwSocAttackPossib_Type()
)
hwSocAttackPossib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSocAttackPossib.setStatus("current")


class _HwSocAttackReason_Type(OctetString):
    """Custom type hwSocAttackReason based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_HwSocAttackReason_Type.__name__ = "OctetString"
_HwSocAttackReason_Object = MibTableColumn
hwSocAttackReason = _HwSocAttackReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 7, 1, 1, 3),
    _HwSocAttackReason_Type()
)
hwSocAttackReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSocAttackReason.setStatus("current")


class _HwSocAttackIfName_Type(OctetString):
    """Custom type hwSocAttackIfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_HwSocAttackIfName_Type.__name__ = "OctetString"
_HwSocAttackIfName_Object = MibTableColumn
hwSocAttackIfName = _HwSocAttackIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 7, 1, 1, 4),
    _HwSocAttackIfName_Type()
)
hwSocAttackIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSocAttackIfName.setStatus("current")


class _HwSocAttackSubIfName_Type(OctetString):
    """Custom type hwSocAttackSubIfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HwSocAttackSubIfName_Type.__name__ = "OctetString"
_HwSocAttackSubIfName_Object = MibTableColumn
hwSocAttackSubIfName = _HwSocAttackSubIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 7, 1, 1, 5),
    _HwSocAttackSubIfName_Type()
)
hwSocAttackSubIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSocAttackSubIfName.setStatus("current")


class _HwSocAttackVlanIndex_Type(OctetString):
    """Custom type hwSocAttackVlanIndex based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwSocAttackVlanIndex_Type.__name__ = "OctetString"
_HwSocAttackVlanIndex_Object = MibTableColumn
hwSocAttackVlanIndex = _HwSocAttackVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 7, 1, 1, 6),
    _HwSocAttackVlanIndex_Type()
)
hwSocAttackVlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSocAttackVlanIndex.setStatus("current")


class _HwSocAttackUserQinQIndex_Type(OctetString):
    """Custom type hwSocAttackUserQinQIndex based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwSocAttackUserQinQIndex_Type.__name__ = "OctetString"
_HwSocAttackUserQinQIndex_Object = MibTableColumn
hwSocAttackUserQinQIndex = _HwSocAttackUserQinQIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 7, 1, 1, 7),
    _HwSocAttackUserQinQIndex_Type()
)
hwSocAttackUserQinQIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSocAttackUserQinQIndex.setStatus("current")


class _HwSocAttackMacAddr_Type(OctetString):
    """Custom type hwSocAttackMacAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HwSocAttackMacAddr_Type.__name__ = "OctetString"
_HwSocAttackMacAddr_Object = MibTableColumn
hwSocAttackMacAddr = _HwSocAttackMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 7, 1, 1, 8),
    _HwSocAttackMacAddr_Type()
)
hwSocAttackMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSocAttackMacAddr.setStatus("current")


class _HwSocAttackIPAddr_Type(OctetString):
    """Custom type hwSocAttackIPAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HwSocAttackIPAddr_Type.__name__ = "OctetString"
_HwSocAttackIPAddr_Object = MibTableColumn
hwSocAttackIPAddr = _HwSocAttackIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 7, 1, 1, 9),
    _HwSocAttackIPAddr_Type()
)
hwSocAttackIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSocAttackIPAddr.setStatus("current")


class _HwSocAttackIPv6Addr_Type(OctetString):
    """Custom type hwSocAttackIPv6Addr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HwSocAttackIPv6Addr_Type.__name__ = "OctetString"
_HwSocAttackIPv6Addr_Object = MibTableColumn
hwSocAttackIPv6Addr = _HwSocAttackIPv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 7, 1, 1, 10),
    _HwSocAttackIPv6Addr_Type()
)
hwSocAttackIPv6Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSocAttackIPv6Addr.setStatus("current")
_HwBaseSecurityNotifications_ObjectIdentity = ObjectIdentity
hwBaseSecurityNotifications = _HwBaseSecurityNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 11)
)
_HwMacFilter_ObjectIdentity = ObjectIdentity
hwMacFilter = _HwMacFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 12)
)
_HwMacFilterModeTable_Object = MibTable
hwMacFilterModeTable = _HwMacFilterModeTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 12, 1)
)
if mibBuilder.loadTexts:
    hwMacFilterModeTable.setStatus("current")
_HwMacFilterModeEntry_Object = MibTableRow
hwMacFilterModeEntry = _HwMacFilterModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 12, 1, 1)
)
hwMacFilterModeEntry.setIndexNames(
    (0, "HUAWEI-SECURITY-MIB", "hwMacFilterIfIndex"),
)
if mibBuilder.loadTexts:
    hwMacFilterModeEntry.setStatus("current")
_HwMacFilterIfIndex_Type = Integer32
_HwMacFilterIfIndex_Object = MibTableColumn
hwMacFilterIfIndex = _HwMacFilterIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 12, 1, 1, 1),
    _HwMacFilterIfIndex_Type()
)
hwMacFilterIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMacFilterIfIndex.setStatus("current")


class _HwMacFilterInterface_Type(DisplayString):
    """Custom type hwMacFilterInterface based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HwMacFilterInterface_Type.__name__ = "DisplayString"
_HwMacFilterInterface_Object = MibTableColumn
hwMacFilterInterface = _HwMacFilterInterface_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 12, 1, 1, 2),
    _HwMacFilterInterface_Type()
)
hwMacFilterInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacFilterInterface.setStatus("current")


class _HwMacFilterEnableMode_Type(Integer32):
    """Custom type hwMacFilterEnableMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("balcklist", 2),
          ("none", 0),
          ("whitelist", 1))
    )


_HwMacFilterEnableMode_Type.__name__ = "Integer32"
_HwMacFilterEnableMode_Object = MibTableColumn
hwMacFilterEnableMode = _HwMacFilterEnableMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 12, 1, 1, 3),
    _HwMacFilterEnableMode_Type()
)
hwMacFilterEnableMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacFilterEnableMode.setStatus("current")
_HwMacFilterMatchNum_Type = Integer32
_HwMacFilterMatchNum_Object = MibTableColumn
hwMacFilterMatchNum = _HwMacFilterMatchNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 12, 1, 1, 4),
    _HwMacFilterMatchNum_Type()
)
hwMacFilterMatchNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacFilterMatchNum.setStatus("current")
_HwMacFilterMacAddrTable_Object = MibTable
hwMacFilterMacAddrTable = _HwMacFilterMacAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 12, 2)
)
if mibBuilder.loadTexts:
    hwMacFilterMacAddrTable.setStatus("current")
_HwMacFilterMacAddrEntry_Object = MibTableRow
hwMacFilterMacAddrEntry = _HwMacFilterMacAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 12, 2, 1)
)
hwMacFilterMacAddrEntry.setIndexNames(
    (0, "HUAWEI-SECURITY-MIB", "hwMacFilterIfindex"),
    (0, "HUAWEI-SECURITY-MIB", "hwMacFilterMacAddr"),
)
if mibBuilder.loadTexts:
    hwMacFilterMacAddrEntry.setStatus("current")
_HwMacFilterIfindex_Type = Integer32
_HwMacFilterIfindex_Object = MibTableColumn
hwMacFilterIfindex = _HwMacFilterIfindex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 12, 2, 1, 1),
    _HwMacFilterIfindex_Type()
)
hwMacFilterIfindex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMacFilterIfindex.setStatus("current")


class _HwMacFilterInterfaceBuf_Type(DisplayString):
    """Custom type hwMacFilterInterfaceBuf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HwMacFilterInterfaceBuf_Type.__name__ = "DisplayString"
_HwMacFilterInterfaceBuf_Object = MibTableColumn
hwMacFilterInterfaceBuf = _HwMacFilterInterfaceBuf_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 12, 2, 1, 2),
    _HwMacFilterInterfaceBuf_Type()
)
hwMacFilterInterfaceBuf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacFilterInterfaceBuf.setStatus("current")


class _HwMacFilterMacAddr_Type(DisplayString):
    """Custom type hwMacFilterMacAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_HwMacFilterMacAddr_Type.__name__ = "DisplayString"
_HwMacFilterMacAddr_Object = MibTableColumn
hwMacFilterMacAddr = _HwMacFilterMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 12, 2, 1, 3),
    _HwMacFilterMacAddr_Type()
)
hwMacFilterMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMacFilterMacAddr.setStatus("current")
_HwBaseSecurityStormControlInterfaceObjects_ObjectIdentity = ObjectIdentity
hwBaseSecurityStormControlInterfaceObjects = _HwBaseSecurityStormControlInterfaceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 13)
)
_HwBaseSecurityStormControlInterfaceTable_Object = MibTable
hwBaseSecurityStormControlInterfaceTable = _HwBaseSecurityStormControlInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 13, 1)
)
if mibBuilder.loadTexts:
    hwBaseSecurityStormControlInterfaceTable.setStatus("current")
_HwBaseSecurityStormControlInterfaceEntry_Object = MibTableRow
hwBaseSecurityStormControlInterfaceEntry = _HwBaseSecurityStormControlInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 13, 1, 1)
)
hwBaseSecurityStormControlInterfaceEntry.setIndexNames(
    (0, "HUAWEI-SECURITY-MIB", "hwBaseSecurityStormControlInterfaceChassisId"),
    (0, "HUAWEI-SECURITY-MIB", "hwBaseSecurityStormControlInterfaceSlotId"),
)
if mibBuilder.loadTexts:
    hwBaseSecurityStormControlInterfaceEntry.setStatus("current")


class _HwBaseSecurityStormControlInterfaceChassisId_Type(Integer32):
    """Custom type hwBaseSecurityStormControlInterfaceChassisId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_HwBaseSecurityStormControlInterfaceChassisId_Type.__name__ = "Integer32"
_HwBaseSecurityStormControlInterfaceChassisId_Object = MibTableColumn
hwBaseSecurityStormControlInterfaceChassisId = _HwBaseSecurityStormControlInterfaceChassisId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 13, 1, 1, 1),
    _HwBaseSecurityStormControlInterfaceChassisId_Type()
)
hwBaseSecurityStormControlInterfaceChassisId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwBaseSecurityStormControlInterfaceChassisId.setStatus("current")


class _HwBaseSecurityStormControlInterfaceSlotId_Type(Integer32):
    """Custom type hwBaseSecurityStormControlInterfaceSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_HwBaseSecurityStormControlInterfaceSlotId_Type.__name__ = "Integer32"
_HwBaseSecurityStormControlInterfaceSlotId_Object = MibTableColumn
hwBaseSecurityStormControlInterfaceSlotId = _HwBaseSecurityStormControlInterfaceSlotId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 13, 1, 1, 2),
    _HwBaseSecurityStormControlInterfaceSlotId_Type()
)
hwBaseSecurityStormControlInterfaceSlotId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwBaseSecurityStormControlInterfaceSlotId.setStatus("current")


class _HwBaseSecurityStormControlInterfaceName_Type(OctetString):
    """Custom type hwBaseSecurityStormControlInterfaceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_HwBaseSecurityStormControlInterfaceName_Type.__name__ = "OctetString"
_HwBaseSecurityStormControlInterfaceName_Object = MibTableColumn
hwBaseSecurityStormControlInterfaceName = _HwBaseSecurityStormControlInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 13, 1, 1, 3),
    _HwBaseSecurityStormControlInterfaceName_Type()
)
hwBaseSecurityStormControlInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBaseSecurityStormControlInterfaceName.setStatus("current")


class _HwBaseSecurityStormControlInterfaceVlanID_Type(Integer32):
    """Custom type hwBaseSecurityStormControlInterfaceVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwBaseSecurityStormControlInterfaceVlanID_Type.__name__ = "Integer32"
_HwBaseSecurityStormControlInterfaceVlanID_Object = MibTableColumn
hwBaseSecurityStormControlInterfaceVlanID = _HwBaseSecurityStormControlInterfaceVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 13, 1, 1, 4),
    _HwBaseSecurityStormControlInterfaceVlanID_Type()
)
hwBaseSecurityStormControlInterfaceVlanID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwBaseSecurityStormControlInterfaceVlanID.setStatus("current")
_HwBaseArpVlanCarTrapObject_ObjectIdentity = ObjectIdentity
hwBaseArpVlanCarTrapObject = _HwBaseArpVlanCarTrapObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 14)
)
_HwBaseArpVlanCarInfoTable_Object = MibTable
hwBaseArpVlanCarInfoTable = _HwBaseArpVlanCarInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 14, 1)
)
if mibBuilder.loadTexts:
    hwBaseArpVlanCarInfoTable.setStatus("current")
_HwBaseArpVlanCarInfoEntry_Object = MibTableRow
hwBaseArpVlanCarInfoEntry = _HwBaseArpVlanCarInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 14, 1, 1)
)
hwBaseArpVlanCarInfoEntry.setIndexNames(
    (0, "HUAWEI-SECURITY-MIB", "hwBaseArpVlanCarLogIfName"),
    (0, "HUAWEI-SECURITY-MIB", "hwBaseArpVlanCarPhyIfName"),
)
if mibBuilder.loadTexts:
    hwBaseArpVlanCarInfoEntry.setStatus("current")
_HwBaseArpVlanCarLogIfName_Type = OctetString
_HwBaseArpVlanCarLogIfName_Object = MibTableColumn
hwBaseArpVlanCarLogIfName = _HwBaseArpVlanCarLogIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 14, 1, 1, 1),
    _HwBaseArpVlanCarLogIfName_Type()
)
hwBaseArpVlanCarLogIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBaseArpVlanCarLogIfName.setStatus("current")
_HwBaseArpVlanCarPhyIfName_Type = OctetString
_HwBaseArpVlanCarPhyIfName_Object = MibTableColumn
hwBaseArpVlanCarPhyIfName = _HwBaseArpVlanCarPhyIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 14, 1, 1, 2),
    _HwBaseArpVlanCarPhyIfName_Type()
)
hwBaseArpVlanCarPhyIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBaseArpVlanCarPhyIfName.setStatus("current")


class _HwBaseArpVlanCarVlanId_Type(Integer32):
    """Custom type hwBaseArpVlanCarVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwBaseArpVlanCarVlanId_Type.__name__ = "Integer32"
_HwBaseArpVlanCarVlanId_Object = MibTableColumn
hwBaseArpVlanCarVlanId = _HwBaseArpVlanCarVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 14, 1, 1, 3),
    _HwBaseArpVlanCarVlanId_Type()
)
hwBaseArpVlanCarVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBaseArpVlanCarVlanId.setStatus("current")
_HwTtlExpiredLoop_ObjectIdentity = ObjectIdentity
hwTtlExpiredLoop = _HwTtlExpiredLoop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 15)
)
_HwTtlExpiredLoopTable_Object = MibTable
hwTtlExpiredLoopTable = _HwTtlExpiredLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 15, 1)
)
if mibBuilder.loadTexts:
    hwTtlExpiredLoopTable.setStatus("current")
_HwTtlExpiredLoopEntry_Object = MibTableRow
hwTtlExpiredLoopEntry = _HwTtlExpiredLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 15, 1, 1)
)
hwTtlExpiredLoopEntry.setIndexNames(
    (0, "HUAWEI-SECURITY-MIB", "hwTtlExpiredLoopChassisId"),
    (0, "HUAWEI-SECURITY-MIB", "hwTtlExpiredLoopSlotId"),
)
if mibBuilder.loadTexts:
    hwTtlExpiredLoopEntry.setStatus("current")
_HwTtlExpiredLoopChassisId_Type = Unsigned32
_HwTtlExpiredLoopChassisId_Object = MibTableColumn
hwTtlExpiredLoopChassisId = _HwTtlExpiredLoopChassisId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 15, 1, 1, 1),
    _HwTtlExpiredLoopChassisId_Type()
)
hwTtlExpiredLoopChassisId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwTtlExpiredLoopChassisId.setStatus("current")
_HwTtlExpiredLoopSlotId_Type = Unsigned32
_HwTtlExpiredLoopSlotId_Object = MibTableColumn
hwTtlExpiredLoopSlotId = _HwTtlExpiredLoopSlotId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 15, 1, 1, 2),
    _HwTtlExpiredLoopSlotId_Type()
)
hwTtlExpiredLoopSlotId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwTtlExpiredLoopSlotId.setStatus("current")
_HwTtlExpiredLoopLastRateLow_Type = Unsigned32
_HwTtlExpiredLoopLastRateLow_Object = MibTableColumn
hwTtlExpiredLoopLastRateLow = _HwTtlExpiredLoopLastRateLow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 15, 1, 1, 3),
    _HwTtlExpiredLoopLastRateLow_Type()
)
hwTtlExpiredLoopLastRateLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTtlExpiredLoopLastRateLow.setStatus("current")
_HwTtlExpiredLoopLastRateHigh_Type = Unsigned32
_HwTtlExpiredLoopLastRateHigh_Object = MibTableColumn
hwTtlExpiredLoopLastRateHigh = _HwTtlExpiredLoopLastRateHigh_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 15, 1, 1, 4),
    _HwTtlExpiredLoopLastRateHigh_Type()
)
hwTtlExpiredLoopLastRateHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTtlExpiredLoopLastRateHigh.setStatus("current")
_HwTtlExpiredLoopCurrentRateLow_Type = Unsigned32
_HwTtlExpiredLoopCurrentRateLow_Object = MibTableColumn
hwTtlExpiredLoopCurrentRateLow = _HwTtlExpiredLoopCurrentRateLow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 15, 1, 1, 5),
    _HwTtlExpiredLoopCurrentRateLow_Type()
)
hwTtlExpiredLoopCurrentRateLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTtlExpiredLoopCurrentRateLow.setStatus("current")
_HwTtlExpiredLoopCurrentRateHigh_Type = Unsigned32
_HwTtlExpiredLoopCurrentRateHigh_Object = MibTableColumn
hwTtlExpiredLoopCurrentRateHigh = _HwTtlExpiredLoopCurrentRateHigh_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 15, 1, 1, 6),
    _HwTtlExpiredLoopCurrentRateHigh_Type()
)
hwTtlExpiredLoopCurrentRateHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTtlExpiredLoopCurrentRateHigh.setStatus("current")
_HwTtlExpiredLoopRateInterval_Type = Unsigned32
_HwTtlExpiredLoopRateInterval_Object = MibTableColumn
hwTtlExpiredLoopRateInterval = _HwTtlExpiredLoopRateInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 15, 1, 1, 7),
    _HwTtlExpiredLoopRateInterval_Type()
)
hwTtlExpiredLoopRateInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTtlExpiredLoopRateInterval.setStatus("current")
_HwTtlExpiredLoopRateThreshold_Type = Unsigned32
_HwTtlExpiredLoopRateThreshold_Object = MibTableColumn
hwTtlExpiredLoopRateThreshold = _HwTtlExpiredLoopRateThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 15, 1, 1, 8),
    _HwTtlExpiredLoopRateThreshold_Type()
)
hwTtlExpiredLoopRateThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTtlExpiredLoopRateThreshold.setStatus("current")
_HwAntiAttack_ObjectIdentity = ObjectIdentity
hwAntiAttack = _HwAntiAttack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 16)
)
_HwAntiAttackTable_Object = MibTable
hwAntiAttackTable = _HwAntiAttackTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 16, 1)
)
if mibBuilder.loadTexts:
    hwAntiAttackTable.setStatus("current")
_HwAntiAttackEntry_Object = MibTableRow
hwAntiAttackEntry = _HwAntiAttackEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 16, 1, 1)
)
hwAntiAttackEntry.setIndexNames(
    (0, "HUAWEI-SECURITY-MIB", "hwAntiAttackType"),
)
if mibBuilder.loadTexts:
    hwAntiAttackEntry.setStatus("current")


class _HwAntiAttackType_Type(Integer32):
    """Custom type hwAntiAttackType based on Integer32"""
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
        *(("abnormal", 1),
          ("fragment", 2),
          ("icmpFlood", 5),
          ("tcpSyn", 3),
          ("udpFlood", 4))
    )


_HwAntiAttackType_Type.__name__ = "Integer32"
_HwAntiAttackType_Object = MibTableColumn
hwAntiAttackType = _HwAntiAttackType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 16, 1, 1, 1),
    _HwAntiAttackType_Type()
)
hwAntiAttackType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAntiAttackType.setStatus("current")
_HwAntiAttackRateThreshold_Type = Integer32
_HwAntiAttackRateThreshold_Object = MibTableColumn
hwAntiAttackRateThreshold = _HwAntiAttackRateThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 16, 1, 1, 2),
    _HwAntiAttackRateThreshold_Type()
)
hwAntiAttackRateThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAntiAttackRateThreshold.setStatus("current")
_HwAntiAttackCurrentRate_Type = Integer32
_HwAntiAttackCurrentRate_Object = MibTableColumn
hwAntiAttackCurrentRate = _HwAntiAttackCurrentRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 16, 1, 1, 3),
    _HwAntiAttackCurrentRate_Type()
)
hwAntiAttackCurrentRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAntiAttackCurrentRate.setStatus("current")
_HwMeSecurityMIBObjects_ObjectIdentity = ObjectIdentity
hwMeSecurityMIBObjects = _HwMeSecurityMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 2)
)
_HwSecurityTrapObject_ObjectIdentity = ObjectIdentity
hwSecurityTrapObject = _HwSecurityTrapObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 2, 1)
)
_HwStrackTrapObject_ObjectIdentity = ObjectIdentity
hwStrackTrapObject = _HwStrackTrapObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 2, 1, 1)
)
_HwStrackTotalPacket_Type = Integer32
_HwStrackTotalPacket_Object = MibScalar
hwStrackTotalPacket = _HwStrackTotalPacket_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 2, 1, 1, 1),
    _HwStrackTotalPacket_Type()
)
hwStrackTotalPacket.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwStrackTotalPacket.setStatus("current")
_HwStrackEndTime_Type = DateAndTime
_HwStrackEndTime_Object = MibScalar
hwStrackEndTime = _HwStrackEndTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 2, 1, 1, 2),
    _HwStrackEndTime_Type()
)
hwStrackEndTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwStrackEndTime.setStatus("current")
_HwStrackSourceMac_Type = OctetString
_HwStrackSourceMac_Object = MibScalar
hwStrackSourceMac = _HwStrackSourceMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 2, 1, 1, 3),
    _HwStrackSourceMac_Type()
)
hwStrackSourceMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwStrackSourceMac.setStatus("current")
_HwStrackPacketPVlan_Type = Integer32
_HwStrackPacketPVlan_Object = MibScalar
hwStrackPacketPVlan = _HwStrackPacketPVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 2, 1, 1, 4),
    _HwStrackPacketPVlan_Type()
)
hwStrackPacketPVlan.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwStrackPacketPVlan.setStatus("current")
_HwStrackPacketCVlan_Type = Integer32
_HwStrackPacketCVlan_Object = MibScalar
hwStrackPacketCVlan = _HwStrackPacketCVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 2, 1, 1, 5),
    _HwStrackPacketCVlan_Type()
)
hwStrackPacketCVlan.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwStrackPacketCVlan.setStatus("current")
_HwStrackPacketIfName_Type = OctetString
_HwStrackPacketIfName_Object = MibScalar
hwStrackPacketIfName = _HwStrackPacketIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 2, 1, 1, 6),
    _HwStrackPacketIfName_Type()
)
hwStrackPacketIfName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwStrackPacketIfName.setStatus("current")
_HwStrackSourceIp_Type = OctetString
_HwStrackSourceIp_Object = MibScalar
hwStrackSourceIp = _HwStrackSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 2, 1, 1, 7),
    _HwStrackSourceIp_Type()
)
hwStrackSourceIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwStrackSourceIp.setStatus("current")
_HwArpsTrapObject_ObjectIdentity = ObjectIdentity
hwArpsTrapObject = _HwArpsTrapObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 2, 1, 2)
)
_HwArpsSourceInterface_Type = OctetString
_HwArpsSourceInterface_Object = MibScalar
hwArpsSourceInterface = _HwArpsSourceInterface_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 2, 1, 2, 1),
    _HwArpsSourceInterface_Type()
)
hwArpsSourceInterface.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwArpsSourceInterface.setStatus("current")
_HwArpsSourceIp_Type = OctetString
_HwArpsSourceIp_Object = MibScalar
hwArpsSourceIp = _HwArpsSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 2, 1, 2, 2),
    _HwArpsSourceIp_Type()
)
hwArpsSourceIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwArpsSourceIp.setStatus("current")
_HwArpsSourceMac_Type = OctetString
_HwArpsSourceMac_Object = MibScalar
hwArpsSourceMac = _HwArpsSourceMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 2, 1, 2, 3),
    _HwArpsSourceMac_Type()
)
hwArpsSourceMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwArpsSourceMac.setStatus("current")
_HwArpsPVlan_Type = Integer32
_HwArpsPVlan_Object = MibScalar
hwArpsPVlan = _HwArpsPVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 2, 1, 2, 4),
    _HwArpsPVlan_Type()
)
hwArpsPVlan.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwArpsPVlan.setStatus("current")
_HwArpsCVlan_Type = Integer32
_HwArpsCVlan_Object = MibScalar
hwArpsCVlan = _HwArpsCVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 2, 1, 2, 5),
    _HwArpsCVlan_Type()
)
hwArpsCVlan.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwArpsCVlan.setStatus("current")
_HwArpsPacketDropNum_Type = Integer32
_HwArpsPacketDropNum_Object = MibScalar
hwArpsPacketDropNum = _HwArpsPacketDropNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 2, 1, 2, 6),
    _HwArpsPacketDropNum_Type()
)
hwArpsPacketDropNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwArpsPacketDropNum.setStatus("current")
_HwArpsAlarmThreshold_Type = Integer32
_HwArpsAlarmThreshold_Object = MibScalar
hwArpsAlarmThreshold = _HwArpsAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 2, 1, 2, 7),
    _HwArpsAlarmThreshold_Type()
)
hwArpsAlarmThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwArpsAlarmThreshold.setStatus("current")
_HwArpsBlockTime_Type = Integer32
_HwArpsBlockTime_Object = MibScalar
hwArpsBlockTime = _HwArpsBlockTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 2, 1, 2, 8),
    _HwArpsBlockTime_Type()
)
hwArpsBlockTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwArpsBlockTime.setStatus("current")
_HwIpsgTrapObject_ObjectIdentity = ObjectIdentity
hwIpsgTrapObject = _HwIpsgTrapObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 2, 1, 3)
)
_HwIpsgPacketDropNum_Type = Integer32
_HwIpsgPacketDropNum_Object = MibScalar
hwIpsgPacketDropNum = _HwIpsgPacketDropNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 2, 1, 3, 1),
    _HwIpsgPacketDropNum_Type()
)
hwIpsgPacketDropNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIpsgPacketDropNum.setStatus("current")
_HwIpsgAlarmThreshold_Type = Integer32
_HwIpsgAlarmThreshold_Object = MibScalar
hwIpsgAlarmThreshold = _HwIpsgAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 2, 1, 3, 2),
    _HwIpsgAlarmThreshold_Type()
)
hwIpsgAlarmThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIpsgAlarmThreshold.setStatus("current")
_HwIpsgSourceInterface_Type = OctetString
_HwIpsgSourceInterface_Object = MibScalar
hwIpsgSourceInterface = _HwIpsgSourceInterface_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 2, 1, 3, 3),
    _HwIpsgSourceInterface_Type()
)
hwIpsgSourceInterface.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIpsgSourceInterface.setStatus("current")
_HwIcmpTrapObject_ObjectIdentity = ObjectIdentity
hwIcmpTrapObject = _HwIcmpTrapObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 2, 1, 4)
)
_HwIcmpPacketDropNum_Type = Integer32
_HwIcmpPacketDropNum_Object = MibScalar
hwIcmpPacketDropNum = _HwIcmpPacketDropNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 2, 1, 4, 1),
    _HwIcmpPacketDropNum_Type()
)
hwIcmpPacketDropNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIcmpPacketDropNum.setStatus("current")
_HwIcmpAlarmThreshold_Type = Integer32
_HwIcmpAlarmThreshold_Object = MibScalar
hwIcmpAlarmThreshold = _HwIcmpAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 2, 1, 4, 2),
    _HwIcmpAlarmThreshold_Type()
)
hwIcmpAlarmThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIcmpAlarmThreshold.setStatus("current")
_HwIcmpSourceInterface_Type = OctetString
_HwIcmpSourceInterface_Object = MibScalar
hwIcmpSourceInterface = _HwIcmpSourceInterface_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 2, 1, 4, 3),
    _HwIcmpSourceInterface_Type()
)
hwIcmpSourceInterface.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIcmpSourceInterface.setStatus("current")
_HwDapTrapObject_ObjectIdentity = ObjectIdentity
hwDapTrapObject = _HwDapTrapObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 2, 1, 5)
)
_HwDapPortChange_Type = Integer32
_HwDapPortChange_Object = MibScalar
hwDapPortChange = _HwDapPortChange_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 2, 1, 5, 1),
    _HwDapPortChange_Type()
)
hwDapPortChange.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwDapPortChange.setStatus("current")
_HwCfgApTrapObject_ObjectIdentity = ObjectIdentity
hwCfgApTrapObject = _HwCfgApTrapObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 2, 1, 6)
)


class _HwCfgApUserName_Type(OctetString):
    """Custom type hwCfgApUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HwCfgApUserName_Type.__name__ = "OctetString"
_HwCfgApUserName_Object = MibScalar
hwCfgApUserName = _HwCfgApUserName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 2, 1, 6, 1),
    _HwCfgApUserName_Type()
)
hwCfgApUserName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwCfgApUserName.setStatus("current")


class _HwCfgApIPAddress_Type(OctetString):
    """Custom type hwCfgApIPAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HwCfgApIPAddress_Type.__name__ = "OctetString"
_HwCfgApIPAddress_Object = MibScalar
hwCfgApIPAddress = _HwCfgApIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 2, 1, 6, 2),
    _HwCfgApIPAddress_Type()
)
hwCfgApIPAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwCfgApIPAddress.setStatus("current")
_HwCfgApApID_Type = Integer32
_HwCfgApApID_Object = MibScalar
hwCfgApApID = _HwCfgApApID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 2, 1, 6, 3),
    _HwCfgApApID_Type()
)
hwCfgApApID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwCfgApApID.setStatus("current")


class _HwCfgApOperation_Type(OctetString):
    """Custom type hwCfgApOperation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HwCfgApOperation_Type.__name__ = "OctetString"
_HwCfgApOperation_Object = MibScalar
hwCfgApOperation = _HwCfgApOperation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 2, 1, 6, 4),
    _HwCfgApOperation_Type()
)
hwCfgApOperation.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwCfgApOperation.setStatus("current")


class _HwCfgApReason_Type(OctetString):
    """Custom type hwCfgApReason based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HwCfgApReason_Type.__name__ = "OctetString"
_HwCfgApReason_Object = MibScalar
hwCfgApReason = _HwCfgApReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 2, 1, 6, 5),
    _HwCfgApReason_Type()
)
hwCfgApReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwCfgApReason.setStatus("current")
_HwSecurityTraps_ObjectIdentity = ObjectIdentity
hwSecurityTraps = _HwSecurityTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 2, 2)
)
_HwStrackTrap_ObjectIdentity = ObjectIdentity
hwStrackTrap = _HwStrackTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 2, 2, 1)
)
_HwArpsTrap_ObjectIdentity = ObjectIdentity
hwArpsTrap = _HwArpsTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 2, 2, 2)
)
_HwIpsgTrap_ObjectIdentity = ObjectIdentity
hwIpsgTrap = _HwIpsgTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 2, 2, 3)
)
_HwIcmpTrap_ObjectIdentity = ObjectIdentity
hwIcmpTrap = _HwIcmpTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 2, 2, 4)
)
_HwDapTrap_ObjectIdentity = ObjectIdentity
hwDapTrap = _HwDapTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 2, 2, 5)
)
_HwCfgApTrap_ObjectIdentity = ObjectIdentity
hwCfgApTrap = _HwCfgApTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 2, 2, 6)
)
_HwTrafficSuppression_ObjectIdentity = ObjectIdentity
hwTrafficSuppression = _HwTrafficSuppression_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 2, 3)
)
_HwTrafficSuppressionTable_Object = MibTable
hwTrafficSuppressionTable = _HwTrafficSuppressionTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 2, 3, 1)
)
if mibBuilder.loadTexts:
    hwTrafficSuppressionTable.setStatus("current")
_HwTrafficSuppressionEntry_Object = MibTableRow
hwTrafficSuppressionEntry = _HwTrafficSuppressionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 2, 3, 1, 1)
)
hwTrafficSuppressionEntry.setIndexNames(
    (0, "HUAWEI-SECURITY-MIB", "hwTrafficSuppressionIfIndex"),
)
if mibBuilder.loadTexts:
    hwTrafficSuppressionEntry.setStatus("current")
_HwTrafficSuppressionIfIndex_Type = Integer32
_HwTrafficSuppressionIfIndex_Object = MibTableColumn
hwTrafficSuppressionIfIndex = _HwTrafficSuppressionIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 2, 3, 1, 1, 1),
    _HwTrafficSuppressionIfIndex_Type()
)
hwTrafficSuppressionIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwTrafficSuppressionIfIndex.setStatus("current")


class _HwTrafficSuppressionBcastRatio_Type(Integer32):
    """Custom type hwTrafficSuppressionBcastRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwTrafficSuppressionBcastRatio_Type.__name__ = "Integer32"
_HwTrafficSuppressionBcastRatio_Object = MibTableColumn
hwTrafficSuppressionBcastRatio = _HwTrafficSuppressionBcastRatio_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 2, 3, 1, 1, 2),
    _HwTrafficSuppressionBcastRatio_Type()
)
hwTrafficSuppressionBcastRatio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwTrafficSuppressionBcastRatio.setStatus("current")
_HwSecurityConformance_ObjectIdentity = ObjectIdentity
hwSecurityConformance = _HwSecurityConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 11)
)
_HwSecurityCompliances_ObjectIdentity = ObjectIdentity
hwSecurityCompliances = _HwSecurityCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 11, 1)
)
_HwBaseSecurityGroups_ObjectIdentity = ObjectIdentity
hwBaseSecurityGroups = _HwBaseSecurityGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 11, 2)
)

# Managed Objects groups

hwLocalUrpfObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 11, 2, 2)
)
hwLocalUrpfObjectGroup.setObjects(
      *(("HUAWEI-SECURITY-MIB", "hwLocalUrpfCurrentRateLow"),
        ("HUAWEI-SECURITY-MIB", "hwLocalUrpfCurrentRateHigh"),
        ("HUAWEI-SECURITY-MIB", "hwLocalUrpfNotifyEnabledStatus"),
        ("HUAWEI-SECURITY-MIB", "hwLocalUrpfRateThreshold"),
        ("HUAWEI-SECURITY-MIB", "hwLocalUrpfRateInterval"),
        ("HUAWEI-SECURITY-MIB", "hwLocalUrpfChassisId"),
        ("HUAWEI-SECURITY-MIB", "hwLocalUrpfSlotId"))
)
if mibBuilder.loadTexts:
    hwLocalUrpfObjectGroup.setStatus("current")

hwTcpIpDefendObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 11, 2, 3)
)
hwTcpIpDefendObjectGroup.setObjects(
      *(("HUAWEI-SECURITY-MIB", "hwTcpIpDefendCurrentRateLow"),
        ("HUAWEI-SECURITY-MIB", "hwTcpIpDefendCurrentRateHigh"),
        ("HUAWEI-SECURITY-MIB", "hwTcpIpDefendNotifyEnabledStatus"),
        ("HUAWEI-SECURITY-MIB", "hwTcpIpDefendRateThreshold"),
        ("HUAWEI-SECURITY-MIB", "hwTcpIpDefendRateInterval"),
        ("HUAWEI-SECURITY-MIB", "hwTcpIpDefendChassisId"),
        ("HUAWEI-SECURITY-MIB", "hwTcpIpDefendSlotId"),
        ("HUAWEI-SECURITY-MIB", "hwTcpIpDefendType"),
        ("HUAWEI-SECURITY-MIB", "hwTcpIpDefendProtocolDescirption"))
)
if mibBuilder.loadTexts:
    hwTcpIpDefendObjectGroup.setStatus("current")

hwMaDefendObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 11, 2, 4)
)
hwMaDefendObjectGroup.setObjects(
      *(("HUAWEI-SECURITY-MIB", "hwMaDefendCurrentRateLow"),
        ("HUAWEI-SECURITY-MIB", "hwMaDefendCurrentRateHigh"),
        ("HUAWEI-SECURITY-MIB", "hwMaDefendNotifyEnabledStatus"),
        ("HUAWEI-SECURITY-MIB", "hwMaDefendRateThreshold"),
        ("HUAWEI-SECURITY-MIB", "hwMaDefendRateInterval"),
        ("HUAWEI-SECURITY-MIB", "hwMaDefendChassisId"),
        ("HUAWEI-SECURITY-MIB", "hwMaDefendSlotId"),
        ("HUAWEI-SECURITY-MIB", "hwMaDefendProtocol"))
)
if mibBuilder.loadTexts:
    hwMaDefendObjectGroup.setStatus("current")

hwApplicationApperceiveObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 11, 2, 5)
)
hwApplicationApperceiveObjectGroup.setObjects(
      *(("HUAWEI-SECURITY-MIB", "hwAppliApperCurrentRateLow"),
        ("HUAWEI-SECURITY-MIB", "hwAppliApperCurrentRateHigh"),
        ("HUAWEI-SECURITY-MIB", "hwAppliApperNotifyEnabledStatus"),
        ("HUAWEI-SECURITY-MIB", "hwAppliApperRateThreshold"),
        ("HUAWEI-SECURITY-MIB", "hwAppliApperRateInterval"),
        ("HUAWEI-SECURITY-MIB", "hwAppliApperChassisId"),
        ("HUAWEI-SECURITY-MIB", "hwAppliApperSlotId"),
        ("HUAWEI-SECURITY-MIB", "hwAppliApperProtocol"),
        ("HUAWEI-SECURITY-MIB", "hwAppliApperProtocolDescirption"))
)
if mibBuilder.loadTexts:
    hwApplicationApperceiveObjectGroup.setStatus("current")

hwMeSecurityObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 11, 2, 7)
)
hwMeSecurityObjectGroup.setObjects(
      *(("HUAWEI-SECURITY-MIB", "hwStrackTotalPacket"),
        ("HUAWEI-SECURITY-MIB", "hwStrackEndTime"),
        ("HUAWEI-SECURITY-MIB", "hwStrackSourceMac"),
        ("HUAWEI-SECURITY-MIB", "hwStrackPacketPVlan"),
        ("HUAWEI-SECURITY-MIB", "hwStrackPacketCVlan"),
        ("HUAWEI-SECURITY-MIB", "hwStrackPacketIfName"),
        ("HUAWEI-SECURITY-MIB", "hwStrackSourceIp"),
        ("HUAWEI-SECURITY-MIB", "hwArpsSourceInterface"),
        ("HUAWEI-SECURITY-MIB", "hwArpsSourceIp"),
        ("HUAWEI-SECURITY-MIB", "hwArpsSourceMac"),
        ("HUAWEI-SECURITY-MIB", "hwArpsPVlan"),
        ("HUAWEI-SECURITY-MIB", "hwArpsCVlan"),
        ("HUAWEI-SECURITY-MIB", "hwArpsPacketDropNum"),
        ("HUAWEI-SECURITY-MIB", "hwArpsAlarmThreshold"),
        ("HUAWEI-SECURITY-MIB", "hwArpsBlockTime"),
        ("HUAWEI-SECURITY-MIB", "hwIpsgPacketDropNum"),
        ("HUAWEI-SECURITY-MIB", "hwIpsgAlarmThreshold"),
        ("HUAWEI-SECURITY-MIB", "hwIpsgSourceInterface"),
        ("HUAWEI-SECURITY-MIB", "hwIcmpPacketDropNum"),
        ("HUAWEI-SECURITY-MIB", "hwIcmpAlarmThreshold"),
        ("HUAWEI-SECURITY-MIB", "hwIcmpSourceInterface"),
        ("HUAWEI-SECURITY-MIB", "hwDapPortChange"),
        ("HUAWEI-SECURITY-MIB", "hwCfgApUserName"),
        ("HUAWEI-SECURITY-MIB", "hwCfgApIPAddress"),
        ("HUAWEI-SECURITY-MIB", "hwCfgApApID"),
        ("HUAWEI-SECURITY-MIB", "hwCfgApOperation"),
        ("HUAWEI-SECURITY-MIB", "hwCfgApReason"))
)
if mibBuilder.loadTexts:
    hwMeSecurityObjectGroup.setStatus("current")

hwDefdPortVlanObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 11, 2, 9)
)
hwDefdPortVlanObjectGroup.setObjects(
      *(("HUAWEI-SECURITY-MIB", "hwDefdPortVlanIfName"),
        ("HUAWEI-SECURITY-MIB", "hwDefdPortVlanId"),
        ("HUAWEI-SECURITY-MIB", "hwDefdPortVlanCheckProtocol"))
)
if mibBuilder.loadTexts:
    hwDefdPortVlanObjectGroup.setStatus("current")

hwSocAttackTrapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 11, 2, 11)
)
hwSocAttackTrapGroup.setObjects(
      *(("HUAWEI-SECURITY-MIB", "hwSocAttackSeqNo"),
        ("HUAWEI-SECURITY-MIB", "hwSocAttackPossib"),
        ("HUAWEI-SECURITY-MIB", "hwSocAttackReason"),
        ("HUAWEI-SECURITY-MIB", "hwSocAttackIfName"),
        ("HUAWEI-SECURITY-MIB", "hwSocAttackSubIfName"),
        ("HUAWEI-SECURITY-MIB", "hwSocAttackVlanIndex"),
        ("HUAWEI-SECURITY-MIB", "hwSocAttackUserQinQIndex"),
        ("HUAWEI-SECURITY-MIB", "hwSocAttackMacAddr"),
        ("HUAWEI-SECURITY-MIB", "hwSocAttackIPAddr"),
        ("HUAWEI-SECURITY-MIB", "hwSocAttackIPv6Addr"))
)
if mibBuilder.loadTexts:
    hwSocAttackTrapGroup.setStatus("current")

hwAntiAttackObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 11, 2, 12)
)
hwAntiAttackObjectGroup.setObjects(
      *(("HUAWEI-SECURITY-MIB", "hwAntiAttackType"),
        ("HUAWEI-SECURITY-MIB", "hwAntiAttackRateThreshold"),
        ("HUAWEI-SECURITY-MIB", "hwAntiAttackCurrentRate"))
)
if mibBuilder.loadTexts:
    hwAntiAttackObjectGroup.setStatus("current")


# Notification objects

hwBaseSecurityUrpfDiscardedRateRising = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 11, 1)
)
hwBaseSecurityUrpfDiscardedRateRising.setObjects(
      *(("HUAWEI-SECURITY-MIB", "hwLocalUrpfCurrentRateLow"),
        ("HUAWEI-SECURITY-MIB", "hwLocalUrpfCurrentRateHigh"),
        ("HUAWEI-SECURITY-MIB", "hwLocalUrpfRateThreshold"),
        ("HUAWEI-SECURITY-MIB", "hwLocalUrpfChassisId"),
        ("HUAWEI-SECURITY-MIB", "hwLocalUrpfSlotId"))
)
if mibBuilder.loadTexts:
    hwBaseSecurityUrpfDiscardedRateRising.setStatus(
        "current"
    )

hwBaseSecurityUrpfDiscardedRateResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 11, 2)
)
hwBaseSecurityUrpfDiscardedRateResume.setObjects(
      *(("HUAWEI-SECURITY-MIB", "hwLocalUrpfCurrentRateLow"),
        ("HUAWEI-SECURITY-MIB", "hwLocalUrpfCurrentRateHigh"),
        ("HUAWEI-SECURITY-MIB", "hwLocalUrpfRateThreshold"),
        ("HUAWEI-SECURITY-MIB", "hwLocalUrpfChassisId"),
        ("HUAWEI-SECURITY-MIB", "hwLocalUrpfSlotId"))
)
if mibBuilder.loadTexts:
    hwBaseSecurityUrpfDiscardedRateResume.setStatus(
        "current"
    )

hwBaseSecurityTcpIpAttackDiscardedRateRising = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 11, 3)
)
hwBaseSecurityTcpIpAttackDiscardedRateRising.setObjects(
      *(("HUAWEI-SECURITY-MIB", "hwTcpIpDefendCurrentRateLow"),
        ("HUAWEI-SECURITY-MIB", "hwTcpIpDefendCurrentRateHigh"),
        ("HUAWEI-SECURITY-MIB", "hwTcpIpDefendRateThreshold"),
        ("HUAWEI-SECURITY-MIB", "hwTcpIpDefendRateInterval"),
        ("HUAWEI-SECURITY-MIB", "hwTcpIpDefendChassisId"),
        ("HUAWEI-SECURITY-MIB", "hwTcpIpDefendSlotId"),
        ("HUAWEI-SECURITY-MIB", "hwTcpIpDefendType"),
        ("HUAWEI-SECURITY-MIB", "hwTcpIpDefendProtocolDescirption"))
)
if mibBuilder.loadTexts:
    hwBaseSecurityTcpIpAttackDiscardedRateRising.setStatus(
        "current"
    )

hwBaseSecurityTcpIpAttackDiscardedRateResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 11, 4)
)
hwBaseSecurityTcpIpAttackDiscardedRateResume.setObjects(
      *(("HUAWEI-SECURITY-MIB", "hwTcpIpDefendCurrentRateLow"),
        ("HUAWEI-SECURITY-MIB", "hwTcpIpDefendCurrentRateHigh"),
        ("HUAWEI-SECURITY-MIB", "hwTcpIpDefendRateThreshold"),
        ("HUAWEI-SECURITY-MIB", "hwTcpIpDefendRateInterval"),
        ("HUAWEI-SECURITY-MIB", "hwTcpIpDefendChassisId"),
        ("HUAWEI-SECURITY-MIB", "hwTcpIpDefendSlotId"),
        ("HUAWEI-SECURITY-MIB", "hwTcpIpDefendType"),
        ("HUAWEI-SECURITY-MIB", "hwTcpIpDefendProtocolDescirption"))
)
if mibBuilder.loadTexts:
    hwBaseSecurityTcpIpAttackDiscardedRateResume.setStatus(
        "current"
    )

hwBaseSecurityMaDiscardedRateRising = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 11, 5)
)
hwBaseSecurityMaDiscardedRateRising.setObjects(
      *(("HUAWEI-SECURITY-MIB", "hwMaDefendCurrentRateLow"),
        ("HUAWEI-SECURITY-MIB", "hwMaDefendCurrentRateHigh"),
        ("HUAWEI-SECURITY-MIB", "hwMaDefendRateThreshold"),
        ("HUAWEI-SECURITY-MIB", "hwMaDefendRateInterval"),
        ("HUAWEI-SECURITY-MIB", "hwMaDefendChassisId"),
        ("HUAWEI-SECURITY-MIB", "hwMaDefendSlotId"),
        ("HUAWEI-SECURITY-MIB", "hwMaDefendProtocol"))
)
if mibBuilder.loadTexts:
    hwBaseSecurityMaDiscardedRateRising.setStatus(
        "current"
    )

hwBaseSecurityMaDiscardedRateResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 11, 6)
)
hwBaseSecurityMaDiscardedRateResume.setObjects(
      *(("HUAWEI-SECURITY-MIB", "hwMaDefendCurrentRateLow"),
        ("HUAWEI-SECURITY-MIB", "hwMaDefendCurrentRateHigh"),
        ("HUAWEI-SECURITY-MIB", "hwMaDefendRateThreshold"),
        ("HUAWEI-SECURITY-MIB", "hwMaDefendRateInterval"),
        ("HUAWEI-SECURITY-MIB", "hwMaDefendChassisId"),
        ("HUAWEI-SECURITY-MIB", "hwMaDefendSlotId"),
        ("HUAWEI-SECURITY-MIB", "hwMaDefendProtocol"))
)
if mibBuilder.loadTexts:
    hwBaseSecurityMaDiscardedRateResume.setStatus(
        "current"
    )

hwBaseSecurityApplicationApperceiveDiscardedRateRising = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 11, 7)
)
hwBaseSecurityApplicationApperceiveDiscardedRateRising.setObjects(
      *(("HUAWEI-SECURITY-MIB", "hwAppliApperCurrentRateLow"),
        ("HUAWEI-SECURITY-MIB", "hwAppliApperCurrentRateHigh"),
        ("HUAWEI-SECURITY-MIB", "hwAppliApperRateThreshold"),
        ("HUAWEI-SECURITY-MIB", "hwAppliApperRateInterval"),
        ("HUAWEI-SECURITY-MIB", "hwAppliApperChassisId"),
        ("HUAWEI-SECURITY-MIB", "hwAppliApperSlotId"),
        ("HUAWEI-SECURITY-MIB", "hwAppliApperProtocol"),
        ("HUAWEI-SECURITY-MIB", "hwAppliApperProtocolDescirption"))
)
if mibBuilder.loadTexts:
    hwBaseSecurityApplicationApperceiveDiscardedRateRising.setStatus(
        "current"
    )

hwBaseSecurityApplicationApperceiveDiscardedRateResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 11, 8)
)
hwBaseSecurityApplicationApperceiveDiscardedRateResume.setObjects(
      *(("HUAWEI-SECURITY-MIB", "hwAppliApperCurrentRateLow"),
        ("HUAWEI-SECURITY-MIB", "hwAppliApperCurrentRateHigh"),
        ("HUAWEI-SECURITY-MIB", "hwAppliApperRateThreshold"),
        ("HUAWEI-SECURITY-MIB", "hwAppliApperRateInterval"),
        ("HUAWEI-SECURITY-MIB", "hwAppliApperChassisId"),
        ("HUAWEI-SECURITY-MIB", "hwAppliApperSlotId"),
        ("HUAWEI-SECURITY-MIB", "hwAppliApperProtocol"),
        ("HUAWEI-SECURITY-MIB", "hwAppliApperProtocolDescirption"))
)
if mibBuilder.loadTexts:
    hwBaseSecurityApplicationApperceiveDiscardedRateResume.setStatus(
        "current"
    )

hwBaseSecurityStormControlInterface = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 11, 9)
)
hwBaseSecurityStormControlInterface.setObjects(
      *(("HUAWEI-SECURITY-MIB", "hwBaseSecurityStormControlInterfaceChassisId"),
        ("HUAWEI-SECURITY-MIB", "hwBaseSecurityStormControlInterfaceSlotId"),
        ("HUAWEI-SECURITY-MIB", "hwBaseSecurityStormControlInterfaceName"),
        ("HUAWEI-SECURITY-MIB", "hwBaseSecurityStormControlInterfaceVlanID"))
)
if mibBuilder.loadTexts:
    hwBaseSecurityStormControlInterface.setStatus(
        "current"
    )

hwBaseSocAttackTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 11, 12)
)
hwBaseSocAttackTrap.setObjects(
      *(("HUAWEI-SECURITY-MIB", "hwSocAttackSeqNo"),
        ("HUAWEI-SECURITY-MIB", "hwSocAttackPossib"),
        ("HUAWEI-SECURITY-MIB", "hwSocAttackReason"),
        ("HUAWEI-SECURITY-MIB", "hwSocAttackIfName"),
        ("HUAWEI-SECURITY-MIB", "hwSocAttackSubIfName"),
        ("HUAWEI-SECURITY-MIB", "hwSocAttackVlanIndex"),
        ("HUAWEI-SECURITY-MIB", "hwSocAttackUserQinQIndex"),
        ("HUAWEI-SECURITY-MIB", "hwSocAttackMacAddr"),
        ("HUAWEI-SECURITY-MIB", "hwSocAttackIPAddr"),
        ("HUAWEI-SECURITY-MIB", "hwSocAttackIPv6Addr"))
)
if mibBuilder.loadTexts:
    hwBaseSocAttackTrap.setStatus(
        "current"
    )

hwBaseSocAttackResumeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 11, 13)
)
hwBaseSocAttackResumeTrap.setObjects(
      *(("HUAWEI-SECURITY-MIB", "hwSocAttackSeqNo"),
        ("HUAWEI-SECURITY-MIB", "hwSocAttackPossib"),
        ("HUAWEI-SECURITY-MIB", "hwSocAttackReason"),
        ("HUAWEI-SECURITY-MIB", "hwSocAttackIfName"),
        ("HUAWEI-SECURITY-MIB", "hwSocAttackSubIfName"),
        ("HUAWEI-SECURITY-MIB", "hwSocAttackVlanIndex"),
        ("HUAWEI-SECURITY-MIB", "hwSocAttackUserQinQIndex"),
        ("HUAWEI-SECURITY-MIB", "hwSocAttackMacAddr"),
        ("HUAWEI-SECURITY-MIB", "hwSocAttackIPAddr"),
        ("HUAWEI-SECURITY-MIB", "hwSocAttackIPv6Addr"))
)
if mibBuilder.loadTexts:
    hwBaseSocAttackResumeTrap.setStatus(
        "current"
    )

hwBaseSecurityStormControlInterfaceResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 11, 14)
)
hwBaseSecurityStormControlInterfaceResume.setObjects(
      *(("HUAWEI-SECURITY-MIB", "hwBaseSecurityStormControlInterfaceChassisId"),
        ("HUAWEI-SECURITY-MIB", "hwBaseSecurityStormControlInterfaceSlotId"),
        ("HUAWEI-SECURITY-MIB", "hwBaseSecurityStormControlInterfaceName"),
        ("HUAWEI-SECURITY-MIB", "hwBaseSecurityStormControlInterfaceVlanID"))
)
if mibBuilder.loadTexts:
    hwBaseSecurityStormControlInterfaceResume.setStatus(
        "current"
    )

hwBaseSecurityTtlExpiredLoop = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 11, 15)
)
hwBaseSecurityTtlExpiredLoop.setObjects(
      *(("HUAWEI-SECURITY-MIB", "hwTtlExpiredLoopChassisId"),
        ("HUAWEI-SECURITY-MIB", "hwTtlExpiredLoopSlotId"),
        ("HUAWEI-SECURITY-MIB", "hwTtlExpiredLoopLastRateLow"),
        ("HUAWEI-SECURITY-MIB", "hwTtlExpiredLoopLastRateHigh"),
        ("HUAWEI-SECURITY-MIB", "hwTtlExpiredLoopCurrentRateLow"),
        ("HUAWEI-SECURITY-MIB", "hwTtlExpiredLoopCurrentRateHigh"),
        ("HUAWEI-SECURITY-MIB", "hwTtlExpiredLoopRateInterval"),
        ("HUAWEI-SECURITY-MIB", "hwTtlExpiredLoopRateThreshold"))
)
if mibBuilder.loadTexts:
    hwBaseSecurityTtlExpiredLoop.setStatus(
        "current"
    )

hwBaseSecurityTtlExpiredLoopResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 11, 16)
)
hwBaseSecurityTtlExpiredLoopResume.setObjects(
      *(("HUAWEI-SECURITY-MIB", "hwTtlExpiredLoopChassisId"),
        ("HUAWEI-SECURITY-MIB", "hwTtlExpiredLoopSlotId"),
        ("HUAWEI-SECURITY-MIB", "hwTtlExpiredLoopLastRateLow"),
        ("HUAWEI-SECURITY-MIB", "hwTtlExpiredLoopLastRateHigh"),
        ("HUAWEI-SECURITY-MIB", "hwTtlExpiredLoopCurrentRateLow"),
        ("HUAWEI-SECURITY-MIB", "hwTtlExpiredLoopCurrentRateHigh"),
        ("HUAWEI-SECURITY-MIB", "hwTtlExpiredLoopRateInterval"),
        ("HUAWEI-SECURITY-MIB", "hwTtlExpiredLoopRateThreshold"))
)
if mibBuilder.loadTexts:
    hwBaseSecurityTtlExpiredLoopResume.setStatus(
        "current"
    )

hwBaseArpVlanCarTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 11, 17)
)
hwBaseArpVlanCarTrap.setObjects(
      *(("HUAWEI-SECURITY-MIB", "hwBaseArpVlanCarLogIfName"),
        ("HUAWEI-SECURITY-MIB", "hwBaseArpVlanCarPhyIfName"))
)
if mibBuilder.loadTexts:
    hwBaseArpVlanCarTrap.setStatus(
        "current"
    )

hwBaseArpVlanCarResumeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 11, 18)
)
hwBaseArpVlanCarResumeTrap.setObjects(
      *(("HUAWEI-SECURITY-MIB", "hwBaseArpVlanCarLogIfName"),
        ("HUAWEI-SECURITY-MIB", "hwBaseArpVlanCarPhyIfName"))
)
if mibBuilder.loadTexts:
    hwBaseArpVlanCarResumeTrap.setStatus(
        "current"
    )

hwBaseSecurityAntiAttackRateRising = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 11, 19)
)
hwBaseSecurityAntiAttackRateRising.setObjects(
      *(("HUAWEI-SECURITY-MIB", "hwAntiAttackType"),
        ("HUAWEI-SECURITY-MIB", "hwAntiAttackRateThreshold"),
        ("HUAWEI-SECURITY-MIB", "hwAntiAttackCurrentRate"))
)
if mibBuilder.loadTexts:
    hwBaseSecurityAntiAttackRateRising.setStatus(
        "current"
    )

hwBaseSecurityAntiAttackRateResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 1, 11, 20)
)
hwBaseSecurityAntiAttackRateResume.setObjects(
      *(("HUAWEI-SECURITY-MIB", "hwAntiAttackType"),
        ("HUAWEI-SECURITY-MIB", "hwAntiAttackRateThreshold"),
        ("HUAWEI-SECURITY-MIB", "hwAntiAttackCurrentRate"))
)
if mibBuilder.loadTexts:
    hwBaseSecurityAntiAttackRateResume.setStatus(
        "current"
    )

hwStrackUserInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 2, 2, 1, 1)
)
hwStrackUserInfo.setObjects(
      *(("HUAWEI-SECURITY-MIB", "hwStrackPacketIfName"),
        ("HUAWEI-SECURITY-MIB", "hwStrackSourceMac"),
        ("HUAWEI-SECURITY-MIB", "hwStrackPacketCVlan"),
        ("HUAWEI-SECURITY-MIB", "hwStrackPacketPVlan"),
        ("HUAWEI-SECURITY-MIB", "hwStrackEndTime"),
        ("HUAWEI-SECURITY-MIB", "hwStrackTotalPacket"))
)
if mibBuilder.loadTexts:
    hwStrackUserInfo.setStatus(
        "current"
    )

hwStrackIfVlanInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 2, 2, 1, 2)
)
hwStrackIfVlanInfo.setObjects(
      *(("HUAWEI-SECURITY-MIB", "hwStrackPacketIfName"),
        ("HUAWEI-SECURITY-MIB", "hwStrackPacketCVlan"),
        ("HUAWEI-SECURITY-MIB", "hwStrackPacketPVlan"),
        ("HUAWEI-SECURITY-MIB", "hwStrackEndTime"),
        ("HUAWEI-SECURITY-MIB", "hwStrackTotalPacket"))
)
if mibBuilder.loadTexts:
    hwStrackIfVlanInfo.setStatus(
        "current"
    )

hwStrackDenyPacket = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 2, 2, 1, 3)
)
hwStrackDenyPacket.setObjects(
      *(("HUAWEI-SECURITY-MIB", "hwStrackPacketIfName"),
        ("HUAWEI-SECURITY-MIB", "hwStrackSourceMac"),
        ("HUAWEI-SECURITY-MIB", "hwStrackSourceIp"),
        ("HUAWEI-SECURITY-MIB", "hwStrackPacketCVlan"),
        ("HUAWEI-SECURITY-MIB", "hwStrackPacketPVlan"))
)
if mibBuilder.loadTexts:
    hwStrackDenyPacket.setStatus(
        "current"
    )

hwStrackErrorDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 2, 2, 1, 4)
)
hwStrackErrorDown.setObjects(
    ("HUAWEI-SECURITY-MIB", "hwStrackPacketIfName")
)
if mibBuilder.loadTexts:
    hwStrackErrorDown.setStatus(
        "current"
    )

hwStrackIpInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 2, 2, 1, 5)
)
hwStrackIpInfo.setObjects(
      *(("HUAWEI-SECURITY-MIB", "hwStrackPacketIfName"),
        ("HUAWEI-SECURITY-MIB", "hwStrackSourceIp"),
        ("HUAWEI-SECURITY-MIB", "hwStrackPacketCVlan"),
        ("HUAWEI-SECURITY-MIB", "hwStrackPacketPVlan"),
        ("HUAWEI-SECURITY-MIB", "hwStrackEndTime"),
        ("HUAWEI-SECURITY-MIB", "hwStrackTotalPacket"))
)
if mibBuilder.loadTexts:
    hwStrackIpInfo.setStatus(
        "current"
    )

hwArpsGatewayConflict = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 2, 2, 2, 1)
)
hwArpsGatewayConflict.setObjects(
      *(("HUAWEI-SECURITY-MIB", "hwArpsSourceInterface"),
        ("HUAWEI-SECURITY-MIB", "hwArpsSourceIp"),
        ("HUAWEI-SECURITY-MIB", "hwArpsSourceMac"),
        ("HUAWEI-SECURITY-MIB", "hwArpsPVlan"),
        ("HUAWEI-SECURITY-MIB", "hwArpsCVlan"))
)
if mibBuilder.loadTexts:
    hwArpsGatewayConflict.setStatus(
        "current"
    )

hwArpsEntryCheck = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 2, 2, 2, 2)
)
hwArpsEntryCheck.setObjects(
      *(("HUAWEI-SECURITY-MIB", "hwArpsSourceInterface"),
        ("HUAWEI-SECURITY-MIB", "hwArpsSourceIp"),
        ("HUAWEI-SECURITY-MIB", "hwArpsSourceMac"),
        ("HUAWEI-SECURITY-MIB", "hwArpsPVlan"),
        ("HUAWEI-SECURITY-MIB", "hwArpsCVlan"))
)
if mibBuilder.loadTexts:
    hwArpsEntryCheck.setStatus(
        "current"
    )

hwArpsPacketCheck = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 2, 2, 2, 3)
)
hwArpsPacketCheck.setObjects(
      *(("HUAWEI-SECURITY-MIB", "hwArpsSourceInterface"),
        ("HUAWEI-SECURITY-MIB", "hwArpsSourceIp"),
        ("HUAWEI-SECURITY-MIB", "hwArpsSourceMac"),
        ("HUAWEI-SECURITY-MIB", "hwArpsPVlan"),
        ("HUAWEI-SECURITY-MIB", "hwArpsCVlan"))
)
if mibBuilder.loadTexts:
    hwArpsPacketCheck.setStatus(
        "current"
    )

hwArpsDaiDropALarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 2, 2, 2, 4)
)
hwArpsDaiDropALarm.setObjects(
      *(("HUAWEI-SECURITY-MIB", "hwArpsPacketDropNum"),
        ("HUAWEI-SECURITY-MIB", "hwArpsAlarmThreshold"),
        ("HUAWEI-SECURITY-MIB", "hwArpsSourceInterface"))
)
if mibBuilder.loadTexts:
    hwArpsDaiDropALarm.setStatus(
        "current"
    )

hwArpGlobleSpeedLimitALarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 2, 2, 2, 5)
)
hwArpGlobleSpeedLimitALarm.setObjects(
    ("HUAWEI-SECURITY-MIB", "hwArpsAlarmThreshold")
)
if mibBuilder.loadTexts:
    hwArpGlobleSpeedLimitALarm.setStatus(
        "current"
    )

hwArpIfSpeedLimitALarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 2, 2, 2, 6)
)
hwArpIfSpeedLimitALarm.setObjects(
      *(("HUAWEI-SECURITY-MIB", "hwArpsAlarmThreshold"),
        ("HUAWEI-SECURITY-MIB", "hwArpsSourceInterface"))
)
if mibBuilder.loadTexts:
    hwArpIfSpeedLimitALarm.setStatus(
        "current"
    )

hwArpVlanSpeedLimitALarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 2, 2, 2, 7)
)
hwArpVlanSpeedLimitALarm.setObjects(
      *(("HUAWEI-SECURITY-MIB", "hwArpsAlarmThreshold"),
        ("HUAWEI-SECURITY-MIB", "hwArpsPVlan"))
)
if mibBuilder.loadTexts:
    hwArpVlanSpeedLimitALarm.setStatus(
        "current"
    )

hwArpMissGlobleSpeedLimitALarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 2, 2, 2, 8)
)
hwArpMissGlobleSpeedLimitALarm.setObjects(
    ("HUAWEI-SECURITY-MIB", "hwArpsAlarmThreshold")
)
if mibBuilder.loadTexts:
    hwArpMissGlobleSpeedLimitALarm.setStatus(
        "current"
    )

hwArpMissIfSpeedLimitALarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 2, 2, 2, 9)
)
hwArpMissIfSpeedLimitALarm.setObjects(
      *(("HUAWEI-SECURITY-MIB", "hwArpsAlarmThreshold"),
        ("HUAWEI-SECURITY-MIB", "hwArpsSourceInterface"))
)
if mibBuilder.loadTexts:
    hwArpMissIfSpeedLimitALarm.setStatus(
        "current"
    )

hwArpMissVlanSpeedLimitALarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 2, 2, 2, 10)
)
hwArpMissVlanSpeedLimitALarm.setObjects(
      *(("HUAWEI-SECURITY-MIB", "hwArpsAlarmThreshold"),
        ("HUAWEI-SECURITY-MIB", "hwArpsPVlan"))
)
if mibBuilder.loadTexts:
    hwArpMissVlanSpeedLimitALarm.setStatus(
        "current"
    )

hwArpSourceIpSpeedLimitALarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 2, 2, 2, 11)
)
hwArpSourceIpSpeedLimitALarm.setObjects(
      *(("HUAWEI-SECURITY-MIB", "hwArpsSourceIp"),
        ("HUAWEI-SECURITY-MIB", "hwArpsAlarmThreshold"))
)
if mibBuilder.loadTexts:
    hwArpSourceIpSpeedLimitALarm.setStatus(
        "current"
    )

hwArpMissSourceIpSpeedLimitALarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 2, 2, 2, 12)
)
hwArpMissSourceIpSpeedLimitALarm.setObjects(
      *(("HUAWEI-SECURITY-MIB", "hwArpsSourceIp"),
        ("HUAWEI-SECURITY-MIB", "hwArpsAlarmThreshold"))
)
if mibBuilder.loadTexts:
    hwArpMissSourceIpSpeedLimitALarm.setStatus(
        "current"
    )

hwArpIfRateLimitBlockALarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 2, 2, 2, 13)
)
hwArpIfRateLimitBlockALarm.setObjects(
      *(("HUAWEI-SECURITY-MIB", "hwArpsSourceInterface"),
        ("HUAWEI-SECURITY-MIB", "hwArpsBlockTime"))
)
if mibBuilder.loadTexts:
    hwArpIfRateLimitBlockALarm.setStatus(
        "current"
    )

hwArpsLearnStrictCheck = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 2, 2, 2, 14)
)
hwArpsLearnStrictCheck.setObjects(
      *(("HUAWEI-SECURITY-MIB", "hwArpsSourceInterface"),
        ("HUAWEI-SECURITY-MIB", "hwArpsSourceIp"),
        ("HUAWEI-SECURITY-MIB", "hwArpsSourceMac"),
        ("HUAWEI-SECURITY-MIB", "hwArpsPVlan"))
)
if mibBuilder.loadTexts:
    hwArpsLearnStrictCheck.setStatus(
        "current"
    )

hwIpsgDropALarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 2, 2, 3, 1)
)
hwIpsgDropALarm.setObjects(
      *(("HUAWEI-SECURITY-MIB", "hwIpsgPacketDropNum"),
        ("HUAWEI-SECURITY-MIB", "hwIpsgAlarmThreshold"),
        ("HUAWEI-SECURITY-MIB", "hwIpsgSourceInterface"))
)
if mibBuilder.loadTexts:
    hwIpsgDropALarm.setStatus(
        "current"
    )

hwIcmpGlobleDropALarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 2, 2, 4, 1)
)
hwIcmpGlobleDropALarm.setObjects(
    ("HUAWEI-SECURITY-MIB", "hwIcmpAlarmThreshold")
)
if mibBuilder.loadTexts:
    hwIcmpGlobleDropALarm.setStatus(
        "current"
    )

hwIcmpIfDropALarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 2, 2, 4, 2)
)
hwIcmpIfDropALarm.setObjects(
      *(("HUAWEI-SECURITY-MIB", "hwIcmpAlarmThreshold"),
        ("HUAWEI-SECURITY-MIB", "hwIcmpSourceInterface"))
)
if mibBuilder.loadTexts:
    hwIcmpIfDropALarm.setStatus(
        "current"
    )

hwDapMibPortChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 2, 2, 5, 1)
)
hwDapMibPortChange.setObjects(
    ("HUAWEI-SECURITY-MIB", "hwDapPortChange")
)
if mibBuilder.loadTexts:
    hwDapMibPortChange.setStatus(
        "current"
    )

hwCfgApTrapFailAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 2, 2, 6, 1)
)
hwCfgApTrapFailAlarm.setObjects(
      *(("HUAWEI-SECURITY-MIB", "hwCfgApUserName"),
        ("HUAWEI-SECURITY-MIB", "hwCfgApIPAddress"),
        ("HUAWEI-SECURITY-MIB", "hwCfgApApID"),
        ("HUAWEI-SECURITY-MIB", "hwCfgApOperation"),
        ("HUAWEI-SECURITY-MIB", "hwCfgApReason"))
)
if mibBuilder.loadTexts:
    hwCfgApTrapFailAlarm.setStatus(
        "current"
    )


# Notifications groups

hwBaseSecurityNotificationsObjectGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 11, 2, 6)
)
hwBaseSecurityNotificationsObjectGroup.setObjects(
      *(("HUAWEI-SECURITY-MIB", "hwBaseSecurityUrpfDiscardedRateRising"),
        ("HUAWEI-SECURITY-MIB", "hwBaseSecurityUrpfDiscardedRateResume"),
        ("HUAWEI-SECURITY-MIB", "hwBaseSecurityTcpIpAttackDiscardedRateRising"),
        ("HUAWEI-SECURITY-MIB", "hwBaseSecurityTcpIpAttackDiscardedRateResume"),
        ("HUAWEI-SECURITY-MIB", "hwBaseSecurityMaDiscardedRateRising"),
        ("HUAWEI-SECURITY-MIB", "hwBaseSecurityMaDiscardedRateResume"),
        ("HUAWEI-SECURITY-MIB", "hwBaseSecurityApplicationApperceiveDiscardedRateRising"),
        ("HUAWEI-SECURITY-MIB", "hwBaseSecurityApplicationApperceiveDiscardedRateResume"),
        ("HUAWEI-SECURITY-MIB", "hwBaseSecurityStormControlInterface"),
        ("HUAWEI-SECURITY-MIB", "hwBaseSocAttackTrap"),
        ("HUAWEI-SECURITY-MIB", "hwBaseSocAttackResumeTrap"),
        ("HUAWEI-SECURITY-MIB", "hwBaseSecurityStormControlInterfaceResume"),
        ("HUAWEI-SECURITY-MIB", "hwBaseSecurityTtlExpiredLoop"),
        ("HUAWEI-SECURITY-MIB", "hwBaseSecurityTtlExpiredLoopResume"),
        ("HUAWEI-SECURITY-MIB", "hwBaseArpVlanCarTrap"),
        ("HUAWEI-SECURITY-MIB", "hwBaseArpVlanCarResumeTrap"),
        ("HUAWEI-SECURITY-MIB", "hwBaseSecurityAntiAttackRateRising"),
        ("HUAWEI-SECURITY-MIB", "hwBaseSecurityAntiAttackRateResume"))
)
if mibBuilder.loadTexts:
    hwBaseSecurityNotificationsObjectGroup.setStatus(
        "current"
    )

hwMeSecurityTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 11, 2, 8)
)
hwMeSecurityTrapGroup.setObjects(
      *(("HUAWEI-SECURITY-MIB", "hwStrackUserInfo"),
        ("HUAWEI-SECURITY-MIB", "hwStrackIfVlanInfo"),
        ("HUAWEI-SECURITY-MIB", "hwStrackDenyPacket"),
        ("HUAWEI-SECURITY-MIB", "hwStrackErrorDown"),
        ("HUAWEI-SECURITY-MIB", "hwStrackIpInfo"),
        ("HUAWEI-SECURITY-MIB", "hwArpsGatewayConflict"),
        ("HUAWEI-SECURITY-MIB", "hwArpsEntryCheck"),
        ("HUAWEI-SECURITY-MIB", "hwArpsPacketCheck"),
        ("HUAWEI-SECURITY-MIB", "hwArpsDaiDropALarm"),
        ("HUAWEI-SECURITY-MIB", "hwArpGlobleSpeedLimitALarm"),
        ("HUAWEI-SECURITY-MIB", "hwArpIfSpeedLimitALarm"),
        ("HUAWEI-SECURITY-MIB", "hwArpVlanSpeedLimitALarm"),
        ("HUAWEI-SECURITY-MIB", "hwArpMissGlobleSpeedLimitALarm"),
        ("HUAWEI-SECURITY-MIB", "hwArpMissIfSpeedLimitALarm"),
        ("HUAWEI-SECURITY-MIB", "hwArpMissVlanSpeedLimitALarm"),
        ("HUAWEI-SECURITY-MIB", "hwArpSourceIpSpeedLimitALarm"),
        ("HUAWEI-SECURITY-MIB", "hwArpMissSourceIpSpeedLimitALarm"),
        ("HUAWEI-SECURITY-MIB", "hwArpIfRateLimitBlockALarm"),
        ("HUAWEI-SECURITY-MIB", "hwArpsLearnStrictCheck"),
        ("HUAWEI-SECURITY-MIB", "hwIpsgDropALarm"),
        ("HUAWEI-SECURITY-MIB", "hwIcmpGlobleDropALarm"),
        ("HUAWEI-SECURITY-MIB", "hwIcmpIfDropALarm"),
        ("HUAWEI-SECURITY-MIB", "hwDapMibPortChange"),
        ("HUAWEI-SECURITY-MIB", "hwCfgApTrapFailAlarm"))
)
if mibBuilder.loadTexts:
    hwMeSecurityTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwSecurityCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 165, 11, 1, 1)
)
if mibBuilder.loadTexts:
    hwSecurityCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-SECURITY-MIB",
    **{"hwSecurityMIB": hwSecurityMIB,
       "hwBaseSecurityMIBObjects": hwBaseSecurityMIBObjects,
       "hwLocalUrpf": hwLocalUrpf,
       "hwLocalUrpfTable": hwLocalUrpfTable,
       "hwLocalUrpfEntry": hwLocalUrpfEntry,
       "hwLocalUrpfChassisId": hwLocalUrpfChassisId,
       "hwLocalUrpfSlotId": hwLocalUrpfSlotId,
       "hwLocalUrpfCurrentRateLow": hwLocalUrpfCurrentRateLow,
       "hwLocalUrpfCurrentRateHigh": hwLocalUrpfCurrentRateHigh,
       "hwLocalUrpfNotifyEnabledStatus": hwLocalUrpfNotifyEnabledStatus,
       "hwLocalUrpfRateThreshold": hwLocalUrpfRateThreshold,
       "hwLocalUrpfRateInterval": hwLocalUrpfRateInterval,
       "hwTcpIpDefend": hwTcpIpDefend,
       "hwTcpIpDefendTable": hwTcpIpDefendTable,
       "hwTcpIpDefendEntry": hwTcpIpDefendEntry,
       "hwTcpIpDefendChassisId": hwTcpIpDefendChassisId,
       "hwTcpIpDefendSlotId": hwTcpIpDefendSlotId,
       "hwTcpIpDefendType": hwTcpIpDefendType,
       "hwTcpIpDefendCurrentRateLow": hwTcpIpDefendCurrentRateLow,
       "hwTcpIpDefendCurrentRateHigh": hwTcpIpDefendCurrentRateHigh,
       "hwTcpIpDefendNotifyEnabledStatus": hwTcpIpDefendNotifyEnabledStatus,
       "hwTcpIpDefendRateThreshold": hwTcpIpDefendRateThreshold,
       "hwTcpIpDefendRateInterval": hwTcpIpDefendRateInterval,
       "hwTcpIpDefendProtocolDescirption": hwTcpIpDefendProtocolDescirption,
       "hwMaDefend": hwMaDefend,
       "hwMaDefendTable": hwMaDefendTable,
       "hwMaDefendEntry": hwMaDefendEntry,
       "hwMaDefendChassisId": hwMaDefendChassisId,
       "hwMaDefendSlotId": hwMaDefendSlotId,
       "hwMaDefendProtocol": hwMaDefendProtocol,
       "hwMaDefendCurrentRateLow": hwMaDefendCurrentRateLow,
       "hwMaDefendCurrentRateHigh": hwMaDefendCurrentRateHigh,
       "hwMaDefendNotifyEnabledStatus": hwMaDefendNotifyEnabledStatus,
       "hwMaDefendRateThreshold": hwMaDefendRateThreshold,
       "hwMaDefendRateInterval": hwMaDefendRateInterval,
       "hwApplicationApperceive": hwApplicationApperceive,
       "hwApplicationApperceiveTable": hwApplicationApperceiveTable,
       "hwApplicationApperceiveEntry": hwApplicationApperceiveEntry,
       "hwAppliApperChassisId": hwAppliApperChassisId,
       "hwAppliApperSlotId": hwAppliApperSlotId,
       "hwAppliApperProtocol": hwAppliApperProtocol,
       "hwAppliApperCurrentRateLow": hwAppliApperCurrentRateLow,
       "hwAppliApperCurrentRateHigh": hwAppliApperCurrentRateHigh,
       "hwAppliApperNotifyEnabledStatus": hwAppliApperNotifyEnabledStatus,
       "hwAppliApperRateThreshold": hwAppliApperRateThreshold,
       "hwAppliApperRateInterval": hwAppliApperRateInterval,
       "hwAppliApperProtocolDescirption": hwAppliApperProtocolDescirption,
       "hwDefdPortVlan": hwDefdPortVlan,
       "hwDefdPortVlanTable": hwDefdPortVlanTable,
       "hwDefdPortVlanEntry": hwDefdPortVlanEntry,
       "hwDefdPortVlanIfIndex": hwDefdPortVlanIfIndex,
       "hwDefdPortVlanIfName": hwDefdPortVlanIfName,
       "hwDefdPortVlanId": hwDefdPortVlanId,
       "hwDefdPortVlanCheckProtocol": hwDefdPortVlanCheckProtocol,
       "hwSocAttackTrapObject": hwSocAttackTrapObject,
       "hwSocAttackInfoTable": hwSocAttackInfoTable,
       "hwSocAttackInfoEntry": hwSocAttackInfoEntry,
       "hwSocAttackSeqNo": hwSocAttackSeqNo,
       "hwSocAttackPossib": hwSocAttackPossib,
       "hwSocAttackReason": hwSocAttackReason,
       "hwSocAttackIfName": hwSocAttackIfName,
       "hwSocAttackSubIfName": hwSocAttackSubIfName,
       "hwSocAttackVlanIndex": hwSocAttackVlanIndex,
       "hwSocAttackUserQinQIndex": hwSocAttackUserQinQIndex,
       "hwSocAttackMacAddr": hwSocAttackMacAddr,
       "hwSocAttackIPAddr": hwSocAttackIPAddr,
       "hwSocAttackIPv6Addr": hwSocAttackIPv6Addr,
       "hwBaseSecurityNotifications": hwBaseSecurityNotifications,
       "hwBaseSecurityUrpfDiscardedRateRising": hwBaseSecurityUrpfDiscardedRateRising,
       "hwBaseSecurityUrpfDiscardedRateResume": hwBaseSecurityUrpfDiscardedRateResume,
       "hwBaseSecurityTcpIpAttackDiscardedRateRising": hwBaseSecurityTcpIpAttackDiscardedRateRising,
       "hwBaseSecurityTcpIpAttackDiscardedRateResume": hwBaseSecurityTcpIpAttackDiscardedRateResume,
       "hwBaseSecurityMaDiscardedRateRising": hwBaseSecurityMaDiscardedRateRising,
       "hwBaseSecurityMaDiscardedRateResume": hwBaseSecurityMaDiscardedRateResume,
       "hwBaseSecurityApplicationApperceiveDiscardedRateRising": hwBaseSecurityApplicationApperceiveDiscardedRateRising,
       "hwBaseSecurityApplicationApperceiveDiscardedRateResume": hwBaseSecurityApplicationApperceiveDiscardedRateResume,
       "hwBaseSecurityStormControlInterface": hwBaseSecurityStormControlInterface,
       "hwBaseSocAttackTrap": hwBaseSocAttackTrap,
       "hwBaseSocAttackResumeTrap": hwBaseSocAttackResumeTrap,
       "hwBaseSecurityStormControlInterfaceResume": hwBaseSecurityStormControlInterfaceResume,
       "hwBaseSecurityTtlExpiredLoop": hwBaseSecurityTtlExpiredLoop,
       "hwBaseSecurityTtlExpiredLoopResume": hwBaseSecurityTtlExpiredLoopResume,
       "hwBaseArpVlanCarTrap": hwBaseArpVlanCarTrap,
       "hwBaseArpVlanCarResumeTrap": hwBaseArpVlanCarResumeTrap,
       "hwBaseSecurityAntiAttackRateRising": hwBaseSecurityAntiAttackRateRising,
       "hwBaseSecurityAntiAttackRateResume": hwBaseSecurityAntiAttackRateResume,
       "hwMacFilter": hwMacFilter,
       "hwMacFilterModeTable": hwMacFilterModeTable,
       "hwMacFilterModeEntry": hwMacFilterModeEntry,
       "hwMacFilterIfIndex": hwMacFilterIfIndex,
       "hwMacFilterInterface": hwMacFilterInterface,
       "hwMacFilterEnableMode": hwMacFilterEnableMode,
       "hwMacFilterMatchNum": hwMacFilterMatchNum,
       "hwMacFilterMacAddrTable": hwMacFilterMacAddrTable,
       "hwMacFilterMacAddrEntry": hwMacFilterMacAddrEntry,
       "hwMacFilterIfindex": hwMacFilterIfindex,
       "hwMacFilterInterfaceBuf": hwMacFilterInterfaceBuf,
       "hwMacFilterMacAddr": hwMacFilterMacAddr,
       "hwBaseSecurityStormControlInterfaceObjects": hwBaseSecurityStormControlInterfaceObjects,
       "hwBaseSecurityStormControlInterfaceTable": hwBaseSecurityStormControlInterfaceTable,
       "hwBaseSecurityStormControlInterfaceEntry": hwBaseSecurityStormControlInterfaceEntry,
       "hwBaseSecurityStormControlInterfaceChassisId": hwBaseSecurityStormControlInterfaceChassisId,
       "hwBaseSecurityStormControlInterfaceSlotId": hwBaseSecurityStormControlInterfaceSlotId,
       "hwBaseSecurityStormControlInterfaceName": hwBaseSecurityStormControlInterfaceName,
       "hwBaseSecurityStormControlInterfaceVlanID": hwBaseSecurityStormControlInterfaceVlanID,
       "hwBaseArpVlanCarTrapObject": hwBaseArpVlanCarTrapObject,
       "hwBaseArpVlanCarInfoTable": hwBaseArpVlanCarInfoTable,
       "hwBaseArpVlanCarInfoEntry": hwBaseArpVlanCarInfoEntry,
       "hwBaseArpVlanCarLogIfName": hwBaseArpVlanCarLogIfName,
       "hwBaseArpVlanCarPhyIfName": hwBaseArpVlanCarPhyIfName,
       "hwBaseArpVlanCarVlanId": hwBaseArpVlanCarVlanId,
       "hwTtlExpiredLoop": hwTtlExpiredLoop,
       "hwTtlExpiredLoopTable": hwTtlExpiredLoopTable,
       "hwTtlExpiredLoopEntry": hwTtlExpiredLoopEntry,
       "hwTtlExpiredLoopChassisId": hwTtlExpiredLoopChassisId,
       "hwTtlExpiredLoopSlotId": hwTtlExpiredLoopSlotId,
       "hwTtlExpiredLoopLastRateLow": hwTtlExpiredLoopLastRateLow,
       "hwTtlExpiredLoopLastRateHigh": hwTtlExpiredLoopLastRateHigh,
       "hwTtlExpiredLoopCurrentRateLow": hwTtlExpiredLoopCurrentRateLow,
       "hwTtlExpiredLoopCurrentRateHigh": hwTtlExpiredLoopCurrentRateHigh,
       "hwTtlExpiredLoopRateInterval": hwTtlExpiredLoopRateInterval,
       "hwTtlExpiredLoopRateThreshold": hwTtlExpiredLoopRateThreshold,
       "hwAntiAttack": hwAntiAttack,
       "hwAntiAttackTable": hwAntiAttackTable,
       "hwAntiAttackEntry": hwAntiAttackEntry,
       "hwAntiAttackType": hwAntiAttackType,
       "hwAntiAttackRateThreshold": hwAntiAttackRateThreshold,
       "hwAntiAttackCurrentRate": hwAntiAttackCurrentRate,
       "hwMeSecurityMIBObjects": hwMeSecurityMIBObjects,
       "hwSecurityTrapObject": hwSecurityTrapObject,
       "hwStrackTrapObject": hwStrackTrapObject,
       "hwStrackTotalPacket": hwStrackTotalPacket,
       "hwStrackEndTime": hwStrackEndTime,
       "hwStrackSourceMac": hwStrackSourceMac,
       "hwStrackPacketPVlan": hwStrackPacketPVlan,
       "hwStrackPacketCVlan": hwStrackPacketCVlan,
       "hwStrackPacketIfName": hwStrackPacketIfName,
       "hwStrackSourceIp": hwStrackSourceIp,
       "hwArpsTrapObject": hwArpsTrapObject,
       "hwArpsSourceInterface": hwArpsSourceInterface,
       "hwArpsSourceIp": hwArpsSourceIp,
       "hwArpsSourceMac": hwArpsSourceMac,
       "hwArpsPVlan": hwArpsPVlan,
       "hwArpsCVlan": hwArpsCVlan,
       "hwArpsPacketDropNum": hwArpsPacketDropNum,
       "hwArpsAlarmThreshold": hwArpsAlarmThreshold,
       "hwArpsBlockTime": hwArpsBlockTime,
       "hwIpsgTrapObject": hwIpsgTrapObject,
       "hwIpsgPacketDropNum": hwIpsgPacketDropNum,
       "hwIpsgAlarmThreshold": hwIpsgAlarmThreshold,
       "hwIpsgSourceInterface": hwIpsgSourceInterface,
       "hwIcmpTrapObject": hwIcmpTrapObject,
       "hwIcmpPacketDropNum": hwIcmpPacketDropNum,
       "hwIcmpAlarmThreshold": hwIcmpAlarmThreshold,
       "hwIcmpSourceInterface": hwIcmpSourceInterface,
       "hwDapTrapObject": hwDapTrapObject,
       "hwDapPortChange": hwDapPortChange,
       "hwCfgApTrapObject": hwCfgApTrapObject,
       "hwCfgApUserName": hwCfgApUserName,
       "hwCfgApIPAddress": hwCfgApIPAddress,
       "hwCfgApApID": hwCfgApApID,
       "hwCfgApOperation": hwCfgApOperation,
       "hwCfgApReason": hwCfgApReason,
       "hwSecurityTraps": hwSecurityTraps,
       "hwStrackTrap": hwStrackTrap,
       "hwStrackUserInfo": hwStrackUserInfo,
       "hwStrackIfVlanInfo": hwStrackIfVlanInfo,
       "hwStrackDenyPacket": hwStrackDenyPacket,
       "hwStrackErrorDown": hwStrackErrorDown,
       "hwStrackIpInfo": hwStrackIpInfo,
       "hwArpsTrap": hwArpsTrap,
       "hwArpsGatewayConflict": hwArpsGatewayConflict,
       "hwArpsEntryCheck": hwArpsEntryCheck,
       "hwArpsPacketCheck": hwArpsPacketCheck,
       "hwArpsDaiDropALarm": hwArpsDaiDropALarm,
       "hwArpGlobleSpeedLimitALarm": hwArpGlobleSpeedLimitALarm,
       "hwArpIfSpeedLimitALarm": hwArpIfSpeedLimitALarm,
       "hwArpVlanSpeedLimitALarm": hwArpVlanSpeedLimitALarm,
       "hwArpMissGlobleSpeedLimitALarm": hwArpMissGlobleSpeedLimitALarm,
       "hwArpMissIfSpeedLimitALarm": hwArpMissIfSpeedLimitALarm,
       "hwArpMissVlanSpeedLimitALarm": hwArpMissVlanSpeedLimitALarm,
       "hwArpSourceIpSpeedLimitALarm": hwArpSourceIpSpeedLimitALarm,
       "hwArpMissSourceIpSpeedLimitALarm": hwArpMissSourceIpSpeedLimitALarm,
       "hwArpIfRateLimitBlockALarm": hwArpIfRateLimitBlockALarm,
       "hwArpsLearnStrictCheck": hwArpsLearnStrictCheck,
       "hwIpsgTrap": hwIpsgTrap,
       "hwIpsgDropALarm": hwIpsgDropALarm,
       "hwIcmpTrap": hwIcmpTrap,
       "hwIcmpGlobleDropALarm": hwIcmpGlobleDropALarm,
       "hwIcmpIfDropALarm": hwIcmpIfDropALarm,
       "hwDapTrap": hwDapTrap,
       "hwDapMibPortChange": hwDapMibPortChange,
       "hwCfgApTrap": hwCfgApTrap,
       "hwCfgApTrapFailAlarm": hwCfgApTrapFailAlarm,
       "hwTrafficSuppression": hwTrafficSuppression,
       "hwTrafficSuppressionTable": hwTrafficSuppressionTable,
       "hwTrafficSuppressionEntry": hwTrafficSuppressionEntry,
       "hwTrafficSuppressionIfIndex": hwTrafficSuppressionIfIndex,
       "hwTrafficSuppressionBcastRatio": hwTrafficSuppressionBcastRatio,
       "hwSecurityConformance": hwSecurityConformance,
       "hwSecurityCompliances": hwSecurityCompliances,
       "hwSecurityCompliance": hwSecurityCompliance,
       "hwBaseSecurityGroups": hwBaseSecurityGroups,
       "hwLocalUrpfObjectGroup": hwLocalUrpfObjectGroup,
       "hwTcpIpDefendObjectGroup": hwTcpIpDefendObjectGroup,
       "hwMaDefendObjectGroup": hwMaDefendObjectGroup,
       "hwApplicationApperceiveObjectGroup": hwApplicationApperceiveObjectGroup,
       "hwBaseSecurityNotificationsObjectGroup": hwBaseSecurityNotificationsObjectGroup,
       "hwMeSecurityObjectGroup": hwMeSecurityObjectGroup,
       "hwMeSecurityTrapGroup": hwMeSecurityTrapGroup,
       "hwDefdPortVlanObjectGroup": hwDefdPortVlanObjectGroup,
       "hwSocAttackTrapGroup": hwSocAttackTrapGroup,
       "hwAntiAttackObjectGroup": hwAntiAttackObjectGroup}
)
