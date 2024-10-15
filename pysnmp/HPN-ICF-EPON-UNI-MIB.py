# SNMP MIB module (HPN-ICF-EPON-UNI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-EPON-UNI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:00:10 2024
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

(hpnicfEpon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfEpon")

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

hpnicfEponUni = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfEponUniSysMan_ObjectIdentity = ObjectIdentity
hpnicfEponUniSysMan = _HpnicfEponUniSysMan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1)
)
_HpnicfEponUniSysManTable_Object = MibTable
hpnicfEponUniSysManTable = _HpnicfEponUniSysManTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfEponUniSysManTable.setStatus("current")
_HpnicfEponUniSysManEntry_Object = MibTableRow
hpnicfEponUniSysManEntry = _HpnicfEponUniSysManEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 1, 1)
)
hpnicfEponUniSysManEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-EPON-UNI-MIB", "hpnicfEponUniIndex"),
)
if mibBuilder.loadTexts:
    hpnicfEponUniSysManEntry.setStatus("current")
_HpnicfEponUniIndex_Type = Integer32
_HpnicfEponUniIndex_Object = MibTableColumn
hpnicfEponUniIndex = _HpnicfEponUniIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 1, 1, 1),
    _HpnicfEponUniIndex_Type()
)
hpnicfEponUniIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfEponUniIndex.setStatus("current")
_HpnicfEponUniDescr_Type = OctetString
_HpnicfEponUniDescr_Object = MibTableColumn
hpnicfEponUniDescr = _HpnicfEponUniDescr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 1, 1, 2),
    _HpnicfEponUniDescr_Type()
)
hpnicfEponUniDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponUniDescr.setStatus("current")


class _HpnicfEponUniAdminStatus_Type(Integer32):
    """Custom type hpnicfEponUniAdminStatus based on Integer32"""
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


_HpnicfEponUniAdminStatus_Type.__name__ = "Integer32"
_HpnicfEponUniAdminStatus_Object = MibTableColumn
hpnicfEponUniAdminStatus = _HpnicfEponUniAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 1, 1, 3),
    _HpnicfEponUniAdminStatus_Type()
)
hpnicfEponUniAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponUniAdminStatus.setStatus("current")


class _HpnicfEponUniMdi_Type(Integer32):
    """Custom type hpnicfEponUniMdi based on Integer32"""
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


_HpnicfEponUniMdi_Type.__name__ = "Integer32"
_HpnicfEponUniMdi_Object = MibTableColumn
hpnicfEponUniMdi = _HpnicfEponUniMdi_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 1, 1, 4),
    _HpnicfEponUniMdi_Type()
)
hpnicfEponUniMdi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponUniMdi.setStatus("current")


class _HpnicfEponUniPriority_Type(Integer32):
    """Custom type hpnicfEponUniPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HpnicfEponUniPriority_Type.__name__ = "Integer32"
_HpnicfEponUniPriority_Object = MibTableColumn
hpnicfEponUniPriority = _HpnicfEponUniPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 1, 1, 5),
    _HpnicfEponUniPriority_Type()
)
hpnicfEponUniPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponUniPriority.setStatus("current")


class _HpnicfEponUniVlanType_Type(Integer32):
    """Custom type hpnicfEponUniVlanType based on Integer32"""
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


_HpnicfEponUniVlanType_Type.__name__ = "Integer32"
_HpnicfEponUniVlanType_Object = MibTableColumn
hpnicfEponUniVlanType = _HpnicfEponUniVlanType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 1, 1, 6),
    _HpnicfEponUniVlanType_Type()
)
hpnicfEponUniVlanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponUniVlanType.setStatus("current")


class _HpnicfEponUniAccessVlan_Type(Integer32):
    """Custom type hpnicfEponUniAccessVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HpnicfEponUniAccessVlan_Type.__name__ = "Integer32"
_HpnicfEponUniAccessVlan_Object = MibTableColumn
hpnicfEponUniAccessVlan = _HpnicfEponUniAccessVlan_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 1, 1, 7),
    _HpnicfEponUniAccessVlan_Type()
)
hpnicfEponUniAccessVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponUniAccessVlan.setStatus("current")


class _HpnicfEponUniTrunkPvid_Type(Integer32):
    """Custom type hpnicfEponUniTrunkPvid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HpnicfEponUniTrunkPvid_Type.__name__ = "Integer32"
_HpnicfEponUniTrunkPvid_Object = MibTableColumn
hpnicfEponUniTrunkPvid = _HpnicfEponUniTrunkPvid_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 1, 1, 8),
    _HpnicfEponUniTrunkPvid_Type()
)
hpnicfEponUniTrunkPvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponUniTrunkPvid.setStatus("current")
_HpnicfEponUniVLANTrunkAllowListLow_Type = OctetString
_HpnicfEponUniVLANTrunkAllowListLow_Object = MibTableColumn
hpnicfEponUniVLANTrunkAllowListLow = _HpnicfEponUniVLANTrunkAllowListLow_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 1, 1, 9),
    _HpnicfEponUniVLANTrunkAllowListLow_Type()
)
hpnicfEponUniVLANTrunkAllowListLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponUniVLANTrunkAllowListLow.setStatus("current")
_HpnicfEponUniVLANTrunkAllowListHigh_Type = OctetString
_HpnicfEponUniVLANTrunkAllowListHigh_Object = MibTableColumn
hpnicfEponUniVLANTrunkAllowListHigh = _HpnicfEponUniVLANTrunkAllowListHigh_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 1, 1, 10),
    _HpnicfEponUniVLANTrunkAllowListHigh_Type()
)
hpnicfEponUniVLANTrunkAllowListHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponUniVLANTrunkAllowListHigh.setStatus("current")
_HpnicfEponUniInboundLineRate_Type = Integer32
_HpnicfEponUniInboundLineRate_Object = MibTableColumn
hpnicfEponUniInboundLineRate = _HpnicfEponUniInboundLineRate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 1, 1, 11),
    _HpnicfEponUniInboundLineRate_Type()
)
hpnicfEponUniInboundLineRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponUniInboundLineRate.setStatus("current")
_HpnicfEponUniOutboundLineRate_Type = Integer32
_HpnicfEponUniOutboundLineRate_Object = MibTableColumn
hpnicfEponUniOutboundLineRate = _HpnicfEponUniOutboundLineRate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 1, 1, 12),
    _HpnicfEponUniOutboundLineRate_Type()
)
hpnicfEponUniOutboundLineRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponUniOutboundLineRate.setStatus("current")
_HpnicfEponUniFlowControl_Type = TruthValue
_HpnicfEponUniFlowControl_Object = MibTableColumn
hpnicfEponUniFlowControl = _HpnicfEponUniFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 1, 1, 13),
    _HpnicfEponUniFlowControl_Type()
)
hpnicfEponUniFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponUniFlowControl.setStatus("current")


class _HpnicfEponUniSpeed_Type(Integer32):
    """Custom type hpnicfEponUniSpeed based on Integer32"""
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


_HpnicfEponUniSpeed_Type.__name__ = "Integer32"
_HpnicfEponUniSpeed_Object = MibTableColumn
hpnicfEponUniSpeed = _HpnicfEponUniSpeed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 1, 1, 14),
    _HpnicfEponUniSpeed_Type()
)
hpnicfEponUniSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponUniSpeed.setStatus("current")


class _HpnicfEponUniDuplex_Type(Integer32):
    """Custom type hpnicfEponUniDuplex based on Integer32"""
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


_HpnicfEponUniDuplex_Type.__name__ = "Integer32"
_HpnicfEponUniDuplex_Object = MibTableColumn
hpnicfEponUniDuplex = _HpnicfEponUniDuplex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 1, 1, 15),
    _HpnicfEponUniDuplex_Type()
)
hpnicfEponUniDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponUniDuplex.setStatus("current")
_HpnicfEponUniVlanVPNStatus_Type = TruthValue
_HpnicfEponUniVlanVPNStatus_Object = MibTableColumn
hpnicfEponUniVlanVPNStatus = _HpnicfEponUniVlanVPNStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 1, 1, 16),
    _HpnicfEponUniVlanVPNStatus_Type()
)
hpnicfEponUniVlanVPNStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponUniVlanVPNStatus.setStatus("current")


class _HpnicfEponUniCountReset_Type(Integer32):
    """Custom type hpnicfEponUniCountReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_HpnicfEponUniCountReset_Type.__name__ = "Integer32"
_HpnicfEponUniCountReset_Object = MibTableColumn
hpnicfEponUniCountReset = _HpnicfEponUniCountReset_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 1, 1, 17),
    _HpnicfEponUniCountReset_Type()
)
hpnicfEponUniCountReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponUniCountReset.setStatus("current")


class _HpnicfEponUniPortIsolate_Type(Integer32):
    """Custom type hpnicfEponUniPortIsolate based on Integer32"""
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


_HpnicfEponUniPortIsolate_Type.__name__ = "Integer32"
_HpnicfEponUniPortIsolate_Object = MibTableColumn
hpnicfEponUniPortIsolate = _HpnicfEponUniPortIsolate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 1, 1, 18),
    _HpnicfEponUniPortIsolate_Type()
)
hpnicfEponUniPortIsolate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponUniPortIsolate.setStatus("current")


class _HpnicfEponUniVlanConfiguration_Type(OctetString):
    """Custom type hpnicfEponUniVlanConfiguration based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfEponUniVlanConfiguration_Type.__name__ = "OctetString"
_HpnicfEponUniVlanConfiguration_Object = MibTableColumn
hpnicfEponUniVlanConfiguration = _HpnicfEponUniVlanConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 1, 1, 23),
    _HpnicfEponUniVlanConfiguration_Type()
)
hpnicfEponUniVlanConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponUniVlanConfiguration.setStatus("current")


class _HpnicfEponUniAutoNegotiation_Type(Integer32):
    """Custom type hpnicfEponUniAutoNegotiation based on Integer32"""
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


_HpnicfEponUniAutoNegotiation_Type.__name__ = "Integer32"
_HpnicfEponUniAutoNegotiation_Object = MibTableColumn
hpnicfEponUniAutoNegotiation = _HpnicfEponUniAutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 1, 1, 25),
    _HpnicfEponUniAutoNegotiation_Type()
)
hpnicfEponUniAutoNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponUniAutoNegotiation.setStatus("current")


class _HpnicfEponUniRestartAutoNeg_Type(Integer32):
    """Custom type hpnicfEponUniRestartAutoNeg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("autoNegotiation", 1)
    )


_HpnicfEponUniRestartAutoNeg_Type.__name__ = "Integer32"
_HpnicfEponUniRestartAutoNeg_Object = MibTableColumn
hpnicfEponUniRestartAutoNeg = _HpnicfEponUniRestartAutoNeg_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 1, 1, 26),
    _HpnicfEponUniRestartAutoNeg_Type()
)
hpnicfEponUniRestartAutoNeg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponUniRestartAutoNeg.setStatus("current")


class _HpnicfEponUniLinkStatus_Type(Integer32):
    """Custom type hpnicfEponUniLinkStatus based on Integer32"""
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


_HpnicfEponUniLinkStatus_Type.__name__ = "Integer32"
_HpnicfEponUniLinkStatus_Object = MibTableColumn
hpnicfEponUniLinkStatus = _HpnicfEponUniLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 1, 1, 29),
    _HpnicfEponUniLinkStatus_Type()
)
hpnicfEponUniLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponUniLinkStatus.setStatus("current")


class _HpnicfEponUniInterfaceType_Type(Integer32):
    """Custom type hpnicfEponUniInterfaceType based on Integer32"""
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


_HpnicfEponUniInterfaceType_Type.__name__ = "Integer32"
_HpnicfEponUniInterfaceType_Object = MibTableColumn
hpnicfEponUniInterfaceType = _HpnicfEponUniInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 1, 1, 30),
    _HpnicfEponUniInterfaceType_Type()
)
hpnicfEponUniInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponUniInterfaceType.setStatus("current")


class _HpnicfEponUniVitualCableTest_Type(Integer32):
    """Custom type hpnicfEponUniVitualCableTest based on Integer32"""
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


_HpnicfEponUniVitualCableTest_Type.__name__ = "Integer32"
_HpnicfEponUniVitualCableTest_Object = MibTableColumn
hpnicfEponUniVitualCableTest = _HpnicfEponUniVitualCableTest_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 1, 1, 31),
    _HpnicfEponUniVitualCableTest_Type()
)
hpnicfEponUniVitualCableTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponUniVitualCableTest.setStatus("current")


class _HpnicfEponUniVCTCableStatus_Type(Integer32):
    """Custom type hpnicfEponUniVCTCableStatus based on Integer32"""
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


_HpnicfEponUniVCTCableStatus_Type.__name__ = "Integer32"
_HpnicfEponUniVCTCableStatus_Object = MibTableColumn
hpnicfEponUniVCTCableStatus = _HpnicfEponUniVCTCableStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 1, 1, 32),
    _HpnicfEponUniVCTCableStatus_Type()
)
hpnicfEponUniVCTCableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponUniVCTCableStatus.setStatus("current")
_HpnicfEponUniVCTCableLength_Type = Integer32
_HpnicfEponUniVCTCableLength_Object = MibTableColumn
hpnicfEponUniVCTCableLength = _HpnicfEponUniVCTCableLength_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 1, 1, 33),
    _HpnicfEponUniVCTCableLength_Type()
)
hpnicfEponUniVCTCableLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponUniVCTCableLength.setStatus("current")


class _HpnicfEponUniVCTImpedanceMismatch_Type(Integer32):
    """Custom type hpnicfEponUniVCTImpedanceMismatch based on Integer32"""
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


_HpnicfEponUniVCTImpedanceMismatch_Type.__name__ = "Integer32"
_HpnicfEponUniVCTImpedanceMismatch_Object = MibTableColumn
hpnicfEponUniVCTImpedanceMismatch = _HpnicfEponUniVCTImpedanceMismatch_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 1, 1, 34),
    _HpnicfEponUniVCTImpedanceMismatch_Type()
)
hpnicfEponUniVCTImpedanceMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponUniVCTImpedanceMismatch.setStatus("current")
_HpnicfEponUniVCTPairSkew_Type = Integer32
_HpnicfEponUniVCTPairSkew_Object = MibTableColumn
hpnicfEponUniVCTPairSkew = _HpnicfEponUniVCTPairSkew_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 1, 1, 35),
    _HpnicfEponUniVCTPairSkew_Type()
)
hpnicfEponUniVCTPairSkew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponUniVCTPairSkew.setStatus("current")


class _HpnicfEponUniVCTPairSwap_Type(Integer32):
    """Custom type hpnicfEponUniVCTPairSwap based on Integer32"""
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


_HpnicfEponUniVCTPairSwap_Type.__name__ = "Integer32"
_HpnicfEponUniVCTPairSwap_Object = MibTableColumn
hpnicfEponUniVCTPairSwap = _HpnicfEponUniVCTPairSwap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 1, 1, 36),
    _HpnicfEponUniVCTPairSwap_Type()
)
hpnicfEponUniVCTPairSwap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponUniVCTPairSwap.setStatus("current")


class _HpnicfEponUniVCTPolaritySwap_Type(Integer32):
    """Custom type hpnicfEponUniVCTPolaritySwap based on Integer32"""
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


_HpnicfEponUniVCTPolaritySwap_Type.__name__ = "Integer32"
_HpnicfEponUniVCTPolaritySwap_Object = MibTableColumn
hpnicfEponUniVCTPolaritySwap = _HpnicfEponUniVCTPolaritySwap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 1, 1, 37),
    _HpnicfEponUniVCTPolaritySwap_Type()
)
hpnicfEponUniVCTPolaritySwap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponUniVCTPolaritySwap.setStatus("current")
_HpnicfEponUniVCTInsertionLoss_Type = Integer32
_HpnicfEponUniVCTInsertionLoss_Object = MibTableColumn
hpnicfEponUniVCTInsertionLoss = _HpnicfEponUniVCTInsertionLoss_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 1, 1, 38),
    _HpnicfEponUniVCTInsertionLoss_Type()
)
hpnicfEponUniVCTInsertionLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponUniVCTInsertionLoss.setStatus("current")
_HpnicfEponUniVCTReturnLoss_Type = Integer32
_HpnicfEponUniVCTReturnLoss_Object = MibTableColumn
hpnicfEponUniVCTReturnLoss = _HpnicfEponUniVCTReturnLoss_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 1, 1, 39),
    _HpnicfEponUniVCTReturnLoss_Type()
)
hpnicfEponUniVCTReturnLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponUniVCTReturnLoss.setStatus("current")
_HpnicfEponUniVCTNearendCrosstalk_Type = Integer32
_HpnicfEponUniVCTNearendCrosstalk_Object = MibTableColumn
hpnicfEponUniVCTNearendCrosstalk = _HpnicfEponUniVCTNearendCrosstalk_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 1, 1, 40),
    _HpnicfEponUniVCTNearendCrosstalk_Type()
)
hpnicfEponUniVCTNearendCrosstalk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponUniVCTNearendCrosstalk.setStatus("current")
_HpnicfEponUniVlan_Type = Integer32
_HpnicfEponUniVlan_Object = MibTableColumn
hpnicfEponUniVlan = _HpnicfEponUniVlan_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 1, 1, 41),
    _HpnicfEponUniVlan_Type()
)
hpnicfEponUniVlan.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfEponUniVlan.setStatus("current")
_HpnicfEponUniCountTable_Object = MibTable
hpnicfEponUniCountTable = _HpnicfEponUniCountTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfEponUniCountTable.setStatus("current")
_HpnicfEponUniCountEntry_Object = MibTableRow
hpnicfEponUniCountEntry = _HpnicfEponUniCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 2, 1)
)
hpnicfEponUniCountEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-EPON-UNI-MIB", "hpnicfEponUniIndex"),
)
if mibBuilder.loadTexts:
    hpnicfEponUniCountEntry.setStatus("current")
_HpnicfEponUniInStatsPkts_Type = Unsigned32
_HpnicfEponUniInStatsPkts_Object = MibTableColumn
hpnicfEponUniInStatsPkts = _HpnicfEponUniInStatsPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 2, 1, 1),
    _HpnicfEponUniInStatsPkts_Type()
)
hpnicfEponUniInStatsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponUniInStatsPkts.setStatus("current")
_HpnicfEponUniInStatsUnicastPkts_Type = Unsigned32
_HpnicfEponUniInStatsUnicastPkts_Object = MibTableColumn
hpnicfEponUniInStatsUnicastPkts = _HpnicfEponUniInStatsUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 2, 1, 2),
    _HpnicfEponUniInStatsUnicastPkts_Type()
)
hpnicfEponUniInStatsUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponUniInStatsUnicastPkts.setStatus("current")
_HpnicfEponUniInStatsBroadcastPkts_Type = Unsigned32
_HpnicfEponUniInStatsBroadcastPkts_Object = MibTableColumn
hpnicfEponUniInStatsBroadcastPkts = _HpnicfEponUniInStatsBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 2, 1, 3),
    _HpnicfEponUniInStatsBroadcastPkts_Type()
)
hpnicfEponUniInStatsBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponUniInStatsBroadcastPkts.setStatus("current")
_HpnicfEponUniInStatsMulticastPkts_Type = Unsigned32
_HpnicfEponUniInStatsMulticastPkts_Object = MibTableColumn
hpnicfEponUniInStatsMulticastPkts = _HpnicfEponUniInStatsMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 2, 1, 4),
    _HpnicfEponUniInStatsMulticastPkts_Type()
)
hpnicfEponUniInStatsMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponUniInStatsMulticastPkts.setStatus("current")
_HpnicfEponUniInPausePkts_Type = Unsigned32
_HpnicfEponUniInPausePkts_Object = MibTableColumn
hpnicfEponUniInPausePkts = _HpnicfEponUniInPausePkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 2, 1, 5),
    _HpnicfEponUniInPausePkts_Type()
)
hpnicfEponUniInPausePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponUniInPausePkts.setStatus("current")
_HpnicfEponUniInTotalErrors_Type = Unsigned32
_HpnicfEponUniInTotalErrors_Object = MibTableColumn
hpnicfEponUniInTotalErrors = _HpnicfEponUniInTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 2, 1, 6),
    _HpnicfEponUniInTotalErrors_Type()
)
hpnicfEponUniInTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponUniInTotalErrors.setStatus("current")
_HpnicfEponUniInStatsCRCAlignErrors_Type = Unsigned32
_HpnicfEponUniInStatsCRCAlignErrors_Object = MibTableColumn
hpnicfEponUniInStatsCRCAlignErrors = _HpnicfEponUniInStatsCRCAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 2, 1, 7),
    _HpnicfEponUniInStatsCRCAlignErrors_Type()
)
hpnicfEponUniInStatsCRCAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponUniInStatsCRCAlignErrors.setStatus("current")
_HpnicfEponUniInStatsUndersizePkts_Type = Unsigned32
_HpnicfEponUniInStatsUndersizePkts_Object = MibTableColumn
hpnicfEponUniInStatsUndersizePkts = _HpnicfEponUniInStatsUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 2, 1, 8),
    _HpnicfEponUniInStatsUndersizePkts_Type()
)
hpnicfEponUniInStatsUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponUniInStatsUndersizePkts.setStatus("current")
_HpnicfEponUniInStatsOversizePkts_Type = Unsigned32
_HpnicfEponUniInStatsOversizePkts_Object = MibTableColumn
hpnicfEponUniInStatsOversizePkts = _HpnicfEponUniInStatsOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 2, 1, 9),
    _HpnicfEponUniInStatsOversizePkts_Type()
)
hpnicfEponUniInStatsOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponUniInStatsOversizePkts.setStatus("current")
_HpnicfEponUniInErrorbyOther_Type = Unsigned32
_HpnicfEponUniInErrorbyOther_Object = MibTableColumn
hpnicfEponUniInErrorbyOther = _HpnicfEponUniInErrorbyOther_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 2, 1, 10),
    _HpnicfEponUniInErrorbyOther_Type()
)
hpnicfEponUniInErrorbyOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponUniInErrorbyOther.setStatus("current")
_HpnicfEponUniOutStatsPkts_Type = Unsigned32
_HpnicfEponUniOutStatsPkts_Object = MibTableColumn
hpnicfEponUniOutStatsPkts = _HpnicfEponUniOutStatsPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 2, 1, 11),
    _HpnicfEponUniOutStatsPkts_Type()
)
hpnicfEponUniOutStatsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponUniOutStatsPkts.setStatus("current")
_HpnicfEponUniOutStatsUnicastPkts_Type = Unsigned32
_HpnicfEponUniOutStatsUnicastPkts_Object = MibTableColumn
hpnicfEponUniOutStatsUnicastPkts = _HpnicfEponUniOutStatsUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 2, 1, 12),
    _HpnicfEponUniOutStatsUnicastPkts_Type()
)
hpnicfEponUniOutStatsUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponUniOutStatsUnicastPkts.setStatus("current")
_HpnicfEponUniOutStatsBroadcastPkts_Type = Unsigned32
_HpnicfEponUniOutStatsBroadcastPkts_Object = MibTableColumn
hpnicfEponUniOutStatsBroadcastPkts = _HpnicfEponUniOutStatsBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 2, 1, 13),
    _HpnicfEponUniOutStatsBroadcastPkts_Type()
)
hpnicfEponUniOutStatsBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponUniOutStatsBroadcastPkts.setStatus("current")
_HpnicfEponUniOutStatsMulticastPkts_Type = Unsigned32
_HpnicfEponUniOutStatsMulticastPkts_Object = MibTableColumn
hpnicfEponUniOutStatsMulticastPkts = _HpnicfEponUniOutStatsMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 2, 1, 14),
    _HpnicfEponUniOutStatsMulticastPkts_Type()
)
hpnicfEponUniOutStatsMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponUniOutStatsMulticastPkts.setStatus("current")
_HpnicfEponUniOutStatsPausePkts_Type = Unsigned32
_HpnicfEponUniOutStatsPausePkts_Object = MibTableColumn
hpnicfEponUniOutStatsPausePkts = _HpnicfEponUniOutStatsPausePkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 2, 1, 15),
    _HpnicfEponUniOutStatsPausePkts_Type()
)
hpnicfEponUniOutStatsPausePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponUniOutStatsPausePkts.setStatus("current")
_HpnicfEponUniOutTotalErrors_Type = Unsigned32
_HpnicfEponUniOutTotalErrors_Object = MibTableColumn
hpnicfEponUniOutTotalErrors = _HpnicfEponUniOutTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 2, 1, 16),
    _HpnicfEponUniOutTotalErrors_Type()
)
hpnicfEponUniOutTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponUniOutTotalErrors.setStatus("current")
_HpnicfEponUniOutStatsCollisions_Type = Unsigned32
_HpnicfEponUniOutStatsCollisions_Object = MibTableColumn
hpnicfEponUniOutStatsCollisions = _HpnicfEponUniOutStatsCollisions_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 2, 1, 17),
    _HpnicfEponUniOutStatsCollisions_Type()
)
hpnicfEponUniOutStatsCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponUniOutStatsCollisions.setStatus("current")
_HpnicfEponUniOutDelayExceededDiscards_Type = Unsigned32
_HpnicfEponUniOutDelayExceededDiscards_Object = MibTableColumn
hpnicfEponUniOutDelayExceededDiscards = _HpnicfEponUniOutDelayExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 2, 1, 18),
    _HpnicfEponUniOutDelayExceededDiscards_Type()
)
hpnicfEponUniOutDelayExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponUniOutDelayExceededDiscards.setStatus("current")
_HpnicfEponUniOutErrorbyOther_Type = Unsigned32
_HpnicfEponUniOutErrorbyOther_Object = MibTableColumn
hpnicfEponUniOutErrorbyOther = _HpnicfEponUniOutErrorbyOther_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 2, 1, 19),
    _HpnicfEponUniOutErrorbyOther_Type()
)
hpnicfEponUniOutErrorbyOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponUniOutErrorbyOther.setStatus("current")
_HpnicfEponUniOutDroppedFrames_Type = Unsigned32
_HpnicfEponUniOutDroppedFrames_Object = MibTableColumn
hpnicfEponUniOutDroppedFrames = _HpnicfEponUniOutDroppedFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 2, 1, 20),
    _HpnicfEponUniOutDroppedFrames_Type()
)
hpnicfEponUniOutDroppedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponUniOutDroppedFrames.setStatus("current")
_HpnicfEponUniIgmpInfoTable_Object = MibTable
hpnicfEponUniIgmpInfoTable = _HpnicfEponUniIgmpInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 3)
)
if mibBuilder.loadTexts:
    hpnicfEponUniIgmpInfoTable.setStatus("current")
_HpnicfEponUniIgmpInfoEntry_Object = MibTableRow
hpnicfEponUniIgmpInfoEntry = _HpnicfEponUniIgmpInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 3, 1)
)
hpnicfEponUniIgmpInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-EPON-UNI-MIB", "hpnicfEponUniIndex"),
    (0, "HPN-ICF-EPON-UNI-MIB", "hpnicfEponUniMacIndex"),
)
if mibBuilder.loadTexts:
    hpnicfEponUniIgmpInfoEntry.setStatus("current")
_HpnicfEponUniMacIndex_Type = Integer32
_HpnicfEponUniMacIndex_Object = MibTableColumn
hpnicfEponUniMacIndex = _HpnicfEponUniMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 3, 1, 1),
    _HpnicfEponUniMacIndex_Type()
)
hpnicfEponUniMacIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfEponUniMacIndex.setStatus("current")
_HpnicfEponUniIgmpMacAddress_Type = MacAddress
_HpnicfEponUniIgmpMacAddress_Object = MibTableColumn
hpnicfEponUniIgmpMacAddress = _HpnicfEponUniIgmpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 3, 1, 2),
    _HpnicfEponUniIgmpMacAddress_Type()
)
hpnicfEponUniIgmpMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponUniIgmpMacAddress.setStatus("current")


class _HpnicfEponUniIgmpVlanId_Type(Integer32):
    """Custom type hpnicfEponUniIgmpVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HpnicfEponUniIgmpVlanId_Type.__name__ = "Integer32"
_HpnicfEponUniIgmpVlanId_Object = MibTableColumn
hpnicfEponUniIgmpVlanId = _HpnicfEponUniIgmpVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 3, 1, 3),
    _HpnicfEponUniIgmpVlanId_Type()
)
hpnicfEponUniIgmpVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponUniIgmpVlanId.setStatus("current")
_HpnicfEponUniParaMan_ObjectIdentity = ObjectIdentity
hpnicfEponUniParaMan = _HpnicfEponUniParaMan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 4)
)
_HpnicfEponUniLineRateMax_Type = Integer32
_HpnicfEponUniLineRateMax_Object = MibScalar
hpnicfEponUniLineRateMax = _HpnicfEponUniLineRateMax_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 4, 1),
    _HpnicfEponUniLineRateMax_Type()
)
hpnicfEponUniLineRateMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponUniLineRateMax.setStatus("current")
_HpnicfEponUniLineRateStep_Type = Integer32
_HpnicfEponUniLineRateStep_Object = MibScalar
hpnicfEponUniLineRateStep = _HpnicfEponUniLineRateStep_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 4, 2),
    _HpnicfEponUniLineRateStep_Type()
)
hpnicfEponUniLineRateStep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponUniLineRateStep.setStatus("current")
_HpnicfEponUniNumberOnOnu_Type = Integer32
_HpnicfEponUniNumberOnOnu_Object = MibScalar
hpnicfEponUniNumberOnOnu = _HpnicfEponUniNumberOnOnu_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 4, 3),
    _HpnicfEponUniNumberOnOnu_Type()
)
hpnicfEponUniNumberOnOnu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponUniNumberOnOnu.setStatus("current")
_HpnicfEponUniScalarGroup_ObjectIdentity = ObjectIdentity
hpnicfEponUniScalarGroup = _HpnicfEponUniScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 5)
)
_HpnicfEponUniPortPolicyTable_Object = MibTable
hpnicfEponUniPortPolicyTable = _HpnicfEponUniPortPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 6)
)
if mibBuilder.loadTexts:
    hpnicfEponUniPortPolicyTable.setStatus("current")
_HpnicfEponUniPortPolicyEntry_Object = MibTableRow
hpnicfEponUniPortPolicyEntry = _HpnicfEponUniPortPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 6, 1)
)
hpnicfEponUniPortPolicyEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-EPON-UNI-MIB", "hpnicfEponUniIndex"),
)
if mibBuilder.loadTexts:
    hpnicfEponUniPortPolicyEntry.setStatus("current")


class _HpnicfEponUniPortPolicyStatus_Type(Integer32):
    """Custom type hpnicfEponUniPortPolicyStatus based on Integer32"""
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


_HpnicfEponUniPortPolicyStatus_Type.__name__ = "Integer32"
_HpnicfEponUniPortPolicyStatus_Object = MibTableColumn
hpnicfEponUniPortPolicyStatus = _HpnicfEponUniPortPolicyStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 6, 1, 1),
    _HpnicfEponUniPortPolicyStatus_Type()
)
hpnicfEponUniPortPolicyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponUniPortPolicyStatus.setStatus("current")


class _HpnicfEponUniPortPolicyCir_Type(Integer32):
    """Custom type hpnicfEponUniPortPolicyCir based on Integer32"""
    defaultValue = 102400


_HpnicfEponUniPortPolicyCir_Object = MibTableColumn
hpnicfEponUniPortPolicyCir = _HpnicfEponUniPortPolicyCir_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 6, 1, 2),
    _HpnicfEponUniPortPolicyCir_Type()
)
hpnicfEponUniPortPolicyCir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponUniPortPolicyCir.setStatus("current")


class _HpnicfEponUniPortPolicyBucketDepth_Type(Integer32):
    """Custom type hpnicfEponUniPortPolicyBucketDepth based on Integer32"""
    defaultValue = 0


_HpnicfEponUniPortPolicyBucketDepth_Object = MibTableColumn
hpnicfEponUniPortPolicyBucketDepth = _HpnicfEponUniPortPolicyBucketDepth_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 6, 1, 3),
    _HpnicfEponUniPortPolicyBucketDepth_Type()
)
hpnicfEponUniPortPolicyBucketDepth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponUniPortPolicyBucketDepth.setStatus("current")


class _HpnicfEponUniPortPolicyExtraBurst_Type(Integer32):
    """Custom type hpnicfEponUniPortPolicyExtraBurst based on Integer32"""
    defaultValue = 0


_HpnicfEponUniPortPolicyExtraBurst_Object = MibTableColumn
hpnicfEponUniPortPolicyExtraBurst = _HpnicfEponUniPortPolicyExtraBurst_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 6, 1, 4),
    _HpnicfEponUniPortPolicyExtraBurst_Type()
)
hpnicfEponUniPortPolicyExtraBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponUniPortPolicyExtraBurst.setStatus("current")
_HpnicfEponUniPortPolicyInboundCir_Type = Integer32
_HpnicfEponUniPortPolicyInboundCir_Object = MibTableColumn
hpnicfEponUniPortPolicyInboundCir = _HpnicfEponUniPortPolicyInboundCir_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 6, 1, 5),
    _HpnicfEponUniPortPolicyInboundCir_Type()
)
hpnicfEponUniPortPolicyInboundCir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponUniPortPolicyInboundCir.setStatus("current")


class _HpnicfEponUniPortPolicyInboundBucketDepth_Type(Integer32):
    """Custom type hpnicfEponUniPortPolicyInboundBucketDepth based on Integer32"""
    defaultValue = 0


_HpnicfEponUniPortPolicyInboundBucketDepth_Object = MibTableColumn
hpnicfEponUniPortPolicyInboundBucketDepth = _HpnicfEponUniPortPolicyInboundBucketDepth_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 6, 1, 6),
    _HpnicfEponUniPortPolicyInboundBucketDepth_Type()
)
hpnicfEponUniPortPolicyInboundBucketDepth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponUniPortPolicyInboundBucketDepth.setStatus("current")


class _HpnicfEponUniPortPolicyInboundExtraBurst_Type(Integer32):
    """Custom type hpnicfEponUniPortPolicyInboundExtraBurst based on Integer32"""
    defaultValue = 0


_HpnicfEponUniPortPolicyInboundExtraBurst_Object = MibTableColumn
hpnicfEponUniPortPolicyInboundExtraBurst = _HpnicfEponUniPortPolicyInboundExtraBurst_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 6, 1, 7),
    _HpnicfEponUniPortPolicyInboundExtraBurst_Type()
)
hpnicfEponUniPortPolicyInboundExtraBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponUniPortPolicyInboundExtraBurst.setStatus("current")
_HpnicfEponUniPortPolicyOutboundCir_Type = Integer32
_HpnicfEponUniPortPolicyOutboundCir_Object = MibTableColumn
hpnicfEponUniPortPolicyOutboundCir = _HpnicfEponUniPortPolicyOutboundCir_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 6, 1, 8),
    _HpnicfEponUniPortPolicyOutboundCir_Type()
)
hpnicfEponUniPortPolicyOutboundCir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponUniPortPolicyOutboundCir.setStatus("current")
_HpnicfEponUniPortPolicyOutboundPir_Type = Integer32
_HpnicfEponUniPortPolicyOutboundPir_Object = MibTableColumn
hpnicfEponUniPortPolicyOutboundPir = _HpnicfEponUniPortPolicyOutboundPir_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 6, 1, 9),
    _HpnicfEponUniPortPolicyOutboundPir_Type()
)
hpnicfEponUniPortPolicyOutboundPir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponUniPortPolicyOutboundPir.setStatus("current")
_HpnicfEponUniMulticastTable_Object = MibTable
hpnicfEponUniMulticastTable = _HpnicfEponUniMulticastTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 7)
)
if mibBuilder.loadTexts:
    hpnicfEponUniMulticastTable.setStatus("current")
_HpnicfEponUniMulticastEntry_Object = MibTableRow
hpnicfEponUniMulticastEntry = _HpnicfEponUniMulticastEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 7, 1)
)
hpnicfEponUniMulticastEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-EPON-UNI-MIB", "hpnicfEponUniIndex"),
)
if mibBuilder.loadTexts:
    hpnicfEponUniMulticastEntry.setStatus("current")


class _HpnicfEponUniMulticastGroupNumber_Type(Integer32):
    """Custom type hpnicfEponUniMulticastGroupNumber based on Integer32"""
    defaultValue = 64


_HpnicfEponUniMulticastGroupNumber_Object = MibTableColumn
hpnicfEponUniMulticastGroupNumber = _HpnicfEponUniMulticastGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 7, 1, 1),
    _HpnicfEponUniMulticastGroupNumber_Type()
)
hpnicfEponUniMulticastGroupNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponUniMulticastGroupNumber.setStatus("current")


class _HpnicfEponUniMulticastVlanList_Type(OctetString):
    """Custom type hpnicfEponUniMulticastVlanList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfEponUniMulticastVlanList_Type.__name__ = "OctetString"
_HpnicfEponUniMulticastVlanList_Object = MibTableColumn
hpnicfEponUniMulticastVlanList = _HpnicfEponUniMulticastVlanList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 7, 1, 2),
    _HpnicfEponUniMulticastVlanList_Type()
)
hpnicfEponUniMulticastVlanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponUniMulticastVlanList.setStatus("current")


class _HpnicfEponUniMulticastStripStatus_Type(Integer32):
    """Custom type hpnicfEponUniMulticastStripStatus based on Integer32"""
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


_HpnicfEponUniMulticastStripStatus_Type.__name__ = "Integer32"
_HpnicfEponUniMulticastStripStatus_Object = MibTableColumn
hpnicfEponUniMulticastStripStatus = _HpnicfEponUniMulticastStripStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 7, 1, 3),
    _HpnicfEponUniMulticastStripStatus_Type()
)
hpnicfEponUniMulticastStripStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponUniMulticastStripStatus.setStatus("current")


class _HpnicfEponUniMulticastFastleave_Type(TruthValue):
    """Custom type hpnicfEponUniMulticastFastleave based on TruthValue"""


_HpnicfEponUniMulticastFastleave_Object = MibTableColumn
hpnicfEponUniMulticastFastleave = _HpnicfEponUniMulticastFastleave_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 7, 1, 4),
    _HpnicfEponUniMulticastFastleave_Type()
)
hpnicfEponUniMulticastFastleave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponUniMulticastFastleave.setStatus("current")
_HpnicfEponUniTechAbilityTable_Object = MibTable
hpnicfEponUniTechAbilityTable = _HpnicfEponUniTechAbilityTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 8)
)
if mibBuilder.loadTexts:
    hpnicfEponUniTechAbilityTable.setStatus("current")
_HpnicfEponUniTechAbilityEntry_Object = MibTableRow
hpnicfEponUniTechAbilityEntry = _HpnicfEponUniTechAbilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 8, 1)
)
hpnicfEponUniTechAbilityEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-EPON-UNI-MIB", "hpnicfEponUniIndex"),
)
if mibBuilder.loadTexts:
    hpnicfEponUniTechAbilityEntry.setStatus("current")


class _HpnicfEponUniLocalTechAbility_Type(OctetString):
    """Custom type hpnicfEponUniLocalTechAbility based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfEponUniLocalTechAbility_Type.__name__ = "OctetString"
_HpnicfEponUniLocalTechAbility_Object = MibTableColumn
hpnicfEponUniLocalTechAbility = _HpnicfEponUniLocalTechAbility_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 8, 1, 1),
    _HpnicfEponUniLocalTechAbility_Type()
)
hpnicfEponUniLocalTechAbility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponUniLocalTechAbility.setStatus("current")


class _HpnicfEponUniAdvertisedTechAbility_Type(OctetString):
    """Custom type hpnicfEponUniAdvertisedTechAbility based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfEponUniAdvertisedTechAbility_Type.__name__ = "OctetString"
_HpnicfEponUniAdvertisedTechAbility_Object = MibTableColumn
hpnicfEponUniAdvertisedTechAbility = _HpnicfEponUniAdvertisedTechAbility_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 8, 1, 2),
    _HpnicfEponUniAdvertisedTechAbility_Type()
)
hpnicfEponUniAdvertisedTechAbility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponUniAdvertisedTechAbility.setStatus("current")
_HpnicfEponUniMulticastControlTable_Object = MibTable
hpnicfEponUniMulticastControlTable = _HpnicfEponUniMulticastControlTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 9)
)
if mibBuilder.loadTexts:
    hpnicfEponUniMulticastControlTable.setStatus("current")
_HpnicfEponUniMulticastControlEntry_Object = MibTableRow
hpnicfEponUniMulticastControlEntry = _HpnicfEponUniMulticastControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 9, 1)
)
hpnicfEponUniMulticastControlEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-EPON-UNI-MIB", "hpnicfEponUniIndex"),
    (0, "HPN-ICF-EPON-UNI-MIB", "hpnicfEponUniMulticastIndex"),
)
if mibBuilder.loadTexts:
    hpnicfEponUniMulticastControlEntry.setStatus("current")
_HpnicfEponUniMulticastVlanIndex_Type = Integer32
_HpnicfEponUniMulticastVlanIndex_Object = MibTableColumn
hpnicfEponUniMulticastVlanIndex = _HpnicfEponUniMulticastVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 9, 1, 1),
    _HpnicfEponUniMulticastVlanIndex_Type()
)
hpnicfEponUniMulticastVlanIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfEponUniMulticastVlanIndex.setStatus("current")


class _HpnicfEponUniMulticastAddressList_Type(OctetString):
    """Custom type hpnicfEponUniMulticastAddressList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfEponUniMulticastAddressList_Type.__name__ = "OctetString"
_HpnicfEponUniMulticastAddressList_Object = MibTableColumn
hpnicfEponUniMulticastAddressList = _HpnicfEponUniMulticastAddressList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 9, 1, 2),
    _HpnicfEponUniMulticastAddressList_Type()
)
hpnicfEponUniMulticastAddressList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfEponUniMulticastAddressList.setStatus("current")


class _HpnicfEponUniMulticastAccessRule_Type(Integer32):
    """Custom type hpnicfEponUniMulticastAccessRule based on Integer32"""
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


_HpnicfEponUniMulticastAccessRule_Type.__name__ = "Integer32"
_HpnicfEponUniMulticastAccessRule_Object = MibTableColumn
hpnicfEponUniMulticastAccessRule = _HpnicfEponUniMulticastAccessRule_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 9, 1, 3),
    _HpnicfEponUniMulticastAccessRule_Type()
)
hpnicfEponUniMulticastAccessRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfEponUniMulticastAccessRule.setStatus("current")
_HpnicfEponUniMulticastChannelLimit_Type = Integer32
_HpnicfEponUniMulticastChannelLimit_Object = MibTableColumn
hpnicfEponUniMulticastChannelLimit = _HpnicfEponUniMulticastChannelLimit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 9, 1, 4),
    _HpnicfEponUniMulticastChannelLimit_Type()
)
hpnicfEponUniMulticastChannelLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfEponUniMulticastChannelLimit.setStatus("current")
_HpnicfEponUniMulticastPreTimeSlice_Type = Integer32
_HpnicfEponUniMulticastPreTimeSlice_Object = MibTableColumn
hpnicfEponUniMulticastPreTimeSlice = _HpnicfEponUniMulticastPreTimeSlice_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 9, 1, 5),
    _HpnicfEponUniMulticastPreTimeSlice_Type()
)
hpnicfEponUniMulticastPreTimeSlice.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfEponUniMulticastPreTimeSlice.setStatus("current")
_HpnicfEponUniMulticastPreTimes_Type = Integer32
_HpnicfEponUniMulticastPreTimes_Object = MibTableColumn
hpnicfEponUniMulticastPreTimes = _HpnicfEponUniMulticastPreTimes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 9, 1, 6),
    _HpnicfEponUniMulticastPreTimes_Type()
)
hpnicfEponUniMulticastPreTimes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfEponUniMulticastPreTimes.setStatus("current")
_HpnicfEponUniMulticastPreInterval_Type = Integer32
_HpnicfEponUniMulticastPreInterval_Object = MibTableColumn
hpnicfEponUniMulticastPreInterval = _HpnicfEponUniMulticastPreInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 9, 1, 7),
    _HpnicfEponUniMulticastPreInterval_Type()
)
hpnicfEponUniMulticastPreInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfEponUniMulticastPreInterval.setStatus("current")
_HpnicfEponUniMulticastRowStatus_Type = RowStatus
_HpnicfEponUniMulticastRowStatus_Object = MibTableColumn
hpnicfEponUniMulticastRowStatus = _HpnicfEponUniMulticastRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 9, 1, 8),
    _HpnicfEponUniMulticastRowStatus_Type()
)
hpnicfEponUniMulticastRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfEponUniMulticastRowStatus.setStatus("current")
_HpnicfEponUniMulticastIndex_Type = Integer32
_HpnicfEponUniMulticastIndex_Object = MibTableColumn
hpnicfEponUniMulticastIndex = _HpnicfEponUniMulticastIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 9, 1, 9),
    _HpnicfEponUniMulticastIndex_Type()
)
hpnicfEponUniMulticastIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfEponUniMulticastIndex.setStatus("current")


class _HpnicfEponUniMulticastSourceIpList_Type(OctetString):
    """Custom type hpnicfEponUniMulticastSourceIpList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnicfEponUniMulticastSourceIpList_Type.__name__ = "OctetString"
_HpnicfEponUniMulticastSourceIpList_Object = MibTableColumn
hpnicfEponUniMulticastSourceIpList = _HpnicfEponUniMulticastSourceIpList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 9, 1, 10),
    _HpnicfEponUniMulticastSourceIpList_Type()
)
hpnicfEponUniMulticastSourceIpList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfEponUniMulticastSourceIpList.setStatus("current")
_HpnicfEponUniMulticastResetInterval_Type = Integer32
_HpnicfEponUniMulticastResetInterval_Object = MibTableColumn
hpnicfEponUniMulticastResetInterval = _HpnicfEponUniMulticastResetInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 9, 1, 11),
    _HpnicfEponUniMulticastResetInterval_Type()
)
hpnicfEponUniMulticastResetInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfEponUniMulticastResetInterval.setStatus("current")
_HpnicfEponUniQosIndexNextTable_Object = MibTable
hpnicfEponUniQosIndexNextTable = _HpnicfEponUniQosIndexNextTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 10)
)
if mibBuilder.loadTexts:
    hpnicfEponUniQosIndexNextTable.setStatus("current")
_HpnicfEponUniQosIndexNextEntry_Object = MibTableRow
hpnicfEponUniQosIndexNextEntry = _HpnicfEponUniQosIndexNextEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 10, 1)
)
hpnicfEponUniQosIndexNextEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-EPON-UNI-MIB", "hpnicfEponUniIndex"),
)
if mibBuilder.loadTexts:
    hpnicfEponUniQosIndexNextEntry.setStatus("current")
_HpnicfEponUniQosConfIndexNext_Type = Integer32
_HpnicfEponUniQosConfIndexNext_Object = MibTableColumn
hpnicfEponUniQosConfIndexNext = _HpnicfEponUniQosConfIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 10, 1, 1),
    _HpnicfEponUniQosConfIndexNext_Type()
)
hpnicfEponUniQosConfIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponUniQosConfIndexNext.setStatus("current")
_HpnicfEponUniQosConfTable_Object = MibTable
hpnicfEponUniQosConfTable = _HpnicfEponUniQosConfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 11)
)
if mibBuilder.loadTexts:
    hpnicfEponUniQosConfTable.setStatus("current")
_HpnicfEponUniQosConfEntry_Object = MibTableRow
hpnicfEponUniQosConfEntry = _HpnicfEponUniQosConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 11, 1)
)
hpnicfEponUniQosConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-EPON-UNI-MIB", "hpnicfEponUniIndex"),
    (0, "HPN-ICF-EPON-UNI-MIB", "hpnicfEponUniQosConfIndex"),
)
if mibBuilder.loadTexts:
    hpnicfEponUniQosConfEntry.setStatus("current")
_HpnicfEponUniQosConfIndex_Type = Integer32
_HpnicfEponUniQosConfIndex_Object = MibTableColumn
hpnicfEponUniQosConfIndex = _HpnicfEponUniQosConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 11, 1, 1),
    _HpnicfEponUniQosConfIndex_Type()
)
hpnicfEponUniQosConfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfEponUniQosConfIndex.setStatus("current")
_HpnicfEponUniQosConfRuleIndexNext_Type = Integer32
_HpnicfEponUniQosConfRuleIndexNext_Object = MibTableColumn
hpnicfEponUniQosConfRuleIndexNext = _HpnicfEponUniQosConfRuleIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 11, 1, 2),
    _HpnicfEponUniQosConfRuleIndexNext_Type()
)
hpnicfEponUniQosConfRuleIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponUniQosConfRuleIndexNext.setStatus("current")
_HpnicfEponUniQosConfMappedQueue_Type = Integer32
_HpnicfEponUniQosConfMappedQueue_Object = MibTableColumn
hpnicfEponUniQosConfMappedQueue = _HpnicfEponUniQosConfMappedQueue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 11, 1, 3),
    _HpnicfEponUniQosConfMappedQueue_Type()
)
hpnicfEponUniQosConfMappedQueue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfEponUniQosConfMappedQueue.setStatus("current")
_HpnicfEponUniQosConfMarkedPriority_Type = Integer32
_HpnicfEponUniQosConfMarkedPriority_Object = MibTableColumn
hpnicfEponUniQosConfMarkedPriority = _HpnicfEponUniQosConfMarkedPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 11, 1, 4),
    _HpnicfEponUniQosConfMarkedPriority_Type()
)
hpnicfEponUniQosConfMarkedPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfEponUniQosConfMarkedPriority.setStatus("current")
_HpnicfEponUniQosConfRowStatus_Type = RowStatus
_HpnicfEponUniQosConfRowStatus_Object = MibTableColumn
hpnicfEponUniQosConfRowStatus = _HpnicfEponUniQosConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 11, 1, 5),
    _HpnicfEponUniQosConfRowStatus_Type()
)
hpnicfEponUniQosConfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfEponUniQosConfRowStatus.setStatus("current")
_HpnicfEponUniQosRuleTable_Object = MibTable
hpnicfEponUniQosRuleTable = _HpnicfEponUniQosRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 12)
)
if mibBuilder.loadTexts:
    hpnicfEponUniQosRuleTable.setStatus("current")
_HpnicfEponUniQosRuleEntry_Object = MibTableRow
hpnicfEponUniQosRuleEntry = _HpnicfEponUniQosRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 12, 1)
)
hpnicfEponUniQosRuleEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-EPON-UNI-MIB", "hpnicfEponUniIndex"),
    (0, "HPN-ICF-EPON-UNI-MIB", "hpnicfEponUniQosConfIndex"),
    (0, "HPN-ICF-EPON-UNI-MIB", "hpnicfEponUniQosRuleIndex"),
)
if mibBuilder.loadTexts:
    hpnicfEponUniQosRuleEntry.setStatus("current")


class _HpnicfEponUniQosRuleIndex_Type(Integer32):
    """Custom type hpnicfEponUniQosRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HpnicfEponUniQosRuleIndex_Type.__name__ = "Integer32"
_HpnicfEponUniQosRuleIndex_Object = MibTableColumn
hpnicfEponUniQosRuleIndex = _HpnicfEponUniQosRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 12, 1, 1),
    _HpnicfEponUniQosRuleIndex_Type()
)
hpnicfEponUniQosRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfEponUniQosRuleIndex.setStatus("current")


class _HpnicfEponUniQosRuleSelector_Type(Integer32):
    """Custom type hpnicfEponUniQosRuleSelector based on Integer32"""
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


_HpnicfEponUniQosRuleSelector_Type.__name__ = "Integer32"
_HpnicfEponUniQosRuleSelector_Object = MibTableColumn
hpnicfEponUniQosRuleSelector = _HpnicfEponUniQosRuleSelector_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 12, 1, 2),
    _HpnicfEponUniQosRuleSelector_Type()
)
hpnicfEponUniQosRuleSelector.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfEponUniQosRuleSelector.setStatus("current")
_HpnicfEponUniQosRuleValue_Type = Integer32
_HpnicfEponUniQosRuleValue_Object = MibTableColumn
hpnicfEponUniQosRuleValue = _HpnicfEponUniQosRuleValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 12, 1, 3),
    _HpnicfEponUniQosRuleValue_Type()
)
hpnicfEponUniQosRuleValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfEponUniQosRuleValue.setStatus("current")
_HpnicfEponUniQosRuleMacAddress_Type = MacAddress
_HpnicfEponUniQosRuleMacAddress_Object = MibTableColumn
hpnicfEponUniQosRuleMacAddress = _HpnicfEponUniQosRuleMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 12, 1, 4),
    _HpnicfEponUniQosRuleMacAddress_Type()
)
hpnicfEponUniQosRuleMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfEponUniQosRuleMacAddress.setStatus("current")


class _HpnicfEponUniQosRuleOperator_Type(Integer32):
    """Custom type hpnicfEponUniQosRuleOperator based on Integer32"""
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


_HpnicfEponUniQosRuleOperator_Type.__name__ = "Integer32"
_HpnicfEponUniQosRuleOperator_Object = MibTableColumn
hpnicfEponUniQosRuleOperator = _HpnicfEponUniQosRuleOperator_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 12, 1, 5),
    _HpnicfEponUniQosRuleOperator_Type()
)
hpnicfEponUniQosRuleOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfEponUniQosRuleOperator.setStatus("current")
_HpnicfEponUniQosRuleRowStatus_Type = RowStatus
_HpnicfEponUniQosRuleRowStatus_Object = MibTableColumn
hpnicfEponUniQosRuleRowStatus = _HpnicfEponUniQosRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 12, 1, 6),
    _HpnicfEponUniQosRuleRowStatus_Type()
)
hpnicfEponUniQosRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfEponUniQosRuleRowStatus.setStatus("current")
_HpnicfEponUniMirrorGroupTable_Object = MibTable
hpnicfEponUniMirrorGroupTable = _HpnicfEponUniMirrorGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 13)
)
if mibBuilder.loadTexts:
    hpnicfEponUniMirrorGroupTable.setStatus("current")
_HpnicfEponUniMirrorGroupEntry_Object = MibTableRow
hpnicfEponUniMirrorGroupEntry = _HpnicfEponUniMirrorGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 13, 1)
)
hpnicfEponUniMirrorGroupEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-EPON-UNI-MIB", "hpnicfEponUniMirrorGroupID"),
)
if mibBuilder.loadTexts:
    hpnicfEponUniMirrorGroupEntry.setStatus("current")
_HpnicfEponUniMirrorGroupID_Type = Integer32
_HpnicfEponUniMirrorGroupID_Object = MibTableColumn
hpnicfEponUniMirrorGroupID = _HpnicfEponUniMirrorGroupID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 13, 1, 1),
    _HpnicfEponUniMirrorGroupID_Type()
)
hpnicfEponUniMirrorGroupID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfEponUniMirrorGroupID.setStatus("current")
_HpnicfEponUniMirrorInboundPortList_Type = OctetString
_HpnicfEponUniMirrorInboundPortList_Object = MibTableColumn
hpnicfEponUniMirrorInboundPortList = _HpnicfEponUniMirrorInboundPortList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 13, 1, 2),
    _HpnicfEponUniMirrorInboundPortList_Type()
)
hpnicfEponUniMirrorInboundPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEponUniMirrorInboundPortList.setStatus("current")
_HpnicfEponUniMirrorOutboundPortList_Type = OctetString
_HpnicfEponUniMirrorOutboundPortList_Object = MibTableColumn
hpnicfEponUniMirrorOutboundPortList = _HpnicfEponUniMirrorOutboundPortList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 13, 1, 3),
    _HpnicfEponUniMirrorOutboundPortList_Type()
)
hpnicfEponUniMirrorOutboundPortList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfEponUniMirrorOutboundPortList.setStatus("current")
_HpnicfEponUniMonitorPort_Type = Integer32
_HpnicfEponUniMonitorPort_Object = MibTableColumn
hpnicfEponUniMonitorPort = _HpnicfEponUniMonitorPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 13, 1, 4),
    _HpnicfEponUniMonitorPort_Type()
)
hpnicfEponUniMonitorPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfEponUniMonitorPort.setStatus("current")
_HpnicfEponUniMirrorRowStatus_Type = RowStatus
_HpnicfEponUniMirrorRowStatus_Object = MibTableColumn
hpnicfEponUniMirrorRowStatus = _HpnicfEponUniMirrorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 13, 1, 5),
    _HpnicfEponUniMirrorRowStatus_Type()
)
hpnicfEponUniMirrorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfEponUniMirrorRowStatus.setStatus("current")
_HpnicfEponUniMirrorGroupIdNextTable_Object = MibTable
hpnicfEponUniMirrorGroupIdNextTable = _HpnicfEponUniMirrorGroupIdNextTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 14)
)
if mibBuilder.loadTexts:
    hpnicfEponUniMirrorGroupIdNextTable.setStatus("current")
_HpnicfEponUniMirrorGroupIdNextEntry_Object = MibTableRow
hpnicfEponUniMirrorGroupIdNextEntry = _HpnicfEponUniMirrorGroupIdNextEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 14, 1)
)
hpnicfEponUniMirrorGroupIdNextEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfEponUniMirrorGroupIdNextEntry.setStatus("current")
_HpnicfEponUniMirrorGroupIDNext_Type = Integer32
_HpnicfEponUniMirrorGroupIDNext_Object = MibTableColumn
hpnicfEponUniMirrorGroupIDNext = _HpnicfEponUniMirrorGroupIDNext_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 14, 1, 1),
    _HpnicfEponUniMirrorGroupIDNext_Type()
)
hpnicfEponUniMirrorGroupIDNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponUniMirrorGroupIDNext.setStatus("current")
_HpnicfEponUniMulticastCtrlInfoTable_Object = MibTable
hpnicfEponUniMulticastCtrlInfoTable = _HpnicfEponUniMulticastCtrlInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 15)
)
if mibBuilder.loadTexts:
    hpnicfEponUniMulticastCtrlInfoTable.setStatus("current")
_HpnicfEponUniMulticastCtrlInfoEntry_Object = MibTableRow
hpnicfEponUniMulticastCtrlInfoEntry = _HpnicfEponUniMulticastCtrlInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 15, 1)
)
hpnicfEponUniMulticastCtrlInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-EPON-UNI-MIB", "hpnicfEponUniIndex"),
    (0, "HPN-ICF-EPON-UNI-MIB", "hpnicfEponUniMultActVlan"),
    (0, "HPN-ICF-EPON-UNI-MIB", "hpnicfEponUniMultActAddress"),
)
if mibBuilder.loadTexts:
    hpnicfEponUniMulticastCtrlInfoEntry.setStatus("current")
_HpnicfEponUniMultActVlan_Type = Integer32
_HpnicfEponUniMultActVlan_Object = MibTableColumn
hpnicfEponUniMultActVlan = _HpnicfEponUniMultActVlan_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 15, 1, 1),
    _HpnicfEponUniMultActVlan_Type()
)
hpnicfEponUniMultActVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfEponUniMultActVlan.setStatus("current")
_HpnicfEponUniMultActAddress_Type = IpAddress
_HpnicfEponUniMultActAddress_Object = MibTableColumn
hpnicfEponUniMultActAddress = _HpnicfEponUniMultActAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 15, 1, 2),
    _HpnicfEponUniMultActAddress_Type()
)
hpnicfEponUniMultActAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfEponUniMultActAddress.setStatus("current")


class _HpnicfEponUniMultActAccessRule_Type(Integer32):
    """Custom type hpnicfEponUniMultActAccessRule based on Integer32"""
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


_HpnicfEponUniMultActAccessRule_Type.__name__ = "Integer32"
_HpnicfEponUniMultActAccessRule_Object = MibTableColumn
hpnicfEponUniMultActAccessRule = _HpnicfEponUniMultActAccessRule_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 15, 1, 3),
    _HpnicfEponUniMultActAccessRule_Type()
)
hpnicfEponUniMultActAccessRule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponUniMultActAccessRule.setStatus("current")
_HpnicfEponUniMultActPreTimes_Type = Integer32
_HpnicfEponUniMultActPreTimes_Object = MibTableColumn
hpnicfEponUniMultActPreTimes = _HpnicfEponUniMultActPreTimes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 15, 1, 4),
    _HpnicfEponUniMultActPreTimes_Type()
)
hpnicfEponUniMultActPreTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponUniMultActPreTimes.setStatus("current")
_HpnicfEponUniMultActPreRemain_Type = Integer32
_HpnicfEponUniMultActPreRemain_Object = MibTableColumn
hpnicfEponUniMultActPreRemain = _HpnicfEponUniMultActPreRemain_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 15, 1, 5),
    _HpnicfEponUniMultActPreRemain_Type()
)
hpnicfEponUniMultActPreRemain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponUniMultActPreRemain.setStatus("current")
_HpnicfEponUniMulticastIndexNextTable_Object = MibTable
hpnicfEponUniMulticastIndexNextTable = _HpnicfEponUniMulticastIndexNextTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 16)
)
if mibBuilder.loadTexts:
    hpnicfEponUniMulticastIndexNextTable.setStatus("current")
_HpnicfEponUniMulticastIndexNextEntry_Object = MibTableRow
hpnicfEponUniMulticastIndexNextEntry = _HpnicfEponUniMulticastIndexNextEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 16, 1)
)
hpnicfEponUniMulticastIndexNextEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-EPON-UNI-MIB", "hpnicfEponUniIndex"),
)
if mibBuilder.loadTexts:
    hpnicfEponUniMulticastIndexNextEntry.setStatus("current")
_HpnicfEponUniMulticastConfIndexNext_Type = Integer32
_HpnicfEponUniMulticastConfIndexNext_Object = MibTableColumn
hpnicfEponUniMulticastConfIndexNext = _HpnicfEponUniMulticastConfIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 1, 16, 1, 1),
    _HpnicfEponUniMulticastConfIndexNext_Type()
)
hpnicfEponUniMulticastConfIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEponUniMulticastConfIndexNext.setStatus("current")
_HpnicfEponUniTrap_ObjectIdentity = ObjectIdentity
hpnicfEponUniTrap = _HpnicfEponUniTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 2)
)
_HpnicfEponUniTrapPrefix_ObjectIdentity = ObjectIdentity
hpnicfEponUniTrapPrefix = _HpnicfEponUniTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 2, 0)
)

# Managed Objects groups


# Notification objects

hpnicfEponUniLinkUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 2, 0, 1)
)
hpnicfEponUniLinkUpTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HPN-ICF-EPON-UNI-MIB", "hpnicfEponUniIndex"),
        ("HPN-ICF-EPON-UNI-MIB", "hpnicfEponUniDescr"),
        ("HPN-ICF-EPON-UNI-MIB", "hpnicfEponUniAdminStatus"))
)
if mibBuilder.loadTexts:
    hpnicfEponUniLinkUpTrap.setStatus(
        "current"
    )

hpnicfEponUniLinkDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 2, 0, 2)
)
hpnicfEponUniLinkDownTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HPN-ICF-EPON-UNI-MIB", "hpnicfEponUniIndex"),
        ("HPN-ICF-EPON-UNI-MIB", "hpnicfEponUniDescr"),
        ("HPN-ICF-EPON-UNI-MIB", "hpnicfEponUniAdminStatus"))
)
if mibBuilder.loadTexts:
    hpnicfEponUniLinkDownTrap.setStatus(
        "current"
    )

hpnicfEponUniLoopBackDetectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 2, 0, 3)
)
hpnicfEponUniLoopBackDetectedTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HPN-ICF-EPON-UNI-MIB", "hpnicfEponUniIndex"),
        ("HPN-ICF-EPON-UNI-MIB", "hpnicfEponUniDescr"),
        ("HPN-ICF-EPON-UNI-MIB", "hpnicfEponUniVlan"))
)
if mibBuilder.loadTexts:
    hpnicfEponUniLoopBackDetectedTrap.setStatus(
        "current"
    )

hpnicfEponUniLoopBackRecoveredTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 42, 5, 2, 0, 4)
)
hpnicfEponUniLoopBackRecoveredTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HPN-ICF-EPON-UNI-MIB", "hpnicfEponUniIndex"),
        ("HPN-ICF-EPON-UNI-MIB", "hpnicfEponUniDescr"),
        ("HPN-ICF-EPON-UNI-MIB", "hpnicfEponUniVlan"))
)
if mibBuilder.loadTexts:
    hpnicfEponUniLoopBackRecoveredTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-EPON-UNI-MIB",
    **{"hpnicfEponUni": hpnicfEponUni,
       "hpnicfEponUniSysMan": hpnicfEponUniSysMan,
       "hpnicfEponUniSysManTable": hpnicfEponUniSysManTable,
       "hpnicfEponUniSysManEntry": hpnicfEponUniSysManEntry,
       "hpnicfEponUniIndex": hpnicfEponUniIndex,
       "hpnicfEponUniDescr": hpnicfEponUniDescr,
       "hpnicfEponUniAdminStatus": hpnicfEponUniAdminStatus,
       "hpnicfEponUniMdi": hpnicfEponUniMdi,
       "hpnicfEponUniPriority": hpnicfEponUniPriority,
       "hpnicfEponUniVlanType": hpnicfEponUniVlanType,
       "hpnicfEponUniAccessVlan": hpnicfEponUniAccessVlan,
       "hpnicfEponUniTrunkPvid": hpnicfEponUniTrunkPvid,
       "hpnicfEponUniVLANTrunkAllowListLow": hpnicfEponUniVLANTrunkAllowListLow,
       "hpnicfEponUniVLANTrunkAllowListHigh": hpnicfEponUniVLANTrunkAllowListHigh,
       "hpnicfEponUniInboundLineRate": hpnicfEponUniInboundLineRate,
       "hpnicfEponUniOutboundLineRate": hpnicfEponUniOutboundLineRate,
       "hpnicfEponUniFlowControl": hpnicfEponUniFlowControl,
       "hpnicfEponUniSpeed": hpnicfEponUniSpeed,
       "hpnicfEponUniDuplex": hpnicfEponUniDuplex,
       "hpnicfEponUniVlanVPNStatus": hpnicfEponUniVlanVPNStatus,
       "hpnicfEponUniCountReset": hpnicfEponUniCountReset,
       "hpnicfEponUniPortIsolate": hpnicfEponUniPortIsolate,
       "hpnicfEponUniVlanConfiguration": hpnicfEponUniVlanConfiguration,
       "hpnicfEponUniAutoNegotiation": hpnicfEponUniAutoNegotiation,
       "hpnicfEponUniRestartAutoNeg": hpnicfEponUniRestartAutoNeg,
       "hpnicfEponUniLinkStatus": hpnicfEponUniLinkStatus,
       "hpnicfEponUniInterfaceType": hpnicfEponUniInterfaceType,
       "hpnicfEponUniVitualCableTest": hpnicfEponUniVitualCableTest,
       "hpnicfEponUniVCTCableStatus": hpnicfEponUniVCTCableStatus,
       "hpnicfEponUniVCTCableLength": hpnicfEponUniVCTCableLength,
       "hpnicfEponUniVCTImpedanceMismatch": hpnicfEponUniVCTImpedanceMismatch,
       "hpnicfEponUniVCTPairSkew": hpnicfEponUniVCTPairSkew,
       "hpnicfEponUniVCTPairSwap": hpnicfEponUniVCTPairSwap,
       "hpnicfEponUniVCTPolaritySwap": hpnicfEponUniVCTPolaritySwap,
       "hpnicfEponUniVCTInsertionLoss": hpnicfEponUniVCTInsertionLoss,
       "hpnicfEponUniVCTReturnLoss": hpnicfEponUniVCTReturnLoss,
       "hpnicfEponUniVCTNearendCrosstalk": hpnicfEponUniVCTNearendCrosstalk,
       "hpnicfEponUniVlan": hpnicfEponUniVlan,
       "hpnicfEponUniCountTable": hpnicfEponUniCountTable,
       "hpnicfEponUniCountEntry": hpnicfEponUniCountEntry,
       "hpnicfEponUniInStatsPkts": hpnicfEponUniInStatsPkts,
       "hpnicfEponUniInStatsUnicastPkts": hpnicfEponUniInStatsUnicastPkts,
       "hpnicfEponUniInStatsBroadcastPkts": hpnicfEponUniInStatsBroadcastPkts,
       "hpnicfEponUniInStatsMulticastPkts": hpnicfEponUniInStatsMulticastPkts,
       "hpnicfEponUniInPausePkts": hpnicfEponUniInPausePkts,
       "hpnicfEponUniInTotalErrors": hpnicfEponUniInTotalErrors,
       "hpnicfEponUniInStatsCRCAlignErrors": hpnicfEponUniInStatsCRCAlignErrors,
       "hpnicfEponUniInStatsUndersizePkts": hpnicfEponUniInStatsUndersizePkts,
       "hpnicfEponUniInStatsOversizePkts": hpnicfEponUniInStatsOversizePkts,
       "hpnicfEponUniInErrorbyOther": hpnicfEponUniInErrorbyOther,
       "hpnicfEponUniOutStatsPkts": hpnicfEponUniOutStatsPkts,
       "hpnicfEponUniOutStatsUnicastPkts": hpnicfEponUniOutStatsUnicastPkts,
       "hpnicfEponUniOutStatsBroadcastPkts": hpnicfEponUniOutStatsBroadcastPkts,
       "hpnicfEponUniOutStatsMulticastPkts": hpnicfEponUniOutStatsMulticastPkts,
       "hpnicfEponUniOutStatsPausePkts": hpnicfEponUniOutStatsPausePkts,
       "hpnicfEponUniOutTotalErrors": hpnicfEponUniOutTotalErrors,
       "hpnicfEponUniOutStatsCollisions": hpnicfEponUniOutStatsCollisions,
       "hpnicfEponUniOutDelayExceededDiscards": hpnicfEponUniOutDelayExceededDiscards,
       "hpnicfEponUniOutErrorbyOther": hpnicfEponUniOutErrorbyOther,
       "hpnicfEponUniOutDroppedFrames": hpnicfEponUniOutDroppedFrames,
       "hpnicfEponUniIgmpInfoTable": hpnicfEponUniIgmpInfoTable,
       "hpnicfEponUniIgmpInfoEntry": hpnicfEponUniIgmpInfoEntry,
       "hpnicfEponUniMacIndex": hpnicfEponUniMacIndex,
       "hpnicfEponUniIgmpMacAddress": hpnicfEponUniIgmpMacAddress,
       "hpnicfEponUniIgmpVlanId": hpnicfEponUniIgmpVlanId,
       "hpnicfEponUniParaMan": hpnicfEponUniParaMan,
       "hpnicfEponUniLineRateMax": hpnicfEponUniLineRateMax,
       "hpnicfEponUniLineRateStep": hpnicfEponUniLineRateStep,
       "hpnicfEponUniNumberOnOnu": hpnicfEponUniNumberOnOnu,
       "hpnicfEponUniScalarGroup": hpnicfEponUniScalarGroup,
       "hpnicfEponUniPortPolicyTable": hpnicfEponUniPortPolicyTable,
       "hpnicfEponUniPortPolicyEntry": hpnicfEponUniPortPolicyEntry,
       "hpnicfEponUniPortPolicyStatus": hpnicfEponUniPortPolicyStatus,
       "hpnicfEponUniPortPolicyCir": hpnicfEponUniPortPolicyCir,
       "hpnicfEponUniPortPolicyBucketDepth": hpnicfEponUniPortPolicyBucketDepth,
       "hpnicfEponUniPortPolicyExtraBurst": hpnicfEponUniPortPolicyExtraBurst,
       "hpnicfEponUniPortPolicyInboundCir": hpnicfEponUniPortPolicyInboundCir,
       "hpnicfEponUniPortPolicyInboundBucketDepth": hpnicfEponUniPortPolicyInboundBucketDepth,
       "hpnicfEponUniPortPolicyInboundExtraBurst": hpnicfEponUniPortPolicyInboundExtraBurst,
       "hpnicfEponUniPortPolicyOutboundCir": hpnicfEponUniPortPolicyOutboundCir,
       "hpnicfEponUniPortPolicyOutboundPir": hpnicfEponUniPortPolicyOutboundPir,
       "hpnicfEponUniMulticastTable": hpnicfEponUniMulticastTable,
       "hpnicfEponUniMulticastEntry": hpnicfEponUniMulticastEntry,
       "hpnicfEponUniMulticastGroupNumber": hpnicfEponUniMulticastGroupNumber,
       "hpnicfEponUniMulticastVlanList": hpnicfEponUniMulticastVlanList,
       "hpnicfEponUniMulticastStripStatus": hpnicfEponUniMulticastStripStatus,
       "hpnicfEponUniMulticastFastleave": hpnicfEponUniMulticastFastleave,
       "hpnicfEponUniTechAbilityTable": hpnicfEponUniTechAbilityTable,
       "hpnicfEponUniTechAbilityEntry": hpnicfEponUniTechAbilityEntry,
       "hpnicfEponUniLocalTechAbility": hpnicfEponUniLocalTechAbility,
       "hpnicfEponUniAdvertisedTechAbility": hpnicfEponUniAdvertisedTechAbility,
       "hpnicfEponUniMulticastControlTable": hpnicfEponUniMulticastControlTable,
       "hpnicfEponUniMulticastControlEntry": hpnicfEponUniMulticastControlEntry,
       "hpnicfEponUniMulticastVlanIndex": hpnicfEponUniMulticastVlanIndex,
       "hpnicfEponUniMulticastAddressList": hpnicfEponUniMulticastAddressList,
       "hpnicfEponUniMulticastAccessRule": hpnicfEponUniMulticastAccessRule,
       "hpnicfEponUniMulticastChannelLimit": hpnicfEponUniMulticastChannelLimit,
       "hpnicfEponUniMulticastPreTimeSlice": hpnicfEponUniMulticastPreTimeSlice,
       "hpnicfEponUniMulticastPreTimes": hpnicfEponUniMulticastPreTimes,
       "hpnicfEponUniMulticastPreInterval": hpnicfEponUniMulticastPreInterval,
       "hpnicfEponUniMulticastRowStatus": hpnicfEponUniMulticastRowStatus,
       "hpnicfEponUniMulticastIndex": hpnicfEponUniMulticastIndex,
       "hpnicfEponUniMulticastSourceIpList": hpnicfEponUniMulticastSourceIpList,
       "hpnicfEponUniMulticastResetInterval": hpnicfEponUniMulticastResetInterval,
       "hpnicfEponUniQosIndexNextTable": hpnicfEponUniQosIndexNextTable,
       "hpnicfEponUniQosIndexNextEntry": hpnicfEponUniQosIndexNextEntry,
       "hpnicfEponUniQosConfIndexNext": hpnicfEponUniQosConfIndexNext,
       "hpnicfEponUniQosConfTable": hpnicfEponUniQosConfTable,
       "hpnicfEponUniQosConfEntry": hpnicfEponUniQosConfEntry,
       "hpnicfEponUniQosConfIndex": hpnicfEponUniQosConfIndex,
       "hpnicfEponUniQosConfRuleIndexNext": hpnicfEponUniQosConfRuleIndexNext,
       "hpnicfEponUniQosConfMappedQueue": hpnicfEponUniQosConfMappedQueue,
       "hpnicfEponUniQosConfMarkedPriority": hpnicfEponUniQosConfMarkedPriority,
       "hpnicfEponUniQosConfRowStatus": hpnicfEponUniQosConfRowStatus,
       "hpnicfEponUniQosRuleTable": hpnicfEponUniQosRuleTable,
       "hpnicfEponUniQosRuleEntry": hpnicfEponUniQosRuleEntry,
       "hpnicfEponUniQosRuleIndex": hpnicfEponUniQosRuleIndex,
       "hpnicfEponUniQosRuleSelector": hpnicfEponUniQosRuleSelector,
       "hpnicfEponUniQosRuleValue": hpnicfEponUniQosRuleValue,
       "hpnicfEponUniQosRuleMacAddress": hpnicfEponUniQosRuleMacAddress,
       "hpnicfEponUniQosRuleOperator": hpnicfEponUniQosRuleOperator,
       "hpnicfEponUniQosRuleRowStatus": hpnicfEponUniQosRuleRowStatus,
       "hpnicfEponUniMirrorGroupTable": hpnicfEponUniMirrorGroupTable,
       "hpnicfEponUniMirrorGroupEntry": hpnicfEponUniMirrorGroupEntry,
       "hpnicfEponUniMirrorGroupID": hpnicfEponUniMirrorGroupID,
       "hpnicfEponUniMirrorInboundPortList": hpnicfEponUniMirrorInboundPortList,
       "hpnicfEponUniMirrorOutboundPortList": hpnicfEponUniMirrorOutboundPortList,
       "hpnicfEponUniMonitorPort": hpnicfEponUniMonitorPort,
       "hpnicfEponUniMirrorRowStatus": hpnicfEponUniMirrorRowStatus,
       "hpnicfEponUniMirrorGroupIdNextTable": hpnicfEponUniMirrorGroupIdNextTable,
       "hpnicfEponUniMirrorGroupIdNextEntry": hpnicfEponUniMirrorGroupIdNextEntry,
       "hpnicfEponUniMirrorGroupIDNext": hpnicfEponUniMirrorGroupIDNext,
       "hpnicfEponUniMulticastCtrlInfoTable": hpnicfEponUniMulticastCtrlInfoTable,
       "hpnicfEponUniMulticastCtrlInfoEntry": hpnicfEponUniMulticastCtrlInfoEntry,
       "hpnicfEponUniMultActVlan": hpnicfEponUniMultActVlan,
       "hpnicfEponUniMultActAddress": hpnicfEponUniMultActAddress,
       "hpnicfEponUniMultActAccessRule": hpnicfEponUniMultActAccessRule,
       "hpnicfEponUniMultActPreTimes": hpnicfEponUniMultActPreTimes,
       "hpnicfEponUniMultActPreRemain": hpnicfEponUniMultActPreRemain,
       "hpnicfEponUniMulticastIndexNextTable": hpnicfEponUniMulticastIndexNextTable,
       "hpnicfEponUniMulticastIndexNextEntry": hpnicfEponUniMulticastIndexNextEntry,
       "hpnicfEponUniMulticastConfIndexNext": hpnicfEponUniMulticastConfIndexNext,
       "hpnicfEponUniTrap": hpnicfEponUniTrap,
       "hpnicfEponUniTrapPrefix": hpnicfEponUniTrapPrefix,
       "hpnicfEponUniLinkUpTrap": hpnicfEponUniLinkUpTrap,
       "hpnicfEponUniLinkDownTrap": hpnicfEponUniLinkDownTrap,
       "hpnicfEponUniLoopBackDetectedTrap": hpnicfEponUniLoopBackDetectedTrap,
       "hpnicfEponUniLoopBackRecoveredTrap": hpnicfEponUniLoopBackRecoveredTrap}
)
