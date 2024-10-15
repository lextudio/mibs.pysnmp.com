# SNMP MIB module (HPN-ICF-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-TRAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:02:01 2024
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

(InterfaceIndex,
 ifDescr,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifDescr",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpnicfTrap = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38)
)
hpnicfTrap.setRevisions(
        ("2010-06-05 10:50",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfTableGroup_ObjectIdentity = ObjectIdentity
hpnicfTableGroup = _HpnicfTableGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38, 1)
)
_HpnicfMacTabStatGroup_ObjectIdentity = ObjectIdentity
hpnicfMacTabStatGroup = _HpnicfMacTabStatGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38, 1, 1)
)


class _HpnicfMacTabTrapEnable_Type(Integer32):
    """Custom type hpnicfMacTabTrapEnable based on Integer32"""
    defaultValue = 1

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


_HpnicfMacTabTrapEnable_Type.__name__ = "Integer32"
_HpnicfMacTabTrapEnable_Object = MibScalar
hpnicfMacTabTrapEnable = _HpnicfMacTabTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38, 1, 1, 1),
    _HpnicfMacTabTrapEnable_Type()
)
hpnicfMacTabTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfMacTabTrapEnable.setStatus("current")


class _HpnicfMacTabTrapInterval_Type(Integer32):
    """Custom type hpnicfMacTabTrapInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 3600),
    )


_HpnicfMacTabTrapInterval_Type.__name__ = "Integer32"
_HpnicfMacTabTrapInterval_Object = MibScalar
hpnicfMacTabTrapInterval = _HpnicfMacTabTrapInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38, 1, 1, 2),
    _HpnicfMacTabTrapInterval_Type()
)
hpnicfMacTabTrapInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfMacTabTrapInterval.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfMacTabTrapInterval.setUnits("seconds")
_HpnicfMacTabTrapInfo_ObjectIdentity = ObjectIdentity
hpnicfMacTabTrapInfo = _HpnicfMacTabTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38, 1, 1, 3)
)
_HpnicfMacTabLen_Type = Integer32
_HpnicfMacTabLen_Object = MibScalar
hpnicfMacTabLen = _HpnicfMacTabLen_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38, 1, 1, 3, 1),
    _HpnicfMacTabLen_Type()
)
hpnicfMacTabLen.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfMacTabLen.setStatus("current")
_HpnicfMacTabTrap_ObjectIdentity = ObjectIdentity
hpnicfMacTabTrap = _HpnicfMacTabTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38, 1, 1, 4)
)
_HpnicfArpTabStatGroup_ObjectIdentity = ObjectIdentity
hpnicfArpTabStatGroup = _HpnicfArpTabStatGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38, 1, 2)
)


class _HpnicfArpTabTrapEnable_Type(Integer32):
    """Custom type hpnicfArpTabTrapEnable based on Integer32"""
    defaultValue = 1

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


_HpnicfArpTabTrapEnable_Type.__name__ = "Integer32"
_HpnicfArpTabTrapEnable_Object = MibScalar
hpnicfArpTabTrapEnable = _HpnicfArpTabTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38, 1, 2, 1),
    _HpnicfArpTabTrapEnable_Type()
)
hpnicfArpTabTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfArpTabTrapEnable.setStatus("current")


class _HpnicfArpTabTrapInterval_Type(Integer32):
    """Custom type hpnicfArpTabTrapInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 3600),
    )


_HpnicfArpTabTrapInterval_Type.__name__ = "Integer32"
_HpnicfArpTabTrapInterval_Object = MibScalar
hpnicfArpTabTrapInterval = _HpnicfArpTabTrapInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38, 1, 2, 2),
    _HpnicfArpTabTrapInterval_Type()
)
hpnicfArpTabTrapInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfArpTabTrapInterval.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfArpTabTrapInterval.setUnits("seconds")
_HpnicfArpTabTrapInfo_ObjectIdentity = ObjectIdentity
hpnicfArpTabTrapInfo = _HpnicfArpTabTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38, 1, 2, 3)
)
_HpnicfArpTabLen_Type = Integer32
_HpnicfArpTabLen_Object = MibScalar
hpnicfArpTabLen = _HpnicfArpTabLen_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38, 1, 2, 3, 1),
    _HpnicfArpTabLen_Type()
)
hpnicfArpTabLen.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfArpTabLen.setStatus("current")
_HpnicfArpTabTrap_ObjectIdentity = ObjectIdentity
hpnicfArpTabTrap = _HpnicfArpTabTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38, 1, 2, 4)
)
_HpnicfRtTabStatGroup_ObjectIdentity = ObjectIdentity
hpnicfRtTabStatGroup = _HpnicfRtTabStatGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38, 1, 3)
)
_HpnicfDetailRtTrapTable_Object = MibTable
hpnicfDetailRtTrapTable = _HpnicfDetailRtTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hpnicfDetailRtTrapTable.setStatus("current")
_HpnicfDetailRtTrapEntry_Object = MibTableRow
hpnicfDetailRtTrapEntry = _HpnicfDetailRtTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38, 1, 3, 1, 1)
)
hpnicfDetailRtTrapEntry.setIndexNames(
    (0, "HPN-ICF-TRAP-MIB", "hpnicfDetailRtProType"),
)
if mibBuilder.loadTexts:
    hpnicfDetailRtTrapEntry.setStatus("current")


class _HpnicfDetailRtProType_Type(Integer32):
    """Custom type hpnicfDetailRtProType based on Integer32"""
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
        *(("bgp", 6),
          ("isis", 4),
          ("local", 2),
          ("ospf", 5),
          ("other", 1),
          ("rip", 3))
    )


_HpnicfDetailRtProType_Type.__name__ = "Integer32"
_HpnicfDetailRtProType_Object = MibTableColumn
hpnicfDetailRtProType = _HpnicfDetailRtProType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38, 1, 3, 1, 1, 1),
    _HpnicfDetailRtProType_Type()
)
hpnicfDetailRtProType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDetailRtProType.setStatus("current")


class _HpnicfDetailRtEnable_Type(Integer32):
    """Custom type hpnicfDetailRtEnable based on Integer32"""
    defaultValue = 1

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


_HpnicfDetailRtEnable_Type.__name__ = "Integer32"
_HpnicfDetailRtEnable_Object = MibTableColumn
hpnicfDetailRtEnable = _HpnicfDetailRtEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38, 1, 3, 1, 1, 2),
    _HpnicfDetailRtEnable_Type()
)
hpnicfDetailRtEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDetailRtEnable.setStatus("current")


class _HpnicfRtTabTrapEnable_Type(Integer32):
    """Custom type hpnicfRtTabTrapEnable based on Integer32"""
    defaultValue = 1

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


_HpnicfRtTabTrapEnable_Type.__name__ = "Integer32"
_HpnicfRtTabTrapEnable_Object = MibScalar
hpnicfRtTabTrapEnable = _HpnicfRtTabTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38, 1, 3, 2),
    _HpnicfRtTabTrapEnable_Type()
)
hpnicfRtTabTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfRtTabTrapEnable.setStatus("current")


class _HpnicfRtTabTrapInterval_Type(Integer32):
    """Custom type hpnicfRtTabTrapInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 3600),
    )


_HpnicfRtTabTrapInterval_Type.__name__ = "Integer32"
_HpnicfRtTabTrapInterval_Object = MibScalar
hpnicfRtTabTrapInterval = _HpnicfRtTabTrapInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38, 1, 3, 3),
    _HpnicfRtTabTrapInterval_Type()
)
hpnicfRtTabTrapInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfRtTabTrapInterval.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfRtTabTrapInterval.setUnits("seconds")
_HpnicfRtTabTrapInfo_ObjectIdentity = ObjectIdentity
hpnicfRtTabTrapInfo = _HpnicfRtTabTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38, 1, 3, 4)
)
_HpnicfRtTabLen_Type = Integer32
_HpnicfRtTabLen_Object = MibScalar
hpnicfRtTabLen = _HpnicfRtTabLen_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38, 1, 3, 4, 1),
    _HpnicfRtTabLen_Type()
)
hpnicfRtTabLen.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfRtTabLen.setStatus("current")
_HpnicfDefaultRtNextHopType_Type = InetAddressType
_HpnicfDefaultRtNextHopType_Object = MibScalar
hpnicfDefaultRtNextHopType = _HpnicfDefaultRtNextHopType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38, 1, 3, 4, 2),
    _HpnicfDefaultRtNextHopType_Type()
)
hpnicfDefaultRtNextHopType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDefaultRtNextHopType.setStatus("current")
_HpnicfDefaultRtNextHop_Type = InetAddress
_HpnicfDefaultRtNextHop_Object = MibScalar
hpnicfDefaultRtNextHop = _HpnicfDefaultRtNextHop_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38, 1, 3, 4, 3),
    _HpnicfDefaultRtNextHop_Type()
)
hpnicfDefaultRtNextHop.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDefaultRtNextHop.setStatus("current")
_HpnicfDefaultRtOutIf_Type = InterfaceIndex
_HpnicfDefaultRtOutIf_Object = MibScalar
hpnicfDefaultRtOutIf = _HpnicfDefaultRtOutIf_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38, 1, 3, 4, 4),
    _HpnicfDefaultRtOutIf_Type()
)
hpnicfDefaultRtOutIf.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfDefaultRtOutIf.setStatus("current")
_HpnicfRtTabTrap_ObjectIdentity = ObjectIdentity
hpnicfRtTabTrap = _HpnicfRtTabTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38, 1, 3, 5)
)


class _HpnicfDefaultRtDelTrapEnable_Type(TruthValue):
    """Custom type hpnicfDefaultRtDelTrapEnable based on TruthValue"""


_HpnicfDefaultRtDelTrapEnable_Object = MibScalar
hpnicfDefaultRtDelTrapEnable = _HpnicfDefaultRtDelTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38, 1, 3, 6),
    _HpnicfDefaultRtDelTrapEnable_Type()
)
hpnicfDefaultRtDelTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDefaultRtDelTrapEnable.setStatus("current")
_HpnicfMulticastTabStatGroup_ObjectIdentity = ObjectIdentity
hpnicfMulticastTabStatGroup = _HpnicfMulticastTabStatGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38, 1, 4)
)


class _HpnicfMulticastTabTrapEnable_Type(Integer32):
    """Custom type hpnicfMulticastTabTrapEnable based on Integer32"""
    defaultValue = 1

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


_HpnicfMulticastTabTrapEnable_Type.__name__ = "Integer32"
_HpnicfMulticastTabTrapEnable_Object = MibScalar
hpnicfMulticastTabTrapEnable = _HpnicfMulticastTabTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38, 1, 4, 1),
    _HpnicfMulticastTabTrapEnable_Type()
)
hpnicfMulticastTabTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfMulticastTabTrapEnable.setStatus("current")


class _HpnicfMulticastTabTrapInterval_Type(Integer32):
    """Custom type hpnicfMulticastTabTrapInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 3600),
    )


_HpnicfMulticastTabTrapInterval_Type.__name__ = "Integer32"
_HpnicfMulticastTabTrapInterval_Object = MibScalar
hpnicfMulticastTabTrapInterval = _HpnicfMulticastTabTrapInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38, 1, 4, 2),
    _HpnicfMulticastTabTrapInterval_Type()
)
hpnicfMulticastTabTrapInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfMulticastTabTrapInterval.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfMulticastTabTrapInterval.setUnits("seconds")
_HpnicfMulticastTabTrapInfo_ObjectIdentity = ObjectIdentity
hpnicfMulticastTabTrapInfo = _HpnicfMulticastTabTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38, 1, 4, 3)
)


class _HpnicfMulticastTabType_Type(Integer32):
    """Custom type hpnicfMulticastTabType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lay2", 1),
          ("lay3", 2))
    )


_HpnicfMulticastTabType_Type.__name__ = "Integer32"
_HpnicfMulticastTabType_Object = MibScalar
hpnicfMulticastTabType = _HpnicfMulticastTabType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38, 1, 4, 3, 1),
    _HpnicfMulticastTabType_Type()
)
hpnicfMulticastTabType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfMulticastTabType.setStatus("current")
_HpnicfMulticastTabLen_Type = Integer32
_HpnicfMulticastTabLen_Object = MibScalar
hpnicfMulticastTabLen = _HpnicfMulticastTabLen_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38, 1, 4, 3, 2),
    _HpnicfMulticastTabLen_Type()
)
hpnicfMulticastTabLen.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfMulticastTabLen.setStatus("current")
_HpnicfMulticastTabTrap_ObjectIdentity = ObjectIdentity
hpnicfMulticastTabTrap = _HpnicfMulticastTabTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38, 1, 4, 4)
)
_HpnicfNdTabStatGroup_ObjectIdentity = ObjectIdentity
hpnicfNdTabStatGroup = _HpnicfNdTabStatGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38, 1, 5)
)


class _HpnicfNdTabTrapEnable_Type(Integer32):
    """Custom type hpnicfNdTabTrapEnable based on Integer32"""
    defaultValue = 1

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


_HpnicfNdTabTrapEnable_Type.__name__ = "Integer32"
_HpnicfNdTabTrapEnable_Object = MibScalar
hpnicfNdTabTrapEnable = _HpnicfNdTabTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38, 1, 5, 1),
    _HpnicfNdTabTrapEnable_Type()
)
hpnicfNdTabTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfNdTabTrapEnable.setStatus("current")


class _HpnicfNdTabTrapInterval_Type(Integer32):
    """Custom type hpnicfNdTabTrapInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 3600),
    )


_HpnicfNdTabTrapInterval_Type.__name__ = "Integer32"
_HpnicfNdTabTrapInterval_Object = MibScalar
hpnicfNdTabTrapInterval = _HpnicfNdTabTrapInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38, 1, 5, 2),
    _HpnicfNdTabTrapInterval_Type()
)
hpnicfNdTabTrapInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfNdTabTrapInterval.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfNdTabTrapInterval.setUnits("seconds")
_HpnicfNdTabTrapInfo_ObjectIdentity = ObjectIdentity
hpnicfNdTabTrapInfo = _HpnicfNdTabTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38, 1, 5, 3)
)
_HpnicfNdTabLen_Type = Integer32
_HpnicfNdTabLen_Object = MibScalar
hpnicfNdTabLen = _HpnicfNdTabLen_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38, 1, 5, 3, 1),
    _HpnicfNdTabLen_Type()
)
hpnicfNdTabLen.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfNdTabLen.setStatus("current")
_HpnicfNdTabTrap_ObjectIdentity = ObjectIdentity
hpnicfNdTabTrap = _HpnicfNdTabTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38, 1, 5, 4)
)
_HpnicfPeriodicalTrapGroup_ObjectIdentity = ObjectIdentity
hpnicfPeriodicalTrapGroup = _HpnicfPeriodicalTrapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38, 1, 6)
)
_HpnicfPeriodicalTrapObjects_ObjectIdentity = ObjectIdentity
hpnicfPeriodicalTrapObjects = _HpnicfPeriodicalTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38, 1, 6, 1)
)


class _HpnicfPeriodicalTrapInterval_Type(Integer32):
    """Custom type hpnicfPeriodicalTrapInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 3600),
    )


_HpnicfPeriodicalTrapInterval_Type.__name__ = "Integer32"
_HpnicfPeriodicalTrapInterval_Object = MibScalar
hpnicfPeriodicalTrapInterval = _HpnicfPeriodicalTrapInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38, 1, 6, 1, 1),
    _HpnicfPeriodicalTrapInterval_Type()
)
hpnicfPeriodicalTrapInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPeriodicalTrapInterval.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfPeriodicalTrapInterval.setUnits("seconds")


class _HpnicfPeriodicalTrapSwitch_Type(Integer32):
    """Custom type hpnicfPeriodicalTrapSwitch based on Integer32"""
    defaultValue = 1

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


_HpnicfPeriodicalTrapSwitch_Type.__name__ = "Integer32"
_HpnicfPeriodicalTrapSwitch_Object = MibScalar
hpnicfPeriodicalTrapSwitch = _HpnicfPeriodicalTrapSwitch_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38, 1, 6, 1, 2),
    _HpnicfPeriodicalTrapSwitch_Type()
)
hpnicfPeriodicalTrapSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPeriodicalTrapSwitch.setStatus("current")


class _HpnicfPeriodicalTrapSwitch2_Type(Integer32):
    """Custom type hpnicfPeriodicalTrapSwitch2 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_HpnicfPeriodicalTrapSwitch2_Type.__name__ = "Integer32"
_HpnicfPeriodicalTrapSwitch2_Object = MibScalar
hpnicfPeriodicalTrapSwitch2 = _HpnicfPeriodicalTrapSwitch2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38, 1, 6, 1, 3),
    _HpnicfPeriodicalTrapSwitch2_Type()
)
hpnicfPeriodicalTrapSwitch2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPeriodicalTrapSwitch2.setStatus("current")
_HpnicfPeriodicalTrapInfo_ObjectIdentity = ObjectIdentity
hpnicfPeriodicalTrapInfo = _HpnicfPeriodicalTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38, 1, 6, 2)
)
_HpnicfPeriodicalNotification_ObjectIdentity = ObjectIdentity
hpnicfPeriodicalNotification = _HpnicfPeriodicalNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38, 1, 6, 3)
)
_HpnicfPeriodicalNotificationPrefix_ObjectIdentity = ObjectIdentity
hpnicfPeriodicalNotificationPrefix = _HpnicfPeriodicalNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38, 1, 6, 3, 0)
)
_HpnicfTrapDesInfo_ObjectIdentity = ObjectIdentity
hpnicfTrapDesInfo = _HpnicfTrapDesInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38, 1, 7)
)
_HpnicfTrapDesInfoTable_Object = MibTable
hpnicfTrapDesInfoTable = _HpnicfTrapDesInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38, 1, 7, 1)
)
if mibBuilder.loadTexts:
    hpnicfTrapDesInfoTable.setStatus("current")
_HpnicfTrapDesInfoEntry_Object = MibTableRow
hpnicfTrapDesInfoEntry = _HpnicfTrapDesInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38, 1, 7, 1, 1)
)
hpnicfTrapDesInfoEntry.setIndexNames(
    (0, "HPN-ICF-TRAP-MIB", "hpnicfTrapDesInfoIndex"),
)
if mibBuilder.loadTexts:
    hpnicfTrapDesInfoEntry.setStatus("current")


class _HpnicfTrapDesInfoIndex_Type(Integer32):
    """Custom type hpnicfTrapDesInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_HpnicfTrapDesInfoIndex_Type.__name__ = "Integer32"
_HpnicfTrapDesInfoIndex_Object = MibTableColumn
hpnicfTrapDesInfoIndex = _HpnicfTrapDesInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38, 1, 7, 1, 1, 1),
    _HpnicfTrapDesInfoIndex_Type()
)
hpnicfTrapDesInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfTrapDesInfoIndex.setStatus("current")
_HpnicfTrapDesIPAddress_Type = IpAddress
_HpnicfTrapDesIPAddress_Object = MibTableColumn
hpnicfTrapDesIPAddress = _HpnicfTrapDesIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38, 1, 7, 1, 1, 2),
    _HpnicfTrapDesIPAddress_Type()
)
hpnicfTrapDesIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfTrapDesIPAddress.setStatus("current")


class _HpnicfTrapDesPort_Type(Integer32):
    """Custom type hpnicfTrapDesPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfTrapDesPort_Type.__name__ = "Integer32"
_HpnicfTrapDesPort_Object = MibTableColumn
hpnicfTrapDesPort = _HpnicfTrapDesPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38, 1, 7, 1, 1, 3),
    _HpnicfTrapDesPort_Type()
)
hpnicfTrapDesPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfTrapDesPort.setStatus("current")
_HpnicfTrapDesRowStatus_Type = RowStatus
_HpnicfTrapDesRowStatus_Object = MibTableColumn
hpnicfTrapDesRowStatus = _HpnicfTrapDesRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38, 1, 7, 1, 1, 4),
    _HpnicfTrapDesRowStatus_Type()
)
hpnicfTrapDesRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfTrapDesRowStatus.setStatus("current")
_HpnicfTrapDesAddrTAddress_Type = TAddress
_HpnicfTrapDesAddrTAddress_Object = MibTableColumn
hpnicfTrapDesAddrTAddress = _HpnicfTrapDesAddrTAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38, 1, 7, 1, 1, 5),
    _HpnicfTrapDesAddrTAddress_Type()
)
hpnicfTrapDesAddrTAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfTrapDesAddrTAddress.setStatus("current")
_HpnicfTrapConfig_ObjectIdentity = ObjectIdentity
hpnicfTrapConfig = _HpnicfTrapConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38, 1, 8)
)
_HpnicfTrapConfigTable_Object = MibTable
hpnicfTrapConfigTable = _HpnicfTrapConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38, 1, 8, 1)
)
if mibBuilder.loadTexts:
    hpnicfTrapConfigTable.setStatus("current")
_HpnicfTrapConfigEntry_Object = MibTableRow
hpnicfTrapConfigEntry = _HpnicfTrapConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38, 1, 8, 1, 1)
)
hpnicfTrapConfigEntry.setIndexNames(
    (0, "HPN-ICF-TRAP-MIB", "hpnicfTrapConfigIndex"),
)
if mibBuilder.loadTexts:
    hpnicfTrapConfigEntry.setStatus("current")


class _HpnicfTrapConfigIndex_Type(Integer32):
    """Custom type hpnicfTrapConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfTrapConfigIndex_Type.__name__ = "Integer32"
_HpnicfTrapConfigIndex_Object = MibTableColumn
hpnicfTrapConfigIndex = _HpnicfTrapConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38, 1, 8, 1, 1, 1),
    _HpnicfTrapConfigIndex_Type()
)
hpnicfTrapConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfTrapConfigIndex.setStatus("current")


class _HpnicfTrapConfigName_Type(SnmpAdminString):
    """Custom type hpnicfTrapConfigName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_HpnicfTrapConfigName_Type.__name__ = "SnmpAdminString"
_HpnicfTrapConfigName_Object = MibTableColumn
hpnicfTrapConfigName = _HpnicfTrapConfigName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38, 1, 8, 1, 1, 2),
    _HpnicfTrapConfigName_Type()
)
hpnicfTrapConfigName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfTrapConfigName.setStatus("current")


class _HpnicfTrapConfigDescr_Type(SnmpAdminString):
    """Custom type hpnicfTrapConfigDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_HpnicfTrapConfigDescr_Type.__name__ = "SnmpAdminString"
_HpnicfTrapConfigDescr_Object = MibTableColumn
hpnicfTrapConfigDescr = _HpnicfTrapConfigDescr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38, 1, 8, 1, 1, 3),
    _HpnicfTrapConfigDescr_Type()
)
hpnicfTrapConfigDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfTrapConfigDescr.setStatus("current")


class _HpnicfTrapConfigSwitch_Type(Integer32):
    """Custom type hpnicfTrapConfigSwitch based on Integer32"""
    defaultValue = 1

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


_HpnicfTrapConfigSwitch_Type.__name__ = "Integer32"
_HpnicfTrapConfigSwitch_Object = MibTableColumn
hpnicfTrapConfigSwitch = _HpnicfTrapConfigSwitch_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38, 1, 8, 1, 1, 4),
    _HpnicfTrapConfigSwitch_Type()
)
hpnicfTrapConfigSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfTrapConfigSwitch.setStatus("current")


class _HpnicfTrapConfigSwitch2_Type(Integer32):
    """Custom type hpnicfTrapConfigSwitch2 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_HpnicfTrapConfigSwitch2_Type.__name__ = "Integer32"
_HpnicfTrapConfigSwitch2_Object = MibTableColumn
hpnicfTrapConfigSwitch2 = _HpnicfTrapConfigSwitch2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38, 1, 8, 1, 1, 5),
    _HpnicfTrapConfigSwitch2_Type()
)
hpnicfTrapConfigSwitch2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfTrapConfigSwitch2.setStatus("current")

# Managed Objects groups


# Notification objects

hpnicfMacTabFullTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38, 1, 1, 4, 1)
)
hpnicfMacTabFullTrap.setObjects(
    ("HPN-ICF-TRAP-MIB", "hpnicfMacTabLen")
)
if mibBuilder.loadTexts:
    hpnicfMacTabFullTrap.setStatus(
        "current"
    )

hpnicfMacTabAlmostFullTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    hpnicfMacTabAlmostFullTrap.setStatus(
        "current"
    )

hpnicfArpTabFullTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38, 1, 2, 4, 1)
)
hpnicfArpTabFullTrap.setObjects(
    ("HPN-ICF-TRAP-MIB", "hpnicfArpTabLen")
)
if mibBuilder.loadTexts:
    hpnicfArpTabFullTrap.setStatus(
        "current"
    )

hpnicfArpPortDynamicEntryFullTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38, 1, 2, 4, 2)
)
hpnicfArpPortDynamicEntryFullTrap.setObjects(
      *(("HPN-ICF-TRAP-MIB", "hpnicfArpTabLen"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hpnicfArpPortDynamicEntryFullTrap.setStatus(
        "current"
    )

hpnicfRtTabFullTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38, 1, 3, 5, 1)
)
hpnicfRtTabFullTrap.setObjects(
    ("HPN-ICF-TRAP-MIB", "hpnicfRtTabLen")
)
if mibBuilder.loadTexts:
    hpnicfRtTabFullTrap.setStatus(
        "current"
    )

hpnicfDetailRtTabFullTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38, 1, 3, 5, 2)
)
hpnicfDetailRtTabFullTrap.setObjects(
      *(("HPN-ICF-TRAP-MIB", "hpnicfDetailRtProType"),
        ("HPN-ICF-TRAP-MIB", "hpnicfRtTabLen"))
)
if mibBuilder.loadTexts:
    hpnicfDetailRtTabFullTrap.setStatus(
        "current"
    )

hpnicfDefaultRtDelTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38, 1, 3, 5, 3)
)
hpnicfDefaultRtDelTrap.setObjects(
      *(("HPN-ICF-TRAP-MIB", "hpnicfDetailRtProType"),
        ("HPN-ICF-TRAP-MIB", "hpnicfDefaultRtNextHopType"),
        ("HPN-ICF-TRAP-MIB", "hpnicfDefaultRtNextHop"),
        ("HPN-ICF-TRAP-MIB", "hpnicfDefaultRtOutIf"))
)
if mibBuilder.loadTexts:
    hpnicfDefaultRtDelTrap.setStatus(
        "current"
    )

hpnicfMulticastTabFullTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38, 1, 4, 4, 1)
)
hpnicfMulticastTabFullTrap.setObjects(
      *(("HPN-ICF-TRAP-MIB", "hpnicfMulticastTabType"),
        ("HPN-ICF-TRAP-MIB", "hpnicfMulticastTabLen"))
)
if mibBuilder.loadTexts:
    hpnicfMulticastTabFullTrap.setStatus(
        "current"
    )

hpnicfNdTabFullTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38, 1, 5, 4, 1)
)
hpnicfNdTabFullTrap.setObjects(
    ("HPN-ICF-TRAP-MIB", "hpnicfNdTabLen")
)
if mibBuilder.loadTexts:
    hpnicfNdTabFullTrap.setStatus(
        "current"
    )

hpnicfPeriodicalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 38, 1, 6, 3, 0, 1)
)
if mibBuilder.loadTexts:
    hpnicfPeriodicalTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-TRAP-MIB",
    **{"hpnicfTrap": hpnicfTrap,
       "hpnicfTableGroup": hpnicfTableGroup,
       "hpnicfMacTabStatGroup": hpnicfMacTabStatGroup,
       "hpnicfMacTabTrapEnable": hpnicfMacTabTrapEnable,
       "hpnicfMacTabTrapInterval": hpnicfMacTabTrapInterval,
       "hpnicfMacTabTrapInfo": hpnicfMacTabTrapInfo,
       "hpnicfMacTabLen": hpnicfMacTabLen,
       "hpnicfMacTabTrap": hpnicfMacTabTrap,
       "hpnicfMacTabFullTrap": hpnicfMacTabFullTrap,
       "hpnicfMacTabAlmostFullTrap": hpnicfMacTabAlmostFullTrap,
       "hpnicfArpTabStatGroup": hpnicfArpTabStatGroup,
       "hpnicfArpTabTrapEnable": hpnicfArpTabTrapEnable,
       "hpnicfArpTabTrapInterval": hpnicfArpTabTrapInterval,
       "hpnicfArpTabTrapInfo": hpnicfArpTabTrapInfo,
       "hpnicfArpTabLen": hpnicfArpTabLen,
       "hpnicfArpTabTrap": hpnicfArpTabTrap,
       "hpnicfArpTabFullTrap": hpnicfArpTabFullTrap,
       "hpnicfArpPortDynamicEntryFullTrap": hpnicfArpPortDynamicEntryFullTrap,
       "hpnicfRtTabStatGroup": hpnicfRtTabStatGroup,
       "hpnicfDetailRtTrapTable": hpnicfDetailRtTrapTable,
       "hpnicfDetailRtTrapEntry": hpnicfDetailRtTrapEntry,
       "hpnicfDetailRtProType": hpnicfDetailRtProType,
       "hpnicfDetailRtEnable": hpnicfDetailRtEnable,
       "hpnicfRtTabTrapEnable": hpnicfRtTabTrapEnable,
       "hpnicfRtTabTrapInterval": hpnicfRtTabTrapInterval,
       "hpnicfRtTabTrapInfo": hpnicfRtTabTrapInfo,
       "hpnicfRtTabLen": hpnicfRtTabLen,
       "hpnicfDefaultRtNextHopType": hpnicfDefaultRtNextHopType,
       "hpnicfDefaultRtNextHop": hpnicfDefaultRtNextHop,
       "hpnicfDefaultRtOutIf": hpnicfDefaultRtOutIf,
       "hpnicfRtTabTrap": hpnicfRtTabTrap,
       "hpnicfRtTabFullTrap": hpnicfRtTabFullTrap,
       "hpnicfDetailRtTabFullTrap": hpnicfDetailRtTabFullTrap,
       "hpnicfDefaultRtDelTrap": hpnicfDefaultRtDelTrap,
       "hpnicfDefaultRtDelTrapEnable": hpnicfDefaultRtDelTrapEnable,
       "hpnicfMulticastTabStatGroup": hpnicfMulticastTabStatGroup,
       "hpnicfMulticastTabTrapEnable": hpnicfMulticastTabTrapEnable,
       "hpnicfMulticastTabTrapInterval": hpnicfMulticastTabTrapInterval,
       "hpnicfMulticastTabTrapInfo": hpnicfMulticastTabTrapInfo,
       "hpnicfMulticastTabType": hpnicfMulticastTabType,
       "hpnicfMulticastTabLen": hpnicfMulticastTabLen,
       "hpnicfMulticastTabTrap": hpnicfMulticastTabTrap,
       "hpnicfMulticastTabFullTrap": hpnicfMulticastTabFullTrap,
       "hpnicfNdTabStatGroup": hpnicfNdTabStatGroup,
       "hpnicfNdTabTrapEnable": hpnicfNdTabTrapEnable,
       "hpnicfNdTabTrapInterval": hpnicfNdTabTrapInterval,
       "hpnicfNdTabTrapInfo": hpnicfNdTabTrapInfo,
       "hpnicfNdTabLen": hpnicfNdTabLen,
       "hpnicfNdTabTrap": hpnicfNdTabTrap,
       "hpnicfNdTabFullTrap": hpnicfNdTabFullTrap,
       "hpnicfPeriodicalTrapGroup": hpnicfPeriodicalTrapGroup,
       "hpnicfPeriodicalTrapObjects": hpnicfPeriodicalTrapObjects,
       "hpnicfPeriodicalTrapInterval": hpnicfPeriodicalTrapInterval,
       "hpnicfPeriodicalTrapSwitch": hpnicfPeriodicalTrapSwitch,
       "hpnicfPeriodicalTrapSwitch2": hpnicfPeriodicalTrapSwitch2,
       "hpnicfPeriodicalTrapInfo": hpnicfPeriodicalTrapInfo,
       "hpnicfPeriodicalNotification": hpnicfPeriodicalNotification,
       "hpnicfPeriodicalNotificationPrefix": hpnicfPeriodicalNotificationPrefix,
       "hpnicfPeriodicalTrap": hpnicfPeriodicalTrap,
       "hpnicfTrapDesInfo": hpnicfTrapDesInfo,
       "hpnicfTrapDesInfoTable": hpnicfTrapDesInfoTable,
       "hpnicfTrapDesInfoEntry": hpnicfTrapDesInfoEntry,
       "hpnicfTrapDesInfoIndex": hpnicfTrapDesInfoIndex,
       "hpnicfTrapDesIPAddress": hpnicfTrapDesIPAddress,
       "hpnicfTrapDesPort": hpnicfTrapDesPort,
       "hpnicfTrapDesRowStatus": hpnicfTrapDesRowStatus,
       "hpnicfTrapDesAddrTAddress": hpnicfTrapDesAddrTAddress,
       "hpnicfTrapConfig": hpnicfTrapConfig,
       "hpnicfTrapConfigTable": hpnicfTrapConfigTable,
       "hpnicfTrapConfigEntry": hpnicfTrapConfigEntry,
       "hpnicfTrapConfigIndex": hpnicfTrapConfigIndex,
       "hpnicfTrapConfigName": hpnicfTrapConfigName,
       "hpnicfTrapConfigDescr": hpnicfTrapConfigDescr,
       "hpnicfTrapConfigSwitch": hpnicfTrapConfigSwitch,
       "hpnicfTrapConfigSwitch2": hpnicfTrapConfigSwitch2}
)
