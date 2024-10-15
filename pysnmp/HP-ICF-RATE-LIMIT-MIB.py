# SNMP MIB module (HP-ICF-RATE-LIMIT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-RATE-LIMIT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:58:02 2024
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

(hpicfObjectModules,
 hpicfRateLimitTrapsPrefix) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpicfObjectModules",
    "hpicfRateLimitTrapsPrefix")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

hpicfRateLimitMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14)
)
hpicfRateLimitMIB.setRevisions(
        ("2017-10-13 00:00",
         "2016-08-03 00:00",
         "2015-09-04 00:00",
         "2014-11-17 10:00",
         "2014-11-18 00:00",
         "2013-07-11 00:00",
         "2013-03-12 15:10",
         "2012-10-05 19:30",
         "2012-03-12 12:30",
         "2010-09-27 11:30",
         "2010-07-14 16:10",
         "2007-12-04 12:30",
         "2007-08-29 11:20",
         "2007-07-27 19:20",
         "2007-06-01 11:46",
         "2007-05-30 16:10",
         "2006-07-07 18:33",
         "2005-04-20 11:30",
         "2004-08-22 10:30")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfRateLimitObjects_ObjectIdentity = ObjectIdentity
hpicfRateLimitObjects = _HpicfRateLimitObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1)
)
_HpicfICMPRateLimitObjects_ObjectIdentity = ObjectIdentity
hpicfICMPRateLimitObjects = _HpicfICMPRateLimitObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 1)
)
_HpICMPRateLimitConfig_ObjectIdentity = ObjectIdentity
hpICMPRateLimitConfig = _HpICMPRateLimitConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 1, 1)
)
_HpICMPRateLimitPortConfigTable_Object = MibTable
hpICMPRateLimitPortConfigTable = _HpICMPRateLimitPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hpICMPRateLimitPortConfigTable.setStatus("current")
_HpICMPRateLimitPortConfigEntry_Object = MibTableRow
hpICMPRateLimitPortConfigEntry = _HpICMPRateLimitPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 1, 1, 1, 1)
)
hpICMPRateLimitPortConfigEntry.setIndexNames(
    (0, "HP-ICF-RATE-LIMIT-MIB", "hpICMPRateLimitPortConfigIndex"),
)
if mibBuilder.loadTexts:
    hpICMPRateLimitPortConfigEntry.setStatus("current")
_HpICMPRateLimitPortConfigIndex_Type = InterfaceIndex
_HpICMPRateLimitPortConfigIndex_Object = MibTableColumn
hpICMPRateLimitPortConfigIndex = _HpICMPRateLimitPortConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 1, 1, 1, 1, 1),
    _HpICMPRateLimitPortConfigIndex_Type()
)
hpICMPRateLimitPortConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpICMPRateLimitPortConfigIndex.setStatus("current")


class _HpICMPRateLimitPortState_Type(Integer32):
    """Custom type hpICMPRateLimitPortState based on Integer32"""
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


_HpICMPRateLimitPortState_Type.__name__ = "Integer32"
_HpICMPRateLimitPortState_Object = MibTableColumn
hpICMPRateLimitPortState = _HpICMPRateLimitPortState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 1, 1, 1, 1, 2),
    _HpICMPRateLimitPortState_Type()
)
hpICMPRateLimitPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpICMPRateLimitPortState.setStatus("deprecated")


class _HpICMPRateLimitPortPrct_Type(Integer32):
    """Custom type hpICMPRateLimitPortPrct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpICMPRateLimitPortPrct_Type.__name__ = "Integer32"
_HpICMPRateLimitPortPrct_Object = MibTableColumn
hpICMPRateLimitPortPrct = _HpICMPRateLimitPortPrct_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 1, 1, 1, 1, 3),
    _HpICMPRateLimitPortPrct_Type()
)
hpICMPRateLimitPortPrct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpICMPRateLimitPortPrct.setStatus("current")


class _HpICMPRateLimitPortAlarmFlag_Type(Integer32):
    """Custom type hpICMPRateLimitPortAlarmFlag based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("set", 2))
    )


_HpICMPRateLimitPortAlarmFlag_Type.__name__ = "Integer32"
_HpICMPRateLimitPortAlarmFlag_Object = MibTableColumn
hpICMPRateLimitPortAlarmFlag = _HpICMPRateLimitPortAlarmFlag_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 1, 1, 1, 1, 4),
    _HpICMPRateLimitPortAlarmFlag_Type()
)
hpICMPRateLimitPortAlarmFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpICMPRateLimitPortAlarmFlag.setStatus("current")
_HpICMPRateLimitPortKbps_Type = Integer32
_HpICMPRateLimitPortKbps_Object = MibTableColumn
hpICMPRateLimitPortKbps = _HpICMPRateLimitPortKbps_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 1, 1, 1, 1, 5),
    _HpICMPRateLimitPortKbps_Type()
)
hpICMPRateLimitPortKbps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpICMPRateLimitPortKbps.setStatus("current")


class _HpICMPRateLimitPortControlMode_Type(Integer32):
    """Custom type hpICMPRateLimitPortControlMode based on Integer32"""
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
        *(("disabled", 1),
          ("portKbps", 3),
          ("portPrct", 2))
    )


_HpICMPRateLimitPortControlMode_Type.__name__ = "Integer32"
_HpICMPRateLimitPortControlMode_Object = MibTableColumn
hpICMPRateLimitPortControlMode = _HpICMPRateLimitPortControlMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 1, 1, 1, 1, 6),
    _HpICMPRateLimitPortControlMode_Type()
)
hpICMPRateLimitPortControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpICMPRateLimitPortControlMode.setStatus("current")


class _HpICMPRateLimitPortIpPacketType_Type(Integer32):
    """Custom type hpICMPRateLimitPortIpPacketType based on Integer32"""
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
        *(("ipv4AndIpv6Packets", 3),
          ("ipv4PacketsOnly", 1),
          ("ipv6PacketsOnly", 2))
    )


_HpICMPRateLimitPortIpPacketType_Type.__name__ = "Integer32"
_HpICMPRateLimitPortIpPacketType_Object = MibTableColumn
hpICMPRateLimitPortIpPacketType = _HpICMPRateLimitPortIpPacketType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 1, 1, 1, 1, 7),
    _HpICMPRateLimitPortIpPacketType_Type()
)
hpICMPRateLimitPortIpPacketType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpICMPRateLimitPortIpPacketType.setStatus("current")
_HpICMPRateLimitNotifyPortIndex_Type = InterfaceIndex
_HpICMPRateLimitNotifyPortIndex_Object = MibScalar
hpICMPRateLimitNotifyPortIndex = _HpICMPRateLimitNotifyPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 1, 2),
    _HpICMPRateLimitNotifyPortIndex_Type()
)
hpICMPRateLimitNotifyPortIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpICMPRateLimitNotifyPortIndex.setStatus("current")
_HpicfBWMinEgressObjects_ObjectIdentity = ObjectIdentity
hpicfBWMinEgressObjects = _HpicfBWMinEgressObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 2)
)
_HpBWMinEgressPortConfig_ObjectIdentity = ObjectIdentity
hpBWMinEgressPortConfig = _HpBWMinEgressPortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 2, 1)
)
_HpBWMinEgressPortNumQueues_Type = Integer32
_HpBWMinEgressPortNumQueues_Object = MibScalar
hpBWMinEgressPortNumQueues = _HpBWMinEgressPortNumQueues_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 2, 1, 1),
    _HpBWMinEgressPortNumQueues_Type()
)
hpBWMinEgressPortNumQueues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpBWMinEgressPortNumQueues.setStatus("current")
_HpBWMinEgressPortPrctTable_Object = MibTable
hpBWMinEgressPortPrctTable = _HpBWMinEgressPortPrctTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    hpBWMinEgressPortPrctTable.setStatus("current")
_HpBWMinEgressPortPrctEntry_Object = MibTableRow
hpBWMinEgressPortPrctEntry = _HpBWMinEgressPortPrctEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 2, 1, 2, 1)
)
hpBWMinEgressPortPrctEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HP-ICF-RATE-LIMIT-MIB", "hpBWMinEgressPortPrctQueue"),
)
if mibBuilder.loadTexts:
    hpBWMinEgressPortPrctEntry.setStatus("current")


class _HpBWMinEgressPortPrctQueue_Type(Integer32):
    """Custom type hpBWMinEgressPortPrctQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9000),
    )


_HpBWMinEgressPortPrctQueue_Type.__name__ = "Integer32"
_HpBWMinEgressPortPrctQueue_Object = MibTableColumn
hpBWMinEgressPortPrctQueue = _HpBWMinEgressPortPrctQueue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 2, 1, 2, 1, 1),
    _HpBWMinEgressPortPrctQueue_Type()
)
hpBWMinEgressPortPrctQueue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpBWMinEgressPortPrctQueue.setStatus("current")


class _HpBWMinEgressPortPrct_Type(Integer32):
    """Custom type hpBWMinEgressPortPrct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpBWMinEgressPortPrct_Type.__name__ = "Integer32"
_HpBWMinEgressPortPrct_Object = MibTableColumn
hpBWMinEgressPortPrct = _HpBWMinEgressPortPrct_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 2, 1, 2, 1, 2),
    _HpBWMinEgressPortPrct_Type()
)
hpBWMinEgressPortPrct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpBWMinEgressPortPrct.setStatus("current")
_HpicfBWMinIngressObjects_ObjectIdentity = ObjectIdentity
hpicfBWMinIngressObjects = _HpicfBWMinIngressObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 3)
)
_HpBWMinIngressPortConfig_ObjectIdentity = ObjectIdentity
hpBWMinIngressPortConfig = _HpBWMinIngressPortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 3, 1)
)
_HpBWMinIngressPortNumQueues_Type = Integer32
_HpBWMinIngressPortNumQueues_Object = MibScalar
hpBWMinIngressPortNumQueues = _HpBWMinIngressPortNumQueues_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 3, 1, 1),
    _HpBWMinIngressPortNumQueues_Type()
)
hpBWMinIngressPortNumQueues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpBWMinIngressPortNumQueues.setStatus("current")
_HpBWMinIngressPortPrctTable_Object = MibTable
hpBWMinIngressPortPrctTable = _HpBWMinIngressPortPrctTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    hpBWMinIngressPortPrctTable.setStatus("current")
_HpBWMinIngressPortPrctEntry_Object = MibTableRow
hpBWMinIngressPortPrctEntry = _HpBWMinIngressPortPrctEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 3, 1, 2, 1)
)
hpBWMinIngressPortPrctEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HP-ICF-RATE-LIMIT-MIB", "hpBWMinIngressPortPrctQueue"),
)
if mibBuilder.loadTexts:
    hpBWMinIngressPortPrctEntry.setStatus("current")


class _HpBWMinIngressPortPrctQueue_Type(Integer32):
    """Custom type hpBWMinIngressPortPrctQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9000),
    )


_HpBWMinIngressPortPrctQueue_Type.__name__ = "Integer32"
_HpBWMinIngressPortPrctQueue_Object = MibTableColumn
hpBWMinIngressPortPrctQueue = _HpBWMinIngressPortPrctQueue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 3, 1, 2, 1, 1),
    _HpBWMinIngressPortPrctQueue_Type()
)
hpBWMinIngressPortPrctQueue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpBWMinIngressPortPrctQueue.setStatus("current")


class _HpBWMinIngressPortPrct_Type(Integer32):
    """Custom type hpBWMinIngressPortPrct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpBWMinIngressPortPrct_Type.__name__ = "Integer32"
_HpBWMinIngressPortPrct_Object = MibTableColumn
hpBWMinIngressPortPrct = _HpBWMinIngressPortPrct_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 3, 1, 2, 1, 2),
    _HpBWMinIngressPortPrct_Type()
)
hpBWMinIngressPortPrct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpBWMinIngressPortPrct.setStatus("current")
_HpicfRateLimitPortObjects_ObjectIdentity = ObjectIdentity
hpicfRateLimitPortObjects = _HpicfRateLimitPortObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 4)
)
_HpRateLimitPortConfig_ObjectIdentity = ObjectIdentity
hpRateLimitPortConfig = _HpRateLimitPortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 4, 1)
)
_HpEgressRateLimitPortNumQueues_Type = Integer32
_HpEgressRateLimitPortNumQueues_Object = MibScalar
hpEgressRateLimitPortNumQueues = _HpEgressRateLimitPortNumQueues_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 4, 1, 1),
    _HpEgressRateLimitPortNumQueues_Type()
)
hpEgressRateLimitPortNumQueues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpEgressRateLimitPortNumQueues.setStatus("current")
_HpEgressRateLimitPortConfigTable_Object = MibTable
hpEgressRateLimitPortConfigTable = _HpEgressRateLimitPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 4, 1, 2)
)
if mibBuilder.loadTexts:
    hpEgressRateLimitPortConfigTable.setStatus("current")
_HpEgressRateLimitPortConfigEntry_Object = MibTableRow
hpEgressRateLimitPortConfigEntry = _HpEgressRateLimitPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 4, 1, 2, 1)
)
hpEgressRateLimitPortConfigEntry.setIndexNames(
    (0, "HP-ICF-RATE-LIMIT-MIB", "hpEgressRateLimitPortIndex"),
)
if mibBuilder.loadTexts:
    hpEgressRateLimitPortConfigEntry.setStatus("current")
_HpEgressRateLimitPortIndex_Type = InterfaceIndex
_HpEgressRateLimitPortIndex_Object = MibTableColumn
hpEgressRateLimitPortIndex = _HpEgressRateLimitPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 4, 1, 2, 1, 1),
    _HpEgressRateLimitPortIndex_Type()
)
hpEgressRateLimitPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpEgressRateLimitPortIndex.setStatus("current")


class _HpEgressRateLimitPortControlMode_Type(Integer32):
    """Custom type hpEgressRateLimitPortControlMode based on Integer32"""
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
        *(("disabled", 1),
          ("egressRateLimitPerPortOnly", 2),
          ("egressRateLimitPerPortOnlyBpsMode", 4),
          ("egressRateLimitPerPortOnlyKbpsMode", 6),
          ("egressRateLimitPerQueue", 3),
          ("egressRateLimitPerQueueBpsMode", 5))
    )


_HpEgressRateLimitPortControlMode_Type.__name__ = "Integer32"
_HpEgressRateLimitPortControlMode_Object = MibTableColumn
hpEgressRateLimitPortControlMode = _HpEgressRateLimitPortControlMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 4, 1, 2, 1, 2),
    _HpEgressRateLimitPortControlMode_Type()
)
hpEgressRateLimitPortControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpEgressRateLimitPortControlMode.setStatus("current")


class _HpEgressRateLimitPortSingleControlPrct_Type(Integer32):
    """Custom type hpEgressRateLimitPortSingleControlPrct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpEgressRateLimitPortSingleControlPrct_Type.__name__ = "Integer32"
_HpEgressRateLimitPortSingleControlPrct_Object = MibTableColumn
hpEgressRateLimitPortSingleControlPrct = _HpEgressRateLimitPortSingleControlPrct_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 4, 1, 2, 1, 3),
    _HpEgressRateLimitPortSingleControlPrct_Type()
)
hpEgressRateLimitPortSingleControlPrct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpEgressRateLimitPortSingleControlPrct.setStatus("current")


class _HpEgressRateLimitPortSingleControlBps_Type(Unsigned32):
    """Custom type hpEgressRateLimitPortSingleControlBps based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4200000000),
    )


_HpEgressRateLimitPortSingleControlBps_Type.__name__ = "Unsigned32"
_HpEgressRateLimitPortSingleControlBps_Object = MibTableColumn
hpEgressRateLimitPortSingleControlBps = _HpEgressRateLimitPortSingleControlBps_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 4, 1, 2, 1, 4),
    _HpEgressRateLimitPortSingleControlBps_Type()
)
hpEgressRateLimitPortSingleControlBps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpEgressRateLimitPortSingleControlBps.setStatus("deprecated")


class _HpEgressRateLimitPortSingleControlKbps_Type(Integer32):
    """Custom type hpEgressRateLimitPortSingleControlKbps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000000),
    )


_HpEgressRateLimitPortSingleControlKbps_Type.__name__ = "Integer32"
_HpEgressRateLimitPortSingleControlKbps_Object = MibTableColumn
hpEgressRateLimitPortSingleControlKbps = _HpEgressRateLimitPortSingleControlKbps_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 4, 1, 2, 1, 5),
    _HpEgressRateLimitPortSingleControlKbps_Type()
)
hpEgressRateLimitPortSingleControlKbps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpEgressRateLimitPortSingleControlKbps.setStatus("current")


class _HpEgressRateLimitPortQueueControlMode_Type(Integer32):
    """Custom type hpEgressRateLimitPortQueueControlMode based on Integer32"""
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
        *(("disabled", 1),
          ("egressRateLimitQueueKbpsMode", 3),
          ("egressRateLimitQueuePrctMode", 2))
    )


_HpEgressRateLimitPortQueueControlMode_Type.__name__ = "Integer32"
_HpEgressRateLimitPortQueueControlMode_Object = MibTableColumn
hpEgressRateLimitPortQueueControlMode = _HpEgressRateLimitPortQueueControlMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 4, 1, 2, 1, 6),
    _HpEgressRateLimitPortQueueControlMode_Type()
)
hpEgressRateLimitPortQueueControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpEgressRateLimitPortQueueControlMode.setStatus("current")
_HpEgressRateLimitPortPrctTable_Object = MibTable
hpEgressRateLimitPortPrctTable = _HpEgressRateLimitPortPrctTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 4, 1, 3)
)
if mibBuilder.loadTexts:
    hpEgressRateLimitPortPrctTable.setStatus("current")
_HpEgressRateLimitPortPrctEntry_Object = MibTableRow
hpEgressRateLimitPortPrctEntry = _HpEgressRateLimitPortPrctEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 4, 1, 3, 1)
)
hpEgressRateLimitPortPrctEntry.setIndexNames(
    (0, "HP-ICF-RATE-LIMIT-MIB", "hpEgressRateLimitPortIndex"),
    (0, "HP-ICF-RATE-LIMIT-MIB", "hpEgressRateLimitPortPrctQueue"),
)
if mibBuilder.loadTexts:
    hpEgressRateLimitPortPrctEntry.setStatus("current")


class _HpEgressRateLimitPortPrctQueue_Type(Integer32):
    """Custom type hpEgressRateLimitPortPrctQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9000),
    )


_HpEgressRateLimitPortPrctQueue_Type.__name__ = "Integer32"
_HpEgressRateLimitPortPrctQueue_Object = MibTableColumn
hpEgressRateLimitPortPrctQueue = _HpEgressRateLimitPortPrctQueue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 4, 1, 3, 1, 1),
    _HpEgressRateLimitPortPrctQueue_Type()
)
hpEgressRateLimitPortPrctQueue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpEgressRateLimitPortPrctQueue.setStatus("current")


class _HpEgressRateLimitPortPrct_Type(Integer32):
    """Custom type hpEgressRateLimitPortPrct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpEgressRateLimitPortPrct_Type.__name__ = "Integer32"
_HpEgressRateLimitPortPrct_Object = MibTableColumn
hpEgressRateLimitPortPrct = _HpEgressRateLimitPortPrct_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 4, 1, 3, 1, 2),
    _HpEgressRateLimitPortPrct_Type()
)
hpEgressRateLimitPortPrct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpEgressRateLimitPortPrct.setStatus("current")
_HpEgressRateLimitPortBpsTable_Object = MibTable
hpEgressRateLimitPortBpsTable = _HpEgressRateLimitPortBpsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 4, 1, 4)
)
if mibBuilder.loadTexts:
    hpEgressRateLimitPortBpsTable.setStatus("deprecated")
_HpEgressRateLimitPortBpsEntry_Object = MibTableRow
hpEgressRateLimitPortBpsEntry = _HpEgressRateLimitPortBpsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 4, 1, 4, 1)
)
hpEgressRateLimitPortBpsEntry.setIndexNames(
    (0, "HP-ICF-RATE-LIMIT-MIB", "hpEgressRateLimitPortIndex"),
    (0, "HP-ICF-RATE-LIMIT-MIB", "hpEgressRateLimitPortBpsQueue"),
)
if mibBuilder.loadTexts:
    hpEgressRateLimitPortBpsEntry.setStatus("deprecated")


class _HpEgressRateLimitPortBpsQueue_Type(Integer32):
    """Custom type hpEgressRateLimitPortBpsQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_HpEgressRateLimitPortBpsQueue_Type.__name__ = "Integer32"
_HpEgressRateLimitPortBpsQueue_Object = MibTableColumn
hpEgressRateLimitPortBpsQueue = _HpEgressRateLimitPortBpsQueue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 4, 1, 4, 1, 1),
    _HpEgressRateLimitPortBpsQueue_Type()
)
hpEgressRateLimitPortBpsQueue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpEgressRateLimitPortBpsQueue.setStatus("deprecated")


class _HpEgressRateLimitPortBps_Type(Unsigned32):
    """Custom type hpEgressRateLimitPortBps based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4200000000),
    )


_HpEgressRateLimitPortBps_Type.__name__ = "Unsigned32"
_HpEgressRateLimitPortBps_Object = MibTableColumn
hpEgressRateLimitPortBps = _HpEgressRateLimitPortBps_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 4, 1, 4, 1, 2),
    _HpEgressRateLimitPortBps_Type()
)
hpEgressRateLimitPortBps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpEgressRateLimitPortBps.setStatus("deprecated")
_HpEgressRateLimitPortQueueConfigTable_Object = MibTable
hpEgressRateLimitPortQueueConfigTable = _HpEgressRateLimitPortQueueConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 4, 1, 5)
)
if mibBuilder.loadTexts:
    hpEgressRateLimitPortQueueConfigTable.setStatus("current")
_HpEgressRateLimitPortQueueConfigEntry_Object = MibTableRow
hpEgressRateLimitPortQueueConfigEntry = _HpEgressRateLimitPortQueueConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 4, 1, 5, 1)
)
hpEgressRateLimitPortQueueConfigEntry.setIndexNames(
    (0, "HP-ICF-RATE-LIMIT-MIB", "hpEgressRateLimitPortIndex"),
    (0, "HP-ICF-RATE-LIMIT-MIB", "hpEgressRateLimitPortQueueIndex"),
)
if mibBuilder.loadTexts:
    hpEgressRateLimitPortQueueConfigEntry.setStatus("current")


class _HpEgressRateLimitPortQueueIndex_Type(Integer32):
    """Custom type hpEgressRateLimitPortQueueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9000),
    )


_HpEgressRateLimitPortQueueIndex_Type.__name__ = "Integer32"
_HpEgressRateLimitPortQueueIndex_Object = MibTableColumn
hpEgressRateLimitPortQueueIndex = _HpEgressRateLimitPortQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 4, 1, 5, 1, 1),
    _HpEgressRateLimitPortQueueIndex_Type()
)
hpEgressRateLimitPortQueueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpEgressRateLimitPortQueueIndex.setStatus("current")


class _HpEgressRateLimitPortQueueMax_Type(Integer32):
    """Custom type hpEgressRateLimitPortQueueMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000000),
    )


_HpEgressRateLimitPortQueueMax_Type.__name__ = "Integer32"
_HpEgressRateLimitPortQueueMax_Object = MibTableColumn
hpEgressRateLimitPortQueueMax = _HpEgressRateLimitPortQueueMax_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 4, 1, 5, 1, 2),
    _HpEgressRateLimitPortQueueMax_Type()
)
hpEgressRateLimitPortQueueMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpEgressRateLimitPortQueueMax.setStatus("current")
_HpicfIngressRateLimitPortObjects_ObjectIdentity = ObjectIdentity
hpicfIngressRateLimitPortObjects = _HpicfIngressRateLimitPortObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 5)
)
_HpRateLimitIngressPortConfig_ObjectIdentity = ObjectIdentity
hpRateLimitIngressPortConfig = _HpRateLimitIngressPortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 5, 1)
)
_HpIngressRateLimitPortNumQueues_Type = Integer32
_HpIngressRateLimitPortNumQueues_Object = MibScalar
hpIngressRateLimitPortNumQueues = _HpIngressRateLimitPortNumQueues_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 5, 1, 1),
    _HpIngressRateLimitPortNumQueues_Type()
)
hpIngressRateLimitPortNumQueues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpIngressRateLimitPortNumQueues.setStatus("current")
_HpIngressRateLimitPortConfigTable_Object = MibTable
hpIngressRateLimitPortConfigTable = _HpIngressRateLimitPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 5, 1, 2)
)
if mibBuilder.loadTexts:
    hpIngressRateLimitPortConfigTable.setStatus("current")
_HpIngressRateLimitPortConfigEntry_Object = MibTableRow
hpIngressRateLimitPortConfigEntry = _HpIngressRateLimitPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 5, 1, 2, 1)
)
hpIngressRateLimitPortConfigEntry.setIndexNames(
    (0, "HP-ICF-RATE-LIMIT-MIB", "hpIngressRateLimitPortIndex"),
)
if mibBuilder.loadTexts:
    hpIngressRateLimitPortConfigEntry.setStatus("current")
_HpIngressRateLimitPortIndex_Type = InterfaceIndex
_HpIngressRateLimitPortIndex_Object = MibTableColumn
hpIngressRateLimitPortIndex = _HpIngressRateLimitPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 5, 1, 2, 1, 1),
    _HpIngressRateLimitPortIndex_Type()
)
hpIngressRateLimitPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpIngressRateLimitPortIndex.setStatus("current")


class _HpIngressRateLimitPortControlMode_Type(Integer32):
    """Custom type hpIngressRateLimitPortControlMode based on Integer32"""
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
        *(("disabled", 1),
          ("ingressRateLimitPerPortOnly", 2),
          ("ingressRateLimitPerPortOnlyBpsMode", 4),
          ("ingressRateLimitPerPortOnlyKbpsMode", 6),
          ("ingressRateLimitPerQueue", 3),
          ("ingressRateLimitPerQueueBpsMode", 5))
    )


_HpIngressRateLimitPortControlMode_Type.__name__ = "Integer32"
_HpIngressRateLimitPortControlMode_Object = MibTableColumn
hpIngressRateLimitPortControlMode = _HpIngressRateLimitPortControlMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 5, 1, 2, 1, 2),
    _HpIngressRateLimitPortControlMode_Type()
)
hpIngressRateLimitPortControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpIngressRateLimitPortControlMode.setStatus("current")


class _HpIngressRateLimitPortSingleControlPrct_Type(Integer32):
    """Custom type hpIngressRateLimitPortSingleControlPrct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpIngressRateLimitPortSingleControlPrct_Type.__name__ = "Integer32"
_HpIngressRateLimitPortSingleControlPrct_Object = MibTableColumn
hpIngressRateLimitPortSingleControlPrct = _HpIngressRateLimitPortSingleControlPrct_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 5, 1, 2, 1, 3),
    _HpIngressRateLimitPortSingleControlPrct_Type()
)
hpIngressRateLimitPortSingleControlPrct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpIngressRateLimitPortSingleControlPrct.setStatus("current")


class _HpIngressRateLimitPortSingleControlBps_Type(Unsigned32):
    """Custom type hpIngressRateLimitPortSingleControlBps based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4200000000),
    )


_HpIngressRateLimitPortSingleControlBps_Type.__name__ = "Unsigned32"
_HpIngressRateLimitPortSingleControlBps_Object = MibTableColumn
hpIngressRateLimitPortSingleControlBps = _HpIngressRateLimitPortSingleControlBps_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 5, 1, 2, 1, 4),
    _HpIngressRateLimitPortSingleControlBps_Type()
)
hpIngressRateLimitPortSingleControlBps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpIngressRateLimitPortSingleControlBps.setStatus("deprecated")


class _HpIngressRateLimitPortSingleControlKbps_Type(Integer32):
    """Custom type hpIngressRateLimitPortSingleControlKbps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000000),
    )


_HpIngressRateLimitPortSingleControlKbps_Type.__name__ = "Integer32"
_HpIngressRateLimitPortSingleControlKbps_Object = MibTableColumn
hpIngressRateLimitPortSingleControlKbps = _HpIngressRateLimitPortSingleControlKbps_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 5, 1, 2, 1, 5),
    _HpIngressRateLimitPortSingleControlKbps_Type()
)
hpIngressRateLimitPortSingleControlKbps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpIngressRateLimitPortSingleControlKbps.setStatus("current")
_HpIngressRateLimitPortPrctTable_Object = MibTable
hpIngressRateLimitPortPrctTable = _HpIngressRateLimitPortPrctTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 5, 1, 3)
)
if mibBuilder.loadTexts:
    hpIngressRateLimitPortPrctTable.setStatus("current")
_HpIngressRateLimitPortPrctEntry_Object = MibTableRow
hpIngressRateLimitPortPrctEntry = _HpIngressRateLimitPortPrctEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 5, 1, 3, 1)
)
hpIngressRateLimitPortPrctEntry.setIndexNames(
    (0, "HP-ICF-RATE-LIMIT-MIB", "hpIngressRateLimitPortIndex"),
    (0, "HP-ICF-RATE-LIMIT-MIB", "hpIngressRateLimitPortPrctQueue"),
)
if mibBuilder.loadTexts:
    hpIngressRateLimitPortPrctEntry.setStatus("current")


class _HpIngressRateLimitPortPrctQueue_Type(Integer32):
    """Custom type hpIngressRateLimitPortPrctQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9000),
    )


_HpIngressRateLimitPortPrctQueue_Type.__name__ = "Integer32"
_HpIngressRateLimitPortPrctQueue_Object = MibTableColumn
hpIngressRateLimitPortPrctQueue = _HpIngressRateLimitPortPrctQueue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 5, 1, 3, 1, 1),
    _HpIngressRateLimitPortPrctQueue_Type()
)
hpIngressRateLimitPortPrctQueue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpIngressRateLimitPortPrctQueue.setStatus("current")


class _HpIngressRateLimitPortPrct_Type(Integer32):
    """Custom type hpIngressRateLimitPortPrct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpIngressRateLimitPortPrct_Type.__name__ = "Integer32"
_HpIngressRateLimitPortPrct_Object = MibTableColumn
hpIngressRateLimitPortPrct = _HpIngressRateLimitPortPrct_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 5, 1, 3, 1, 2),
    _HpIngressRateLimitPortPrct_Type()
)
hpIngressRateLimitPortPrct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpIngressRateLimitPortPrct.setStatus("current")
_HpIngressRateLimitPortBpsTable_Object = MibTable
hpIngressRateLimitPortBpsTable = _HpIngressRateLimitPortBpsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 5, 1, 4)
)
if mibBuilder.loadTexts:
    hpIngressRateLimitPortBpsTable.setStatus("deprecated")
_HpIngressRateLimitPortBpsEntry_Object = MibTableRow
hpIngressRateLimitPortBpsEntry = _HpIngressRateLimitPortBpsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 5, 1, 4, 1)
)
hpIngressRateLimitPortBpsEntry.setIndexNames(
    (0, "HP-ICF-RATE-LIMIT-MIB", "hpIngressRateLimitPortIndex"),
    (0, "HP-ICF-RATE-LIMIT-MIB", "hpIngressRateLimitPortBpsQueue"),
)
if mibBuilder.loadTexts:
    hpIngressRateLimitPortBpsEntry.setStatus("deprecated")


class _HpIngressRateLimitPortBpsQueue_Type(Integer32):
    """Custom type hpIngressRateLimitPortBpsQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_HpIngressRateLimitPortBpsQueue_Type.__name__ = "Integer32"
_HpIngressRateLimitPortBpsQueue_Object = MibTableColumn
hpIngressRateLimitPortBpsQueue = _HpIngressRateLimitPortBpsQueue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 5, 1, 4, 1, 1),
    _HpIngressRateLimitPortBpsQueue_Type()
)
hpIngressRateLimitPortBpsQueue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpIngressRateLimitPortBpsQueue.setStatus("deprecated")


class _HpIngressRateLimitPortBps_Type(Unsigned32):
    """Custom type hpIngressRateLimitPortBps based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4200000000),
    )


_HpIngressRateLimitPortBps_Type.__name__ = "Unsigned32"
_HpIngressRateLimitPortBps_Object = MibTableColumn
hpIngressRateLimitPortBps = _HpIngressRateLimitPortBps_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 5, 1, 4, 1, 2),
    _HpIngressRateLimitPortBps_Type()
)
hpIngressRateLimitPortBps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpIngressRateLimitPortBps.setStatus("deprecated")
_HpicfIngressBcastLimitPortObjects_ObjectIdentity = ObjectIdentity
hpicfIngressBcastLimitPortObjects = _HpicfIngressBcastLimitPortObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 6)
)
_HpBcastLimitIngressPortConfig_ObjectIdentity = ObjectIdentity
hpBcastLimitIngressPortConfig = _HpBcastLimitIngressPortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 6, 1)
)
_HpIngressBcastLimitPortConfigTable_Object = MibTable
hpIngressBcastLimitPortConfigTable = _HpIngressBcastLimitPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 6, 1, 1)
)
if mibBuilder.loadTexts:
    hpIngressBcastLimitPortConfigTable.setStatus("current")
_HpIngressBcastLimitPortConfigEntry_Object = MibTableRow
hpIngressBcastLimitPortConfigEntry = _HpIngressBcastLimitPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 6, 1, 1, 1)
)
hpIngressBcastLimitPortConfigEntry.setIndexNames(
    (0, "HP-ICF-RATE-LIMIT-MIB", "hpIngressBcastLimitPortIndex"),
)
if mibBuilder.loadTexts:
    hpIngressBcastLimitPortConfigEntry.setStatus("current")
_HpIngressBcastLimitPortIndex_Type = InterfaceIndex
_HpIngressBcastLimitPortIndex_Object = MibTableColumn
hpIngressBcastLimitPortIndex = _HpIngressBcastLimitPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 6, 1, 1, 1, 1),
    _HpIngressBcastLimitPortIndex_Type()
)
hpIngressBcastLimitPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpIngressBcastLimitPortIndex.setStatus("current")


class _HpIngressBcastLimitPortControlMode_Type(Integer32):
    """Custom type hpIngressBcastLimitPortControlMode based on Integer32"""
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
        *(("disabled", 1),
          ("ingressBcastLimitPerPortOnly", 2),
          ("ingressBcastLimitPerPortOnlyKbpsMode", 3))
    )


_HpIngressBcastLimitPortControlMode_Type.__name__ = "Integer32"
_HpIngressBcastLimitPortControlMode_Object = MibTableColumn
hpIngressBcastLimitPortControlMode = _HpIngressBcastLimitPortControlMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 6, 1, 1, 1, 2),
    _HpIngressBcastLimitPortControlMode_Type()
)
hpIngressBcastLimitPortControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpIngressBcastLimitPortControlMode.setStatus("current")


class _HpIngressBcastLimitPortSingleControlPrct_Type(Integer32):
    """Custom type hpIngressBcastLimitPortSingleControlPrct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpIngressBcastLimitPortSingleControlPrct_Type.__name__ = "Integer32"
_HpIngressBcastLimitPortSingleControlPrct_Object = MibTableColumn
hpIngressBcastLimitPortSingleControlPrct = _HpIngressBcastLimitPortSingleControlPrct_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 6, 1, 1, 1, 3),
    _HpIngressBcastLimitPortSingleControlPrct_Type()
)
hpIngressBcastLimitPortSingleControlPrct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpIngressBcastLimitPortSingleControlPrct.setStatus("current")


class _HpIngressBcastLimitPortSingleControlKbps_Type(Integer32):
    """Custom type hpIngressBcastLimitPortSingleControlKbps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000000),
    )


_HpIngressBcastLimitPortSingleControlKbps_Type.__name__ = "Integer32"
_HpIngressBcastLimitPortSingleControlKbps_Object = MibTableColumn
hpIngressBcastLimitPortSingleControlKbps = _HpIngressBcastLimitPortSingleControlKbps_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 6, 1, 1, 1, 4),
    _HpIngressBcastLimitPortSingleControlKbps_Type()
)
hpIngressBcastLimitPortSingleControlKbps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpIngressBcastLimitPortSingleControlKbps.setStatus("current")
_HpicfIngressMcastLimitPortObjects_ObjectIdentity = ObjectIdentity
hpicfIngressMcastLimitPortObjects = _HpicfIngressMcastLimitPortObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 7)
)
_HpMcastLimitIngressPortConfig_ObjectIdentity = ObjectIdentity
hpMcastLimitIngressPortConfig = _HpMcastLimitIngressPortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 7, 1)
)
_HpIngressMcastLimitPortConfigTable_Object = MibTable
hpIngressMcastLimitPortConfigTable = _HpIngressMcastLimitPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 7, 1, 1)
)
if mibBuilder.loadTexts:
    hpIngressMcastLimitPortConfigTable.setStatus("current")
_HpIngressMcastLimitPortConfigEntry_Object = MibTableRow
hpIngressMcastLimitPortConfigEntry = _HpIngressMcastLimitPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 7, 1, 1, 1)
)
hpIngressMcastLimitPortConfigEntry.setIndexNames(
    (0, "HP-ICF-RATE-LIMIT-MIB", "hpIngressMcastLimitPortIndex"),
)
if mibBuilder.loadTexts:
    hpIngressMcastLimitPortConfigEntry.setStatus("current")
_HpIngressMcastLimitPortIndex_Type = InterfaceIndex
_HpIngressMcastLimitPortIndex_Object = MibTableColumn
hpIngressMcastLimitPortIndex = _HpIngressMcastLimitPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 7, 1, 1, 1, 1),
    _HpIngressMcastLimitPortIndex_Type()
)
hpIngressMcastLimitPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpIngressMcastLimitPortIndex.setStatus("current")


class _HpIngressMcastLimitPortControlMode_Type(Integer32):
    """Custom type hpIngressMcastLimitPortControlMode based on Integer32"""
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
        *(("disabled", 1),
          ("ingressMcastLimitPerPortOnly", 2),
          ("ingressMcastLimitPerPortOnlyKbpsMode", 3))
    )


_HpIngressMcastLimitPortControlMode_Type.__name__ = "Integer32"
_HpIngressMcastLimitPortControlMode_Object = MibTableColumn
hpIngressMcastLimitPortControlMode = _HpIngressMcastLimitPortControlMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 7, 1, 1, 1, 2),
    _HpIngressMcastLimitPortControlMode_Type()
)
hpIngressMcastLimitPortControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpIngressMcastLimitPortControlMode.setStatus("current")


class _HpIngressMcastLimitPortSingleControlPrct_Type(Integer32):
    """Custom type hpIngressMcastLimitPortSingleControlPrct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpIngressMcastLimitPortSingleControlPrct_Type.__name__ = "Integer32"
_HpIngressMcastLimitPortSingleControlPrct_Object = MibTableColumn
hpIngressMcastLimitPortSingleControlPrct = _HpIngressMcastLimitPortSingleControlPrct_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 7, 1, 1, 1, 3),
    _HpIngressMcastLimitPortSingleControlPrct_Type()
)
hpIngressMcastLimitPortSingleControlPrct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpIngressMcastLimitPortSingleControlPrct.setStatus("current")


class _HpIngressMcastLimitPortSingleControlKbps_Type(Integer32):
    """Custom type hpIngressMcastLimitPortSingleControlKbps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000000),
    )


_HpIngressMcastLimitPortSingleControlKbps_Type.__name__ = "Integer32"
_HpIngressMcastLimitPortSingleControlKbps_Object = MibTableColumn
hpIngressMcastLimitPortSingleControlKbps = _HpIngressMcastLimitPortSingleControlKbps_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 7, 1, 1, 1, 4),
    _HpIngressMcastLimitPortSingleControlKbps_Type()
)
hpIngressMcastLimitPortSingleControlKbps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpIngressMcastLimitPortSingleControlKbps.setStatus("current")
_HpicfUnknownUnicastLimitPortObjects_ObjectIdentity = ObjectIdentity
hpicfUnknownUnicastLimitPortObjects = _HpicfUnknownUnicastLimitPortObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 8)
)
_HpUnknownUnicastLimitPortConfig_ObjectIdentity = ObjectIdentity
hpUnknownUnicastLimitPortConfig = _HpUnknownUnicastLimitPortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 8, 1)
)
_HpUnknownUnicastLimitConfigTable_Object = MibTable
hpUnknownUnicastLimitConfigTable = _HpUnknownUnicastLimitConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 8, 1, 1)
)
if mibBuilder.loadTexts:
    hpUnknownUnicastLimitConfigTable.setStatus("current")
_HpUnknownUnicastLimitConfigEntry_Object = MibTableRow
hpUnknownUnicastLimitConfigEntry = _HpUnknownUnicastLimitConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 8, 1, 1, 1)
)
hpUnknownUnicastLimitConfigEntry.setIndexNames(
    (0, "HP-ICF-RATE-LIMIT-MIB", "hpUnknownUnicastLimitPortIndex"),
)
if mibBuilder.loadTexts:
    hpUnknownUnicastLimitConfigEntry.setStatus("current")
_HpUnknownUnicastLimitPortIndex_Type = InterfaceIndex
_HpUnknownUnicastLimitPortIndex_Object = MibTableColumn
hpUnknownUnicastLimitPortIndex = _HpUnknownUnicastLimitPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 8, 1, 1, 1, 1),
    _HpUnknownUnicastLimitPortIndex_Type()
)
hpUnknownUnicastLimitPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpUnknownUnicastLimitPortIndex.setStatus("current")


class _HpUnknownUnicastLimitPortControlMode_Type(Integer32):
    """Custom type hpUnknownUnicastLimitPortControlMode based on Integer32"""
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
        *(("disabled", 1),
          ("unknownUnicastLimitPerPortOnly", 2),
          ("unknownUnicastLimitPerPortOnlyKbpsMode", 3))
    )


_HpUnknownUnicastLimitPortControlMode_Type.__name__ = "Integer32"
_HpUnknownUnicastLimitPortControlMode_Object = MibTableColumn
hpUnknownUnicastLimitPortControlMode = _HpUnknownUnicastLimitPortControlMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 8, 1, 1, 1, 2),
    _HpUnknownUnicastLimitPortControlMode_Type()
)
hpUnknownUnicastLimitPortControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpUnknownUnicastLimitPortControlMode.setStatus("current")


class _HpUnknownUnicastLimitPortSingleControlPrct_Type(Integer32):
    """Custom type hpUnknownUnicastLimitPortSingleControlPrct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpUnknownUnicastLimitPortSingleControlPrct_Type.__name__ = "Integer32"
_HpUnknownUnicastLimitPortSingleControlPrct_Object = MibTableColumn
hpUnknownUnicastLimitPortSingleControlPrct = _HpUnknownUnicastLimitPortSingleControlPrct_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 8, 1, 1, 1, 3),
    _HpUnknownUnicastLimitPortSingleControlPrct_Type()
)
hpUnknownUnicastLimitPortSingleControlPrct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpUnknownUnicastLimitPortSingleControlPrct.setStatus("current")


class _HpUnknownUnicastLimitPortSingleControlKbps_Type(Integer32):
    """Custom type hpUnknownUnicastLimitPortSingleControlKbps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000000),
    )


_HpUnknownUnicastLimitPortSingleControlKbps_Type.__name__ = "Integer32"
_HpUnknownUnicastLimitPortSingleControlKbps_Object = MibTableColumn
hpUnknownUnicastLimitPortSingleControlKbps = _HpUnknownUnicastLimitPortSingleControlKbps_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 8, 1, 1, 1, 4),
    _HpUnknownUnicastLimitPortSingleControlKbps_Type()
)
hpUnknownUnicastLimitPortSingleControlKbps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpUnknownUnicastLimitPortSingleControlKbps.setStatus("current")
_HpicfIngressRateLimitVlanObjects_ObjectIdentity = ObjectIdentity
hpicfIngressRateLimitVlanObjects = _HpicfIngressRateLimitVlanObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 9)
)
_HpicfIngressRateLimitVlanConfigTable_Object = MibTable
hpicfIngressRateLimitVlanConfigTable = _HpicfIngressRateLimitVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 9, 1)
)
if mibBuilder.loadTexts:
    hpicfIngressRateLimitVlanConfigTable.setStatus("current")
_HpicfIngressRateLimitVlanConfigEntry_Object = MibTableRow
hpicfIngressRateLimitVlanConfigEntry = _HpicfIngressRateLimitVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 9, 1, 1)
)
hpicfIngressRateLimitVlanConfigEntry.setIndexNames(
    (0, "HP-ICF-RATE-LIMIT-MIB", "hpicfIngressRateLimitVlanIndex"),
)
if mibBuilder.loadTexts:
    hpicfIngressRateLimitVlanConfigEntry.setStatus("current")
_HpicfIngressRateLimitVlanIndex_Type = InterfaceIndex
_HpicfIngressRateLimitVlanIndex_Object = MibTableColumn
hpicfIngressRateLimitVlanIndex = _HpicfIngressRateLimitVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 9, 1, 1, 1),
    _HpicfIngressRateLimitVlanIndex_Type()
)
hpicfIngressRateLimitVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfIngressRateLimitVlanIndex.setStatus("current")


class _HpicfIngressRateLimitVlanControlMode_Type(Integer32):
    """Custom type hpicfIngressRateLimitVlanControlMode based on Integer32"""
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
          ("ingressVlanKbps", 2))
    )


_HpicfIngressRateLimitVlanControlMode_Type.__name__ = "Integer32"
_HpicfIngressRateLimitVlanControlMode_Object = MibTableColumn
hpicfIngressRateLimitVlanControlMode = _HpicfIngressRateLimitVlanControlMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 9, 1, 1, 2),
    _HpicfIngressRateLimitVlanControlMode_Type()
)
hpicfIngressRateLimitVlanControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfIngressRateLimitVlanControlMode.setStatus("current")


class _HpicfIngressRateLimitVlanKbps_Type(Unsigned32):
    """Custom type hpicfIngressRateLimitVlanKbps based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 260000000),
    )


_HpicfIngressRateLimitVlanKbps_Type.__name__ = "Unsigned32"
_HpicfIngressRateLimitVlanKbps_Object = MibTableColumn
hpicfIngressRateLimitVlanKbps = _HpicfIngressRateLimitVlanKbps_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 1, 9, 1, 1, 3),
    _HpicfIngressRateLimitVlanKbps_Type()
)
hpicfIngressRateLimitVlanKbps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfIngressRateLimitVlanKbps.setStatus("current")
_HpicfRateLimitConformance_ObjectIdentity = ObjectIdentity
hpicfRateLimitConformance = _HpicfRateLimitConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 2)
)
_HpicfRateLimitGroups_ObjectIdentity = ObjectIdentity
hpicfRateLimitGroups = _HpicfRateLimitGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 2, 1)
)
_HpicfRateLimitCompliances_ObjectIdentity = ObjectIdentity
hpicfRateLimitCompliances = _HpicfRateLimitCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 2, 2)
)

# Managed Objects groups

hpICMPRateLimitPortConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 2, 1, 1)
)
hpICMPRateLimitPortConfigGroup.setObjects(
      *(("HP-ICF-RATE-LIMIT-MIB", "hpICMPRateLimitPortState"),
        ("HP-ICF-RATE-LIMIT-MIB", "hpICMPRateLimitPortPrct"),
        ("HP-ICF-RATE-LIMIT-MIB", "hpICMPRateLimitPortAlarmFlag"),
        ("HP-ICF-RATE-LIMIT-MIB", "hpICMPRateLimitNotifyPortIndex"))
)
if mibBuilder.loadTexts:
    hpICMPRateLimitPortConfigGroup.setStatus("deprecated")

hpBWMinIngressPortConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 2, 1, 3)
)
hpBWMinIngressPortConfigGroup.setObjects(
      *(("HP-ICF-RATE-LIMIT-MIB", "hpBWMinIngressPortNumQueues"),
        ("HP-ICF-RATE-LIMIT-MIB", "hpBWMinIngressPortPrct"))
)
if mibBuilder.loadTexts:
    hpBWMinIngressPortConfigGroup.setStatus("current")

hpBWMinEgressPortConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 2, 1, 4)
)
hpBWMinEgressPortConfigGroup.setObjects(
      *(("HP-ICF-RATE-LIMIT-MIB", "hpBWMinEgressPortNumQueues"),
        ("HP-ICF-RATE-LIMIT-MIB", "hpBWMinEgressPortPrct"))
)
if mibBuilder.loadTexts:
    hpBWMinEgressPortConfigGroup.setStatus("current")

hpEgressRateLimitPortConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 2, 1, 5)
)
hpEgressRateLimitPortConfigGroup.setObjects(
      *(("HP-ICF-RATE-LIMIT-MIB", "hpEgressRateLimitPortNumQueues"),
        ("HP-ICF-RATE-LIMIT-MIB", "hpEgressRateLimitPortControlMode"),
        ("HP-ICF-RATE-LIMIT-MIB", "hpEgressRateLimitPortSingleControlPrct"),
        ("HP-ICF-RATE-LIMIT-MIB", "hpEgressRateLimitPortSingleControlBps"),
        ("HP-ICF-RATE-LIMIT-MIB", "hpEgressRateLimitPortPrct"),
        ("HP-ICF-RATE-LIMIT-MIB", "hpEgressRateLimitPortBps"),
        ("HP-ICF-RATE-LIMIT-MIB", "hpEgressRateLimitPortSingleControlKbps"))
)
if mibBuilder.loadTexts:
    hpEgressRateLimitPortConfigGroup.setStatus("deprecated")

hpIngressRateLimitPortConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 2, 1, 6)
)
hpIngressRateLimitPortConfigGroup.setObjects(
      *(("HP-ICF-RATE-LIMIT-MIB", "hpIngressRateLimitPortNumQueues"),
        ("HP-ICF-RATE-LIMIT-MIB", "hpIngressRateLimitPortControlMode"),
        ("HP-ICF-RATE-LIMIT-MIB", "hpIngressRateLimitPortSingleControlPrct"),
        ("HP-ICF-RATE-LIMIT-MIB", "hpIngressRateLimitPortSingleControlBps"),
        ("HP-ICF-RATE-LIMIT-MIB", "hpIngressRateLimitPortPrct"),
        ("HP-ICF-RATE-LIMIT-MIB", "hpIngressRateLimitPortBps"),
        ("HP-ICF-RATE-LIMIT-MIB", "hpIngressRateLimitPortSingleControlKbps"))
)
if mibBuilder.loadTexts:
    hpIngressRateLimitPortConfigGroup.setStatus("deprecated")

hpICMPRateLimitPortConfigGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 2, 1, 7)
)
hpICMPRateLimitPortConfigGroup2.setObjects(
      *(("HP-ICF-RATE-LIMIT-MIB", "hpICMPRateLimitPortPrct"),
        ("HP-ICF-RATE-LIMIT-MIB", "hpICMPRateLimitPortAlarmFlag"),
        ("HP-ICF-RATE-LIMIT-MIB", "hpICMPRateLimitNotifyPortIndex"),
        ("HP-ICF-RATE-LIMIT-MIB", "hpICMPRateLimitPortKbps"),
        ("HP-ICF-RATE-LIMIT-MIB", "hpICMPRateLimitPortControlMode"))
)
if mibBuilder.loadTexts:
    hpICMPRateLimitPortConfigGroup2.setStatus("deprecated")

hpEgressRateLimitPortConfigGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 2, 1, 8)
)
hpEgressRateLimitPortConfigGroup2.setObjects(
      *(("HP-ICF-RATE-LIMIT-MIB", "hpEgressRateLimitPortNumQueues"),
        ("HP-ICF-RATE-LIMIT-MIB", "hpEgressRateLimitPortControlMode"),
        ("HP-ICF-RATE-LIMIT-MIB", "hpEgressRateLimitPortSingleControlPrct"),
        ("HP-ICF-RATE-LIMIT-MIB", "hpEgressRateLimitPortPrct"),
        ("HP-ICF-RATE-LIMIT-MIB", "hpEgressRateLimitPortSingleControlKbps"))
)
if mibBuilder.loadTexts:
    hpEgressRateLimitPortConfigGroup2.setStatus("deprecated")

hpIngressRateLimitPortConfigGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 2, 1, 9)
)
hpIngressRateLimitPortConfigGroup2.setObjects(
      *(("HP-ICF-RATE-LIMIT-MIB", "hpIngressRateLimitPortNumQueues"),
        ("HP-ICF-RATE-LIMIT-MIB", "hpIngressRateLimitPortControlMode"),
        ("HP-ICF-RATE-LIMIT-MIB", "hpIngressRateLimitPortSingleControlPrct"),
        ("HP-ICF-RATE-LIMIT-MIB", "hpIngressRateLimitPortPrct"),
        ("HP-ICF-RATE-LIMIT-MIB", "hpIngressRateLimitPortSingleControlKbps"))
)
if mibBuilder.loadTexts:
    hpIngressRateLimitPortConfigGroup2.setStatus("current")

hpBcastLimitIngressPortConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 2, 1, 10)
)
hpBcastLimitIngressPortConfigGroup.setObjects(
      *(("HP-ICF-RATE-LIMIT-MIB", "hpIngressBcastLimitPortControlMode"),
        ("HP-ICF-RATE-LIMIT-MIB", "hpIngressBcastLimitPortSingleControlPrct"))
)
if mibBuilder.loadTexts:
    hpBcastLimitIngressPortConfigGroup.setStatus("deprecated")

hpMcastLimitIngressPortConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 2, 1, 11)
)
hpMcastLimitIngressPortConfigGroup.setObjects(
      *(("HP-ICF-RATE-LIMIT-MIB", "hpIngressMcastLimitPortControlMode"),
        ("HP-ICF-RATE-LIMIT-MIB", "hpIngressMcastLimitPortSingleControlPrct"))
)
if mibBuilder.loadTexts:
    hpMcastLimitIngressPortConfigGroup.setStatus("current")

hpBcastLimitIngressPortConfigGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 2, 1, 12)
)
hpBcastLimitIngressPortConfigGroup2.setObjects(
      *(("HP-ICF-RATE-LIMIT-MIB", "hpIngressBcastLimitPortControlMode"),
        ("HP-ICF-RATE-LIMIT-MIB", "hpIngressBcastLimitPortSingleControlPrct"),
        ("HP-ICF-RATE-LIMIT-MIB", "hpIngressBcastLimitPortSingleControlKbps"))
)
if mibBuilder.loadTexts:
    hpBcastLimitIngressPortConfigGroup2.setStatus("current")

hpMcastLimitIngressPortConfigGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 2, 1, 13)
)
hpMcastLimitIngressPortConfigGroup2.setObjects(
      *(("HP-ICF-RATE-LIMIT-MIB", "hpIngressMcastLimitPortControlMode"),
        ("HP-ICF-RATE-LIMIT-MIB", "hpIngressMcastLimitPortSingleControlPrct"),
        ("HP-ICF-RATE-LIMIT-MIB", "hpIngressMcastLimitPortSingleControlKbps"))
)
if mibBuilder.loadTexts:
    hpMcastLimitIngressPortConfigGroup2.setStatus("current")

hpICMPRateLimitPortConfigGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 2, 1, 14)
)
hpICMPRateLimitPortConfigGroup3.setObjects(
      *(("HP-ICF-RATE-LIMIT-MIB", "hpICMPRateLimitPortPrct"),
        ("HP-ICF-RATE-LIMIT-MIB", "hpICMPRateLimitPortAlarmFlag"),
        ("HP-ICF-RATE-LIMIT-MIB", "hpICMPRateLimitNotifyPortIndex"),
        ("HP-ICF-RATE-LIMIT-MIB", "hpICMPRateLimitPortKbps"),
        ("HP-ICF-RATE-LIMIT-MIB", "hpICMPRateLimitPortControlMode"),
        ("HP-ICF-RATE-LIMIT-MIB", "hpICMPRateLimitPortIpPacketType"))
)
if mibBuilder.loadTexts:
    hpICMPRateLimitPortConfigGroup3.setStatus("current")

hpUnknownUcastLimitIngressPortConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 2, 1, 15)
)
hpUnknownUcastLimitIngressPortConfigGroup.setObjects(
      *(("HP-ICF-RATE-LIMIT-MIB", "hpUnknownUnicastLimitPortControlMode"),
        ("HP-ICF-RATE-LIMIT-MIB", "hpUnknownUnicastLimitPortSingleControlPrct"))
)
if mibBuilder.loadTexts:
    hpUnknownUcastLimitIngressPortConfigGroup.setStatus("deprecated")

hpicfIngressRateLimitVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 2, 1, 16)
)
hpicfIngressRateLimitVlanGroup.setObjects(
      *(("HP-ICF-RATE-LIMIT-MIB", "hpicfIngressRateLimitVlanControlMode"),
        ("HP-ICF-RATE-LIMIT-MIB", "hpicfIngressRateLimitVlanKbps"))
)
if mibBuilder.loadTexts:
    hpicfIngressRateLimitVlanGroup.setStatus("current")

hpUnknownUcastLimitIngressPortConfigGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 2, 1, 17)
)
hpUnknownUcastLimitIngressPortConfigGroup2.setObjects(
      *(("HP-ICF-RATE-LIMIT-MIB", "hpUnknownUnicastLimitPortControlMode"),
        ("HP-ICF-RATE-LIMIT-MIB", "hpUnknownUnicastLimitPortSingleControlPrct"),
        ("HP-ICF-RATE-LIMIT-MIB", "hpUnknownUnicastLimitPortSingleControlKbps"))
)
if mibBuilder.loadTexts:
    hpUnknownUcastLimitIngressPortConfigGroup2.setStatus("current")

hpEgressRateLimitPortConfigGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 2, 1, 18)
)
hpEgressRateLimitPortConfigGroup3.setObjects(
      *(("HP-ICF-RATE-LIMIT-MIB", "hpEgressRateLimitPortNumQueues"),
        ("HP-ICF-RATE-LIMIT-MIB", "hpEgressRateLimitPortControlMode"),
        ("HP-ICF-RATE-LIMIT-MIB", "hpEgressRateLimitPortSingleControlPrct"),
        ("HP-ICF-RATE-LIMIT-MIB", "hpEgressRateLimitPortPrct"),
        ("HP-ICF-RATE-LIMIT-MIB", "hpEgressRateLimitPortSingleControlKbps"),
        ("HP-ICF-RATE-LIMIT-MIB", "hpEgressRateLimitPortQueueControlMode"))
)
if mibBuilder.loadTexts:
    hpEgressRateLimitPortConfigGroup3.setStatus("current")

hpEgressRateLimitPortQueueConfigEntryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 2, 1, 19)
)
hpEgressRateLimitPortQueueConfigEntryGroup.setObjects(
    ("HP-ICF-RATE-LIMIT-MIB", "hpEgressRateLimitPortQueueMax")
)
if mibBuilder.loadTexts:
    hpEgressRateLimitPortQueueConfigEntryGroup.setStatus("current")


# Notification objects

hpICMPRateLimitPortNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 12, 5, 0, 1)
)
hpICMPRateLimitPortNotification.setObjects(
    ("HP-ICF-RATE-LIMIT-MIB", "hpICMPRateLimitNotifyPortIndex")
)
if mibBuilder.loadTexts:
    hpICMPRateLimitPortNotification.setStatus(
        "current"
    )


# Notifications groups

hpICMPRateLimitPortNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 2, 1, 2)
)
hpICMPRateLimitPortNotifyGroup.setObjects(
    ("HP-ICF-RATE-LIMIT-MIB", "hpICMPRateLimitPortNotification")
)
if mibBuilder.loadTexts:
    hpICMPRateLimitPortNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hpicfRateLimitCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hpicfRateLimitCompliance.setStatus(
        "deprecated"
    )

hpicfRateLimitCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 2, 2, 2)
)
if mibBuilder.loadTexts:
    hpicfRateLimitCompliance1.setStatus(
        "deprecated"
    )

hpicfRateLimitCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 2, 2, 3)
)
if mibBuilder.loadTexts:
    hpicfRateLimitCompliance2.setStatus(
        "deprecated"
    )

hpicfRateLimitCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 2, 2, 4)
)
if mibBuilder.loadTexts:
    hpicfRateLimitCompliance3.setStatus(
        "current"
    )

hpicfRateLimitCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 14, 2, 2, 5)
)
if mibBuilder.loadTexts:
    hpicfRateLimitCompliance4.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-RATE-LIMIT-MIB",
    **{"hpicfRateLimitMIB": hpicfRateLimitMIB,
       "hpicfRateLimitObjects": hpicfRateLimitObjects,
       "hpicfICMPRateLimitObjects": hpicfICMPRateLimitObjects,
       "hpICMPRateLimitConfig": hpICMPRateLimitConfig,
       "hpICMPRateLimitPortConfigTable": hpICMPRateLimitPortConfigTable,
       "hpICMPRateLimitPortConfigEntry": hpICMPRateLimitPortConfigEntry,
       "hpICMPRateLimitPortConfigIndex": hpICMPRateLimitPortConfigIndex,
       "hpICMPRateLimitPortState": hpICMPRateLimitPortState,
       "hpICMPRateLimitPortPrct": hpICMPRateLimitPortPrct,
       "hpICMPRateLimitPortAlarmFlag": hpICMPRateLimitPortAlarmFlag,
       "hpICMPRateLimitPortKbps": hpICMPRateLimitPortKbps,
       "hpICMPRateLimitPortControlMode": hpICMPRateLimitPortControlMode,
       "hpICMPRateLimitPortIpPacketType": hpICMPRateLimitPortIpPacketType,
       "hpICMPRateLimitNotifyPortIndex": hpICMPRateLimitNotifyPortIndex,
       "hpicfBWMinEgressObjects": hpicfBWMinEgressObjects,
       "hpBWMinEgressPortConfig": hpBWMinEgressPortConfig,
       "hpBWMinEgressPortNumQueues": hpBWMinEgressPortNumQueues,
       "hpBWMinEgressPortPrctTable": hpBWMinEgressPortPrctTable,
       "hpBWMinEgressPortPrctEntry": hpBWMinEgressPortPrctEntry,
       "hpBWMinEgressPortPrctQueue": hpBWMinEgressPortPrctQueue,
       "hpBWMinEgressPortPrct": hpBWMinEgressPortPrct,
       "hpicfBWMinIngressObjects": hpicfBWMinIngressObjects,
       "hpBWMinIngressPortConfig": hpBWMinIngressPortConfig,
       "hpBWMinIngressPortNumQueues": hpBWMinIngressPortNumQueues,
       "hpBWMinIngressPortPrctTable": hpBWMinIngressPortPrctTable,
       "hpBWMinIngressPortPrctEntry": hpBWMinIngressPortPrctEntry,
       "hpBWMinIngressPortPrctQueue": hpBWMinIngressPortPrctQueue,
       "hpBWMinIngressPortPrct": hpBWMinIngressPortPrct,
       "hpicfRateLimitPortObjects": hpicfRateLimitPortObjects,
       "hpRateLimitPortConfig": hpRateLimitPortConfig,
       "hpEgressRateLimitPortNumQueues": hpEgressRateLimitPortNumQueues,
       "hpEgressRateLimitPortConfigTable": hpEgressRateLimitPortConfigTable,
       "hpEgressRateLimitPortConfigEntry": hpEgressRateLimitPortConfigEntry,
       "hpEgressRateLimitPortIndex": hpEgressRateLimitPortIndex,
       "hpEgressRateLimitPortControlMode": hpEgressRateLimitPortControlMode,
       "hpEgressRateLimitPortSingleControlPrct": hpEgressRateLimitPortSingleControlPrct,
       "hpEgressRateLimitPortSingleControlBps": hpEgressRateLimitPortSingleControlBps,
       "hpEgressRateLimitPortSingleControlKbps": hpEgressRateLimitPortSingleControlKbps,
       "hpEgressRateLimitPortQueueControlMode": hpEgressRateLimitPortQueueControlMode,
       "hpEgressRateLimitPortPrctTable": hpEgressRateLimitPortPrctTable,
       "hpEgressRateLimitPortPrctEntry": hpEgressRateLimitPortPrctEntry,
       "hpEgressRateLimitPortPrctQueue": hpEgressRateLimitPortPrctQueue,
       "hpEgressRateLimitPortPrct": hpEgressRateLimitPortPrct,
       "hpEgressRateLimitPortBpsTable": hpEgressRateLimitPortBpsTable,
       "hpEgressRateLimitPortBpsEntry": hpEgressRateLimitPortBpsEntry,
       "hpEgressRateLimitPortBpsQueue": hpEgressRateLimitPortBpsQueue,
       "hpEgressRateLimitPortBps": hpEgressRateLimitPortBps,
       "hpEgressRateLimitPortQueueConfigTable": hpEgressRateLimitPortQueueConfigTable,
       "hpEgressRateLimitPortQueueConfigEntry": hpEgressRateLimitPortQueueConfigEntry,
       "hpEgressRateLimitPortQueueIndex": hpEgressRateLimitPortQueueIndex,
       "hpEgressRateLimitPortQueueMax": hpEgressRateLimitPortQueueMax,
       "hpicfIngressRateLimitPortObjects": hpicfIngressRateLimitPortObjects,
       "hpRateLimitIngressPortConfig": hpRateLimitIngressPortConfig,
       "hpIngressRateLimitPortNumQueues": hpIngressRateLimitPortNumQueues,
       "hpIngressRateLimitPortConfigTable": hpIngressRateLimitPortConfigTable,
       "hpIngressRateLimitPortConfigEntry": hpIngressRateLimitPortConfigEntry,
       "hpIngressRateLimitPortIndex": hpIngressRateLimitPortIndex,
       "hpIngressRateLimitPortControlMode": hpIngressRateLimitPortControlMode,
       "hpIngressRateLimitPortSingleControlPrct": hpIngressRateLimitPortSingleControlPrct,
       "hpIngressRateLimitPortSingleControlBps": hpIngressRateLimitPortSingleControlBps,
       "hpIngressRateLimitPortSingleControlKbps": hpIngressRateLimitPortSingleControlKbps,
       "hpIngressRateLimitPortPrctTable": hpIngressRateLimitPortPrctTable,
       "hpIngressRateLimitPortPrctEntry": hpIngressRateLimitPortPrctEntry,
       "hpIngressRateLimitPortPrctQueue": hpIngressRateLimitPortPrctQueue,
       "hpIngressRateLimitPortPrct": hpIngressRateLimitPortPrct,
       "hpIngressRateLimitPortBpsTable": hpIngressRateLimitPortBpsTable,
       "hpIngressRateLimitPortBpsEntry": hpIngressRateLimitPortBpsEntry,
       "hpIngressRateLimitPortBpsQueue": hpIngressRateLimitPortBpsQueue,
       "hpIngressRateLimitPortBps": hpIngressRateLimitPortBps,
       "hpicfIngressBcastLimitPortObjects": hpicfIngressBcastLimitPortObjects,
       "hpBcastLimitIngressPortConfig": hpBcastLimitIngressPortConfig,
       "hpIngressBcastLimitPortConfigTable": hpIngressBcastLimitPortConfigTable,
       "hpIngressBcastLimitPortConfigEntry": hpIngressBcastLimitPortConfigEntry,
       "hpIngressBcastLimitPortIndex": hpIngressBcastLimitPortIndex,
       "hpIngressBcastLimitPortControlMode": hpIngressBcastLimitPortControlMode,
       "hpIngressBcastLimitPortSingleControlPrct": hpIngressBcastLimitPortSingleControlPrct,
       "hpIngressBcastLimitPortSingleControlKbps": hpIngressBcastLimitPortSingleControlKbps,
       "hpicfIngressMcastLimitPortObjects": hpicfIngressMcastLimitPortObjects,
       "hpMcastLimitIngressPortConfig": hpMcastLimitIngressPortConfig,
       "hpIngressMcastLimitPortConfigTable": hpIngressMcastLimitPortConfigTable,
       "hpIngressMcastLimitPortConfigEntry": hpIngressMcastLimitPortConfigEntry,
       "hpIngressMcastLimitPortIndex": hpIngressMcastLimitPortIndex,
       "hpIngressMcastLimitPortControlMode": hpIngressMcastLimitPortControlMode,
       "hpIngressMcastLimitPortSingleControlPrct": hpIngressMcastLimitPortSingleControlPrct,
       "hpIngressMcastLimitPortSingleControlKbps": hpIngressMcastLimitPortSingleControlKbps,
       "hpicfUnknownUnicastLimitPortObjects": hpicfUnknownUnicastLimitPortObjects,
       "hpUnknownUnicastLimitPortConfig": hpUnknownUnicastLimitPortConfig,
       "hpUnknownUnicastLimitConfigTable": hpUnknownUnicastLimitConfigTable,
       "hpUnknownUnicastLimitConfigEntry": hpUnknownUnicastLimitConfigEntry,
       "hpUnknownUnicastLimitPortIndex": hpUnknownUnicastLimitPortIndex,
       "hpUnknownUnicastLimitPortControlMode": hpUnknownUnicastLimitPortControlMode,
       "hpUnknownUnicastLimitPortSingleControlPrct": hpUnknownUnicastLimitPortSingleControlPrct,
       "hpUnknownUnicastLimitPortSingleControlKbps": hpUnknownUnicastLimitPortSingleControlKbps,
       "hpicfIngressRateLimitVlanObjects": hpicfIngressRateLimitVlanObjects,
       "hpicfIngressRateLimitVlanConfigTable": hpicfIngressRateLimitVlanConfigTable,
       "hpicfIngressRateLimitVlanConfigEntry": hpicfIngressRateLimitVlanConfigEntry,
       "hpicfIngressRateLimitVlanIndex": hpicfIngressRateLimitVlanIndex,
       "hpicfIngressRateLimitVlanControlMode": hpicfIngressRateLimitVlanControlMode,
       "hpicfIngressRateLimitVlanKbps": hpicfIngressRateLimitVlanKbps,
       "hpicfRateLimitConformance": hpicfRateLimitConformance,
       "hpicfRateLimitGroups": hpicfRateLimitGroups,
       "hpICMPRateLimitPortConfigGroup": hpICMPRateLimitPortConfigGroup,
       "hpICMPRateLimitPortNotifyGroup": hpICMPRateLimitPortNotifyGroup,
       "hpBWMinIngressPortConfigGroup": hpBWMinIngressPortConfigGroup,
       "hpBWMinEgressPortConfigGroup": hpBWMinEgressPortConfigGroup,
       "hpEgressRateLimitPortConfigGroup": hpEgressRateLimitPortConfigGroup,
       "hpIngressRateLimitPortConfigGroup": hpIngressRateLimitPortConfigGroup,
       "hpICMPRateLimitPortConfigGroup2": hpICMPRateLimitPortConfigGroup2,
       "hpEgressRateLimitPortConfigGroup2": hpEgressRateLimitPortConfigGroup2,
       "hpIngressRateLimitPortConfigGroup2": hpIngressRateLimitPortConfigGroup2,
       "hpBcastLimitIngressPortConfigGroup": hpBcastLimitIngressPortConfigGroup,
       "hpMcastLimitIngressPortConfigGroup": hpMcastLimitIngressPortConfigGroup,
       "hpBcastLimitIngressPortConfigGroup2": hpBcastLimitIngressPortConfigGroup2,
       "hpMcastLimitIngressPortConfigGroup2": hpMcastLimitIngressPortConfigGroup2,
       "hpICMPRateLimitPortConfigGroup3": hpICMPRateLimitPortConfigGroup3,
       "hpUnknownUcastLimitIngressPortConfigGroup": hpUnknownUcastLimitIngressPortConfigGroup,
       "hpicfIngressRateLimitVlanGroup": hpicfIngressRateLimitVlanGroup,
       "hpUnknownUcastLimitIngressPortConfigGroup2": hpUnknownUcastLimitIngressPortConfigGroup2,
       "hpEgressRateLimitPortConfigGroup3": hpEgressRateLimitPortConfigGroup3,
       "hpEgressRateLimitPortQueueConfigEntryGroup": hpEgressRateLimitPortQueueConfigEntryGroup,
       "hpicfRateLimitCompliances": hpicfRateLimitCompliances,
       "hpicfRateLimitCompliance": hpicfRateLimitCompliance,
       "hpicfRateLimitCompliance1": hpicfRateLimitCompliance1,
       "hpicfRateLimitCompliance2": hpicfRateLimitCompliance2,
       "hpicfRateLimitCompliance3": hpicfRateLimitCompliance3,
       "hpicfRateLimitCompliance4": hpicfRateLimitCompliance4,
       "hpICMPRateLimitPortNotification": hpICMPRateLimitPortNotification}
)
