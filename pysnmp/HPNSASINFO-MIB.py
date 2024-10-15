# SNMP MIB module (HPNSASINFO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPNSASINFO-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:02:26 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hp_ObjectIdentity = ObjectIdentity
hp = _Hp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11)
)
_Nm_ObjectIdentity = ObjectIdentity
nm = _Nm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2)
)
_Hpnsa_ObjectIdentity = ObjectIdentity
hpnsa = _Hpnsa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23)
)
_HpnsaSystemInfo_ObjectIdentity = ObjectIdentity
hpnsaSystemInfo = _HpnsaSystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7)
)
_HpnsaSiMibRev_ObjectIdentity = ObjectIdentity
hpnsaSiMibRev = _HpnsaSiMibRev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 1)
)


class _HpnsaSiMibRevMajor_Type(Integer32):
    """Custom type hpnsaSiMibRevMajor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnsaSiMibRevMajor_Type.__name__ = "Integer32"
_HpnsaSiMibRevMajor_Object = MibScalar
hpnsaSiMibRevMajor = _HpnsaSiMibRevMajor_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 1, 1),
    _HpnsaSiMibRevMajor_Type()
)
hpnsaSiMibRevMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiMibRevMajor.setStatus("mandatory")


class _HpnsaSiMibRevMinor_Type(Integer32):
    """Custom type hpnsaSiMibRevMinor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnsaSiMibRevMinor_Type.__name__ = "Integer32"
_HpnsaSiMibRevMinor_Object = MibScalar
hpnsaSiMibRevMinor = _HpnsaSiMibRevMinor_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 1, 2),
    _HpnsaSiMibRevMinor_Type()
)
hpnsaSiMibRevMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiMibRevMinor.setStatus("mandatory")
_HpnsaSiAgent_ObjectIdentity = ObjectIdentity
hpnsaSiAgent = _HpnsaSiAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 2)
)
_HpnsaSiAgentTable_Object = MibTable
hpnsaSiAgentTable = _HpnsaSiAgentTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 2, 1)
)
if mibBuilder.loadTexts:
    hpnsaSiAgentTable.setStatus("mandatory")
_HpnsaSiAgentEntry_Object = MibTableRow
hpnsaSiAgentEntry = _HpnsaSiAgentEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 2, 1, 1)
)
hpnsaSiAgentEntry.setIndexNames(
    (0, "HPNSASINFO-MIB", "hpnsaSiAgentIndex"),
)
if mibBuilder.loadTexts:
    hpnsaSiAgentEntry.setStatus("mandatory")


class _HpnsaSiAgentIndex_Type(Integer32):
    """Custom type hpnsaSiAgentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnsaSiAgentIndex_Type.__name__ = "Integer32"
_HpnsaSiAgentIndex_Object = MibTableColumn
hpnsaSiAgentIndex = _HpnsaSiAgentIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 2, 1, 1, 1),
    _HpnsaSiAgentIndex_Type()
)
hpnsaSiAgentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiAgentIndex.setStatus("mandatory")


class _HpnsaSiAgentName_Type(DisplayString):
    """Custom type hpnsaSiAgentName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnsaSiAgentName_Type.__name__ = "DisplayString"
_HpnsaSiAgentName_Object = MibTableColumn
hpnsaSiAgentName = _HpnsaSiAgentName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 2, 1, 1, 2),
    _HpnsaSiAgentName_Type()
)
hpnsaSiAgentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiAgentName.setStatus("mandatory")


class _HpnsaSiAgentVersion_Type(DisplayString):
    """Custom type hpnsaSiAgentVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_HpnsaSiAgentVersion_Type.__name__ = "DisplayString"
_HpnsaSiAgentVersion_Object = MibTableColumn
hpnsaSiAgentVersion = _HpnsaSiAgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 2, 1, 1, 3),
    _HpnsaSiAgentVersion_Type()
)
hpnsaSiAgentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiAgentVersion.setStatus("mandatory")


class _HpnsaSiAgentDate_Type(OctetString):
    """Custom type hpnsaSiAgentDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )


_HpnsaSiAgentDate_Type.__name__ = "OctetString"
_HpnsaSiAgentDate_Object = MibTableColumn
hpnsaSiAgentDate = _HpnsaSiAgentDate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 2, 1, 1, 4),
    _HpnsaSiAgentDate_Type()
)
hpnsaSiAgentDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiAgentDate.setStatus("mandatory")
_HpnsaSiBasicInfo_ObjectIdentity = ObjectIdentity
hpnsaSiBasicInfo = _HpnsaSiBasicInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 3)
)


class _HpnsaSiModel_Type(Integer32):
    """Custom type hpnsaSiModel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              32,
              35,
              36,
              40,
              42,
              52,
              54,
              61,
              63,
              65,
              66,
              67,
              68,
              69,
              71,
              75,
              79,
              80,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89)
        )
    )
    namedValues = NamedValues(
        *(("hp-netserver-e-series", 71),
          ("hp-netserver-lc-series", 61),
          ("hp-netserver-lc2000", 68),
          ("hp-netserver-lc2000u3", 84),
          ("hp-netserver-ld-series", 52),
          ("hp-netserver-le-series", 35),
          ("hp-netserver-lf-series", 40),
          ("hp-netserver-lh-series", 63),
          ("hp-netserver-lh3000", 66),
          ("hp-netserver-lh3000u3", 85),
          ("hp-netserver-lh6000", 67),
          ("hp-netserver-lh6000u3", 82),
          ("hp-netserver-lm-series", 36),
          ("hp-netserver-lp1000r", 86),
          ("hp-netserver-lp2000r", 87),
          ("hp-netserver-ls-series", 42),
          ("hp-netserver-lt6000", 69),
          ("hp-netserver-lt6000ru3", 83),
          ("hp-netserver-lx-series", 65),
          ("hp-netserver-racks-series", 54),
          ("hp-netserver-rc7100", 89),
          ("hp-netserver-tc3100", 79),
          ("hp-netserver-tc4100", 80),
          ("hp-netserver-tc6100", 75),
          ("hp-netserver-tc7100", 88),
          ("hp-vectra-286-12-pc", 15),
          ("hp-vectra-386-16n-pc", 18),
          ("hp-vectra-386-20-pc", 17),
          ("hp-vectra-386-20n-pc", 19),
          ("hp-vectra-386-25-pc", 13),
          ("hp-vectra-386-25n", 27),
          ("hp-vectra-386-33n", 30),
          ("hp-vectra-386s-20-pc", 21),
          ("hp-vectra-386s-25", 29),
          ("hp-vectra-486-25t-pc", 14),
          ("hp-vectra-486-25u-pc", 22),
          ("hp-vectra-486-33n", 32),
          ("hp-vectra-486-33t-pc", 16),
          ("hp-vectra-486-33u-pc", 23),
          ("hp-vectra-486-50u-pc", 24),
          ("hp-vectra-486-66u-pc", 25),
          ("hp-vectra-486-n", 28),
          ("hp-vectra-486-st-series", 26),
          ("hp-vectra-486s-20-pc", 20),
          ("hp-vectra-cs-pc", 5),
          ("hp-vectra-es-12-pc", 1),
          ("hp-vectra-es-pc", 4),
          ("hp-vectra-ls-286-pc", 11),
          ("hp-vectra-pc", 0),
          ("hp-vectra-portablecs-pc", 3),
          ("hp-vectra-qs-16-pc", 7),
          ("hp-vectra-qs-16s-pc", 12),
          ("hp-vectra-qs-20-pc", 8),
          ("hp-vectra-rs-16-pc", 6),
          ("hp-vectra-rs-20-pc", 2),
          ("hp-vectra-rs-20c-pc", 9),
          ("hp-vectra-rs-25c-pc", 10))
    )


_HpnsaSiModel_Type.__name__ = "Integer32"
_HpnsaSiModel_Object = MibScalar
hpnsaSiModel = _HpnsaSiModel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 3, 1),
    _HpnsaSiModel_Type()
)
hpnsaSiModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiModel.setStatus("mandatory")


class _HpnsaSiBIOSVersion_Type(DisplayString):
    """Custom type hpnsaSiBIOSVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnsaSiBIOSVersion_Type.__name__ = "DisplayString"
_HpnsaSiBIOSVersion_Object = MibScalar
hpnsaSiBIOSVersion = _HpnsaSiBIOSVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 3, 2),
    _HpnsaSiBIOSVersion_Type()
)
hpnsaSiBIOSVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiBIOSVersion.setStatus("mandatory")


class _HpnsaSiVideoBIOSVersion_Type(DisplayString):
    """Custom type hpnsaSiVideoBIOSVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnsaSiVideoBIOSVersion_Type.__name__ = "DisplayString"
_HpnsaSiVideoBIOSVersion_Object = MibScalar
hpnsaSiVideoBIOSVersion = _HpnsaSiVideoBIOSVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 3, 3),
    _HpnsaSiVideoBIOSVersion_Type()
)
hpnsaSiVideoBIOSVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiVideoBIOSVersion.setStatus("optional")


class _HpnsaSiSCSIBIOSVersion_Type(DisplayString):
    """Custom type hpnsaSiSCSIBIOSVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnsaSiSCSIBIOSVersion_Type.__name__ = "DisplayString"
_HpnsaSiSCSIBIOSVersion_Object = MibScalar
hpnsaSiSCSIBIOSVersion = _HpnsaSiSCSIBIOSVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 3, 4),
    _HpnsaSiSCSIBIOSVersion_Type()
)
hpnsaSiSCSIBIOSVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiSCSIBIOSVersion.setStatus("mandatory")
_HpnsaSiNumEISASlots_Type = Integer32
_HpnsaSiNumEISASlots_Object = MibScalar
hpnsaSiNumEISASlots = _HpnsaSiNumEISASlots_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 3, 5),
    _HpnsaSiNumEISASlots_Type()
)
hpnsaSiNumEISASlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiNumEISASlots.setStatus("mandatory")
_HpnsaSiNumPCISlots_Type = Integer32
_HpnsaSiNumPCISlots_Object = MibScalar
hpnsaSiNumPCISlots = _HpnsaSiNumPCISlots_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 3, 6),
    _HpnsaSiNumPCISlots_Type()
)
hpnsaSiNumPCISlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiNumPCISlots.setStatus("mandatory")
_HpnsaSiNumCPU_Type = Integer32
_HpnsaSiNumCPU_Object = MibScalar
hpnsaSiNumCPU = _HpnsaSiNumCPU_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 3, 7),
    _HpnsaSiNumCPU_Type()
)
hpnsaSiNumCPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiNumCPU.setStatus("mandatory")
_HpnsaSiCPUTable_Object = MibTable
hpnsaSiCPUTable = _HpnsaSiCPUTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 3, 8)
)
if mibBuilder.loadTexts:
    hpnsaSiCPUTable.setStatus("mandatory")
_HpnsaSiCPUEntry_Object = MibTableRow
hpnsaSiCPUEntry = _HpnsaSiCPUEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 3, 8, 1)
)
hpnsaSiCPUEntry.setIndexNames(
    (0, "HPNSASINFO-MIB", "hpnsaSiCPUIndex"),
)
if mibBuilder.loadTexts:
    hpnsaSiCPUEntry.setStatus("mandatory")


class _HpnsaSiCPUIndex_Type(Integer32):
    """Custom type hpnsaSiCPUIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnsaSiCPUIndex_Type.__name__ = "Integer32"
_HpnsaSiCPUIndex_Object = MibTableColumn
hpnsaSiCPUIndex = _HpnsaSiCPUIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 3, 8, 1, 1),
    _HpnsaSiCPUIndex_Type()
)
hpnsaSiCPUIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiCPUIndex.setStatus("mandatory")


class _HpnsaSiCPUModel_Type(Integer32):
    """Custom type hpnsaSiCPUModel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              25,
              253,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("cpu-486-24c", 13),
          ("cpu-486-dx", 5),
          ("cpu-486-dx2-or-overdrive", 8),
          ("cpu-486-p23t", 9),
          ("cpu-486-sl", 18),
          ("cpu-486-sx", 6),
          ("cpu-486-sx2", 17),
          ("cpu-487-sx", 10),
          ("cpu-80286", 0),
          ("cpu-80386", 3),
          ("cpu-80386-sx", 4),
          ("cpu-8086", 2),
          ("cpu-8088", 1),
          ("cpu-dual-pentium", 254),
          ("cpu-itanium", 25),
          ("cpu-pentium", 11),
          ("cpu-pentium-ii", 20),
          ("cpu-pentium-ii-xeon", 21),
          ("cpu-pentium-iii", 22),
          ("cpu-pentium-iii-xeon", 23),
          ("cpu-pentium-overdrive", 12),
          ("cpu-pentium-series-p54c", 14),
          ("cpu-pentium-series-p54cm", 16),
          ("cpu-pentium-series-p54ct", 15),
          ("cpu-pentium-series-p6", 19),
          ("cpu-unknown", 255),
          ("notpresent", 253))
    )


_HpnsaSiCPUModel_Type.__name__ = "Integer32"
_HpnsaSiCPUModel_Object = MibTableColumn
hpnsaSiCPUModel = _HpnsaSiCPUModel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 3, 8, 1, 2),
    _HpnsaSiCPUModel_Type()
)
hpnsaSiCPUModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiCPUModel.setStatus("mandatory")
_HpnsaSiCPUSpeed_Type = Integer32
_HpnsaSiCPUSpeed_Object = MibTableColumn
hpnsaSiCPUSpeed = _HpnsaSiCPUSpeed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 3, 8, 1, 3),
    _HpnsaSiCPUSpeed_Type()
)
hpnsaSiCPUSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiCPUSpeed.setStatus("mandatory")


class _HpnsaSiOpSysType_Type(DisplayString):
    """Custom type hpnsaSiOpSysType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnsaSiOpSysType_Type.__name__ = "DisplayString"
_HpnsaSiOpSysType_Object = MibScalar
hpnsaSiOpSysType = _HpnsaSiOpSysType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 3, 9),
    _HpnsaSiOpSysType_Type()
)
hpnsaSiOpSysType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiOpSysType.setStatus("mandatory")


class _HpnsaSiOpSysVer_Type(DisplayString):
    """Custom type hpnsaSiOpSysVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnsaSiOpSysVer_Type.__name__ = "DisplayString"
_HpnsaSiOpSysVer_Object = MibScalar
hpnsaSiOpSysVer = _HpnsaSiOpSysVer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 3, 10),
    _HpnsaSiOpSysVer_Type()
)
hpnsaSiOpSysVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiOpSysVer.setStatus("mandatory")


class _HpnsaSiSystemName_Type(DisplayString):
    """Custom type hpnsaSiSystemName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnsaSiSystemName_Type.__name__ = "DisplayString"
_HpnsaSiSystemName_Object = MibScalar
hpnsaSiSystemName = _HpnsaSiSystemName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 3, 11),
    _HpnsaSiSystemName_Type()
)
hpnsaSiSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiSystemName.setStatus("mandatory")


class _HpnsaSiSystemID_Type(DisplayString):
    """Custom type hpnsaSiSystemID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnsaSiSystemID_Type.__name__ = "DisplayString"
_HpnsaSiSystemID_Object = MibScalar
hpnsaSiSystemID = _HpnsaSiSystemID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 3, 12),
    _HpnsaSiSystemID_Type()
)
hpnsaSiSystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiSystemID.setStatus("optional")


class _HpnsaSiKbdType_Type(DisplayString):
    """Custom type hpnsaSiKbdType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnsaSiKbdType_Type.__name__ = "DisplayString"
_HpnsaSiKbdType_Object = MibScalar
hpnsaSiKbdType = _HpnsaSiKbdType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 3, 13),
    _HpnsaSiKbdType_Type()
)
hpnsaSiKbdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiKbdType.setStatus("optional")


class _HpnsaSiMouseType_Type(DisplayString):
    """Custom type hpnsaSiMouseType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnsaSiMouseType_Type.__name__ = "DisplayString"
_HpnsaSiMouseType_Object = MibScalar
hpnsaSiMouseType = _HpnsaSiMouseType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 3, 14),
    _HpnsaSiMouseType_Type()
)
hpnsaSiMouseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiMouseType.setStatus("optional")


class _HpnsaSiVideoType_Type(DisplayString):
    """Custom type hpnsaSiVideoType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnsaSiVideoType_Type.__name__ = "DisplayString"
_HpnsaSiVideoType_Object = MibScalar
hpnsaSiVideoType = _HpnsaSiVideoType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 3, 15),
    _HpnsaSiVideoType_Type()
)
hpnsaSiVideoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiVideoType.setStatus("optional")
_HpnsaSiNumISASlots_Type = Integer32
_HpnsaSiNumISASlots_Object = MibScalar
hpnsaSiNumISASlots = _HpnsaSiNumISASlots_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 3, 16),
    _HpnsaSiNumISASlots_Type()
)
hpnsaSiNumISASlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiNumISASlots.setStatus("mandatory")


class _HpnsaSiModelName_Type(DisplayString):
    """Custom type hpnsaSiModelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnsaSiModelName_Type.__name__ = "DisplayString"
_HpnsaSiModelName_Object = MibScalar
hpnsaSiModelName = _HpnsaSiModelName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 3, 17),
    _HpnsaSiModelName_Type()
)
hpnsaSiModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiModelName.setStatus("mandatory")


class _HpnsaSiOpSysDescription_Type(DisplayString):
    """Custom type hpnsaSiOpSysDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpnsaSiOpSysDescription_Type.__name__ = "DisplayString"
_HpnsaSiOpSysDescription_Object = MibScalar
hpnsaSiOpSysDescription = _HpnsaSiOpSysDescription_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 3, 18),
    _HpnsaSiOpSysDescription_Type()
)
hpnsaSiOpSysDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiOpSysDescription.setStatus("mandatory")
_HpnsaSiSecurity_ObjectIdentity = ObjectIdentity
hpnsaSiSecurity = _HpnsaSiSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 4)
)


class _HpnsaSiPowerOnPassword_Type(Integer32):
    """Custom type hpnsaSiPowerOnPassword based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("n-a", 0))
    )


_HpnsaSiPowerOnPassword_Type.__name__ = "Integer32"
_HpnsaSiPowerOnPassword_Object = MibScalar
hpnsaSiPowerOnPassword = _HpnsaSiPowerOnPassword_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 4, 1),
    _HpnsaSiPowerOnPassword_Type()
)
hpnsaSiPowerOnPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiPowerOnPassword.setStatus("mandatory")


class _HpnsaSiNetServerMode_Type(Integer32):
    """Custom type hpnsaSiNetServerMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("n-a", 0))
    )


_HpnsaSiNetServerMode_Type.__name__ = "Integer32"
_HpnsaSiNetServerMode_Object = MibScalar
hpnsaSiNetServerMode = _HpnsaSiNetServerMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 4, 2),
    _HpnsaSiNetServerMode_Type()
)
hpnsaSiNetServerMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiNetServerMode.setStatus("mandatory")


class _HpnsaSiKeyboardLockPassword_Type(Integer32):
    """Custom type hpnsaSiKeyboardLockPassword based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("n-a", 0))
    )


_HpnsaSiKeyboardLockPassword_Type.__name__ = "Integer32"
_HpnsaSiKeyboardLockPassword_Object = MibScalar
hpnsaSiKeyboardLockPassword = _HpnsaSiKeyboardLockPassword_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 4, 3),
    _HpnsaSiKeyboardLockPassword_Type()
)
hpnsaSiKeyboardLockPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiKeyboardLockPassword.setStatus("mandatory")


class _HpnsaSiVideoBlankMode_Type(Integer32):
    """Custom type hpnsaSiVideoBlankMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("n-a", 0))
    )


_HpnsaSiVideoBlankMode_Type.__name__ = "Integer32"
_HpnsaSiVideoBlankMode_Object = MibScalar
hpnsaSiVideoBlankMode = _HpnsaSiVideoBlankMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 4, 4),
    _HpnsaSiVideoBlankMode_Type()
)
hpnsaSiVideoBlankMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiVideoBlankMode.setStatus("mandatory")


class _HpnsaSiBootDiskPriority_Type(Integer32):
    """Custom type hpnsaSiBootDiskPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("a-only", 4),
          ("a-then-c", 2),
          ("c-only", 3),
          ("c-then-a", 1),
          ("n-a", 0))
    )


_HpnsaSiBootDiskPriority_Type.__name__ = "Integer32"
_HpnsaSiBootDiskPriority_Object = MibScalar
hpnsaSiBootDiskPriority = _HpnsaSiBootDiskPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 4, 5),
    _HpnsaSiBootDiskPriority_Type()
)
hpnsaSiBootDiskPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiBootDiskPriority.setStatus("mandatory")


class _HpnsaSiWriteToFloppy_Type(Integer32):
    """Custom type hpnsaSiWriteToFloppy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("n-a", 0))
    )


_HpnsaSiWriteToFloppy_Type.__name__ = "Integer32"
_HpnsaSiWriteToFloppy_Object = MibScalar
hpnsaSiWriteToFloppy = _HpnsaSiWriteToFloppy_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 4, 6),
    _HpnsaSiWriteToFloppy_Type()
)
hpnsaSiWriteToFloppy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiWriteToFloppy.setStatus("mandatory")


class _HpnsaSiKbdMouseInactivityTO_Type(Integer32):
    """Custom type hpnsaSiKbdMouseInactivityTO based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("n-a", 0))
    )


_HpnsaSiKbdMouseInactivityTO_Type.__name__ = "Integer32"
_HpnsaSiKbdMouseInactivityTO_Object = MibScalar
hpnsaSiKbdMouseInactivityTO = _HpnsaSiKbdMouseInactivityTO_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 4, 7),
    _HpnsaSiKbdMouseInactivityTO_Type()
)
hpnsaSiKbdMouseInactivityTO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiKbdMouseInactivityTO.setStatus("mandatory")
_HpnsaSiPort_ObjectIdentity = ObjectIdentity
hpnsaSiPort = _HpnsaSiPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 5)
)
_HpnsaSiPortTable_Object = MibTable
hpnsaSiPortTable = _HpnsaSiPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 5, 1)
)
if mibBuilder.loadTexts:
    hpnsaSiPortTable.setStatus("mandatory")
_HpnsaSiPortEntry_Object = MibTableRow
hpnsaSiPortEntry = _HpnsaSiPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 5, 1, 1)
)
hpnsaSiPortEntry.setIndexNames(
    (0, "HPNSASINFO-MIB", "hpnsaSiPortIndex"),
)
if mibBuilder.loadTexts:
    hpnsaSiPortEntry.setStatus("mandatory")
_HpnsaSiPortIndex_Type = Integer32
_HpnsaSiPortIndex_Object = MibTableColumn
hpnsaSiPortIndex = _HpnsaSiPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 5, 1, 1, 1),
    _HpnsaSiPortIndex_Type()
)
hpnsaSiPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiPortIndex.setStatus("mandatory")


class _HpnsaSiPortType_Type(Integer32):
    """Custom type hpnsaSiPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("parallel", 2),
          ("serial", 1))
    )


_HpnsaSiPortType_Type.__name__ = "Integer32"
_HpnsaSiPortType_Object = MibTableColumn
hpnsaSiPortType = _HpnsaSiPortType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 5, 1, 1, 2),
    _HpnsaSiPortType_Type()
)
hpnsaSiPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiPortType.setStatus("mandatory")
_HpnsaSiPortStartAddress_Type = Integer32
_HpnsaSiPortStartAddress_Object = MibTableColumn
hpnsaSiPortStartAddress = _HpnsaSiPortStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 5, 1, 1, 3),
    _HpnsaSiPortStartAddress_Type()
)
hpnsaSiPortStartAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiPortStartAddress.setStatus("mandatory")
_HpnsaSiPortEndAddress_Type = Integer32
_HpnsaSiPortEndAddress_Object = MibTableColumn
hpnsaSiPortEndAddress = _HpnsaSiPortEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 5, 1, 1, 4),
    _HpnsaSiPortEndAddress_Type()
)
hpnsaSiPortEndAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiPortEndAddress.setStatus("mandatory")
_HpnsaSiPortInterruptNum_Type = Integer32
_HpnsaSiPortInterruptNum_Object = MibTableColumn
hpnsaSiPortInterruptNum = _HpnsaSiPortInterruptNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 5, 1, 1, 5),
    _HpnsaSiPortInterruptNum_Type()
)
hpnsaSiPortInterruptNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiPortInterruptNum.setStatus("mandatory")
_HpnsaSiMemory_ObjectIdentity = ObjectIdentity
hpnsaSiMemory = _HpnsaSiMemory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 6)
)


class _HpnsaSiBaseMemSize_Type(Integer32):
    """Custom type hpnsaSiBaseMemSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnsaSiBaseMemSize_Type.__name__ = "Integer32"
_HpnsaSiBaseMemSize_Object = MibScalar
hpnsaSiBaseMemSize = _HpnsaSiBaseMemSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 6, 1),
    _HpnsaSiBaseMemSize_Type()
)
hpnsaSiBaseMemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiBaseMemSize.setStatus("mandatory")


class _HpnsaSiExtMemSize_Type(Integer32):
    """Custom type hpnsaSiExtMemSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnsaSiExtMemSize_Type.__name__ = "Integer32"
_HpnsaSiExtMemSize_Object = MibScalar
hpnsaSiExtMemSize = _HpnsaSiExtMemSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 6, 2),
    _HpnsaSiExtMemSize_Type()
)
hpnsaSiExtMemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiExtMemSize.setStatus("mandatory")


class _HpnsaSiMemType_Type(Integer32):
    """Custom type hpnsaSiMemType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("doubleWidthModule", 3),
          ("on-board", 1),
          ("other", 0),
          ("simm", 4),
          ("singleWidthModule", 2))
    )


_HpnsaSiMemType_Type.__name__ = "Integer32"
_HpnsaSiMemType_Object = MibScalar
hpnsaSiMemType = _HpnsaSiMemType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 6, 3),
    _HpnsaSiMemType_Type()
)
hpnsaSiMemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiMemType.setStatus("optional")


class _HpnsaSiMemSpeed_Type(Integer32):
    """Custom type hpnsaSiMemSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnsaSiMemSpeed_Type.__name__ = "Integer32"
_HpnsaSiMemSpeed_Object = MibScalar
hpnsaSiMemSpeed = _HpnsaSiMemSpeed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 6, 4),
    _HpnsaSiMemSpeed_Type()
)
hpnsaSiMemSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiMemSpeed.setStatus("optional")
_HpnsaSiFloppyDrive_ObjectIdentity = ObjectIdentity
hpnsaSiFloppyDrive = _HpnsaSiFloppyDrive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 8)
)
_HpnsaSiNumFloppyDrives_Type = Integer32
_HpnsaSiNumFloppyDrives_Object = MibScalar
hpnsaSiNumFloppyDrives = _HpnsaSiNumFloppyDrives_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 8, 1),
    _HpnsaSiNumFloppyDrives_Type()
)
hpnsaSiNumFloppyDrives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiNumFloppyDrives.setStatus("mandatory")
_HpnsaSiFloppyDriveTable_Object = MibTable
hpnsaSiFloppyDriveTable = _HpnsaSiFloppyDriveTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 8, 2)
)
if mibBuilder.loadTexts:
    hpnsaSiFloppyDriveTable.setStatus("mandatory")
_HpnsaSiFloppyDriveEntry_Object = MibTableRow
hpnsaSiFloppyDriveEntry = _HpnsaSiFloppyDriveEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 8, 2, 1)
)
hpnsaSiFloppyDriveEntry.setIndexNames(
    (0, "HPNSASINFO-MIB", "hpnsaSiFloppyDriveIndex"),
)
if mibBuilder.loadTexts:
    hpnsaSiFloppyDriveEntry.setStatus("mandatory")
_HpnsaSiFloppyDriveIndex_Type = Integer32
_HpnsaSiFloppyDriveIndex_Object = MibTableColumn
hpnsaSiFloppyDriveIndex = _HpnsaSiFloppyDriveIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 8, 2, 1, 1),
    _HpnsaSiFloppyDriveIndex_Type()
)
hpnsaSiFloppyDriveIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiFloppyDriveIndex.setStatus("mandatory")


class _HpnsaSiFloppyDriveType_Type(Integer32):
    """Custom type hpnsaSiFloppyDriveType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("m-1-2-MB", 3),
          ("m-1-2MB", 2),
          ("m-1-44MB", 4),
          ("m-360K", 1),
          ("unknown", 0))
    )


_HpnsaSiFloppyDriveType_Type.__name__ = "Integer32"
_HpnsaSiFloppyDriveType_Object = MibTableColumn
hpnsaSiFloppyDriveType = _HpnsaSiFloppyDriveType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 8, 2, 1, 2),
    _HpnsaSiFloppyDriveType_Type()
)
hpnsaSiFloppyDriveType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiFloppyDriveType.setStatus("mandatory")
_HpnsaSiRemoteLocatorLED_ObjectIdentity = ObjectIdentity
hpnsaSiRemoteLocatorLED = _HpnsaSiRemoteLocatorLED_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 9)
)


class _HpnsaSiRemoteLocatorLEDSupported_Type(Integer32):
    """Custom type hpnsaSiRemoteLocatorLEDSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notsupported", 0),
          ("supported", 1))
    )


_HpnsaSiRemoteLocatorLEDSupported_Type.__name__ = "Integer32"
_HpnsaSiRemoteLocatorLEDSupported_Object = MibScalar
hpnsaSiRemoteLocatorLEDSupported = _HpnsaSiRemoteLocatorLEDSupported_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 9, 1),
    _HpnsaSiRemoteLocatorLEDSupported_Type()
)
hpnsaSiRemoteLocatorLEDSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiRemoteLocatorLEDSupported.setStatus("mandatory")


class _HpnsaSiRemoteLocatorLEDStatus_Type(Integer32):
    """Custom type hpnsaSiRemoteLocatorLEDStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ledoff", 0),
          ("ledon", 1))
    )


_HpnsaSiRemoteLocatorLEDStatus_Type.__name__ = "Integer32"
_HpnsaSiRemoteLocatorLEDStatus_Object = MibScalar
hpnsaSiRemoteLocatorLEDStatus = _HpnsaSiRemoteLocatorLEDStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 9, 2),
    _HpnsaSiRemoteLocatorLEDStatus_Type()
)
hpnsaSiRemoteLocatorLEDStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnsaSiRemoteLocatorLEDStatus.setStatus("mandatory")


class _HpnsaSiRemoteLocatorLEDSet_Type(Integer32):
    """Custom type hpnsaSiRemoteLocatorLEDSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ledoff", 0),
          ("ledon", 1))
    )


_HpnsaSiRemoteLocatorLEDSet_Type.__name__ = "Integer32"
_HpnsaSiRemoteLocatorLEDSet_Object = MibScalar
hpnsaSiRemoteLocatorLEDSet = _HpnsaSiRemoteLocatorLEDSet_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 7, 9, 3),
    _HpnsaSiRemoteLocatorLEDSet_Type()
)
hpnsaSiRemoteLocatorLEDSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnsaSiRemoteLocatorLEDSet.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPNSASINFO-MIB",
    **{"hp": hp,
       "nm": nm,
       "hpnsa": hpnsa,
       "hpnsaSystemInfo": hpnsaSystemInfo,
       "hpnsaSiMibRev": hpnsaSiMibRev,
       "hpnsaSiMibRevMajor": hpnsaSiMibRevMajor,
       "hpnsaSiMibRevMinor": hpnsaSiMibRevMinor,
       "hpnsaSiAgent": hpnsaSiAgent,
       "hpnsaSiAgentTable": hpnsaSiAgentTable,
       "hpnsaSiAgentEntry": hpnsaSiAgentEntry,
       "hpnsaSiAgentIndex": hpnsaSiAgentIndex,
       "hpnsaSiAgentName": hpnsaSiAgentName,
       "hpnsaSiAgentVersion": hpnsaSiAgentVersion,
       "hpnsaSiAgentDate": hpnsaSiAgentDate,
       "hpnsaSiBasicInfo": hpnsaSiBasicInfo,
       "hpnsaSiModel": hpnsaSiModel,
       "hpnsaSiBIOSVersion": hpnsaSiBIOSVersion,
       "hpnsaSiVideoBIOSVersion": hpnsaSiVideoBIOSVersion,
       "hpnsaSiSCSIBIOSVersion": hpnsaSiSCSIBIOSVersion,
       "hpnsaSiNumEISASlots": hpnsaSiNumEISASlots,
       "hpnsaSiNumPCISlots": hpnsaSiNumPCISlots,
       "hpnsaSiNumCPU": hpnsaSiNumCPU,
       "hpnsaSiCPUTable": hpnsaSiCPUTable,
       "hpnsaSiCPUEntry": hpnsaSiCPUEntry,
       "hpnsaSiCPUIndex": hpnsaSiCPUIndex,
       "hpnsaSiCPUModel": hpnsaSiCPUModel,
       "hpnsaSiCPUSpeed": hpnsaSiCPUSpeed,
       "hpnsaSiOpSysType": hpnsaSiOpSysType,
       "hpnsaSiOpSysVer": hpnsaSiOpSysVer,
       "hpnsaSiSystemName": hpnsaSiSystemName,
       "hpnsaSiSystemID": hpnsaSiSystemID,
       "hpnsaSiKbdType": hpnsaSiKbdType,
       "hpnsaSiMouseType": hpnsaSiMouseType,
       "hpnsaSiVideoType": hpnsaSiVideoType,
       "hpnsaSiNumISASlots": hpnsaSiNumISASlots,
       "hpnsaSiModelName": hpnsaSiModelName,
       "hpnsaSiOpSysDescription": hpnsaSiOpSysDescription,
       "hpnsaSiSecurity": hpnsaSiSecurity,
       "hpnsaSiPowerOnPassword": hpnsaSiPowerOnPassword,
       "hpnsaSiNetServerMode": hpnsaSiNetServerMode,
       "hpnsaSiKeyboardLockPassword": hpnsaSiKeyboardLockPassword,
       "hpnsaSiVideoBlankMode": hpnsaSiVideoBlankMode,
       "hpnsaSiBootDiskPriority": hpnsaSiBootDiskPriority,
       "hpnsaSiWriteToFloppy": hpnsaSiWriteToFloppy,
       "hpnsaSiKbdMouseInactivityTO": hpnsaSiKbdMouseInactivityTO,
       "hpnsaSiPort": hpnsaSiPort,
       "hpnsaSiPortTable": hpnsaSiPortTable,
       "hpnsaSiPortEntry": hpnsaSiPortEntry,
       "hpnsaSiPortIndex": hpnsaSiPortIndex,
       "hpnsaSiPortType": hpnsaSiPortType,
       "hpnsaSiPortStartAddress": hpnsaSiPortStartAddress,
       "hpnsaSiPortEndAddress": hpnsaSiPortEndAddress,
       "hpnsaSiPortInterruptNum": hpnsaSiPortInterruptNum,
       "hpnsaSiMemory": hpnsaSiMemory,
       "hpnsaSiBaseMemSize": hpnsaSiBaseMemSize,
       "hpnsaSiExtMemSize": hpnsaSiExtMemSize,
       "hpnsaSiMemType": hpnsaSiMemType,
       "hpnsaSiMemSpeed": hpnsaSiMemSpeed,
       "hpnsaSiFloppyDrive": hpnsaSiFloppyDrive,
       "hpnsaSiNumFloppyDrives": hpnsaSiNumFloppyDrives,
       "hpnsaSiFloppyDriveTable": hpnsaSiFloppyDriveTable,
       "hpnsaSiFloppyDriveEntry": hpnsaSiFloppyDriveEntry,
       "hpnsaSiFloppyDriveIndex": hpnsaSiFloppyDriveIndex,
       "hpnsaSiFloppyDriveType": hpnsaSiFloppyDriveType,
       "hpnsaSiRemoteLocatorLED": hpnsaSiRemoteLocatorLED,
       "hpnsaSiRemoteLocatorLEDSupported": hpnsaSiRemoteLocatorLEDSupported,
       "hpnsaSiRemoteLocatorLEDStatus": hpnsaSiRemoteLocatorLEDStatus,
       "hpnsaSiRemoteLocatorLEDSet": hpnsaSiRemoteLocatorLEDSet}
)
