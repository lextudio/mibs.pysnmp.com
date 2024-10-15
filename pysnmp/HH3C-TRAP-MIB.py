# SNMP MIB module (HH3C-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-TRAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:55:07 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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

hh3cTrap = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 38)
)
hh3cTrap.setRevisions(
        ("2010-06-05 10:50",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cTableGroup_ObjectIdentity = ObjectIdentity
hh3cTableGroup = _Hh3cTableGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 38, 1)
)
_Hh3cMacTabStatGroup_ObjectIdentity = ObjectIdentity
hh3cMacTabStatGroup = _Hh3cMacTabStatGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 38, 1, 1)
)


class _Hh3cMacTabTrapEnable_Type(Integer32):
    """Custom type hh3cMacTabTrapEnable based on Integer32"""
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


_Hh3cMacTabTrapEnable_Type.__name__ = "Integer32"
_Hh3cMacTabTrapEnable_Object = MibScalar
hh3cMacTabTrapEnable = _Hh3cMacTabTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 38, 1, 1, 1),
    _Hh3cMacTabTrapEnable_Type()
)
hh3cMacTabTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cMacTabTrapEnable.setStatus("current")


class _Hh3cMacTabTrapInterval_Type(Integer32):
    """Custom type hh3cMacTabTrapInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 3600),
    )


_Hh3cMacTabTrapInterval_Type.__name__ = "Integer32"
_Hh3cMacTabTrapInterval_Object = MibScalar
hh3cMacTabTrapInterval = _Hh3cMacTabTrapInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 38, 1, 1, 2),
    _Hh3cMacTabTrapInterval_Type()
)
hh3cMacTabTrapInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cMacTabTrapInterval.setStatus("current")
if mibBuilder.loadTexts:
    hh3cMacTabTrapInterval.setUnits("seconds")
_Hh3cMacTabTrapInfo_ObjectIdentity = ObjectIdentity
hh3cMacTabTrapInfo = _Hh3cMacTabTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 38, 1, 1, 3)
)
_Hh3cMacTabLen_Type = Integer32
_Hh3cMacTabLen_Object = MibScalar
hh3cMacTabLen = _Hh3cMacTabLen_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 38, 1, 1, 3, 1),
    _Hh3cMacTabLen_Type()
)
hh3cMacTabLen.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cMacTabLen.setStatus("current")
_Hh3cMacTabTrap_ObjectIdentity = ObjectIdentity
hh3cMacTabTrap = _Hh3cMacTabTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 38, 1, 1, 4)
)
_Hh3cArpTabStatGroup_ObjectIdentity = ObjectIdentity
hh3cArpTabStatGroup = _Hh3cArpTabStatGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 38, 1, 2)
)


class _Hh3cArpTabTrapEnable_Type(Integer32):
    """Custom type hh3cArpTabTrapEnable based on Integer32"""
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


_Hh3cArpTabTrapEnable_Type.__name__ = "Integer32"
_Hh3cArpTabTrapEnable_Object = MibScalar
hh3cArpTabTrapEnable = _Hh3cArpTabTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 38, 1, 2, 1),
    _Hh3cArpTabTrapEnable_Type()
)
hh3cArpTabTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cArpTabTrapEnable.setStatus("current")


class _Hh3cArpTabTrapInterval_Type(Integer32):
    """Custom type hh3cArpTabTrapInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 3600),
    )


_Hh3cArpTabTrapInterval_Type.__name__ = "Integer32"
_Hh3cArpTabTrapInterval_Object = MibScalar
hh3cArpTabTrapInterval = _Hh3cArpTabTrapInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 38, 1, 2, 2),
    _Hh3cArpTabTrapInterval_Type()
)
hh3cArpTabTrapInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cArpTabTrapInterval.setStatus("current")
if mibBuilder.loadTexts:
    hh3cArpTabTrapInterval.setUnits("seconds")
_Hh3cArpTabTrapInfo_ObjectIdentity = ObjectIdentity
hh3cArpTabTrapInfo = _Hh3cArpTabTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 38, 1, 2, 3)
)
_Hh3cArpTabLen_Type = Integer32
_Hh3cArpTabLen_Object = MibScalar
hh3cArpTabLen = _Hh3cArpTabLen_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 38, 1, 2, 3, 1),
    _Hh3cArpTabLen_Type()
)
hh3cArpTabLen.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cArpTabLen.setStatus("current")
_Hh3cArpTabTrap_ObjectIdentity = ObjectIdentity
hh3cArpTabTrap = _Hh3cArpTabTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 38, 1, 2, 4)
)
_Hh3cRtTabStatGroup_ObjectIdentity = ObjectIdentity
hh3cRtTabStatGroup = _Hh3cRtTabStatGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 38, 1, 3)
)
_Hh3cDetailRtTrapTable_Object = MibTable
hh3cDetailRtTrapTable = _Hh3cDetailRtTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 38, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hh3cDetailRtTrapTable.setStatus("current")
_Hh3cDetailRtTrapEntry_Object = MibTableRow
hh3cDetailRtTrapEntry = _Hh3cDetailRtTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 38, 1, 3, 1, 1)
)
hh3cDetailRtTrapEntry.setIndexNames(
    (0, "HH3C-TRAP-MIB", "hh3cDetailRtProType"),
)
if mibBuilder.loadTexts:
    hh3cDetailRtTrapEntry.setStatus("current")


class _Hh3cDetailRtProType_Type(Integer32):
    """Custom type hh3cDetailRtProType based on Integer32"""
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


_Hh3cDetailRtProType_Type.__name__ = "Integer32"
_Hh3cDetailRtProType_Object = MibTableColumn
hh3cDetailRtProType = _Hh3cDetailRtProType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 38, 1, 3, 1, 1, 1),
    _Hh3cDetailRtProType_Type()
)
hh3cDetailRtProType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDetailRtProType.setStatus("current")


class _Hh3cDetailRtEnable_Type(Integer32):
    """Custom type hh3cDetailRtEnable based on Integer32"""
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


_Hh3cDetailRtEnable_Type.__name__ = "Integer32"
_Hh3cDetailRtEnable_Object = MibTableColumn
hh3cDetailRtEnable = _Hh3cDetailRtEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 38, 1, 3, 1, 1, 2),
    _Hh3cDetailRtEnable_Type()
)
hh3cDetailRtEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDetailRtEnable.setStatus("current")


class _Hh3cRtTabTrapEnable_Type(Integer32):
    """Custom type hh3cRtTabTrapEnable based on Integer32"""
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


_Hh3cRtTabTrapEnable_Type.__name__ = "Integer32"
_Hh3cRtTabTrapEnable_Object = MibScalar
hh3cRtTabTrapEnable = _Hh3cRtTabTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 38, 1, 3, 2),
    _Hh3cRtTabTrapEnable_Type()
)
hh3cRtTabTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cRtTabTrapEnable.setStatus("current")


class _Hh3cRtTabTrapInterval_Type(Integer32):
    """Custom type hh3cRtTabTrapInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 3600),
    )


_Hh3cRtTabTrapInterval_Type.__name__ = "Integer32"
_Hh3cRtTabTrapInterval_Object = MibScalar
hh3cRtTabTrapInterval = _Hh3cRtTabTrapInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 38, 1, 3, 3),
    _Hh3cRtTabTrapInterval_Type()
)
hh3cRtTabTrapInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cRtTabTrapInterval.setStatus("current")
if mibBuilder.loadTexts:
    hh3cRtTabTrapInterval.setUnits("seconds")
_Hh3cRtTabTrapInfo_ObjectIdentity = ObjectIdentity
hh3cRtTabTrapInfo = _Hh3cRtTabTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 38, 1, 3, 4)
)
_Hh3cRtTabLen_Type = Integer32
_Hh3cRtTabLen_Object = MibScalar
hh3cRtTabLen = _Hh3cRtTabLen_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 38, 1, 3, 4, 1),
    _Hh3cRtTabLen_Type()
)
hh3cRtTabLen.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cRtTabLen.setStatus("current")
_Hh3cDefaultRtNextHopType_Type = InetAddressType
_Hh3cDefaultRtNextHopType_Object = MibScalar
hh3cDefaultRtNextHopType = _Hh3cDefaultRtNextHopType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 38, 1, 3, 4, 2),
    _Hh3cDefaultRtNextHopType_Type()
)
hh3cDefaultRtNextHopType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDefaultRtNextHopType.setStatus("current")
_Hh3cDefaultRtNextHop_Type = InetAddress
_Hh3cDefaultRtNextHop_Object = MibScalar
hh3cDefaultRtNextHop = _Hh3cDefaultRtNextHop_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 38, 1, 3, 4, 3),
    _Hh3cDefaultRtNextHop_Type()
)
hh3cDefaultRtNextHop.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDefaultRtNextHop.setStatus("current")
_Hh3cDefaultRtOutIf_Type = InterfaceIndex
_Hh3cDefaultRtOutIf_Object = MibScalar
hh3cDefaultRtOutIf = _Hh3cDefaultRtOutIf_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 38, 1, 3, 4, 4),
    _Hh3cDefaultRtOutIf_Type()
)
hh3cDefaultRtOutIf.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cDefaultRtOutIf.setStatus("current")
_Hh3cRtTabTrap_ObjectIdentity = ObjectIdentity
hh3cRtTabTrap = _Hh3cRtTabTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 38, 1, 3, 5)
)


class _Hh3cDefaultRtDelTrapEnable_Type(TruthValue):
    """Custom type hh3cDefaultRtDelTrapEnable based on TruthValue"""


_Hh3cDefaultRtDelTrapEnable_Object = MibScalar
hh3cDefaultRtDelTrapEnable = _Hh3cDefaultRtDelTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 38, 1, 3, 6),
    _Hh3cDefaultRtDelTrapEnable_Type()
)
hh3cDefaultRtDelTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDefaultRtDelTrapEnable.setStatus("current")
_Hh3cMulticastTabStatGroup_ObjectIdentity = ObjectIdentity
hh3cMulticastTabStatGroup = _Hh3cMulticastTabStatGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 38, 1, 4)
)


class _Hh3cMulticastTabTrapEnable_Type(Integer32):
    """Custom type hh3cMulticastTabTrapEnable based on Integer32"""
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


_Hh3cMulticastTabTrapEnable_Type.__name__ = "Integer32"
_Hh3cMulticastTabTrapEnable_Object = MibScalar
hh3cMulticastTabTrapEnable = _Hh3cMulticastTabTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 38, 1, 4, 1),
    _Hh3cMulticastTabTrapEnable_Type()
)
hh3cMulticastTabTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cMulticastTabTrapEnable.setStatus("current")


class _Hh3cMulticastTabTrapInterval_Type(Integer32):
    """Custom type hh3cMulticastTabTrapInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 3600),
    )


_Hh3cMulticastTabTrapInterval_Type.__name__ = "Integer32"
_Hh3cMulticastTabTrapInterval_Object = MibScalar
hh3cMulticastTabTrapInterval = _Hh3cMulticastTabTrapInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 38, 1, 4, 2),
    _Hh3cMulticastTabTrapInterval_Type()
)
hh3cMulticastTabTrapInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cMulticastTabTrapInterval.setStatus("current")
if mibBuilder.loadTexts:
    hh3cMulticastTabTrapInterval.setUnits("seconds")
_Hh3cMulticastTabTrapInfo_ObjectIdentity = ObjectIdentity
hh3cMulticastTabTrapInfo = _Hh3cMulticastTabTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 38, 1, 4, 3)
)


class _Hh3cMulticastTabType_Type(Integer32):
    """Custom type hh3cMulticastTabType based on Integer32"""
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


_Hh3cMulticastTabType_Type.__name__ = "Integer32"
_Hh3cMulticastTabType_Object = MibScalar
hh3cMulticastTabType = _Hh3cMulticastTabType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 38, 1, 4, 3, 1),
    _Hh3cMulticastTabType_Type()
)
hh3cMulticastTabType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cMulticastTabType.setStatus("current")
_Hh3cMulticastTabLen_Type = Integer32
_Hh3cMulticastTabLen_Object = MibScalar
hh3cMulticastTabLen = _Hh3cMulticastTabLen_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 38, 1, 4, 3, 2),
    _Hh3cMulticastTabLen_Type()
)
hh3cMulticastTabLen.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cMulticastTabLen.setStatus("current")
_Hh3cMulticastTabTrap_ObjectIdentity = ObjectIdentity
hh3cMulticastTabTrap = _Hh3cMulticastTabTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 38, 1, 4, 4)
)
_Hh3cNdTabStatGroup_ObjectIdentity = ObjectIdentity
hh3cNdTabStatGroup = _Hh3cNdTabStatGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 38, 1, 5)
)


class _Hh3cNdTabTrapEnable_Type(Integer32):
    """Custom type hh3cNdTabTrapEnable based on Integer32"""
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


_Hh3cNdTabTrapEnable_Type.__name__ = "Integer32"
_Hh3cNdTabTrapEnable_Object = MibScalar
hh3cNdTabTrapEnable = _Hh3cNdTabTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 38, 1, 5, 1),
    _Hh3cNdTabTrapEnable_Type()
)
hh3cNdTabTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cNdTabTrapEnable.setStatus("current")


class _Hh3cNdTabTrapInterval_Type(Integer32):
    """Custom type hh3cNdTabTrapInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 3600),
    )


_Hh3cNdTabTrapInterval_Type.__name__ = "Integer32"
_Hh3cNdTabTrapInterval_Object = MibScalar
hh3cNdTabTrapInterval = _Hh3cNdTabTrapInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 38, 1, 5, 2),
    _Hh3cNdTabTrapInterval_Type()
)
hh3cNdTabTrapInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cNdTabTrapInterval.setStatus("current")
if mibBuilder.loadTexts:
    hh3cNdTabTrapInterval.setUnits("seconds")
_Hh3cNdTabTrapInfo_ObjectIdentity = ObjectIdentity
hh3cNdTabTrapInfo = _Hh3cNdTabTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 38, 1, 5, 3)
)
_Hh3cNdTabLen_Type = Integer32
_Hh3cNdTabLen_Object = MibScalar
hh3cNdTabLen = _Hh3cNdTabLen_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 38, 1, 5, 3, 1),
    _Hh3cNdTabLen_Type()
)
hh3cNdTabLen.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cNdTabLen.setStatus("current")
_Hh3cNdTabTrap_ObjectIdentity = ObjectIdentity
hh3cNdTabTrap = _Hh3cNdTabTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 38, 1, 5, 4)
)
_Hh3cPeriodicalTrapGroup_ObjectIdentity = ObjectIdentity
hh3cPeriodicalTrapGroup = _Hh3cPeriodicalTrapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 38, 1, 6)
)
_Hh3cPeriodicalTrapObjects_ObjectIdentity = ObjectIdentity
hh3cPeriodicalTrapObjects = _Hh3cPeriodicalTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 38, 1, 6, 1)
)


class _Hh3cPeriodicalTrapInterval_Type(Integer32):
    """Custom type hh3cPeriodicalTrapInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 3600),
    )


_Hh3cPeriodicalTrapInterval_Type.__name__ = "Integer32"
_Hh3cPeriodicalTrapInterval_Object = MibScalar
hh3cPeriodicalTrapInterval = _Hh3cPeriodicalTrapInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 38, 1, 6, 1, 1),
    _Hh3cPeriodicalTrapInterval_Type()
)
hh3cPeriodicalTrapInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPeriodicalTrapInterval.setStatus("current")
if mibBuilder.loadTexts:
    hh3cPeriodicalTrapInterval.setUnits("seconds")


class _Hh3cPeriodicalTrapSwitch_Type(Integer32):
    """Custom type hh3cPeriodicalTrapSwitch based on Integer32"""
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


_Hh3cPeriodicalTrapSwitch_Type.__name__ = "Integer32"
_Hh3cPeriodicalTrapSwitch_Object = MibScalar
hh3cPeriodicalTrapSwitch = _Hh3cPeriodicalTrapSwitch_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 38, 1, 6, 1, 2),
    _Hh3cPeriodicalTrapSwitch_Type()
)
hh3cPeriodicalTrapSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPeriodicalTrapSwitch.setStatus("current")
_Hh3cPeriodicalTrapInfo_ObjectIdentity = ObjectIdentity
hh3cPeriodicalTrapInfo = _Hh3cPeriodicalTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 38, 1, 6, 2)
)
_Hh3cPeriodicalNotification_ObjectIdentity = ObjectIdentity
hh3cPeriodicalNotification = _Hh3cPeriodicalNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 38, 1, 6, 3)
)
_Hh3cPeriodicalNotificationPrefix_ObjectIdentity = ObjectIdentity
hh3cPeriodicalNotificationPrefix = _Hh3cPeriodicalNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 38, 1, 6, 3, 0)
)
_Hh3cTrapDesInfo_ObjectIdentity = ObjectIdentity
hh3cTrapDesInfo = _Hh3cTrapDesInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 38, 1, 7)
)
_Hh3cTrapDesInfoTable_Object = MibTable
hh3cTrapDesInfoTable = _Hh3cTrapDesInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 38, 1, 7, 1)
)
if mibBuilder.loadTexts:
    hh3cTrapDesInfoTable.setStatus("current")
_Hh3cTrapDesInfoEntry_Object = MibTableRow
hh3cTrapDesInfoEntry = _Hh3cTrapDesInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 38, 1, 7, 1, 1)
)
hh3cTrapDesInfoEntry.setIndexNames(
    (0, "HH3C-TRAP-MIB", "hh3cTrapDesInfoIndex"),
)
if mibBuilder.loadTexts:
    hh3cTrapDesInfoEntry.setStatus("current")


class _Hh3cTrapDesInfoIndex_Type(Integer32):
    """Custom type hh3cTrapDesInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_Hh3cTrapDesInfoIndex_Type.__name__ = "Integer32"
_Hh3cTrapDesInfoIndex_Object = MibTableColumn
hh3cTrapDesInfoIndex = _Hh3cTrapDesInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 38, 1, 7, 1, 1, 1),
    _Hh3cTrapDesInfoIndex_Type()
)
hh3cTrapDesInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cTrapDesInfoIndex.setStatus("current")
_Hh3cTrapDesIPAddress_Type = IpAddress
_Hh3cTrapDesIPAddress_Object = MibTableColumn
hh3cTrapDesIPAddress = _Hh3cTrapDesIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 38, 1, 7, 1, 1, 2),
    _Hh3cTrapDesIPAddress_Type()
)
hh3cTrapDesIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTrapDesIPAddress.setStatus("current")


class _Hh3cTrapDesPort_Type(Integer32):
    """Custom type hh3cTrapDesPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cTrapDesPort_Type.__name__ = "Integer32"
_Hh3cTrapDesPort_Object = MibTableColumn
hh3cTrapDesPort = _Hh3cTrapDesPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 38, 1, 7, 1, 1, 3),
    _Hh3cTrapDesPort_Type()
)
hh3cTrapDesPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTrapDesPort.setStatus("current")
_Hh3cTrapDesRowStatus_Type = RowStatus
_Hh3cTrapDesRowStatus_Object = MibTableColumn
hh3cTrapDesRowStatus = _Hh3cTrapDesRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 38, 1, 7, 1, 1, 4),
    _Hh3cTrapDesRowStatus_Type()
)
hh3cTrapDesRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTrapDesRowStatus.setStatus("current")
_Hh3cTrapDesAddrTAddress_Type = TAddress
_Hh3cTrapDesAddrTAddress_Object = MibTableColumn
hh3cTrapDesAddrTAddress = _Hh3cTrapDesAddrTAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 38, 1, 7, 1, 1, 5),
    _Hh3cTrapDesAddrTAddress_Type()
)
hh3cTrapDesAddrTAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTrapDesAddrTAddress.setStatus("current")
_Hh3cTrapConfig_ObjectIdentity = ObjectIdentity
hh3cTrapConfig = _Hh3cTrapConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 38, 1, 8)
)
_Hh3cTrapConfigTable_Object = MibTable
hh3cTrapConfigTable = _Hh3cTrapConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 38, 1, 8, 1)
)
if mibBuilder.loadTexts:
    hh3cTrapConfigTable.setStatus("current")
_Hh3cTrapConfigEntry_Object = MibTableRow
hh3cTrapConfigEntry = _Hh3cTrapConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 38, 1, 8, 1, 1)
)
hh3cTrapConfigEntry.setIndexNames(
    (0, "HH3C-TRAP-MIB", "hh3cTrapConfigIndex"),
)
if mibBuilder.loadTexts:
    hh3cTrapConfigEntry.setStatus("current")


class _Hh3cTrapConfigIndex_Type(Integer32):
    """Custom type hh3cTrapConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cTrapConfigIndex_Type.__name__ = "Integer32"
_Hh3cTrapConfigIndex_Object = MibTableColumn
hh3cTrapConfigIndex = _Hh3cTrapConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 38, 1, 8, 1, 1, 1),
    _Hh3cTrapConfigIndex_Type()
)
hh3cTrapConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cTrapConfigIndex.setStatus("current")


class _Hh3cTrapConfigName_Type(SnmpAdminString):
    """Custom type hh3cTrapConfigName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cTrapConfigName_Type.__name__ = "SnmpAdminString"
_Hh3cTrapConfigName_Object = MibTableColumn
hh3cTrapConfigName = _Hh3cTrapConfigName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 38, 1, 8, 1, 1, 2),
    _Hh3cTrapConfigName_Type()
)
hh3cTrapConfigName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cTrapConfigName.setStatus("current")


class _Hh3cTrapConfigDescr_Type(SnmpAdminString):
    """Custom type hh3cTrapConfigDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cTrapConfigDescr_Type.__name__ = "SnmpAdminString"
_Hh3cTrapConfigDescr_Object = MibTableColumn
hh3cTrapConfigDescr = _Hh3cTrapConfigDescr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 38, 1, 8, 1, 1, 3),
    _Hh3cTrapConfigDescr_Type()
)
hh3cTrapConfigDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cTrapConfigDescr.setStatus("current")


class _Hh3cTrapConfigSwitch_Type(Integer32):
    """Custom type hh3cTrapConfigSwitch based on Integer32"""
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


_Hh3cTrapConfigSwitch_Type.__name__ = "Integer32"
_Hh3cTrapConfigSwitch_Object = MibTableColumn
hh3cTrapConfigSwitch = _Hh3cTrapConfigSwitch_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 38, 1, 8, 1, 1, 4),
    _Hh3cTrapConfigSwitch_Type()
)
hh3cTrapConfigSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cTrapConfigSwitch.setStatus("current")

# Managed Objects groups


# Notification objects

hh3cMacTabFullTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 38, 1, 1, 4, 1)
)
hh3cMacTabFullTrap.setObjects(
    ("HH3C-TRAP-MIB", "hh3cMacTabLen")
)
if mibBuilder.loadTexts:
    hh3cMacTabFullTrap.setStatus(
        "current"
    )

hh3cMacTabAlmostFullTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 38, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    hh3cMacTabAlmostFullTrap.setStatus(
        "current"
    )

hh3cArpTabFullTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 38, 1, 2, 4, 1)
)
hh3cArpTabFullTrap.setObjects(
    ("HH3C-TRAP-MIB", "hh3cArpTabLen")
)
if mibBuilder.loadTexts:
    hh3cArpTabFullTrap.setStatus(
        "current"
    )

hh3cArpPortDynamicEntryFullTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 38, 1, 2, 4, 2)
)
hh3cArpPortDynamicEntryFullTrap.setObjects(
      *(("HH3C-TRAP-MIB", "hh3cArpTabLen"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hh3cArpPortDynamicEntryFullTrap.setStatus(
        "current"
    )

hh3cRtTabFullTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 38, 1, 3, 5, 1)
)
hh3cRtTabFullTrap.setObjects(
    ("HH3C-TRAP-MIB", "hh3cRtTabLen")
)
if mibBuilder.loadTexts:
    hh3cRtTabFullTrap.setStatus(
        "current"
    )

hh3cDetailRtTabFullTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 38, 1, 3, 5, 2)
)
hh3cDetailRtTabFullTrap.setObjects(
      *(("HH3C-TRAP-MIB", "hh3cDetailRtProType"),
        ("HH3C-TRAP-MIB", "hh3cRtTabLen"))
)
if mibBuilder.loadTexts:
    hh3cDetailRtTabFullTrap.setStatus(
        "current"
    )

hh3cDefaultRtDelTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 38, 1, 3, 5, 3)
)
hh3cDefaultRtDelTrap.setObjects(
      *(("HH3C-TRAP-MIB", "hh3cDetailRtProType"),
        ("HH3C-TRAP-MIB", "hh3cDefaultRtNextHopType"),
        ("HH3C-TRAP-MIB", "hh3cDefaultRtNextHop"),
        ("HH3C-TRAP-MIB", "hh3cDefaultRtOutIf"))
)
if mibBuilder.loadTexts:
    hh3cDefaultRtDelTrap.setStatus(
        "current"
    )

hh3cMulticastTabFullTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 38, 1, 4, 4, 1)
)
hh3cMulticastTabFullTrap.setObjects(
      *(("HH3C-TRAP-MIB", "hh3cMulticastTabType"),
        ("HH3C-TRAP-MIB", "hh3cMulticastTabLen"))
)
if mibBuilder.loadTexts:
    hh3cMulticastTabFullTrap.setStatus(
        "current"
    )

hh3cNdTabFullTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 38, 1, 5, 4, 1)
)
hh3cNdTabFullTrap.setObjects(
    ("HH3C-TRAP-MIB", "hh3cNdTabLen")
)
if mibBuilder.loadTexts:
    hh3cNdTabFullTrap.setStatus(
        "current"
    )

hh3cPeriodicalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 38, 1, 6, 3, 0, 1)
)
if mibBuilder.loadTexts:
    hh3cPeriodicalTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-TRAP-MIB",
    **{"hh3cTrap": hh3cTrap,
       "hh3cTableGroup": hh3cTableGroup,
       "hh3cMacTabStatGroup": hh3cMacTabStatGroup,
       "hh3cMacTabTrapEnable": hh3cMacTabTrapEnable,
       "hh3cMacTabTrapInterval": hh3cMacTabTrapInterval,
       "hh3cMacTabTrapInfo": hh3cMacTabTrapInfo,
       "hh3cMacTabLen": hh3cMacTabLen,
       "hh3cMacTabTrap": hh3cMacTabTrap,
       "hh3cMacTabFullTrap": hh3cMacTabFullTrap,
       "hh3cMacTabAlmostFullTrap": hh3cMacTabAlmostFullTrap,
       "hh3cArpTabStatGroup": hh3cArpTabStatGroup,
       "hh3cArpTabTrapEnable": hh3cArpTabTrapEnable,
       "hh3cArpTabTrapInterval": hh3cArpTabTrapInterval,
       "hh3cArpTabTrapInfo": hh3cArpTabTrapInfo,
       "hh3cArpTabLen": hh3cArpTabLen,
       "hh3cArpTabTrap": hh3cArpTabTrap,
       "hh3cArpTabFullTrap": hh3cArpTabFullTrap,
       "hh3cArpPortDynamicEntryFullTrap": hh3cArpPortDynamicEntryFullTrap,
       "hh3cRtTabStatGroup": hh3cRtTabStatGroup,
       "hh3cDetailRtTrapTable": hh3cDetailRtTrapTable,
       "hh3cDetailRtTrapEntry": hh3cDetailRtTrapEntry,
       "hh3cDetailRtProType": hh3cDetailRtProType,
       "hh3cDetailRtEnable": hh3cDetailRtEnable,
       "hh3cRtTabTrapEnable": hh3cRtTabTrapEnable,
       "hh3cRtTabTrapInterval": hh3cRtTabTrapInterval,
       "hh3cRtTabTrapInfo": hh3cRtTabTrapInfo,
       "hh3cRtTabLen": hh3cRtTabLen,
       "hh3cDefaultRtNextHopType": hh3cDefaultRtNextHopType,
       "hh3cDefaultRtNextHop": hh3cDefaultRtNextHop,
       "hh3cDefaultRtOutIf": hh3cDefaultRtOutIf,
       "hh3cRtTabTrap": hh3cRtTabTrap,
       "hh3cRtTabFullTrap": hh3cRtTabFullTrap,
       "hh3cDetailRtTabFullTrap": hh3cDetailRtTabFullTrap,
       "hh3cDefaultRtDelTrap": hh3cDefaultRtDelTrap,
       "hh3cDefaultRtDelTrapEnable": hh3cDefaultRtDelTrapEnable,
       "hh3cMulticastTabStatGroup": hh3cMulticastTabStatGroup,
       "hh3cMulticastTabTrapEnable": hh3cMulticastTabTrapEnable,
       "hh3cMulticastTabTrapInterval": hh3cMulticastTabTrapInterval,
       "hh3cMulticastTabTrapInfo": hh3cMulticastTabTrapInfo,
       "hh3cMulticastTabType": hh3cMulticastTabType,
       "hh3cMulticastTabLen": hh3cMulticastTabLen,
       "hh3cMulticastTabTrap": hh3cMulticastTabTrap,
       "hh3cMulticastTabFullTrap": hh3cMulticastTabFullTrap,
       "hh3cNdTabStatGroup": hh3cNdTabStatGroup,
       "hh3cNdTabTrapEnable": hh3cNdTabTrapEnable,
       "hh3cNdTabTrapInterval": hh3cNdTabTrapInterval,
       "hh3cNdTabTrapInfo": hh3cNdTabTrapInfo,
       "hh3cNdTabLen": hh3cNdTabLen,
       "hh3cNdTabTrap": hh3cNdTabTrap,
       "hh3cNdTabFullTrap": hh3cNdTabFullTrap,
       "hh3cPeriodicalTrapGroup": hh3cPeriodicalTrapGroup,
       "hh3cPeriodicalTrapObjects": hh3cPeriodicalTrapObjects,
       "hh3cPeriodicalTrapInterval": hh3cPeriodicalTrapInterval,
       "hh3cPeriodicalTrapSwitch": hh3cPeriodicalTrapSwitch,
       "hh3cPeriodicalTrapInfo": hh3cPeriodicalTrapInfo,
       "hh3cPeriodicalNotification": hh3cPeriodicalNotification,
       "hh3cPeriodicalNotificationPrefix": hh3cPeriodicalNotificationPrefix,
       "hh3cPeriodicalTrap": hh3cPeriodicalTrap,
       "hh3cTrapDesInfo": hh3cTrapDesInfo,
       "hh3cTrapDesInfoTable": hh3cTrapDesInfoTable,
       "hh3cTrapDesInfoEntry": hh3cTrapDesInfoEntry,
       "hh3cTrapDesInfoIndex": hh3cTrapDesInfoIndex,
       "hh3cTrapDesIPAddress": hh3cTrapDesIPAddress,
       "hh3cTrapDesPort": hh3cTrapDesPort,
       "hh3cTrapDesRowStatus": hh3cTrapDesRowStatus,
       "hh3cTrapDesAddrTAddress": hh3cTrapDesAddrTAddress,
       "hh3cTrapConfig": hh3cTrapConfig,
       "hh3cTrapConfigTable": hh3cTrapConfigTable,
       "hh3cTrapConfigEntry": hh3cTrapConfigEntry,
       "hh3cTrapConfigIndex": hh3cTrapConfigIndex,
       "hh3cTrapConfigName": hh3cTrapConfigName,
       "hh3cTrapConfigDescr": hh3cTrapConfigDescr,
       "hh3cTrapConfigSwitch": hh3cTrapConfigSwitch}
)
