# SNMP MIB module (CISCO-IETF-NAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IETF-NAT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:01:46 2024
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

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 mib_2) = mibBuilder.importSymbols(
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
    "mib-2")

(DisplayString,
 RowStatus,
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention")


# MODULE-IDENTITY

ciscoIetfNatMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 77)
)
ciscoIetfNatMIB.setRevisions(
        ("2001-03-01 00:00",)
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



# MIB Managed Objects in the order of their OIDs

_CiscoNatMIBObjects_ObjectIdentity = ObjectIdentity
ciscoNatMIBObjects = _CiscoNatMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1)
)
_CnatConfig_ObjectIdentity = ObjectIdentity
cnatConfig = _CnatConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 1)
)
_CnatConfTable_Object = MibTable
cnatConfTable = _CnatConfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cnatConfTable.setStatus("current")
_CnatConfEntry_Object = MibTableRow
cnatConfEntry = _CnatConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 1, 1, 1)
)
cnatConfEntry.setIndexNames(
    (1, "CISCO-IETF-NAT-MIB", "cnatConfName"),
)
if mibBuilder.loadTexts:
    cnatConfEntry.setStatus("current")


class _CnatConfName_Type(SnmpAdminString):
    """Custom type cnatConfName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CnatConfName_Type.__name__ = "SnmpAdminString"
_CnatConfName_Object = MibTableColumn
cnatConfName = _CnatConfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 1, 1, 1, 1),
    _CnatConfName_Type()
)
cnatConfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnatConfName.setStatus("current")


class _CnatConfServiceType_Type(Integer32):
    """Custom type cnatConfServiceType based on Integer32"""
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
        *(("basicNat", 1),
          ("bidirectionalNat", 3),
          ("multihomedNat", 5),
          ("napt", 2),
          ("twiceNat", 4))
    )


_CnatConfServiceType_Type.__name__ = "Integer32"
_CnatConfServiceType_Object = MibTableColumn
cnatConfServiceType = _CnatConfServiceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 1, 1, 1, 2),
    _CnatConfServiceType_Type()
)
cnatConfServiceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnatConfServiceType.setStatus("current")


class _CnatConfTimeoutIcmpIdle_Type(Integer32):
    """Custom type cnatConfTimeoutIcmpIdle based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CnatConfTimeoutIcmpIdle_Type.__name__ = "Integer32"
_CnatConfTimeoutIcmpIdle_Object = MibTableColumn
cnatConfTimeoutIcmpIdle = _CnatConfTimeoutIcmpIdle_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 1, 1, 1, 3),
    _CnatConfTimeoutIcmpIdle_Type()
)
cnatConfTimeoutIcmpIdle.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnatConfTimeoutIcmpIdle.setStatus("current")
if mibBuilder.loadTexts:
    cnatConfTimeoutIcmpIdle.setUnits("seconds")


class _CnatConfTimeoutUdpIdle_Type(Integer32):
    """Custom type cnatConfTimeoutUdpIdle based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CnatConfTimeoutUdpIdle_Type.__name__ = "Integer32"
_CnatConfTimeoutUdpIdle_Object = MibTableColumn
cnatConfTimeoutUdpIdle = _CnatConfTimeoutUdpIdle_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 1, 1, 1, 4),
    _CnatConfTimeoutUdpIdle_Type()
)
cnatConfTimeoutUdpIdle.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnatConfTimeoutUdpIdle.setStatus("current")
if mibBuilder.loadTexts:
    cnatConfTimeoutUdpIdle.setUnits("seconds")


class _CnatConfTimeoutTcpIdle_Type(Integer32):
    """Custom type cnatConfTimeoutTcpIdle based on Integer32"""
    defaultValue = 86400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CnatConfTimeoutTcpIdle_Type.__name__ = "Integer32"
_CnatConfTimeoutTcpIdle_Object = MibTableColumn
cnatConfTimeoutTcpIdle = _CnatConfTimeoutTcpIdle_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 1, 1, 1, 5),
    _CnatConfTimeoutTcpIdle_Type()
)
cnatConfTimeoutTcpIdle.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnatConfTimeoutTcpIdle.setStatus("current")
if mibBuilder.loadTexts:
    cnatConfTimeoutTcpIdle.setUnits("seconds")


class _CnatConfTimeoutTcpNeg_Type(Integer32):
    """Custom type cnatConfTimeoutTcpNeg based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CnatConfTimeoutTcpNeg_Type.__name__ = "Integer32"
_CnatConfTimeoutTcpNeg_Object = MibTableColumn
cnatConfTimeoutTcpNeg = _CnatConfTimeoutTcpNeg_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 1, 1, 1, 6),
    _CnatConfTimeoutTcpNeg_Type()
)
cnatConfTimeoutTcpNeg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnatConfTimeoutTcpNeg.setStatus("current")
if mibBuilder.loadTexts:
    cnatConfTimeoutTcpNeg.setUnits("seconds")


class _CnatConfTimeoutOther_Type(Integer32):
    """Custom type cnatConfTimeoutOther based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CnatConfTimeoutOther_Type.__name__ = "Integer32"
_CnatConfTimeoutOther_Object = MibTableColumn
cnatConfTimeoutOther = _CnatConfTimeoutOther_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 1, 1, 1, 7),
    _CnatConfTimeoutOther_Type()
)
cnatConfTimeoutOther.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnatConfTimeoutOther.setStatus("current")
if mibBuilder.loadTexts:
    cnatConfTimeoutOther.setUnits("seconds")


class _CnatConfMaxBindLeaseTime_Type(Integer32):
    """Custom type cnatConfMaxBindLeaseTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CnatConfMaxBindLeaseTime_Type.__name__ = "Integer32"
_CnatConfMaxBindLeaseTime_Object = MibTableColumn
cnatConfMaxBindLeaseTime = _CnatConfMaxBindLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 1, 1, 1, 8),
    _CnatConfMaxBindLeaseTime_Type()
)
cnatConfMaxBindLeaseTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnatConfMaxBindLeaseTime.setStatus("current")
if mibBuilder.loadTexts:
    cnatConfMaxBindLeaseTime.setUnits("seconds")


class _CnatConfMaxBindIdleTime_Type(Integer32):
    """Custom type cnatConfMaxBindIdleTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CnatConfMaxBindIdleTime_Type.__name__ = "Integer32"
_CnatConfMaxBindIdleTime_Object = MibTableColumn
cnatConfMaxBindIdleTime = _CnatConfMaxBindIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 1, 1, 1, 9),
    _CnatConfMaxBindIdleTime_Type()
)
cnatConfMaxBindIdleTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnatConfMaxBindIdleTime.setStatus("current")
if mibBuilder.loadTexts:
    cnatConfMaxBindIdleTime.setUnits("seconds")


class _CnatConfStorageType_Type(StorageType):
    """Custom type cnatConfStorageType based on StorageType"""


_CnatConfStorageType_Object = MibTableColumn
cnatConfStorageType = _CnatConfStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 1, 1, 1, 10),
    _CnatConfStorageType_Type()
)
cnatConfStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnatConfStorageType.setStatus("current")
_CnatConfStatus_Type = RowStatus
_CnatConfStatus_Object = MibTableColumn
cnatConfStatus = _CnatConfStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 1, 1, 1, 11),
    _CnatConfStatus_Type()
)
cnatConfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnatConfStatus.setStatus("current")
_CnatConfStaticAddrMapTable_Object = MibTable
cnatConfStaticAddrMapTable = _CnatConfStaticAddrMapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cnatConfStaticAddrMapTable.setStatus("current")
_CnatConfStaticAddrMapEntry_Object = MibTableRow
cnatConfStaticAddrMapEntry = _CnatConfStaticAddrMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 1, 2, 1)
)
cnatConfStaticAddrMapEntry.setIndexNames(
    (0, "CISCO-IETF-NAT-MIB", "cnatConfName"),
    (0, "CISCO-IETF-NAT-MIB", "cnatConfStaticAddrMapName"),
)
if mibBuilder.loadTexts:
    cnatConfStaticAddrMapEntry.setStatus("current")


class _CnatConfStaticAddrMapName_Type(SnmpAdminString):
    """Custom type cnatConfStaticAddrMapName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CnatConfStaticAddrMapName_Type.__name__ = "SnmpAdminString"
_CnatConfStaticAddrMapName_Object = MibTableColumn
cnatConfStaticAddrMapName = _CnatConfStaticAddrMapName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 1, 2, 1, 1),
    _CnatConfStaticAddrMapName_Type()
)
cnatConfStaticAddrMapName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnatConfStaticAddrMapName.setStatus("current")


class _CnatConfStaticAddrMapType_Type(Integer32):
    """Custom type cnatConfStaticAddrMapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("inbound", 1),
          ("outbound", 2))
    )


_CnatConfStaticAddrMapType_Type.__name__ = "Integer32"
_CnatConfStaticAddrMapType_Object = MibTableColumn
cnatConfStaticAddrMapType = _CnatConfStaticAddrMapType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 1, 2, 1, 2),
    _CnatConfStaticAddrMapType_Type()
)
cnatConfStaticAddrMapType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnatConfStaticAddrMapType.setStatus("current")
_CnatConfStaticLocalAddrFrom_Type = IpAddress
_CnatConfStaticLocalAddrFrom_Object = MibTableColumn
cnatConfStaticLocalAddrFrom = _CnatConfStaticLocalAddrFrom_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 1, 2, 1, 3),
    _CnatConfStaticLocalAddrFrom_Type()
)
cnatConfStaticLocalAddrFrom.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnatConfStaticLocalAddrFrom.setStatus("current")
_CnatConfStaticLocalAddrTo_Type = IpAddress
_CnatConfStaticLocalAddrTo_Object = MibTableColumn
cnatConfStaticLocalAddrTo = _CnatConfStaticLocalAddrTo_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 1, 2, 1, 4),
    _CnatConfStaticLocalAddrTo_Type()
)
cnatConfStaticLocalAddrTo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnatConfStaticLocalAddrTo.setStatus("current")


class _CnatConfStaticLocalPortFrom_Type(Integer32):
    """Custom type cnatConfStaticLocalPortFrom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CnatConfStaticLocalPortFrom_Type.__name__ = "Integer32"
_CnatConfStaticLocalPortFrom_Object = MibTableColumn
cnatConfStaticLocalPortFrom = _CnatConfStaticLocalPortFrom_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 1, 2, 1, 5),
    _CnatConfStaticLocalPortFrom_Type()
)
cnatConfStaticLocalPortFrom.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnatConfStaticLocalPortFrom.setStatus("current")


class _CnatConfStaticLocalPortTo_Type(Integer32):
    """Custom type cnatConfStaticLocalPortTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CnatConfStaticLocalPortTo_Type.__name__ = "Integer32"
_CnatConfStaticLocalPortTo_Object = MibTableColumn
cnatConfStaticLocalPortTo = _CnatConfStaticLocalPortTo_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 1, 2, 1, 6),
    _CnatConfStaticLocalPortTo_Type()
)
cnatConfStaticLocalPortTo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnatConfStaticLocalPortTo.setStatus("current")
_CnatConfStaticGlobalAddrFrom_Type = IpAddress
_CnatConfStaticGlobalAddrFrom_Object = MibTableColumn
cnatConfStaticGlobalAddrFrom = _CnatConfStaticGlobalAddrFrom_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 1, 2, 1, 7),
    _CnatConfStaticGlobalAddrFrom_Type()
)
cnatConfStaticGlobalAddrFrom.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnatConfStaticGlobalAddrFrom.setStatus("current")
_CnatConfStaticGlobalAddrTo_Type = IpAddress
_CnatConfStaticGlobalAddrTo_Object = MibTableColumn
cnatConfStaticGlobalAddrTo = _CnatConfStaticGlobalAddrTo_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 1, 2, 1, 8),
    _CnatConfStaticGlobalAddrTo_Type()
)
cnatConfStaticGlobalAddrTo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnatConfStaticGlobalAddrTo.setStatus("current")


class _CnatConfStaticGlobalPortFrom_Type(Integer32):
    """Custom type cnatConfStaticGlobalPortFrom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CnatConfStaticGlobalPortFrom_Type.__name__ = "Integer32"
_CnatConfStaticGlobalPortFrom_Object = MibTableColumn
cnatConfStaticGlobalPortFrom = _CnatConfStaticGlobalPortFrom_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 1, 2, 1, 9),
    _CnatConfStaticGlobalPortFrom_Type()
)
cnatConfStaticGlobalPortFrom.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnatConfStaticGlobalPortFrom.setStatus("current")


class _CnatConfStaticGlobalPortTo_Type(Integer32):
    """Custom type cnatConfStaticGlobalPortTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CnatConfStaticGlobalPortTo_Type.__name__ = "Integer32"
_CnatConfStaticGlobalPortTo_Object = MibTableColumn
cnatConfStaticGlobalPortTo = _CnatConfStaticGlobalPortTo_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 1, 2, 1, 10),
    _CnatConfStaticGlobalPortTo_Type()
)
cnatConfStaticGlobalPortTo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnatConfStaticGlobalPortTo.setStatus("current")


class _CnatConfStaticProtocol_Type(Bits):
    """Custom type cnatConfStaticProtocol based on Bits"""
    namedValues = NamedValues(
        *(("all", 0),
          ("icmp", 2),
          ("other", 1),
          ("tcp", 4),
          ("udp", 3))
    )

_CnatConfStaticProtocol_Type.__name__ = "Bits"
_CnatConfStaticProtocol_Object = MibTableColumn
cnatConfStaticProtocol = _CnatConfStaticProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 1, 2, 1, 11),
    _CnatConfStaticProtocol_Type()
)
cnatConfStaticProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnatConfStaticProtocol.setStatus("current")


class _CnatConfStaticAddrMapStorageType_Type(StorageType):
    """Custom type cnatConfStaticAddrMapStorageType based on StorageType"""


_CnatConfStaticAddrMapStorageType_Object = MibTableColumn
cnatConfStaticAddrMapStorageType = _CnatConfStaticAddrMapStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 1, 2, 1, 12),
    _CnatConfStaticAddrMapStorageType_Type()
)
cnatConfStaticAddrMapStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnatConfStaticAddrMapStorageType.setStatus("current")
_CnatConfStaticAddrMapStatus_Type = RowStatus
_CnatConfStaticAddrMapStatus_Object = MibTableColumn
cnatConfStaticAddrMapStatus = _CnatConfStaticAddrMapStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 1, 2, 1, 13),
    _CnatConfStaticAddrMapStatus_Type()
)
cnatConfStaticAddrMapStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnatConfStaticAddrMapStatus.setStatus("current")
_CnatConfDynAddrMapTable_Object = MibTable
cnatConfDynAddrMapTable = _CnatConfDynAddrMapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cnatConfDynAddrMapTable.setStatus("current")
_CnatConfDynAddrMapEntry_Object = MibTableRow
cnatConfDynAddrMapEntry = _CnatConfDynAddrMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 1, 3, 1)
)
cnatConfDynAddrMapEntry.setIndexNames(
    (0, "CISCO-IETF-NAT-MIB", "cnatConfName"),
    (0, "CISCO-IETF-NAT-MIB", "cnatConfDynAddrMapName"),
)
if mibBuilder.loadTexts:
    cnatConfDynAddrMapEntry.setStatus("current")


class _CnatConfDynAddrMapName_Type(SnmpAdminString):
    """Custom type cnatConfDynAddrMapName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CnatConfDynAddrMapName_Type.__name__ = "SnmpAdminString"
_CnatConfDynAddrMapName_Object = MibTableColumn
cnatConfDynAddrMapName = _CnatConfDynAddrMapName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 1, 3, 1, 1),
    _CnatConfDynAddrMapName_Type()
)
cnatConfDynAddrMapName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnatConfDynAddrMapName.setStatus("current")


class _CnatConfDynAddressMapType_Type(Integer32):
    """Custom type cnatConfDynAddressMapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("inbound", 1),
          ("outbound", 2))
    )


_CnatConfDynAddressMapType_Type.__name__ = "Integer32"
_CnatConfDynAddressMapType_Object = MibTableColumn
cnatConfDynAddressMapType = _CnatConfDynAddressMapType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 1, 3, 1, 2),
    _CnatConfDynAddressMapType_Type()
)
cnatConfDynAddressMapType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnatConfDynAddressMapType.setStatus("current")
_CnatConfDynLocalAddrFrom_Type = IpAddress
_CnatConfDynLocalAddrFrom_Object = MibTableColumn
cnatConfDynLocalAddrFrom = _CnatConfDynLocalAddrFrom_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 1, 3, 1, 3),
    _CnatConfDynLocalAddrFrom_Type()
)
cnatConfDynLocalAddrFrom.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnatConfDynLocalAddrFrom.setStatus("current")
_CnatConfDynLocalAddrTo_Type = IpAddress
_CnatConfDynLocalAddrTo_Object = MibTableColumn
cnatConfDynLocalAddrTo = _CnatConfDynLocalAddrTo_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 1, 3, 1, 4),
    _CnatConfDynLocalAddrTo_Type()
)
cnatConfDynLocalAddrTo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnatConfDynLocalAddrTo.setStatus("current")


class _CnatConfDynLocalPortFrom_Type(Integer32):
    """Custom type cnatConfDynLocalPortFrom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CnatConfDynLocalPortFrom_Type.__name__ = "Integer32"
_CnatConfDynLocalPortFrom_Object = MibTableColumn
cnatConfDynLocalPortFrom = _CnatConfDynLocalPortFrom_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 1, 3, 1, 5),
    _CnatConfDynLocalPortFrom_Type()
)
cnatConfDynLocalPortFrom.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnatConfDynLocalPortFrom.setStatus("current")


class _CnatConfDynLocalPortTo_Type(Integer32):
    """Custom type cnatConfDynLocalPortTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CnatConfDynLocalPortTo_Type.__name__ = "Integer32"
_CnatConfDynLocalPortTo_Object = MibTableColumn
cnatConfDynLocalPortTo = _CnatConfDynLocalPortTo_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 1, 3, 1, 6),
    _CnatConfDynLocalPortTo_Type()
)
cnatConfDynLocalPortTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnatConfDynLocalPortTo.setStatus("current")
_CnatConfDynGlobalAddrFrom_Type = IpAddress
_CnatConfDynGlobalAddrFrom_Object = MibTableColumn
cnatConfDynGlobalAddrFrom = _CnatConfDynGlobalAddrFrom_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 1, 3, 1, 7),
    _CnatConfDynGlobalAddrFrom_Type()
)
cnatConfDynGlobalAddrFrom.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnatConfDynGlobalAddrFrom.setStatus("current")
_CnatConfDynGlobalAddrTo_Type = IpAddress
_CnatConfDynGlobalAddrTo_Object = MibTableColumn
cnatConfDynGlobalAddrTo = _CnatConfDynGlobalAddrTo_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 1, 3, 1, 8),
    _CnatConfDynGlobalAddrTo_Type()
)
cnatConfDynGlobalAddrTo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnatConfDynGlobalAddrTo.setStatus("current")


class _CnatConfDynGlobalPortFrom_Type(Integer32):
    """Custom type cnatConfDynGlobalPortFrom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CnatConfDynGlobalPortFrom_Type.__name__ = "Integer32"
_CnatConfDynGlobalPortFrom_Object = MibTableColumn
cnatConfDynGlobalPortFrom = _CnatConfDynGlobalPortFrom_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 1, 3, 1, 9),
    _CnatConfDynGlobalPortFrom_Type()
)
cnatConfDynGlobalPortFrom.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnatConfDynGlobalPortFrom.setStatus("current")


class _CnatConfDynGlobalPortTo_Type(Integer32):
    """Custom type cnatConfDynGlobalPortTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CnatConfDynGlobalPortTo_Type.__name__ = "Integer32"
_CnatConfDynGlobalPortTo_Object = MibTableColumn
cnatConfDynGlobalPortTo = _CnatConfDynGlobalPortTo_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 1, 3, 1, 10),
    _CnatConfDynGlobalPortTo_Type()
)
cnatConfDynGlobalPortTo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnatConfDynGlobalPortTo.setStatus("current")


class _CnatConfDynProtocol_Type(Bits):
    """Custom type cnatConfDynProtocol based on Bits"""
    namedValues = NamedValues(
        *(("all", 0),
          ("icmp", 2),
          ("other", 1),
          ("tcp", 4),
          ("udp", 3))
    )

_CnatConfDynProtocol_Type.__name__ = "Bits"
_CnatConfDynProtocol_Object = MibTableColumn
cnatConfDynProtocol = _CnatConfDynProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 1, 3, 1, 11),
    _CnatConfDynProtocol_Type()
)
cnatConfDynProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnatConfDynProtocol.setStatus("current")


class _CnatConfDynAddrMapStorageType_Type(StorageType):
    """Custom type cnatConfDynAddrMapStorageType based on StorageType"""


_CnatConfDynAddrMapStorageType_Object = MibTableColumn
cnatConfDynAddrMapStorageType = _CnatConfDynAddrMapStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 1, 3, 1, 12),
    _CnatConfDynAddrMapStorageType_Type()
)
cnatConfDynAddrMapStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnatConfDynAddrMapStorageType.setStatus("current")
_CnatConfDynAddrMapStatus_Type = RowStatus
_CnatConfDynAddrMapStatus_Object = MibTableColumn
cnatConfDynAddrMapStatus = _CnatConfDynAddrMapStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 1, 3, 1, 13),
    _CnatConfDynAddrMapStatus_Type()
)
cnatConfDynAddrMapStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnatConfDynAddrMapStatus.setStatus("current")
_CnatInterfaceTable_Object = MibTable
cnatInterfaceTable = _CnatInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cnatInterfaceTable.setStatus("current")
_CnatInterfaceEntry_Object = MibTableRow
cnatInterfaceEntry = _CnatInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 1, 4, 1)
)
cnatInterfaceEntry.setIndexNames(
    (0, "CISCO-IETF-NAT-MIB", "cnatInterfaceIndex"),
)
if mibBuilder.loadTexts:
    cnatInterfaceEntry.setStatus("current")
_CnatInterfaceIndex_Type = InterfaceIndex
_CnatInterfaceIndex_Object = MibTableColumn
cnatInterfaceIndex = _CnatInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 1, 4, 1, 1),
    _CnatInterfaceIndex_Type()
)
cnatInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnatInterfaceIndex.setStatus("current")


class _CnatInterfaceRealm_Type(Integer32):
    """Custom type cnatInterfaceRealm based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("private", 1),
          ("public", 2))
    )


_CnatInterfaceRealm_Type.__name__ = "Integer32"
_CnatInterfaceRealm_Object = MibTableColumn
cnatInterfaceRealm = _CnatInterfaceRealm_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 1, 4, 1, 2),
    _CnatInterfaceRealm_Type()
)
cnatInterfaceRealm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnatInterfaceRealm.setStatus("current")


class _CnatInterfaceStorageType_Type(StorageType):
    """Custom type cnatInterfaceStorageType based on StorageType"""


_CnatInterfaceStorageType_Object = MibTableColumn
cnatInterfaceStorageType = _CnatInterfaceStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 1, 4, 1, 3),
    _CnatInterfaceStorageType_Type()
)
cnatInterfaceStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnatInterfaceStorageType.setStatus("current")
_CnatInterfaceStatus_Type = RowStatus
_CnatInterfaceStatus_Object = MibTableColumn
cnatInterfaceStatus = _CnatInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 1, 4, 1, 4),
    _CnatInterfaceStatus_Type()
)
cnatInterfaceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnatInterfaceStatus.setStatus("current")
_CnatBind_ObjectIdentity = ObjectIdentity
cnatBind = _CnatBind_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 2)
)
_CnatAddrBindNumberOfEntries_Type = Gauge32
_CnatAddrBindNumberOfEntries_Object = MibScalar
cnatAddrBindNumberOfEntries = _CnatAddrBindNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 2, 1),
    _CnatAddrBindNumberOfEntries_Type()
)
cnatAddrBindNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnatAddrBindNumberOfEntries.setStatus("current")
_CnatAddrBindTable_Object = MibTable
cnatAddrBindTable = _CnatAddrBindTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cnatAddrBindTable.setStatus("current")
_CnatAddrBindEntry_Object = MibTableRow
cnatAddrBindEntry = _CnatAddrBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 2, 2, 1)
)
cnatAddrBindEntry.setIndexNames(
    (0, "CISCO-IETF-NAT-MIB", "cnatAddrBindLocalAddr"),
)
if mibBuilder.loadTexts:
    cnatAddrBindEntry.setStatus("current")
_CnatAddrBindLocalAddr_Type = IpAddress
_CnatAddrBindLocalAddr_Object = MibTableColumn
cnatAddrBindLocalAddr = _CnatAddrBindLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 2, 2, 1, 1),
    _CnatAddrBindLocalAddr_Type()
)
cnatAddrBindLocalAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnatAddrBindLocalAddr.setStatus("current")
_CnatAddrBindGlobalAddr_Type = IpAddress
_CnatAddrBindGlobalAddr_Object = MibTableColumn
cnatAddrBindGlobalAddr = _CnatAddrBindGlobalAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 2, 2, 1, 2),
    _CnatAddrBindGlobalAddr_Type()
)
cnatAddrBindGlobalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnatAddrBindGlobalAddr.setStatus("current")
_CnatAddrBindId_Type = Unsigned32
_CnatAddrBindId_Object = MibTableColumn
cnatAddrBindId = _CnatAddrBindId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 2, 2, 1, 3),
    _CnatAddrBindId_Type()
)
cnatAddrBindId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnatAddrBindId.setStatus("current")


class _CnatAddrBindDirection_Type(Integer32):
    """Custom type cnatAddrBindDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("biDirectional", 2),
          ("uniDirectional", 1))
    )


_CnatAddrBindDirection_Type.__name__ = "Integer32"
_CnatAddrBindDirection_Object = MibTableColumn
cnatAddrBindDirection = _CnatAddrBindDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 2, 2, 1, 4),
    _CnatAddrBindDirection_Type()
)
cnatAddrBindDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnatAddrBindDirection.setStatus("current")


class _CnatAddrBindType_Type(Integer32):
    """Custom type cnatAddrBindType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_CnatAddrBindType_Type.__name__ = "Integer32"
_CnatAddrBindType_Object = MibTableColumn
cnatAddrBindType = _CnatAddrBindType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 2, 2, 1, 5),
    _CnatAddrBindType_Type()
)
cnatAddrBindType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnatAddrBindType.setStatus("current")


class _CnatAddrBindConfName_Type(SnmpAdminString):
    """Custom type cnatAddrBindConfName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CnatAddrBindConfName_Type.__name__ = "SnmpAdminString"
_CnatAddrBindConfName_Object = MibTableColumn
cnatAddrBindConfName = _CnatAddrBindConfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 2, 2, 1, 6),
    _CnatAddrBindConfName_Type()
)
cnatAddrBindConfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnatAddrBindConfName.setStatus("current")
_CnatAddrBindSessionCount_Type = Gauge32
_CnatAddrBindSessionCount_Object = MibTableColumn
cnatAddrBindSessionCount = _CnatAddrBindSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 2, 2, 1, 7),
    _CnatAddrBindSessionCount_Type()
)
cnatAddrBindSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnatAddrBindSessionCount.setStatus("current")
_CnatAddrBindCurrentIdleTime_Type = TimeTicks
_CnatAddrBindCurrentIdleTime_Object = MibTableColumn
cnatAddrBindCurrentIdleTime = _CnatAddrBindCurrentIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 2, 2, 1, 8),
    _CnatAddrBindCurrentIdleTime_Type()
)
cnatAddrBindCurrentIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnatAddrBindCurrentIdleTime.setStatus("current")
_CnatAddrBindInTranslate_Type = Counter32
_CnatAddrBindInTranslate_Object = MibTableColumn
cnatAddrBindInTranslate = _CnatAddrBindInTranslate_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 2, 2, 1, 9),
    _CnatAddrBindInTranslate_Type()
)
cnatAddrBindInTranslate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnatAddrBindInTranslate.setStatus("current")
_CnatAddrBindOutTranslate_Type = Counter32
_CnatAddrBindOutTranslate_Object = MibTableColumn
cnatAddrBindOutTranslate = _CnatAddrBindOutTranslate_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 2, 2, 1, 10),
    _CnatAddrBindOutTranslate_Type()
)
cnatAddrBindOutTranslate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnatAddrBindOutTranslate.setStatus("current")
_CnatAddrPortBindNumberOfEntries_Type = Gauge32
_CnatAddrPortBindNumberOfEntries_Object = MibScalar
cnatAddrPortBindNumberOfEntries = _CnatAddrPortBindNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 2, 3),
    _CnatAddrPortBindNumberOfEntries_Type()
)
cnatAddrPortBindNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnatAddrPortBindNumberOfEntries.setStatus("current")
_CnatAddrPortBindTable_Object = MibTable
cnatAddrPortBindTable = _CnatAddrPortBindTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 2, 4)
)
if mibBuilder.loadTexts:
    cnatAddrPortBindTable.setStatus("current")
_CnatAddrPortBindEntry_Object = MibTableRow
cnatAddrPortBindEntry = _CnatAddrPortBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 2, 4, 1)
)
cnatAddrPortBindEntry.setIndexNames(
    (0, "CISCO-IETF-NAT-MIB", "cnatAddrPortBindLocalAddr"),
    (0, "CISCO-IETF-NAT-MIB", "cnatAddrPortBindLocalPort"),
    (0, "CISCO-IETF-NAT-MIB", "cnatAddrPortBindProtocol"),
)
if mibBuilder.loadTexts:
    cnatAddrPortBindEntry.setStatus("current")
_CnatAddrPortBindLocalAddr_Type = IpAddress
_CnatAddrPortBindLocalAddr_Object = MibTableColumn
cnatAddrPortBindLocalAddr = _CnatAddrPortBindLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 2, 4, 1, 1),
    _CnatAddrPortBindLocalAddr_Type()
)
cnatAddrPortBindLocalAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnatAddrPortBindLocalAddr.setStatus("current")


class _CnatAddrPortBindLocalPort_Type(Integer32):
    """Custom type cnatAddrPortBindLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CnatAddrPortBindLocalPort_Type.__name__ = "Integer32"
_CnatAddrPortBindLocalPort_Object = MibTableColumn
cnatAddrPortBindLocalPort = _CnatAddrPortBindLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 2, 4, 1, 2),
    _CnatAddrPortBindLocalPort_Type()
)
cnatAddrPortBindLocalPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnatAddrPortBindLocalPort.setStatus("current")


class _CnatAddrPortBindProtocol_Type(Bits):
    """Custom type cnatAddrPortBindProtocol based on Bits"""
    namedValues = NamedValues(
        *(("all", 0),
          ("icmp", 2),
          ("other", 1),
          ("tcp", 4),
          ("udp", 3))
    )

_CnatAddrPortBindProtocol_Type.__name__ = "Bits"
_CnatAddrPortBindProtocol_Object = MibTableColumn
cnatAddrPortBindProtocol = _CnatAddrPortBindProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 2, 4, 1, 3),
    _CnatAddrPortBindProtocol_Type()
)
cnatAddrPortBindProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnatAddrPortBindProtocol.setStatus("current")
_CnatAddrPortBindGlobalAddr_Type = IpAddress
_CnatAddrPortBindGlobalAddr_Object = MibTableColumn
cnatAddrPortBindGlobalAddr = _CnatAddrPortBindGlobalAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 2, 4, 1, 4),
    _CnatAddrPortBindGlobalAddr_Type()
)
cnatAddrPortBindGlobalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnatAddrPortBindGlobalAddr.setStatus("current")


class _CnatAddrPortBindGlobalPort_Type(Integer32):
    """Custom type cnatAddrPortBindGlobalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CnatAddrPortBindGlobalPort_Type.__name__ = "Integer32"
_CnatAddrPortBindGlobalPort_Object = MibTableColumn
cnatAddrPortBindGlobalPort = _CnatAddrPortBindGlobalPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 2, 4, 1, 5),
    _CnatAddrPortBindGlobalPort_Type()
)
cnatAddrPortBindGlobalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnatAddrPortBindGlobalPort.setStatus("current")
_CnatAddrPortBindId_Type = Unsigned32
_CnatAddrPortBindId_Object = MibTableColumn
cnatAddrPortBindId = _CnatAddrPortBindId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 2, 4, 1, 6),
    _CnatAddrPortBindId_Type()
)
cnatAddrPortBindId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnatAddrPortBindId.setStatus("current")


class _CnatAddrPortBindDirection_Type(Integer32):
    """Custom type cnatAddrPortBindDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("biDirectional", 2),
          ("uniDirectional", 1))
    )


_CnatAddrPortBindDirection_Type.__name__ = "Integer32"
_CnatAddrPortBindDirection_Object = MibTableColumn
cnatAddrPortBindDirection = _CnatAddrPortBindDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 2, 4, 1, 7),
    _CnatAddrPortBindDirection_Type()
)
cnatAddrPortBindDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnatAddrPortBindDirection.setStatus("current")


class _CnatAddrPortBindType_Type(Integer32):
    """Custom type cnatAddrPortBindType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_CnatAddrPortBindType_Type.__name__ = "Integer32"
_CnatAddrPortBindType_Object = MibTableColumn
cnatAddrPortBindType = _CnatAddrPortBindType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 2, 4, 1, 8),
    _CnatAddrPortBindType_Type()
)
cnatAddrPortBindType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnatAddrPortBindType.setStatus("current")
_CnatAddrPortBindConfName_Type = SnmpAdminString
_CnatAddrPortBindConfName_Object = MibTableColumn
cnatAddrPortBindConfName = _CnatAddrPortBindConfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 2, 4, 1, 9),
    _CnatAddrPortBindConfName_Type()
)
cnatAddrPortBindConfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnatAddrPortBindConfName.setStatus("current")
_CnatAddrPortBindSessionCount_Type = Gauge32
_CnatAddrPortBindSessionCount_Object = MibTableColumn
cnatAddrPortBindSessionCount = _CnatAddrPortBindSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 2, 4, 1, 10),
    _CnatAddrPortBindSessionCount_Type()
)
cnatAddrPortBindSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnatAddrPortBindSessionCount.setStatus("current")
_CnatAddrPortBindCurrentIdleTime_Type = TimeTicks
_CnatAddrPortBindCurrentIdleTime_Object = MibTableColumn
cnatAddrPortBindCurrentIdleTime = _CnatAddrPortBindCurrentIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 2, 4, 1, 11),
    _CnatAddrPortBindCurrentIdleTime_Type()
)
cnatAddrPortBindCurrentIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnatAddrPortBindCurrentIdleTime.setStatus("current")
_CnatAddrPortBindInTranslate_Type = Counter32
_CnatAddrPortBindInTranslate_Object = MibTableColumn
cnatAddrPortBindInTranslate = _CnatAddrPortBindInTranslate_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 2, 4, 1, 12),
    _CnatAddrPortBindInTranslate_Type()
)
cnatAddrPortBindInTranslate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnatAddrPortBindInTranslate.setStatus("current")
_CnatAddrPortBindOutTranslate_Type = Counter32
_CnatAddrPortBindOutTranslate_Object = MibTableColumn
cnatAddrPortBindOutTranslate = _CnatAddrPortBindOutTranslate_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 2, 4, 1, 13),
    _CnatAddrPortBindOutTranslate_Type()
)
cnatAddrPortBindOutTranslate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnatAddrPortBindOutTranslate.setStatus("current")
_CnatSessionTable_Object = MibTable
cnatSessionTable = _CnatSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 2, 5)
)
if mibBuilder.loadTexts:
    cnatSessionTable.setStatus("current")
_CnatSessionEntry_Object = MibTableRow
cnatSessionEntry = _CnatSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 2, 5, 1)
)
cnatSessionEntry.setIndexNames(
    (0, "CISCO-IETF-NAT-MIB", "cnatSessionBindId"),
    (0, "CISCO-IETF-NAT-MIB", "cnatSessionId"),
)
if mibBuilder.loadTexts:
    cnatSessionEntry.setStatus("current")
_CnatSessionBindId_Type = Unsigned32
_CnatSessionBindId_Object = MibTableColumn
cnatSessionBindId = _CnatSessionBindId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 2, 5, 1, 1),
    _CnatSessionBindId_Type()
)
cnatSessionBindId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnatSessionBindId.setStatus("current")
_CnatSessionId_Type = Unsigned32
_CnatSessionId_Object = MibTableColumn
cnatSessionId = _CnatSessionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 2, 5, 1, 2),
    _CnatSessionId_Type()
)
cnatSessionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnatSessionId.setStatus("current")


class _CnatSessionDirection_Type(Integer32):
    """Custom type cnatSessionDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )


_CnatSessionDirection_Type.__name__ = "Integer32"
_CnatSessionDirection_Object = MibTableColumn
cnatSessionDirection = _CnatSessionDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 2, 5, 1, 3),
    _CnatSessionDirection_Type()
)
cnatSessionDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnatSessionDirection.setStatus("current")
_CnatSessionUpTime_Type = TimeTicks
_CnatSessionUpTime_Object = MibTableColumn
cnatSessionUpTime = _CnatSessionUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 2, 5, 1, 4),
    _CnatSessionUpTime_Type()
)
cnatSessionUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnatSessionUpTime.setStatus("current")
_CnatSessionProtocolType_Type = NATProtocolType
_CnatSessionProtocolType_Object = MibTableColumn
cnatSessionProtocolType = _CnatSessionProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 2, 5, 1, 5),
    _CnatSessionProtocolType_Type()
)
cnatSessionProtocolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnatSessionProtocolType.setStatus("current")
_CnatSessionOrigPrivateAddr_Type = IpAddress
_CnatSessionOrigPrivateAddr_Object = MibTableColumn
cnatSessionOrigPrivateAddr = _CnatSessionOrigPrivateAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 2, 5, 1, 6),
    _CnatSessionOrigPrivateAddr_Type()
)
cnatSessionOrigPrivateAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnatSessionOrigPrivateAddr.setStatus("current")
_CnatSessionTransPrivateAddr_Type = IpAddress
_CnatSessionTransPrivateAddr_Object = MibTableColumn
cnatSessionTransPrivateAddr = _CnatSessionTransPrivateAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 2, 5, 1, 7),
    _CnatSessionTransPrivateAddr_Type()
)
cnatSessionTransPrivateAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnatSessionTransPrivateAddr.setStatus("current")


class _CnatSessionOrigPrivatePort_Type(Integer32):
    """Custom type cnatSessionOrigPrivatePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CnatSessionOrigPrivatePort_Type.__name__ = "Integer32"
_CnatSessionOrigPrivatePort_Object = MibTableColumn
cnatSessionOrigPrivatePort = _CnatSessionOrigPrivatePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 2, 5, 1, 8),
    _CnatSessionOrigPrivatePort_Type()
)
cnatSessionOrigPrivatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnatSessionOrigPrivatePort.setStatus("current")


class _CnatSessionTransPrivatePort_Type(Integer32):
    """Custom type cnatSessionTransPrivatePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CnatSessionTransPrivatePort_Type.__name__ = "Integer32"
_CnatSessionTransPrivatePort_Object = MibTableColumn
cnatSessionTransPrivatePort = _CnatSessionTransPrivatePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 2, 5, 1, 9),
    _CnatSessionTransPrivatePort_Type()
)
cnatSessionTransPrivatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnatSessionTransPrivatePort.setStatus("current")
_CnatSessionOrigPublicAddr_Type = IpAddress
_CnatSessionOrigPublicAddr_Object = MibTableColumn
cnatSessionOrigPublicAddr = _CnatSessionOrigPublicAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 2, 5, 1, 10),
    _CnatSessionOrigPublicAddr_Type()
)
cnatSessionOrigPublicAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnatSessionOrigPublicAddr.setStatus("current")
_CnatSessionTransPublicAddr_Type = IpAddress
_CnatSessionTransPublicAddr_Object = MibTableColumn
cnatSessionTransPublicAddr = _CnatSessionTransPublicAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 2, 5, 1, 11),
    _CnatSessionTransPublicAddr_Type()
)
cnatSessionTransPublicAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnatSessionTransPublicAddr.setStatus("current")


class _CnatSessionOrigPublicPort_Type(Integer32):
    """Custom type cnatSessionOrigPublicPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CnatSessionOrigPublicPort_Type.__name__ = "Integer32"
_CnatSessionOrigPublicPort_Object = MibTableColumn
cnatSessionOrigPublicPort = _CnatSessionOrigPublicPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 2, 5, 1, 12),
    _CnatSessionOrigPublicPort_Type()
)
cnatSessionOrigPublicPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnatSessionOrigPublicPort.setStatus("current")


class _CnatSessionTransPublicPort_Type(Integer32):
    """Custom type cnatSessionTransPublicPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CnatSessionTransPublicPort_Type.__name__ = "Integer32"
_CnatSessionTransPublicPort_Object = MibTableColumn
cnatSessionTransPublicPort = _CnatSessionTransPublicPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 2, 5, 1, 13),
    _CnatSessionTransPublicPort_Type()
)
cnatSessionTransPublicPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnatSessionTransPublicPort.setStatus("current")
_CnatSessionCurrentIdletime_Type = TimeTicks
_CnatSessionCurrentIdletime_Object = MibTableColumn
cnatSessionCurrentIdletime = _CnatSessionCurrentIdletime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 2, 5, 1, 14),
    _CnatSessionCurrentIdletime_Type()
)
cnatSessionCurrentIdletime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnatSessionCurrentIdletime.setStatus("current")
_CnatSessionSecondBindId_Type = Unsigned32
_CnatSessionSecondBindId_Object = MibTableColumn
cnatSessionSecondBindId = _CnatSessionSecondBindId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 2, 5, 1, 15),
    _CnatSessionSecondBindId_Type()
)
cnatSessionSecondBindId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnatSessionSecondBindId.setStatus("current")
_CnatSessionInTranslate_Type = Counter32
_CnatSessionInTranslate_Object = MibTableColumn
cnatSessionInTranslate = _CnatSessionInTranslate_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 2, 5, 1, 16),
    _CnatSessionInTranslate_Type()
)
cnatSessionInTranslate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnatSessionInTranslate.setStatus("current")
_CnatSessionOutTranslate_Type = Counter32
_CnatSessionOutTranslate_Object = MibTableColumn
cnatSessionOutTranslate = _CnatSessionOutTranslate_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 2, 5, 1, 17),
    _CnatSessionOutTranslate_Type()
)
cnatSessionOutTranslate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnatSessionOutTranslate.setStatus("current")
_CnatStatistics_ObjectIdentity = ObjectIdentity
cnatStatistics = _CnatStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 3)
)
_CnatProtocolStatsTable_Object = MibTable
cnatProtocolStatsTable = _CnatProtocolStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cnatProtocolStatsTable.setStatus("current")
_CnatProtocolStatsEntry_Object = MibTableRow
cnatProtocolStatsEntry = _CnatProtocolStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 3, 1, 1)
)
cnatProtocolStatsEntry.setIndexNames(
    (0, "CISCO-IETF-NAT-MIB", "cnatProtocolStatsName"),
)
if mibBuilder.loadTexts:
    cnatProtocolStatsEntry.setStatus("current")
_CnatProtocolStatsName_Type = NATProtocolType
_CnatProtocolStatsName_Object = MibTableColumn
cnatProtocolStatsName = _CnatProtocolStatsName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 3, 1, 1, 1),
    _CnatProtocolStatsName_Type()
)
cnatProtocolStatsName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnatProtocolStatsName.setStatus("current")
_CnatProtocolStatsInTranslate_Type = Counter32
_CnatProtocolStatsInTranslate_Object = MibTableColumn
cnatProtocolStatsInTranslate = _CnatProtocolStatsInTranslate_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 3, 1, 1, 2),
    _CnatProtocolStatsInTranslate_Type()
)
cnatProtocolStatsInTranslate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnatProtocolStatsInTranslate.setStatus("current")
_CnatProtocolStatsOutTranslate_Type = Counter32
_CnatProtocolStatsOutTranslate_Object = MibTableColumn
cnatProtocolStatsOutTranslate = _CnatProtocolStatsOutTranslate_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 3, 1, 1, 3),
    _CnatProtocolStatsOutTranslate_Type()
)
cnatProtocolStatsOutTranslate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnatProtocolStatsOutTranslate.setStatus("current")
_CnatProtocolStatsRejectCount_Type = Counter32
_CnatProtocolStatsRejectCount_Object = MibTableColumn
cnatProtocolStatsRejectCount = _CnatProtocolStatsRejectCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 3, 1, 1, 4),
    _CnatProtocolStatsRejectCount_Type()
)
cnatProtocolStatsRejectCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnatProtocolStatsRejectCount.setStatus("current")
_CnatAddrMapStatsTable_Object = MibTable
cnatAddrMapStatsTable = _CnatAddrMapStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cnatAddrMapStatsTable.setStatus("current")
_CnatAddrMapStatsEntry_Object = MibTableRow
cnatAddrMapStatsEntry = _CnatAddrMapStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 3, 2, 1)
)
cnatAddrMapStatsEntry.setIndexNames(
    (0, "CISCO-IETF-NAT-MIB", "cnatAddrMapStatsConfName"),
    (0, "CISCO-IETF-NAT-MIB", "cnatAddrMapStatsMapName"),
)
if mibBuilder.loadTexts:
    cnatAddrMapStatsEntry.setStatus("current")


class _CnatAddrMapStatsConfName_Type(SnmpAdminString):
    """Custom type cnatAddrMapStatsConfName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CnatAddrMapStatsConfName_Type.__name__ = "SnmpAdminString"
_CnatAddrMapStatsConfName_Object = MibTableColumn
cnatAddrMapStatsConfName = _CnatAddrMapStatsConfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 3, 2, 1, 1),
    _CnatAddrMapStatsConfName_Type()
)
cnatAddrMapStatsConfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnatAddrMapStatsConfName.setStatus("current")


class _CnatAddrMapStatsMapName_Type(SnmpAdminString):
    """Custom type cnatAddrMapStatsMapName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CnatAddrMapStatsMapName_Type.__name__ = "SnmpAdminString"
_CnatAddrMapStatsMapName_Object = MibTableColumn
cnatAddrMapStatsMapName = _CnatAddrMapStatsMapName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 3, 2, 1, 2),
    _CnatAddrMapStatsMapName_Type()
)
cnatAddrMapStatsMapName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnatAddrMapStatsMapName.setStatus("current")
_CnatAddrMapStatsInTranslate_Type = Counter32
_CnatAddrMapStatsInTranslate_Object = MibTableColumn
cnatAddrMapStatsInTranslate = _CnatAddrMapStatsInTranslate_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 3, 2, 1, 3),
    _CnatAddrMapStatsInTranslate_Type()
)
cnatAddrMapStatsInTranslate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnatAddrMapStatsInTranslate.setStatus("current")
_CnatAddrMapStatsOutTranslate_Type = Counter32
_CnatAddrMapStatsOutTranslate_Object = MibTableColumn
cnatAddrMapStatsOutTranslate = _CnatAddrMapStatsOutTranslate_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 3, 2, 1, 4),
    _CnatAddrMapStatsOutTranslate_Type()
)
cnatAddrMapStatsOutTranslate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnatAddrMapStatsOutTranslate.setStatus("current")
_CnatAddrMapStatsNoResource_Type = Counter32
_CnatAddrMapStatsNoResource_Object = MibTableColumn
cnatAddrMapStatsNoResource = _CnatAddrMapStatsNoResource_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 3, 2, 1, 5),
    _CnatAddrMapStatsNoResource_Type()
)
cnatAddrMapStatsNoResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnatAddrMapStatsNoResource.setStatus("current")
_CnatAddrMapStatsAddrUsed_Type = Gauge32
_CnatAddrMapStatsAddrUsed_Object = MibTableColumn
cnatAddrMapStatsAddrUsed = _CnatAddrMapStatsAddrUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 3, 2, 1, 6),
    _CnatAddrMapStatsAddrUsed_Type()
)
cnatAddrMapStatsAddrUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnatAddrMapStatsAddrUsed.setStatus("current")
_CnatInterfaceStatsTable_Object = MibTable
cnatInterfaceStatsTable = _CnatInterfaceStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 3, 3)
)
if mibBuilder.loadTexts:
    cnatInterfaceStatsTable.setStatus("current")
_CnatInterfaceStatsEntry_Object = MibTableRow
cnatInterfaceStatsEntry = _CnatInterfaceStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    cnatInterfaceStatsEntry.setStatus("current")
_CnatInterfacePktsIn_Type = Counter32
_CnatInterfacePktsIn_Object = MibTableColumn
cnatInterfacePktsIn = _CnatInterfacePktsIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 3, 3, 1, 1),
    _CnatInterfacePktsIn_Type()
)
cnatInterfacePktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnatInterfacePktsIn.setStatus("current")
_CnatInterfacePktsOut_Type = Counter32
_CnatInterfacePktsOut_Object = MibTableColumn
cnatInterfacePktsOut = _CnatInterfacePktsOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 1, 3, 3, 1, 2),
    _CnatInterfacePktsOut_Type()
)
cnatInterfacePktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnatInterfacePktsOut.setStatus("current")
_CiscoNatMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
ciscoNatMIBNotificationPrefix = _CiscoNatMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 2)
)
_CiscoNatMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoNatMIBNotifications = _CiscoNatMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 2, 0)
)
_CiscoNatMIBConformance_ObjectIdentity = ObjectIdentity
ciscoNatMIBConformance = _CiscoNatMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 3)
)
_CiscoNatMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoNatMIBCompliances = _CiscoNatMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 3, 1)
)
_CiscoNatMIBGroups_ObjectIdentity = ObjectIdentity
ciscoNatMIBGroups = _CiscoNatMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 3, 2)
)
cnatInterfaceEntry.registerAugmentions(
    ("CISCO-IETF-NAT-MIB",
     "cnatInterfaceStatsEntry")
)
cnatInterfaceStatsEntry.setIndexNames(*cnatInterfaceEntry.getIndexNames())

# Managed Objects groups

cnatConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 3, 2, 1)
)
cnatConfigGroup.setObjects(
      *(("CISCO-IETF-NAT-MIB", "cnatConfServiceType"),
        ("CISCO-IETF-NAT-MIB", "cnatConfTimeoutIcmpIdle"),
        ("CISCO-IETF-NAT-MIB", "cnatConfTimeoutUdpIdle"),
        ("CISCO-IETF-NAT-MIB", "cnatConfTimeoutTcpIdle"),
        ("CISCO-IETF-NAT-MIB", "cnatConfTimeoutTcpNeg"),
        ("CISCO-IETF-NAT-MIB", "cnatConfTimeoutOther"),
        ("CISCO-IETF-NAT-MIB", "cnatConfMaxBindLeaseTime"),
        ("CISCO-IETF-NAT-MIB", "cnatConfMaxBindIdleTime"),
        ("CISCO-IETF-NAT-MIB", "cnatConfStorageType"),
        ("CISCO-IETF-NAT-MIB", "cnatConfStatus"),
        ("CISCO-IETF-NAT-MIB", "cnatConfStaticAddrMapType"),
        ("CISCO-IETF-NAT-MIB", "cnatConfStaticLocalAddrFrom"),
        ("CISCO-IETF-NAT-MIB", "cnatConfStaticLocalAddrTo"),
        ("CISCO-IETF-NAT-MIB", "cnatConfStaticLocalPortFrom"),
        ("CISCO-IETF-NAT-MIB", "cnatConfStaticLocalPortTo"),
        ("CISCO-IETF-NAT-MIB", "cnatConfStaticGlobalAddrFrom"),
        ("CISCO-IETF-NAT-MIB", "cnatConfStaticGlobalAddrTo"),
        ("CISCO-IETF-NAT-MIB", "cnatConfStaticGlobalPortFrom"),
        ("CISCO-IETF-NAT-MIB", "cnatConfStaticGlobalPortTo"),
        ("CISCO-IETF-NAT-MIB", "cnatConfStaticProtocol"),
        ("CISCO-IETF-NAT-MIB", "cnatConfStaticAddrMapStorageType"),
        ("CISCO-IETF-NAT-MIB", "cnatConfStaticAddrMapStatus"),
        ("CISCO-IETF-NAT-MIB", "cnatConfDynAddressMapType"),
        ("CISCO-IETF-NAT-MIB", "cnatConfDynLocalAddrFrom"),
        ("CISCO-IETF-NAT-MIB", "cnatConfDynLocalAddrTo"),
        ("CISCO-IETF-NAT-MIB", "cnatConfDynLocalPortFrom"),
        ("CISCO-IETF-NAT-MIB", "cnatConfDynLocalPortTo"),
        ("CISCO-IETF-NAT-MIB", "cnatConfDynGlobalAddrFrom"),
        ("CISCO-IETF-NAT-MIB", "cnatConfDynGlobalAddrTo"),
        ("CISCO-IETF-NAT-MIB", "cnatConfDynGlobalPortFrom"),
        ("CISCO-IETF-NAT-MIB", "cnatConfDynGlobalPortTo"),
        ("CISCO-IETF-NAT-MIB", "cnatConfDynProtocol"),
        ("CISCO-IETF-NAT-MIB", "cnatConfDynAddrMapStorageType"),
        ("CISCO-IETF-NAT-MIB", "cnatConfDynAddrMapStatus"),
        ("CISCO-IETF-NAT-MIB", "cnatInterfaceRealm"),
        ("CISCO-IETF-NAT-MIB", "cnatInterfaceStorageType"),
        ("CISCO-IETF-NAT-MIB", "cnatInterfaceStatus"))
)
if mibBuilder.loadTexts:
    cnatConfigGroup.setStatus("current")

cnatBindGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 3, 2, 2)
)
cnatBindGroup.setObjects(
      *(("CISCO-IETF-NAT-MIB", "cnatAddrBindNumberOfEntries"),
        ("CISCO-IETF-NAT-MIB", "cnatAddrBindGlobalAddr"),
        ("CISCO-IETF-NAT-MIB", "cnatAddrBindId"),
        ("CISCO-IETF-NAT-MIB", "cnatAddrBindDirection"),
        ("CISCO-IETF-NAT-MIB", "cnatAddrBindType"),
        ("CISCO-IETF-NAT-MIB", "cnatAddrBindConfName"),
        ("CISCO-IETF-NAT-MIB", "cnatAddrBindSessionCount"),
        ("CISCO-IETF-NAT-MIB", "cnatAddrBindCurrentIdleTime"),
        ("CISCO-IETF-NAT-MIB", "cnatAddrBindInTranslate"),
        ("CISCO-IETF-NAT-MIB", "cnatAddrBindOutTranslate"),
        ("CISCO-IETF-NAT-MIB", "cnatAddrPortBindNumberOfEntries"),
        ("CISCO-IETF-NAT-MIB", "cnatAddrPortBindGlobalAddr"),
        ("CISCO-IETF-NAT-MIB", "cnatAddrPortBindGlobalPort"),
        ("CISCO-IETF-NAT-MIB", "cnatAddrPortBindId"),
        ("CISCO-IETF-NAT-MIB", "cnatAddrPortBindDirection"),
        ("CISCO-IETF-NAT-MIB", "cnatAddrPortBindType"),
        ("CISCO-IETF-NAT-MIB", "cnatAddrPortBindConfName"),
        ("CISCO-IETF-NAT-MIB", "cnatAddrPortBindSessionCount"),
        ("CISCO-IETF-NAT-MIB", "cnatAddrPortBindCurrentIdleTime"),
        ("CISCO-IETF-NAT-MIB", "cnatAddrPortBindInTranslate"),
        ("CISCO-IETF-NAT-MIB", "cnatAddrPortBindOutTranslate"),
        ("CISCO-IETF-NAT-MIB", "cnatSessionDirection"),
        ("CISCO-IETF-NAT-MIB", "cnatSessionUpTime"),
        ("CISCO-IETF-NAT-MIB", "cnatSessionProtocolType"),
        ("CISCO-IETF-NAT-MIB", "cnatSessionOrigPrivateAddr"),
        ("CISCO-IETF-NAT-MIB", "cnatSessionTransPrivateAddr"),
        ("CISCO-IETF-NAT-MIB", "cnatSessionOrigPrivatePort"),
        ("CISCO-IETF-NAT-MIB", "cnatSessionTransPrivatePort"),
        ("CISCO-IETF-NAT-MIB", "cnatSessionOrigPublicAddr"),
        ("CISCO-IETF-NAT-MIB", "cnatSessionTransPublicAddr"),
        ("CISCO-IETF-NAT-MIB", "cnatSessionOrigPublicPort"),
        ("CISCO-IETF-NAT-MIB", "cnatSessionTransPublicPort"),
        ("CISCO-IETF-NAT-MIB", "cnatSessionCurrentIdletime"),
        ("CISCO-IETF-NAT-MIB", "cnatSessionSecondBindId"),
        ("CISCO-IETF-NAT-MIB", "cnatSessionInTranslate"),
        ("CISCO-IETF-NAT-MIB", "cnatSessionOutTranslate"))
)
if mibBuilder.loadTexts:
    cnatBindGroup.setStatus("current")

cnatStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 3, 2, 3)
)
cnatStatsGroup.setObjects(
      *(("CISCO-IETF-NAT-MIB", "cnatProtocolStatsInTranslate"),
        ("CISCO-IETF-NAT-MIB", "cnatProtocolStatsOutTranslate"),
        ("CISCO-IETF-NAT-MIB", "cnatProtocolStatsRejectCount"),
        ("CISCO-IETF-NAT-MIB", "cnatAddrMapStatsInTranslate"),
        ("CISCO-IETF-NAT-MIB", "cnatAddrMapStatsOutTranslate"),
        ("CISCO-IETF-NAT-MIB", "cnatAddrMapStatsNoResource"),
        ("CISCO-IETF-NAT-MIB", "cnatAddrMapStatsAddrUsed"),
        ("CISCO-IETF-NAT-MIB", "cnatInterfacePktsIn"),
        ("CISCO-IETF-NAT-MIB", "cnatInterfacePktsOut"))
)
if mibBuilder.loadTexts:
    cnatStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoNatMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 77, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoNatMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IETF-NAT-MIB",
    **{"NATProtocolType": NATProtocolType,
       "ciscoIetfNatMIB": ciscoIetfNatMIB,
       "ciscoNatMIBObjects": ciscoNatMIBObjects,
       "cnatConfig": cnatConfig,
       "cnatConfTable": cnatConfTable,
       "cnatConfEntry": cnatConfEntry,
       "cnatConfName": cnatConfName,
       "cnatConfServiceType": cnatConfServiceType,
       "cnatConfTimeoutIcmpIdle": cnatConfTimeoutIcmpIdle,
       "cnatConfTimeoutUdpIdle": cnatConfTimeoutUdpIdle,
       "cnatConfTimeoutTcpIdle": cnatConfTimeoutTcpIdle,
       "cnatConfTimeoutTcpNeg": cnatConfTimeoutTcpNeg,
       "cnatConfTimeoutOther": cnatConfTimeoutOther,
       "cnatConfMaxBindLeaseTime": cnatConfMaxBindLeaseTime,
       "cnatConfMaxBindIdleTime": cnatConfMaxBindIdleTime,
       "cnatConfStorageType": cnatConfStorageType,
       "cnatConfStatus": cnatConfStatus,
       "cnatConfStaticAddrMapTable": cnatConfStaticAddrMapTable,
       "cnatConfStaticAddrMapEntry": cnatConfStaticAddrMapEntry,
       "cnatConfStaticAddrMapName": cnatConfStaticAddrMapName,
       "cnatConfStaticAddrMapType": cnatConfStaticAddrMapType,
       "cnatConfStaticLocalAddrFrom": cnatConfStaticLocalAddrFrom,
       "cnatConfStaticLocalAddrTo": cnatConfStaticLocalAddrTo,
       "cnatConfStaticLocalPortFrom": cnatConfStaticLocalPortFrom,
       "cnatConfStaticLocalPortTo": cnatConfStaticLocalPortTo,
       "cnatConfStaticGlobalAddrFrom": cnatConfStaticGlobalAddrFrom,
       "cnatConfStaticGlobalAddrTo": cnatConfStaticGlobalAddrTo,
       "cnatConfStaticGlobalPortFrom": cnatConfStaticGlobalPortFrom,
       "cnatConfStaticGlobalPortTo": cnatConfStaticGlobalPortTo,
       "cnatConfStaticProtocol": cnatConfStaticProtocol,
       "cnatConfStaticAddrMapStorageType": cnatConfStaticAddrMapStorageType,
       "cnatConfStaticAddrMapStatus": cnatConfStaticAddrMapStatus,
       "cnatConfDynAddrMapTable": cnatConfDynAddrMapTable,
       "cnatConfDynAddrMapEntry": cnatConfDynAddrMapEntry,
       "cnatConfDynAddrMapName": cnatConfDynAddrMapName,
       "cnatConfDynAddressMapType": cnatConfDynAddressMapType,
       "cnatConfDynLocalAddrFrom": cnatConfDynLocalAddrFrom,
       "cnatConfDynLocalAddrTo": cnatConfDynLocalAddrTo,
       "cnatConfDynLocalPortFrom": cnatConfDynLocalPortFrom,
       "cnatConfDynLocalPortTo": cnatConfDynLocalPortTo,
       "cnatConfDynGlobalAddrFrom": cnatConfDynGlobalAddrFrom,
       "cnatConfDynGlobalAddrTo": cnatConfDynGlobalAddrTo,
       "cnatConfDynGlobalPortFrom": cnatConfDynGlobalPortFrom,
       "cnatConfDynGlobalPortTo": cnatConfDynGlobalPortTo,
       "cnatConfDynProtocol": cnatConfDynProtocol,
       "cnatConfDynAddrMapStorageType": cnatConfDynAddrMapStorageType,
       "cnatConfDynAddrMapStatus": cnatConfDynAddrMapStatus,
       "cnatInterfaceTable": cnatInterfaceTable,
       "cnatInterfaceEntry": cnatInterfaceEntry,
       "cnatInterfaceIndex": cnatInterfaceIndex,
       "cnatInterfaceRealm": cnatInterfaceRealm,
       "cnatInterfaceStorageType": cnatInterfaceStorageType,
       "cnatInterfaceStatus": cnatInterfaceStatus,
       "cnatBind": cnatBind,
       "cnatAddrBindNumberOfEntries": cnatAddrBindNumberOfEntries,
       "cnatAddrBindTable": cnatAddrBindTable,
       "cnatAddrBindEntry": cnatAddrBindEntry,
       "cnatAddrBindLocalAddr": cnatAddrBindLocalAddr,
       "cnatAddrBindGlobalAddr": cnatAddrBindGlobalAddr,
       "cnatAddrBindId": cnatAddrBindId,
       "cnatAddrBindDirection": cnatAddrBindDirection,
       "cnatAddrBindType": cnatAddrBindType,
       "cnatAddrBindConfName": cnatAddrBindConfName,
       "cnatAddrBindSessionCount": cnatAddrBindSessionCount,
       "cnatAddrBindCurrentIdleTime": cnatAddrBindCurrentIdleTime,
       "cnatAddrBindInTranslate": cnatAddrBindInTranslate,
       "cnatAddrBindOutTranslate": cnatAddrBindOutTranslate,
       "cnatAddrPortBindNumberOfEntries": cnatAddrPortBindNumberOfEntries,
       "cnatAddrPortBindTable": cnatAddrPortBindTable,
       "cnatAddrPortBindEntry": cnatAddrPortBindEntry,
       "cnatAddrPortBindLocalAddr": cnatAddrPortBindLocalAddr,
       "cnatAddrPortBindLocalPort": cnatAddrPortBindLocalPort,
       "cnatAddrPortBindProtocol": cnatAddrPortBindProtocol,
       "cnatAddrPortBindGlobalAddr": cnatAddrPortBindGlobalAddr,
       "cnatAddrPortBindGlobalPort": cnatAddrPortBindGlobalPort,
       "cnatAddrPortBindId": cnatAddrPortBindId,
       "cnatAddrPortBindDirection": cnatAddrPortBindDirection,
       "cnatAddrPortBindType": cnatAddrPortBindType,
       "cnatAddrPortBindConfName": cnatAddrPortBindConfName,
       "cnatAddrPortBindSessionCount": cnatAddrPortBindSessionCount,
       "cnatAddrPortBindCurrentIdleTime": cnatAddrPortBindCurrentIdleTime,
       "cnatAddrPortBindInTranslate": cnatAddrPortBindInTranslate,
       "cnatAddrPortBindOutTranslate": cnatAddrPortBindOutTranslate,
       "cnatSessionTable": cnatSessionTable,
       "cnatSessionEntry": cnatSessionEntry,
       "cnatSessionBindId": cnatSessionBindId,
       "cnatSessionId": cnatSessionId,
       "cnatSessionDirection": cnatSessionDirection,
       "cnatSessionUpTime": cnatSessionUpTime,
       "cnatSessionProtocolType": cnatSessionProtocolType,
       "cnatSessionOrigPrivateAddr": cnatSessionOrigPrivateAddr,
       "cnatSessionTransPrivateAddr": cnatSessionTransPrivateAddr,
       "cnatSessionOrigPrivatePort": cnatSessionOrigPrivatePort,
       "cnatSessionTransPrivatePort": cnatSessionTransPrivatePort,
       "cnatSessionOrigPublicAddr": cnatSessionOrigPublicAddr,
       "cnatSessionTransPublicAddr": cnatSessionTransPublicAddr,
       "cnatSessionOrigPublicPort": cnatSessionOrigPublicPort,
       "cnatSessionTransPublicPort": cnatSessionTransPublicPort,
       "cnatSessionCurrentIdletime": cnatSessionCurrentIdletime,
       "cnatSessionSecondBindId": cnatSessionSecondBindId,
       "cnatSessionInTranslate": cnatSessionInTranslate,
       "cnatSessionOutTranslate": cnatSessionOutTranslate,
       "cnatStatistics": cnatStatistics,
       "cnatProtocolStatsTable": cnatProtocolStatsTable,
       "cnatProtocolStatsEntry": cnatProtocolStatsEntry,
       "cnatProtocolStatsName": cnatProtocolStatsName,
       "cnatProtocolStatsInTranslate": cnatProtocolStatsInTranslate,
       "cnatProtocolStatsOutTranslate": cnatProtocolStatsOutTranslate,
       "cnatProtocolStatsRejectCount": cnatProtocolStatsRejectCount,
       "cnatAddrMapStatsTable": cnatAddrMapStatsTable,
       "cnatAddrMapStatsEntry": cnatAddrMapStatsEntry,
       "cnatAddrMapStatsConfName": cnatAddrMapStatsConfName,
       "cnatAddrMapStatsMapName": cnatAddrMapStatsMapName,
       "cnatAddrMapStatsInTranslate": cnatAddrMapStatsInTranslate,
       "cnatAddrMapStatsOutTranslate": cnatAddrMapStatsOutTranslate,
       "cnatAddrMapStatsNoResource": cnatAddrMapStatsNoResource,
       "cnatAddrMapStatsAddrUsed": cnatAddrMapStatsAddrUsed,
       "cnatInterfaceStatsTable": cnatInterfaceStatsTable,
       "cnatInterfaceStatsEntry": cnatInterfaceStatsEntry,
       "cnatInterfacePktsIn": cnatInterfacePktsIn,
       "cnatInterfacePktsOut": cnatInterfacePktsOut,
       "ciscoNatMIBNotificationPrefix": ciscoNatMIBNotificationPrefix,
       "ciscoNatMIBNotifications": ciscoNatMIBNotifications,
       "ciscoNatMIBConformance": ciscoNatMIBConformance,
       "ciscoNatMIBCompliances": ciscoNatMIBCompliances,
       "ciscoNatMIBCompliance": ciscoNatMIBCompliance,
       "ciscoNatMIBGroups": ciscoNatMIBGroups,
       "cnatConfigGroup": cnatConfigGroup,
       "cnatBindGroup": cnatBindGroup,
       "cnatStatsGroup": cnatStatsGroup}
)
