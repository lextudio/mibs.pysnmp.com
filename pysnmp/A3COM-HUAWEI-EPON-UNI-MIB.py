# SNMP MIB module (A3COM-HUAWEI-EPON-UNI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-EPON-UNI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:27:55 2024
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

(h3cEpon,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "h3cEpon")

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

h3cEponUni = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cEponUniSysMan_ObjectIdentity = ObjectIdentity
h3cEponUniSysMan = _H3cEponUniSysMan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1)
)
_H3cEponUniSysManTable_Object = MibTable
h3cEponUniSysManTable = _H3cEponUniSysManTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 1)
)
if mibBuilder.loadTexts:
    h3cEponUniSysManTable.setStatus("current")
_H3cEponUniSysManEntry_Object = MibTableRow
h3cEponUniSysManEntry = _H3cEponUniSysManEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 1, 1)
)
h3cEponUniSysManEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "A3COM-HUAWEI-EPON-UNI-MIB", "h3cEponUniIndex"),
)
if mibBuilder.loadTexts:
    h3cEponUniSysManEntry.setStatus("current")
_H3cEponUniIndex_Type = Integer32
_H3cEponUniIndex_Object = MibTableColumn
h3cEponUniIndex = _H3cEponUniIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 1, 1, 1),
    _H3cEponUniIndex_Type()
)
h3cEponUniIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cEponUniIndex.setStatus("current")
_H3cEponUniDescr_Type = OctetString
_H3cEponUniDescr_Object = MibTableColumn
h3cEponUniDescr = _H3cEponUniDescr_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 1, 1, 2),
    _H3cEponUniDescr_Type()
)
h3cEponUniDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponUniDescr.setStatus("current")


class _H3cEponUniAdminStatus_Type(Integer32):
    """Custom type h3cEponUniAdminStatus based on Integer32"""
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


_H3cEponUniAdminStatus_Type.__name__ = "Integer32"
_H3cEponUniAdminStatus_Object = MibTableColumn
h3cEponUniAdminStatus = _H3cEponUniAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 1, 1, 3),
    _H3cEponUniAdminStatus_Type()
)
h3cEponUniAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEponUniAdminStatus.setStatus("current")


class _H3cEponUniMdi_Type(Integer32):
    """Custom type h3cEponUniMdi based on Integer32"""
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


_H3cEponUniMdi_Type.__name__ = "Integer32"
_H3cEponUniMdi_Object = MibTableColumn
h3cEponUniMdi = _H3cEponUniMdi_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 1, 1, 4),
    _H3cEponUniMdi_Type()
)
h3cEponUniMdi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEponUniMdi.setStatus("current")


class _H3cEponUniPriority_Type(Integer32):
    """Custom type h3cEponUniPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_H3cEponUniPriority_Type.__name__ = "Integer32"
_H3cEponUniPriority_Object = MibTableColumn
h3cEponUniPriority = _H3cEponUniPriority_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 1, 1, 5),
    _H3cEponUniPriority_Type()
)
h3cEponUniPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEponUniPriority.setStatus("current")


class _H3cEponUniVlanType_Type(Integer32):
    """Custom type h3cEponUniVlanType based on Integer32"""
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


_H3cEponUniVlanType_Type.__name__ = "Integer32"
_H3cEponUniVlanType_Object = MibTableColumn
h3cEponUniVlanType = _H3cEponUniVlanType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 1, 1, 6),
    _H3cEponUniVlanType_Type()
)
h3cEponUniVlanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEponUniVlanType.setStatus("current")


class _H3cEponUniAccessVlan_Type(Integer32):
    """Custom type h3cEponUniAccessVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_H3cEponUniAccessVlan_Type.__name__ = "Integer32"
_H3cEponUniAccessVlan_Object = MibTableColumn
h3cEponUniAccessVlan = _H3cEponUniAccessVlan_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 1, 1, 7),
    _H3cEponUniAccessVlan_Type()
)
h3cEponUniAccessVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEponUniAccessVlan.setStatus("current")


class _H3cEponUniTrunkPvid_Type(Integer32):
    """Custom type h3cEponUniTrunkPvid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_H3cEponUniTrunkPvid_Type.__name__ = "Integer32"
_H3cEponUniTrunkPvid_Object = MibTableColumn
h3cEponUniTrunkPvid = _H3cEponUniTrunkPvid_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 1, 1, 8),
    _H3cEponUniTrunkPvid_Type()
)
h3cEponUniTrunkPvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEponUniTrunkPvid.setStatus("current")
_H3cEponUniVLANTrunkAllowListLow_Type = OctetString
_H3cEponUniVLANTrunkAllowListLow_Object = MibTableColumn
h3cEponUniVLANTrunkAllowListLow = _H3cEponUniVLANTrunkAllowListLow_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 1, 1, 9),
    _H3cEponUniVLANTrunkAllowListLow_Type()
)
h3cEponUniVLANTrunkAllowListLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEponUniVLANTrunkAllowListLow.setStatus("current")
_H3cEponUniVLANTrunkAllowListHigh_Type = OctetString
_H3cEponUniVLANTrunkAllowListHigh_Object = MibTableColumn
h3cEponUniVLANTrunkAllowListHigh = _H3cEponUniVLANTrunkAllowListHigh_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 1, 1, 10),
    _H3cEponUniVLANTrunkAllowListHigh_Type()
)
h3cEponUniVLANTrunkAllowListHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEponUniVLANTrunkAllowListHigh.setStatus("current")
_H3cEponUniInboundLineRate_Type = Integer32
_H3cEponUniInboundLineRate_Object = MibTableColumn
h3cEponUniInboundLineRate = _H3cEponUniInboundLineRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 1, 1, 11),
    _H3cEponUniInboundLineRate_Type()
)
h3cEponUniInboundLineRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEponUniInboundLineRate.setStatus("current")
_H3cEponUniOutboundLineRate_Type = Integer32
_H3cEponUniOutboundLineRate_Object = MibTableColumn
h3cEponUniOutboundLineRate = _H3cEponUniOutboundLineRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 1, 1, 12),
    _H3cEponUniOutboundLineRate_Type()
)
h3cEponUniOutboundLineRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEponUniOutboundLineRate.setStatus("current")
_H3cEponUniFlowControl_Type = TruthValue
_H3cEponUniFlowControl_Object = MibTableColumn
h3cEponUniFlowControl = _H3cEponUniFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 1, 1, 13),
    _H3cEponUniFlowControl_Type()
)
h3cEponUniFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEponUniFlowControl.setStatus("current")


class _H3cEponUniSpeed_Type(Integer32):
    """Custom type h3cEponUniSpeed based on Integer32"""
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


_H3cEponUniSpeed_Type.__name__ = "Integer32"
_H3cEponUniSpeed_Object = MibTableColumn
h3cEponUniSpeed = _H3cEponUniSpeed_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 1, 1, 14),
    _H3cEponUniSpeed_Type()
)
h3cEponUniSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEponUniSpeed.setStatus("current")


class _H3cEponUniDuplex_Type(Integer32):
    """Custom type h3cEponUniDuplex based on Integer32"""
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


_H3cEponUniDuplex_Type.__name__ = "Integer32"
_H3cEponUniDuplex_Object = MibTableColumn
h3cEponUniDuplex = _H3cEponUniDuplex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 1, 1, 15),
    _H3cEponUniDuplex_Type()
)
h3cEponUniDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEponUniDuplex.setStatus("current")
_H3cEponUniVlanVPNStatus_Type = TruthValue
_H3cEponUniVlanVPNStatus_Object = MibTableColumn
h3cEponUniVlanVPNStatus = _H3cEponUniVlanVPNStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 1, 1, 16),
    _H3cEponUniVlanVPNStatus_Type()
)
h3cEponUniVlanVPNStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEponUniVlanVPNStatus.setStatus("current")


class _H3cEponUniCountReset_Type(Integer32):
    """Custom type h3cEponUniCountReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_H3cEponUniCountReset_Type.__name__ = "Integer32"
_H3cEponUniCountReset_Object = MibTableColumn
h3cEponUniCountReset = _H3cEponUniCountReset_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 1, 1, 17),
    _H3cEponUniCountReset_Type()
)
h3cEponUniCountReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEponUniCountReset.setStatus("current")


class _H3cEponUniPortIsolate_Type(Integer32):
    """Custom type h3cEponUniPortIsolate based on Integer32"""
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


_H3cEponUniPortIsolate_Type.__name__ = "Integer32"
_H3cEponUniPortIsolate_Object = MibTableColumn
h3cEponUniPortIsolate = _H3cEponUniPortIsolate_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 1, 1, 18),
    _H3cEponUniPortIsolate_Type()
)
h3cEponUniPortIsolate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEponUniPortIsolate.setStatus("current")


class _H3cEponUniVlanConfiguration_Type(OctetString):
    """Custom type h3cEponUniVlanConfiguration based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3cEponUniVlanConfiguration_Type.__name__ = "OctetString"
_H3cEponUniVlanConfiguration_Object = MibTableColumn
h3cEponUniVlanConfiguration = _H3cEponUniVlanConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 1, 1, 23),
    _H3cEponUniVlanConfiguration_Type()
)
h3cEponUniVlanConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEponUniVlanConfiguration.setStatus("current")


class _H3cEponUniAutoNegotiation_Type(Integer32):
    """Custom type h3cEponUniAutoNegotiation based on Integer32"""
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


_H3cEponUniAutoNegotiation_Type.__name__ = "Integer32"
_H3cEponUniAutoNegotiation_Object = MibTableColumn
h3cEponUniAutoNegotiation = _H3cEponUniAutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 1, 1, 25),
    _H3cEponUniAutoNegotiation_Type()
)
h3cEponUniAutoNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEponUniAutoNegotiation.setStatus("current")


class _H3cEponUniRestartAutoNeg_Type(Integer32):
    """Custom type h3cEponUniRestartAutoNeg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("autoNegotiation", 1)
    )


_H3cEponUniRestartAutoNeg_Type.__name__ = "Integer32"
_H3cEponUniRestartAutoNeg_Object = MibTableColumn
h3cEponUniRestartAutoNeg = _H3cEponUniRestartAutoNeg_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 1, 1, 26),
    _H3cEponUniRestartAutoNeg_Type()
)
h3cEponUniRestartAutoNeg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEponUniRestartAutoNeg.setStatus("current")


class _H3cEponUniLinkStatus_Type(Integer32):
    """Custom type h3cEponUniLinkStatus based on Integer32"""
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


_H3cEponUniLinkStatus_Type.__name__ = "Integer32"
_H3cEponUniLinkStatus_Object = MibTableColumn
h3cEponUniLinkStatus = _H3cEponUniLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 1, 1, 29),
    _H3cEponUniLinkStatus_Type()
)
h3cEponUniLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponUniLinkStatus.setStatus("current")


class _H3cEponUniInterfaceType_Type(Integer32):
    """Custom type h3cEponUniInterfaceType based on Integer32"""
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


_H3cEponUniInterfaceType_Type.__name__ = "Integer32"
_H3cEponUniInterfaceType_Object = MibTableColumn
h3cEponUniInterfaceType = _H3cEponUniInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 1, 1, 30),
    _H3cEponUniInterfaceType_Type()
)
h3cEponUniInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponUniInterfaceType.setStatus("current")


class _H3cEponUniVitualCableTest_Type(Integer32):
    """Custom type h3cEponUniVitualCableTest based on Integer32"""
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


_H3cEponUniVitualCableTest_Type.__name__ = "Integer32"
_H3cEponUniVitualCableTest_Object = MibTableColumn
h3cEponUniVitualCableTest = _H3cEponUniVitualCableTest_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 1, 1, 31),
    _H3cEponUniVitualCableTest_Type()
)
h3cEponUniVitualCableTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEponUniVitualCableTest.setStatus("current")


class _H3cEponUniVCTCableStatus_Type(Integer32):
    """Custom type h3cEponUniVCTCableStatus based on Integer32"""
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


_H3cEponUniVCTCableStatus_Type.__name__ = "Integer32"
_H3cEponUniVCTCableStatus_Object = MibTableColumn
h3cEponUniVCTCableStatus = _H3cEponUniVCTCableStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 1, 1, 32),
    _H3cEponUniVCTCableStatus_Type()
)
h3cEponUniVCTCableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponUniVCTCableStatus.setStatus("current")
_H3cEponUniVCTCableLength_Type = Integer32
_H3cEponUniVCTCableLength_Object = MibTableColumn
h3cEponUniVCTCableLength = _H3cEponUniVCTCableLength_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 1, 1, 33),
    _H3cEponUniVCTCableLength_Type()
)
h3cEponUniVCTCableLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponUniVCTCableLength.setStatus("current")


class _H3cEponUniVCTImpedanceMismatch_Type(Integer32):
    """Custom type h3cEponUniVCTImpedanceMismatch based on Integer32"""
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


_H3cEponUniVCTImpedanceMismatch_Type.__name__ = "Integer32"
_H3cEponUniVCTImpedanceMismatch_Object = MibTableColumn
h3cEponUniVCTImpedanceMismatch = _H3cEponUniVCTImpedanceMismatch_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 1, 1, 34),
    _H3cEponUniVCTImpedanceMismatch_Type()
)
h3cEponUniVCTImpedanceMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponUniVCTImpedanceMismatch.setStatus("current")
_H3cEponUniVCTPairSkew_Type = Integer32
_H3cEponUniVCTPairSkew_Object = MibTableColumn
h3cEponUniVCTPairSkew = _H3cEponUniVCTPairSkew_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 1, 1, 35),
    _H3cEponUniVCTPairSkew_Type()
)
h3cEponUniVCTPairSkew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponUniVCTPairSkew.setStatus("current")


class _H3cEponUniVCTPairSwap_Type(Integer32):
    """Custom type h3cEponUniVCTPairSwap based on Integer32"""
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


_H3cEponUniVCTPairSwap_Type.__name__ = "Integer32"
_H3cEponUniVCTPairSwap_Object = MibTableColumn
h3cEponUniVCTPairSwap = _H3cEponUniVCTPairSwap_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 1, 1, 36),
    _H3cEponUniVCTPairSwap_Type()
)
h3cEponUniVCTPairSwap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponUniVCTPairSwap.setStatus("current")


class _H3cEponUniVCTPolaritySwap_Type(Integer32):
    """Custom type h3cEponUniVCTPolaritySwap based on Integer32"""
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


_H3cEponUniVCTPolaritySwap_Type.__name__ = "Integer32"
_H3cEponUniVCTPolaritySwap_Object = MibTableColumn
h3cEponUniVCTPolaritySwap = _H3cEponUniVCTPolaritySwap_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 1, 1, 37),
    _H3cEponUniVCTPolaritySwap_Type()
)
h3cEponUniVCTPolaritySwap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponUniVCTPolaritySwap.setStatus("current")
_H3cEponUniVCTInsertionLoss_Type = Integer32
_H3cEponUniVCTInsertionLoss_Object = MibTableColumn
h3cEponUniVCTInsertionLoss = _H3cEponUniVCTInsertionLoss_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 1, 1, 38),
    _H3cEponUniVCTInsertionLoss_Type()
)
h3cEponUniVCTInsertionLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponUniVCTInsertionLoss.setStatus("current")
_H3cEponUniVCTReturnLoss_Type = Integer32
_H3cEponUniVCTReturnLoss_Object = MibTableColumn
h3cEponUniVCTReturnLoss = _H3cEponUniVCTReturnLoss_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 1, 1, 39),
    _H3cEponUniVCTReturnLoss_Type()
)
h3cEponUniVCTReturnLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponUniVCTReturnLoss.setStatus("current")
_H3cEponUniVCTNearendCrosstalk_Type = Integer32
_H3cEponUniVCTNearendCrosstalk_Object = MibTableColumn
h3cEponUniVCTNearendCrosstalk = _H3cEponUniVCTNearendCrosstalk_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 1, 1, 40),
    _H3cEponUniVCTNearendCrosstalk_Type()
)
h3cEponUniVCTNearendCrosstalk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponUniVCTNearendCrosstalk.setStatus("current")
_H3cEponUniCountTable_Object = MibTable
h3cEponUniCountTable = _H3cEponUniCountTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 2)
)
if mibBuilder.loadTexts:
    h3cEponUniCountTable.setStatus("current")
_H3cEponUniCountEntry_Object = MibTableRow
h3cEponUniCountEntry = _H3cEponUniCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 2, 1)
)
h3cEponUniCountEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "A3COM-HUAWEI-EPON-UNI-MIB", "h3cEponUniIndex"),
)
if mibBuilder.loadTexts:
    h3cEponUniCountEntry.setStatus("current")
_H3cEponUniInStatsPkts_Type = Unsigned32
_H3cEponUniInStatsPkts_Object = MibTableColumn
h3cEponUniInStatsPkts = _H3cEponUniInStatsPkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 2, 1, 1),
    _H3cEponUniInStatsPkts_Type()
)
h3cEponUniInStatsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponUniInStatsPkts.setStatus("current")
_H3cEponUniInStatsUnicastPkts_Type = Unsigned32
_H3cEponUniInStatsUnicastPkts_Object = MibTableColumn
h3cEponUniInStatsUnicastPkts = _H3cEponUniInStatsUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 2, 1, 2),
    _H3cEponUniInStatsUnicastPkts_Type()
)
h3cEponUniInStatsUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponUniInStatsUnicastPkts.setStatus("current")
_H3cEponUniInStatsBroadcastPkts_Type = Unsigned32
_H3cEponUniInStatsBroadcastPkts_Object = MibTableColumn
h3cEponUniInStatsBroadcastPkts = _H3cEponUniInStatsBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 2, 1, 3),
    _H3cEponUniInStatsBroadcastPkts_Type()
)
h3cEponUniInStatsBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponUniInStatsBroadcastPkts.setStatus("current")
_H3cEponUniInStatsMulticastPkts_Type = Unsigned32
_H3cEponUniInStatsMulticastPkts_Object = MibTableColumn
h3cEponUniInStatsMulticastPkts = _H3cEponUniInStatsMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 2, 1, 4),
    _H3cEponUniInStatsMulticastPkts_Type()
)
h3cEponUniInStatsMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponUniInStatsMulticastPkts.setStatus("current")
_H3cEponUniInPausePkts_Type = Unsigned32
_H3cEponUniInPausePkts_Object = MibTableColumn
h3cEponUniInPausePkts = _H3cEponUniInPausePkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 2, 1, 5),
    _H3cEponUniInPausePkts_Type()
)
h3cEponUniInPausePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponUniInPausePkts.setStatus("current")
_H3cEponUniInTotalErrors_Type = Unsigned32
_H3cEponUniInTotalErrors_Object = MibTableColumn
h3cEponUniInTotalErrors = _H3cEponUniInTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 2, 1, 6),
    _H3cEponUniInTotalErrors_Type()
)
h3cEponUniInTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponUniInTotalErrors.setStatus("current")
_H3cEponUniInStatsCRCAlignErrors_Type = Unsigned32
_H3cEponUniInStatsCRCAlignErrors_Object = MibTableColumn
h3cEponUniInStatsCRCAlignErrors = _H3cEponUniInStatsCRCAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 2, 1, 7),
    _H3cEponUniInStatsCRCAlignErrors_Type()
)
h3cEponUniInStatsCRCAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponUniInStatsCRCAlignErrors.setStatus("current")
_H3cEponUniInStatsUndersizePkts_Type = Unsigned32
_H3cEponUniInStatsUndersizePkts_Object = MibTableColumn
h3cEponUniInStatsUndersizePkts = _H3cEponUniInStatsUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 2, 1, 8),
    _H3cEponUniInStatsUndersizePkts_Type()
)
h3cEponUniInStatsUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponUniInStatsUndersizePkts.setStatus("current")
_H3cEponUniInStatsOversizePkts_Type = Unsigned32
_H3cEponUniInStatsOversizePkts_Object = MibTableColumn
h3cEponUniInStatsOversizePkts = _H3cEponUniInStatsOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 2, 1, 9),
    _H3cEponUniInStatsOversizePkts_Type()
)
h3cEponUniInStatsOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponUniInStatsOversizePkts.setStatus("current")
_H3cEponUniInErrorbyOther_Type = Unsigned32
_H3cEponUniInErrorbyOther_Object = MibTableColumn
h3cEponUniInErrorbyOther = _H3cEponUniInErrorbyOther_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 2, 1, 10),
    _H3cEponUniInErrorbyOther_Type()
)
h3cEponUniInErrorbyOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponUniInErrorbyOther.setStatus("current")
_H3cEponUniOutStatsPkts_Type = Unsigned32
_H3cEponUniOutStatsPkts_Object = MibTableColumn
h3cEponUniOutStatsPkts = _H3cEponUniOutStatsPkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 2, 1, 11),
    _H3cEponUniOutStatsPkts_Type()
)
h3cEponUniOutStatsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponUniOutStatsPkts.setStatus("current")
_H3cEponUniOutStatsUnicastPkts_Type = Unsigned32
_H3cEponUniOutStatsUnicastPkts_Object = MibTableColumn
h3cEponUniOutStatsUnicastPkts = _H3cEponUniOutStatsUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 2, 1, 12),
    _H3cEponUniOutStatsUnicastPkts_Type()
)
h3cEponUniOutStatsUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponUniOutStatsUnicastPkts.setStatus("current")
_H3cEponUniOutStatsBroadcastPkts_Type = Unsigned32
_H3cEponUniOutStatsBroadcastPkts_Object = MibTableColumn
h3cEponUniOutStatsBroadcastPkts = _H3cEponUniOutStatsBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 2, 1, 13),
    _H3cEponUniOutStatsBroadcastPkts_Type()
)
h3cEponUniOutStatsBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponUniOutStatsBroadcastPkts.setStatus("current")
_H3cEponUniOutStatsMulticastPkts_Type = Unsigned32
_H3cEponUniOutStatsMulticastPkts_Object = MibTableColumn
h3cEponUniOutStatsMulticastPkts = _H3cEponUniOutStatsMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 2, 1, 14),
    _H3cEponUniOutStatsMulticastPkts_Type()
)
h3cEponUniOutStatsMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponUniOutStatsMulticastPkts.setStatus("current")
_H3cEponUniOutStatsPausePkts_Type = Unsigned32
_H3cEponUniOutStatsPausePkts_Object = MibTableColumn
h3cEponUniOutStatsPausePkts = _H3cEponUniOutStatsPausePkts_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 2, 1, 15),
    _H3cEponUniOutStatsPausePkts_Type()
)
h3cEponUniOutStatsPausePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponUniOutStatsPausePkts.setStatus("current")
_H3cEponUniOutTotalErrors_Type = Unsigned32
_H3cEponUniOutTotalErrors_Object = MibTableColumn
h3cEponUniOutTotalErrors = _H3cEponUniOutTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 2, 1, 16),
    _H3cEponUniOutTotalErrors_Type()
)
h3cEponUniOutTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponUniOutTotalErrors.setStatus("current")
_H3cEponUniOutStatsCollisions_Type = Unsigned32
_H3cEponUniOutStatsCollisions_Object = MibTableColumn
h3cEponUniOutStatsCollisions = _H3cEponUniOutStatsCollisions_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 2, 1, 17),
    _H3cEponUniOutStatsCollisions_Type()
)
h3cEponUniOutStatsCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponUniOutStatsCollisions.setStatus("current")
_H3cEponUniOutDelayExceededDiscards_Type = Unsigned32
_H3cEponUniOutDelayExceededDiscards_Object = MibTableColumn
h3cEponUniOutDelayExceededDiscards = _H3cEponUniOutDelayExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 2, 1, 18),
    _H3cEponUniOutDelayExceededDiscards_Type()
)
h3cEponUniOutDelayExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponUniOutDelayExceededDiscards.setStatus("current")
_H3cEponUniOutErrorbyOther_Type = Unsigned32
_H3cEponUniOutErrorbyOther_Object = MibTableColumn
h3cEponUniOutErrorbyOther = _H3cEponUniOutErrorbyOther_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 2, 1, 19),
    _H3cEponUniOutErrorbyOther_Type()
)
h3cEponUniOutErrorbyOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponUniOutErrorbyOther.setStatus("current")
_H3cEponUniOutDroppedFrames_Type = Unsigned32
_H3cEponUniOutDroppedFrames_Object = MibTableColumn
h3cEponUniOutDroppedFrames = _H3cEponUniOutDroppedFrames_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 2, 1, 20),
    _H3cEponUniOutDroppedFrames_Type()
)
h3cEponUniOutDroppedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponUniOutDroppedFrames.setStatus("current")
_H3cEponUniIgmpInfoTable_Object = MibTable
h3cEponUniIgmpInfoTable = _H3cEponUniIgmpInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 3)
)
if mibBuilder.loadTexts:
    h3cEponUniIgmpInfoTable.setStatus("current")
_H3cEponUniIgmpInfoEntry_Object = MibTableRow
h3cEponUniIgmpInfoEntry = _H3cEponUniIgmpInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 3, 1)
)
h3cEponUniIgmpInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "A3COM-HUAWEI-EPON-UNI-MIB", "h3cEponUniIndex"),
    (0, "A3COM-HUAWEI-EPON-UNI-MIB", "h3cEponUniMacIndex"),
)
if mibBuilder.loadTexts:
    h3cEponUniIgmpInfoEntry.setStatus("current")
_H3cEponUniMacIndex_Type = Integer32
_H3cEponUniMacIndex_Object = MibTableColumn
h3cEponUniMacIndex = _H3cEponUniMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 3, 1, 1),
    _H3cEponUniMacIndex_Type()
)
h3cEponUniMacIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cEponUniMacIndex.setStatus("current")
_H3cEponUniIgmpMacAddress_Type = MacAddress
_H3cEponUniIgmpMacAddress_Object = MibTableColumn
h3cEponUniIgmpMacAddress = _H3cEponUniIgmpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 3, 1, 2),
    _H3cEponUniIgmpMacAddress_Type()
)
h3cEponUniIgmpMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponUniIgmpMacAddress.setStatus("current")


class _H3cEponUniIgmpVlanId_Type(Integer32):
    """Custom type h3cEponUniIgmpVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_H3cEponUniIgmpVlanId_Type.__name__ = "Integer32"
_H3cEponUniIgmpVlanId_Object = MibTableColumn
h3cEponUniIgmpVlanId = _H3cEponUniIgmpVlanId_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 3, 1, 3),
    _H3cEponUniIgmpVlanId_Type()
)
h3cEponUniIgmpVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponUniIgmpVlanId.setStatus("current")
_H3cEponUniParaMan_ObjectIdentity = ObjectIdentity
h3cEponUniParaMan = _H3cEponUniParaMan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 4)
)
_H3cEponUniLineRateMax_Type = Integer32
_H3cEponUniLineRateMax_Object = MibScalar
h3cEponUniLineRateMax = _H3cEponUniLineRateMax_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 4, 1),
    _H3cEponUniLineRateMax_Type()
)
h3cEponUniLineRateMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponUniLineRateMax.setStatus("current")
_H3cEponUniLineRateStep_Type = Integer32
_H3cEponUniLineRateStep_Object = MibScalar
h3cEponUniLineRateStep = _H3cEponUniLineRateStep_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 4, 2),
    _H3cEponUniLineRateStep_Type()
)
h3cEponUniLineRateStep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponUniLineRateStep.setStatus("current")
_H3cEponUniNumberOnOnu_Type = Integer32
_H3cEponUniNumberOnOnu_Object = MibScalar
h3cEponUniNumberOnOnu = _H3cEponUniNumberOnOnu_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 4, 3),
    _H3cEponUniNumberOnOnu_Type()
)
h3cEponUniNumberOnOnu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponUniNumberOnOnu.setStatus("current")
_H3cEponUniScalarGroup_ObjectIdentity = ObjectIdentity
h3cEponUniScalarGroup = _H3cEponUniScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 5)
)
_H3cEponUniPortPolicyTable_Object = MibTable
h3cEponUniPortPolicyTable = _H3cEponUniPortPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 6)
)
if mibBuilder.loadTexts:
    h3cEponUniPortPolicyTable.setStatus("current")
_H3cEponUniPortPolicyEntry_Object = MibTableRow
h3cEponUniPortPolicyEntry = _H3cEponUniPortPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 6, 1)
)
h3cEponUniPortPolicyEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "A3COM-HUAWEI-EPON-UNI-MIB", "h3cEponUniIndex"),
)
if mibBuilder.loadTexts:
    h3cEponUniPortPolicyEntry.setStatus("current")


class _H3cEponUniPortPolicyStatus_Type(Integer32):
    """Custom type h3cEponUniPortPolicyStatus based on Integer32"""
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


_H3cEponUniPortPolicyStatus_Type.__name__ = "Integer32"
_H3cEponUniPortPolicyStatus_Object = MibTableColumn
h3cEponUniPortPolicyStatus = _H3cEponUniPortPolicyStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 6, 1, 1),
    _H3cEponUniPortPolicyStatus_Type()
)
h3cEponUniPortPolicyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEponUniPortPolicyStatus.setStatus("current")


class _H3cEponUniPortPolicyCir_Type(Integer32):
    """Custom type h3cEponUniPortPolicyCir based on Integer32"""
    defaultValue = 102400


_H3cEponUniPortPolicyCir_Object = MibTableColumn
h3cEponUniPortPolicyCir = _H3cEponUniPortPolicyCir_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 6, 1, 2),
    _H3cEponUniPortPolicyCir_Type()
)
h3cEponUniPortPolicyCir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEponUniPortPolicyCir.setStatus("current")


class _H3cEponUniPortPolicyBucketDepth_Type(Integer32):
    """Custom type h3cEponUniPortPolicyBucketDepth based on Integer32"""
    defaultValue = 0


_H3cEponUniPortPolicyBucketDepth_Object = MibTableColumn
h3cEponUniPortPolicyBucketDepth = _H3cEponUniPortPolicyBucketDepth_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 6, 1, 3),
    _H3cEponUniPortPolicyBucketDepth_Type()
)
h3cEponUniPortPolicyBucketDepth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEponUniPortPolicyBucketDepth.setStatus("current")


class _H3cEponUniPortPolicyExtraBurst_Type(Integer32):
    """Custom type h3cEponUniPortPolicyExtraBurst based on Integer32"""
    defaultValue = 0


_H3cEponUniPortPolicyExtraBurst_Object = MibTableColumn
h3cEponUniPortPolicyExtraBurst = _H3cEponUniPortPolicyExtraBurst_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 6, 1, 4),
    _H3cEponUniPortPolicyExtraBurst_Type()
)
h3cEponUniPortPolicyExtraBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEponUniPortPolicyExtraBurst.setStatus("current")
_H3cEponUniPortPolicyInboundCir_Type = Integer32
_H3cEponUniPortPolicyInboundCir_Object = MibTableColumn
h3cEponUniPortPolicyInboundCir = _H3cEponUniPortPolicyInboundCir_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 6, 1, 5),
    _H3cEponUniPortPolicyInboundCir_Type()
)
h3cEponUniPortPolicyInboundCir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEponUniPortPolicyInboundCir.setStatus("current")


class _H3cEponUniPortPolicyInboundBucketDepth_Type(Integer32):
    """Custom type h3cEponUniPortPolicyInboundBucketDepth based on Integer32"""
    defaultValue = 0


_H3cEponUniPortPolicyInboundBucketDepth_Object = MibTableColumn
h3cEponUniPortPolicyInboundBucketDepth = _H3cEponUniPortPolicyInboundBucketDepth_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 6, 1, 6),
    _H3cEponUniPortPolicyInboundBucketDepth_Type()
)
h3cEponUniPortPolicyInboundBucketDepth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEponUniPortPolicyInboundBucketDepth.setStatus("current")


class _H3cEponUniPortPolicyInboundExtraBurst_Type(Integer32):
    """Custom type h3cEponUniPortPolicyInboundExtraBurst based on Integer32"""
    defaultValue = 0


_H3cEponUniPortPolicyInboundExtraBurst_Object = MibTableColumn
h3cEponUniPortPolicyInboundExtraBurst = _H3cEponUniPortPolicyInboundExtraBurst_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 6, 1, 7),
    _H3cEponUniPortPolicyInboundExtraBurst_Type()
)
h3cEponUniPortPolicyInboundExtraBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEponUniPortPolicyInboundExtraBurst.setStatus("current")
_H3cEponUniPortPolicyOutboundCir_Type = Integer32
_H3cEponUniPortPolicyOutboundCir_Object = MibTableColumn
h3cEponUniPortPolicyOutboundCir = _H3cEponUniPortPolicyOutboundCir_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 6, 1, 8),
    _H3cEponUniPortPolicyOutboundCir_Type()
)
h3cEponUniPortPolicyOutboundCir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEponUniPortPolicyOutboundCir.setStatus("current")
_H3cEponUniPortPolicyOutboundPir_Type = Integer32
_H3cEponUniPortPolicyOutboundPir_Object = MibTableColumn
h3cEponUniPortPolicyOutboundPir = _H3cEponUniPortPolicyOutboundPir_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 6, 1, 9),
    _H3cEponUniPortPolicyOutboundPir_Type()
)
h3cEponUniPortPolicyOutboundPir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEponUniPortPolicyOutboundPir.setStatus("current")
_H3cEponUniMulticastTable_Object = MibTable
h3cEponUniMulticastTable = _H3cEponUniMulticastTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 7)
)
if mibBuilder.loadTexts:
    h3cEponUniMulticastTable.setStatus("current")
_H3cEponUniMulticastEntry_Object = MibTableRow
h3cEponUniMulticastEntry = _H3cEponUniMulticastEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 7, 1)
)
h3cEponUniMulticastEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "A3COM-HUAWEI-EPON-UNI-MIB", "h3cEponUniIndex"),
)
if mibBuilder.loadTexts:
    h3cEponUniMulticastEntry.setStatus("current")


class _H3cEponUniMulticastGroupNumber_Type(Integer32):
    """Custom type h3cEponUniMulticastGroupNumber based on Integer32"""
    defaultValue = 64


_H3cEponUniMulticastGroupNumber_Object = MibTableColumn
h3cEponUniMulticastGroupNumber = _H3cEponUniMulticastGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 7, 1, 1),
    _H3cEponUniMulticastGroupNumber_Type()
)
h3cEponUniMulticastGroupNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEponUniMulticastGroupNumber.setStatus("current")


class _H3cEponUniMulticastVlanList_Type(OctetString):
    """Custom type h3cEponUniMulticastVlanList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3cEponUniMulticastVlanList_Type.__name__ = "OctetString"
_H3cEponUniMulticastVlanList_Object = MibTableColumn
h3cEponUniMulticastVlanList = _H3cEponUniMulticastVlanList_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 7, 1, 2),
    _H3cEponUniMulticastVlanList_Type()
)
h3cEponUniMulticastVlanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEponUniMulticastVlanList.setStatus("current")


class _H3cEponUniMulticastStripStatus_Type(Integer32):
    """Custom type h3cEponUniMulticastStripStatus based on Integer32"""
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


_H3cEponUniMulticastStripStatus_Type.__name__ = "Integer32"
_H3cEponUniMulticastStripStatus_Object = MibTableColumn
h3cEponUniMulticastStripStatus = _H3cEponUniMulticastStripStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 7, 1, 3),
    _H3cEponUniMulticastStripStatus_Type()
)
h3cEponUniMulticastStripStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEponUniMulticastStripStatus.setStatus("current")


class _H3cEponUniMulticastFastleave_Type(TruthValue):
    """Custom type h3cEponUniMulticastFastleave based on TruthValue"""


_H3cEponUniMulticastFastleave_Object = MibTableColumn
h3cEponUniMulticastFastleave = _H3cEponUniMulticastFastleave_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 7, 1, 4),
    _H3cEponUniMulticastFastleave_Type()
)
h3cEponUniMulticastFastleave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEponUniMulticastFastleave.setStatus("current")
_H3cEponUniTechAbilityTable_Object = MibTable
h3cEponUniTechAbilityTable = _H3cEponUniTechAbilityTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 8)
)
if mibBuilder.loadTexts:
    h3cEponUniTechAbilityTable.setStatus("current")
_H3cEponUniTechAbilityEntry_Object = MibTableRow
h3cEponUniTechAbilityEntry = _H3cEponUniTechAbilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 8, 1)
)
h3cEponUniTechAbilityEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "A3COM-HUAWEI-EPON-UNI-MIB", "h3cEponUniIndex"),
)
if mibBuilder.loadTexts:
    h3cEponUniTechAbilityEntry.setStatus("current")


class _H3cEponUniLocalTechAbility_Type(OctetString):
    """Custom type h3cEponUniLocalTechAbility based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3cEponUniLocalTechAbility_Type.__name__ = "OctetString"
_H3cEponUniLocalTechAbility_Object = MibTableColumn
h3cEponUniLocalTechAbility = _H3cEponUniLocalTechAbility_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 8, 1, 1),
    _H3cEponUniLocalTechAbility_Type()
)
h3cEponUniLocalTechAbility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponUniLocalTechAbility.setStatus("current")


class _H3cEponUniAdvertisedTechAbility_Type(OctetString):
    """Custom type h3cEponUniAdvertisedTechAbility based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3cEponUniAdvertisedTechAbility_Type.__name__ = "OctetString"
_H3cEponUniAdvertisedTechAbility_Object = MibTableColumn
h3cEponUniAdvertisedTechAbility = _H3cEponUniAdvertisedTechAbility_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 8, 1, 2),
    _H3cEponUniAdvertisedTechAbility_Type()
)
h3cEponUniAdvertisedTechAbility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponUniAdvertisedTechAbility.setStatus("current")
_H3cEponUniMulticastControlTable_Object = MibTable
h3cEponUniMulticastControlTable = _H3cEponUniMulticastControlTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 9)
)
if mibBuilder.loadTexts:
    h3cEponUniMulticastControlTable.setStatus("current")
_H3cEponUniMulticastControlEntry_Object = MibTableRow
h3cEponUniMulticastControlEntry = _H3cEponUniMulticastControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 9, 1)
)
h3cEponUniMulticastControlEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "A3COM-HUAWEI-EPON-UNI-MIB", "h3cEponUniIndex"),
    (0, "A3COM-HUAWEI-EPON-UNI-MIB", "h3cEponUniMulticastIndex"),
)
if mibBuilder.loadTexts:
    h3cEponUniMulticastControlEntry.setStatus("current")
_H3cEponUniMulticastVlanIndex_Type = Integer32
_H3cEponUniMulticastVlanIndex_Object = MibTableColumn
h3cEponUniMulticastVlanIndex = _H3cEponUniMulticastVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 9, 1, 1),
    _H3cEponUniMulticastVlanIndex_Type()
)
h3cEponUniMulticastVlanIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cEponUniMulticastVlanIndex.setStatus("current")


class _H3cEponUniMulticastAddressList_Type(OctetString):
    """Custom type h3cEponUniMulticastAddressList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3cEponUniMulticastAddressList_Type.__name__ = "OctetString"
_H3cEponUniMulticastAddressList_Object = MibTableColumn
h3cEponUniMulticastAddressList = _H3cEponUniMulticastAddressList_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 9, 1, 2),
    _H3cEponUniMulticastAddressList_Type()
)
h3cEponUniMulticastAddressList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cEponUniMulticastAddressList.setStatus("current")


class _H3cEponUniMulticastAccessRule_Type(Integer32):
    """Custom type h3cEponUniMulticastAccessRule based on Integer32"""
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


_H3cEponUniMulticastAccessRule_Type.__name__ = "Integer32"
_H3cEponUniMulticastAccessRule_Object = MibTableColumn
h3cEponUniMulticastAccessRule = _H3cEponUniMulticastAccessRule_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 9, 1, 3),
    _H3cEponUniMulticastAccessRule_Type()
)
h3cEponUniMulticastAccessRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cEponUniMulticastAccessRule.setStatus("current")
_H3cEponUniMulticastChannelLimit_Type = Integer32
_H3cEponUniMulticastChannelLimit_Object = MibTableColumn
h3cEponUniMulticastChannelLimit = _H3cEponUniMulticastChannelLimit_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 9, 1, 4),
    _H3cEponUniMulticastChannelLimit_Type()
)
h3cEponUniMulticastChannelLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cEponUniMulticastChannelLimit.setStatus("current")
_H3cEponUniMulticastPreTimeSlice_Type = Integer32
_H3cEponUniMulticastPreTimeSlice_Object = MibTableColumn
h3cEponUniMulticastPreTimeSlice = _H3cEponUniMulticastPreTimeSlice_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 9, 1, 5),
    _H3cEponUniMulticastPreTimeSlice_Type()
)
h3cEponUniMulticastPreTimeSlice.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cEponUniMulticastPreTimeSlice.setStatus("current")
_H3cEponUniMulticastPreTimes_Type = Integer32
_H3cEponUniMulticastPreTimes_Object = MibTableColumn
h3cEponUniMulticastPreTimes = _H3cEponUniMulticastPreTimes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 9, 1, 6),
    _H3cEponUniMulticastPreTimes_Type()
)
h3cEponUniMulticastPreTimes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cEponUniMulticastPreTimes.setStatus("current")
_H3cEponUniMulticastPreInterval_Type = Integer32
_H3cEponUniMulticastPreInterval_Object = MibTableColumn
h3cEponUniMulticastPreInterval = _H3cEponUniMulticastPreInterval_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 9, 1, 7),
    _H3cEponUniMulticastPreInterval_Type()
)
h3cEponUniMulticastPreInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cEponUniMulticastPreInterval.setStatus("current")
_H3cEponUniMulticastRowStatus_Type = RowStatus
_H3cEponUniMulticastRowStatus_Object = MibTableColumn
h3cEponUniMulticastRowStatus = _H3cEponUniMulticastRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 9, 1, 8),
    _H3cEponUniMulticastRowStatus_Type()
)
h3cEponUniMulticastRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cEponUniMulticastRowStatus.setStatus("current")
_H3cEponUniMulticastIndex_Type = Integer32
_H3cEponUniMulticastIndex_Object = MibTableColumn
h3cEponUniMulticastIndex = _H3cEponUniMulticastIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 9, 1, 9),
    _H3cEponUniMulticastIndex_Type()
)
h3cEponUniMulticastIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cEponUniMulticastIndex.setStatus("current")


class _H3cEponUniMulticastSourceIpList_Type(OctetString):
    """Custom type h3cEponUniMulticastSourceIpList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3cEponUniMulticastSourceIpList_Type.__name__ = "OctetString"
_H3cEponUniMulticastSourceIpList_Object = MibTableColumn
h3cEponUniMulticastSourceIpList = _H3cEponUniMulticastSourceIpList_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 9, 1, 10),
    _H3cEponUniMulticastSourceIpList_Type()
)
h3cEponUniMulticastSourceIpList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cEponUniMulticastSourceIpList.setStatus("current")
_H3cEponUniMulticastResetInterval_Type = Integer32
_H3cEponUniMulticastResetInterval_Object = MibTableColumn
h3cEponUniMulticastResetInterval = _H3cEponUniMulticastResetInterval_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 9, 1, 11),
    _H3cEponUniMulticastResetInterval_Type()
)
h3cEponUniMulticastResetInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cEponUniMulticastResetInterval.setStatus("current")
_H3cEponUniQosIndexNextTable_Object = MibTable
h3cEponUniQosIndexNextTable = _H3cEponUniQosIndexNextTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 10)
)
if mibBuilder.loadTexts:
    h3cEponUniQosIndexNextTable.setStatus("current")
_H3cEponUniQosIndexNextEntry_Object = MibTableRow
h3cEponUniQosIndexNextEntry = _H3cEponUniQosIndexNextEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 10, 1)
)
h3cEponUniQosIndexNextEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "A3COM-HUAWEI-EPON-UNI-MIB", "h3cEponUniIndex"),
)
if mibBuilder.loadTexts:
    h3cEponUniQosIndexNextEntry.setStatus("current")
_H3cEponUniQosConfIndexNext_Type = Integer32
_H3cEponUniQosConfIndexNext_Object = MibTableColumn
h3cEponUniQosConfIndexNext = _H3cEponUniQosConfIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 10, 1, 1),
    _H3cEponUniQosConfIndexNext_Type()
)
h3cEponUniQosConfIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponUniQosConfIndexNext.setStatus("current")
_H3cEponUniQosConfTable_Object = MibTable
h3cEponUniQosConfTable = _H3cEponUniQosConfTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 11)
)
if mibBuilder.loadTexts:
    h3cEponUniQosConfTable.setStatus("current")
_H3cEponUniQosConfEntry_Object = MibTableRow
h3cEponUniQosConfEntry = _H3cEponUniQosConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 11, 1)
)
h3cEponUniQosConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "A3COM-HUAWEI-EPON-UNI-MIB", "h3cEponUniIndex"),
    (0, "A3COM-HUAWEI-EPON-UNI-MIB", "h3cEponUniQosConfIndex"),
)
if mibBuilder.loadTexts:
    h3cEponUniQosConfEntry.setStatus("current")
_H3cEponUniQosConfIndex_Type = Integer32
_H3cEponUniQosConfIndex_Object = MibTableColumn
h3cEponUniQosConfIndex = _H3cEponUniQosConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 11, 1, 1),
    _H3cEponUniQosConfIndex_Type()
)
h3cEponUniQosConfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cEponUniQosConfIndex.setStatus("current")
_H3cEponUniQosConfRuleIndexNext_Type = Integer32
_H3cEponUniQosConfRuleIndexNext_Object = MibTableColumn
h3cEponUniQosConfRuleIndexNext = _H3cEponUniQosConfRuleIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 11, 1, 2),
    _H3cEponUniQosConfRuleIndexNext_Type()
)
h3cEponUniQosConfRuleIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponUniQosConfRuleIndexNext.setStatus("current")
_H3cEponUniQosConfMappedQueue_Type = Integer32
_H3cEponUniQosConfMappedQueue_Object = MibTableColumn
h3cEponUniQosConfMappedQueue = _H3cEponUniQosConfMappedQueue_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 11, 1, 3),
    _H3cEponUniQosConfMappedQueue_Type()
)
h3cEponUniQosConfMappedQueue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cEponUniQosConfMappedQueue.setStatus("current")
_H3cEponUniQosConfMarkedPriority_Type = Integer32
_H3cEponUniQosConfMarkedPriority_Object = MibTableColumn
h3cEponUniQosConfMarkedPriority = _H3cEponUniQosConfMarkedPriority_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 11, 1, 4),
    _H3cEponUniQosConfMarkedPriority_Type()
)
h3cEponUniQosConfMarkedPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cEponUniQosConfMarkedPriority.setStatus("current")
_H3cEponUniQosConfRowStatus_Type = RowStatus
_H3cEponUniQosConfRowStatus_Object = MibTableColumn
h3cEponUniQosConfRowStatus = _H3cEponUniQosConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 11, 1, 5),
    _H3cEponUniQosConfRowStatus_Type()
)
h3cEponUniQosConfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cEponUniQosConfRowStatus.setStatus("current")
_H3cEponUniQosRuleTable_Object = MibTable
h3cEponUniQosRuleTable = _H3cEponUniQosRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 12)
)
if mibBuilder.loadTexts:
    h3cEponUniQosRuleTable.setStatus("current")
_H3cEponUniQosRuleEntry_Object = MibTableRow
h3cEponUniQosRuleEntry = _H3cEponUniQosRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 12, 1)
)
h3cEponUniQosRuleEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "A3COM-HUAWEI-EPON-UNI-MIB", "h3cEponUniIndex"),
    (0, "A3COM-HUAWEI-EPON-UNI-MIB", "h3cEponUniQosConfIndex"),
    (0, "A3COM-HUAWEI-EPON-UNI-MIB", "h3cEponUniQosRuleIndex"),
)
if mibBuilder.loadTexts:
    h3cEponUniQosRuleEntry.setStatus("current")


class _H3cEponUniQosRuleIndex_Type(Integer32):
    """Custom type h3cEponUniQosRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_H3cEponUniQosRuleIndex_Type.__name__ = "Integer32"
_H3cEponUniQosRuleIndex_Object = MibTableColumn
h3cEponUniQosRuleIndex = _H3cEponUniQosRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 12, 1, 1),
    _H3cEponUniQosRuleIndex_Type()
)
h3cEponUniQosRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cEponUniQosRuleIndex.setStatus("current")


class _H3cEponUniQosRuleSelector_Type(Integer32):
    """Custom type h3cEponUniQosRuleSelector based on Integer32"""
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


_H3cEponUniQosRuleSelector_Type.__name__ = "Integer32"
_H3cEponUniQosRuleSelector_Object = MibTableColumn
h3cEponUniQosRuleSelector = _H3cEponUniQosRuleSelector_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 12, 1, 2),
    _H3cEponUniQosRuleSelector_Type()
)
h3cEponUniQosRuleSelector.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cEponUniQosRuleSelector.setStatus("current")
_H3cEponUniQosRuleValue_Type = Integer32
_H3cEponUniQosRuleValue_Object = MibTableColumn
h3cEponUniQosRuleValue = _H3cEponUniQosRuleValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 12, 1, 3),
    _H3cEponUniQosRuleValue_Type()
)
h3cEponUniQosRuleValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cEponUniQosRuleValue.setStatus("current")
_H3cEponUniQosRuleMacAddress_Type = MacAddress
_H3cEponUniQosRuleMacAddress_Object = MibTableColumn
h3cEponUniQosRuleMacAddress = _H3cEponUniQosRuleMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 12, 1, 4),
    _H3cEponUniQosRuleMacAddress_Type()
)
h3cEponUniQosRuleMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cEponUniQosRuleMacAddress.setStatus("current")


class _H3cEponUniQosRuleOperator_Type(Integer32):
    """Custom type h3cEponUniQosRuleOperator based on Integer32"""
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


_H3cEponUniQosRuleOperator_Type.__name__ = "Integer32"
_H3cEponUniQosRuleOperator_Object = MibTableColumn
h3cEponUniQosRuleOperator = _H3cEponUniQosRuleOperator_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 12, 1, 5),
    _H3cEponUniQosRuleOperator_Type()
)
h3cEponUniQosRuleOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cEponUniQosRuleOperator.setStatus("current")
_H3cEponUniQosRuleRowStatus_Type = RowStatus
_H3cEponUniQosRuleRowStatus_Object = MibTableColumn
h3cEponUniQosRuleRowStatus = _H3cEponUniQosRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 12, 1, 6),
    _H3cEponUniQosRuleRowStatus_Type()
)
h3cEponUniQosRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cEponUniQosRuleRowStatus.setStatus("current")
_H3cEponUniMirrorGroupTable_Object = MibTable
h3cEponUniMirrorGroupTable = _H3cEponUniMirrorGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 13)
)
if mibBuilder.loadTexts:
    h3cEponUniMirrorGroupTable.setStatus("current")
_H3cEponUniMirrorGroupEntry_Object = MibTableRow
h3cEponUniMirrorGroupEntry = _H3cEponUniMirrorGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 13, 1)
)
h3cEponUniMirrorGroupEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "A3COM-HUAWEI-EPON-UNI-MIB", "h3cEponUniMirrorGroupID"),
)
if mibBuilder.loadTexts:
    h3cEponUniMirrorGroupEntry.setStatus("current")
_H3cEponUniMirrorGroupID_Type = Integer32
_H3cEponUniMirrorGroupID_Object = MibTableColumn
h3cEponUniMirrorGroupID = _H3cEponUniMirrorGroupID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 13, 1, 1),
    _H3cEponUniMirrorGroupID_Type()
)
h3cEponUniMirrorGroupID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cEponUniMirrorGroupID.setStatus("current")
_H3cEponUniMirrorInboundPortList_Type = OctetString
_H3cEponUniMirrorInboundPortList_Object = MibTableColumn
h3cEponUniMirrorInboundPortList = _H3cEponUniMirrorInboundPortList_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 13, 1, 2),
    _H3cEponUniMirrorInboundPortList_Type()
)
h3cEponUniMirrorInboundPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEponUniMirrorInboundPortList.setStatus("current")
_H3cEponUniMirrorOutboundPortList_Type = OctetString
_H3cEponUniMirrorOutboundPortList_Object = MibTableColumn
h3cEponUniMirrorOutboundPortList = _H3cEponUniMirrorOutboundPortList_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 13, 1, 3),
    _H3cEponUniMirrorOutboundPortList_Type()
)
h3cEponUniMirrorOutboundPortList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cEponUniMirrorOutboundPortList.setStatus("current")
_H3cEponUniMonitorPort_Type = Integer32
_H3cEponUniMonitorPort_Object = MibTableColumn
h3cEponUniMonitorPort = _H3cEponUniMonitorPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 13, 1, 4),
    _H3cEponUniMonitorPort_Type()
)
h3cEponUniMonitorPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cEponUniMonitorPort.setStatus("current")
_H3cEponUniMirrorRowStatus_Type = RowStatus
_H3cEponUniMirrorRowStatus_Object = MibTableColumn
h3cEponUniMirrorRowStatus = _H3cEponUniMirrorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 13, 1, 5),
    _H3cEponUniMirrorRowStatus_Type()
)
h3cEponUniMirrorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cEponUniMirrorRowStatus.setStatus("current")
_H3cEponUniMirrorGroupIdNextTable_Object = MibTable
h3cEponUniMirrorGroupIdNextTable = _H3cEponUniMirrorGroupIdNextTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 14)
)
if mibBuilder.loadTexts:
    h3cEponUniMirrorGroupIdNextTable.setStatus("current")
_H3cEponUniMirrorGroupIdNextEntry_Object = MibTableRow
h3cEponUniMirrorGroupIdNextEntry = _H3cEponUniMirrorGroupIdNextEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 14, 1)
)
h3cEponUniMirrorGroupIdNextEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cEponUniMirrorGroupIdNextEntry.setStatus("current")
_H3cEponUniMirrorGroupIDNext_Type = Integer32
_H3cEponUniMirrorGroupIDNext_Object = MibTableColumn
h3cEponUniMirrorGroupIDNext = _H3cEponUniMirrorGroupIDNext_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 14, 1, 1),
    _H3cEponUniMirrorGroupIDNext_Type()
)
h3cEponUniMirrorGroupIDNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponUniMirrorGroupIDNext.setStatus("current")
_H3cEponUniMulticastCtrlInfoTable_Object = MibTable
h3cEponUniMulticastCtrlInfoTable = _H3cEponUniMulticastCtrlInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 15)
)
if mibBuilder.loadTexts:
    h3cEponUniMulticastCtrlInfoTable.setStatus("current")
_H3cEponUniMulticastCtrlInfoEntry_Object = MibTableRow
h3cEponUniMulticastCtrlInfoEntry = _H3cEponUniMulticastCtrlInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 15, 1)
)
h3cEponUniMulticastCtrlInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "A3COM-HUAWEI-EPON-UNI-MIB", "h3cEponUniIndex"),
    (0, "A3COM-HUAWEI-EPON-UNI-MIB", "h3cEponUniMultActVlan"),
    (0, "A3COM-HUAWEI-EPON-UNI-MIB", "h3cEponUniMultActAddress"),
)
if mibBuilder.loadTexts:
    h3cEponUniMulticastCtrlInfoEntry.setStatus("current")
_H3cEponUniMultActVlan_Type = Integer32
_H3cEponUniMultActVlan_Object = MibTableColumn
h3cEponUniMultActVlan = _H3cEponUniMultActVlan_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 15, 1, 1),
    _H3cEponUniMultActVlan_Type()
)
h3cEponUniMultActVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cEponUniMultActVlan.setStatus("current")
_H3cEponUniMultActAddress_Type = IpAddress
_H3cEponUniMultActAddress_Object = MibTableColumn
h3cEponUniMultActAddress = _H3cEponUniMultActAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 15, 1, 2),
    _H3cEponUniMultActAddress_Type()
)
h3cEponUniMultActAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cEponUniMultActAddress.setStatus("current")


class _H3cEponUniMultActAccessRule_Type(Integer32):
    """Custom type h3cEponUniMultActAccessRule based on Integer32"""
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


_H3cEponUniMultActAccessRule_Type.__name__ = "Integer32"
_H3cEponUniMultActAccessRule_Object = MibTableColumn
h3cEponUniMultActAccessRule = _H3cEponUniMultActAccessRule_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 15, 1, 3),
    _H3cEponUniMultActAccessRule_Type()
)
h3cEponUniMultActAccessRule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponUniMultActAccessRule.setStatus("current")
_H3cEponUniMultActPreTimes_Type = Integer32
_H3cEponUniMultActPreTimes_Object = MibTableColumn
h3cEponUniMultActPreTimes = _H3cEponUniMultActPreTimes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 15, 1, 4),
    _H3cEponUniMultActPreTimes_Type()
)
h3cEponUniMultActPreTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponUniMultActPreTimes.setStatus("current")
_H3cEponUniMultActPreRemain_Type = Integer32
_H3cEponUniMultActPreRemain_Object = MibTableColumn
h3cEponUniMultActPreRemain = _H3cEponUniMultActPreRemain_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 15, 1, 5),
    _H3cEponUniMultActPreRemain_Type()
)
h3cEponUniMultActPreRemain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponUniMultActPreRemain.setStatus("current")
_H3cEponUniMulticastIndexNextTable_Object = MibTable
h3cEponUniMulticastIndexNextTable = _H3cEponUniMulticastIndexNextTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 16)
)
if mibBuilder.loadTexts:
    h3cEponUniMulticastIndexNextTable.setStatus("current")
_H3cEponUniMulticastIndexNextEntry_Object = MibTableRow
h3cEponUniMulticastIndexNextEntry = _H3cEponUniMulticastIndexNextEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 16, 1)
)
h3cEponUniMulticastIndexNextEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "A3COM-HUAWEI-EPON-UNI-MIB", "h3cEponUniIndex"),
)
if mibBuilder.loadTexts:
    h3cEponUniMulticastIndexNextEntry.setStatus("current")
_H3cEponUniMulticastConfIndexNext_Type = Integer32
_H3cEponUniMulticastConfIndexNext_Object = MibTableColumn
h3cEponUniMulticastConfIndexNext = _H3cEponUniMulticastConfIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 1, 16, 1, 1),
    _H3cEponUniMulticastConfIndexNext_Type()
)
h3cEponUniMulticastConfIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEponUniMulticastConfIndexNext.setStatus("current")
_H3cEponUniTrap_ObjectIdentity = ObjectIdentity
h3cEponUniTrap = _H3cEponUniTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 2)
)
_H3cEponUniTrapPrefix_ObjectIdentity = ObjectIdentity
h3cEponUniTrapPrefix = _H3cEponUniTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 2, 0)
)

# Managed Objects groups


# Notification objects

h3cEponUniLinkUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 2, 0, 1)
)
h3cEponUniLinkUpTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("A3COM-HUAWEI-EPON-UNI-MIB", "h3cEponUniIndex"),
        ("A3COM-HUAWEI-EPON-UNI-MIB", "h3cEponUniDescr"),
        ("A3COM-HUAWEI-EPON-UNI-MIB", "h3cEponUniAdminStatus"))
)
if mibBuilder.loadTexts:
    h3cEponUniLinkUpTrap.setStatus(
        "current"
    )

h3cEponUniLinkDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 42, 5, 2, 0, 2)
)
h3cEponUniLinkDownTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("A3COM-HUAWEI-EPON-UNI-MIB", "h3cEponUniIndex"),
        ("A3COM-HUAWEI-EPON-UNI-MIB", "h3cEponUniDescr"),
        ("A3COM-HUAWEI-EPON-UNI-MIB", "h3cEponUniAdminStatus"))
)
if mibBuilder.loadTexts:
    h3cEponUniLinkDownTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-EPON-UNI-MIB",
    **{"h3cEponUni": h3cEponUni,
       "h3cEponUniSysMan": h3cEponUniSysMan,
       "h3cEponUniSysManTable": h3cEponUniSysManTable,
       "h3cEponUniSysManEntry": h3cEponUniSysManEntry,
       "h3cEponUniIndex": h3cEponUniIndex,
       "h3cEponUniDescr": h3cEponUniDescr,
       "h3cEponUniAdminStatus": h3cEponUniAdminStatus,
       "h3cEponUniMdi": h3cEponUniMdi,
       "h3cEponUniPriority": h3cEponUniPriority,
       "h3cEponUniVlanType": h3cEponUniVlanType,
       "h3cEponUniAccessVlan": h3cEponUniAccessVlan,
       "h3cEponUniTrunkPvid": h3cEponUniTrunkPvid,
       "h3cEponUniVLANTrunkAllowListLow": h3cEponUniVLANTrunkAllowListLow,
       "h3cEponUniVLANTrunkAllowListHigh": h3cEponUniVLANTrunkAllowListHigh,
       "h3cEponUniInboundLineRate": h3cEponUniInboundLineRate,
       "h3cEponUniOutboundLineRate": h3cEponUniOutboundLineRate,
       "h3cEponUniFlowControl": h3cEponUniFlowControl,
       "h3cEponUniSpeed": h3cEponUniSpeed,
       "h3cEponUniDuplex": h3cEponUniDuplex,
       "h3cEponUniVlanVPNStatus": h3cEponUniVlanVPNStatus,
       "h3cEponUniCountReset": h3cEponUniCountReset,
       "h3cEponUniPortIsolate": h3cEponUniPortIsolate,
       "h3cEponUniVlanConfiguration": h3cEponUniVlanConfiguration,
       "h3cEponUniAutoNegotiation": h3cEponUniAutoNegotiation,
       "h3cEponUniRestartAutoNeg": h3cEponUniRestartAutoNeg,
       "h3cEponUniLinkStatus": h3cEponUniLinkStatus,
       "h3cEponUniInterfaceType": h3cEponUniInterfaceType,
       "h3cEponUniVitualCableTest": h3cEponUniVitualCableTest,
       "h3cEponUniVCTCableStatus": h3cEponUniVCTCableStatus,
       "h3cEponUniVCTCableLength": h3cEponUniVCTCableLength,
       "h3cEponUniVCTImpedanceMismatch": h3cEponUniVCTImpedanceMismatch,
       "h3cEponUniVCTPairSkew": h3cEponUniVCTPairSkew,
       "h3cEponUniVCTPairSwap": h3cEponUniVCTPairSwap,
       "h3cEponUniVCTPolaritySwap": h3cEponUniVCTPolaritySwap,
       "h3cEponUniVCTInsertionLoss": h3cEponUniVCTInsertionLoss,
       "h3cEponUniVCTReturnLoss": h3cEponUniVCTReturnLoss,
       "h3cEponUniVCTNearendCrosstalk": h3cEponUniVCTNearendCrosstalk,
       "h3cEponUniCountTable": h3cEponUniCountTable,
       "h3cEponUniCountEntry": h3cEponUniCountEntry,
       "h3cEponUniInStatsPkts": h3cEponUniInStatsPkts,
       "h3cEponUniInStatsUnicastPkts": h3cEponUniInStatsUnicastPkts,
       "h3cEponUniInStatsBroadcastPkts": h3cEponUniInStatsBroadcastPkts,
       "h3cEponUniInStatsMulticastPkts": h3cEponUniInStatsMulticastPkts,
       "h3cEponUniInPausePkts": h3cEponUniInPausePkts,
       "h3cEponUniInTotalErrors": h3cEponUniInTotalErrors,
       "h3cEponUniInStatsCRCAlignErrors": h3cEponUniInStatsCRCAlignErrors,
       "h3cEponUniInStatsUndersizePkts": h3cEponUniInStatsUndersizePkts,
       "h3cEponUniInStatsOversizePkts": h3cEponUniInStatsOversizePkts,
       "h3cEponUniInErrorbyOther": h3cEponUniInErrorbyOther,
       "h3cEponUniOutStatsPkts": h3cEponUniOutStatsPkts,
       "h3cEponUniOutStatsUnicastPkts": h3cEponUniOutStatsUnicastPkts,
       "h3cEponUniOutStatsBroadcastPkts": h3cEponUniOutStatsBroadcastPkts,
       "h3cEponUniOutStatsMulticastPkts": h3cEponUniOutStatsMulticastPkts,
       "h3cEponUniOutStatsPausePkts": h3cEponUniOutStatsPausePkts,
       "h3cEponUniOutTotalErrors": h3cEponUniOutTotalErrors,
       "h3cEponUniOutStatsCollisions": h3cEponUniOutStatsCollisions,
       "h3cEponUniOutDelayExceededDiscards": h3cEponUniOutDelayExceededDiscards,
       "h3cEponUniOutErrorbyOther": h3cEponUniOutErrorbyOther,
       "h3cEponUniOutDroppedFrames": h3cEponUniOutDroppedFrames,
       "h3cEponUniIgmpInfoTable": h3cEponUniIgmpInfoTable,
       "h3cEponUniIgmpInfoEntry": h3cEponUniIgmpInfoEntry,
       "h3cEponUniMacIndex": h3cEponUniMacIndex,
       "h3cEponUniIgmpMacAddress": h3cEponUniIgmpMacAddress,
       "h3cEponUniIgmpVlanId": h3cEponUniIgmpVlanId,
       "h3cEponUniParaMan": h3cEponUniParaMan,
       "h3cEponUniLineRateMax": h3cEponUniLineRateMax,
       "h3cEponUniLineRateStep": h3cEponUniLineRateStep,
       "h3cEponUniNumberOnOnu": h3cEponUniNumberOnOnu,
       "h3cEponUniScalarGroup": h3cEponUniScalarGroup,
       "h3cEponUniPortPolicyTable": h3cEponUniPortPolicyTable,
       "h3cEponUniPortPolicyEntry": h3cEponUniPortPolicyEntry,
       "h3cEponUniPortPolicyStatus": h3cEponUniPortPolicyStatus,
       "h3cEponUniPortPolicyCir": h3cEponUniPortPolicyCir,
       "h3cEponUniPortPolicyBucketDepth": h3cEponUniPortPolicyBucketDepth,
       "h3cEponUniPortPolicyExtraBurst": h3cEponUniPortPolicyExtraBurst,
       "h3cEponUniPortPolicyInboundCir": h3cEponUniPortPolicyInboundCir,
       "h3cEponUniPortPolicyInboundBucketDepth": h3cEponUniPortPolicyInboundBucketDepth,
       "h3cEponUniPortPolicyInboundExtraBurst": h3cEponUniPortPolicyInboundExtraBurst,
       "h3cEponUniPortPolicyOutboundCir": h3cEponUniPortPolicyOutboundCir,
       "h3cEponUniPortPolicyOutboundPir": h3cEponUniPortPolicyOutboundPir,
       "h3cEponUniMulticastTable": h3cEponUniMulticastTable,
       "h3cEponUniMulticastEntry": h3cEponUniMulticastEntry,
       "h3cEponUniMulticastGroupNumber": h3cEponUniMulticastGroupNumber,
       "h3cEponUniMulticastVlanList": h3cEponUniMulticastVlanList,
       "h3cEponUniMulticastStripStatus": h3cEponUniMulticastStripStatus,
       "h3cEponUniMulticastFastleave": h3cEponUniMulticastFastleave,
       "h3cEponUniTechAbilityTable": h3cEponUniTechAbilityTable,
       "h3cEponUniTechAbilityEntry": h3cEponUniTechAbilityEntry,
       "h3cEponUniLocalTechAbility": h3cEponUniLocalTechAbility,
       "h3cEponUniAdvertisedTechAbility": h3cEponUniAdvertisedTechAbility,
       "h3cEponUniMulticastControlTable": h3cEponUniMulticastControlTable,
       "h3cEponUniMulticastControlEntry": h3cEponUniMulticastControlEntry,
       "h3cEponUniMulticastVlanIndex": h3cEponUniMulticastVlanIndex,
       "h3cEponUniMulticastAddressList": h3cEponUniMulticastAddressList,
       "h3cEponUniMulticastAccessRule": h3cEponUniMulticastAccessRule,
       "h3cEponUniMulticastChannelLimit": h3cEponUniMulticastChannelLimit,
       "h3cEponUniMulticastPreTimeSlice": h3cEponUniMulticastPreTimeSlice,
       "h3cEponUniMulticastPreTimes": h3cEponUniMulticastPreTimes,
       "h3cEponUniMulticastPreInterval": h3cEponUniMulticastPreInterval,
       "h3cEponUniMulticastRowStatus": h3cEponUniMulticastRowStatus,
       "h3cEponUniMulticastIndex": h3cEponUniMulticastIndex,
       "h3cEponUniMulticastSourceIpList": h3cEponUniMulticastSourceIpList,
       "h3cEponUniMulticastResetInterval": h3cEponUniMulticastResetInterval,
       "h3cEponUniQosIndexNextTable": h3cEponUniQosIndexNextTable,
       "h3cEponUniQosIndexNextEntry": h3cEponUniQosIndexNextEntry,
       "h3cEponUniQosConfIndexNext": h3cEponUniQosConfIndexNext,
       "h3cEponUniQosConfTable": h3cEponUniQosConfTable,
       "h3cEponUniQosConfEntry": h3cEponUniQosConfEntry,
       "h3cEponUniQosConfIndex": h3cEponUniQosConfIndex,
       "h3cEponUniQosConfRuleIndexNext": h3cEponUniQosConfRuleIndexNext,
       "h3cEponUniQosConfMappedQueue": h3cEponUniQosConfMappedQueue,
       "h3cEponUniQosConfMarkedPriority": h3cEponUniQosConfMarkedPriority,
       "h3cEponUniQosConfRowStatus": h3cEponUniQosConfRowStatus,
       "h3cEponUniQosRuleTable": h3cEponUniQosRuleTable,
       "h3cEponUniQosRuleEntry": h3cEponUniQosRuleEntry,
       "h3cEponUniQosRuleIndex": h3cEponUniQosRuleIndex,
       "h3cEponUniQosRuleSelector": h3cEponUniQosRuleSelector,
       "h3cEponUniQosRuleValue": h3cEponUniQosRuleValue,
       "h3cEponUniQosRuleMacAddress": h3cEponUniQosRuleMacAddress,
       "h3cEponUniQosRuleOperator": h3cEponUniQosRuleOperator,
       "h3cEponUniQosRuleRowStatus": h3cEponUniQosRuleRowStatus,
       "h3cEponUniMirrorGroupTable": h3cEponUniMirrorGroupTable,
       "h3cEponUniMirrorGroupEntry": h3cEponUniMirrorGroupEntry,
       "h3cEponUniMirrorGroupID": h3cEponUniMirrorGroupID,
       "h3cEponUniMirrorInboundPortList": h3cEponUniMirrorInboundPortList,
       "h3cEponUniMirrorOutboundPortList": h3cEponUniMirrorOutboundPortList,
       "h3cEponUniMonitorPort": h3cEponUniMonitorPort,
       "h3cEponUniMirrorRowStatus": h3cEponUniMirrorRowStatus,
       "h3cEponUniMirrorGroupIdNextTable": h3cEponUniMirrorGroupIdNextTable,
       "h3cEponUniMirrorGroupIdNextEntry": h3cEponUniMirrorGroupIdNextEntry,
       "h3cEponUniMirrorGroupIDNext": h3cEponUniMirrorGroupIDNext,
       "h3cEponUniMulticastCtrlInfoTable": h3cEponUniMulticastCtrlInfoTable,
       "h3cEponUniMulticastCtrlInfoEntry": h3cEponUniMulticastCtrlInfoEntry,
       "h3cEponUniMultActVlan": h3cEponUniMultActVlan,
       "h3cEponUniMultActAddress": h3cEponUniMultActAddress,
       "h3cEponUniMultActAccessRule": h3cEponUniMultActAccessRule,
       "h3cEponUniMultActPreTimes": h3cEponUniMultActPreTimes,
       "h3cEponUniMultActPreRemain": h3cEponUniMultActPreRemain,
       "h3cEponUniMulticastIndexNextTable": h3cEponUniMulticastIndexNextTable,
       "h3cEponUniMulticastIndexNextEntry": h3cEponUniMulticastIndexNextEntry,
       "h3cEponUniMulticastConfIndexNext": h3cEponUniMulticastConfIndexNext,
       "h3cEponUniTrap": h3cEponUniTrap,
       "h3cEponUniTrapPrefix": h3cEponUniTrapPrefix,
       "h3cEponUniLinkUpTrap": h3cEponUniLinkUpTrap,
       "h3cEponUniLinkDownTrap": h3cEponUniLinkDownTrap}
)
