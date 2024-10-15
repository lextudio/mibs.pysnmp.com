# SNMP MIB module (CISCOSB-TUNNEL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCOSB-TUNNEL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:15:07 2024
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

(switch001,) = mibBuilder.importSymbols(
    "CISCOSB-MIB",
    "switch001")

(DnsName,) = mibBuilder.importSymbols(
    "DNS-SERVER-MIB",
    "DnsName")

(IANAtunnelType,) = mibBuilder.importSymbols(
    "IANAifType-MIB",
    "IANAtunnelType")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(tunnelIfEntry,) = mibBuilder.importSymbols(
    "TUNNEL-MIB",
    "tunnelIfEntry")


# MODULE-IDENTITY

rlTunnel = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 122)
)
rlTunnel.setRevisions(
        ("2012-05-21 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _RlTunnelIsatapStatus_Type(Integer32):
    """Custom type rlTunnelIsatapStatus based on Integer32"""
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


_RlTunnelIsatapStatus_Type.__name__ = "Integer32"
_RlTunnelIsatapStatus_Object = MibScalar
rlTunnelIsatapStatus = _RlTunnelIsatapStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 122, 1),
    _RlTunnelIsatapStatus_Type()
)
rlTunnelIsatapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTunnelIsatapStatus.setStatus("deprecated")


class _RlTunnelIsatapRobustness_Type(Unsigned32):
    """Custom type rlTunnelIsatapRobustness based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_RlTunnelIsatapRobustness_Type.__name__ = "Unsigned32"
_RlTunnelIsatapRobustness_Object = MibScalar
rlTunnelIsatapRobustness = _RlTunnelIsatapRobustness_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 122, 2),
    _RlTunnelIsatapRobustness_Type()
)
rlTunnelIsatapRobustness.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTunnelIsatapRobustness.setStatus("deprecated")
_RlTunnelIsatapDnsHostName_Type = DnsName
_RlTunnelIsatapDnsHostName_Object = MibScalar
rlTunnelIsatapDnsHostName = _RlTunnelIsatapDnsHostName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 122, 3),
    _RlTunnelIsatapDnsHostName_Type()
)
rlTunnelIsatapDnsHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTunnelIsatapDnsHostName.setStatus("deprecated")


class _RlTunnelIsatapQueryInterval_Type(Unsigned32):
    """Custom type rlTunnelIsatapQueryInterval based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 3600),
    )


_RlTunnelIsatapQueryInterval_Type.__name__ = "Unsigned32"
_RlTunnelIsatapQueryInterval_Object = MibScalar
rlTunnelIsatapQueryInterval = _RlTunnelIsatapQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 122, 4),
    _RlTunnelIsatapQueryInterval_Type()
)
rlTunnelIsatapQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTunnelIsatapQueryInterval.setStatus("deprecated")


class _RlTunnelIsatapRSInterval_Type(Unsigned32):
    """Custom type rlTunnelIsatapRSInterval based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 3600),
    )


_RlTunnelIsatapRSInterval_Type.__name__ = "Unsigned32"
_RlTunnelIsatapRSInterval_Object = MibScalar
rlTunnelIsatapRSInterval = _RlTunnelIsatapRSInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 122, 5),
    _RlTunnelIsatapRSInterval_Type()
)
rlTunnelIsatapRSInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTunnelIsatapRSInterval.setStatus("deprecated")


class _RlTunnelIsatapMinQueryInterval_Type(Unsigned32):
    """Custom type rlTunnelIsatapMinQueryInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_RlTunnelIsatapMinQueryInterval_Type.__name__ = "Unsigned32"
_RlTunnelIsatapMinQueryInterval_Object = MibScalar
rlTunnelIsatapMinQueryInterval = _RlTunnelIsatapMinQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 122, 6),
    _RlTunnelIsatapMinQueryInterval_Type()
)
rlTunnelIsatapMinQueryInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlTunnelIsatapMinQueryInterval.setStatus("deprecated")


class _RlTunnelIsatapMinRSInterval_Type(Unsigned32):
    """Custom type rlTunnelIsatapMinRSInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_RlTunnelIsatapMinRSInterval_Type.__name__ = "Unsigned32"
_RlTunnelIsatapMinRSInterval_Object = MibScalar
rlTunnelIsatapMinRSInterval = _RlTunnelIsatapMinRSInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 122, 7),
    _RlTunnelIsatapMinRSInterval_Type()
)
rlTunnelIsatapMinRSInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlTunnelIsatapMinRSInterval.setStatus("deprecated")


class _RlTunnelIsatapRouterAddress_Type(IpAddress):
    """Custom type rlTunnelIsatapRouterAddress based on IpAddress"""
    defaultValue = 0


_RlTunnelIsatapRouterAddress_Object = MibScalar
rlTunnelIsatapRouterAddress = _RlTunnelIsatapRouterAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 122, 8),
    _RlTunnelIsatapRouterAddress_Type()
)
rlTunnelIsatapRouterAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlTunnelIsatapRouterAddress.setStatus("deprecated")


class _RlTunnelIsatapLocalIPv4Address_Type(IpAddress):
    """Custom type rlTunnelIsatapLocalIPv4Address based on IpAddress"""
    defaultValue = 0


_RlTunnelIsatapLocalIPv4Address_Object = MibScalar
rlTunnelIsatapLocalIPv4Address = _RlTunnelIsatapLocalIPv4Address_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 122, 9),
    _RlTunnelIsatapLocalIPv4Address_Type()
)
rlTunnelIsatapLocalIPv4Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlTunnelIsatapLocalIPv4Address.setStatus("deprecated")
_RlTunnelGeneral_ObjectIdentity = ObjectIdentity
rlTunnelGeneral = _RlTunnelGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 122, 11)
)
_RlTunnelIfTable_Object = MibTable
rlTunnelIfTable = _RlTunnelIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 122, 11, 1)
)
if mibBuilder.loadTexts:
    rlTunnelIfTable.setStatus("current")
_RlTunnelIfEntry_Object = MibTableRow
rlTunnelIfEntry = _RlTunnelIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 122, 11, 1, 1)
)
if mibBuilder.loadTexts:
    rlTunnelIfEntry.setStatus("current")
_RlTunnelIfEncapsMethod_Type = IANAtunnelType
_RlTunnelIfEncapsMethod_Object = MibTableColumn
rlTunnelIfEncapsMethod = _RlTunnelIfEncapsMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 122, 11, 1, 1, 1),
    _RlTunnelIfEncapsMethod_Type()
)
rlTunnelIfEncapsMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTunnelIfEncapsMethod.setStatus("current")


class _RlTunnelIfLocalAddressSource_Type(Integer32):
    """Custom type rlTunnelIfLocalAddressSource based on Integer32"""
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
        *(("auto", 2),
          ("configured", 1),
          ("interface", 3))
    )


_RlTunnelIfLocalAddressSource_Type.__name__ = "Integer32"
_RlTunnelIfLocalAddressSource_Object = MibTableColumn
rlTunnelIfLocalAddressSource = _RlTunnelIfLocalAddressSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 122, 11, 1, 1, 2),
    _RlTunnelIfLocalAddressSource_Type()
)
rlTunnelIfLocalAddressSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTunnelIfLocalAddressSource.setStatus("current")


class _RlTunnelIfLocalAddressInterfaceId_Type(Unsigned32):
    """Custom type rlTunnelIfLocalAddressInterfaceId based on Unsigned32"""
    defaultValue = 0


_RlTunnelIfLocalAddressInterfaceId_Object = MibTableColumn
rlTunnelIfLocalAddressInterfaceId = _RlTunnelIfLocalAddressInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 122, 11, 1, 1, 3),
    _RlTunnelIfLocalAddressInterfaceId_Type()
)
rlTunnelIfLocalAddressInterfaceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTunnelIfLocalAddressInterfaceId.setStatus("current")


class _RlTunnelIfLocalIPv4Address_Type(IpAddress):
    """Custom type rlTunnelIfLocalIPv4Address based on IpAddress"""
    defaultValue = 0


_RlTunnelIfLocalIPv4Address_Object = MibTableColumn
rlTunnelIfLocalIPv4Address = _RlTunnelIfLocalIPv4Address_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 122, 11, 1, 1, 4),
    _RlTunnelIfLocalIPv4Address_Type()
)
rlTunnelIfLocalIPv4Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlTunnelIfLocalIPv4Address.setStatus("current")
_RlTunnelIfStatus_Type = RowStatus
_RlTunnelIfStatus_Object = MibTableColumn
rlTunnelIfStatus = _RlTunnelIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 122, 11, 1, 1, 5),
    _RlTunnelIfStatus_Type()
)
rlTunnelIfStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTunnelIfStatus.setStatus("current")
_RlTunnelTypeSpecific_ObjectIdentity = ObjectIdentity
rlTunnelTypeSpecific = _RlTunnelTypeSpecific_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 122, 12)
)
_RlTunnelIsatap_ObjectIdentity = ObjectIdentity
rlTunnelIsatap = _RlTunnelIsatap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 122, 12, 1)
)
_RlTunnelIsatapConfTable_Object = MibTable
rlTunnelIsatapConfTable = _RlTunnelIsatapConfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 122, 12, 1, 1)
)
if mibBuilder.loadTexts:
    rlTunnelIsatapConfTable.setStatus("current")
_RlTunnelIsatapConfEntry_Object = MibTableRow
rlTunnelIsatapConfEntry = _RlTunnelIsatapConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 122, 12, 1, 1, 1)
)
rlTunnelIsatapConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rlTunnelIsatapConfEntry.setStatus("current")


class _RlTunnelIsatapConfDnsName_Type(OctetString):
    """Custom type rlTunnelIsatapConfDnsName based on OctetString"""
    defaultValue = OctetString("ISATAP")


_RlTunnelIsatapConfDnsName_Object = MibTableColumn
rlTunnelIsatapConfDnsName = _RlTunnelIsatapConfDnsName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 122, 12, 1, 1, 1, 1),
    _RlTunnelIsatapConfDnsName_Type()
)
rlTunnelIsatapConfDnsName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTunnelIsatapConfDnsName.setStatus("current")
_RlTunnelIsatapConfRowStatus_Type = RowStatus
_RlTunnelIsatapConfRowStatus_Object = MibTableColumn
rlTunnelIsatapConfRowStatus = _RlTunnelIsatapConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 122, 12, 1, 1, 1, 2),
    _RlTunnelIsatapConfRowStatus_Type()
)
rlTunnelIsatapConfRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTunnelIsatapConfRowStatus.setStatus("current")
_RlTunnelIsatapPrlTable_Object = MibTable
rlTunnelIsatapPrlTable = _RlTunnelIsatapPrlTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 122, 12, 1, 2)
)
if mibBuilder.loadTexts:
    rlTunnelIsatapPrlTable.setStatus("current")
_RlTunnelIsatapPrlEntry_Object = MibTableRow
rlTunnelIsatapPrlEntry = _RlTunnelIsatapPrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 122, 12, 1, 2, 1)
)
rlTunnelIsatapPrlEntry.setIndexNames(
    (0, "CISCOSB-TUNNEL-MIB", "rlTunnelIsatapPrlIfIndex"),
    (0, "CISCOSB-TUNNEL-MIB", "rlTunnelIsatapPrlPriority"),
)
if mibBuilder.loadTexts:
    rlTunnelIsatapPrlEntry.setStatus("current")
_RlTunnelIsatapPrlIfIndex_Type = Unsigned32
_RlTunnelIsatapPrlIfIndex_Object = MibTableColumn
rlTunnelIsatapPrlIfIndex = _RlTunnelIsatapPrlIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 122, 12, 1, 2, 1, 1),
    _RlTunnelIsatapPrlIfIndex_Type()
)
rlTunnelIsatapPrlIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlTunnelIsatapPrlIfIndex.setStatus("current")
_RlTunnelIsatapPrlPriority_Type = Unsigned32
_RlTunnelIsatapPrlPriority_Object = MibTableColumn
rlTunnelIsatapPrlPriority = _RlTunnelIsatapPrlPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 122, 12, 1, 2, 1, 2),
    _RlTunnelIsatapPrlPriority_Type()
)
rlTunnelIsatapPrlPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlTunnelIsatapPrlPriority.setStatus("current")
_RlTunnelIsatapPrlAddress_Type = IpAddress
_RlTunnelIsatapPrlAddress_Object = MibTableColumn
rlTunnelIsatapPrlAddress = _RlTunnelIsatapPrlAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 122, 12, 1, 2, 1, 3),
    _RlTunnelIsatapPrlAddress_Type()
)
rlTunnelIsatapPrlAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlTunnelIsatapPrlAddress.setStatus("current")


class _RlTunnelIsatapPrlIsActive_Type(Integer32):
    """Custom type rlTunnelIsatapPrlIsActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_RlTunnelIsatapPrlIsActive_Type.__name__ = "Integer32"
_RlTunnelIsatapPrlIsActive_Object = MibTableColumn
rlTunnelIsatapPrlIsActive = _RlTunnelIsatapPrlIsActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 122, 12, 1, 2, 1, 4),
    _RlTunnelIsatapPrlIsActive_Type()
)
rlTunnelIsatapPrlIsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlTunnelIsatapPrlIsActive.setStatus("current")


class _RlTunnelIsatapConfRSInterval_Type(Unsigned32):
    """Custom type rlTunnelIsatapConfRSInterval based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 3600),
    )


_RlTunnelIsatapConfRSInterval_Type.__name__ = "Unsigned32"
_RlTunnelIsatapConfRSInterval_Object = MibScalar
rlTunnelIsatapConfRSInterval = _RlTunnelIsatapConfRSInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 122, 12, 1, 11),
    _RlTunnelIsatapConfRSInterval_Type()
)
rlTunnelIsatapConfRSInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTunnelIsatapConfRSInterval.setStatus("current")


class _RlTunnelIsatapConfRobustness_Type(Unsigned32):
    """Custom type rlTunnelIsatapConfRobustness based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_RlTunnelIsatapConfRobustness_Type.__name__ = "Unsigned32"
_RlTunnelIsatapConfRobustness_Object = MibScalar
rlTunnelIsatapConfRobustness = _RlTunnelIsatapConfRobustness_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 122, 12, 1, 12),
    _RlTunnelIsatapConfRobustness_Type()
)
rlTunnelIsatapConfRobustness.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlTunnelIsatapConfRobustness.setStatus("current")
tunnelIfEntry.registerAugmentions(
    ("CISCOSB-TUNNEL-MIB",
     "rlTunnelIfEntry")
)
rlTunnelIfEntry.setIndexNames(*tunnelIfEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOSB-TUNNEL-MIB",
    **{"rlTunnel": rlTunnel,
       "rlTunnelIsatapStatus": rlTunnelIsatapStatus,
       "rlTunnelIsatapRobustness": rlTunnelIsatapRobustness,
       "rlTunnelIsatapDnsHostName": rlTunnelIsatapDnsHostName,
       "rlTunnelIsatapQueryInterval": rlTunnelIsatapQueryInterval,
       "rlTunnelIsatapRSInterval": rlTunnelIsatapRSInterval,
       "rlTunnelIsatapMinQueryInterval": rlTunnelIsatapMinQueryInterval,
       "rlTunnelIsatapMinRSInterval": rlTunnelIsatapMinRSInterval,
       "rlTunnelIsatapRouterAddress": rlTunnelIsatapRouterAddress,
       "rlTunnelIsatapLocalIPv4Address": rlTunnelIsatapLocalIPv4Address,
       "rlTunnelGeneral": rlTunnelGeneral,
       "rlTunnelIfTable": rlTunnelIfTable,
       "rlTunnelIfEntry": rlTunnelIfEntry,
       "rlTunnelIfEncapsMethod": rlTunnelIfEncapsMethod,
       "rlTunnelIfLocalAddressSource": rlTunnelIfLocalAddressSource,
       "rlTunnelIfLocalAddressInterfaceId": rlTunnelIfLocalAddressInterfaceId,
       "rlTunnelIfLocalIPv4Address": rlTunnelIfLocalIPv4Address,
       "rlTunnelIfStatus": rlTunnelIfStatus,
       "rlTunnelTypeSpecific": rlTunnelTypeSpecific,
       "rlTunnelIsatap": rlTunnelIsatap,
       "rlTunnelIsatapConfTable": rlTunnelIsatapConfTable,
       "rlTunnelIsatapConfEntry": rlTunnelIsatapConfEntry,
       "rlTunnelIsatapConfDnsName": rlTunnelIsatapConfDnsName,
       "rlTunnelIsatapConfRowStatus": rlTunnelIsatapConfRowStatus,
       "rlTunnelIsatapPrlTable": rlTunnelIsatapPrlTable,
       "rlTunnelIsatapPrlEntry": rlTunnelIsatapPrlEntry,
       "rlTunnelIsatapPrlIfIndex": rlTunnelIsatapPrlIfIndex,
       "rlTunnelIsatapPrlPriority": rlTunnelIsatapPrlPriority,
       "rlTunnelIsatapPrlAddress": rlTunnelIsatapPrlAddress,
       "rlTunnelIsatapPrlIsActive": rlTunnelIsatapPrlIsActive,
       "rlTunnelIsatapConfRSInterval": rlTunnelIsatapConfRSInterval,
       "rlTunnelIsatapConfRobustness": rlTunnelIsatapConfRobustness}
)
