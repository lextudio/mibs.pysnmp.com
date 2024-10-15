# SNMP MIB module (HUAWEI-NAT-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-NAT-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:05:21 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hwNatExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class NATProtocolType(Integer32, TextualConvention):
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
        *(("icmp", 2),
          ("other", 1),
          ("tcp", 4),
          ("udp", 3))
    )



class NATFilterMode(Integer32, TextualConvention):
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
        *(("endPointDependent", 2),
          ("endPointIndependent", 1),
          ("endPointPortDependent", 3))
    )



# MIB Managed Objects in the order of their OIDs

_HwNatExtMIBNotifications_ObjectIdentity = ObjectIdentity
hwNatExtMIBNotifications = _HwNatExtMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 1)
)
_HwNatExtMIBObjects_ObjectIdentity = ObjectIdentity
hwNatExtMIBObjects = _HwNatExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2)
)
_HwNatBind_ObjectIdentity = ObjectIdentity
hwNatBind = _HwNatBind_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 1)
)
_HwNatAddrBindNumberOfEntries_Type = Gauge32
_HwNatAddrBindNumberOfEntries_Object = MibScalar
hwNatAddrBindNumberOfEntries = _HwNatAddrBindNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 1, 1),
    _HwNatAddrBindNumberOfEntries_Type()
)
hwNatAddrBindNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatAddrBindNumberOfEntries.setStatus("current")
_HwNatAddrBindTable_Object = MibTable
hwNatAddrBindTable = _HwNatAddrBindTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 1, 2)
)
if mibBuilder.loadTexts:
    hwNatAddrBindTable.setStatus("current")
_HwNatAddrBindEntry_Object = MibTableRow
hwNatAddrBindEntry = _HwNatAddrBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 1, 2, 1)
)
hwNatAddrBindEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HUAWEI-NAT-EXT-MIB", "hwNatAddrBindQueryVrfName"),
    (0, "HUAWEI-NAT-EXT-MIB", "hwNatAddrBindQueryAddr"),
    (0, "HUAWEI-NAT-EXT-MIB", "hwNatAddrBindType"),
)
if mibBuilder.loadTexts:
    hwNatAddrBindEntry.setStatus("current")


class _HwNatAddrBindQueryVrfName_Type(DisplayString):
    """Custom type hwNatAddrBindQueryVrfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwNatAddrBindQueryVrfName_Type.__name__ = "DisplayString"
_HwNatAddrBindQueryVrfName_Object = MibTableColumn
hwNatAddrBindQueryVrfName = _HwNatAddrBindQueryVrfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 1, 2, 1, 1),
    _HwNatAddrBindQueryVrfName_Type()
)
hwNatAddrBindQueryVrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwNatAddrBindQueryVrfName.setStatus("current")
_HwNatAddrBindQueryAddr_Type = IpAddress
_HwNatAddrBindQueryAddr_Object = MibTableColumn
hwNatAddrBindQueryAddr = _HwNatAddrBindQueryAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 1, 2, 1, 2),
    _HwNatAddrBindQueryAddr_Type()
)
hwNatAddrBindQueryAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwNatAddrBindQueryAddr.setStatus("current")


class _HwNatAddrBindType_Type(Integer32):
    """Custom type hwNatAddrBindType based on Integer32"""
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
        *(("natOutbound", 1),
          ("natServer", 2),
          ("staticNatGlobalToLocal", 4),
          ("staticNatLocalToGlobal", 3))
    )


_HwNatAddrBindType_Type.__name__ = "Integer32"
_HwNatAddrBindType_Object = MibTableColumn
hwNatAddrBindType = _HwNatAddrBindType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 1, 2, 1, 3),
    _HwNatAddrBindType_Type()
)
hwNatAddrBindType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwNatAddrBindType.setStatus("current")


class _HwNatAddrBindMappedVrfName_Type(DisplayString):
    """Custom type hwNatAddrBindMappedVrfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwNatAddrBindMappedVrfName_Type.__name__ = "DisplayString"
_HwNatAddrBindMappedVrfName_Object = MibTableColumn
hwNatAddrBindMappedVrfName = _HwNatAddrBindMappedVrfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 1, 2, 1, 4),
    _HwNatAddrBindMappedVrfName_Type()
)
hwNatAddrBindMappedVrfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatAddrBindMappedVrfName.setStatus("current")
_HwNatAddrBindMappedAddr_Type = IpAddress
_HwNatAddrBindMappedAddr_Object = MibTableColumn
hwNatAddrBindMappedAddr = _HwNatAddrBindMappedAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 1, 2, 1, 5),
    _HwNatAddrBindMappedAddr_Type()
)
hwNatAddrBindMappedAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatAddrBindMappedAddr.setStatus("current")
_HwNatAddrBindId_Type = Unsigned32
_HwNatAddrBindId_Object = MibTableColumn
hwNatAddrBindId = _HwNatAddrBindId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 1, 2, 1, 8),
    _HwNatAddrBindId_Type()
)
hwNatAddrBindId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatAddrBindId.setStatus("current")
_HwNatAddrBindSessionCount_Type = Gauge32
_HwNatAddrBindSessionCount_Object = MibTableColumn
hwNatAddrBindSessionCount = _HwNatAddrBindSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 1, 2, 1, 9),
    _HwNatAddrBindSessionCount_Type()
)
hwNatAddrBindSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatAddrBindSessionCount.setStatus("current")
_HwNatAddrBindCurrentIdleTime_Type = TimeTicks
_HwNatAddrBindCurrentIdleTime_Object = MibTableColumn
hwNatAddrBindCurrentIdleTime = _HwNatAddrBindCurrentIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 1, 2, 1, 10),
    _HwNatAddrBindCurrentIdleTime_Type()
)
hwNatAddrBindCurrentIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatAddrBindCurrentIdleTime.setStatus("current")
_HwNatAddrBindInTranslate_Type = Counter32
_HwNatAddrBindInTranslate_Object = MibTableColumn
hwNatAddrBindInTranslate = _HwNatAddrBindInTranslate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 1, 2, 1, 11),
    _HwNatAddrBindInTranslate_Type()
)
hwNatAddrBindInTranslate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatAddrBindInTranslate.setStatus("current")
_HwNatAddrBindOutTranslate_Type = Counter32
_HwNatAddrBindOutTranslate_Object = MibTableColumn
hwNatAddrBindOutTranslate = _HwNatAddrBindOutTranslate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 1, 2, 1, 12),
    _HwNatAddrBindOutTranslate_Type()
)
hwNatAddrBindOutTranslate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatAddrBindOutTranslate.setStatus("current")
_HwNatAddrPortBindNumberOfEntries_Type = Gauge32
_HwNatAddrPortBindNumberOfEntries_Object = MibScalar
hwNatAddrPortBindNumberOfEntries = _HwNatAddrPortBindNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 1, 3),
    _HwNatAddrPortBindNumberOfEntries_Type()
)
hwNatAddrPortBindNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatAddrPortBindNumberOfEntries.setStatus("current")
_HwNatAddrPortBindTable_Object = MibTable
hwNatAddrPortBindTable = _HwNatAddrPortBindTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 1, 4)
)
if mibBuilder.loadTexts:
    hwNatAddrPortBindTable.setStatus("current")
_HwNatAddrPortBindEntry_Object = MibTableRow
hwNatAddrPortBindEntry = _HwNatAddrPortBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 1, 4, 1)
)
hwNatAddrPortBindEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HUAWEI-NAT-EXT-MIB", "hwNatAddrPortBindQueryVrfName"),
    (0, "HUAWEI-NAT-EXT-MIB", "hwNatAddrPortBindQueryAddr"),
    (0, "HUAWEI-NAT-EXT-MIB", "hwNatAddrPortBindQueryProtocol"),
    (0, "HUAWEI-NAT-EXT-MIB", "hwNatAddrPortBindQueryPort"),
    (0, "HUAWEI-NAT-EXT-MIB", "hwNatAddrPortBindType"),
)
if mibBuilder.loadTexts:
    hwNatAddrPortBindEntry.setStatus("current")


class _HwNatAddrPortBindQueryVrfName_Type(DisplayString):
    """Custom type hwNatAddrPortBindQueryVrfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwNatAddrPortBindQueryVrfName_Type.__name__ = "DisplayString"
_HwNatAddrPortBindQueryVrfName_Object = MibTableColumn
hwNatAddrPortBindQueryVrfName = _HwNatAddrPortBindQueryVrfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 1, 4, 1, 1),
    _HwNatAddrPortBindQueryVrfName_Type()
)
hwNatAddrPortBindQueryVrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwNatAddrPortBindQueryVrfName.setStatus("current")
_HwNatAddrPortBindQueryAddr_Type = IpAddress
_HwNatAddrPortBindQueryAddr_Object = MibTableColumn
hwNatAddrPortBindQueryAddr = _HwNatAddrPortBindQueryAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 1, 4, 1, 2),
    _HwNatAddrPortBindQueryAddr_Type()
)
hwNatAddrPortBindQueryAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwNatAddrPortBindQueryAddr.setStatus("current")


class _HwNatAddrPortBindQueryProtocol_Type(Integer32):
    """Custom type hwNatAddrPortBindQueryProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HwNatAddrPortBindQueryProtocol_Type.__name__ = "Integer32"
_HwNatAddrPortBindQueryProtocol_Object = MibTableColumn
hwNatAddrPortBindQueryProtocol = _HwNatAddrPortBindQueryProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 1, 4, 1, 3),
    _HwNatAddrPortBindQueryProtocol_Type()
)
hwNatAddrPortBindQueryProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwNatAddrPortBindQueryProtocol.setStatus("current")


class _HwNatAddrPortBindQueryPort_Type(Integer32):
    """Custom type hwNatAddrPortBindQueryPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwNatAddrPortBindQueryPort_Type.__name__ = "Integer32"
_HwNatAddrPortBindQueryPort_Object = MibTableColumn
hwNatAddrPortBindQueryPort = _HwNatAddrPortBindQueryPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 1, 4, 1, 4),
    _HwNatAddrPortBindQueryPort_Type()
)
hwNatAddrPortBindQueryPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwNatAddrPortBindQueryPort.setStatus("current")


class _HwNatAddrPortBindType_Type(Integer32):
    """Custom type hwNatAddrPortBindType based on Integer32"""
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
        *(("natOutbound", 1),
          ("natServer", 2),
          ("staticPatGlobalToLocal", 4),
          ("staticPatLocalToGlobal", 3))
    )


_HwNatAddrPortBindType_Type.__name__ = "Integer32"
_HwNatAddrPortBindType_Object = MibTableColumn
hwNatAddrPortBindType = _HwNatAddrPortBindType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 1, 4, 1, 5),
    _HwNatAddrPortBindType_Type()
)
hwNatAddrPortBindType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwNatAddrPortBindType.setStatus("current")


class _HwNatAddrPortBindMappedVrfName_Type(DisplayString):
    """Custom type hwNatAddrPortBindMappedVrfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwNatAddrPortBindMappedVrfName_Type.__name__ = "DisplayString"
_HwNatAddrPortBindMappedVrfName_Object = MibTableColumn
hwNatAddrPortBindMappedVrfName = _HwNatAddrPortBindMappedVrfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 1, 4, 1, 6),
    _HwNatAddrPortBindMappedVrfName_Type()
)
hwNatAddrPortBindMappedVrfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatAddrPortBindMappedVrfName.setStatus("current")
_HwNatAddrPortBindMappedAddr_Type = IpAddress
_HwNatAddrPortBindMappedAddr_Object = MibTableColumn
hwNatAddrPortBindMappedAddr = _HwNatAddrPortBindMappedAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 1, 4, 1, 7),
    _HwNatAddrPortBindMappedAddr_Type()
)
hwNatAddrPortBindMappedAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatAddrPortBindMappedAddr.setStatus("current")


class _HwNatAddrPortBindMappedPort_Type(Integer32):
    """Custom type hwNatAddrPortBindMappedPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwNatAddrPortBindMappedPort_Type.__name__ = "Integer32"
_HwNatAddrPortBindMappedPort_Object = MibTableColumn
hwNatAddrPortBindMappedPort = _HwNatAddrPortBindMappedPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 1, 4, 1, 8),
    _HwNatAddrPortBindMappedPort_Type()
)
hwNatAddrPortBindMappedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatAddrPortBindMappedPort.setStatus("current")
_HwNatAddrPortBindId_Type = Unsigned32
_HwNatAddrPortBindId_Object = MibTableColumn
hwNatAddrPortBindId = _HwNatAddrPortBindId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 1, 4, 1, 10),
    _HwNatAddrPortBindId_Type()
)
hwNatAddrPortBindId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatAddrPortBindId.setStatus("current")
_HwNatAddrPortBindSessionCount_Type = Gauge32
_HwNatAddrPortBindSessionCount_Object = MibTableColumn
hwNatAddrPortBindSessionCount = _HwNatAddrPortBindSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 1, 4, 1, 12),
    _HwNatAddrPortBindSessionCount_Type()
)
hwNatAddrPortBindSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatAddrPortBindSessionCount.setStatus("current")
_HwNatAddrPortBindCurrentIdleTime_Type = TimeTicks
_HwNatAddrPortBindCurrentIdleTime_Object = MibTableColumn
hwNatAddrPortBindCurrentIdleTime = _HwNatAddrPortBindCurrentIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 1, 4, 1, 13),
    _HwNatAddrPortBindCurrentIdleTime_Type()
)
hwNatAddrPortBindCurrentIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatAddrPortBindCurrentIdleTime.setStatus("current")
_HwNatAddrPortBindInTranslate_Type = Counter32
_HwNatAddrPortBindInTranslate_Object = MibTableColumn
hwNatAddrPortBindInTranslate = _HwNatAddrPortBindInTranslate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 1, 4, 1, 14),
    _HwNatAddrPortBindInTranslate_Type()
)
hwNatAddrPortBindInTranslate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatAddrPortBindInTranslate.setStatus("current")
_HwNatAddrPortBindOutTranslate_Type = Counter32
_HwNatAddrPortBindOutTranslate_Object = MibTableColumn
hwNatAddrPortBindOutTranslate = _HwNatAddrPortBindOutTranslate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 1, 4, 1, 15),
    _HwNatAddrPortBindOutTranslate_Type()
)
hwNatAddrPortBindOutTranslate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatAddrPortBindOutTranslate.setStatus("current")
_HwNatExtIfTable_Object = MibTable
hwNatExtIfTable = _HwNatExtIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 1, 5)
)
if mibBuilder.loadTexts:
    hwNatExtIfTable.setStatus("current")
_HwNatExtIfEntry_Object = MibTableRow
hwNatExtIfEntry = _HwNatExtIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 1, 5, 1)
)
hwNatExtIfEntry.setIndexNames(
    (0, "HUAWEI-NAT-EXT-MIB", "hwNatExtIfName"),
)
if mibBuilder.loadTexts:
    hwNatExtIfEntry.setStatus("current")


class _HwNatExtIfName_Type(OctetString):
    """Custom type hwNatExtIfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 47),
    )


_HwNatExtIfName_Type.__name__ = "OctetString"
_HwNatExtIfName_Object = MibTableColumn
hwNatExtIfName = _HwNatExtIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 1, 5, 1, 1),
    _HwNatExtIfName_Type()
)
hwNatExtIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatExtIfName.setStatus("current")
_HwNatStatistics_ObjectIdentity = ObjectIdentity
hwNatStatistics = _HwNatStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 2)
)
_HwNatProtocolStatsTable_Object = MibTable
hwNatProtocolStatsTable = _HwNatProtocolStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hwNatProtocolStatsTable.setStatus("current")
_HwNatProtocolStatsEntry_Object = MibTableRow
hwNatProtocolStatsEntry = _HwNatProtocolStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 2, 1, 1)
)
hwNatProtocolStatsEntry.setIndexNames(
    (0, "HUAWEI-NAT-EXT-MIB", "hwNatProtocolStatsName"),
)
if mibBuilder.loadTexts:
    hwNatProtocolStatsEntry.setStatus("current")
_HwNatProtocolStatsName_Type = NATProtocolType
_HwNatProtocolStatsName_Object = MibTableColumn
hwNatProtocolStatsName = _HwNatProtocolStatsName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 2, 1, 1, 1),
    _HwNatProtocolStatsName_Type()
)
hwNatProtocolStatsName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwNatProtocolStatsName.setStatus("current")
_HwNatProtocolStatsInTranslate_Type = Counter32
_HwNatProtocolStatsInTranslate_Object = MibTableColumn
hwNatProtocolStatsInTranslate = _HwNatProtocolStatsInTranslate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 2, 1, 1, 2),
    _HwNatProtocolStatsInTranslate_Type()
)
hwNatProtocolStatsInTranslate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatProtocolStatsInTranslate.setStatus("current")
_HwNatProtocolStatsOutTranslate_Type = Counter32
_HwNatProtocolStatsOutTranslate_Object = MibTableColumn
hwNatProtocolStatsOutTranslate = _HwNatProtocolStatsOutTranslate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 2, 1, 1, 3),
    _HwNatProtocolStatsOutTranslate_Type()
)
hwNatProtocolStatsOutTranslate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatProtocolStatsOutTranslate.setStatus("current")
_HwNatProtocolStatsRejectCount_Type = Counter32
_HwNatProtocolStatsRejectCount_Object = MibTableColumn
hwNatProtocolStatsRejectCount = _HwNatProtocolStatsRejectCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 2, 1, 1, 4),
    _HwNatProtocolStatsRejectCount_Type()
)
hwNatProtocolStatsRejectCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatProtocolStatsRejectCount.setStatus("current")
_HwNatInterfaceStatsTable_Object = MibTable
hwNatInterfaceStatsTable = _HwNatInterfaceStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 2, 2)
)
if mibBuilder.loadTexts:
    hwNatInterfaceStatsTable.setStatus("current")
_HwNatInterfaceStatsEntry_Object = MibTableRow
hwNatInterfaceStatsEntry = _HwNatInterfaceStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 2, 2, 1)
)
hwNatInterfaceStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hwNatInterfaceStatsEntry.setStatus("current")
_HwNatInterfacePktsIn_Type = Counter32
_HwNatInterfacePktsIn_Object = MibTableColumn
hwNatInterfacePktsIn = _HwNatInterfacePktsIn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 2, 2, 1, 1),
    _HwNatInterfacePktsIn_Type()
)
hwNatInterfacePktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatInterfacePktsIn.setStatus("current")
_HwNatInterfacePktsOut_Type = Counter32
_HwNatInterfacePktsOut_Object = MibTableColumn
hwNatInterfacePktsOut = _HwNatInterfacePktsOut_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 2, 2, 1, 2),
    _HwNatInterfacePktsOut_Type()
)
hwNatInterfacePktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatInterfacePktsOut.setStatus("current")
_HwNATSessionCntTable_Object = MibTable
hwNATSessionCntTable = _HwNATSessionCntTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 2, 3)
)
if mibBuilder.loadTexts:
    hwNATSessionCntTable.setStatus("current")
_HwNATSessionCntEntry_Object = MibTableRow
hwNATSessionCntEntry = _HwNATSessionCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 2, 3, 1)
)
hwNATSessionCntEntry.setIndexNames(
    (0, "HUAWEI-NAT-EXT-MIB", "hwNATSlotIndex"),
)
if mibBuilder.loadTexts:
    hwNATSessionCntEntry.setStatus("current")


class _HwNATSlotIndex_Type(Integer32):
    """Custom type hwNATSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_HwNATSlotIndex_Type.__name__ = "Integer32"
_HwNATSlotIndex_Object = MibTableColumn
hwNATSlotIndex = _HwNATSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 2, 3, 1, 1),
    _HwNATSlotIndex_Type()
)
hwNATSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNATSlotIndex.setStatus("current")
_HwNATSessionCnt_Type = Unsigned32
_HwNATSessionCnt_Object = MibTableColumn
hwNATSessionCnt = _HwNATSessionCnt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 2, 3, 1, 2),
    _HwNATSessionCnt_Type()
)
hwNATSessionCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNATSessionCnt.setStatus("current")
_HwNatAddrPool_ObjectIdentity = ObjectIdentity
hwNatAddrPool = _HwNatAddrPool_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 3)
)


class _HwNatAddrPoolNumOfEntries_Type(Gauge32):
    """Custom type hwNatAddrPoolNumOfEntries based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_HwNatAddrPoolNumOfEntries_Type.__name__ = "Gauge32"
_HwNatAddrPoolNumOfEntries_Object = MibScalar
hwNatAddrPoolNumOfEntries = _HwNatAddrPoolNumOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 3, 1),
    _HwNatAddrPoolNumOfEntries_Type()
)
hwNatAddrPoolNumOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatAddrPoolNumOfEntries.setStatus("current")
_HwNatAddrPoolTable_Object = MibTable
hwNatAddrPoolTable = _HwNatAddrPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 3, 2)
)
if mibBuilder.loadTexts:
    hwNatAddrPoolTable.setStatus("current")
_HwNatAddrPoolEntry_Object = MibTableRow
hwNatAddrPoolEntry = _HwNatAddrPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 3, 2, 1)
)
hwNatAddrPoolEntry.setIndexNames(
    (0, "HUAWEI-NAT-EXT-MIB", "hwNatAddrPoolIndex"),
)
if mibBuilder.loadTexts:
    hwNatAddrPoolEntry.setStatus("current")


class _HwNatAddrPoolIndex_Type(Unsigned32):
    """Custom type hwNatAddrPoolIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_HwNatAddrPoolIndex_Type.__name__ = "Unsigned32"
_HwNatAddrPoolIndex_Object = MibTableColumn
hwNatAddrPoolIndex = _HwNatAddrPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 3, 2, 1, 1),
    _HwNatAddrPoolIndex_Type()
)
hwNatAddrPoolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwNatAddrPoolIndex.setStatus("current")
_HwNatAddrPoolStartAddr_Type = IpAddress
_HwNatAddrPoolStartAddr_Object = MibTableColumn
hwNatAddrPoolStartAddr = _HwNatAddrPoolStartAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 3, 2, 1, 2),
    _HwNatAddrPoolStartAddr_Type()
)
hwNatAddrPoolStartAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatAddrPoolStartAddr.setStatus("current")
_HwNatAddrPoolEndAddr_Type = IpAddress
_HwNatAddrPoolEndAddr_Object = MibTableColumn
hwNatAddrPoolEndAddr = _HwNatAddrPoolEndAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 3, 2, 1, 3),
    _HwNatAddrPoolEndAddr_Type()
)
hwNatAddrPoolEndAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatAddrPoolEndAddr.setStatus("current")
_HwNatAddrPoolRefTimes_Type = Gauge32
_HwNatAddrPoolRefTimes_Object = MibTableColumn
hwNatAddrPoolRefTimes = _HwNatAddrPoolRefTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 3, 2, 1, 4),
    _HwNatAddrPoolRefTimes_Type()
)
hwNatAddrPoolRefTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatAddrPoolRefTimes.setStatus("current")


class _HwNatAddrPoolRefType_Type(Integer32):
    """Custom type hwNatAddrPoolRefType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_HwNatAddrPoolRefType_Type.__name__ = "Integer32"
_HwNatAddrPoolRefType_Object = MibTableColumn
hwNatAddrPoolRefType = _HwNatAddrPoolRefType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 3, 2, 1, 5),
    _HwNatAddrPoolRefType_Type()
)
hwNatAddrPoolRefType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatAddrPoolRefType.setStatus("current")
_HwNatDnsMap_ObjectIdentity = ObjectIdentity
hwNatDnsMap = _HwNatDnsMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 4)
)
_HwNatDnsMapNumOfEntries_Type = Gauge32
_HwNatDnsMapNumOfEntries_Object = MibScalar
hwNatDnsMapNumOfEntries = _HwNatDnsMapNumOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 4, 1),
    _HwNatDnsMapNumOfEntries_Type()
)
hwNatDnsMapNumOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatDnsMapNumOfEntries.setStatus("current")
_HwNatDnsMapTable_Object = MibTable
hwNatDnsMapTable = _HwNatDnsMapTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 4, 2)
)
if mibBuilder.loadTexts:
    hwNatDnsMapTable.setStatus("current")
_HwNatDnsMapEntry_Object = MibTableRow
hwNatDnsMapEntry = _HwNatDnsMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 4, 2, 1)
)
hwNatDnsMapEntry.setIndexNames(
    (0, "HUAWEI-NAT-EXT-MIB", "hwNatDnsMapIndex"),
)
if mibBuilder.loadTexts:
    hwNatDnsMapEntry.setStatus("current")
_HwNatDnsMapIndex_Type = Unsigned32
_HwNatDnsMapIndex_Object = MibTableColumn
hwNatDnsMapIndex = _HwNatDnsMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 4, 2, 1, 1),
    _HwNatDnsMapIndex_Type()
)
hwNatDnsMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwNatDnsMapIndex.setStatus("current")


class _HwNatDnsMapDomainName_Type(OctetString):
    """Custom type hwNatDnsMapDomainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwNatDnsMapDomainName_Type.__name__ = "OctetString"
_HwNatDnsMapDomainName_Object = MibTableColumn
hwNatDnsMapDomainName = _HwNatDnsMapDomainName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 4, 2, 1, 2),
    _HwNatDnsMapDomainName_Type()
)
hwNatDnsMapDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatDnsMapDomainName.setStatus("current")
_HwNatDnsMapIpAddr_Type = IpAddress
_HwNatDnsMapIpAddr_Object = MibTableColumn
hwNatDnsMapIpAddr = _HwNatDnsMapIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 4, 2, 1, 3),
    _HwNatDnsMapIpAddr_Type()
)
hwNatDnsMapIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatDnsMapIpAddr.setStatus("current")
_HwNatDnsMapPort_Type = Unsigned32
_HwNatDnsMapPort_Object = MibTableColumn
hwNatDnsMapPort = _HwNatDnsMapPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 4, 2, 1, 4),
    _HwNatDnsMapPort_Type()
)
hwNatDnsMapPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatDnsMapPort.setStatus("current")


class _HwNatDnsMapProtocol_Type(Integer32):
    """Custom type hwNatDnsMapProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HwNatDnsMapProtocol_Type.__name__ = "Integer32"
_HwNatDnsMapProtocol_Object = MibTableColumn
hwNatDnsMapProtocol = _HwNatDnsMapProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 4, 2, 1, 5),
    _HwNatDnsMapProtocol_Type()
)
hwNatDnsMapProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatDnsMapProtocol.setStatus("current")
_HwNatOutbound_ObjectIdentity = ObjectIdentity
hwNatOutbound = _HwNatOutbound_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 5)
)
_HwNatOutboundNumOfEntries_Type = Gauge32
_HwNatOutboundNumOfEntries_Object = MibScalar
hwNatOutboundNumOfEntries = _HwNatOutboundNumOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 5, 1),
    _HwNatOutboundNumOfEntries_Type()
)
hwNatOutboundNumOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatOutboundNumOfEntries.setStatus("current")
_HwNatOutboundTable_Object = MibTable
hwNatOutboundTable = _HwNatOutboundTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 5, 2)
)
if mibBuilder.loadTexts:
    hwNatOutboundTable.setStatus("current")
_HwNatOutboundEntry_Object = MibTableRow
hwNatOutboundEntry = _HwNatOutboundEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 5, 2, 1)
)
hwNatOutboundEntry.setIndexNames(
    (0, "HUAWEI-NAT-EXT-MIB", "hwNatOutboundIndex"),
)
if mibBuilder.loadTexts:
    hwNatOutboundEntry.setStatus("current")


class _HwNatOutboundIndex_Type(Unsigned32):
    """Custom type hwNatOutboundIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_HwNatOutboundIndex_Type.__name__ = "Unsigned32"
_HwNatOutboundIndex_Object = MibTableColumn
hwNatOutboundIndex = _HwNatOutboundIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 5, 2, 1, 1),
    _HwNatOutboundIndex_Type()
)
hwNatOutboundIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwNatOutboundIndex.setStatus("current")
_HwNatOutboundInterface_Type = Unsigned32
_HwNatOutboundInterface_Object = MibTableColumn
hwNatOutboundInterface = _HwNatOutboundInterface_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 5, 2, 1, 2),
    _HwNatOutboundInterface_Type()
)
hwNatOutboundInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatOutboundInterface.setStatus("current")


class _HwNatOutboundAclNum_Type(Unsigned32):
    """Custom type hwNatOutboundAclNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 3999),
    )


_HwNatOutboundAclNum_Type.__name__ = "Unsigned32"
_HwNatOutboundAclNum_Object = MibTableColumn
hwNatOutboundAclNum = _HwNatOutboundAclNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 5, 2, 1, 3),
    _HwNatOutboundAclNum_Type()
)
hwNatOutboundAclNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatOutboundAclNum.setStatus("current")
_HwNatOutboundAddr_Type = IpAddress
_HwNatOutboundAddr_Object = MibTableColumn
hwNatOutboundAddr = _HwNatOutboundAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 5, 2, 1, 4),
    _HwNatOutboundAddr_Type()
)
hwNatOutboundAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatOutboundAddr.setStatus("current")


class _HwNatOutboundPat_Type(Integer32):
    """Custom type hwNatOutboundPat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_HwNatOutboundPat_Type.__name__ = "Integer32"
_HwNatOutboundPat_Object = MibTableColumn
hwNatOutboundPat = _HwNatOutboundPat_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 5, 2, 1, 5),
    _HwNatOutboundPat_Type()
)
hwNatOutboundPat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatOutboundPat.setStatus("current")
_HwNatOutboundEasyIp_Type = TruthValue
_HwNatOutboundEasyIp_Object = MibTableColumn
hwNatOutboundEasyIp = _HwNatOutboundEasyIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 5, 2, 1, 6),
    _HwNatOutboundEasyIp_Type()
)
hwNatOutboundEasyIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatOutboundEasyIp.setStatus("current")
_HwNatOverlapMap_ObjectIdentity = ObjectIdentity
hwNatOverlapMap = _HwNatOverlapMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 6)
)
_HwNatOverlapMapNumOfEntries_Type = Gauge32
_HwNatOverlapMapNumOfEntries_Object = MibScalar
hwNatOverlapMapNumOfEntries = _HwNatOverlapMapNumOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 6, 1),
    _HwNatOverlapMapNumOfEntries_Type()
)
hwNatOverlapMapNumOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatOverlapMapNumOfEntries.setStatus("current")
_HwNatOverlapMapTable_Object = MibTable
hwNatOverlapMapTable = _HwNatOverlapMapTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 6, 2)
)
if mibBuilder.loadTexts:
    hwNatOverlapMapTable.setStatus("current")
_HwNatOverlapMapEntry_Object = MibTableRow
hwNatOverlapMapEntry = _HwNatOverlapMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 6, 2, 1)
)
hwNatOverlapMapEntry.setIndexNames(
    (0, "HUAWEI-NAT-EXT-MIB", "hwNatOverlapMapIndex"),
)
if mibBuilder.loadTexts:
    hwNatOverlapMapEntry.setStatus("current")
_HwNatOverlapMapIndex_Type = Unsigned32
_HwNatOverlapMapIndex_Object = MibTableColumn
hwNatOverlapMapIndex = _HwNatOverlapMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 6, 2, 1, 1),
    _HwNatOverlapMapIndex_Type()
)
hwNatOverlapMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwNatOverlapMapIndex.setStatus("current")
_HwNatOverlapMapLapAddr_Type = IpAddress
_HwNatOverlapMapLapAddr_Object = MibTableColumn
hwNatOverlapMapLapAddr = _HwNatOverlapMapLapAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 6, 2, 1, 2),
    _HwNatOverlapMapLapAddr_Type()
)
hwNatOverlapMapLapAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatOverlapMapLapAddr.setStatus("current")
_HwNatOverlapMapTmpAddr_Type = IpAddress
_HwNatOverlapMapTmpAddr_Object = MibTableColumn
hwNatOverlapMapTmpAddr = _HwNatOverlapMapTmpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 6, 2, 1, 3),
    _HwNatOverlapMapTmpAddr_Type()
)
hwNatOverlapMapTmpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatOverlapMapTmpAddr.setStatus("current")
_HwNatOverlapMapPoolLen_Type = Unsigned32
_HwNatOverlapMapPoolLen_Object = MibTableColumn
hwNatOverlapMapPoolLen = _HwNatOverlapMapPoolLen_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 6, 2, 1, 4),
    _HwNatOverlapMapPoolLen_Type()
)
hwNatOverlapMapPoolLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatOverlapMapPoolLen.setStatus("current")
_HwNatOverlapMapVpnName_Type = OctetString
_HwNatOverlapMapVpnName_Object = MibTableColumn
hwNatOverlapMapVpnName = _HwNatOverlapMapVpnName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 6, 2, 1, 5),
    _HwNatOverlapMapVpnName_Type()
)
hwNatOverlapMapVpnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatOverlapMapVpnName.setStatus("current")
_HwNatServer_ObjectIdentity = ObjectIdentity
hwNatServer = _HwNatServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 7)
)
_HwNatServerNumOfEntries_Type = Gauge32
_HwNatServerNumOfEntries_Object = MibScalar
hwNatServerNumOfEntries = _HwNatServerNumOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 7, 1),
    _HwNatServerNumOfEntries_Type()
)
hwNatServerNumOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatServerNumOfEntries.setStatus("current")
_HwNatServerTable_Object = MibTable
hwNatServerTable = _HwNatServerTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 7, 2)
)
if mibBuilder.loadTexts:
    hwNatServerTable.setStatus("current")
_HwNatServerEntry_Object = MibTableRow
hwNatServerEntry = _HwNatServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 7, 2, 1)
)
hwNatServerEntry.setIndexNames(
    (0, "HUAWEI-NAT-EXT-MIB", "hwNatServerIndex"),
)
if mibBuilder.loadTexts:
    hwNatServerEntry.setStatus("current")
_HwNatServerIndex_Type = Unsigned32
_HwNatServerIndex_Object = MibTableColumn
hwNatServerIndex = _HwNatServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 7, 2, 1, 1),
    _HwNatServerIndex_Type()
)
hwNatServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwNatServerIndex.setStatus("current")
_HwNatServerInterface_Type = OctetString
_HwNatServerInterface_Object = MibTableColumn
hwNatServerInterface = _HwNatServerInterface_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 7, 2, 1, 2),
    _HwNatServerInterface_Type()
)
hwNatServerInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatServerInterface.setStatus("current")


class _HwNatServerProtocol_Type(Integer32):
    """Custom type hwNatServerProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HwNatServerProtocol_Type.__name__ = "Integer32"
_HwNatServerProtocol_Object = MibTableColumn
hwNatServerProtocol = _HwNatServerProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 7, 2, 1, 3),
    _HwNatServerProtocol_Type()
)
hwNatServerProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatServerProtocol.setStatus("current")
_HwNatServerGlobalAddr_Type = IpAddress
_HwNatServerGlobalAddr_Object = MibTableColumn
hwNatServerGlobalAddr = _HwNatServerGlobalAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 7, 2, 1, 4),
    _HwNatServerGlobalAddr_Type()
)
hwNatServerGlobalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatServerGlobalAddr.setStatus("current")
_HwNatServerGlobalPort_Type = Unsigned32
_HwNatServerGlobalPort_Object = MibTableColumn
hwNatServerGlobalPort = _HwNatServerGlobalPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 7, 2, 1, 5),
    _HwNatServerGlobalPort_Type()
)
hwNatServerGlobalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatServerGlobalPort.setStatus("current")
_HwNatServerInsideAddr_Type = IpAddress
_HwNatServerInsideAddr_Object = MibTableColumn
hwNatServerInsideAddr = _HwNatServerInsideAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 7, 2, 1, 6),
    _HwNatServerInsideAddr_Type()
)
hwNatServerInsideAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatServerInsideAddr.setStatus("current")
_HwNatServerInsidePort_Type = Unsigned32
_HwNatServerInsidePort_Object = MibTableColumn
hwNatServerInsidePort = _HwNatServerInsidePort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 7, 2, 1, 7),
    _HwNatServerInsidePort_Type()
)
hwNatServerInsidePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatServerInsidePort.setStatus("current")
_HwNatServerVpnName_Type = OctetString
_HwNatServerVpnName_Object = MibTableColumn
hwNatServerVpnName = _HwNatServerVpnName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 7, 2, 1, 8),
    _HwNatServerVpnName_Type()
)
hwNatServerVpnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatServerVpnName.setStatus("current")
_HwNatStatic_ObjectIdentity = ObjectIdentity
hwNatStatic = _HwNatStatic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 8)
)
_HwNatStaticNumOfEntries_Type = Gauge32
_HwNatStaticNumOfEntries_Object = MibScalar
hwNatStaticNumOfEntries = _HwNatStaticNumOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 8, 1),
    _HwNatStaticNumOfEntries_Type()
)
hwNatStaticNumOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatStaticNumOfEntries.setStatus("current")
_HwNatStaticTable_Object = MibTable
hwNatStaticTable = _HwNatStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 8, 2)
)
if mibBuilder.loadTexts:
    hwNatStaticTable.setStatus("current")
_HwNatStaticEntry_Object = MibTableRow
hwNatStaticEntry = _HwNatStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 8, 2, 1)
)
hwNatStaticEntry.setIndexNames(
    (0, "HUAWEI-NAT-EXT-MIB", "hwNatStaticIndex"),
)
if mibBuilder.loadTexts:
    hwNatStaticEntry.setStatus("current")
_HwNatStaticIndex_Type = Unsigned32
_HwNatStaticIndex_Object = MibTableColumn
hwNatStaticIndex = _HwNatStaticIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 8, 2, 1, 1),
    _HwNatStaticIndex_Type()
)
hwNatStaticIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwNatStaticIndex.setStatus("current")
_HwNatStaticInterface_Type = OctetString
_HwNatStaticInterface_Object = MibTableColumn
hwNatStaticInterface = _HwNatStaticInterface_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 8, 2, 1, 2),
    _HwNatStaticInterface_Type()
)
hwNatStaticInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatStaticInterface.setStatus("current")


class _HwNatStaticProtocol_Type(Integer32):
    """Custom type hwNatStaticProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HwNatStaticProtocol_Type.__name__ = "Integer32"
_HwNatStaticProtocol_Object = MibTableColumn
hwNatStaticProtocol = _HwNatStaticProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 8, 2, 1, 3),
    _HwNatStaticProtocol_Type()
)
hwNatStaticProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatStaticProtocol.setStatus("current")
_HwNatStaticGlobalAddr_Type = IpAddress
_HwNatStaticGlobalAddr_Object = MibTableColumn
hwNatStaticGlobalAddr = _HwNatStaticGlobalAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 8, 2, 1, 4),
    _HwNatStaticGlobalAddr_Type()
)
hwNatStaticGlobalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatStaticGlobalAddr.setStatus("current")
_HwNatStaticGlobalPort_Type = Unsigned32
_HwNatStaticGlobalPort_Object = MibTableColumn
hwNatStaticGlobalPort = _HwNatStaticGlobalPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 8, 2, 1, 5),
    _HwNatStaticGlobalPort_Type()
)
hwNatStaticGlobalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatStaticGlobalPort.setStatus("current")
_HwNatStaticInsideAddr_Type = IpAddress
_HwNatStaticInsideAddr_Object = MibTableColumn
hwNatStaticInsideAddr = _HwNatStaticInsideAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 8, 2, 1, 6),
    _HwNatStaticInsideAddr_Type()
)
hwNatStaticInsideAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatStaticInsideAddr.setStatus("current")
_HwNatStaticInsidePort_Type = Unsigned32
_HwNatStaticInsidePort_Object = MibTableColumn
hwNatStaticInsidePort = _HwNatStaticInsidePort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 8, 2, 1, 7),
    _HwNatStaticInsidePort_Type()
)
hwNatStaticInsidePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatStaticInsidePort.setStatus("current")
_HwNatStaticVpnName_Type = OctetString
_HwNatStaticVpnName_Object = MibTableColumn
hwNatStaticVpnName = _HwNatStaticVpnName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 8, 2, 1, 8),
    _HwNatStaticVpnName_Type()
)
hwNatStaticVpnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatStaticVpnName.setStatus("current")
_HwNatStaticNetMask_Type = IpAddress
_HwNatStaticNetMask_Object = MibTableColumn
hwNatStaticNetMask = _HwNatStaticNetMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 8, 2, 1, 9),
    _HwNatStaticNetMask_Type()
)
hwNatStaticNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatStaticNetMask.setStatus("current")
_HwNatAlg_ObjectIdentity = ObjectIdentity
hwNatAlg = _HwNatAlg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 9)
)
_HwNatAlgFtp_Type = TruthValue
_HwNatAlgFtp_Object = MibScalar
hwNatAlgFtp = _HwNatAlgFtp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 9, 1),
    _HwNatAlgFtp_Type()
)
hwNatAlgFtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatAlgFtp.setStatus("current")
_HwNatAlgDns_Type = TruthValue
_HwNatAlgDns_Object = MibScalar
hwNatAlgDns = _HwNatAlgDns_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 9, 2),
    _HwNatAlgDns_Type()
)
hwNatAlgDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatAlgDns.setStatus("current")
_HwNatAlgSip_Type = TruthValue
_HwNatAlgSip_Object = MibScalar
hwNatAlgSip = _HwNatAlgSip_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 9, 3),
    _HwNatAlgSip_Type()
)
hwNatAlgSip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatAlgSip.setStatus("current")
_HwNatAlgRtsp_Type = TruthValue
_HwNatAlgRtsp_Object = MibScalar
hwNatAlgRtsp = _HwNatAlgRtsp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 9, 4),
    _HwNatAlgRtsp_Type()
)
hwNatAlgRtsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatAlgRtsp.setStatus("current")
_HwNatFilter_ObjectIdentity = ObjectIdentity
hwNatFilter = _HwNatFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 10)
)
_HwNatFilterMode_Type = NATFilterMode
_HwNatFilterMode_Object = MibScalar
hwNatFilterMode = _HwNatFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 10, 1),
    _HwNatFilterMode_Type()
)
hwNatFilterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatFilterMode.setStatus("current")
_HwNatPortMap_ObjectIdentity = ObjectIdentity
hwNatPortMap = _HwNatPortMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 11)
)


class _HwNatPortMapSipPort_Type(Unsigned32):
    """Custom type hwNatPortMapSipPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwNatPortMapSipPort_Type.__name__ = "Unsigned32"
_HwNatPortMapSipPort_Object = MibScalar
hwNatPortMapSipPort = _HwNatPortMapSipPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 11, 1),
    _HwNatPortMapSipPort_Type()
)
hwNatPortMapSipPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatPortMapSipPort.setStatus("current")


class _HwNatPortMapSipAcl_Type(Unsigned32):
    """Custom type hwNatPortMapSipAcl based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 2999),
    )


_HwNatPortMapSipAcl_Type.__name__ = "Unsigned32"
_HwNatPortMapSipAcl_Object = MibScalar
hwNatPortMapSipAcl = _HwNatPortMapSipAcl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 11, 2),
    _HwNatPortMapSipAcl_Type()
)
hwNatPortMapSipAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatPortMapSipAcl.setStatus("current")


class _HwNatPortMapRtspPort_Type(Unsigned32):
    """Custom type hwNatPortMapRtspPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwNatPortMapRtspPort_Type.__name__ = "Unsigned32"
_HwNatPortMapRtspPort_Object = MibScalar
hwNatPortMapRtspPort = _HwNatPortMapRtspPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 11, 3),
    _HwNatPortMapRtspPort_Type()
)
hwNatPortMapRtspPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatPortMapRtspPort.setStatus("current")


class _HwNatPortMapRtspAcl_Type(Unsigned32):
    """Custom type hwNatPortMapRtspAcl based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 2999),
    )


_HwNatPortMapRtspAcl_Type.__name__ = "Unsigned32"
_HwNatPortMapRtspAcl_Object = MibScalar
hwNatPortMapRtspAcl = _HwNatPortMapRtspAcl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 11, 4),
    _HwNatPortMapRtspAcl_Type()
)
hwNatPortMapRtspAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatPortMapRtspAcl.setStatus("current")
_HwNatProtoAgingTime_ObjectIdentity = ObjectIdentity
hwNatProtoAgingTime = _HwNatProtoAgingTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 12)
)
_HwNatSipAgingTime_Type = TimeTicks
_HwNatSipAgingTime_Object = MibScalar
hwNatSipAgingTime = _HwNatSipAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 12, 1),
    _HwNatSipAgingTime_Type()
)
hwNatSipAgingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatSipAgingTime.setStatus("current")
_HwNatSipMediaAgingTime_Type = TimeTicks
_HwNatSipMediaAgingTime_Object = MibScalar
hwNatSipMediaAgingTime = _HwNatSipMediaAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 12, 2),
    _HwNatSipMediaAgingTime_Type()
)
hwNatSipMediaAgingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatSipMediaAgingTime.setStatus("current")
_HwNatRtspAgingTime_Type = TimeTicks
_HwNatRtspAgingTime_Object = MibScalar
hwNatRtspAgingTime = _HwNatRtspAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 12, 3),
    _HwNatRtspAgingTime_Type()
)
hwNatRtspAgingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatRtspAgingTime.setStatus("current")
_HwNatRtspMediaAgingTime_Type = TimeTicks
_HwNatRtspMediaAgingTime_Object = MibScalar
hwNatRtspMediaAgingTime = _HwNatRtspMediaAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 12, 4),
    _HwNatRtspMediaAgingTime_Type()
)
hwNatRtspMediaAgingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatRtspMediaAgingTime.setStatus("current")
_HwNatMap_ObjectIdentity = ObjectIdentity
hwNatMap = _HwNatMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 13)
)
_HwNatMapNumOfEntries_Type = Gauge32
_HwNatMapNumOfEntries_Object = MibScalar
hwNatMapNumOfEntries = _HwNatMapNumOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 13, 1),
    _HwNatMapNumOfEntries_Type()
)
hwNatMapNumOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatMapNumOfEntries.setStatus("current")
_HwNatMapTable_Object = MibTable
hwNatMapTable = _HwNatMapTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 13, 2)
)
if mibBuilder.loadTexts:
    hwNatMapTable.setStatus("current")
_HwNatMapEntry_Object = MibTableRow
hwNatMapEntry = _HwNatMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 13, 2, 1)
)
hwNatMapEntry.setIndexNames(
    (0, "HUAWEI-NAT-EXT-MIB", "hwNatMapIndex"),
)
if mibBuilder.loadTexts:
    hwNatMapEntry.setStatus("current")


class _HwNatMapIndex_Type(Unsigned32):
    """Custom type hwNatMapIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_HwNatMapIndex_Type.__name__ = "Unsigned32"
_HwNatMapIndex_Object = MibTableColumn
hwNatMapIndex = _HwNatMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 13, 2, 1, 1),
    _HwNatMapIndex_Type()
)
hwNatMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwNatMapIndex.setStatus("current")
_HwNatMapProtocol_Type = Unsigned32
_HwNatMapProtocol_Object = MibTableColumn
hwNatMapProtocol = _HwNatMapProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 13, 2, 1, 2),
    _HwNatMapProtocol_Type()
)
hwNatMapProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatMapProtocol.setStatus("current")


class _HwNatMapDestPort_Type(Unsigned32):
    """Custom type hwNatMapDestPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwNatMapDestPort_Type.__name__ = "Unsigned32"
_HwNatMapDestPort_Object = MibTableColumn
hwNatMapDestPort = _HwNatMapDestPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 2, 13, 2, 1, 3),
    _HwNatMapDestPort_Type()
)
hwNatMapDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNatMapDestPort.setStatus("current")
_HwNatExtMIBConformance_ObjectIdentity = ObjectIdentity
hwNatExtMIBConformance = _HwNatExtMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 4)
)
_HwNatExtMIBCompliances_ObjectIdentity = ObjectIdentity
hwNatExtMIBCompliances = _HwNatExtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 4, 1)
)
_HwNatExtMIBGroups_ObjectIdentity = ObjectIdentity
hwNatExtMIBGroups = _HwNatExtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 4, 2)
)

# Managed Objects groups

hwNatBindGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 4, 2, 2)
)
hwNatBindGroup.setObjects(
      *(("HUAWEI-NAT-EXT-MIB", "hwNatAddrBindNumberOfEntries"),
        ("HUAWEI-NAT-EXT-MIB", "hwNatAddrBindId"),
        ("HUAWEI-NAT-EXT-MIB", "hwNatAddrBindSessionCount"),
        ("HUAWEI-NAT-EXT-MIB", "hwNatAddrBindCurrentIdleTime"),
        ("HUAWEI-NAT-EXT-MIB", "hwNatAddrBindInTranslate"),
        ("HUAWEI-NAT-EXT-MIB", "hwNatAddrBindOutTranslate"),
        ("HUAWEI-NAT-EXT-MIB", "hwNatAddrPortBindNumberOfEntries"),
        ("HUAWEI-NAT-EXT-MIB", "hwNatAddrPortBindId"),
        ("HUAWEI-NAT-EXT-MIB", "hwNatAddrPortBindSessionCount"),
        ("HUAWEI-NAT-EXT-MIB", "hwNatAddrPortBindCurrentIdleTime"),
        ("HUAWEI-NAT-EXT-MIB", "hwNatAddrPortBindInTranslate"),
        ("HUAWEI-NAT-EXT-MIB", "hwNatAddrPortBindOutTranslate"),
        ("HUAWEI-NAT-EXT-MIB", "hwNatAddrBindMappedAddr"),
        ("HUAWEI-NAT-EXT-MIB", "hwNatAddrBindMappedVrfName"),
        ("HUAWEI-NAT-EXT-MIB", "hwNatAddrPortBindMappedPort"),
        ("HUAWEI-NAT-EXT-MIB", "hwNatAddrPortBindMappedAddr"),
        ("HUAWEI-NAT-EXT-MIB", "hwNatAddrPortBindMappedVrfName"))
)
if mibBuilder.loadTexts:
    hwNatBindGroup.setStatus("current")

hwNatStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 4, 2, 3)
)
hwNatStatsGroup.setObjects(
      *(("HUAWEI-NAT-EXT-MIB", "hwNatProtocolStatsInTranslate"),
        ("HUAWEI-NAT-EXT-MIB", "hwNatProtocolStatsOutTranslate"),
        ("HUAWEI-NAT-EXT-MIB", "hwNatProtocolStatsRejectCount"),
        ("HUAWEI-NAT-EXT-MIB", "hwNatInterfacePktsIn"),
        ("HUAWEI-NAT-EXT-MIB", "hwNatInterfacePktsOut"))
)
if mibBuilder.loadTexts:
    hwNatStatsGroup.setStatus("current")

hwNatExtIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 4, 2, 4)
)
hwNatExtIfGroup.setObjects(
    ("HUAWEI-NAT-EXT-MIB", "hwNatExtIfName")
)
if mibBuilder.loadTexts:
    hwNatExtIfGroup.setStatus("current")

hwNatAddrPoolGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 4, 2, 5)
)
hwNatAddrPoolGroup.setObjects(
      *(("HUAWEI-NAT-EXT-MIB", "hwNatAddrPoolNumOfEntries"),
        ("HUAWEI-NAT-EXT-MIB", "hwNatAddrPoolStartAddr"),
        ("HUAWEI-NAT-EXT-MIB", "hwNatAddrPoolEndAddr"),
        ("HUAWEI-NAT-EXT-MIB", "hwNatAddrPoolRefTimes"),
        ("HUAWEI-NAT-EXT-MIB", "hwNatAddrPoolRefType"))
)
if mibBuilder.loadTexts:
    hwNatAddrPoolGroup.setStatus("current")

hwNatDnsMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 4, 2, 6)
)
hwNatDnsMapGroup.setObjects(
      *(("HUAWEI-NAT-EXT-MIB", "hwNatDnsMapNumOfEntries"),
        ("HUAWEI-NAT-EXT-MIB", "hwNatDnsMapDomainName"),
        ("HUAWEI-NAT-EXT-MIB", "hwNatDnsMapIpAddr"),
        ("HUAWEI-NAT-EXT-MIB", "hwNatDnsMapPort"),
        ("HUAWEI-NAT-EXT-MIB", "hwNatDnsMapProtocol"))
)
if mibBuilder.loadTexts:
    hwNatDnsMapGroup.setStatus("current")

hwNatOutboundGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 4, 2, 7)
)
hwNatOutboundGroup.setObjects(
      *(("HUAWEI-NAT-EXT-MIB", "hwNatOutboundNumOfEntries"),
        ("HUAWEI-NAT-EXT-MIB", "hwNatOutboundInterface"),
        ("HUAWEI-NAT-EXT-MIB", "hwNatOutboundAclNum"),
        ("HUAWEI-NAT-EXT-MIB", "hwNatOutboundAddr"),
        ("HUAWEI-NAT-EXT-MIB", "hwNatOutboundPat"),
        ("HUAWEI-NAT-EXT-MIB", "hwNatOutboundEasyIp"))
)
if mibBuilder.loadTexts:
    hwNatOutboundGroup.setStatus("current")

hwNatOverlapMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 4, 2, 8)
)
hwNatOverlapMapGroup.setObjects(
      *(("HUAWEI-NAT-EXT-MIB", "hwNatOverlapMapNumOfEntries"),
        ("HUAWEI-NAT-EXT-MIB", "hwNatOverlapMapLapAddr"),
        ("HUAWEI-NAT-EXT-MIB", "hwNatOverlapMapTmpAddr"),
        ("HUAWEI-NAT-EXT-MIB", "hwNatOverlapMapPoolLen"),
        ("HUAWEI-NAT-EXT-MIB", "hwNatOverlapMapVpnName"))
)
if mibBuilder.loadTexts:
    hwNatOverlapMapGroup.setStatus("current")

hwNatServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 4, 2, 9)
)
hwNatServerGroup.setObjects(
      *(("HUAWEI-NAT-EXT-MIB", "hwNatServerNumOfEntries"),
        ("HUAWEI-NAT-EXT-MIB", "hwNatServerInterface"),
        ("HUAWEI-NAT-EXT-MIB", "hwNatServerProtocol"),
        ("HUAWEI-NAT-EXT-MIB", "hwNatServerGlobalAddr"),
        ("HUAWEI-NAT-EXT-MIB", "hwNatServerGlobalPort"),
        ("HUAWEI-NAT-EXT-MIB", "hwNatServerInsideAddr"),
        ("HUAWEI-NAT-EXT-MIB", "hwNatServerInsidePort"),
        ("HUAWEI-NAT-EXT-MIB", "hwNatServerVpnName"))
)
if mibBuilder.loadTexts:
    hwNatServerGroup.setStatus("current")

hwNatStaticGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 4, 2, 10)
)
hwNatStaticGroup.setObjects(
      *(("HUAWEI-NAT-EXT-MIB", "hwNatStaticNumOfEntries"),
        ("HUAWEI-NAT-EXT-MIB", "hwNatStaticInterface"),
        ("HUAWEI-NAT-EXT-MIB", "hwNatStaticProtocol"),
        ("HUAWEI-NAT-EXT-MIB", "hwNatStaticGlobalAddr"),
        ("HUAWEI-NAT-EXT-MIB", "hwNatStaticGlobalPort"),
        ("HUAWEI-NAT-EXT-MIB", "hwNatStaticInsideAddr"),
        ("HUAWEI-NAT-EXT-MIB", "hwNatStaticInsidePort"),
        ("HUAWEI-NAT-EXT-MIB", "hwNatStaticVpnName"),
        ("HUAWEI-NAT-EXT-MIB", "hwNatStaticNetMask"))
)
if mibBuilder.loadTexts:
    hwNatStaticGroup.setStatus("current")

hwNatAlgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 4, 2, 11)
)
hwNatAlgGroup.setObjects(
      *(("HUAWEI-NAT-EXT-MIB", "hwNatAlgFtp"),
        ("HUAWEI-NAT-EXT-MIB", "hwNatAlgDns"),
        ("HUAWEI-NAT-EXT-MIB", "hwNatAlgSip"),
        ("HUAWEI-NAT-EXT-MIB", "hwNatAlgRtsp"))
)
if mibBuilder.loadTexts:
    hwNatAlgGroup.setStatus("current")

hwNatFilterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 4, 2, 12)
)
hwNatFilterGroup.setObjects(
    ("HUAWEI-NAT-EXT-MIB", "hwNatFilterMode")
)
if mibBuilder.loadTexts:
    hwNatFilterGroup.setStatus("current")

hwNatPortMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 4, 2, 13)
)
hwNatPortMapGroup.setObjects(
      *(("HUAWEI-NAT-EXT-MIB", "hwNatPortMapSipPort"),
        ("HUAWEI-NAT-EXT-MIB", "hwNatPortMapSipAcl"),
        ("HUAWEI-NAT-EXT-MIB", "hwNatPortMapRtspPort"),
        ("HUAWEI-NAT-EXT-MIB", "hwNatPortMapRtspAcl"))
)
if mibBuilder.loadTexts:
    hwNatPortMapGroup.setStatus("current")

hwNatAgingTimeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 4, 2, 14)
)
hwNatAgingTimeGroup.setObjects(
      *(("HUAWEI-NAT-EXT-MIB", "hwNatSipAgingTime"),
        ("HUAWEI-NAT-EXT-MIB", "hwNatSipMediaAgingTime"),
        ("HUAWEI-NAT-EXT-MIB", "hwNatRtspAgingTime"),
        ("HUAWEI-NAT-EXT-MIB", "hwNatRtspMediaAgingTime"))
)
if mibBuilder.loadTexts:
    hwNatAgingTimeGroup.setStatus("current")

hwNatMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 4, 2, 15)
)
hwNatMapGroup.setObjects(
      *(("HUAWEI-NAT-EXT-MIB", "hwNatMapNumOfEntries"),
        ("HUAWEI-NAT-EXT-MIB", "hwNatMapProtocol"),
        ("HUAWEI-NAT-EXT-MIB", "hwNatMapDestPort"))
)
if mibBuilder.loadTexts:
    hwNatMapGroup.setStatus("current")


# Notification objects

hwNatPacketDiscard = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 1, 1)
)
hwNatPacketDiscard.setObjects(
    ("HUAWEI-NAT-EXT-MIB", "hwNatExtIfName")
)
if mibBuilder.loadTexts:
    hwNatPacketDiscard.setStatus(
        "current"
    )


# Notifications groups

hwNatNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 4, 2, 1)
)
hwNatNotificationGroup.setObjects(
    ("HUAWEI-NAT-EXT-MIB", "hwNatPacketDiscard")
)
if mibBuilder.loadTexts:
    hwNatNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwNatExtMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 226, 4, 1, 1)
)
if mibBuilder.loadTexts:
    hwNatExtMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-NAT-EXT-MIB",
    **{"NATProtocolType": NATProtocolType,
       "NATFilterMode": NATFilterMode,
       "hwNatExtMIB": hwNatExtMIB,
       "hwNatExtMIBNotifications": hwNatExtMIBNotifications,
       "hwNatPacketDiscard": hwNatPacketDiscard,
       "hwNatExtMIBObjects": hwNatExtMIBObjects,
       "hwNatBind": hwNatBind,
       "hwNatAddrBindNumberOfEntries": hwNatAddrBindNumberOfEntries,
       "hwNatAddrBindTable": hwNatAddrBindTable,
       "hwNatAddrBindEntry": hwNatAddrBindEntry,
       "hwNatAddrBindQueryVrfName": hwNatAddrBindQueryVrfName,
       "hwNatAddrBindQueryAddr": hwNatAddrBindQueryAddr,
       "hwNatAddrBindType": hwNatAddrBindType,
       "hwNatAddrBindMappedVrfName": hwNatAddrBindMappedVrfName,
       "hwNatAddrBindMappedAddr": hwNatAddrBindMappedAddr,
       "hwNatAddrBindId": hwNatAddrBindId,
       "hwNatAddrBindSessionCount": hwNatAddrBindSessionCount,
       "hwNatAddrBindCurrentIdleTime": hwNatAddrBindCurrentIdleTime,
       "hwNatAddrBindInTranslate": hwNatAddrBindInTranslate,
       "hwNatAddrBindOutTranslate": hwNatAddrBindOutTranslate,
       "hwNatAddrPortBindNumberOfEntries": hwNatAddrPortBindNumberOfEntries,
       "hwNatAddrPortBindTable": hwNatAddrPortBindTable,
       "hwNatAddrPortBindEntry": hwNatAddrPortBindEntry,
       "hwNatAddrPortBindQueryVrfName": hwNatAddrPortBindQueryVrfName,
       "hwNatAddrPortBindQueryAddr": hwNatAddrPortBindQueryAddr,
       "hwNatAddrPortBindQueryProtocol": hwNatAddrPortBindQueryProtocol,
       "hwNatAddrPortBindQueryPort": hwNatAddrPortBindQueryPort,
       "hwNatAddrPortBindType": hwNatAddrPortBindType,
       "hwNatAddrPortBindMappedVrfName": hwNatAddrPortBindMappedVrfName,
       "hwNatAddrPortBindMappedAddr": hwNatAddrPortBindMappedAddr,
       "hwNatAddrPortBindMappedPort": hwNatAddrPortBindMappedPort,
       "hwNatAddrPortBindId": hwNatAddrPortBindId,
       "hwNatAddrPortBindSessionCount": hwNatAddrPortBindSessionCount,
       "hwNatAddrPortBindCurrentIdleTime": hwNatAddrPortBindCurrentIdleTime,
       "hwNatAddrPortBindInTranslate": hwNatAddrPortBindInTranslate,
       "hwNatAddrPortBindOutTranslate": hwNatAddrPortBindOutTranslate,
       "hwNatExtIfTable": hwNatExtIfTable,
       "hwNatExtIfEntry": hwNatExtIfEntry,
       "hwNatExtIfName": hwNatExtIfName,
       "hwNatStatistics": hwNatStatistics,
       "hwNatProtocolStatsTable": hwNatProtocolStatsTable,
       "hwNatProtocolStatsEntry": hwNatProtocolStatsEntry,
       "hwNatProtocolStatsName": hwNatProtocolStatsName,
       "hwNatProtocolStatsInTranslate": hwNatProtocolStatsInTranslate,
       "hwNatProtocolStatsOutTranslate": hwNatProtocolStatsOutTranslate,
       "hwNatProtocolStatsRejectCount": hwNatProtocolStatsRejectCount,
       "hwNatInterfaceStatsTable": hwNatInterfaceStatsTable,
       "hwNatInterfaceStatsEntry": hwNatInterfaceStatsEntry,
       "hwNatInterfacePktsIn": hwNatInterfacePktsIn,
       "hwNatInterfacePktsOut": hwNatInterfacePktsOut,
       "hwNATSessionCntTable": hwNATSessionCntTable,
       "hwNATSessionCntEntry": hwNATSessionCntEntry,
       "hwNATSlotIndex": hwNATSlotIndex,
       "hwNATSessionCnt": hwNATSessionCnt,
       "hwNatAddrPool": hwNatAddrPool,
       "hwNatAddrPoolNumOfEntries": hwNatAddrPoolNumOfEntries,
       "hwNatAddrPoolTable": hwNatAddrPoolTable,
       "hwNatAddrPoolEntry": hwNatAddrPoolEntry,
       "hwNatAddrPoolIndex": hwNatAddrPoolIndex,
       "hwNatAddrPoolStartAddr": hwNatAddrPoolStartAddr,
       "hwNatAddrPoolEndAddr": hwNatAddrPoolEndAddr,
       "hwNatAddrPoolRefTimes": hwNatAddrPoolRefTimes,
       "hwNatAddrPoolRefType": hwNatAddrPoolRefType,
       "hwNatDnsMap": hwNatDnsMap,
       "hwNatDnsMapNumOfEntries": hwNatDnsMapNumOfEntries,
       "hwNatDnsMapTable": hwNatDnsMapTable,
       "hwNatDnsMapEntry": hwNatDnsMapEntry,
       "hwNatDnsMapIndex": hwNatDnsMapIndex,
       "hwNatDnsMapDomainName": hwNatDnsMapDomainName,
       "hwNatDnsMapIpAddr": hwNatDnsMapIpAddr,
       "hwNatDnsMapPort": hwNatDnsMapPort,
       "hwNatDnsMapProtocol": hwNatDnsMapProtocol,
       "hwNatOutbound": hwNatOutbound,
       "hwNatOutboundNumOfEntries": hwNatOutboundNumOfEntries,
       "hwNatOutboundTable": hwNatOutboundTable,
       "hwNatOutboundEntry": hwNatOutboundEntry,
       "hwNatOutboundIndex": hwNatOutboundIndex,
       "hwNatOutboundInterface": hwNatOutboundInterface,
       "hwNatOutboundAclNum": hwNatOutboundAclNum,
       "hwNatOutboundAddr": hwNatOutboundAddr,
       "hwNatOutboundPat": hwNatOutboundPat,
       "hwNatOutboundEasyIp": hwNatOutboundEasyIp,
       "hwNatOverlapMap": hwNatOverlapMap,
       "hwNatOverlapMapNumOfEntries": hwNatOverlapMapNumOfEntries,
       "hwNatOverlapMapTable": hwNatOverlapMapTable,
       "hwNatOverlapMapEntry": hwNatOverlapMapEntry,
       "hwNatOverlapMapIndex": hwNatOverlapMapIndex,
       "hwNatOverlapMapLapAddr": hwNatOverlapMapLapAddr,
       "hwNatOverlapMapTmpAddr": hwNatOverlapMapTmpAddr,
       "hwNatOverlapMapPoolLen": hwNatOverlapMapPoolLen,
       "hwNatOverlapMapVpnName": hwNatOverlapMapVpnName,
       "hwNatServer": hwNatServer,
       "hwNatServerNumOfEntries": hwNatServerNumOfEntries,
       "hwNatServerTable": hwNatServerTable,
       "hwNatServerEntry": hwNatServerEntry,
       "hwNatServerIndex": hwNatServerIndex,
       "hwNatServerInterface": hwNatServerInterface,
       "hwNatServerProtocol": hwNatServerProtocol,
       "hwNatServerGlobalAddr": hwNatServerGlobalAddr,
       "hwNatServerGlobalPort": hwNatServerGlobalPort,
       "hwNatServerInsideAddr": hwNatServerInsideAddr,
       "hwNatServerInsidePort": hwNatServerInsidePort,
       "hwNatServerVpnName": hwNatServerVpnName,
       "hwNatStatic": hwNatStatic,
       "hwNatStaticNumOfEntries": hwNatStaticNumOfEntries,
       "hwNatStaticTable": hwNatStaticTable,
       "hwNatStaticEntry": hwNatStaticEntry,
       "hwNatStaticIndex": hwNatStaticIndex,
       "hwNatStaticInterface": hwNatStaticInterface,
       "hwNatStaticProtocol": hwNatStaticProtocol,
       "hwNatStaticGlobalAddr": hwNatStaticGlobalAddr,
       "hwNatStaticGlobalPort": hwNatStaticGlobalPort,
       "hwNatStaticInsideAddr": hwNatStaticInsideAddr,
       "hwNatStaticInsidePort": hwNatStaticInsidePort,
       "hwNatStaticVpnName": hwNatStaticVpnName,
       "hwNatStaticNetMask": hwNatStaticNetMask,
       "hwNatAlg": hwNatAlg,
       "hwNatAlgFtp": hwNatAlgFtp,
       "hwNatAlgDns": hwNatAlgDns,
       "hwNatAlgSip": hwNatAlgSip,
       "hwNatAlgRtsp": hwNatAlgRtsp,
       "hwNatFilter": hwNatFilter,
       "hwNatFilterMode": hwNatFilterMode,
       "hwNatPortMap": hwNatPortMap,
       "hwNatPortMapSipPort": hwNatPortMapSipPort,
       "hwNatPortMapSipAcl": hwNatPortMapSipAcl,
       "hwNatPortMapRtspPort": hwNatPortMapRtspPort,
       "hwNatPortMapRtspAcl": hwNatPortMapRtspAcl,
       "hwNatProtoAgingTime": hwNatProtoAgingTime,
       "hwNatSipAgingTime": hwNatSipAgingTime,
       "hwNatSipMediaAgingTime": hwNatSipMediaAgingTime,
       "hwNatRtspAgingTime": hwNatRtspAgingTime,
       "hwNatRtspMediaAgingTime": hwNatRtspMediaAgingTime,
       "hwNatMap": hwNatMap,
       "hwNatMapNumOfEntries": hwNatMapNumOfEntries,
       "hwNatMapTable": hwNatMapTable,
       "hwNatMapEntry": hwNatMapEntry,
       "hwNatMapIndex": hwNatMapIndex,
       "hwNatMapProtocol": hwNatMapProtocol,
       "hwNatMapDestPort": hwNatMapDestPort,
       "hwNatExtMIBConformance": hwNatExtMIBConformance,
       "hwNatExtMIBCompliances": hwNatExtMIBCompliances,
       "hwNatExtMIBCompliance": hwNatExtMIBCompliance,
       "hwNatExtMIBGroups": hwNatExtMIBGroups,
       "hwNatNotificationGroup": hwNatNotificationGroup,
       "hwNatBindGroup": hwNatBindGroup,
       "hwNatStatsGroup": hwNatStatsGroup,
       "hwNatExtIfGroup": hwNatExtIfGroup,
       "hwNatAddrPoolGroup": hwNatAddrPoolGroup,
       "hwNatDnsMapGroup": hwNatDnsMapGroup,
       "hwNatOutboundGroup": hwNatOutboundGroup,
       "hwNatOverlapMapGroup": hwNatOverlapMapGroup,
       "hwNatServerGroup": hwNatServerGroup,
       "hwNatStaticGroup": hwNatStaticGroup,
       "hwNatAlgGroup": hwNatAlgGroup,
       "hwNatFilterGroup": hwNatFilterGroup,
       "hwNatPortMapGroup": hwNatPortMapGroup,
       "hwNatAgingTimeGroup": hwNatAgingTimeGroup,
       "hwNatMapGroup": hwNatMapGroup}
)
