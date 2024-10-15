# SNMP MIB module (H3C-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H3C-TRAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:51:34 2024
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

(h3cCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

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

h3cTrap = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 38)
)
h3cTrap.setRevisions(
        ("2010-06-05 10:50",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cTableGroup_ObjectIdentity = ObjectIdentity
h3cTableGroup = _H3cTableGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 38, 1)
)
_H3cMacTabStatGroup_ObjectIdentity = ObjectIdentity
h3cMacTabStatGroup = _H3cMacTabStatGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 38, 1, 1)
)


class _H3cMacTabTrapEnable_Type(Integer32):
    """Custom type h3cMacTabTrapEnable based on Integer32"""
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


_H3cMacTabTrapEnable_Type.__name__ = "Integer32"
_H3cMacTabTrapEnable_Object = MibScalar
h3cMacTabTrapEnable = _H3cMacTabTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 38, 1, 1, 1),
    _H3cMacTabTrapEnable_Type()
)
h3cMacTabTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cMacTabTrapEnable.setStatus("current")


class _H3cMacTabTrapInterval_Type(Integer32):
    """Custom type h3cMacTabTrapInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 3600),
    )


_H3cMacTabTrapInterval_Type.__name__ = "Integer32"
_H3cMacTabTrapInterval_Object = MibScalar
h3cMacTabTrapInterval = _H3cMacTabTrapInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 38, 1, 1, 2),
    _H3cMacTabTrapInterval_Type()
)
h3cMacTabTrapInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cMacTabTrapInterval.setStatus("current")
if mibBuilder.loadTexts:
    h3cMacTabTrapInterval.setUnits("seconds")
_H3cMacTabTrapInfo_ObjectIdentity = ObjectIdentity
h3cMacTabTrapInfo = _H3cMacTabTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 38, 1, 1, 3)
)
_H3cMacTabLen_Type = Integer32
_H3cMacTabLen_Object = MibScalar
h3cMacTabLen = _H3cMacTabLen_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 38, 1, 1, 3, 1),
    _H3cMacTabLen_Type()
)
h3cMacTabLen.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cMacTabLen.setStatus("current")
_H3cMacTabTrap_ObjectIdentity = ObjectIdentity
h3cMacTabTrap = _H3cMacTabTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 38, 1, 1, 4)
)
_H3cArpTabStatGroup_ObjectIdentity = ObjectIdentity
h3cArpTabStatGroup = _H3cArpTabStatGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 38, 1, 2)
)


class _H3cArpTabTrapEnable_Type(Integer32):
    """Custom type h3cArpTabTrapEnable based on Integer32"""
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


_H3cArpTabTrapEnable_Type.__name__ = "Integer32"
_H3cArpTabTrapEnable_Object = MibScalar
h3cArpTabTrapEnable = _H3cArpTabTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 38, 1, 2, 1),
    _H3cArpTabTrapEnable_Type()
)
h3cArpTabTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cArpTabTrapEnable.setStatus("current")


class _H3cArpTabTrapInterval_Type(Integer32):
    """Custom type h3cArpTabTrapInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 3600),
    )


_H3cArpTabTrapInterval_Type.__name__ = "Integer32"
_H3cArpTabTrapInterval_Object = MibScalar
h3cArpTabTrapInterval = _H3cArpTabTrapInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 38, 1, 2, 2),
    _H3cArpTabTrapInterval_Type()
)
h3cArpTabTrapInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cArpTabTrapInterval.setStatus("current")
if mibBuilder.loadTexts:
    h3cArpTabTrapInterval.setUnits("seconds")
_H3cArpTabTrapInfo_ObjectIdentity = ObjectIdentity
h3cArpTabTrapInfo = _H3cArpTabTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 38, 1, 2, 3)
)
_H3cArpTabLen_Type = Integer32
_H3cArpTabLen_Object = MibScalar
h3cArpTabLen = _H3cArpTabLen_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 38, 1, 2, 3, 1),
    _H3cArpTabLen_Type()
)
h3cArpTabLen.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cArpTabLen.setStatus("current")
_H3cArpTabTrap_ObjectIdentity = ObjectIdentity
h3cArpTabTrap = _H3cArpTabTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 38, 1, 2, 4)
)
_H3cRtTabStatGroup_ObjectIdentity = ObjectIdentity
h3cRtTabStatGroup = _H3cRtTabStatGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 38, 1, 3)
)
_H3cDetailRtTrapTable_Object = MibTable
h3cDetailRtTrapTable = _H3cDetailRtTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 38, 1, 3, 1)
)
if mibBuilder.loadTexts:
    h3cDetailRtTrapTable.setStatus("current")
_H3cDetailRtTrapEntry_Object = MibTableRow
h3cDetailRtTrapEntry = _H3cDetailRtTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 38, 1, 3, 1, 1)
)
h3cDetailRtTrapEntry.setIndexNames(
    (0, "H3C-TRAP-MIB", "h3cDetailRtProType"),
)
if mibBuilder.loadTexts:
    h3cDetailRtTrapEntry.setStatus("current")


class _H3cDetailRtProType_Type(Integer32):
    """Custom type h3cDetailRtProType based on Integer32"""
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


_H3cDetailRtProType_Type.__name__ = "Integer32"
_H3cDetailRtProType_Object = MibTableColumn
h3cDetailRtProType = _H3cDetailRtProType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 38, 1, 3, 1, 1, 1),
    _H3cDetailRtProType_Type()
)
h3cDetailRtProType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDetailRtProType.setStatus("current")


class _H3cDetailRtEnable_Type(Integer32):
    """Custom type h3cDetailRtEnable based on Integer32"""
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


_H3cDetailRtEnable_Type.__name__ = "Integer32"
_H3cDetailRtEnable_Object = MibTableColumn
h3cDetailRtEnable = _H3cDetailRtEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 38, 1, 3, 1, 1, 2),
    _H3cDetailRtEnable_Type()
)
h3cDetailRtEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDetailRtEnable.setStatus("current")


class _H3cRtTabTrapEnable_Type(Integer32):
    """Custom type h3cRtTabTrapEnable based on Integer32"""
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


_H3cRtTabTrapEnable_Type.__name__ = "Integer32"
_H3cRtTabTrapEnable_Object = MibScalar
h3cRtTabTrapEnable = _H3cRtTabTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 38, 1, 3, 2),
    _H3cRtTabTrapEnable_Type()
)
h3cRtTabTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cRtTabTrapEnable.setStatus("current")


class _H3cRtTabTrapInterval_Type(Integer32):
    """Custom type h3cRtTabTrapInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 3600),
    )


_H3cRtTabTrapInterval_Type.__name__ = "Integer32"
_H3cRtTabTrapInterval_Object = MibScalar
h3cRtTabTrapInterval = _H3cRtTabTrapInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 38, 1, 3, 3),
    _H3cRtTabTrapInterval_Type()
)
h3cRtTabTrapInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cRtTabTrapInterval.setStatus("current")
if mibBuilder.loadTexts:
    h3cRtTabTrapInterval.setUnits("seconds")
_H3cRtTabTrapInfo_ObjectIdentity = ObjectIdentity
h3cRtTabTrapInfo = _H3cRtTabTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 38, 1, 3, 4)
)
_H3cRtTabLen_Type = Integer32
_H3cRtTabLen_Object = MibScalar
h3cRtTabLen = _H3cRtTabLen_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 38, 1, 3, 4, 1),
    _H3cRtTabLen_Type()
)
h3cRtTabLen.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cRtTabLen.setStatus("current")
_H3cDefaultRtNextHopType_Type = InetAddressType
_H3cDefaultRtNextHopType_Object = MibScalar
h3cDefaultRtNextHopType = _H3cDefaultRtNextHopType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 38, 1, 3, 4, 2),
    _H3cDefaultRtNextHopType_Type()
)
h3cDefaultRtNextHopType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDefaultRtNextHopType.setStatus("current")
_H3cDefaultRtNextHop_Type = InetAddress
_H3cDefaultRtNextHop_Object = MibScalar
h3cDefaultRtNextHop = _H3cDefaultRtNextHop_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 38, 1, 3, 4, 3),
    _H3cDefaultRtNextHop_Type()
)
h3cDefaultRtNextHop.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDefaultRtNextHop.setStatus("current")
_H3cDefaultRtOutIf_Type = InterfaceIndex
_H3cDefaultRtOutIf_Object = MibScalar
h3cDefaultRtOutIf = _H3cDefaultRtOutIf_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 38, 1, 3, 4, 4),
    _H3cDefaultRtOutIf_Type()
)
h3cDefaultRtOutIf.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cDefaultRtOutIf.setStatus("current")
_H3cRtTabTrap_ObjectIdentity = ObjectIdentity
h3cRtTabTrap = _H3cRtTabTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 38, 1, 3, 5)
)


class _H3cDefaultRtDelTrapEnable_Type(TruthValue):
    """Custom type h3cDefaultRtDelTrapEnable based on TruthValue"""


_H3cDefaultRtDelTrapEnable_Object = MibScalar
h3cDefaultRtDelTrapEnable = _H3cDefaultRtDelTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 38, 1, 3, 6),
    _H3cDefaultRtDelTrapEnable_Type()
)
h3cDefaultRtDelTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDefaultRtDelTrapEnable.setStatus("current")
_H3cMulticastTabStatGroup_ObjectIdentity = ObjectIdentity
h3cMulticastTabStatGroup = _H3cMulticastTabStatGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 38, 1, 4)
)


class _H3cMulticastTabTrapEnable_Type(Integer32):
    """Custom type h3cMulticastTabTrapEnable based on Integer32"""
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


_H3cMulticastTabTrapEnable_Type.__name__ = "Integer32"
_H3cMulticastTabTrapEnable_Object = MibScalar
h3cMulticastTabTrapEnable = _H3cMulticastTabTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 38, 1, 4, 1),
    _H3cMulticastTabTrapEnable_Type()
)
h3cMulticastTabTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cMulticastTabTrapEnable.setStatus("current")


class _H3cMulticastTabTrapInterval_Type(Integer32):
    """Custom type h3cMulticastTabTrapInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 3600),
    )


_H3cMulticastTabTrapInterval_Type.__name__ = "Integer32"
_H3cMulticastTabTrapInterval_Object = MibScalar
h3cMulticastTabTrapInterval = _H3cMulticastTabTrapInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 38, 1, 4, 2),
    _H3cMulticastTabTrapInterval_Type()
)
h3cMulticastTabTrapInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cMulticastTabTrapInterval.setStatus("current")
if mibBuilder.loadTexts:
    h3cMulticastTabTrapInterval.setUnits("seconds")
_H3cMulticastTabTrapInfo_ObjectIdentity = ObjectIdentity
h3cMulticastTabTrapInfo = _H3cMulticastTabTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 38, 1, 4, 3)
)


class _H3cMulticastTabType_Type(Integer32):
    """Custom type h3cMulticastTabType based on Integer32"""
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


_H3cMulticastTabType_Type.__name__ = "Integer32"
_H3cMulticastTabType_Object = MibScalar
h3cMulticastTabType = _H3cMulticastTabType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 38, 1, 4, 3, 1),
    _H3cMulticastTabType_Type()
)
h3cMulticastTabType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cMulticastTabType.setStatus("current")
_H3cMulticastTabLen_Type = Integer32
_H3cMulticastTabLen_Object = MibScalar
h3cMulticastTabLen = _H3cMulticastTabLen_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 38, 1, 4, 3, 2),
    _H3cMulticastTabLen_Type()
)
h3cMulticastTabLen.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cMulticastTabLen.setStatus("current")
_H3cMulticastTabTrap_ObjectIdentity = ObjectIdentity
h3cMulticastTabTrap = _H3cMulticastTabTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 38, 1, 4, 4)
)
_H3cNdTabStatGroup_ObjectIdentity = ObjectIdentity
h3cNdTabStatGroup = _H3cNdTabStatGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 38, 1, 5)
)


class _H3cNdTabTrapEnable_Type(Integer32):
    """Custom type h3cNdTabTrapEnable based on Integer32"""
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


_H3cNdTabTrapEnable_Type.__name__ = "Integer32"
_H3cNdTabTrapEnable_Object = MibScalar
h3cNdTabTrapEnable = _H3cNdTabTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 38, 1, 5, 1),
    _H3cNdTabTrapEnable_Type()
)
h3cNdTabTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cNdTabTrapEnable.setStatus("current")


class _H3cNdTabTrapInterval_Type(Integer32):
    """Custom type h3cNdTabTrapInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 3600),
    )


_H3cNdTabTrapInterval_Type.__name__ = "Integer32"
_H3cNdTabTrapInterval_Object = MibScalar
h3cNdTabTrapInterval = _H3cNdTabTrapInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 38, 1, 5, 2),
    _H3cNdTabTrapInterval_Type()
)
h3cNdTabTrapInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cNdTabTrapInterval.setStatus("current")
if mibBuilder.loadTexts:
    h3cNdTabTrapInterval.setUnits("seconds")
_H3cNdTabTrapInfo_ObjectIdentity = ObjectIdentity
h3cNdTabTrapInfo = _H3cNdTabTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 38, 1, 5, 3)
)
_H3cNdTabLen_Type = Integer32
_H3cNdTabLen_Object = MibScalar
h3cNdTabLen = _H3cNdTabLen_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 38, 1, 5, 3, 1),
    _H3cNdTabLen_Type()
)
h3cNdTabLen.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cNdTabLen.setStatus("current")
_H3cNdTabTrap_ObjectIdentity = ObjectIdentity
h3cNdTabTrap = _H3cNdTabTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 38, 1, 5, 4)
)
_H3cPeriodicalTrapGroup_ObjectIdentity = ObjectIdentity
h3cPeriodicalTrapGroup = _H3cPeriodicalTrapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 38, 1, 6)
)
_H3cPeriodicalTrapObjects_ObjectIdentity = ObjectIdentity
h3cPeriodicalTrapObjects = _H3cPeriodicalTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 38, 1, 6, 1)
)


class _H3cPeriodicalTrapInterval_Type(Integer32):
    """Custom type h3cPeriodicalTrapInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 3600),
    )


_H3cPeriodicalTrapInterval_Type.__name__ = "Integer32"
_H3cPeriodicalTrapInterval_Object = MibScalar
h3cPeriodicalTrapInterval = _H3cPeriodicalTrapInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 38, 1, 6, 1, 1),
    _H3cPeriodicalTrapInterval_Type()
)
h3cPeriodicalTrapInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cPeriodicalTrapInterval.setStatus("current")
if mibBuilder.loadTexts:
    h3cPeriodicalTrapInterval.setUnits("seconds")


class _H3cPeriodicalTrapSwitch_Type(Integer32):
    """Custom type h3cPeriodicalTrapSwitch based on Integer32"""
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


_H3cPeriodicalTrapSwitch_Type.__name__ = "Integer32"
_H3cPeriodicalTrapSwitch_Object = MibScalar
h3cPeriodicalTrapSwitch = _H3cPeriodicalTrapSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 38, 1, 6, 1, 2),
    _H3cPeriodicalTrapSwitch_Type()
)
h3cPeriodicalTrapSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cPeriodicalTrapSwitch.setStatus("current")
_H3cPeriodicalTrapInfo_ObjectIdentity = ObjectIdentity
h3cPeriodicalTrapInfo = _H3cPeriodicalTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 38, 1, 6, 2)
)
_H3cPeriodicalNotification_ObjectIdentity = ObjectIdentity
h3cPeriodicalNotification = _H3cPeriodicalNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 38, 1, 6, 3)
)
_H3cPeriodicalNotificationPrefix_ObjectIdentity = ObjectIdentity
h3cPeriodicalNotificationPrefix = _H3cPeriodicalNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 38, 1, 6, 3, 0)
)
_H3cTrapDesInfo_ObjectIdentity = ObjectIdentity
h3cTrapDesInfo = _H3cTrapDesInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 38, 1, 7)
)
_H3cTrapDesInfoTable_Object = MibTable
h3cTrapDesInfoTable = _H3cTrapDesInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 38, 1, 7, 1)
)
if mibBuilder.loadTexts:
    h3cTrapDesInfoTable.setStatus("current")
_H3cTrapDesInfoEntry_Object = MibTableRow
h3cTrapDesInfoEntry = _H3cTrapDesInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 38, 1, 7, 1, 1)
)
h3cTrapDesInfoEntry.setIndexNames(
    (0, "H3C-TRAP-MIB", "h3cTrapDesInfoIndex"),
)
if mibBuilder.loadTexts:
    h3cTrapDesInfoEntry.setStatus("current")


class _H3cTrapDesInfoIndex_Type(Integer32):
    """Custom type h3cTrapDesInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_H3cTrapDesInfoIndex_Type.__name__ = "Integer32"
_H3cTrapDesInfoIndex_Object = MibTableColumn
h3cTrapDesInfoIndex = _H3cTrapDesInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 38, 1, 7, 1, 1, 1),
    _H3cTrapDesInfoIndex_Type()
)
h3cTrapDesInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cTrapDesInfoIndex.setStatus("current")
_H3cTrapDesIPAddress_Type = IpAddress
_H3cTrapDesIPAddress_Object = MibTableColumn
h3cTrapDesIPAddress = _H3cTrapDesIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 38, 1, 7, 1, 1, 2),
    _H3cTrapDesIPAddress_Type()
)
h3cTrapDesIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cTrapDesIPAddress.setStatus("current")


class _H3cTrapDesPort_Type(Integer32):
    """Custom type h3cTrapDesPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cTrapDesPort_Type.__name__ = "Integer32"
_H3cTrapDesPort_Object = MibTableColumn
h3cTrapDesPort = _H3cTrapDesPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 38, 1, 7, 1, 1, 3),
    _H3cTrapDesPort_Type()
)
h3cTrapDesPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cTrapDesPort.setStatus("current")
_H3cTrapDesRowStatus_Type = RowStatus
_H3cTrapDesRowStatus_Object = MibTableColumn
h3cTrapDesRowStatus = _H3cTrapDesRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 38, 1, 7, 1, 1, 4),
    _H3cTrapDesRowStatus_Type()
)
h3cTrapDesRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cTrapDesRowStatus.setStatus("current")
_H3cTrapDesAddrTAddress_Type = TAddress
_H3cTrapDesAddrTAddress_Object = MibTableColumn
h3cTrapDesAddrTAddress = _H3cTrapDesAddrTAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 38, 1, 7, 1, 1, 5),
    _H3cTrapDesAddrTAddress_Type()
)
h3cTrapDesAddrTAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cTrapDesAddrTAddress.setStatus("current")
_H3cTrapConfig_ObjectIdentity = ObjectIdentity
h3cTrapConfig = _H3cTrapConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 38, 1, 8)
)
_H3cTrapConfigTable_Object = MibTable
h3cTrapConfigTable = _H3cTrapConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 38, 1, 8, 1)
)
if mibBuilder.loadTexts:
    h3cTrapConfigTable.setStatus("current")
_H3cTrapConfigEntry_Object = MibTableRow
h3cTrapConfigEntry = _H3cTrapConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 38, 1, 8, 1, 1)
)
h3cTrapConfigEntry.setIndexNames(
    (0, "H3C-TRAP-MIB", "h3cTrapConfigIndex"),
)
if mibBuilder.loadTexts:
    h3cTrapConfigEntry.setStatus("current")


class _H3cTrapConfigIndex_Type(Integer32):
    """Custom type h3cTrapConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cTrapConfigIndex_Type.__name__ = "Integer32"
_H3cTrapConfigIndex_Object = MibTableColumn
h3cTrapConfigIndex = _H3cTrapConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 38, 1, 8, 1, 1, 1),
    _H3cTrapConfigIndex_Type()
)
h3cTrapConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cTrapConfigIndex.setStatus("current")


class _H3cTrapConfigName_Type(SnmpAdminString):
    """Custom type h3cTrapConfigName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_H3cTrapConfigName_Type.__name__ = "SnmpAdminString"
_H3cTrapConfigName_Object = MibTableColumn
h3cTrapConfigName = _H3cTrapConfigName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 38, 1, 8, 1, 1, 2),
    _H3cTrapConfigName_Type()
)
h3cTrapConfigName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cTrapConfigName.setStatus("current")


class _H3cTrapConfigDescr_Type(SnmpAdminString):
    """Custom type h3cTrapConfigDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_H3cTrapConfigDescr_Type.__name__ = "SnmpAdminString"
_H3cTrapConfigDescr_Object = MibTableColumn
h3cTrapConfigDescr = _H3cTrapConfigDescr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 38, 1, 8, 1, 1, 3),
    _H3cTrapConfigDescr_Type()
)
h3cTrapConfigDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cTrapConfigDescr.setStatus("current")


class _H3cTrapConfigSwitch_Type(Integer32):
    """Custom type h3cTrapConfigSwitch based on Integer32"""
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


_H3cTrapConfigSwitch_Type.__name__ = "Integer32"
_H3cTrapConfigSwitch_Object = MibTableColumn
h3cTrapConfigSwitch = _H3cTrapConfigSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 38, 1, 8, 1, 1, 4),
    _H3cTrapConfigSwitch_Type()
)
h3cTrapConfigSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cTrapConfigSwitch.setStatus("current")

# Managed Objects groups


# Notification objects

h3cMacTabFullTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 38, 1, 1, 4, 1)
)
h3cMacTabFullTrap.setObjects(
    ("H3C-TRAP-MIB", "h3cMacTabLen")
)
if mibBuilder.loadTexts:
    h3cMacTabFullTrap.setStatus(
        "current"
    )

h3cMacTabAlmostFullTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 38, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    h3cMacTabAlmostFullTrap.setStatus(
        "current"
    )

h3cArpTabFullTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 38, 1, 2, 4, 1)
)
h3cArpTabFullTrap.setObjects(
    ("H3C-TRAP-MIB", "h3cArpTabLen")
)
if mibBuilder.loadTexts:
    h3cArpTabFullTrap.setStatus(
        "current"
    )

h3cArpPortDynamicEntryFullTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 38, 1, 2, 4, 2)
)
h3cArpPortDynamicEntryFullTrap.setObjects(
      *(("H3C-TRAP-MIB", "h3cArpTabLen"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    h3cArpPortDynamicEntryFullTrap.setStatus(
        "current"
    )

h3cRtTabFullTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 38, 1, 3, 5, 1)
)
h3cRtTabFullTrap.setObjects(
    ("H3C-TRAP-MIB", "h3cRtTabLen")
)
if mibBuilder.loadTexts:
    h3cRtTabFullTrap.setStatus(
        "current"
    )

h3cDetailRtTabFullTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 38, 1, 3, 5, 2)
)
h3cDetailRtTabFullTrap.setObjects(
      *(("H3C-TRAP-MIB", "h3cDetailRtProType"),
        ("H3C-TRAP-MIB", "h3cRtTabLen"))
)
if mibBuilder.loadTexts:
    h3cDetailRtTabFullTrap.setStatus(
        "current"
    )

h3cDefaultRtDelTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 38, 1, 3, 5, 3)
)
h3cDefaultRtDelTrap.setObjects(
      *(("H3C-TRAP-MIB", "h3cDetailRtProType"),
        ("H3C-TRAP-MIB", "h3cDefaultRtNextHopType"),
        ("H3C-TRAP-MIB", "h3cDefaultRtNextHop"),
        ("H3C-TRAP-MIB", "h3cDefaultRtOutIf"))
)
if mibBuilder.loadTexts:
    h3cDefaultRtDelTrap.setStatus(
        "current"
    )

h3cMulticastTabFullTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 38, 1, 4, 4, 1)
)
h3cMulticastTabFullTrap.setObjects(
      *(("H3C-TRAP-MIB", "h3cMulticastTabType"),
        ("H3C-TRAP-MIB", "h3cMulticastTabLen"))
)
if mibBuilder.loadTexts:
    h3cMulticastTabFullTrap.setStatus(
        "current"
    )

h3cNdTabFullTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 38, 1, 5, 4, 1)
)
h3cNdTabFullTrap.setObjects(
    ("H3C-TRAP-MIB", "h3cNdTabLen")
)
if mibBuilder.loadTexts:
    h3cNdTabFullTrap.setStatus(
        "current"
    )

h3cPeriodicalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 38, 1, 6, 3, 0, 1)
)
if mibBuilder.loadTexts:
    h3cPeriodicalTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-TRAP-MIB",
    **{"h3cTrap": h3cTrap,
       "h3cTableGroup": h3cTableGroup,
       "h3cMacTabStatGroup": h3cMacTabStatGroup,
       "h3cMacTabTrapEnable": h3cMacTabTrapEnable,
       "h3cMacTabTrapInterval": h3cMacTabTrapInterval,
       "h3cMacTabTrapInfo": h3cMacTabTrapInfo,
       "h3cMacTabLen": h3cMacTabLen,
       "h3cMacTabTrap": h3cMacTabTrap,
       "h3cMacTabFullTrap": h3cMacTabFullTrap,
       "h3cMacTabAlmostFullTrap": h3cMacTabAlmostFullTrap,
       "h3cArpTabStatGroup": h3cArpTabStatGroup,
       "h3cArpTabTrapEnable": h3cArpTabTrapEnable,
       "h3cArpTabTrapInterval": h3cArpTabTrapInterval,
       "h3cArpTabTrapInfo": h3cArpTabTrapInfo,
       "h3cArpTabLen": h3cArpTabLen,
       "h3cArpTabTrap": h3cArpTabTrap,
       "h3cArpTabFullTrap": h3cArpTabFullTrap,
       "h3cArpPortDynamicEntryFullTrap": h3cArpPortDynamicEntryFullTrap,
       "h3cRtTabStatGroup": h3cRtTabStatGroup,
       "h3cDetailRtTrapTable": h3cDetailRtTrapTable,
       "h3cDetailRtTrapEntry": h3cDetailRtTrapEntry,
       "h3cDetailRtProType": h3cDetailRtProType,
       "h3cDetailRtEnable": h3cDetailRtEnable,
       "h3cRtTabTrapEnable": h3cRtTabTrapEnable,
       "h3cRtTabTrapInterval": h3cRtTabTrapInterval,
       "h3cRtTabTrapInfo": h3cRtTabTrapInfo,
       "h3cRtTabLen": h3cRtTabLen,
       "h3cDefaultRtNextHopType": h3cDefaultRtNextHopType,
       "h3cDefaultRtNextHop": h3cDefaultRtNextHop,
       "h3cDefaultRtOutIf": h3cDefaultRtOutIf,
       "h3cRtTabTrap": h3cRtTabTrap,
       "h3cRtTabFullTrap": h3cRtTabFullTrap,
       "h3cDetailRtTabFullTrap": h3cDetailRtTabFullTrap,
       "h3cDefaultRtDelTrap": h3cDefaultRtDelTrap,
       "h3cDefaultRtDelTrapEnable": h3cDefaultRtDelTrapEnable,
       "h3cMulticastTabStatGroup": h3cMulticastTabStatGroup,
       "h3cMulticastTabTrapEnable": h3cMulticastTabTrapEnable,
       "h3cMulticastTabTrapInterval": h3cMulticastTabTrapInterval,
       "h3cMulticastTabTrapInfo": h3cMulticastTabTrapInfo,
       "h3cMulticastTabType": h3cMulticastTabType,
       "h3cMulticastTabLen": h3cMulticastTabLen,
       "h3cMulticastTabTrap": h3cMulticastTabTrap,
       "h3cMulticastTabFullTrap": h3cMulticastTabFullTrap,
       "h3cNdTabStatGroup": h3cNdTabStatGroup,
       "h3cNdTabTrapEnable": h3cNdTabTrapEnable,
       "h3cNdTabTrapInterval": h3cNdTabTrapInterval,
       "h3cNdTabTrapInfo": h3cNdTabTrapInfo,
       "h3cNdTabLen": h3cNdTabLen,
       "h3cNdTabTrap": h3cNdTabTrap,
       "h3cNdTabFullTrap": h3cNdTabFullTrap,
       "h3cPeriodicalTrapGroup": h3cPeriodicalTrapGroup,
       "h3cPeriodicalTrapObjects": h3cPeriodicalTrapObjects,
       "h3cPeriodicalTrapInterval": h3cPeriodicalTrapInterval,
       "h3cPeriodicalTrapSwitch": h3cPeriodicalTrapSwitch,
       "h3cPeriodicalTrapInfo": h3cPeriodicalTrapInfo,
       "h3cPeriodicalNotification": h3cPeriodicalNotification,
       "h3cPeriodicalNotificationPrefix": h3cPeriodicalNotificationPrefix,
       "h3cPeriodicalTrap": h3cPeriodicalTrap,
       "h3cTrapDesInfo": h3cTrapDesInfo,
       "h3cTrapDesInfoTable": h3cTrapDesInfoTable,
       "h3cTrapDesInfoEntry": h3cTrapDesInfoEntry,
       "h3cTrapDesInfoIndex": h3cTrapDesInfoIndex,
       "h3cTrapDesIPAddress": h3cTrapDesIPAddress,
       "h3cTrapDesPort": h3cTrapDesPort,
       "h3cTrapDesRowStatus": h3cTrapDesRowStatus,
       "h3cTrapDesAddrTAddress": h3cTrapDesAddrTAddress,
       "h3cTrapConfig": h3cTrapConfig,
       "h3cTrapConfigTable": h3cTrapConfigTable,
       "h3cTrapConfigEntry": h3cTrapConfigEntry,
       "h3cTrapConfigIndex": h3cTrapConfigIndex,
       "h3cTrapConfigName": h3cTrapConfigName,
       "h3cTrapConfigDescr": h3cTrapConfigDescr,
       "h3cTrapConfigSwitch": h3cTrapConfigSwitch}
)
