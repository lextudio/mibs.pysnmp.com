# SNMP MIB module (TIMETRA-SAS-FILTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TIMETRA-SAS-FILTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:04:21 2024
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

(InetAddressIPv6,
 InetAddressPrefixLength) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv6",
    "InetAddressPrefixLength")

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
 Opaque,
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
    "Opaque",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 MacAddress,
 RowPointer,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowPointer",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(tIPFilterEntry,
 tIPv6FilterEntry) = mibBuilder.importSymbols(
    "TIMETRA-FILTER-MIB",
    "tIPFilterEntry",
    "tIPv6FilterEntry")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(timetraSASConfs,
 timetraSASModules,
 timetraSASNotifyPrefix,
 timetraSASObjs) = mibBuilder.importSymbols(
    "TIMETRA-SAS-GLOBAL-MIB",
    "timetraSASConfs",
    "timetraSASModules",
    "timetraSASNotifyPrefix",
    "timetraSASObjs")

(Dot1PPriority,
 IpAddressPrefixLength,
 SdpBindId,
 ServiceAccessPoint,
 TDSCPFilterActionValue,
 TDSCPNameOrEmpty,
 TFrameType,
 TIpOption,
 TIpProtocol,
 TItemDescription,
 TNamedItem,
 TNamedItemOrEmpty,
 TTcpUdpPort,
 TTcpUdpPortOperator,
 TmnxAdminState,
 TmnxEncapVal,
 TmnxOperState,
 TmnxPortID,
 TmnxServId) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "Dot1PPriority",
    "IpAddressPrefixLength",
    "SdpBindId",
    "ServiceAccessPoint",
    "TDSCPFilterActionValue",
    "TDSCPNameOrEmpty",
    "TFrameType",
    "TIpOption",
    "TIpProtocol",
    "TItemDescription",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TTcpUdpPort",
    "TTcpUdpPortOperator",
    "TmnxAdminState",
    "TmnxEncapVal",
    "TmnxOperState",
    "TmnxPortID",
    "TmnxServId")


# MODULE-IDENTITY

timetraSASFilterMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 1, 1, 16)
)
timetraSASFilterMIBModule.setRevisions(
        ("1912-04-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TmnxSASFilterObjs_ObjectIdentity = ObjectIdentity
tmnxSASFilterObjs = _TmnxSASFilterObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 21)
)
_TSASFilterObjects_ObjectIdentity = ObjectIdentity
tSASFilterObjects = _TSASFilterObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 21, 1)
)
_TIPFilterExtnTable_Object = MibTable
tIPFilterExtnTable = _TIPFilterExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 21, 1, 1)
)
if mibBuilder.loadTexts:
    tIPFilterExtnTable.setStatus("current")
_TIPFilterExtnEntry_Object = MibTableRow
tIPFilterExtnEntry = _TIPFilterExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 21, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tIPFilterExtnEntry.setStatus("current")


class _TFilterUseIpv6Resource_Type(TruthValue):
    """Custom type tFilterUseIpv6Resource based on TruthValue"""


_TFilterUseIpv6Resource_Object = MibTableColumn
tFilterUseIpv6Resource = _TFilterUseIpv6Resource_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 21, 1, 1, 1, 1),
    _TFilterUseIpv6Resource_Type()
)
tFilterUseIpv6Resource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilterUseIpv6Resource.setStatus("current")
_TIPv6FilterExtnTable_Object = MibTable
tIPv6FilterExtnTable = _TIPv6FilterExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 21, 1, 2)
)
if mibBuilder.loadTexts:
    tIPv6FilterExtnTable.setStatus("current")
_TIPv6FilterExtnEntry_Object = MibTableRow
tIPv6FilterExtnEntry = _TIPv6FilterExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 21, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tIPv6FilterExtnEntry.setStatus("current")


class _TFilter64Bitsor128_Type(Integer32):
    """Custom type tFilter64Bitsor128 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv6128", 1),
          ("ipv664", 2))
    )


_TFilter64Bitsor128_Type.__name__ = "Integer32"
_TFilter64Bitsor128_Object = MibTableColumn
tFilter64Bitsor128 = _TFilter64Bitsor128_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 21, 1, 2, 1, 1),
    _TFilter64Bitsor128_Type()
)
tFilter64Bitsor128.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFilter64Bitsor128.setStatus("current")
tIPFilterEntry.registerAugmentions(
    ("TIMETRA-SAS-FILTER-MIB",
     "tIPFilterExtnEntry")
)
tIPFilterExtnEntry.setIndexNames(*tIPFilterEntry.getIndexNames())
tIPv6FilterEntry.registerAugmentions(
    ("TIMETRA-SAS-FILTER-MIB",
     "tIPv6FilterExtnEntry")
)
tIPv6FilterExtnEntry.setIndexNames(*tIPv6FilterEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-SAS-FILTER-MIB",
    **{"timetraSASFilterMIBModule": timetraSASFilterMIBModule,
       "tmnxSASFilterObjs": tmnxSASFilterObjs,
       "tSASFilterObjects": tSASFilterObjects,
       "tIPFilterExtnTable": tIPFilterExtnTable,
       "tIPFilterExtnEntry": tIPFilterExtnEntry,
       "tFilterUseIpv6Resource": tFilterUseIpv6Resource,
       "tIPv6FilterExtnTable": tIPv6FilterExtnTable,
       "tIPv6FilterExtnEntry": tIPv6FilterExtnEntry,
       "tFilter64Bitsor128": tFilter64Bitsor128}
)
