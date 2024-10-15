# SNMP MIB module (HH3C-EPON-UNI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-EPON-UNI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:53:10 2024
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

(hh3cEpon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cEpon")

(ifDescr,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifDescr",
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


# MODULE-IDENTITY

hh3cEponUni = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cEponUniSysMan_ObjectIdentity = ObjectIdentity
hh3cEponUniSysMan = _Hh3cEponUniSysMan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1)
)
_Hh3cEponUniSysManTable_Object = MibTable
hh3cEponUniSysManTable = _Hh3cEponUniSysManTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cEponUniSysManTable.setStatus("current")
_Hh3cEponUniSysManEntry_Object = MibTableRow
hh3cEponUniSysManEntry = _Hh3cEponUniSysManEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 1, 1)
)
hh3cEponUniSysManEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-EPON-UNI-MIB", "hh3cEponUniIndex"),
)
if mibBuilder.loadTexts:
    hh3cEponUniSysManEntry.setStatus("current")
_Hh3cEponUniIndex_Type = Integer32
_Hh3cEponUniIndex_Object = MibTableColumn
hh3cEponUniIndex = _Hh3cEponUniIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 1, 1, 1),
    _Hh3cEponUniIndex_Type()
)
hh3cEponUniIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cEponUniIndex.setStatus("current")
_Hh3cEponUniDescr_Type = OctetString
_Hh3cEponUniDescr_Object = MibTableColumn
hh3cEponUniDescr = _Hh3cEponUniDescr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 1, 1, 2),
    _Hh3cEponUniDescr_Type()
)
hh3cEponUniDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniDescr.setStatus("current")


class _Hh3cEponUniAdminStatus_Type(Integer32):
    """Custom type hh3cEponUniAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_Hh3cEponUniAdminStatus_Type.__name__ = "Integer32"
_Hh3cEponUniAdminStatus_Object = MibTableColumn
hh3cEponUniAdminStatus = _Hh3cEponUniAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 1, 1, 3),
    _Hh3cEponUniAdminStatus_Type()
)
hh3cEponUniAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponUniAdminStatus.setStatus("current")


class _Hh3cEponUniMdi_Type(Integer32):
    """Custom type hh3cEponUniMdi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mdi-auto", 3),
          ("mdi-ii", 1),
          ("mdi-x", 2))
    )


_Hh3cEponUniMdi_Type.__name__ = "Integer32"
_Hh3cEponUniMdi_Object = MibTableColumn
hh3cEponUniMdi = _Hh3cEponUniMdi_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 1, 1, 4),
    _Hh3cEponUniMdi_Type()
)
hh3cEponUniMdi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponUniMdi.setStatus("current")


class _Hh3cEponUniPriority_Type(Integer32):
    """Custom type hh3cEponUniPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Hh3cEponUniPriority_Type.__name__ = "Integer32"
_Hh3cEponUniPriority_Object = MibTableColumn
hh3cEponUniPriority = _Hh3cEponUniPriority_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 1, 1, 5),
    _Hh3cEponUniPriority_Type()
)
hh3cEponUniPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponUniPriority.setStatus("current")


class _Hh3cEponUniVlanType_Type(Integer32):
    """Custom type hh3cEponUniVlanType based on Integer32"""
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
        *(("access", 2),
          ("doubletagged", 6),
          ("hybrid", 3),
          ("tag", 7),
          ("translation", 8),
          ("transparent", 5),
          ("untagged", 4),
          ("vlantrunk", 1))
    )


_Hh3cEponUniVlanType_Type.__name__ = "Integer32"
_Hh3cEponUniVlanType_Object = MibTableColumn
hh3cEponUniVlanType = _Hh3cEponUniVlanType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 1, 1, 6),
    _Hh3cEponUniVlanType_Type()
)
hh3cEponUniVlanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponUniVlanType.setStatus("current")


class _Hh3cEponUniAccessVlan_Type(Integer32):
    """Custom type hh3cEponUniAccessVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Hh3cEponUniAccessVlan_Type.__name__ = "Integer32"
_Hh3cEponUniAccessVlan_Object = MibTableColumn
hh3cEponUniAccessVlan = _Hh3cEponUniAccessVlan_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 1, 1, 7),
    _Hh3cEponUniAccessVlan_Type()
)
hh3cEponUniAccessVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponUniAccessVlan.setStatus("current")


class _Hh3cEponUniTrunkPvid_Type(Integer32):
    """Custom type hh3cEponUniTrunkPvid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Hh3cEponUniTrunkPvid_Type.__name__ = "Integer32"
_Hh3cEponUniTrunkPvid_Object = MibTableColumn
hh3cEponUniTrunkPvid = _Hh3cEponUniTrunkPvid_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 1, 1, 8),
    _Hh3cEponUniTrunkPvid_Type()
)
hh3cEponUniTrunkPvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponUniTrunkPvid.setStatus("current")
_Hh3cEponUniVLANTrunkAllowListLow_Type = OctetString
_Hh3cEponUniVLANTrunkAllowListLow_Object = MibTableColumn
hh3cEponUniVLANTrunkAllowListLow = _Hh3cEponUniVLANTrunkAllowListLow_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 1, 1, 9),
    _Hh3cEponUniVLANTrunkAllowListLow_Type()
)
hh3cEponUniVLANTrunkAllowListLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponUniVLANTrunkAllowListLow.setStatus("current")
_Hh3cEponUniVLANTrunkAllowListHigh_Type = OctetString
_Hh3cEponUniVLANTrunkAllowListHigh_Object = MibTableColumn
hh3cEponUniVLANTrunkAllowListHigh = _Hh3cEponUniVLANTrunkAllowListHigh_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 1, 1, 10),
    _Hh3cEponUniVLANTrunkAllowListHigh_Type()
)
hh3cEponUniVLANTrunkAllowListHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponUniVLANTrunkAllowListHigh.setStatus("current")
_Hh3cEponUniInboundLineRate_Type = Integer32
_Hh3cEponUniInboundLineRate_Object = MibTableColumn
hh3cEponUniInboundLineRate = _Hh3cEponUniInboundLineRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 1, 1, 11),
    _Hh3cEponUniInboundLineRate_Type()
)
hh3cEponUniInboundLineRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponUniInboundLineRate.setStatus("current")
_Hh3cEponUniOutboundLineRate_Type = Integer32
_Hh3cEponUniOutboundLineRate_Object = MibTableColumn
hh3cEponUniOutboundLineRate = _Hh3cEponUniOutboundLineRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 1, 1, 12),
    _Hh3cEponUniOutboundLineRate_Type()
)
hh3cEponUniOutboundLineRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponUniOutboundLineRate.setStatus("current")
_Hh3cEponUniFlowControl_Type = TruthValue
_Hh3cEponUniFlowControl_Object = MibTableColumn
hh3cEponUniFlowControl = _Hh3cEponUniFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 1, 1, 13),
    _Hh3cEponUniFlowControl_Type()
)
hh3cEponUniFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponUniFlowControl.setStatus("current")


class _Hh3cEponUniSpeed_Type(Integer32):
    """Custom type hh3cEponUniSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              10,
              100,
              1000,
              10000,
              24000)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("s10000M", 10000),
          ("s1000M", 1000),
          ("s100M", 100),
          ("s10M", 10),
          ("s24000M", 24000))
    )


_Hh3cEponUniSpeed_Type.__name__ = "Integer32"
_Hh3cEponUniSpeed_Object = MibTableColumn
hh3cEponUniSpeed = _Hh3cEponUniSpeed_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 1, 1, 14),
    _Hh3cEponUniSpeed_Type()
)
hh3cEponUniSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponUniSpeed.setStatus("current")


class _Hh3cEponUniDuplex_Type(Integer32):
    """Custom type hh3cEponUniDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("full", 1),
          ("half", 2))
    )


_Hh3cEponUniDuplex_Type.__name__ = "Integer32"
_Hh3cEponUniDuplex_Object = MibTableColumn
hh3cEponUniDuplex = _Hh3cEponUniDuplex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 1, 1, 15),
    _Hh3cEponUniDuplex_Type()
)
hh3cEponUniDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponUniDuplex.setStatus("current")
_Hh3cEponUniVlanVPNStatus_Type = TruthValue
_Hh3cEponUniVlanVPNStatus_Object = MibTableColumn
hh3cEponUniVlanVPNStatus = _Hh3cEponUniVlanVPNStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 1, 1, 16),
    _Hh3cEponUniVlanVPNStatus_Type()
)
hh3cEponUniVlanVPNStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponUniVlanVPNStatus.setStatus("current")


class _Hh3cEponUniCountReset_Type(Integer32):
    """Custom type hh3cEponUniCountReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_Hh3cEponUniCountReset_Type.__name__ = "Integer32"
_Hh3cEponUniCountReset_Object = MibTableColumn
hh3cEponUniCountReset = _Hh3cEponUniCountReset_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 1, 1, 17),
    _Hh3cEponUniCountReset_Type()
)
hh3cEponUniCountReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponUniCountReset.setStatus("current")


class _Hh3cEponUniPortIsolate_Type(Integer32):
    """Custom type hh3cEponUniPortIsolate based on Integer32"""
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


_Hh3cEponUniPortIsolate_Type.__name__ = "Integer32"
_Hh3cEponUniPortIsolate_Object = MibTableColumn
hh3cEponUniPortIsolate = _Hh3cEponUniPortIsolate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 1, 1, 18),
    _Hh3cEponUniPortIsolate_Type()
)
hh3cEponUniPortIsolate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponUniPortIsolate.setStatus("current")


class _Hh3cEponUniVlanConfiguration_Type(OctetString):
    """Custom type hh3cEponUniVlanConfiguration based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cEponUniVlanConfiguration_Type.__name__ = "OctetString"
_Hh3cEponUniVlanConfiguration_Object = MibTableColumn
hh3cEponUniVlanConfiguration = _Hh3cEponUniVlanConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 1, 1, 23),
    _Hh3cEponUniVlanConfiguration_Type()
)
hh3cEponUniVlanConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponUniVlanConfiguration.setStatus("current")


class _Hh3cEponUniAutoNegotiation_Type(Integer32):
    """Custom type hh3cEponUniAutoNegotiation based on Integer32"""
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


_Hh3cEponUniAutoNegotiation_Type.__name__ = "Integer32"
_Hh3cEponUniAutoNegotiation_Object = MibTableColumn
hh3cEponUniAutoNegotiation = _Hh3cEponUniAutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 1, 1, 25),
    _Hh3cEponUniAutoNegotiation_Type()
)
hh3cEponUniAutoNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponUniAutoNegotiation.setStatus("current")


class _Hh3cEponUniRestartAutoNeg_Type(Integer32):
    """Custom type hh3cEponUniRestartAutoNeg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("autoNegotiation", 1)
    )


_Hh3cEponUniRestartAutoNeg_Type.__name__ = "Integer32"
_Hh3cEponUniRestartAutoNeg_Object = MibTableColumn
hh3cEponUniRestartAutoNeg = _Hh3cEponUniRestartAutoNeg_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 1, 1, 26),
    _Hh3cEponUniRestartAutoNeg_Type()
)
hh3cEponUniRestartAutoNeg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponUniRestartAutoNeg.setStatus("current")


class _Hh3cEponUniLinkStatus_Type(Integer32):
    """Custom type hh3cEponUniLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_Hh3cEponUniLinkStatus_Type.__name__ = "Integer32"
_Hh3cEponUniLinkStatus_Object = MibTableColumn
hh3cEponUniLinkStatus = _Hh3cEponUniLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 1, 1, 29),
    _Hh3cEponUniLinkStatus_Type()
)
hh3cEponUniLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniLinkStatus.setStatus("current")


class _Hh3cEponUniInterfaceType_Type(Integer32):
    """Custom type hh3cEponUniInterfaceType based on Integer32"""
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
        *(("e1port", 4),
          ("fastethernetport", 2),
          ("gigabitethernetport", 1),
          ("voipport", 3))
    )


_Hh3cEponUniInterfaceType_Type.__name__ = "Integer32"
_Hh3cEponUniInterfaceType_Object = MibTableColumn
hh3cEponUniInterfaceType = _Hh3cEponUniInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 1, 1, 30),
    _Hh3cEponUniInterfaceType_Type()
)
hh3cEponUniInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniInterfaceType.setStatus("current")


class _Hh3cEponUniVitualCableTest_Type(Integer32):
    """Custom type hh3cEponUniVitualCableTest based on Integer32"""
    defaultValue = 2

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


_Hh3cEponUniVitualCableTest_Type.__name__ = "Integer32"
_Hh3cEponUniVitualCableTest_Object = MibTableColumn
hh3cEponUniVitualCableTest = _Hh3cEponUniVitualCableTest_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 1, 1, 31),
    _Hh3cEponUniVitualCableTest_Type()
)
hh3cEponUniVitualCableTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponUniVitualCableTest.setStatus("current")


class _Hh3cEponUniVCTCableStatus_Type(Integer32):
    """Custom type hh3cEponUniVCTCableStatus based on Integer32"""
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
        *(("abnormal", 2),
          ("abnormalOpen", 3),
          ("abnormalShort", 4),
          ("failure", 5),
          ("normal", 1))
    )


_Hh3cEponUniVCTCableStatus_Type.__name__ = "Integer32"
_Hh3cEponUniVCTCableStatus_Object = MibTableColumn
hh3cEponUniVCTCableStatus = _Hh3cEponUniVCTCableStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 1, 1, 32),
    _Hh3cEponUniVCTCableStatus_Type()
)
hh3cEponUniVCTCableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniVCTCableStatus.setStatus("current")
_Hh3cEponUniVCTCableLength_Type = Integer32
_Hh3cEponUniVCTCableLength_Object = MibTableColumn
hh3cEponUniVCTCableLength = _Hh3cEponUniVCTCableLength_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 1, 1, 33),
    _Hh3cEponUniVCTCableLength_Type()
)
hh3cEponUniVCTCableLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniVCTCableLength.setStatus("current")


class _Hh3cEponUniVCTImpedanceMismatch_Type(Integer32):
    """Custom type hh3cEponUniVCTImpedanceMismatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 3),
          ("not-support", 1),
          ("true", 2))
    )


_Hh3cEponUniVCTImpedanceMismatch_Type.__name__ = "Integer32"
_Hh3cEponUniVCTImpedanceMismatch_Object = MibTableColumn
hh3cEponUniVCTImpedanceMismatch = _Hh3cEponUniVCTImpedanceMismatch_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 1, 1, 34),
    _Hh3cEponUniVCTImpedanceMismatch_Type()
)
hh3cEponUniVCTImpedanceMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniVCTImpedanceMismatch.setStatus("current")
_Hh3cEponUniVCTPairSkew_Type = Integer32
_Hh3cEponUniVCTPairSkew_Object = MibTableColumn
hh3cEponUniVCTPairSkew = _Hh3cEponUniVCTPairSkew_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 1, 1, 35),
    _Hh3cEponUniVCTPairSkew_Type()
)
hh3cEponUniVCTPairSkew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniVCTPairSkew.setStatus("current")


class _Hh3cEponUniVCTPairSwap_Type(Integer32):
    """Custom type hh3cEponUniVCTPairSwap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 3),
          ("notSupport", 1),
          ("true", 2))
    )


_Hh3cEponUniVCTPairSwap_Type.__name__ = "Integer32"
_Hh3cEponUniVCTPairSwap_Object = MibTableColumn
hh3cEponUniVCTPairSwap = _Hh3cEponUniVCTPairSwap_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 1, 1, 36),
    _Hh3cEponUniVCTPairSwap_Type()
)
hh3cEponUniVCTPairSwap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniVCTPairSwap.setStatus("current")


class _Hh3cEponUniVCTPolaritySwap_Type(Integer32):
    """Custom type hh3cEponUniVCTPolaritySwap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 3),
          ("notSupport", 1),
          ("true", 2))
    )


_Hh3cEponUniVCTPolaritySwap_Type.__name__ = "Integer32"
_Hh3cEponUniVCTPolaritySwap_Object = MibTableColumn
hh3cEponUniVCTPolaritySwap = _Hh3cEponUniVCTPolaritySwap_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 1, 1, 37),
    _Hh3cEponUniVCTPolaritySwap_Type()
)
hh3cEponUniVCTPolaritySwap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniVCTPolaritySwap.setStatus("current")
_Hh3cEponUniVCTInsertionLoss_Type = Integer32
_Hh3cEponUniVCTInsertionLoss_Object = MibTableColumn
hh3cEponUniVCTInsertionLoss = _Hh3cEponUniVCTInsertionLoss_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 1, 1, 38),
    _Hh3cEponUniVCTInsertionLoss_Type()
)
hh3cEponUniVCTInsertionLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniVCTInsertionLoss.setStatus("current")
_Hh3cEponUniVCTReturnLoss_Type = Integer32
_Hh3cEponUniVCTReturnLoss_Object = MibTableColumn
hh3cEponUniVCTReturnLoss = _Hh3cEponUniVCTReturnLoss_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 1, 1, 39),
    _Hh3cEponUniVCTReturnLoss_Type()
)
hh3cEponUniVCTReturnLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniVCTReturnLoss.setStatus("current")
_Hh3cEponUniVCTNearendCrosstalk_Type = Integer32
_Hh3cEponUniVCTNearendCrosstalk_Object = MibTableColumn
hh3cEponUniVCTNearendCrosstalk = _Hh3cEponUniVCTNearendCrosstalk_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 1, 1, 40),
    _Hh3cEponUniVCTNearendCrosstalk_Type()
)
hh3cEponUniVCTNearendCrosstalk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniVCTNearendCrosstalk.setStatus("current")
_Hh3cEponUniCountTable_Object = MibTable
hh3cEponUniCountTable = _Hh3cEponUniCountTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cEponUniCountTable.setStatus("current")
_Hh3cEponUniCountEntry_Object = MibTableRow
hh3cEponUniCountEntry = _Hh3cEponUniCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 2, 1)
)
hh3cEponUniCountEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-EPON-UNI-MIB", "hh3cEponUniIndex"),
)
if mibBuilder.loadTexts:
    hh3cEponUniCountEntry.setStatus("current")
_Hh3cEponUniInStatsPkts_Type = Unsigned32
_Hh3cEponUniInStatsPkts_Object = MibTableColumn
hh3cEponUniInStatsPkts = _Hh3cEponUniInStatsPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 2, 1, 1),
    _Hh3cEponUniInStatsPkts_Type()
)
hh3cEponUniInStatsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniInStatsPkts.setStatus("current")
_Hh3cEponUniInStatsUnicastPkts_Type = Unsigned32
_Hh3cEponUniInStatsUnicastPkts_Object = MibTableColumn
hh3cEponUniInStatsUnicastPkts = _Hh3cEponUniInStatsUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 2, 1, 2),
    _Hh3cEponUniInStatsUnicastPkts_Type()
)
hh3cEponUniInStatsUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniInStatsUnicastPkts.setStatus("current")
_Hh3cEponUniInStatsBroadcastPkts_Type = Unsigned32
_Hh3cEponUniInStatsBroadcastPkts_Object = MibTableColumn
hh3cEponUniInStatsBroadcastPkts = _Hh3cEponUniInStatsBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 2, 1, 3),
    _Hh3cEponUniInStatsBroadcastPkts_Type()
)
hh3cEponUniInStatsBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniInStatsBroadcastPkts.setStatus("current")
_Hh3cEponUniInStatsMulticastPkts_Type = Unsigned32
_Hh3cEponUniInStatsMulticastPkts_Object = MibTableColumn
hh3cEponUniInStatsMulticastPkts = _Hh3cEponUniInStatsMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 2, 1, 4),
    _Hh3cEponUniInStatsMulticastPkts_Type()
)
hh3cEponUniInStatsMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniInStatsMulticastPkts.setStatus("current")
_Hh3cEponUniInPausePkts_Type = Unsigned32
_Hh3cEponUniInPausePkts_Object = MibTableColumn
hh3cEponUniInPausePkts = _Hh3cEponUniInPausePkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 2, 1, 5),
    _Hh3cEponUniInPausePkts_Type()
)
hh3cEponUniInPausePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniInPausePkts.setStatus("current")
_Hh3cEponUniInTotalErrors_Type = Unsigned32
_Hh3cEponUniInTotalErrors_Object = MibTableColumn
hh3cEponUniInTotalErrors = _Hh3cEponUniInTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 2, 1, 6),
    _Hh3cEponUniInTotalErrors_Type()
)
hh3cEponUniInTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniInTotalErrors.setStatus("current")
_Hh3cEponUniInStatsCRCAlignErrors_Type = Unsigned32
_Hh3cEponUniInStatsCRCAlignErrors_Object = MibTableColumn
hh3cEponUniInStatsCRCAlignErrors = _Hh3cEponUniInStatsCRCAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 2, 1, 7),
    _Hh3cEponUniInStatsCRCAlignErrors_Type()
)
hh3cEponUniInStatsCRCAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniInStatsCRCAlignErrors.setStatus("current")
_Hh3cEponUniInStatsUndersizePkts_Type = Unsigned32
_Hh3cEponUniInStatsUndersizePkts_Object = MibTableColumn
hh3cEponUniInStatsUndersizePkts = _Hh3cEponUniInStatsUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 2, 1, 8),
    _Hh3cEponUniInStatsUndersizePkts_Type()
)
hh3cEponUniInStatsUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniInStatsUndersizePkts.setStatus("current")
_Hh3cEponUniInStatsOversizePkts_Type = Unsigned32
_Hh3cEponUniInStatsOversizePkts_Object = MibTableColumn
hh3cEponUniInStatsOversizePkts = _Hh3cEponUniInStatsOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 2, 1, 9),
    _Hh3cEponUniInStatsOversizePkts_Type()
)
hh3cEponUniInStatsOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniInStatsOversizePkts.setStatus("current")
_Hh3cEponUniInErrorbyOther_Type = Unsigned32
_Hh3cEponUniInErrorbyOther_Object = MibTableColumn
hh3cEponUniInErrorbyOther = _Hh3cEponUniInErrorbyOther_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 2, 1, 10),
    _Hh3cEponUniInErrorbyOther_Type()
)
hh3cEponUniInErrorbyOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniInErrorbyOther.setStatus("current")
_Hh3cEponUniOutStatsPkts_Type = Unsigned32
_Hh3cEponUniOutStatsPkts_Object = MibTableColumn
hh3cEponUniOutStatsPkts = _Hh3cEponUniOutStatsPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 2, 1, 11),
    _Hh3cEponUniOutStatsPkts_Type()
)
hh3cEponUniOutStatsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniOutStatsPkts.setStatus("current")
_Hh3cEponUniOutStatsUnicastPkts_Type = Unsigned32
_Hh3cEponUniOutStatsUnicastPkts_Object = MibTableColumn
hh3cEponUniOutStatsUnicastPkts = _Hh3cEponUniOutStatsUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 2, 1, 12),
    _Hh3cEponUniOutStatsUnicastPkts_Type()
)
hh3cEponUniOutStatsUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniOutStatsUnicastPkts.setStatus("current")
_Hh3cEponUniOutStatsBroadcastPkts_Type = Unsigned32
_Hh3cEponUniOutStatsBroadcastPkts_Object = MibTableColumn
hh3cEponUniOutStatsBroadcastPkts = _Hh3cEponUniOutStatsBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 2, 1, 13),
    _Hh3cEponUniOutStatsBroadcastPkts_Type()
)
hh3cEponUniOutStatsBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniOutStatsBroadcastPkts.setStatus("current")
_Hh3cEponUniOutStatsMulticastPkts_Type = Unsigned32
_Hh3cEponUniOutStatsMulticastPkts_Object = MibTableColumn
hh3cEponUniOutStatsMulticastPkts = _Hh3cEponUniOutStatsMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 2, 1, 14),
    _Hh3cEponUniOutStatsMulticastPkts_Type()
)
hh3cEponUniOutStatsMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniOutStatsMulticastPkts.setStatus("current")
_Hh3cEponUniOutStatsPausePkts_Type = Unsigned32
_Hh3cEponUniOutStatsPausePkts_Object = MibTableColumn
hh3cEponUniOutStatsPausePkts = _Hh3cEponUniOutStatsPausePkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 2, 1, 15),
    _Hh3cEponUniOutStatsPausePkts_Type()
)
hh3cEponUniOutStatsPausePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniOutStatsPausePkts.setStatus("current")
_Hh3cEponUniOutTotalErrors_Type = Unsigned32
_Hh3cEponUniOutTotalErrors_Object = MibTableColumn
hh3cEponUniOutTotalErrors = _Hh3cEponUniOutTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 2, 1, 16),
    _Hh3cEponUniOutTotalErrors_Type()
)
hh3cEponUniOutTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniOutTotalErrors.setStatus("current")
_Hh3cEponUniOutStatsCollisions_Type = Unsigned32
_Hh3cEponUniOutStatsCollisions_Object = MibTableColumn
hh3cEponUniOutStatsCollisions = _Hh3cEponUniOutStatsCollisions_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 2, 1, 17),
    _Hh3cEponUniOutStatsCollisions_Type()
)
hh3cEponUniOutStatsCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniOutStatsCollisions.setStatus("current")
_Hh3cEponUniOutDelayExceededDiscards_Type = Unsigned32
_Hh3cEponUniOutDelayExceededDiscards_Object = MibTableColumn
hh3cEponUniOutDelayExceededDiscards = _Hh3cEponUniOutDelayExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 2, 1, 18),
    _Hh3cEponUniOutDelayExceededDiscards_Type()
)
hh3cEponUniOutDelayExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniOutDelayExceededDiscards.setStatus("current")
_Hh3cEponUniOutErrorbyOther_Type = Unsigned32
_Hh3cEponUniOutErrorbyOther_Object = MibTableColumn
hh3cEponUniOutErrorbyOther = _Hh3cEponUniOutErrorbyOther_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 2, 1, 19),
    _Hh3cEponUniOutErrorbyOther_Type()
)
hh3cEponUniOutErrorbyOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniOutErrorbyOther.setStatus("current")
_Hh3cEponUniOutDroppedFrames_Type = Unsigned32
_Hh3cEponUniOutDroppedFrames_Object = MibTableColumn
hh3cEponUniOutDroppedFrames = _Hh3cEponUniOutDroppedFrames_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 2, 1, 20),
    _Hh3cEponUniOutDroppedFrames_Type()
)
hh3cEponUniOutDroppedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniOutDroppedFrames.setStatus("current")
_Hh3cEponUniIgmpInfoTable_Object = MibTable
hh3cEponUniIgmpInfoTable = _Hh3cEponUniIgmpInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cEponUniIgmpInfoTable.setStatus("current")
_Hh3cEponUniIgmpInfoEntry_Object = MibTableRow
hh3cEponUniIgmpInfoEntry = _Hh3cEponUniIgmpInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 3, 1)
)
hh3cEponUniIgmpInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-EPON-UNI-MIB", "hh3cEponUniIndex"),
    (0, "HH3C-EPON-UNI-MIB", "hh3cEponUniMacIndex"),
)
if mibBuilder.loadTexts:
    hh3cEponUniIgmpInfoEntry.setStatus("current")
_Hh3cEponUniMacIndex_Type = Integer32
_Hh3cEponUniMacIndex_Object = MibTableColumn
hh3cEponUniMacIndex = _Hh3cEponUniMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 3, 1, 1),
    _Hh3cEponUniMacIndex_Type()
)
hh3cEponUniMacIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cEponUniMacIndex.setStatus("current")
_Hh3cEponUniIgmpMacAddress_Type = MacAddress
_Hh3cEponUniIgmpMacAddress_Object = MibTableColumn
hh3cEponUniIgmpMacAddress = _Hh3cEponUniIgmpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 3, 1, 2),
    _Hh3cEponUniIgmpMacAddress_Type()
)
hh3cEponUniIgmpMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniIgmpMacAddress.setStatus("current")


class _Hh3cEponUniIgmpVlanId_Type(Integer32):
    """Custom type hh3cEponUniIgmpVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Hh3cEponUniIgmpVlanId_Type.__name__ = "Integer32"
_Hh3cEponUniIgmpVlanId_Object = MibTableColumn
hh3cEponUniIgmpVlanId = _Hh3cEponUniIgmpVlanId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 3, 1, 3),
    _Hh3cEponUniIgmpVlanId_Type()
)
hh3cEponUniIgmpVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniIgmpVlanId.setStatus("current")
_Hh3cEponUniParaMan_ObjectIdentity = ObjectIdentity
hh3cEponUniParaMan = _Hh3cEponUniParaMan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 4)
)
_Hh3cEponUniLineRateMax_Type = Integer32
_Hh3cEponUniLineRateMax_Object = MibScalar
hh3cEponUniLineRateMax = _Hh3cEponUniLineRateMax_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 4, 1),
    _Hh3cEponUniLineRateMax_Type()
)
hh3cEponUniLineRateMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniLineRateMax.setStatus("current")
_Hh3cEponUniLineRateStep_Type = Integer32
_Hh3cEponUniLineRateStep_Object = MibScalar
hh3cEponUniLineRateStep = _Hh3cEponUniLineRateStep_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 4, 2),
    _Hh3cEponUniLineRateStep_Type()
)
hh3cEponUniLineRateStep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniLineRateStep.setStatus("current")
_Hh3cEponUniNumberOnOnu_Type = Integer32
_Hh3cEponUniNumberOnOnu_Object = MibScalar
hh3cEponUniNumberOnOnu = _Hh3cEponUniNumberOnOnu_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 4, 3),
    _Hh3cEponUniNumberOnOnu_Type()
)
hh3cEponUniNumberOnOnu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniNumberOnOnu.setStatus("current")
_Hh3cEponUniScalarGroup_ObjectIdentity = ObjectIdentity
hh3cEponUniScalarGroup = _Hh3cEponUniScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 5)
)
_Hh3cEponUniPortPolicyTable_Object = MibTable
hh3cEponUniPortPolicyTable = _Hh3cEponUniPortPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 6)
)
if mibBuilder.loadTexts:
    hh3cEponUniPortPolicyTable.setStatus("current")
_Hh3cEponUniPortPolicyEntry_Object = MibTableRow
hh3cEponUniPortPolicyEntry = _Hh3cEponUniPortPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 6, 1)
)
hh3cEponUniPortPolicyEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-EPON-UNI-MIB", "hh3cEponUniIndex"),
)
if mibBuilder.loadTexts:
    hh3cEponUniPortPolicyEntry.setStatus("current")


class _Hh3cEponUniPortPolicyStatus_Type(Integer32):
    """Custom type hh3cEponUniPortPolicyStatus based on Integer32"""
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


_Hh3cEponUniPortPolicyStatus_Type.__name__ = "Integer32"
_Hh3cEponUniPortPolicyStatus_Object = MibTableColumn
hh3cEponUniPortPolicyStatus = _Hh3cEponUniPortPolicyStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 6, 1, 1),
    _Hh3cEponUniPortPolicyStatus_Type()
)
hh3cEponUniPortPolicyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponUniPortPolicyStatus.setStatus("current")


class _Hh3cEponUniPortPolicyCir_Type(Integer32):
    """Custom type hh3cEponUniPortPolicyCir based on Integer32"""
    defaultValue = 102400


_Hh3cEponUniPortPolicyCir_Object = MibTableColumn
hh3cEponUniPortPolicyCir = _Hh3cEponUniPortPolicyCir_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 6, 1, 2),
    _Hh3cEponUniPortPolicyCir_Type()
)
hh3cEponUniPortPolicyCir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponUniPortPolicyCir.setStatus("current")


class _Hh3cEponUniPortPolicyBucketDepth_Type(Integer32):
    """Custom type hh3cEponUniPortPolicyBucketDepth based on Integer32"""
    defaultValue = 0


_Hh3cEponUniPortPolicyBucketDepth_Object = MibTableColumn
hh3cEponUniPortPolicyBucketDepth = _Hh3cEponUniPortPolicyBucketDepth_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 6, 1, 3),
    _Hh3cEponUniPortPolicyBucketDepth_Type()
)
hh3cEponUniPortPolicyBucketDepth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponUniPortPolicyBucketDepth.setStatus("current")


class _Hh3cEponUniPortPolicyExtraBurst_Type(Integer32):
    """Custom type hh3cEponUniPortPolicyExtraBurst based on Integer32"""
    defaultValue = 0


_Hh3cEponUniPortPolicyExtraBurst_Object = MibTableColumn
hh3cEponUniPortPolicyExtraBurst = _Hh3cEponUniPortPolicyExtraBurst_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 6, 1, 4),
    _Hh3cEponUniPortPolicyExtraBurst_Type()
)
hh3cEponUniPortPolicyExtraBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponUniPortPolicyExtraBurst.setStatus("current")
_Hh3cEponUniPortPolicyInboundCir_Type = Integer32
_Hh3cEponUniPortPolicyInboundCir_Object = MibTableColumn
hh3cEponUniPortPolicyInboundCir = _Hh3cEponUniPortPolicyInboundCir_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 6, 1, 5),
    _Hh3cEponUniPortPolicyInboundCir_Type()
)
hh3cEponUniPortPolicyInboundCir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponUniPortPolicyInboundCir.setStatus("current")


class _Hh3cEponUniPortPolicyInboundBucketDepth_Type(Integer32):
    """Custom type hh3cEponUniPortPolicyInboundBucketDepth based on Integer32"""
    defaultValue = 0


_Hh3cEponUniPortPolicyInboundBucketDepth_Object = MibTableColumn
hh3cEponUniPortPolicyInboundBucketDepth = _Hh3cEponUniPortPolicyInboundBucketDepth_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 6, 1, 6),
    _Hh3cEponUniPortPolicyInboundBucketDepth_Type()
)
hh3cEponUniPortPolicyInboundBucketDepth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponUniPortPolicyInboundBucketDepth.setStatus("current")


class _Hh3cEponUniPortPolicyInboundExtraBurst_Type(Integer32):
    """Custom type hh3cEponUniPortPolicyInboundExtraBurst based on Integer32"""
    defaultValue = 0


_Hh3cEponUniPortPolicyInboundExtraBurst_Object = MibTableColumn
hh3cEponUniPortPolicyInboundExtraBurst = _Hh3cEponUniPortPolicyInboundExtraBurst_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 6, 1, 7),
    _Hh3cEponUniPortPolicyInboundExtraBurst_Type()
)
hh3cEponUniPortPolicyInboundExtraBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponUniPortPolicyInboundExtraBurst.setStatus("current")
_Hh3cEponUniPortPolicyOutboundCir_Type = Integer32
_Hh3cEponUniPortPolicyOutboundCir_Object = MibTableColumn
hh3cEponUniPortPolicyOutboundCir = _Hh3cEponUniPortPolicyOutboundCir_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 6, 1, 8),
    _Hh3cEponUniPortPolicyOutboundCir_Type()
)
hh3cEponUniPortPolicyOutboundCir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponUniPortPolicyOutboundCir.setStatus("current")
_Hh3cEponUniPortPolicyOutboundPir_Type = Integer32
_Hh3cEponUniPortPolicyOutboundPir_Object = MibTableColumn
hh3cEponUniPortPolicyOutboundPir = _Hh3cEponUniPortPolicyOutboundPir_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 6, 1, 9),
    _Hh3cEponUniPortPolicyOutboundPir_Type()
)
hh3cEponUniPortPolicyOutboundPir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponUniPortPolicyOutboundPir.setStatus("current")
_Hh3cEponUniMulticastTable_Object = MibTable
hh3cEponUniMulticastTable = _Hh3cEponUniMulticastTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 7)
)
if mibBuilder.loadTexts:
    hh3cEponUniMulticastTable.setStatus("current")
_Hh3cEponUniMulticastEntry_Object = MibTableRow
hh3cEponUniMulticastEntry = _Hh3cEponUniMulticastEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 7, 1)
)
hh3cEponUniMulticastEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-EPON-UNI-MIB", "hh3cEponUniIndex"),
)
if mibBuilder.loadTexts:
    hh3cEponUniMulticastEntry.setStatus("current")


class _Hh3cEponUniMulticastGroupNumber_Type(Integer32):
    """Custom type hh3cEponUniMulticastGroupNumber based on Integer32"""
    defaultValue = 64


_Hh3cEponUniMulticastGroupNumber_Object = MibTableColumn
hh3cEponUniMulticastGroupNumber = _Hh3cEponUniMulticastGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 7, 1, 1),
    _Hh3cEponUniMulticastGroupNumber_Type()
)
hh3cEponUniMulticastGroupNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponUniMulticastGroupNumber.setStatus("current")


class _Hh3cEponUniMulticastVlanList_Type(OctetString):
    """Custom type hh3cEponUniMulticastVlanList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cEponUniMulticastVlanList_Type.__name__ = "OctetString"
_Hh3cEponUniMulticastVlanList_Object = MibTableColumn
hh3cEponUniMulticastVlanList = _Hh3cEponUniMulticastVlanList_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 7, 1, 2),
    _Hh3cEponUniMulticastVlanList_Type()
)
hh3cEponUniMulticastVlanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponUniMulticastVlanList.setStatus("current")


class _Hh3cEponUniMulticastStripStatus_Type(Integer32):
    """Custom type hh3cEponUniMulticastStripStatus based on Integer32"""
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


_Hh3cEponUniMulticastStripStatus_Type.__name__ = "Integer32"
_Hh3cEponUniMulticastStripStatus_Object = MibTableColumn
hh3cEponUniMulticastStripStatus = _Hh3cEponUniMulticastStripStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 7, 1, 3),
    _Hh3cEponUniMulticastStripStatus_Type()
)
hh3cEponUniMulticastStripStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponUniMulticastStripStatus.setStatus("current")


class _Hh3cEponUniMulticastFastleave_Type(TruthValue):
    """Custom type hh3cEponUniMulticastFastleave based on TruthValue"""


_Hh3cEponUniMulticastFastleave_Object = MibTableColumn
hh3cEponUniMulticastFastleave = _Hh3cEponUniMulticastFastleave_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 7, 1, 4),
    _Hh3cEponUniMulticastFastleave_Type()
)
hh3cEponUniMulticastFastleave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponUniMulticastFastleave.setStatus("current")
_Hh3cEponUniTechAbilityTable_Object = MibTable
hh3cEponUniTechAbilityTable = _Hh3cEponUniTechAbilityTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 8)
)
if mibBuilder.loadTexts:
    hh3cEponUniTechAbilityTable.setStatus("current")
_Hh3cEponUniTechAbilityEntry_Object = MibTableRow
hh3cEponUniTechAbilityEntry = _Hh3cEponUniTechAbilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 8, 1)
)
hh3cEponUniTechAbilityEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-EPON-UNI-MIB", "hh3cEponUniIndex"),
)
if mibBuilder.loadTexts:
    hh3cEponUniTechAbilityEntry.setStatus("current")


class _Hh3cEponUniLocalTechAbility_Type(OctetString):
    """Custom type hh3cEponUniLocalTechAbility based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cEponUniLocalTechAbility_Type.__name__ = "OctetString"
_Hh3cEponUniLocalTechAbility_Object = MibTableColumn
hh3cEponUniLocalTechAbility = _Hh3cEponUniLocalTechAbility_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 8, 1, 1),
    _Hh3cEponUniLocalTechAbility_Type()
)
hh3cEponUniLocalTechAbility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniLocalTechAbility.setStatus("current")


class _Hh3cEponUniAdvertisedTechAbility_Type(OctetString):
    """Custom type hh3cEponUniAdvertisedTechAbility based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cEponUniAdvertisedTechAbility_Type.__name__ = "OctetString"
_Hh3cEponUniAdvertisedTechAbility_Object = MibTableColumn
hh3cEponUniAdvertisedTechAbility = _Hh3cEponUniAdvertisedTechAbility_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 8, 1, 2),
    _Hh3cEponUniAdvertisedTechAbility_Type()
)
hh3cEponUniAdvertisedTechAbility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniAdvertisedTechAbility.setStatus("current")
_Hh3cEponUniMulticastControlTable_Object = MibTable
hh3cEponUniMulticastControlTable = _Hh3cEponUniMulticastControlTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 9)
)
if mibBuilder.loadTexts:
    hh3cEponUniMulticastControlTable.setStatus("current")
_Hh3cEponUniMulticastControlEntry_Object = MibTableRow
hh3cEponUniMulticastControlEntry = _Hh3cEponUniMulticastControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 9, 1)
)
hh3cEponUniMulticastControlEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-EPON-UNI-MIB", "hh3cEponUniIndex"),
    (0, "HH3C-EPON-UNI-MIB", "hh3cEponUniMulticastIndex"),
)
if mibBuilder.loadTexts:
    hh3cEponUniMulticastControlEntry.setStatus("current")
_Hh3cEponUniMulticastVlanIndex_Type = Integer32
_Hh3cEponUniMulticastVlanIndex_Object = MibTableColumn
hh3cEponUniMulticastVlanIndex = _Hh3cEponUniMulticastVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 9, 1, 1),
    _Hh3cEponUniMulticastVlanIndex_Type()
)
hh3cEponUniMulticastVlanIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEponUniMulticastVlanIndex.setStatus("current")


class _Hh3cEponUniMulticastAddressList_Type(OctetString):
    """Custom type hh3cEponUniMulticastAddressList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cEponUniMulticastAddressList_Type.__name__ = "OctetString"
_Hh3cEponUniMulticastAddressList_Object = MibTableColumn
hh3cEponUniMulticastAddressList = _Hh3cEponUniMulticastAddressList_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 9, 1, 2),
    _Hh3cEponUniMulticastAddressList_Type()
)
hh3cEponUniMulticastAddressList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEponUniMulticastAddressList.setStatus("current")


class _Hh3cEponUniMulticastAccessRule_Type(Integer32):
    """Custom type hh3cEponUniMulticastAccessRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 2),
          ("preview", 3))
    )


_Hh3cEponUniMulticastAccessRule_Type.__name__ = "Integer32"
_Hh3cEponUniMulticastAccessRule_Object = MibTableColumn
hh3cEponUniMulticastAccessRule = _Hh3cEponUniMulticastAccessRule_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 9, 1, 3),
    _Hh3cEponUniMulticastAccessRule_Type()
)
hh3cEponUniMulticastAccessRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEponUniMulticastAccessRule.setStatus("current")
_Hh3cEponUniMulticastChannelLimit_Type = Integer32
_Hh3cEponUniMulticastChannelLimit_Object = MibTableColumn
hh3cEponUniMulticastChannelLimit = _Hh3cEponUniMulticastChannelLimit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 9, 1, 4),
    _Hh3cEponUniMulticastChannelLimit_Type()
)
hh3cEponUniMulticastChannelLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEponUniMulticastChannelLimit.setStatus("current")
_Hh3cEponUniMulticastPreTimeSlice_Type = Integer32
_Hh3cEponUniMulticastPreTimeSlice_Object = MibTableColumn
hh3cEponUniMulticastPreTimeSlice = _Hh3cEponUniMulticastPreTimeSlice_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 9, 1, 5),
    _Hh3cEponUniMulticastPreTimeSlice_Type()
)
hh3cEponUniMulticastPreTimeSlice.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEponUniMulticastPreTimeSlice.setStatus("current")
_Hh3cEponUniMulticastPreTimes_Type = Integer32
_Hh3cEponUniMulticastPreTimes_Object = MibTableColumn
hh3cEponUniMulticastPreTimes = _Hh3cEponUniMulticastPreTimes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 9, 1, 6),
    _Hh3cEponUniMulticastPreTimes_Type()
)
hh3cEponUniMulticastPreTimes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEponUniMulticastPreTimes.setStatus("current")
_Hh3cEponUniMulticastPreInterval_Type = Integer32
_Hh3cEponUniMulticastPreInterval_Object = MibTableColumn
hh3cEponUniMulticastPreInterval = _Hh3cEponUniMulticastPreInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 9, 1, 7),
    _Hh3cEponUniMulticastPreInterval_Type()
)
hh3cEponUniMulticastPreInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEponUniMulticastPreInterval.setStatus("current")
_Hh3cEponUniMulticastRowStatus_Type = RowStatus
_Hh3cEponUniMulticastRowStatus_Object = MibTableColumn
hh3cEponUniMulticastRowStatus = _Hh3cEponUniMulticastRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 9, 1, 8),
    _Hh3cEponUniMulticastRowStatus_Type()
)
hh3cEponUniMulticastRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEponUniMulticastRowStatus.setStatus("current")
_Hh3cEponUniMulticastIndex_Type = Integer32
_Hh3cEponUniMulticastIndex_Object = MibTableColumn
hh3cEponUniMulticastIndex = _Hh3cEponUniMulticastIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 9, 1, 9),
    _Hh3cEponUniMulticastIndex_Type()
)
hh3cEponUniMulticastIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cEponUniMulticastIndex.setStatus("current")


class _Hh3cEponUniMulticastSourceIpList_Type(OctetString):
    """Custom type hh3cEponUniMulticastSourceIpList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hh3cEponUniMulticastSourceIpList_Type.__name__ = "OctetString"
_Hh3cEponUniMulticastSourceIpList_Object = MibTableColumn
hh3cEponUniMulticastSourceIpList = _Hh3cEponUniMulticastSourceIpList_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 9, 1, 10),
    _Hh3cEponUniMulticastSourceIpList_Type()
)
hh3cEponUniMulticastSourceIpList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEponUniMulticastSourceIpList.setStatus("current")
_Hh3cEponUniMulticastResetInterval_Type = Integer32
_Hh3cEponUniMulticastResetInterval_Object = MibTableColumn
hh3cEponUniMulticastResetInterval = _Hh3cEponUniMulticastResetInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 9, 1, 11),
    _Hh3cEponUniMulticastResetInterval_Type()
)
hh3cEponUniMulticastResetInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEponUniMulticastResetInterval.setStatus("current")
_Hh3cEponUniQosIndexNextTable_Object = MibTable
hh3cEponUniQosIndexNextTable = _Hh3cEponUniQosIndexNextTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 10)
)
if mibBuilder.loadTexts:
    hh3cEponUniQosIndexNextTable.setStatus("current")
_Hh3cEponUniQosIndexNextEntry_Object = MibTableRow
hh3cEponUniQosIndexNextEntry = _Hh3cEponUniQosIndexNextEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 10, 1)
)
hh3cEponUniQosIndexNextEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-EPON-UNI-MIB", "hh3cEponUniIndex"),
)
if mibBuilder.loadTexts:
    hh3cEponUniQosIndexNextEntry.setStatus("current")
_Hh3cEponUniQosConfIndexNext_Type = Integer32
_Hh3cEponUniQosConfIndexNext_Object = MibTableColumn
hh3cEponUniQosConfIndexNext = _Hh3cEponUniQosConfIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 10, 1, 1),
    _Hh3cEponUniQosConfIndexNext_Type()
)
hh3cEponUniQosConfIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniQosConfIndexNext.setStatus("current")
_Hh3cEponUniQosConfTable_Object = MibTable
hh3cEponUniQosConfTable = _Hh3cEponUniQosConfTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 11)
)
if mibBuilder.loadTexts:
    hh3cEponUniQosConfTable.setStatus("current")
_Hh3cEponUniQosConfEntry_Object = MibTableRow
hh3cEponUniQosConfEntry = _Hh3cEponUniQosConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 11, 1)
)
hh3cEponUniQosConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-EPON-UNI-MIB", "hh3cEponUniIndex"),
    (0, "HH3C-EPON-UNI-MIB", "hh3cEponUniQosConfIndex"),
)
if mibBuilder.loadTexts:
    hh3cEponUniQosConfEntry.setStatus("current")
_Hh3cEponUniQosConfIndex_Type = Integer32
_Hh3cEponUniQosConfIndex_Object = MibTableColumn
hh3cEponUniQosConfIndex = _Hh3cEponUniQosConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 11, 1, 1),
    _Hh3cEponUniQosConfIndex_Type()
)
hh3cEponUniQosConfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cEponUniQosConfIndex.setStatus("current")
_Hh3cEponUniQosConfRuleIndexNext_Type = Integer32
_Hh3cEponUniQosConfRuleIndexNext_Object = MibTableColumn
hh3cEponUniQosConfRuleIndexNext = _Hh3cEponUniQosConfRuleIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 11, 1, 2),
    _Hh3cEponUniQosConfRuleIndexNext_Type()
)
hh3cEponUniQosConfRuleIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniQosConfRuleIndexNext.setStatus("current")
_Hh3cEponUniQosConfMappedQueue_Type = Integer32
_Hh3cEponUniQosConfMappedQueue_Object = MibTableColumn
hh3cEponUniQosConfMappedQueue = _Hh3cEponUniQosConfMappedQueue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 11, 1, 3),
    _Hh3cEponUniQosConfMappedQueue_Type()
)
hh3cEponUniQosConfMappedQueue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEponUniQosConfMappedQueue.setStatus("current")
_Hh3cEponUniQosConfMarkedPriority_Type = Integer32
_Hh3cEponUniQosConfMarkedPriority_Object = MibTableColumn
hh3cEponUniQosConfMarkedPriority = _Hh3cEponUniQosConfMarkedPriority_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 11, 1, 4),
    _Hh3cEponUniQosConfMarkedPriority_Type()
)
hh3cEponUniQosConfMarkedPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEponUniQosConfMarkedPriority.setStatus("current")
_Hh3cEponUniQosConfRowStatus_Type = RowStatus
_Hh3cEponUniQosConfRowStatus_Object = MibTableColumn
hh3cEponUniQosConfRowStatus = _Hh3cEponUniQosConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 11, 1, 5),
    _Hh3cEponUniQosConfRowStatus_Type()
)
hh3cEponUniQosConfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEponUniQosConfRowStatus.setStatus("current")
_Hh3cEponUniQosRuleTable_Object = MibTable
hh3cEponUniQosRuleTable = _Hh3cEponUniQosRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 12)
)
if mibBuilder.loadTexts:
    hh3cEponUniQosRuleTable.setStatus("current")
_Hh3cEponUniQosRuleEntry_Object = MibTableRow
hh3cEponUniQosRuleEntry = _Hh3cEponUniQosRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 12, 1)
)
hh3cEponUniQosRuleEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-EPON-UNI-MIB", "hh3cEponUniIndex"),
    (0, "HH3C-EPON-UNI-MIB", "hh3cEponUniQosConfIndex"),
    (0, "HH3C-EPON-UNI-MIB", "hh3cEponUniQosRuleIndex"),
)
if mibBuilder.loadTexts:
    hh3cEponUniQosRuleEntry.setStatus("current")


class _Hh3cEponUniQosRuleIndex_Type(Integer32):
    """Custom type hh3cEponUniQosRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Hh3cEponUniQosRuleIndex_Type.__name__ = "Integer32"
_Hh3cEponUniQosRuleIndex_Object = MibTableColumn
hh3cEponUniQosRuleIndex = _Hh3cEponUniQosRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 12, 1, 1),
    _Hh3cEponUniQosRuleIndex_Type()
)
hh3cEponUniQosRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cEponUniQosRuleIndex.setStatus("current")


class _Hh3cEponUniQosRuleSelector_Type(Integer32):
    """Custom type hh3cEponUniQosRuleSelector based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("dstip", 6),
          ("dstmac", 1),
          ("dstport", 12),
          ("ethernetpriority", 3),
          ("ethernettype", 5),
          ("ipprototype", 8),
          ("ipv4tosdscp", 9),
          ("ipv6precedence", 10),
          ("srcip", 7),
          ("srcmac", 2),
          ("srcport", 11),
          ("vlanid", 4))
    )


_Hh3cEponUniQosRuleSelector_Type.__name__ = "Integer32"
_Hh3cEponUniQosRuleSelector_Object = MibTableColumn
hh3cEponUniQosRuleSelector = _Hh3cEponUniQosRuleSelector_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 12, 1, 2),
    _Hh3cEponUniQosRuleSelector_Type()
)
hh3cEponUniQosRuleSelector.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEponUniQosRuleSelector.setStatus("current")
_Hh3cEponUniQosRuleValue_Type = Integer32
_Hh3cEponUniQosRuleValue_Object = MibTableColumn
hh3cEponUniQosRuleValue = _Hh3cEponUniQosRuleValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 12, 1, 3),
    _Hh3cEponUniQosRuleValue_Type()
)
hh3cEponUniQosRuleValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEponUniQosRuleValue.setStatus("current")
_Hh3cEponUniQosRuleMacAddress_Type = MacAddress
_Hh3cEponUniQosRuleMacAddress_Object = MibTableColumn
hh3cEponUniQosRuleMacAddress = _Hh3cEponUniQosRuleMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 12, 1, 4),
    _Hh3cEponUniQosRuleMacAddress_Type()
)
hh3cEponUniQosRuleMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEponUniQosRuleMacAddress.setStatus("current")


class _Hh3cEponUniQosRuleOperator_Type(Integer32):
    """Custom type hh3cEponUniQosRuleOperator based on Integer32"""
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
        *(("alwaysmatch", 8),
          ("equal", 2),
          ("fieldexist", 6),
          ("fieldnotexist", 7),
          ("greaterthanequal", 5),
          ("lessthanequal", 4),
          ("nevermatch", 1),
          ("notequal", 3))
    )


_Hh3cEponUniQosRuleOperator_Type.__name__ = "Integer32"
_Hh3cEponUniQosRuleOperator_Object = MibTableColumn
hh3cEponUniQosRuleOperator = _Hh3cEponUniQosRuleOperator_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 12, 1, 5),
    _Hh3cEponUniQosRuleOperator_Type()
)
hh3cEponUniQosRuleOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEponUniQosRuleOperator.setStatus("current")
_Hh3cEponUniQosRuleRowStatus_Type = RowStatus
_Hh3cEponUniQosRuleRowStatus_Object = MibTableColumn
hh3cEponUniQosRuleRowStatus = _Hh3cEponUniQosRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 12, 1, 6),
    _Hh3cEponUniQosRuleRowStatus_Type()
)
hh3cEponUniQosRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEponUniQosRuleRowStatus.setStatus("current")
_Hh3cEponUniMirrorGroupTable_Object = MibTable
hh3cEponUniMirrorGroupTable = _Hh3cEponUniMirrorGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 13)
)
if mibBuilder.loadTexts:
    hh3cEponUniMirrorGroupTable.setStatus("current")
_Hh3cEponUniMirrorGroupEntry_Object = MibTableRow
hh3cEponUniMirrorGroupEntry = _Hh3cEponUniMirrorGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 13, 1)
)
hh3cEponUniMirrorGroupEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-EPON-UNI-MIB", "hh3cEponUniMirrorGroupID"),
)
if mibBuilder.loadTexts:
    hh3cEponUniMirrorGroupEntry.setStatus("current")
_Hh3cEponUniMirrorGroupID_Type = Integer32
_Hh3cEponUniMirrorGroupID_Object = MibTableColumn
hh3cEponUniMirrorGroupID = _Hh3cEponUniMirrorGroupID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 13, 1, 1),
    _Hh3cEponUniMirrorGroupID_Type()
)
hh3cEponUniMirrorGroupID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cEponUniMirrorGroupID.setStatus("current")
_Hh3cEponUniMirrorInboundPortList_Type = OctetString
_Hh3cEponUniMirrorInboundPortList_Object = MibTableColumn
hh3cEponUniMirrorInboundPortList = _Hh3cEponUniMirrorInboundPortList_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 13, 1, 2),
    _Hh3cEponUniMirrorInboundPortList_Type()
)
hh3cEponUniMirrorInboundPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEponUniMirrorInboundPortList.setStatus("current")
_Hh3cEponUniMirrorOutboundPortList_Type = OctetString
_Hh3cEponUniMirrorOutboundPortList_Object = MibTableColumn
hh3cEponUniMirrorOutboundPortList = _Hh3cEponUniMirrorOutboundPortList_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 13, 1, 3),
    _Hh3cEponUniMirrorOutboundPortList_Type()
)
hh3cEponUniMirrorOutboundPortList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEponUniMirrorOutboundPortList.setStatus("current")
_Hh3cEponUniMonitorPort_Type = Integer32
_Hh3cEponUniMonitorPort_Object = MibTableColumn
hh3cEponUniMonitorPort = _Hh3cEponUniMonitorPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 13, 1, 4),
    _Hh3cEponUniMonitorPort_Type()
)
hh3cEponUniMonitorPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEponUniMonitorPort.setStatus("current")
_Hh3cEponUniMirrorRowStatus_Type = RowStatus
_Hh3cEponUniMirrorRowStatus_Object = MibTableColumn
hh3cEponUniMirrorRowStatus = _Hh3cEponUniMirrorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 13, 1, 5),
    _Hh3cEponUniMirrorRowStatus_Type()
)
hh3cEponUniMirrorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEponUniMirrorRowStatus.setStatus("current")
_Hh3cEponUniMirrorGroupIdNextTable_Object = MibTable
hh3cEponUniMirrorGroupIdNextTable = _Hh3cEponUniMirrorGroupIdNextTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 14)
)
if mibBuilder.loadTexts:
    hh3cEponUniMirrorGroupIdNextTable.setStatus("current")
_Hh3cEponUniMirrorGroupIdNextEntry_Object = MibTableRow
hh3cEponUniMirrorGroupIdNextEntry = _Hh3cEponUniMirrorGroupIdNextEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 14, 1)
)
hh3cEponUniMirrorGroupIdNextEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cEponUniMirrorGroupIdNextEntry.setStatus("current")
_Hh3cEponUniMirrorGroupIDNext_Type = Integer32
_Hh3cEponUniMirrorGroupIDNext_Object = MibTableColumn
hh3cEponUniMirrorGroupIDNext = _Hh3cEponUniMirrorGroupIDNext_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 14, 1, 1),
    _Hh3cEponUniMirrorGroupIDNext_Type()
)
hh3cEponUniMirrorGroupIDNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniMirrorGroupIDNext.setStatus("current")
_Hh3cEponUniMulticastCtrlInfoTable_Object = MibTable
hh3cEponUniMulticastCtrlInfoTable = _Hh3cEponUniMulticastCtrlInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 15)
)
if mibBuilder.loadTexts:
    hh3cEponUniMulticastCtrlInfoTable.setStatus("current")
_Hh3cEponUniMulticastCtrlInfoEntry_Object = MibTableRow
hh3cEponUniMulticastCtrlInfoEntry = _Hh3cEponUniMulticastCtrlInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 15, 1)
)
hh3cEponUniMulticastCtrlInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-EPON-UNI-MIB", "hh3cEponUniIndex"),
    (0, "HH3C-EPON-UNI-MIB", "hh3cEponUniMultActVlan"),
    (0, "HH3C-EPON-UNI-MIB", "hh3cEponUniMultActAddress"),
)
if mibBuilder.loadTexts:
    hh3cEponUniMulticastCtrlInfoEntry.setStatus("current")
_Hh3cEponUniMultActVlan_Type = Integer32
_Hh3cEponUniMultActVlan_Object = MibTableColumn
hh3cEponUniMultActVlan = _Hh3cEponUniMultActVlan_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 15, 1, 1),
    _Hh3cEponUniMultActVlan_Type()
)
hh3cEponUniMultActVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cEponUniMultActVlan.setStatus("current")
_Hh3cEponUniMultActAddress_Type = IpAddress
_Hh3cEponUniMultActAddress_Object = MibTableColumn
hh3cEponUniMultActAddress = _Hh3cEponUniMultActAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 15, 1, 2),
    _Hh3cEponUniMultActAddress_Type()
)
hh3cEponUniMultActAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cEponUniMultActAddress.setStatus("current")


class _Hh3cEponUniMultActAccessRule_Type(Integer32):
    """Custom type hh3cEponUniMultActAccessRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 2),
          ("preview", 3))
    )


_Hh3cEponUniMultActAccessRule_Type.__name__ = "Integer32"
_Hh3cEponUniMultActAccessRule_Object = MibTableColumn
hh3cEponUniMultActAccessRule = _Hh3cEponUniMultActAccessRule_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 15, 1, 3),
    _Hh3cEponUniMultActAccessRule_Type()
)
hh3cEponUniMultActAccessRule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniMultActAccessRule.setStatus("current")
_Hh3cEponUniMultActPreTimes_Type = Integer32
_Hh3cEponUniMultActPreTimes_Object = MibTableColumn
hh3cEponUniMultActPreTimes = _Hh3cEponUniMultActPreTimes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 15, 1, 4),
    _Hh3cEponUniMultActPreTimes_Type()
)
hh3cEponUniMultActPreTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniMultActPreTimes.setStatus("current")
_Hh3cEponUniMultActPreRemain_Type = Integer32
_Hh3cEponUniMultActPreRemain_Object = MibTableColumn
hh3cEponUniMultActPreRemain = _Hh3cEponUniMultActPreRemain_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 15, 1, 5),
    _Hh3cEponUniMultActPreRemain_Type()
)
hh3cEponUniMultActPreRemain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniMultActPreRemain.setStatus("current")
_Hh3cEponUniMulticastIndexNextTable_Object = MibTable
hh3cEponUniMulticastIndexNextTable = _Hh3cEponUniMulticastIndexNextTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 16)
)
if mibBuilder.loadTexts:
    hh3cEponUniMulticastIndexNextTable.setStatus("current")
_Hh3cEponUniMulticastIndexNextEntry_Object = MibTableRow
hh3cEponUniMulticastIndexNextEntry = _Hh3cEponUniMulticastIndexNextEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 16, 1)
)
hh3cEponUniMulticastIndexNextEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-EPON-UNI-MIB", "hh3cEponUniIndex"),
)
if mibBuilder.loadTexts:
    hh3cEponUniMulticastIndexNextEntry.setStatus("current")
_Hh3cEponUniMulticastConfIndexNext_Type = Integer32
_Hh3cEponUniMulticastConfIndexNext_Object = MibTableColumn
hh3cEponUniMulticastConfIndexNext = _Hh3cEponUniMulticastConfIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 1, 16, 1, 1),
    _Hh3cEponUniMulticastConfIndexNext_Type()
)
hh3cEponUniMulticastConfIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEponUniMulticastConfIndexNext.setStatus("current")
_Hh3cEponUniTrap_ObjectIdentity = ObjectIdentity
hh3cEponUniTrap = _Hh3cEponUniTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 2)
)
_Hh3cEponUniTrapPrefix_ObjectIdentity = ObjectIdentity
hh3cEponUniTrapPrefix = _Hh3cEponUniTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 2, 0)
)

# Managed Objects groups


# Notification objects

hh3cEponUniLinkUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 2, 0, 1)
)
hh3cEponUniLinkUpTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-EPON-UNI-MIB", "hh3cEponUniIndex"),
        ("HH3C-EPON-UNI-MIB", "hh3cEponUniDescr"),
        ("HH3C-EPON-UNI-MIB", "hh3cEponUniAdminStatus"))
)
if mibBuilder.loadTexts:
    hh3cEponUniLinkUpTrap.setStatus(
        "current"
    )

hh3cEponUniLinkDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 42, 5, 2, 0, 2)
)
hh3cEponUniLinkDownTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-EPON-UNI-MIB", "hh3cEponUniIndex"),
        ("HH3C-EPON-UNI-MIB", "hh3cEponUniDescr"),
        ("HH3C-EPON-UNI-MIB", "hh3cEponUniAdminStatus"))
)
if mibBuilder.loadTexts:
    hh3cEponUniLinkDownTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-EPON-UNI-MIB",
    **{"hh3cEponUni": hh3cEponUni,
       "hh3cEponUniSysMan": hh3cEponUniSysMan,
       "hh3cEponUniSysManTable": hh3cEponUniSysManTable,
       "hh3cEponUniSysManEntry": hh3cEponUniSysManEntry,
       "hh3cEponUniIndex": hh3cEponUniIndex,
       "hh3cEponUniDescr": hh3cEponUniDescr,
       "hh3cEponUniAdminStatus": hh3cEponUniAdminStatus,
       "hh3cEponUniMdi": hh3cEponUniMdi,
       "hh3cEponUniPriority": hh3cEponUniPriority,
       "hh3cEponUniVlanType": hh3cEponUniVlanType,
       "hh3cEponUniAccessVlan": hh3cEponUniAccessVlan,
       "hh3cEponUniTrunkPvid": hh3cEponUniTrunkPvid,
       "hh3cEponUniVLANTrunkAllowListLow": hh3cEponUniVLANTrunkAllowListLow,
       "hh3cEponUniVLANTrunkAllowListHigh": hh3cEponUniVLANTrunkAllowListHigh,
       "hh3cEponUniInboundLineRate": hh3cEponUniInboundLineRate,
       "hh3cEponUniOutboundLineRate": hh3cEponUniOutboundLineRate,
       "hh3cEponUniFlowControl": hh3cEponUniFlowControl,
       "hh3cEponUniSpeed": hh3cEponUniSpeed,
       "hh3cEponUniDuplex": hh3cEponUniDuplex,
       "hh3cEponUniVlanVPNStatus": hh3cEponUniVlanVPNStatus,
       "hh3cEponUniCountReset": hh3cEponUniCountReset,
       "hh3cEponUniPortIsolate": hh3cEponUniPortIsolate,
       "hh3cEponUniVlanConfiguration": hh3cEponUniVlanConfiguration,
       "hh3cEponUniAutoNegotiation": hh3cEponUniAutoNegotiation,
       "hh3cEponUniRestartAutoNeg": hh3cEponUniRestartAutoNeg,
       "hh3cEponUniLinkStatus": hh3cEponUniLinkStatus,
       "hh3cEponUniInterfaceType": hh3cEponUniInterfaceType,
       "hh3cEponUniVitualCableTest": hh3cEponUniVitualCableTest,
       "hh3cEponUniVCTCableStatus": hh3cEponUniVCTCableStatus,
       "hh3cEponUniVCTCableLength": hh3cEponUniVCTCableLength,
       "hh3cEponUniVCTImpedanceMismatch": hh3cEponUniVCTImpedanceMismatch,
       "hh3cEponUniVCTPairSkew": hh3cEponUniVCTPairSkew,
       "hh3cEponUniVCTPairSwap": hh3cEponUniVCTPairSwap,
       "hh3cEponUniVCTPolaritySwap": hh3cEponUniVCTPolaritySwap,
       "hh3cEponUniVCTInsertionLoss": hh3cEponUniVCTInsertionLoss,
       "hh3cEponUniVCTReturnLoss": hh3cEponUniVCTReturnLoss,
       "hh3cEponUniVCTNearendCrosstalk": hh3cEponUniVCTNearendCrosstalk,
       "hh3cEponUniCountTable": hh3cEponUniCountTable,
       "hh3cEponUniCountEntry": hh3cEponUniCountEntry,
       "hh3cEponUniInStatsPkts": hh3cEponUniInStatsPkts,
       "hh3cEponUniInStatsUnicastPkts": hh3cEponUniInStatsUnicastPkts,
       "hh3cEponUniInStatsBroadcastPkts": hh3cEponUniInStatsBroadcastPkts,
       "hh3cEponUniInStatsMulticastPkts": hh3cEponUniInStatsMulticastPkts,
       "hh3cEponUniInPausePkts": hh3cEponUniInPausePkts,
       "hh3cEponUniInTotalErrors": hh3cEponUniInTotalErrors,
       "hh3cEponUniInStatsCRCAlignErrors": hh3cEponUniInStatsCRCAlignErrors,
       "hh3cEponUniInStatsUndersizePkts": hh3cEponUniInStatsUndersizePkts,
       "hh3cEponUniInStatsOversizePkts": hh3cEponUniInStatsOversizePkts,
       "hh3cEponUniInErrorbyOther": hh3cEponUniInErrorbyOther,
       "hh3cEponUniOutStatsPkts": hh3cEponUniOutStatsPkts,
       "hh3cEponUniOutStatsUnicastPkts": hh3cEponUniOutStatsUnicastPkts,
       "hh3cEponUniOutStatsBroadcastPkts": hh3cEponUniOutStatsBroadcastPkts,
       "hh3cEponUniOutStatsMulticastPkts": hh3cEponUniOutStatsMulticastPkts,
       "hh3cEponUniOutStatsPausePkts": hh3cEponUniOutStatsPausePkts,
       "hh3cEponUniOutTotalErrors": hh3cEponUniOutTotalErrors,
       "hh3cEponUniOutStatsCollisions": hh3cEponUniOutStatsCollisions,
       "hh3cEponUniOutDelayExceededDiscards": hh3cEponUniOutDelayExceededDiscards,
       "hh3cEponUniOutErrorbyOther": hh3cEponUniOutErrorbyOther,
       "hh3cEponUniOutDroppedFrames": hh3cEponUniOutDroppedFrames,
       "hh3cEponUniIgmpInfoTable": hh3cEponUniIgmpInfoTable,
       "hh3cEponUniIgmpInfoEntry": hh3cEponUniIgmpInfoEntry,
       "hh3cEponUniMacIndex": hh3cEponUniMacIndex,
       "hh3cEponUniIgmpMacAddress": hh3cEponUniIgmpMacAddress,
       "hh3cEponUniIgmpVlanId": hh3cEponUniIgmpVlanId,
       "hh3cEponUniParaMan": hh3cEponUniParaMan,
       "hh3cEponUniLineRateMax": hh3cEponUniLineRateMax,
       "hh3cEponUniLineRateStep": hh3cEponUniLineRateStep,
       "hh3cEponUniNumberOnOnu": hh3cEponUniNumberOnOnu,
       "hh3cEponUniScalarGroup": hh3cEponUniScalarGroup,
       "hh3cEponUniPortPolicyTable": hh3cEponUniPortPolicyTable,
       "hh3cEponUniPortPolicyEntry": hh3cEponUniPortPolicyEntry,
       "hh3cEponUniPortPolicyStatus": hh3cEponUniPortPolicyStatus,
       "hh3cEponUniPortPolicyCir": hh3cEponUniPortPolicyCir,
       "hh3cEponUniPortPolicyBucketDepth": hh3cEponUniPortPolicyBucketDepth,
       "hh3cEponUniPortPolicyExtraBurst": hh3cEponUniPortPolicyExtraBurst,
       "hh3cEponUniPortPolicyInboundCir": hh3cEponUniPortPolicyInboundCir,
       "hh3cEponUniPortPolicyInboundBucketDepth": hh3cEponUniPortPolicyInboundBucketDepth,
       "hh3cEponUniPortPolicyInboundExtraBurst": hh3cEponUniPortPolicyInboundExtraBurst,
       "hh3cEponUniPortPolicyOutboundCir": hh3cEponUniPortPolicyOutboundCir,
       "hh3cEponUniPortPolicyOutboundPir": hh3cEponUniPortPolicyOutboundPir,
       "hh3cEponUniMulticastTable": hh3cEponUniMulticastTable,
       "hh3cEponUniMulticastEntry": hh3cEponUniMulticastEntry,
       "hh3cEponUniMulticastGroupNumber": hh3cEponUniMulticastGroupNumber,
       "hh3cEponUniMulticastVlanList": hh3cEponUniMulticastVlanList,
       "hh3cEponUniMulticastStripStatus": hh3cEponUniMulticastStripStatus,
       "hh3cEponUniMulticastFastleave": hh3cEponUniMulticastFastleave,
       "hh3cEponUniTechAbilityTable": hh3cEponUniTechAbilityTable,
       "hh3cEponUniTechAbilityEntry": hh3cEponUniTechAbilityEntry,
       "hh3cEponUniLocalTechAbility": hh3cEponUniLocalTechAbility,
       "hh3cEponUniAdvertisedTechAbility": hh3cEponUniAdvertisedTechAbility,
       "hh3cEponUniMulticastControlTable": hh3cEponUniMulticastControlTable,
       "hh3cEponUniMulticastControlEntry": hh3cEponUniMulticastControlEntry,
       "hh3cEponUniMulticastVlanIndex": hh3cEponUniMulticastVlanIndex,
       "hh3cEponUniMulticastAddressList": hh3cEponUniMulticastAddressList,
       "hh3cEponUniMulticastAccessRule": hh3cEponUniMulticastAccessRule,
       "hh3cEponUniMulticastChannelLimit": hh3cEponUniMulticastChannelLimit,
       "hh3cEponUniMulticastPreTimeSlice": hh3cEponUniMulticastPreTimeSlice,
       "hh3cEponUniMulticastPreTimes": hh3cEponUniMulticastPreTimes,
       "hh3cEponUniMulticastPreInterval": hh3cEponUniMulticastPreInterval,
       "hh3cEponUniMulticastRowStatus": hh3cEponUniMulticastRowStatus,
       "hh3cEponUniMulticastIndex": hh3cEponUniMulticastIndex,
       "hh3cEponUniMulticastSourceIpList": hh3cEponUniMulticastSourceIpList,
       "hh3cEponUniMulticastResetInterval": hh3cEponUniMulticastResetInterval,
       "hh3cEponUniQosIndexNextTable": hh3cEponUniQosIndexNextTable,
       "hh3cEponUniQosIndexNextEntry": hh3cEponUniQosIndexNextEntry,
       "hh3cEponUniQosConfIndexNext": hh3cEponUniQosConfIndexNext,
       "hh3cEponUniQosConfTable": hh3cEponUniQosConfTable,
       "hh3cEponUniQosConfEntry": hh3cEponUniQosConfEntry,
       "hh3cEponUniQosConfIndex": hh3cEponUniQosConfIndex,
       "hh3cEponUniQosConfRuleIndexNext": hh3cEponUniQosConfRuleIndexNext,
       "hh3cEponUniQosConfMappedQueue": hh3cEponUniQosConfMappedQueue,
       "hh3cEponUniQosConfMarkedPriority": hh3cEponUniQosConfMarkedPriority,
       "hh3cEponUniQosConfRowStatus": hh3cEponUniQosConfRowStatus,
       "hh3cEponUniQosRuleTable": hh3cEponUniQosRuleTable,
       "hh3cEponUniQosRuleEntry": hh3cEponUniQosRuleEntry,
       "hh3cEponUniQosRuleIndex": hh3cEponUniQosRuleIndex,
       "hh3cEponUniQosRuleSelector": hh3cEponUniQosRuleSelector,
       "hh3cEponUniQosRuleValue": hh3cEponUniQosRuleValue,
       "hh3cEponUniQosRuleMacAddress": hh3cEponUniQosRuleMacAddress,
       "hh3cEponUniQosRuleOperator": hh3cEponUniQosRuleOperator,
       "hh3cEponUniQosRuleRowStatus": hh3cEponUniQosRuleRowStatus,
       "hh3cEponUniMirrorGroupTable": hh3cEponUniMirrorGroupTable,
       "hh3cEponUniMirrorGroupEntry": hh3cEponUniMirrorGroupEntry,
       "hh3cEponUniMirrorGroupID": hh3cEponUniMirrorGroupID,
       "hh3cEponUniMirrorInboundPortList": hh3cEponUniMirrorInboundPortList,
       "hh3cEponUniMirrorOutboundPortList": hh3cEponUniMirrorOutboundPortList,
       "hh3cEponUniMonitorPort": hh3cEponUniMonitorPort,
       "hh3cEponUniMirrorRowStatus": hh3cEponUniMirrorRowStatus,
       "hh3cEponUniMirrorGroupIdNextTable": hh3cEponUniMirrorGroupIdNextTable,
       "hh3cEponUniMirrorGroupIdNextEntry": hh3cEponUniMirrorGroupIdNextEntry,
       "hh3cEponUniMirrorGroupIDNext": hh3cEponUniMirrorGroupIDNext,
       "hh3cEponUniMulticastCtrlInfoTable": hh3cEponUniMulticastCtrlInfoTable,
       "hh3cEponUniMulticastCtrlInfoEntry": hh3cEponUniMulticastCtrlInfoEntry,
       "hh3cEponUniMultActVlan": hh3cEponUniMultActVlan,
       "hh3cEponUniMultActAddress": hh3cEponUniMultActAddress,
       "hh3cEponUniMultActAccessRule": hh3cEponUniMultActAccessRule,
       "hh3cEponUniMultActPreTimes": hh3cEponUniMultActPreTimes,
       "hh3cEponUniMultActPreRemain": hh3cEponUniMultActPreRemain,
       "hh3cEponUniMulticastIndexNextTable": hh3cEponUniMulticastIndexNextTable,
       "hh3cEponUniMulticastIndexNextEntry": hh3cEponUniMulticastIndexNextEntry,
       "hh3cEponUniMulticastConfIndexNext": hh3cEponUniMulticastConfIndexNext,
       "hh3cEponUniTrap": hh3cEponUniTrap,
       "hh3cEponUniTrapPrefix": hh3cEponUniTrapPrefix,
       "hh3cEponUniLinkUpTrap": hh3cEponUniLinkUpTrap,
       "hh3cEponUniLinkDownTrap": hh3cEponUniLinkDownTrap}
)
