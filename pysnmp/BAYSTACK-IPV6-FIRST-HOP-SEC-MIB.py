# SNMP MIB module (BAYSTACK-IPV6-FIRST-HOP-SEC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BAYSTACK-IPV6-FIRST-HOP-SEC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:46:25 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

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

(bayStackMibs,) = mibBuilder.importSymbols(
    "SYNOPTICS-ROOT-MIB",
    "bayStackMibs")


# MODULE-IDENTITY

bayStackIpv6FirstHopSecMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 45)
)
bayStackIpv6FirstHopSecMib.setRevisions(
        ("2015-04-08 00:00",
         "2014-03-20 00:00",
         "2014-01-17 00:00",
         "2013-11-18 00:00",
         "2013-10-11 00:00",
         "2013-08-20 00:00",
         "2013-05-27 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class FhsRaGuardDeviceRole(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("host", 2),
          ("router", 1))
    )



class FhsRaManagedConfigFlag(Integer32, TextualConvention):
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
        *(("none", 1),
          ("off", 3),
          ("on", 2))
    )



class FhsRaRouterPrefMax(Integer32, TextualConvention):
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
        *(("high", 2),
          ("low", 4),
          ("medium", 3),
          ("none", 1))
    )



class FhsDhcpv6GuardDeviceRole(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("client", 2),
          ("server", 1))
    )



class FhsListName(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )



class FhsAccessType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 2))
    )



class FhsSbtState(Integer32, TextualConvention):
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
        *(("down", 4),
          ("incomplete", 1),
          ("reachable", 2),
          ("stale", 3))
    )



class FhsSbtType(Integer32, TextualConvention):
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
        *(("dhcp", 3),
          ("nd", 2),
          ("static", 1))
    )



# MIB Managed Objects in the order of their OIDs

_BsIpv6FirstHopSecNotifications_ObjectIdentity = ObjectIdentity
bsIpv6FirstHopSecNotifications = _BsIpv6FirstHopSecNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 0)
)
_BsIpv6FirstHopSecObjects_ObjectIdentity = ObjectIdentity
bsIpv6FirstHopSecObjects = _BsIpv6FirstHopSecObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1)
)
_BsIpv6FHSScalVar_ObjectIdentity = ObjectIdentity
bsIpv6FHSScalVar = _BsIpv6FHSScalVar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 1)
)


class _BsIpv6FHSAdmin_Type(TruthValue):
    """Custom type bsIpv6FHSAdmin based on TruthValue"""


_BsIpv6FHSAdmin_Object = MibScalar
bsIpv6FHSAdmin = _BsIpv6FHSAdmin_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 1, 1),
    _BsIpv6FHSAdmin_Type()
)
bsIpv6FHSAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsIpv6FHSAdmin.setStatus("current")


class _BsIpv6FHSRagAdmin_Type(TruthValue):
    """Custom type bsIpv6FHSRagAdmin based on TruthValue"""


_BsIpv6FHSRagAdmin_Object = MibScalar
bsIpv6FHSRagAdmin = _BsIpv6FHSRagAdmin_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 1, 2),
    _BsIpv6FHSRagAdmin_Type()
)
bsIpv6FHSRagAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsIpv6FHSRagAdmin.setStatus("current")


class _BsIpv6FHSDhcpv6gAdmin_Type(TruthValue):
    """Custom type bsIpv6FHSDhcpv6gAdmin based on TruthValue"""


_BsIpv6FHSDhcpv6gAdmin_Object = MibScalar
bsIpv6FHSDhcpv6gAdmin = _BsIpv6FHSDhcpv6gAdmin_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 1, 3),
    _BsIpv6FHSDhcpv6gAdmin_Type()
)
bsIpv6FHSDhcpv6gAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsIpv6FHSDhcpv6gAdmin.setStatus("current")


class _BsIpv6FHSNdInspectAdmin_Type(TruthValue):
    """Custom type bsIpv6FHSNdInspectAdmin based on TruthValue"""


_BsIpv6FHSNdInspectAdmin_Object = MibScalar
bsIpv6FHSNdInspectAdmin = _BsIpv6FHSNdInspectAdmin_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 1, 4),
    _BsIpv6FHSNdInspectAdmin_Type()
)
bsIpv6FHSNdInspectAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsIpv6FHSNdInspectAdmin.setStatus("current")


class _BsIpv6FHSMaxDynSbtEntries_Type(Integer32):
    """Custom type bsIpv6FHSMaxDynSbtEntries based on Integer32"""
    defaultValue = 1024

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_BsIpv6FHSMaxDynSbtEntries_Type.__name__ = "Integer32"
_BsIpv6FHSMaxDynSbtEntries_Object = MibScalar
bsIpv6FHSMaxDynSbtEntries = _BsIpv6FHSMaxDynSbtEntries_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 1, 5),
    _BsIpv6FHSMaxDynSbtEntries_Type()
)
bsIpv6FHSMaxDynSbtEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsIpv6FHSMaxDynSbtEntries.setStatus("current")


class _BsIpv6FHSSbtReachLifeTime_Type(Integer32):
    """Custom type bsIpv6FHSSbtReachLifeTime based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 864000),
    )


_BsIpv6FHSSbtReachLifeTime_Type.__name__ = "Integer32"
_BsIpv6FHSSbtReachLifeTime_Object = MibScalar
bsIpv6FHSSbtReachLifeTime = _BsIpv6FHSSbtReachLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 1, 6),
    _BsIpv6FHSSbtReachLifeTime_Type()
)
bsIpv6FHSSbtReachLifeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsIpv6FHSSbtReachLifeTime.setStatus("current")


class _BsIpv6FHSSbtStaleLifeTime_Type(Integer32):
    """Custom type bsIpv6FHSSbtStaleLifeTime based on Integer32"""
    defaultValue = 86400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_BsIpv6FHSSbtStaleLifeTime_Type.__name__ = "Integer32"
_BsIpv6FHSSbtStaleLifeTime_Object = MibScalar
bsIpv6FHSSbtStaleLifeTime = _BsIpv6FHSSbtStaleLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 1, 7),
    _BsIpv6FHSSbtStaleLifeTime_Type()
)
bsIpv6FHSSbtStaleLifeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsIpv6FHSSbtStaleLifeTime.setStatus("current")


class _BsIpv6FHSSbtDownLifeTime_Type(Integer32):
    """Custom type bsIpv6FHSSbtDownLifeTime based on Integer32"""
    defaultValue = 86400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_BsIpv6FHSSbtDownLifeTime_Type.__name__ = "Integer32"
_BsIpv6FHSSbtDownLifeTime_Object = MibScalar
bsIpv6FHSSbtDownLifeTime = _BsIpv6FHSSbtDownLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 1, 8),
    _BsIpv6FHSSbtDownLifeTime_Type()
)
bsIpv6FHSSbtDownLifeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsIpv6FHSSbtDownLifeTime.setStatus("current")
_BsIpv6FHSSbtTblOverFlow_Type = Counter32
_BsIpv6FHSSbtTblOverFlow_Object = MibScalar
bsIpv6FHSSbtTblOverFlow = _BsIpv6FHSSbtTblOverFlow_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 1, 9),
    _BsIpv6FHSSbtTblOverFlow_Type()
)
bsIpv6FHSSbtTblOverFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsIpv6FHSSbtTblOverFlow.setStatus("current")
_BsIpv6FHSIpv6AccessListTable_Object = MibTable
bsIpv6FHSIpv6AccessListTable = _BsIpv6FHSIpv6AccessListTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 2)
)
if mibBuilder.loadTexts:
    bsIpv6FHSIpv6AccessListTable.setStatus("current")
_BsIpv6FHSIpv6AccessListEntry_Object = MibTableRow
bsIpv6FHSIpv6AccessListEntry = _BsIpv6FHSIpv6AccessListEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 2, 1)
)
bsIpv6FHSIpv6AccessListEntry.setIndexNames(
    (0, "BAYSTACK-IPV6-FIRST-HOP-SEC-MIB", "bsIpv6FHSIpv6AccessListName"),
    (0, "BAYSTACK-IPV6-FIRST-HOP-SEC-MIB", "bsIpv6FHSIpv6AccessListPrefix"),
    (0, "BAYSTACK-IPV6-FIRST-HOP-SEC-MIB", "bsIpv6FHSIpv6AccessListPrefixMaskLen"),
)
if mibBuilder.loadTexts:
    bsIpv6FHSIpv6AccessListEntry.setStatus("current")
_BsIpv6FHSIpv6AccessListName_Type = FhsListName
_BsIpv6FHSIpv6AccessListName_Object = MibTableColumn
bsIpv6FHSIpv6AccessListName = _BsIpv6FHSIpv6AccessListName_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 2, 1, 1),
    _BsIpv6FHSIpv6AccessListName_Type()
)
bsIpv6FHSIpv6AccessListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsIpv6FHSIpv6AccessListName.setStatus("current")
_BsIpv6FHSIpv6AccessListPrefix_Type = Ipv6Address
_BsIpv6FHSIpv6AccessListPrefix_Object = MibTableColumn
bsIpv6FHSIpv6AccessListPrefix = _BsIpv6FHSIpv6AccessListPrefix_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 2, 1, 2),
    _BsIpv6FHSIpv6AccessListPrefix_Type()
)
bsIpv6FHSIpv6AccessListPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsIpv6FHSIpv6AccessListPrefix.setStatus("current")


class _BsIpv6FHSIpv6AccessListPrefixMaskLen_Type(Integer32):
    """Custom type bsIpv6FHSIpv6AccessListPrefixMaskLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_BsIpv6FHSIpv6AccessListPrefixMaskLen_Type.__name__ = "Integer32"
_BsIpv6FHSIpv6AccessListPrefixMaskLen_Object = MibTableColumn
bsIpv6FHSIpv6AccessListPrefixMaskLen = _BsIpv6FHSIpv6AccessListPrefixMaskLen_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 2, 1, 3),
    _BsIpv6FHSIpv6AccessListPrefixMaskLen_Type()
)
bsIpv6FHSIpv6AccessListPrefixMaskLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsIpv6FHSIpv6AccessListPrefixMaskLen.setStatus("current")


class _BsIpv6FHSIpv6AccessListMaskLenFrom_Type(Integer32):
    """Custom type bsIpv6FHSIpv6AccessListMaskLenFrom based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_BsIpv6FHSIpv6AccessListMaskLenFrom_Type.__name__ = "Integer32"
_BsIpv6FHSIpv6AccessListMaskLenFrom_Object = MibTableColumn
bsIpv6FHSIpv6AccessListMaskLenFrom = _BsIpv6FHSIpv6AccessListMaskLenFrom_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 2, 1, 4),
    _BsIpv6FHSIpv6AccessListMaskLenFrom_Type()
)
bsIpv6FHSIpv6AccessListMaskLenFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsIpv6FHSIpv6AccessListMaskLenFrom.setStatus("current")


class _BsIpv6FHSIpv6AccessListMaskLenTo_Type(Integer32):
    """Custom type bsIpv6FHSIpv6AccessListMaskLenTo based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_BsIpv6FHSIpv6AccessListMaskLenTo_Type.__name__ = "Integer32"
_BsIpv6FHSIpv6AccessListMaskLenTo_Object = MibTableColumn
bsIpv6FHSIpv6AccessListMaskLenTo = _BsIpv6FHSIpv6AccessListMaskLenTo_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 2, 1, 5),
    _BsIpv6FHSIpv6AccessListMaskLenTo_Type()
)
bsIpv6FHSIpv6AccessListMaskLenTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsIpv6FHSIpv6AccessListMaskLenTo.setStatus("current")


class _BsIpv6FHSIpv6AccessListAccessType_Type(FhsAccessType):
    """Custom type bsIpv6FHSIpv6AccessListAccessType based on FhsAccessType"""


_BsIpv6FHSIpv6AccessListAccessType_Object = MibTableColumn
bsIpv6FHSIpv6AccessListAccessType = _BsIpv6FHSIpv6AccessListAccessType_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 2, 1, 6),
    _BsIpv6FHSIpv6AccessListAccessType_Type()
)
bsIpv6FHSIpv6AccessListAccessType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsIpv6FHSIpv6AccessListAccessType.setStatus("current")
_BsIpv6FHSIpv6AccessListRowStatus_Type = RowStatus
_BsIpv6FHSIpv6AccessListRowStatus_Object = MibTableColumn
bsIpv6FHSIpv6AccessListRowStatus = _BsIpv6FHSIpv6AccessListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 2, 1, 7),
    _BsIpv6FHSIpv6AccessListRowStatus_Type()
)
bsIpv6FHSIpv6AccessListRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsIpv6FHSIpv6AccessListRowStatus.setStatus("current")
_BsIpv6FHSMacAccessListTable_Object = MibTable
bsIpv6FHSMacAccessListTable = _BsIpv6FHSMacAccessListTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 3)
)
if mibBuilder.loadTexts:
    bsIpv6FHSMacAccessListTable.setStatus("current")
_BsIpv6FHSMacAccessListEntry_Object = MibTableRow
bsIpv6FHSMacAccessListEntry = _BsIpv6FHSMacAccessListEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 3, 3)
)
bsIpv6FHSMacAccessListEntry.setIndexNames(
    (0, "BAYSTACK-IPV6-FIRST-HOP-SEC-MIB", "bsIpv6FHSMacAccessListName"),
    (0, "BAYSTACK-IPV6-FIRST-HOP-SEC-MIB", "bsIpv6FHSMacAccessListMac"),
)
if mibBuilder.loadTexts:
    bsIpv6FHSMacAccessListEntry.setStatus("current")
_BsIpv6FHSMacAccessListName_Type = FhsListName
_BsIpv6FHSMacAccessListName_Object = MibTableColumn
bsIpv6FHSMacAccessListName = _BsIpv6FHSMacAccessListName_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 3, 3, 1),
    _BsIpv6FHSMacAccessListName_Type()
)
bsIpv6FHSMacAccessListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsIpv6FHSMacAccessListName.setStatus("current")
_BsIpv6FHSMacAccessListMac_Type = MacAddress
_BsIpv6FHSMacAccessListMac_Object = MibTableColumn
bsIpv6FHSMacAccessListMac = _BsIpv6FHSMacAccessListMac_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 3, 3, 2),
    _BsIpv6FHSMacAccessListMac_Type()
)
bsIpv6FHSMacAccessListMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsIpv6FHSMacAccessListMac.setStatus("current")


class _BsIpv6FHSMacAccessListAccessType_Type(FhsAccessType):
    """Custom type bsIpv6FHSMacAccessListAccessType based on FhsAccessType"""


_BsIpv6FHSMacAccessListAccessType_Object = MibTableColumn
bsIpv6FHSMacAccessListAccessType = _BsIpv6FHSMacAccessListAccessType_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 3, 3, 3),
    _BsIpv6FHSMacAccessListAccessType_Type()
)
bsIpv6FHSMacAccessListAccessType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsIpv6FHSMacAccessListAccessType.setStatus("current")
_BsIpv6FHSMacAccessListRowStatus_Type = RowStatus
_BsIpv6FHSMacAccessListRowStatus_Object = MibTableColumn
bsIpv6FHSMacAccessListRowStatus = _BsIpv6FHSMacAccessListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 3, 3, 4),
    _BsIpv6FHSMacAccessListRowStatus_Type()
)
bsIpv6FHSMacAccessListRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsIpv6FHSMacAccessListRowStatus.setStatus("current")
_BsIpv6FHSPolicyPortMapTable_Object = MibTable
bsIpv6FHSPolicyPortMapTable = _BsIpv6FHSPolicyPortMapTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 4)
)
if mibBuilder.loadTexts:
    bsIpv6FHSPolicyPortMapTable.setStatus("current")
_BsIpv6FHSPolicyPortMapEntry_Object = MibTableRow
bsIpv6FHSPolicyPortMapEntry = _BsIpv6FHSPolicyPortMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 4, 1)
)
bsIpv6FHSPolicyPortMapEntry.setIndexNames(
    (0, "BAYSTACK-IPV6-FIRST-HOP-SEC-MIB", "bsIpv6FHSPolicyPortMapIfIndex"),
)
if mibBuilder.loadTexts:
    bsIpv6FHSPolicyPortMapEntry.setStatus("current")
_BsIpv6FHSPolicyPortMapIfIndex_Type = InterfaceIndex
_BsIpv6FHSPolicyPortMapIfIndex_Object = MibTableColumn
bsIpv6FHSPolicyPortMapIfIndex = _BsIpv6FHSPolicyPortMapIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 4, 1, 1),
    _BsIpv6FHSPolicyPortMapIfIndex_Type()
)
bsIpv6FHSPolicyPortMapIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsIpv6FHSPolicyPortMapIfIndex.setStatus("current")
_BsIpv6FHSPolicyPortMapDhcpv6gPolicyName_Type = FhsListName
_BsIpv6FHSPolicyPortMapDhcpv6gPolicyName_Object = MibTableColumn
bsIpv6FHSPolicyPortMapDhcpv6gPolicyName = _BsIpv6FHSPolicyPortMapDhcpv6gPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 4, 1, 2),
    _BsIpv6FHSPolicyPortMapDhcpv6gPolicyName_Type()
)
bsIpv6FHSPolicyPortMapDhcpv6gPolicyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsIpv6FHSPolicyPortMapDhcpv6gPolicyName.setStatus("current")
_BsIpv6FHSPolicyPortMapRagPolicyName_Type = FhsListName
_BsIpv6FHSPolicyPortMapRagPolicyName_Object = MibTableColumn
bsIpv6FHSPolicyPortMapRagPolicyName = _BsIpv6FHSPolicyPortMapRagPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 4, 1, 3),
    _BsIpv6FHSPolicyPortMapRagPolicyName_Type()
)
bsIpv6FHSPolicyPortMapRagPolicyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsIpv6FHSPolicyPortMapRagPolicyName.setStatus("current")


class _BsIpv6FHSPolicyPortMapNDAdmin_Type(TruthValue):
    """Custom type bsIpv6FHSPolicyPortMapNDAdmin based on TruthValue"""


_BsIpv6FHSPolicyPortMapNDAdmin_Object = MibTableColumn
bsIpv6FHSPolicyPortMapNDAdmin = _BsIpv6FHSPolicyPortMapNDAdmin_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 4, 1, 4),
    _BsIpv6FHSPolicyPortMapNDAdmin_Type()
)
bsIpv6FHSPolicyPortMapNDAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsIpv6FHSPolicyPortMapNDAdmin.setStatus("current")


class _BsIpv6FHSPolicyPortMapSbtDynLearnAdmin_Type(TruthValue):
    """Custom type bsIpv6FHSPolicyPortMapSbtDynLearnAdmin based on TruthValue"""


_BsIpv6FHSPolicyPortMapSbtDynLearnAdmin_Object = MibTableColumn
bsIpv6FHSPolicyPortMapSbtDynLearnAdmin = _BsIpv6FHSPolicyPortMapSbtDynLearnAdmin_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 4, 1, 5),
    _BsIpv6FHSPolicyPortMapSbtDynLearnAdmin_Type()
)
bsIpv6FHSPolicyPortMapSbtDynLearnAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsIpv6FHSPolicyPortMapSbtDynLearnAdmin.setStatus("current")
_BsIpv6FHSPolicyPortMapTotDhcpv6PktRcv_Type = Counter32
_BsIpv6FHSPolicyPortMapTotDhcpv6PktRcv_Object = MibTableColumn
bsIpv6FHSPolicyPortMapTotDhcpv6PktRcv = _BsIpv6FHSPolicyPortMapTotDhcpv6PktRcv_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 4, 1, 6),
    _BsIpv6FHSPolicyPortMapTotDhcpv6PktRcv_Type()
)
bsIpv6FHSPolicyPortMapTotDhcpv6PktRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsIpv6FHSPolicyPortMapTotDhcpv6PktRcv.setStatus("current")
_BsIpv6FHSPolicyPortMapTotDhcpv6PktDropped_Type = Counter32
_BsIpv6FHSPolicyPortMapTotDhcpv6PktDropped_Object = MibTableColumn
bsIpv6FHSPolicyPortMapTotDhcpv6PktDropped = _BsIpv6FHSPolicyPortMapTotDhcpv6PktDropped_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 4, 1, 7),
    _BsIpv6FHSPolicyPortMapTotDhcpv6PktDropped_Type()
)
bsIpv6FHSPolicyPortMapTotDhcpv6PktDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsIpv6FHSPolicyPortMapTotDhcpv6PktDropped.setStatus("current")
_BsIpv6FHSPolicyPortMapTotRaPktRcv_Type = Counter32
_BsIpv6FHSPolicyPortMapTotRaPktRcv_Object = MibTableColumn
bsIpv6FHSPolicyPortMapTotRaPktRcv = _BsIpv6FHSPolicyPortMapTotRaPktRcv_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 4, 1, 8),
    _BsIpv6FHSPolicyPortMapTotRaPktRcv_Type()
)
bsIpv6FHSPolicyPortMapTotRaPktRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsIpv6FHSPolicyPortMapTotRaPktRcv.setStatus("current")
_BsIpv6FHSPolicyPortMapTotRaPktDropped_Type = Counter32
_BsIpv6FHSPolicyPortMapTotRaPktDropped_Object = MibTableColumn
bsIpv6FHSPolicyPortMapTotRaPktDropped = _BsIpv6FHSPolicyPortMapTotRaPktDropped_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 4, 1, 9),
    _BsIpv6FHSPolicyPortMapTotRaPktDropped_Type()
)
bsIpv6FHSPolicyPortMapTotRaPktDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsIpv6FHSPolicyPortMapTotRaPktDropped.setStatus("current")
_BsIpv6FHSPolicyPortMapTotNdPktRcv_Type = Counter32
_BsIpv6FHSPolicyPortMapTotNdPktRcv_Object = MibTableColumn
bsIpv6FHSPolicyPortMapTotNdPktRcv = _BsIpv6FHSPolicyPortMapTotNdPktRcv_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 4, 1, 10),
    _BsIpv6FHSPolicyPortMapTotNdPktRcv_Type()
)
bsIpv6FHSPolicyPortMapTotNdPktRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsIpv6FHSPolicyPortMapTotNdPktRcv.setStatus("current")
_BsIpv6FHSPolicyPortMapTotNdPktDropped_Type = Counter32
_BsIpv6FHSPolicyPortMapTotNdPktDropped_Object = MibTableColumn
bsIpv6FHSPolicyPortMapTotNdPktDropped = _BsIpv6FHSPolicyPortMapTotNdPktDropped_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 4, 1, 11),
    _BsIpv6FHSPolicyPortMapTotNdPktDropped_Type()
)
bsIpv6FHSPolicyPortMapTotNdPktDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsIpv6FHSPolicyPortMapTotNdPktDropped.setStatus("current")


class _BsIpv6FHSPolicyPortMapClearDhcpGuardStats_Type(TruthValue):
    """Custom type bsIpv6FHSPolicyPortMapClearDhcpGuardStats based on TruthValue"""


_BsIpv6FHSPolicyPortMapClearDhcpGuardStats_Object = MibTableColumn
bsIpv6FHSPolicyPortMapClearDhcpGuardStats = _BsIpv6FHSPolicyPortMapClearDhcpGuardStats_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 4, 1, 12),
    _BsIpv6FHSPolicyPortMapClearDhcpGuardStats_Type()
)
bsIpv6FHSPolicyPortMapClearDhcpGuardStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsIpv6FHSPolicyPortMapClearDhcpGuardStats.setStatus("current")


class _BsIpv6FHSPolicyPortMapClearRaGuardStats_Type(TruthValue):
    """Custom type bsIpv6FHSPolicyPortMapClearRaGuardStats based on TruthValue"""


_BsIpv6FHSPolicyPortMapClearRaGuardStats_Object = MibTableColumn
bsIpv6FHSPolicyPortMapClearRaGuardStats = _BsIpv6FHSPolicyPortMapClearRaGuardStats_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 4, 1, 13),
    _BsIpv6FHSPolicyPortMapClearRaGuardStats_Type()
)
bsIpv6FHSPolicyPortMapClearRaGuardStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsIpv6FHSPolicyPortMapClearRaGuardStats.setStatus("current")


class _BsIpv6FHSPolicyPortMapClearNDInspectStats_Type(TruthValue):
    """Custom type bsIpv6FHSPolicyPortMapClearNDInspectStats based on TruthValue"""


_BsIpv6FHSPolicyPortMapClearNDInspectStats_Object = MibTableColumn
bsIpv6FHSPolicyPortMapClearNDInspectStats = _BsIpv6FHSPolicyPortMapClearNDInspectStats_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 4, 1, 14),
    _BsIpv6FHSPolicyPortMapClearNDInspectStats_Type()
)
bsIpv6FHSPolicyPortMapClearNDInspectStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsIpv6FHSPolicyPortMapClearNDInspectStats.setStatus("current")
_BsIpv6FHSPolicyPortMapRowStatus_Type = RowStatus
_BsIpv6FHSPolicyPortMapRowStatus_Object = MibTableColumn
bsIpv6FHSPolicyPortMapRowStatus = _BsIpv6FHSPolicyPortMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 4, 1, 15),
    _BsIpv6FHSPolicyPortMapRowStatus_Type()
)
bsIpv6FHSPolicyPortMapRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsIpv6FHSPolicyPortMapRowStatus.setStatus("current")
_BsIpv6FHSDhcpv6gPolicyListTable_Object = MibTable
bsIpv6FHSDhcpv6gPolicyListTable = _BsIpv6FHSDhcpv6gPolicyListTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 5)
)
if mibBuilder.loadTexts:
    bsIpv6FHSDhcpv6gPolicyListTable.setStatus("current")
_BsIpv6FHSDhcpv6gPolicyListEntry_Object = MibTableRow
bsIpv6FHSDhcpv6gPolicyListEntry = _BsIpv6FHSDhcpv6gPolicyListEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 5, 1)
)
bsIpv6FHSDhcpv6gPolicyListEntry.setIndexNames(
    (0, "BAYSTACK-IPV6-FIRST-HOP-SEC-MIB", "bsIpv6FHSDhcpv6gPolicyName"),
)
if mibBuilder.loadTexts:
    bsIpv6FHSDhcpv6gPolicyListEntry.setStatus("current")
_BsIpv6FHSDhcpv6gPolicyName_Type = FhsListName
_BsIpv6FHSDhcpv6gPolicyName_Object = MibTableColumn
bsIpv6FHSDhcpv6gPolicyName = _BsIpv6FHSDhcpv6gPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 5, 1, 1),
    _BsIpv6FHSDhcpv6gPolicyName_Type()
)
bsIpv6FHSDhcpv6gPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsIpv6FHSDhcpv6gPolicyName.setStatus("current")
_BsIpv6FHSDhcpv6gDeviceRole_Type = FhsDhcpv6GuardDeviceRole
_BsIpv6FHSDhcpv6gDeviceRole_Object = MibTableColumn
bsIpv6FHSDhcpv6gDeviceRole = _BsIpv6FHSDhcpv6gDeviceRole_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 5, 1, 2),
    _BsIpv6FHSDhcpv6gDeviceRole_Type()
)
bsIpv6FHSDhcpv6gDeviceRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsIpv6FHSDhcpv6gDeviceRole.setStatus("current")
_BsIpv6FHSDhcpv6gServerAccessListName_Type = FhsListName
_BsIpv6FHSDhcpv6gServerAccessListName_Object = MibTableColumn
bsIpv6FHSDhcpv6gServerAccessListName = _BsIpv6FHSDhcpv6gServerAccessListName_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 5, 1, 3),
    _BsIpv6FHSDhcpv6gServerAccessListName_Type()
)
bsIpv6FHSDhcpv6gServerAccessListName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsIpv6FHSDhcpv6gServerAccessListName.setStatus("current")
_BsIpv6FHSDhcpv6gReplyPrefixListName_Type = FhsListName
_BsIpv6FHSDhcpv6gReplyPrefixListName_Object = MibTableColumn
bsIpv6FHSDhcpv6gReplyPrefixListName = _BsIpv6FHSDhcpv6gReplyPrefixListName_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 5, 1, 4),
    _BsIpv6FHSDhcpv6gReplyPrefixListName_Type()
)
bsIpv6FHSDhcpv6gReplyPrefixListName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsIpv6FHSDhcpv6gReplyPrefixListName.setStatus("current")


class _BsIpv6FHSDhcpv6gPrefLimitMin_Type(Integer32):
    """Custom type bsIpv6FHSDhcpv6gPrefLimitMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BsIpv6FHSDhcpv6gPrefLimitMin_Type.__name__ = "Integer32"
_BsIpv6FHSDhcpv6gPrefLimitMin_Object = MibTableColumn
bsIpv6FHSDhcpv6gPrefLimitMin = _BsIpv6FHSDhcpv6gPrefLimitMin_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 5, 1, 5),
    _BsIpv6FHSDhcpv6gPrefLimitMin_Type()
)
bsIpv6FHSDhcpv6gPrefLimitMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsIpv6FHSDhcpv6gPrefLimitMin.setStatus("current")


class _BsIpv6FHSDhcpv6gPrefLimitMax_Type(Integer32):
    """Custom type bsIpv6FHSDhcpv6gPrefLimitMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BsIpv6FHSDhcpv6gPrefLimitMax_Type.__name__ = "Integer32"
_BsIpv6FHSDhcpv6gPrefLimitMax_Object = MibTableColumn
bsIpv6FHSDhcpv6gPrefLimitMax = _BsIpv6FHSDhcpv6gPrefLimitMax_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 5, 1, 6),
    _BsIpv6FHSDhcpv6gPrefLimitMax_Type()
)
bsIpv6FHSDhcpv6gPrefLimitMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsIpv6FHSDhcpv6gPrefLimitMax.setStatus("current")
_BsIpv6FHSDhcpv6gPolicyListRowStatus_Type = RowStatus
_BsIpv6FHSDhcpv6gPolicyListRowStatus_Object = MibTableColumn
bsIpv6FHSDhcpv6gPolicyListRowStatus = _BsIpv6FHSDhcpv6gPolicyListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 5, 1, 7),
    _BsIpv6FHSDhcpv6gPolicyListRowStatus_Type()
)
bsIpv6FHSDhcpv6gPolicyListRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsIpv6FHSDhcpv6gPolicyListRowStatus.setStatus("current")
_BsIpv6FHSRagPolicyListTable_Object = MibTable
bsIpv6FHSRagPolicyListTable = _BsIpv6FHSRagPolicyListTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 6)
)
if mibBuilder.loadTexts:
    bsIpv6FHSRagPolicyListTable.setStatus("current")
_BsIpv6FHSRagPolicyListEntry_Object = MibTableRow
bsIpv6FHSRagPolicyListEntry = _BsIpv6FHSRagPolicyListEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 6, 1)
)
bsIpv6FHSRagPolicyListEntry.setIndexNames(
    (0, "BAYSTACK-IPV6-FIRST-HOP-SEC-MIB", "bsIpv6FHSRagPolicyName"),
)
if mibBuilder.loadTexts:
    bsIpv6FHSRagPolicyListEntry.setStatus("current")
_BsIpv6FHSRagPolicyName_Type = FhsListName
_BsIpv6FHSRagPolicyName_Object = MibTableColumn
bsIpv6FHSRagPolicyName = _BsIpv6FHSRagPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 6, 1, 1),
    _BsIpv6FHSRagPolicyName_Type()
)
bsIpv6FHSRagPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsIpv6FHSRagPolicyName.setStatus("current")


class _BsIpv6FHSRagDeviceRole_Type(FhsRaGuardDeviceRole):
    """Custom type bsIpv6FHSRagDeviceRole based on FhsRaGuardDeviceRole"""


_BsIpv6FHSRagDeviceRole_Object = MibTableColumn
bsIpv6FHSRagDeviceRole = _BsIpv6FHSRagDeviceRole_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 6, 1, 2),
    _BsIpv6FHSRagDeviceRole_Type()
)
bsIpv6FHSRagDeviceRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsIpv6FHSRagDeviceRole.setStatus("current")
_BsIpv6FHSRagIpv6AccessListName_Type = FhsListName
_BsIpv6FHSRagIpv6AccessListName_Object = MibTableColumn
bsIpv6FHSRagIpv6AccessListName = _BsIpv6FHSRagIpv6AccessListName_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 6, 1, 3),
    _BsIpv6FHSRagIpv6AccessListName_Type()
)
bsIpv6FHSRagIpv6AccessListName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsIpv6FHSRagIpv6AccessListName.setStatus("current")
_BsIpv6FHSRagIpv6PrefixListName_Type = FhsListName
_BsIpv6FHSRagIpv6PrefixListName_Object = MibTableColumn
bsIpv6FHSRagIpv6PrefixListName = _BsIpv6FHSRagIpv6PrefixListName_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 6, 1, 4),
    _BsIpv6FHSRagIpv6PrefixListName_Type()
)
bsIpv6FHSRagIpv6PrefixListName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsIpv6FHSRagIpv6PrefixListName.setStatus("current")
_BsIpv6FHSRagMacListName_Type = FhsListName
_BsIpv6FHSRagMacListName_Object = MibTableColumn
bsIpv6FHSRagMacListName = _BsIpv6FHSRagMacListName_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 6, 1, 5),
    _BsIpv6FHSRagMacListName_Type()
)
bsIpv6FHSRagMacListName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsIpv6FHSRagMacListName.setStatus("current")
_BsIpv6FHSRagManagedConfigFlag_Type = FhsRaManagedConfigFlag
_BsIpv6FHSRagManagedConfigFlag_Object = MibTableColumn
bsIpv6FHSRagManagedConfigFlag = _BsIpv6FHSRagManagedConfigFlag_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 6, 1, 6),
    _BsIpv6FHSRagManagedConfigFlag_Type()
)
bsIpv6FHSRagManagedConfigFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsIpv6FHSRagManagedConfigFlag.setStatus("current")


class _BsIpv6FHSRagRouterPrefMax_Type(FhsRaRouterPrefMax):
    """Custom type bsIpv6FHSRagRouterPrefMax based on FhsRaRouterPrefMax"""


_BsIpv6FHSRagRouterPrefMax_Object = MibTableColumn
bsIpv6FHSRagRouterPrefMax = _BsIpv6FHSRagRouterPrefMax_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 6, 1, 7),
    _BsIpv6FHSRagRouterPrefMax_Type()
)
bsIpv6FHSRagRouterPrefMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsIpv6FHSRagRouterPrefMax.setStatus("current")


class _BsIpv6FHSRagHopLimitMin_Type(Integer32):
    """Custom type bsIpv6FHSRagHopLimitMin based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BsIpv6FHSRagHopLimitMin_Type.__name__ = "Integer32"
_BsIpv6FHSRagHopLimitMin_Object = MibTableColumn
bsIpv6FHSRagHopLimitMin = _BsIpv6FHSRagHopLimitMin_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 6, 1, 8),
    _BsIpv6FHSRagHopLimitMin_Type()
)
bsIpv6FHSRagHopLimitMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsIpv6FHSRagHopLimitMin.setStatus("current")


class _BsIpv6FHSRagHopLimitMax_Type(Integer32):
    """Custom type bsIpv6FHSRagHopLimitMax based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BsIpv6FHSRagHopLimitMax_Type.__name__ = "Integer32"
_BsIpv6FHSRagHopLimitMax_Object = MibTableColumn
bsIpv6FHSRagHopLimitMax = _BsIpv6FHSRagHopLimitMax_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 6, 1, 9),
    _BsIpv6FHSRagHopLimitMax_Type()
)
bsIpv6FHSRagHopLimitMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsIpv6FHSRagHopLimitMax.setStatus("current")
_BsIpv6FHSRagPolicyListRowStatus_Type = RowStatus
_BsIpv6FHSRagPolicyListRowStatus_Object = MibTableColumn
bsIpv6FHSRagPolicyListRowStatus = _BsIpv6FHSRagPolicyListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 6, 1, 10),
    _BsIpv6FHSRagPolicyListRowStatus_Type()
)
bsIpv6FHSRagPolicyListRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsIpv6FHSRagPolicyListRowStatus.setStatus("current")
_BsIpv6FHSSbtTable_Object = MibTable
bsIpv6FHSSbtTable = _BsIpv6FHSSbtTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 7)
)
if mibBuilder.loadTexts:
    bsIpv6FHSSbtTable.setStatus("current")
_BsIpv6FHSSbtListEntry_Object = MibTableRow
bsIpv6FHSSbtListEntry = _BsIpv6FHSSbtListEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 7, 1)
)
bsIpv6FHSSbtListEntry.setIndexNames(
    (0, "BAYSTACK-IPV6-FIRST-HOP-SEC-MIB", "bsIpv6FHSSbtInterfaceIndex"),
    (0, "BAYSTACK-IPV6-FIRST-HOP-SEC-MIB", "bsIpv6FHSSbtVlan"),
    (0, "BAYSTACK-IPV6-FIRST-HOP-SEC-MIB", "bsIpv6FHSSbtSrcIp"),
)
if mibBuilder.loadTexts:
    bsIpv6FHSSbtListEntry.setStatus("current")
_BsIpv6FHSSbtInterfaceIndex_Type = InterfaceIndex
_BsIpv6FHSSbtInterfaceIndex_Object = MibTableColumn
bsIpv6FHSSbtInterfaceIndex = _BsIpv6FHSSbtInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 7, 1, 1),
    _BsIpv6FHSSbtInterfaceIndex_Type()
)
bsIpv6FHSSbtInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsIpv6FHSSbtInterfaceIndex.setStatus("current")


class _BsIpv6FHSSbtVlan_Type(Integer32):
    """Custom type bsIpv6FHSSbtVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_BsIpv6FHSSbtVlan_Type.__name__ = "Integer32"
_BsIpv6FHSSbtVlan_Object = MibTableColumn
bsIpv6FHSSbtVlan = _BsIpv6FHSSbtVlan_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 7, 1, 2),
    _BsIpv6FHSSbtVlan_Type()
)
bsIpv6FHSSbtVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsIpv6FHSSbtVlan.setStatus("current")
_BsIpv6FHSSbtSrcIp_Type = Ipv6Address
_BsIpv6FHSSbtSrcIp_Object = MibTableColumn
bsIpv6FHSSbtSrcIp = _BsIpv6FHSSbtSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 7, 1, 3),
    _BsIpv6FHSSbtSrcIp_Type()
)
bsIpv6FHSSbtSrcIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsIpv6FHSSbtSrcIp.setStatus("current")
_BsIpv6FHSSbtLinkLayerAddress_Type = MacAddress
_BsIpv6FHSSbtLinkLayerAddress_Object = MibTableColumn
bsIpv6FHSSbtLinkLayerAddress = _BsIpv6FHSSbtLinkLayerAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 7, 1, 4),
    _BsIpv6FHSSbtLinkLayerAddress_Type()
)
bsIpv6FHSSbtLinkLayerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsIpv6FHSSbtLinkLayerAddress.setStatus("current")
_BsIpv6FHSSbtLearnType_Type = FhsSbtType
_BsIpv6FHSSbtLearnType_Object = MibTableColumn
bsIpv6FHSSbtLearnType = _BsIpv6FHSSbtLearnType_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 7, 1, 5),
    _BsIpv6FHSSbtLearnType_Type()
)
bsIpv6FHSSbtLearnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsIpv6FHSSbtLearnType.setStatus("current")
_BsIpv6FHSSbtLearnPriority_Type = Integer32
_BsIpv6FHSSbtLearnPriority_Object = MibTableColumn
bsIpv6FHSSbtLearnPriority = _BsIpv6FHSSbtLearnPriority_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 7, 1, 6),
    _BsIpv6FHSSbtLearnPriority_Type()
)
bsIpv6FHSSbtLearnPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsIpv6FHSSbtLearnPriority.setStatus("current")
_BsIpv6FHSSbtLearnState_Type = FhsSbtState
_BsIpv6FHSSbtLearnState_Object = MibTableColumn
bsIpv6FHSSbtLearnState = _BsIpv6FHSSbtLearnState_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 7, 1, 7),
    _BsIpv6FHSSbtLearnState_Type()
)
bsIpv6FHSSbtLearnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsIpv6FHSSbtLearnState.setStatus("current")
_BsIpv6FHSSbtLearnAge_Type = Integer32
_BsIpv6FHSSbtLearnAge_Object = MibTableColumn
bsIpv6FHSSbtLearnAge = _BsIpv6FHSSbtLearnAge_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 7, 1, 8),
    _BsIpv6FHSSbtLearnAge_Type()
)
bsIpv6FHSSbtLearnAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsIpv6FHSSbtLearnAge.setStatus("current")
_BsIpv6FHSSbtRowStatus_Type = RowStatus
_BsIpv6FHSSbtRowStatus_Object = MibTableColumn
bsIpv6FHSSbtRowStatus = _BsIpv6FHSSbtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 7, 1, 9),
    _BsIpv6FHSSbtRowStatus_Type()
)
bsIpv6FHSSbtRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsIpv6FHSSbtRowStatus.setStatus("current")
_BsIpv6NDTrapNotificationObjects_ObjectIdentity = ObjectIdentity
bsIpv6NDTrapNotificationObjects = _BsIpv6NDTrapNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 8)
)
_BsIpv6NDInspectionNotificationClientMACAddr_Type = MacAddress
_BsIpv6NDInspectionNotificationClientMACAddr_Object = MibScalar
bsIpv6NDInspectionNotificationClientMACAddr = _BsIpv6NDInspectionNotificationClientMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 8, 1),
    _BsIpv6NDInspectionNotificationClientMACAddr_Type()
)
bsIpv6NDInspectionNotificationClientMACAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsIpv6NDInspectionNotificationClientMACAddr.setStatus("current")


class _BsIpv6NDInspectionNotificationMsgType_Type(Integer32):
    """Custom type bsIpv6NDInspectionNotificationMsgType based on Integer32"""
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
        *(("ipv6NDNA", 2),
          ("ipv6NDNS", 1),
          ("ipv6NDRA", 4),
          ("ipv6NDRS", 3),
          ("ipv6NDRedir", 5))
    )


_BsIpv6NDInspectionNotificationMsgType_Type.__name__ = "Integer32"
_BsIpv6NDInspectionNotificationMsgType_Object = MibScalar
bsIpv6NDInspectionNotificationMsgType = _BsIpv6NDInspectionNotificationMsgType_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 8, 2),
    _BsIpv6NDInspectionNotificationMsgType_Type()
)
bsIpv6NDInspectionNotificationMsgType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsIpv6NDInspectionNotificationMsgType.setStatus("current")
_BsIpv6FHSNDInterfaceIndex_Type = InterfaceIndex
_BsIpv6FHSNDInterfaceIndex_Object = MibScalar
bsIpv6FHSNDInterfaceIndex = _BsIpv6FHSNDInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 8, 3),
    _BsIpv6FHSNDInterfaceIndex_Type()
)
bsIpv6FHSNDInterfaceIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsIpv6FHSNDInterfaceIndex.setStatus("current")
_BsIpv6FHSNDIpv6Address_Type = Ipv6Address
_BsIpv6FHSNDIpv6Address_Object = MibScalar
bsIpv6FHSNDIpv6Address = _BsIpv6FHSNDIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 8, 4),
    _BsIpv6FHSNDIpv6Address_Type()
)
bsIpv6FHSNDIpv6Address.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsIpv6FHSNDIpv6Address.setStatus("current")


class _BsIpv6FHSNDVlanID_Type(Integer32):
    """Custom type bsIpv6FHSNDVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_BsIpv6FHSNDVlanID_Type.__name__ = "Integer32"
_BsIpv6FHSNDVlanID_Object = MibScalar
bsIpv6FHSNDVlanID = _BsIpv6FHSNDVlanID_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 8, 5),
    _BsIpv6FHSNDVlanID_Type()
)
bsIpv6FHSNDVlanID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsIpv6FHSNDVlanID.setStatus("current")
_BsIpv6FHSSourceGuardInterfaceConfigTable_Object = MibTable
bsIpv6FHSSourceGuardInterfaceConfigTable = _BsIpv6FHSSourceGuardInterfaceConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 9)
)
if mibBuilder.loadTexts:
    bsIpv6FHSSourceGuardInterfaceConfigTable.setStatus("current")
_BsIpv6FHSSourceGuardInterfaceConfigEntry_Object = MibTableRow
bsIpv6FHSSourceGuardInterfaceConfigEntry = _BsIpv6FHSSourceGuardInterfaceConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 9, 1)
)
bsIpv6FHSSourceGuardInterfaceConfigEntry.setIndexNames(
    (0, "BAYSTACK-IPV6-FIRST-HOP-SEC-MIB", "bsIpv6FHSSourceGuardIfIndex"),
)
if mibBuilder.loadTexts:
    bsIpv6FHSSourceGuardInterfaceConfigEntry.setStatus("current")
_BsIpv6FHSSourceGuardIfIndex_Type = InterfaceIndex
_BsIpv6FHSSourceGuardIfIndex_Object = MibTableColumn
bsIpv6FHSSourceGuardIfIndex = _BsIpv6FHSSourceGuardIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 9, 1, 1),
    _BsIpv6FHSSourceGuardIfIndex_Type()
)
bsIpv6FHSSourceGuardIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsIpv6FHSSourceGuardIfIndex.setStatus("current")


class _BsIpv6FHSSourceGuardInterfaceState_Type(TruthValue):
    """Custom type bsIpv6FHSSourceGuardInterfaceState based on TruthValue"""


_BsIpv6FHSSourceGuardInterfaceState_Object = MibTableColumn
bsIpv6FHSSourceGuardInterfaceState = _BsIpv6FHSSourceGuardInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 9, 1, 2),
    _BsIpv6FHSSourceGuardInterfaceState_Type()
)
bsIpv6FHSSourceGuardInterfaceState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsIpv6FHSSourceGuardInterfaceState.setStatus("current")


class _BsIpv6FHSSourceGuardMaxAddr_Type(Integer32):
    """Custom type bsIpv6FHSSourceGuardMaxAddr based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_BsIpv6FHSSourceGuardMaxAddr_Type.__name__ = "Integer32"
_BsIpv6FHSSourceGuardMaxAddr_Object = MibTableColumn
bsIpv6FHSSourceGuardMaxAddr = _BsIpv6FHSSourceGuardMaxAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 9, 1, 3),
    _BsIpv6FHSSourceGuardMaxAddr_Type()
)
bsIpv6FHSSourceGuardMaxAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsIpv6FHSSourceGuardMaxAddr.setStatus("current")
_BsIpv6FHSSourceGuardOverflowCount_Type = Counter32
_BsIpv6FHSSourceGuardOverflowCount_Object = MibTableColumn
bsIpv6FHSSourceGuardOverflowCount = _BsIpv6FHSSourceGuardOverflowCount_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 9, 1, 4),
    _BsIpv6FHSSourceGuardOverflowCount_Type()
)
bsIpv6FHSSourceGuardOverflowCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsIpv6FHSSourceGuardOverflowCount.setStatus("current")
_BsIpv6FHSSourceGuardClearOverflowCount_Type = TruthValue
_BsIpv6FHSSourceGuardClearOverflowCount_Object = MibTableColumn
bsIpv6FHSSourceGuardClearOverflowCount = _BsIpv6FHSSourceGuardClearOverflowCount_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 9, 1, 5),
    _BsIpv6FHSSourceGuardClearOverflowCount_Type()
)
bsIpv6FHSSourceGuardClearOverflowCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsIpv6FHSSourceGuardClearOverflowCount.setStatus("current")
_BsIpv6FHSSourceGuardBindingTable_Object = MibTable
bsIpv6FHSSourceGuardBindingTable = _BsIpv6FHSSourceGuardBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 10)
)
if mibBuilder.loadTexts:
    bsIpv6FHSSourceGuardBindingTable.setStatus("current")
_BsIpv6FHSSourceGuardBindingEntry_Object = MibTableRow
bsIpv6FHSSourceGuardBindingEntry = _BsIpv6FHSSourceGuardBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 10, 1)
)
bsIpv6FHSSourceGuardBindingEntry.setIndexNames(
    (0, "BAYSTACK-IPV6-FIRST-HOP-SEC-MIB", "bsIpv6FHSSourceGuardEntryIfIndex"),
    (0, "BAYSTACK-IPV6-FIRST-HOP-SEC-MIB", "bsIpv6FHSSourceGuardEntryIpv6Addr"),
)
if mibBuilder.loadTexts:
    bsIpv6FHSSourceGuardBindingEntry.setStatus("current")
_BsIpv6FHSSourceGuardEntryIfIndex_Type = InterfaceIndex
_BsIpv6FHSSourceGuardEntryIfIndex_Object = MibTableColumn
bsIpv6FHSSourceGuardEntryIfIndex = _BsIpv6FHSSourceGuardEntryIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 10, 1, 1),
    _BsIpv6FHSSourceGuardEntryIfIndex_Type()
)
bsIpv6FHSSourceGuardEntryIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsIpv6FHSSourceGuardEntryIfIndex.setStatus("current")
_BsIpv6FHSSourceGuardEntryIpv6Addr_Type = Ipv6Address
_BsIpv6FHSSourceGuardEntryIpv6Addr_Object = MibTableColumn
bsIpv6FHSSourceGuardEntryIpv6Addr = _BsIpv6FHSSourceGuardEntryIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 1, 10, 1, 2),
    _BsIpv6FHSSourceGuardEntryIpv6Addr_Type()
)
bsIpv6FHSSourceGuardEntryIpv6Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsIpv6FHSSourceGuardEntryIpv6Addr.setStatus("current")

# Managed Objects groups


# Notification objects

bsIpv6NDSBTTableFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 0, 1)
)
bsIpv6NDSBTTableFull.setObjects(
      *(("BAYSTACK-IPV6-FIRST-HOP-SEC-MIB", "bsIpv6NDInspectionNotificationClientMACAddr"),
        ("BAYSTACK-IPV6-FIRST-HOP-SEC-MIB", "bsIpv6NDInspectionNotificationMsgType"),
        ("BAYSTACK-IPV6-FIRST-HOP-SEC-MIB", "bsIpv6FHSNDInterfaceIndex"),
        ("BAYSTACK-IPV6-FIRST-HOP-SEC-MIB", "bsIpv6FHSNDIpv6Address"),
        ("BAYSTACK-IPV6-FIRST-HOP-SEC-MIB", "bsIpv6FHSNDVlanID"))
)
if mibBuilder.loadTexts:
    bsIpv6NDSBTTableFull.setStatus(
        "current"
    )

bsIpv6NDNotificationsUntrustedPort = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 45, 0, 2)
)
bsIpv6NDNotificationsUntrustedPort.setObjects(
      *(("BAYSTACK-IPV6-FIRST-HOP-SEC-MIB", "bsIpv6NDInspectionNotificationClientMACAddr"),
        ("BAYSTACK-IPV6-FIRST-HOP-SEC-MIB", "bsIpv6NDInspectionNotificationMsgType"),
        ("BAYSTACK-IPV6-FIRST-HOP-SEC-MIB", "bsIpv6FHSNDInterfaceIndex"),
        ("BAYSTACK-IPV6-FIRST-HOP-SEC-MIB", "bsIpv6FHSNDIpv6Address"),
        ("BAYSTACK-IPV6-FIRST-HOP-SEC-MIB", "bsIpv6FHSNDVlanID"))
)
if mibBuilder.loadTexts:
    bsIpv6NDNotificationsUntrustedPort.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BAYSTACK-IPV6-FIRST-HOP-SEC-MIB",
    **{"FhsRaGuardDeviceRole": FhsRaGuardDeviceRole,
       "FhsRaManagedConfigFlag": FhsRaManagedConfigFlag,
       "FhsRaRouterPrefMax": FhsRaRouterPrefMax,
       "FhsDhcpv6GuardDeviceRole": FhsDhcpv6GuardDeviceRole,
       "FhsListName": FhsListName,
       "FhsAccessType": FhsAccessType,
       "FhsSbtState": FhsSbtState,
       "FhsSbtType": FhsSbtType,
       "bayStackIpv6FirstHopSecMib": bayStackIpv6FirstHopSecMib,
       "bsIpv6FirstHopSecNotifications": bsIpv6FirstHopSecNotifications,
       "bsIpv6NDSBTTableFull": bsIpv6NDSBTTableFull,
       "bsIpv6NDNotificationsUntrustedPort": bsIpv6NDNotificationsUntrustedPort,
       "bsIpv6FirstHopSecObjects": bsIpv6FirstHopSecObjects,
       "bsIpv6FHSScalVar": bsIpv6FHSScalVar,
       "bsIpv6FHSAdmin": bsIpv6FHSAdmin,
       "bsIpv6FHSRagAdmin": bsIpv6FHSRagAdmin,
       "bsIpv6FHSDhcpv6gAdmin": bsIpv6FHSDhcpv6gAdmin,
       "bsIpv6FHSNdInspectAdmin": bsIpv6FHSNdInspectAdmin,
       "bsIpv6FHSMaxDynSbtEntries": bsIpv6FHSMaxDynSbtEntries,
       "bsIpv6FHSSbtReachLifeTime": bsIpv6FHSSbtReachLifeTime,
       "bsIpv6FHSSbtStaleLifeTime": bsIpv6FHSSbtStaleLifeTime,
       "bsIpv6FHSSbtDownLifeTime": bsIpv6FHSSbtDownLifeTime,
       "bsIpv6FHSSbtTblOverFlow": bsIpv6FHSSbtTblOverFlow,
       "bsIpv6FHSIpv6AccessListTable": bsIpv6FHSIpv6AccessListTable,
       "bsIpv6FHSIpv6AccessListEntry": bsIpv6FHSIpv6AccessListEntry,
       "bsIpv6FHSIpv6AccessListName": bsIpv6FHSIpv6AccessListName,
       "bsIpv6FHSIpv6AccessListPrefix": bsIpv6FHSIpv6AccessListPrefix,
       "bsIpv6FHSIpv6AccessListPrefixMaskLen": bsIpv6FHSIpv6AccessListPrefixMaskLen,
       "bsIpv6FHSIpv6AccessListMaskLenFrom": bsIpv6FHSIpv6AccessListMaskLenFrom,
       "bsIpv6FHSIpv6AccessListMaskLenTo": bsIpv6FHSIpv6AccessListMaskLenTo,
       "bsIpv6FHSIpv6AccessListAccessType": bsIpv6FHSIpv6AccessListAccessType,
       "bsIpv6FHSIpv6AccessListRowStatus": bsIpv6FHSIpv6AccessListRowStatus,
       "bsIpv6FHSMacAccessListTable": bsIpv6FHSMacAccessListTable,
       "bsIpv6FHSMacAccessListEntry": bsIpv6FHSMacAccessListEntry,
       "bsIpv6FHSMacAccessListName": bsIpv6FHSMacAccessListName,
       "bsIpv6FHSMacAccessListMac": bsIpv6FHSMacAccessListMac,
       "bsIpv6FHSMacAccessListAccessType": bsIpv6FHSMacAccessListAccessType,
       "bsIpv6FHSMacAccessListRowStatus": bsIpv6FHSMacAccessListRowStatus,
       "bsIpv6FHSPolicyPortMapTable": bsIpv6FHSPolicyPortMapTable,
       "bsIpv6FHSPolicyPortMapEntry": bsIpv6FHSPolicyPortMapEntry,
       "bsIpv6FHSPolicyPortMapIfIndex": bsIpv6FHSPolicyPortMapIfIndex,
       "bsIpv6FHSPolicyPortMapDhcpv6gPolicyName": bsIpv6FHSPolicyPortMapDhcpv6gPolicyName,
       "bsIpv6FHSPolicyPortMapRagPolicyName": bsIpv6FHSPolicyPortMapRagPolicyName,
       "bsIpv6FHSPolicyPortMapNDAdmin": bsIpv6FHSPolicyPortMapNDAdmin,
       "bsIpv6FHSPolicyPortMapSbtDynLearnAdmin": bsIpv6FHSPolicyPortMapSbtDynLearnAdmin,
       "bsIpv6FHSPolicyPortMapTotDhcpv6PktRcv": bsIpv6FHSPolicyPortMapTotDhcpv6PktRcv,
       "bsIpv6FHSPolicyPortMapTotDhcpv6PktDropped": bsIpv6FHSPolicyPortMapTotDhcpv6PktDropped,
       "bsIpv6FHSPolicyPortMapTotRaPktRcv": bsIpv6FHSPolicyPortMapTotRaPktRcv,
       "bsIpv6FHSPolicyPortMapTotRaPktDropped": bsIpv6FHSPolicyPortMapTotRaPktDropped,
       "bsIpv6FHSPolicyPortMapTotNdPktRcv": bsIpv6FHSPolicyPortMapTotNdPktRcv,
       "bsIpv6FHSPolicyPortMapTotNdPktDropped": bsIpv6FHSPolicyPortMapTotNdPktDropped,
       "bsIpv6FHSPolicyPortMapClearDhcpGuardStats": bsIpv6FHSPolicyPortMapClearDhcpGuardStats,
       "bsIpv6FHSPolicyPortMapClearRaGuardStats": bsIpv6FHSPolicyPortMapClearRaGuardStats,
       "bsIpv6FHSPolicyPortMapClearNDInspectStats": bsIpv6FHSPolicyPortMapClearNDInspectStats,
       "bsIpv6FHSPolicyPortMapRowStatus": bsIpv6FHSPolicyPortMapRowStatus,
       "bsIpv6FHSDhcpv6gPolicyListTable": bsIpv6FHSDhcpv6gPolicyListTable,
       "bsIpv6FHSDhcpv6gPolicyListEntry": bsIpv6FHSDhcpv6gPolicyListEntry,
       "bsIpv6FHSDhcpv6gPolicyName": bsIpv6FHSDhcpv6gPolicyName,
       "bsIpv6FHSDhcpv6gDeviceRole": bsIpv6FHSDhcpv6gDeviceRole,
       "bsIpv6FHSDhcpv6gServerAccessListName": bsIpv6FHSDhcpv6gServerAccessListName,
       "bsIpv6FHSDhcpv6gReplyPrefixListName": bsIpv6FHSDhcpv6gReplyPrefixListName,
       "bsIpv6FHSDhcpv6gPrefLimitMin": bsIpv6FHSDhcpv6gPrefLimitMin,
       "bsIpv6FHSDhcpv6gPrefLimitMax": bsIpv6FHSDhcpv6gPrefLimitMax,
       "bsIpv6FHSDhcpv6gPolicyListRowStatus": bsIpv6FHSDhcpv6gPolicyListRowStatus,
       "bsIpv6FHSRagPolicyListTable": bsIpv6FHSRagPolicyListTable,
       "bsIpv6FHSRagPolicyListEntry": bsIpv6FHSRagPolicyListEntry,
       "bsIpv6FHSRagPolicyName": bsIpv6FHSRagPolicyName,
       "bsIpv6FHSRagDeviceRole": bsIpv6FHSRagDeviceRole,
       "bsIpv6FHSRagIpv6AccessListName": bsIpv6FHSRagIpv6AccessListName,
       "bsIpv6FHSRagIpv6PrefixListName": bsIpv6FHSRagIpv6PrefixListName,
       "bsIpv6FHSRagMacListName": bsIpv6FHSRagMacListName,
       "bsIpv6FHSRagManagedConfigFlag": bsIpv6FHSRagManagedConfigFlag,
       "bsIpv6FHSRagRouterPrefMax": bsIpv6FHSRagRouterPrefMax,
       "bsIpv6FHSRagHopLimitMin": bsIpv6FHSRagHopLimitMin,
       "bsIpv6FHSRagHopLimitMax": bsIpv6FHSRagHopLimitMax,
       "bsIpv6FHSRagPolicyListRowStatus": bsIpv6FHSRagPolicyListRowStatus,
       "bsIpv6FHSSbtTable": bsIpv6FHSSbtTable,
       "bsIpv6FHSSbtListEntry": bsIpv6FHSSbtListEntry,
       "bsIpv6FHSSbtInterfaceIndex": bsIpv6FHSSbtInterfaceIndex,
       "bsIpv6FHSSbtVlan": bsIpv6FHSSbtVlan,
       "bsIpv6FHSSbtSrcIp": bsIpv6FHSSbtSrcIp,
       "bsIpv6FHSSbtLinkLayerAddress": bsIpv6FHSSbtLinkLayerAddress,
       "bsIpv6FHSSbtLearnType": bsIpv6FHSSbtLearnType,
       "bsIpv6FHSSbtLearnPriority": bsIpv6FHSSbtLearnPriority,
       "bsIpv6FHSSbtLearnState": bsIpv6FHSSbtLearnState,
       "bsIpv6FHSSbtLearnAge": bsIpv6FHSSbtLearnAge,
       "bsIpv6FHSSbtRowStatus": bsIpv6FHSSbtRowStatus,
       "bsIpv6NDTrapNotificationObjects": bsIpv6NDTrapNotificationObjects,
       "bsIpv6NDInspectionNotificationClientMACAddr": bsIpv6NDInspectionNotificationClientMACAddr,
       "bsIpv6NDInspectionNotificationMsgType": bsIpv6NDInspectionNotificationMsgType,
       "bsIpv6FHSNDInterfaceIndex": bsIpv6FHSNDInterfaceIndex,
       "bsIpv6FHSNDIpv6Address": bsIpv6FHSNDIpv6Address,
       "bsIpv6FHSNDVlanID": bsIpv6FHSNDVlanID,
       "bsIpv6FHSSourceGuardInterfaceConfigTable": bsIpv6FHSSourceGuardInterfaceConfigTable,
       "bsIpv6FHSSourceGuardInterfaceConfigEntry": bsIpv6FHSSourceGuardInterfaceConfigEntry,
       "bsIpv6FHSSourceGuardIfIndex": bsIpv6FHSSourceGuardIfIndex,
       "bsIpv6FHSSourceGuardInterfaceState": bsIpv6FHSSourceGuardInterfaceState,
       "bsIpv6FHSSourceGuardMaxAddr": bsIpv6FHSSourceGuardMaxAddr,
       "bsIpv6FHSSourceGuardOverflowCount": bsIpv6FHSSourceGuardOverflowCount,
       "bsIpv6FHSSourceGuardClearOverflowCount": bsIpv6FHSSourceGuardClearOverflowCount,
       "bsIpv6FHSSourceGuardBindingTable": bsIpv6FHSSourceGuardBindingTable,
       "bsIpv6FHSSourceGuardBindingEntry": bsIpv6FHSSourceGuardBindingEntry,
       "bsIpv6FHSSourceGuardEntryIfIndex": bsIpv6FHSSourceGuardEntryIfIndex,
       "bsIpv6FHSSourceGuardEntryIpv6Addr": bsIpv6FHSSourceGuardEntryIpv6Addr}
)
