# SNMP MIB module (TY3250I-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TY3250I-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:08:05 2024
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
 NotificationType,
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
    "NotificationType",
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

_Tylink_ObjectIdentity = ObjectIdentity
tylink = _Tylink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 466)
)
_Ty3250_ObjectIdentity = ObjectIdentity
ty3250 = _Ty3250_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 466, 4)
)
_Ty3250SysTable_ObjectIdentity = ObjectIdentity
ty3250SysTable = _Ty3250SysTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 466, 4, 1)
)


class _Ty3250SysType_Type(DisplayString):
    """Custom type ty3250SysType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_Ty3250SysType_Type.__name__ = "DisplayString"
_Ty3250SysType_Object = MibScalar
ty3250SysType = _Ty3250SysType_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 1, 1),
    _Ty3250SysType_Type()
)
ty3250SysType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty3250SysType.setStatus("mandatory")


class _Ty3250SysSoftRev_Type(DisplayString):
    """Custom type ty3250SysSoftRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_Ty3250SysSoftRev_Type.__name__ = "DisplayString"
_Ty3250SysSoftRev_Object = MibScalar
ty3250SysSoftRev = _Ty3250SysSoftRev_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 1, 2),
    _Ty3250SysSoftRev_Type()
)
ty3250SysSoftRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty3250SysSoftRev.setStatus("mandatory")


class _Ty3250SysHardRev_Type(DisplayString):
    """Custom type ty3250SysHardRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_Ty3250SysHardRev_Type.__name__ = "DisplayString"
_Ty3250SysHardRev_Object = MibScalar
ty3250SysHardRev = _Ty3250SysHardRev_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 1, 3),
    _Ty3250SysHardRev_Type()
)
ty3250SysHardRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty3250SysHardRev.setStatus("mandatory")


class _Ty3250SysNumT1Installed_Type(Integer32):
    """Custom type ty3250SysNumT1Installed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Ty3250SysNumT1Installed_Type.__name__ = "Integer32"
_Ty3250SysNumT1Installed_Object = MibScalar
ty3250SysNumT1Installed = _Ty3250SysNumT1Installed_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 1, 4),
    _Ty3250SysNumT1Installed_Type()
)
ty3250SysNumT1Installed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty3250SysNumT1Installed.setStatus("mandatory")


class _Ty3250SysNumDteInstalled_Type(Integer32):
    """Custom type ty3250SysNumDteInstalled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Ty3250SysNumDteInstalled_Type.__name__ = "Integer32"
_Ty3250SysNumDteInstalled_Object = MibScalar
ty3250SysNumDteInstalled = _Ty3250SysNumDteInstalled_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 1, 5),
    _Ty3250SysNumDteInstalled_Type()
)
ty3250SysNumDteInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty3250SysNumDteInstalled.setStatus("mandatory")


class _Ty3250SysNumCommInstalled_Type(Integer32):
    """Custom type ty3250SysNumCommInstalled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Ty3250SysNumCommInstalled_Type.__name__ = "Integer32"
_Ty3250SysNumCommInstalled_Object = MibScalar
ty3250SysNumCommInstalled = _Ty3250SysNumCommInstalled_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 1, 6),
    _Ty3250SysNumCommInstalled_Type()
)
ty3250SysNumCommInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty3250SysNumCommInstalled.setStatus("mandatory")


class _Ty3250SysName_Type(DisplayString):
    """Custom type ty3250SysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Ty3250SysName_Type.__name__ = "DisplayString"
_Ty3250SysName_Object = MibScalar
ty3250SysName = _Ty3250SysName_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 1, 7),
    _Ty3250SysName_Type()
)
ty3250SysName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ty3250SysName.setStatus("mandatory")


class _Ty3250SysResetNode_Type(Integer32):
    """Custom type ty3250SysResetNode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            321
        )
    )
    namedValues = NamedValues(
        ("reset-node", 321)
    )


_Ty3250SysResetNode_Type.__name__ = "Integer32"
_Ty3250SysResetNode_Object = MibScalar
ty3250SysResetNode = _Ty3250SysResetNode_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 1, 8),
    _Ty3250SysResetNode_Type()
)
ty3250SysResetNode.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    ty3250SysResetNode.setStatus("mandatory")
_Ty3250CfgT1Table_ObjectIdentity = ObjectIdentity
ty3250CfgT1Table = _Ty3250CfgT1Table_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 466, 4, 3)
)


class _Ty3250CfgT1Framing_Type(Integer32):
    """Custom type ty3250CfgT1Framing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("d4", 1),
          ("esf-54016", 2),
          ("esf-ansi", 3))
    )


_Ty3250CfgT1Framing_Type.__name__ = "Integer32"
_Ty3250CfgT1Framing_Object = MibScalar
ty3250CfgT1Framing = _Ty3250CfgT1Framing_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 3, 1),
    _Ty3250CfgT1Framing_Type()
)
ty3250CfgT1Framing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ty3250CfgT1Framing.setStatus("mandatory")


class _Ty3250CfgT1LineEncoding_Type(Integer32):
    """Custom type ty3250CfgT1LineEncoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ami", 1),
          ("b8zs", 2))
    )


_Ty3250CfgT1LineEncoding_Type.__name__ = "Integer32"
_Ty3250CfgT1LineEncoding_Object = MibScalar
ty3250CfgT1LineEncoding = _Ty3250CfgT1LineEncoding_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 3, 2),
    _Ty3250CfgT1LineEncoding_Type()
)
ty3250CfgT1LineEncoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ty3250CfgT1LineEncoding.setStatus("mandatory")


class _Ty3250CfgT1Density_Type(Integer32):
    """Custom type ty3250CfgT1Density based on Integer32"""
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
        *(("no-density", 1),
          ("one-in-16", 3),
          ("one-in-64", 4),
          ("twelve-half-percent", 2))
    )


_Ty3250CfgT1Density_Type.__name__ = "Integer32"
_Ty3250CfgT1Density_Object = MibScalar
ty3250CfgT1Density = _Ty3250CfgT1Density_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 3, 3),
    _Ty3250CfgT1Density_Type()
)
ty3250CfgT1Density.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ty3250CfgT1Density.setStatus("mandatory")


class _Ty3250CfgT1Interface_Type(Integer32):
    """Custom type ty3250CfgT1Interface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("csu", 2),
          ("dsx-1", 1))
    )


_Ty3250CfgT1Interface_Type.__name__ = "Integer32"
_Ty3250CfgT1Interface_Object = MibScalar
ty3250CfgT1Interface = _Ty3250CfgT1Interface_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 3, 4),
    _Ty3250CfgT1Interface_Type()
)
ty3250CfgT1Interface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ty3250CfgT1Interface.setStatus("mandatory")


class _Ty3250CfgT1LboSetting_Type(Integer32):
    """Custom type ty3250CfgT1LboSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("n15-db", 1),
          ("n7-5-db", 3),
          ("zero-db", 2))
    )


_Ty3250CfgT1LboSetting_Type.__name__ = "Integer32"
_Ty3250CfgT1LboSetting_Object = MibScalar
ty3250CfgT1LboSetting = _Ty3250CfgT1LboSetting_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 3, 5),
    _Ty3250CfgT1LboSetting_Type()
)
ty3250CfgT1LboSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ty3250CfgT1LboSetting.setStatus("mandatory")


class _Ty3250CfgT1Timing_Type(Integer32):
    """Custom type ty3250CfgT1Timing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("internal", 1),
          ("loop", 2))
    )


_Ty3250CfgT1Timing_Type.__name__ = "Integer32"
_Ty3250CfgT1Timing_Object = MibScalar
ty3250CfgT1Timing = _Ty3250CfgT1Timing_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 3, 6),
    _Ty3250CfgT1Timing_Type()
)
ty3250CfgT1Timing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ty3250CfgT1Timing.setStatus("mandatory")


class _Ty3250CfgT1CicuitID_Type(DisplayString):
    """Custom type ty3250CfgT1CicuitID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Ty3250CfgT1CicuitID_Type.__name__ = "DisplayString"
_Ty3250CfgT1CicuitID_Object = MibScalar
ty3250CfgT1CicuitID = _Ty3250CfgT1CicuitID_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 3, 7),
    _Ty3250CfgT1CicuitID_Type()
)
ty3250CfgT1CicuitID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ty3250CfgT1CicuitID.setStatus("mandatory")
_Ty3250CfgDteTable_ObjectIdentity = ObjectIdentity
ty3250CfgDteTable = _Ty3250CfgDteTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 466, 4, 4)
)


class _Ty3250CfgDteLineRate_Type(Integer32):
    """Custom type ty3250CfgDteLineRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1536000),
    )


_Ty3250CfgDteLineRate_Type.__name__ = "Integer32"
_Ty3250CfgDteLineRate_Object = MibScalar
ty3250CfgDteLineRate = _Ty3250CfgDteLineRate_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 4, 1),
    _Ty3250CfgDteLineRate_Type()
)
ty3250CfgDteLineRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ty3250CfgDteLineRate.setStatus("mandatory")


class _Ty3250CfgDteChannelDensity_Type(Integer32):
    """Custom type ty3250CfgDteChannelDensity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(56,
              64)
        )
    )
    namedValues = NamedValues(
        *(("bit-7-stuff", 56),
          ("clear-channel", 64))
    )


_Ty3250CfgDteChannelDensity_Type.__name__ = "Integer32"
_Ty3250CfgDteChannelDensity_Object = MibScalar
ty3250CfgDteChannelDensity = _Ty3250CfgDteChannelDensity_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 4, 2),
    _Ty3250CfgDteChannelDensity_Type()
)
ty3250CfgDteChannelDensity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ty3250CfgDteChannelDensity.setStatus("mandatory")


class _Ty3250CfgDteTiming_Type(Integer32):
    """Custom type ty3250CfgDteTiming based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loop-1", 1),
          ("loop-2", 2))
    )


_Ty3250CfgDteTiming_Type.__name__ = "Integer32"
_Ty3250CfgDteTiming_Object = MibScalar
ty3250CfgDteTiming = _Ty3250CfgDteTiming_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 4, 3),
    _Ty3250CfgDteTiming_Type()
)
ty3250CfgDteTiming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ty3250CfgDteTiming.setStatus("mandatory")


class _Ty3250CfgDteClockMode_Type(Integer32):
    """Custom type ty3250CfgDteClockMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clock-invert", 2),
          ("clock-normal", 1))
    )


_Ty3250CfgDteClockMode_Type.__name__ = "Integer32"
_Ty3250CfgDteClockMode_Object = MibScalar
ty3250CfgDteClockMode = _Ty3250CfgDteClockMode_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 4, 4),
    _Ty3250CfgDteClockMode_Type()
)
ty3250CfgDteClockMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ty3250CfgDteClockMode.setStatus("mandatory")


class _Ty3250CfgDteDataMode_Type(Integer32):
    """Custom type ty3250CfgDteDataMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data-invert", 2),
          ("data-normal", 1))
    )


_Ty3250CfgDteDataMode_Type.__name__ = "Integer32"
_Ty3250CfgDteDataMode_Object = MibScalar
ty3250CfgDteDataMode = _Ty3250CfgDteDataMode_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 4, 5),
    _Ty3250CfgDteDataMode_Type()
)
ty3250CfgDteDataMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ty3250CfgDteDataMode.setStatus("mandatory")


class _Ty3250CfgDteIntfType_Type(Integer32):
    """Custom type ty3250CfgDteIntfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("intf-rs449", 4),
          ("intf-v35", 3))
    )


_Ty3250CfgDteIntfType_Type.__name__ = "Integer32"
_Ty3250CfgDteIntfType_Object = MibScalar
ty3250CfgDteIntfType = _Ty3250CfgDteIntfType_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 4, 6),
    _Ty3250CfgDteIntfType_Type()
)
ty3250CfgDteIntfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ty3250CfgDteIntfType.setStatus("mandatory")
_Ty3250CfgConnectTable_ObjectIdentity = ObjectIdentity
ty3250CfgConnectTable = _Ty3250CfgConnectTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 466, 4, 5)
)
_Ty3250CfgConnAutoAssign_ObjectIdentity = ObjectIdentity
ty3250CfgConnAutoAssign = _Ty3250CfgConnAutoAssign_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 466, 4, 5, 1)
)


class _Ty3250ConnAutoT1Index_Type(Integer32):
    """Custom type ty3250ConnAutoT1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Ty3250ConnAutoT1Index_Type.__name__ = "Integer32"
_Ty3250ConnAutoT1Index_Object = MibScalar
ty3250ConnAutoT1Index = _Ty3250ConnAutoT1Index_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 5, 1, 1),
    _Ty3250ConnAutoT1Index_Type()
)
ty3250ConnAutoT1Index.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ty3250ConnAutoT1Index.setStatus("mandatory")


class _Ty3250ConnStartDS0_Type(Integer32):
    """Custom type ty3250ConnStartDS0 based on Integer32"""
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
              40,
              41)
        )
    )
    namedValues = NamedValues(
        *(("ds0-01", 1),
          ("ds0-02", 2),
          ("ds0-03", 3),
          ("ds0-04", 4),
          ("ds0-05", 5),
          ("ds0-06", 6),
          ("ds0-07", 7),
          ("ds0-08", 8),
          ("ds0-09", 9),
          ("ds0-10", 10),
          ("ds0-11", 11),
          ("ds0-12", 12),
          ("ds0-13", 13),
          ("ds0-14", 14),
          ("ds0-15", 15),
          ("ds0-16", 16),
          ("ds0-17", 17),
          ("ds0-18", 18),
          ("ds0-19", 19),
          ("ds0-20", 20),
          ("ds0-21", 21),
          ("ds0-22", 22),
          ("ds0-23", 23),
          ("ds0-24", 24),
          ("no-current-connections", 40),
          ("non-continuous-ds0s", 41))
    )


_Ty3250ConnStartDS0_Type.__name__ = "Integer32"
_Ty3250ConnStartDS0_Object = MibScalar
ty3250ConnStartDS0 = _Ty3250ConnStartDS0_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 5, 1, 2),
    _Ty3250ConnStartDS0_Type()
)
ty3250ConnStartDS0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ty3250ConnStartDS0.setStatus("mandatory")


class _Ty3250ConnAutoPort_Type(Integer32):
    """Custom type ty3250ConnAutoPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              33)
        )
    )
    namedValues = NamedValues(
        *(("not-connected", 33),
          ("port1-t1", 1),
          ("port2-dte", 2))
    )


_Ty3250ConnAutoPort_Type.__name__ = "Integer32"
_Ty3250ConnAutoPort_Object = MibScalar
ty3250ConnAutoPort = _Ty3250ConnAutoPort_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 5, 1, 3),
    _Ty3250ConnAutoPort_Type()
)
ty3250ConnAutoPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ty3250ConnAutoPort.setStatus("mandatory")


class _Ty3250ConnAutoType_Type(Integer32):
    """Custom type ty3250ConnAutoType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data", 1),
          ("voice", 2))
    )


_Ty3250ConnAutoType_Type.__name__ = "Integer32"
_Ty3250ConnAutoType_Object = MibScalar
ty3250ConnAutoType = _Ty3250ConnAutoType_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 5, 1, 4),
    _Ty3250ConnAutoType_Type()
)
ty3250ConnAutoType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ty3250ConnAutoType.setStatus("mandatory")


class _Ty3250ConnDteRate_Type(Integer32):
    """Custom type ty3250ConnDteRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1536000),
    )


_Ty3250ConnDteRate_Type.__name__ = "Integer32"
_Ty3250ConnDteRate_Object = MibScalar
ty3250ConnDteRate = _Ty3250ConnDteRate_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 5, 1, 5),
    _Ty3250ConnDteRate_Type()
)
ty3250ConnDteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty3250ConnDteRate.setStatus("mandatory")


class _Ty3250ConnDteDensity_Type(Integer32):
    """Custom type ty3250ConnDteDensity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(56,
              64)
        )
    )
    namedValues = NamedValues(
        *(("bit-7-stuff", 56),
          ("clear-channel", 64))
    )


_Ty3250ConnDteDensity_Type.__name__ = "Integer32"
_Ty3250ConnDteDensity_Object = MibScalar
ty3250ConnDteDensity = _Ty3250ConnDteDensity_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 5, 1, 6),
    _Ty3250ConnDteDensity_Type()
)
ty3250ConnDteDensity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty3250ConnDteDensity.setStatus("mandatory")


class _Ty3250ConnDs0Required_Type(Integer32):
    """Custom type ty3250ConnDs0Required based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_Ty3250ConnDs0Required_Type.__name__ = "Integer32"
_Ty3250ConnDs0Required_Object = MibScalar
ty3250ConnDs0Required = _Ty3250ConnDs0Required_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 5, 1, 7),
    _Ty3250ConnDs0Required_Type()
)
ty3250ConnDs0Required.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty3250ConnDs0Required.setStatus("mandatory")


class _Ty3250ConnAutoStatus_Type(Integer32):
    """Custom type ty3250ConnAutoStatus based on Integer32"""
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
        *(("bandwidth-conflict", 3),
          ("connections-valid", 1),
          ("incorrect-bandwidth", 2),
          ("no-current-connections", 4))
    )


_Ty3250ConnAutoStatus_Type.__name__ = "Integer32"
_Ty3250ConnAutoStatus_Object = MibScalar
ty3250ConnAutoStatus = _Ty3250ConnAutoStatus_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 5, 1, 8),
    _Ty3250ConnAutoStatus_Type()
)
ty3250ConnAutoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty3250ConnAutoStatus.setStatus("mandatory")
_Ty3250CfgCurrentConnTable_Object = MibTable
ty3250CfgCurrentConnTable = _Ty3250CfgCurrentConnTable_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 5, 2)
)
if mibBuilder.loadTexts:
    ty3250CfgCurrentConnTable.setStatus("mandatory")
_Ty3250CfgCurrentConnections_Object = MibTableRow
ty3250CfgCurrentConnections = _Ty3250CfgCurrentConnections_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 5, 2, 1)
)
ty3250CfgCurrentConnections.setIndexNames(
    (0, "TY3250I-MIB", "ty3250T1Index"),
    (0, "TY3250I-MIB", "ty3250Ds0"),
)
if mibBuilder.loadTexts:
    ty3250CfgCurrentConnections.setStatus("mandatory")


class _Ty3250T1Index_Type(Integer32):
    """Custom type ty3250T1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Ty3250T1Index_Type.__name__ = "Integer32"
_Ty3250T1Index_Object = MibTableColumn
ty3250T1Index = _Ty3250T1Index_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 5, 2, 1, 1),
    _Ty3250T1Index_Type()
)
ty3250T1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty3250T1Index.setStatus("mandatory")


class _Ty3250Ds0_Type(Integer32):
    """Custom type ty3250Ds0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Ty3250Ds0_Type.__name__ = "Integer32"
_Ty3250Ds0_Object = MibTableColumn
ty3250Ds0 = _Ty3250Ds0_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 5, 2, 1, 2),
    _Ty3250Ds0_Type()
)
ty3250Ds0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty3250Ds0.setStatus("mandatory")


class _Ty3250DtePort_Type(Integer32):
    """Custom type ty3250DtePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              33)
        )
    )
    namedValues = NamedValues(
        *(("not-connected", 33),
          ("port1-t1", 1),
          ("port2-dte", 2))
    )


_Ty3250DtePort_Type.__name__ = "Integer32"
_Ty3250DtePort_Object = MibTableColumn
ty3250DtePort = _Ty3250DtePort_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 5, 2, 1, 3),
    _Ty3250DtePort_Type()
)
ty3250DtePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty3250DtePort.setStatus("mandatory")


class _Ty3250Type_Type(Integer32):
    """Custom type ty3250Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data", 1),
          ("voice", 2))
    )


_Ty3250Type_Type.__name__ = "Integer32"
_Ty3250Type_Object = MibTableColumn
ty3250Type = _Ty3250Type_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 5, 2, 1, 4),
    _Ty3250Type_Type()
)
ty3250Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty3250Type.setStatus("mandatory")
_Ty3250CfgEditConnMenu_ObjectIdentity = ObjectIdentity
ty3250CfgEditConnMenu = _Ty3250CfgEditConnMenu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 466, 4, 5, 3)
)


class _Ty3250CfgEditConnCopyCurrtoEdit_Type(Integer32):
    """Custom type ty3250CfgEditConnCopyCurrtoEdit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("copy-current", 1)
    )


_Ty3250CfgEditConnCopyCurrtoEdit_Type.__name__ = "Integer32"
_Ty3250CfgEditConnCopyCurrtoEdit_Object = MibScalar
ty3250CfgEditConnCopyCurrtoEdit = _Ty3250CfgEditConnCopyCurrtoEdit_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 5, 3, 1),
    _Ty3250CfgEditConnCopyCurrtoEdit_Type()
)
ty3250CfgEditConnCopyCurrtoEdit.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    ty3250CfgEditConnCopyCurrtoEdit.setStatus("mandatory")
_Ty3250CfgEditConnTable_Object = MibTable
ty3250CfgEditConnTable = _Ty3250CfgEditConnTable_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 5, 3, 2)
)
if mibBuilder.loadTexts:
    ty3250CfgEditConnTable.setStatus("mandatory")
_Ty3250CfgEditConnEntry_Object = MibTableRow
ty3250CfgEditConnEntry = _Ty3250CfgEditConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 5, 3, 2, 1)
)
ty3250CfgEditConnEntry.setIndexNames(
    (0, "TY3250I-MIB", "ty3250ConnT1Index"),
    (0, "TY3250I-MIB", "ty3250ConnDS0"),
)
if mibBuilder.loadTexts:
    ty3250CfgEditConnEntry.setStatus("mandatory")


class _Ty3250ConnT1Index_Type(Integer32):
    """Custom type ty3250ConnT1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Ty3250ConnT1Index_Type.__name__ = "Integer32"
_Ty3250ConnT1Index_Object = MibTableColumn
ty3250ConnT1Index = _Ty3250ConnT1Index_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 5, 3, 2, 1, 1),
    _Ty3250ConnT1Index_Type()
)
ty3250ConnT1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty3250ConnT1Index.setStatus("mandatory")


class _Ty3250ConnDS0_Type(Integer32):
    """Custom type ty3250ConnDS0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Ty3250ConnDS0_Type.__name__ = "Integer32"
_Ty3250ConnDS0_Object = MibTableColumn
ty3250ConnDS0 = _Ty3250ConnDS0_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 5, 3, 2, 1, 2),
    _Ty3250ConnDS0_Type()
)
ty3250ConnDS0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty3250ConnDS0.setStatus("mandatory")


class _Ty3250ConnDTE_Type(Integer32):
    """Custom type ty3250ConnDTE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              33)
        )
    )
    namedValues = NamedValues(
        *(("not-connected", 33),
          ("port1-t1", 1),
          ("port2-dte", 2))
    )


_Ty3250ConnDTE_Type.__name__ = "Integer32"
_Ty3250ConnDTE_Object = MibTableColumn
ty3250ConnDTE = _Ty3250ConnDTE_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 5, 3, 2, 1, 3),
    _Ty3250ConnDTE_Type()
)
ty3250ConnDTE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ty3250ConnDTE.setStatus("mandatory")


class _Ty3250ConnType_Type(Integer32):
    """Custom type ty3250ConnType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("data", 1),
          ("voice", 2))
    )


_Ty3250ConnType_Type.__name__ = "Integer32"
_Ty3250ConnType_Object = MibTableColumn
ty3250ConnType = _Ty3250ConnType_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 5, 3, 2, 1, 4),
    _Ty3250ConnType_Type()
)
ty3250ConnType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ty3250ConnType.setStatus("mandatory")
_Ty3250CfgConnUpdate_ObjectIdentity = ObjectIdentity
ty3250CfgConnUpdate = _Ty3250CfgConnUpdate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 466, 4, 5, 3, 3)
)


class _Ty3250CfgConnUpdateCmd_Type(Integer32):
    """Custom type ty3250CfgConnUpdateCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("update", 1)
    )


_Ty3250CfgConnUpdateCmd_Type.__name__ = "Integer32"
_Ty3250CfgConnUpdateCmd_Object = MibScalar
ty3250CfgConnUpdateCmd = _Ty3250CfgConnUpdateCmd_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 5, 3, 3, 1),
    _Ty3250CfgConnUpdateCmd_Type()
)
ty3250CfgConnUpdateCmd.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    ty3250CfgConnUpdateCmd.setStatus("mandatory")


class _Ty3250CfgConnStatus_Type(Integer32):
    """Custom type ty3250CfgConnStatus based on Integer32"""
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
        *(("bandwidth-conflict", 3),
          ("connections-valid", 1),
          ("incorrect-bandwidth", 2),
          ("no-current-connections", 4))
    )


_Ty3250CfgConnStatus_Type.__name__ = "Integer32"
_Ty3250CfgConnStatus_Object = MibScalar
ty3250CfgConnStatus = _Ty3250CfgConnStatus_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 5, 3, 3, 2),
    _Ty3250CfgConnStatus_Type()
)
ty3250CfgConnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty3250CfgConnStatus.setStatus("mandatory")


class _Ty3250CfgEditConnClearEditBuff_Type(Integer32):
    """Custom type ty3250CfgEditConnClearEditBuff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear-edit", 1)
    )


_Ty3250CfgEditConnClearEditBuff_Type.__name__ = "Integer32"
_Ty3250CfgEditConnClearEditBuff_Object = MibScalar
ty3250CfgEditConnClearEditBuff = _Ty3250CfgEditConnClearEditBuff_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 5, 3, 4),
    _Ty3250CfgEditConnClearEditBuff_Type()
)
ty3250CfgEditConnClearEditBuff.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    ty3250CfgEditConnClearEditBuff.setStatus("mandatory")
_Ty3250CfgCommTable_ObjectIdentity = ObjectIdentity
ty3250CfgCommTable = _Ty3250CfgCommTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 466, 4, 6)
)
_Ty3250CfgCommFormat_Object = MibTable
ty3250CfgCommFormat = _Ty3250CfgCommFormat_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 6, 1)
)
if mibBuilder.loadTexts:
    ty3250CfgCommFormat.setStatus("mandatory")
_Ty3250CfgCommIntf_Object = MibTableRow
ty3250CfgCommIntf = _Ty3250CfgCommIntf_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 6, 1, 1)
)
ty3250CfgCommIntf.setIndexNames(
    (0, "TY3250I-MIB", "ty3250CfgCommIndex"),
)
if mibBuilder.loadTexts:
    ty3250CfgCommIntf.setStatus("mandatory")


class _Ty3250CfgCommIndex_Type(Integer32):
    """Custom type ty3250CfgCommIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("comm", 1),
          ("maint", 2))
    )


_Ty3250CfgCommIndex_Type.__name__ = "Integer32"
_Ty3250CfgCommIndex_Object = MibTableColumn
ty3250CfgCommIndex = _Ty3250CfgCommIndex_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 6, 1, 1, 1),
    _Ty3250CfgCommIndex_Type()
)
ty3250CfgCommIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty3250CfgCommIndex.setStatus("mandatory")


class _Ty3250CfgCommBaud_Type(Integer32):
    """Custom type ty3250CfgCommBaud based on Integer32"""
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
        *(("baud-1200", 1),
          ("baud-19200", 5),
          ("baud-2400", 2),
          ("baud-38400", 6),
          ("baud-4800", 3),
          ("baud-9600", 4))
    )


_Ty3250CfgCommBaud_Type.__name__ = "Integer32"
_Ty3250CfgCommBaud_Object = MibTableColumn
ty3250CfgCommBaud = _Ty3250CfgCommBaud_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 6, 1, 1, 2),
    _Ty3250CfgCommBaud_Type()
)
ty3250CfgCommBaud.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ty3250CfgCommBaud.setStatus("mandatory")


class _Ty3250CfgCommDataBits_Type(Integer32):
    """Custom type ty3250CfgCommDataBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("databits-7", 1),
          ("databits-8", 2))
    )


_Ty3250CfgCommDataBits_Type.__name__ = "Integer32"
_Ty3250CfgCommDataBits_Object = MibTableColumn
ty3250CfgCommDataBits = _Ty3250CfgCommDataBits_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 6, 1, 1, 3),
    _Ty3250CfgCommDataBits_Type()
)
ty3250CfgCommDataBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ty3250CfgCommDataBits.setStatus("mandatory")


class _Ty3250CfgCommStopBits_Type(Integer32):
    """Custom type ty3250CfgCommStopBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("stopbits-1", 1),
          ("stopbits-1-5", 2),
          ("stopbits-2", 3))
    )


_Ty3250CfgCommStopBits_Type.__name__ = "Integer32"
_Ty3250CfgCommStopBits_Object = MibTableColumn
ty3250CfgCommStopBits = _Ty3250CfgCommStopBits_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 6, 1, 1, 4),
    _Ty3250CfgCommStopBits_Type()
)
ty3250CfgCommStopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ty3250CfgCommStopBits.setStatus("mandatory")


class _Ty3250CfgCommParity_Type(Integer32):
    """Custom type ty3250CfgCommParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("even-parity", 3),
          ("no-parity", 1),
          ("odd-parity", 2))
    )


_Ty3250CfgCommParity_Type.__name__ = "Integer32"
_Ty3250CfgCommParity_Object = MibTableColumn
ty3250CfgCommParity = _Ty3250CfgCommParity_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 6, 1, 1, 5),
    _Ty3250CfgCommParity_Type()
)
ty3250CfgCommParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ty3250CfgCommParity.setStatus("mandatory")


class _Ty3250CfgCommFlowCtrl_Type(Integer32):
    """Custom type ty3250CfgCommFlowCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hardware-flow-control", 3),
          ("no-flow-control", 1),
          ("software-flow-control", 2))
    )


_Ty3250CfgCommFlowCtrl_Type.__name__ = "Integer32"
_Ty3250CfgCommFlowCtrl_Object = MibTableColumn
ty3250CfgCommFlowCtrl = _Ty3250CfgCommFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 6, 1, 1, 6),
    _Ty3250CfgCommFlowCtrl_Type()
)
ty3250CfgCommFlowCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ty3250CfgCommFlowCtrl.setStatus("mandatory")
_Ty3250CfgCommModeTable_Object = MibTable
ty3250CfgCommModeTable = _Ty3250CfgCommModeTable_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 6, 2)
)
if mibBuilder.loadTexts:
    ty3250CfgCommModeTable.setStatus("mandatory")
_Ty3250CfgCommModeEntry_Object = MibTableRow
ty3250CfgCommModeEntry = _Ty3250CfgCommModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 6, 2, 1)
)
ty3250CfgCommModeEntry.setIndexNames(
    (0, "TY3250I-MIB", "ty3250CfgCommModeIndex"),
)
if mibBuilder.loadTexts:
    ty3250CfgCommModeEntry.setStatus("mandatory")


class _Ty3250CfgCommModeIndex_Type(Integer32):
    """Custom type ty3250CfgCommModeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("comm", 1),
          ("maint", 2))
    )


_Ty3250CfgCommModeIndex_Type.__name__ = "Integer32"
_Ty3250CfgCommModeIndex_Object = MibTableColumn
ty3250CfgCommModeIndex = _Ty3250CfgCommModeIndex_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 6, 2, 1, 1),
    _Ty3250CfgCommModeIndex_Type()
)
ty3250CfgCommModeIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ty3250CfgCommModeIndex.setStatus("mandatory")


class _Ty3250CfgCommMode_Type(Integer32):
    """Custom type ty3250CfgCommMode based on Integer32"""
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
        *(("ethernet", 3),
          ("slip", 2),
          ("token-ring", 4),
          ("user-interface-vt100", 1))
    )


_Ty3250CfgCommMode_Type.__name__ = "Integer32"
_Ty3250CfgCommMode_Object = MibTableColumn
ty3250CfgCommMode = _Ty3250CfgCommMode_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 6, 2, 1, 2),
    _Ty3250CfgCommMode_Type()
)
ty3250CfgCommMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ty3250CfgCommMode.setStatus("mandatory")
_Ty3250CfgCommMyIP_Type = IpAddress
_Ty3250CfgCommMyIP_Object = MibTableColumn
ty3250CfgCommMyIP = _Ty3250CfgCommMyIP_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 6, 2, 1, 3),
    _Ty3250CfgCommMyIP_Type()
)
ty3250CfgCommMyIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ty3250CfgCommMyIP.setStatus("mandatory")
_Ty3250CfgCommPeerIP_Type = IpAddress
_Ty3250CfgCommPeerIP_Object = MibTableColumn
ty3250CfgCommPeerIP = _Ty3250CfgCommPeerIP_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 6, 2, 1, 4),
    _Ty3250CfgCommPeerIP_Type()
)
ty3250CfgCommPeerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ty3250CfgCommPeerIP.setStatus("mandatory")
_Ty3250CfgCommMask_Type = IpAddress
_Ty3250CfgCommMask_Object = MibTableColumn
ty3250CfgCommMask = _Ty3250CfgCommMask_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 6, 2, 1, 5),
    _Ty3250CfgCommMask_Type()
)
ty3250CfgCommMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ty3250CfgCommMask.setStatus("mandatory")


class _Ty3250CfgCommMaxMTU_Type(Integer32):
    """Custom type ty3250CfgCommMaxMTU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_Ty3250CfgCommMaxMTU_Type.__name__ = "Integer32"
_Ty3250CfgCommMaxMTU_Object = MibTableColumn
ty3250CfgCommMaxMTU = _Ty3250CfgCommMaxMTU_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 6, 2, 1, 6),
    _Ty3250CfgCommMaxMTU_Type()
)
ty3250CfgCommMaxMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ty3250CfgCommMaxMTU.setStatus("mandatory")
_Ty3250CfgSnmpTable_Object = MibTable
ty3250CfgSnmpTable = _Ty3250CfgSnmpTable_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 7)
)
if mibBuilder.loadTexts:
    ty3250CfgSnmpTable.setStatus("mandatory")
_Ty3250SnmpEntry_Object = MibTableRow
ty3250SnmpEntry = _Ty3250SnmpEntry_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 7, 1)
)
ty3250SnmpEntry.setIndexNames(
    (0, "TY3250I-MIB", "ty3250SnmpIndex"),
)
if mibBuilder.loadTexts:
    ty3250SnmpEntry.setStatus("mandatory")


class _Ty3250SnmpIndex_Type(Integer32):
    """Custom type ty3250SnmpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Ty3250SnmpIndex_Type.__name__ = "Integer32"
_Ty3250SnmpIndex_Object = MibTableColumn
ty3250SnmpIndex = _Ty3250SnmpIndex_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 7, 1, 1),
    _Ty3250SnmpIndex_Type()
)
ty3250SnmpIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ty3250SnmpIndex.setStatus("mandatory")
_Ty3250SnmpManagerIP_Type = IpAddress
_Ty3250SnmpManagerIP_Object = MibTableColumn
ty3250SnmpManagerIP = _Ty3250SnmpManagerIP_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 7, 1, 2),
    _Ty3250SnmpManagerIP_Type()
)
ty3250SnmpManagerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ty3250SnmpManagerIP.setStatus("mandatory")
_Ty3250DiagT1Table_ObjectIdentity = ObjectIdentity
ty3250DiagT1Table = _Ty3250DiagT1Table_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 466, 4, 10)
)


class _Ty3250DiagT1LocLineLpbk_Type(Integer32):
    """Custom type ty3250DiagT1LocLineLpbk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("line-lpbk-disable", 1),
          ("line-lpbk-enable", 2))
    )


_Ty3250DiagT1LocLineLpbk_Type.__name__ = "Integer32"
_Ty3250DiagT1LocLineLpbk_Object = MibScalar
ty3250DiagT1LocLineLpbk = _Ty3250DiagT1LocLineLpbk_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 10, 1),
    _Ty3250DiagT1LocLineLpbk_Type()
)
ty3250DiagT1LocLineLpbk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ty3250DiagT1LocLineLpbk.setStatus("mandatory")


class _Ty3250DiagT1LocPylLpbk_Type(Integer32):
    """Custom type ty3250DiagT1LocPylLpbk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pyl-lpbk-disable", 1),
          ("pyl-lpbk-enable", 2))
    )


_Ty3250DiagT1LocPylLpbk_Type.__name__ = "Integer32"
_Ty3250DiagT1LocPylLpbk_Object = MibScalar
ty3250DiagT1LocPylLpbk = _Ty3250DiagT1LocPylLpbk_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 10, 2),
    _Ty3250DiagT1LocPylLpbk_Type()
)
ty3250DiagT1LocPylLpbk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ty3250DiagT1LocPylLpbk.setStatus("mandatory")


class _Ty3250DiagT1LocAggrLpbk_Type(Integer32):
    """Custom type ty3250DiagT1LocAggrLpbk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aggr-lpbk-disable", 1),
          ("aggr-lpbk-enable", 2))
    )


_Ty3250DiagT1LocAggrLpbk_Type.__name__ = "Integer32"
_Ty3250DiagT1LocAggrLpbk_Object = MibScalar
ty3250DiagT1LocAggrLpbk = _Ty3250DiagT1LocAggrLpbk_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 10, 3),
    _Ty3250DiagT1LocAggrLpbk_Type()
)
ty3250DiagT1LocAggrLpbk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ty3250DiagT1LocAggrLpbk.setStatus("mandatory")


class _Ty3250DiagT1RmtLpbkStatus_Type(Integer32):
    """Custom type ty3250DiagT1RmtLpbkStatus based on Integer32"""
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
        *(("csu-lpbk-from-remote", 2),
          ("csu-lpbk-sent-to-remote", 5),
          ("dsu-lpbk-from-remote", 3),
          ("dsu-lpbk-sent-to-remote", 6),
          ("no-remote-lpbks", 1),
          ("pyl-lpbk-from-remote", 4))
    )


_Ty3250DiagT1RmtLpbkStatus_Type.__name__ = "Integer32"
_Ty3250DiagT1RmtLpbkStatus_Object = MibScalar
ty3250DiagT1RmtLpbkStatus = _Ty3250DiagT1RmtLpbkStatus_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 10, 4),
    _Ty3250DiagT1RmtLpbkStatus_Type()
)
ty3250DiagT1RmtLpbkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty3250DiagT1RmtLpbkStatus.setStatus("mandatory")


class _Ty3250DiagT1RmtLpbkCmd_Type(Integer32):
    """Custom type ty3250DiagT1RmtLpbkCmd based on Integer32"""
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
        *(("rmt-csu-lpbk-loopdown", 2),
          ("rmt-csu-lpbk-loopup", 1),
          ("rmt-dsu-lpbk-loopdown", 4),
          ("rmt-dsu-lpbk-loopup", 3))
    )


_Ty3250DiagT1RmtLpbkCmd_Type.__name__ = "Integer32"
_Ty3250DiagT1RmtLpbkCmd_Object = MibScalar
ty3250DiagT1RmtLpbkCmd = _Ty3250DiagT1RmtLpbkCmd_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 10, 5),
    _Ty3250DiagT1RmtLpbkCmd_Type()
)
ty3250DiagT1RmtLpbkCmd.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    ty3250DiagT1RmtLpbkCmd.setStatus("mandatory")
_Ty3250DiagDteTable_ObjectIdentity = ObjectIdentity
ty3250DiagDteTable = _Ty3250DiagDteTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 466, 4, 11)
)


class _Ty3250DiagDteLocBidirLpbk_Type(Integer32):
    """Custom type ty3250DiagDteLocBidirLpbk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bidir-lpbk-disable", 1),
          ("bidir-lpbk-enable", 2))
    )


_Ty3250DiagDteLocBidirLpbk_Type.__name__ = "Integer32"
_Ty3250DiagDteLocBidirLpbk_Object = MibScalar
ty3250DiagDteLocBidirLpbk = _Ty3250DiagDteLocBidirLpbk_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 11, 1),
    _Ty3250DiagDteLocBidirLpbk_Type()
)
ty3250DiagDteLocBidirLpbk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ty3250DiagDteLocBidirLpbk.setStatus("mandatory")


class _Ty3250DiagDteRmtLpbkStatus_Type(Integer32):
    """Custom type ty3250DiagDteRmtLpbkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bidir-lpbk-from-remote", 2),
          ("bidir-lpbk-sent-to-remote", 3),
          ("no-remote-lpbks", 1))
    )


_Ty3250DiagDteRmtLpbkStatus_Type.__name__ = "Integer32"
_Ty3250DiagDteRmtLpbkStatus_Object = MibScalar
ty3250DiagDteRmtLpbkStatus = _Ty3250DiagDteRmtLpbkStatus_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 11, 2),
    _Ty3250DiagDteRmtLpbkStatus_Type()
)
ty3250DiagDteRmtLpbkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty3250DiagDteRmtLpbkStatus.setStatus("mandatory")


class _Ty3250DiagDteRmtLpbkCmd_Type(Integer32):
    """Custom type ty3250DiagDteRmtLpbkCmd based on Integer32"""
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
        *(("rmt-bidir-lpbk-loopdown-tyl", 2),
          ("rmt-bidir-lpbk-loopdown-v54", 4),
          ("rmt-bidir-lpbk-loopup-tyl", 1),
          ("rmt-bidir-lpbk-loopup-v54", 3))
    )


_Ty3250DiagDteRmtLpbkCmd_Type.__name__ = "Integer32"
_Ty3250DiagDteRmtLpbkCmd_Object = MibScalar
ty3250DiagDteRmtLpbkCmd = _Ty3250DiagDteRmtLpbkCmd_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 11, 3),
    _Ty3250DiagDteRmtLpbkCmd_Type()
)
ty3250DiagDteRmtLpbkCmd.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    ty3250DiagDteRmtLpbkCmd.setStatus("mandatory")
_Ty3250DiagBerTable_ObjectIdentity = ObjectIdentity
ty3250DiagBerTable = _Ty3250DiagBerTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 466, 4, 12)
)


class _Ty3250DiagBerPattrn_Type(Integer32):
    """Custom type ty3250DiagBerPattrn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pattrn-511", 1),
          ("pattrn-qrss", 2))
    )


_Ty3250DiagBerPattrn_Type.__name__ = "Integer32"
_Ty3250DiagBerPattrn_Object = MibScalar
ty3250DiagBerPattrn = _Ty3250DiagBerPattrn_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 12, 1),
    _Ty3250DiagBerPattrn_Type()
)
ty3250DiagBerPattrn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ty3250DiagBerPattrn.setStatus("mandatory")


class _Ty3250DiagBerState_Type(Integer32):
    """Custom type ty3250DiagBerState based on Integer32"""
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
        *(("clear-error-bert-test", 5),
          ("disable-bert-test", 3),
          ("enable-t1-bert-on-DTE-bw", 2),
          ("enable-t1-bert-on-full-bw", 1),
          ("inject-error-bert-test", 4))
    )


_Ty3250DiagBerState_Type.__name__ = "Integer32"
_Ty3250DiagBerState_Object = MibScalar
ty3250DiagBerState = _Ty3250DiagBerState_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 12, 2),
    _Ty3250DiagBerState_Type()
)
ty3250DiagBerState.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    ty3250DiagBerState.setStatus("mandatory")


class _Ty3250DiagBerStatus_Type(Integer32):
    """Custom type ty3250DiagBerStatus based on Integer32"""
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
        *(("bert-DTE-bw-in-sync", 5),
          ("bert-DTE-bw-out-of-sync", 3),
          ("bert-full-bw-in-sync", 4),
          ("bert-full-bw-out-of-sync", 2),
          ("bert-off", 1))
    )


_Ty3250DiagBerStatus_Type.__name__ = "Integer32"
_Ty3250DiagBerStatus_Object = MibScalar
ty3250DiagBerStatus = _Ty3250DiagBerStatus_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 12, 3),
    _Ty3250DiagBerStatus_Type()
)
ty3250DiagBerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty3250DiagBerStatus.setStatus("mandatory")
_Ty3250DiagBerErrors_Type = Counter32
_Ty3250DiagBerErrors_Object = MibScalar
ty3250DiagBerErrors = _Ty3250DiagBerErrors_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 12, 4),
    _Ty3250DiagBerErrors_Type()
)
ty3250DiagBerErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty3250DiagBerErrors.setStatus("mandatory")
_Ty3250DiagBerTimeElaps_Type = TimeTicks
_Ty3250DiagBerTimeElaps_Object = MibScalar
ty3250DiagBerTimeElaps = _Ty3250DiagBerTimeElaps_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 12, 5),
    _Ty3250DiagBerTimeElaps_Type()
)
ty3250DiagBerTimeElaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty3250DiagBerTimeElaps.setStatus("mandatory")
_Ty3250PortStatusTable_Object = MibTable
ty3250PortStatusTable = _Ty3250PortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 13)
)
if mibBuilder.loadTexts:
    ty3250PortStatusTable.setStatus("mandatory")
_Ty3250PortStatus_Object = MibTableRow
ty3250PortStatus = _Ty3250PortStatus_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 13, 1)
)
ty3250PortStatus.setIndexNames(
    (0, "TY3250I-MIB", "ty3250IntfIndex"),
)
if mibBuilder.loadTexts:
    ty3250PortStatus.setStatus("mandatory")


class _Ty3250IntfIndex_Type(Integer32):
    """Custom type ty3250IntfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Ty3250IntfIndex_Type.__name__ = "Integer32"
_Ty3250IntfIndex_Object = MibTableColumn
ty3250IntfIndex = _Ty3250IntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 13, 1, 1),
    _Ty3250IntfIndex_Type()
)
ty3250IntfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty3250IntfIndex.setStatus("mandatory")


class _Ty3250IntfType_Type(Integer32):
    """Custom type ty3250IntfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dte-port", 2),
          ("t1-port", 1))
    )


_Ty3250IntfType_Type.__name__ = "Integer32"
_Ty3250IntfType_Object = MibTableColumn
ty3250IntfType = _Ty3250IntfType_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 13, 1, 2),
    _Ty3250IntfType_Type()
)
ty3250IntfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty3250IntfType.setStatus("mandatory")


class _Ty3250IntfMode_Type(Integer32):
    """Custom type ty3250IntfMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1),
          ("test-mode", 3))
    )


_Ty3250IntfMode_Type.__name__ = "Integer32"
_Ty3250IntfMode_Object = MibTableColumn
ty3250IntfMode = _Ty3250IntfMode_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 13, 1, 3),
    _Ty3250IntfMode_Type()
)
ty3250IntfMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty3250IntfMode.setStatus("mandatory")


class _Ty3250IntfStatus_Type(Integer32):
    """Custom type ty3250IntfStatus based on Integer32"""
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
        *(("not-applicable", 5),
          ("signal-not-present", 4),
          ("signal-present-without-frame-sync", 3),
          ("t1-frame-sync-okay", 1),
          ("t1-frame-sync-with-errors", 2))
    )


_Ty3250IntfStatus_Type.__name__ = "Integer32"
_Ty3250IntfStatus_Object = MibTableColumn
ty3250IntfStatus = _Ty3250IntfStatus_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 13, 1, 4),
    _Ty3250IntfStatus_Type()
)
ty3250IntfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty3250IntfStatus.setStatus("mandatory")


class _Ty3250IntfAlarms_Type(Integer32):
    """Custom type ty3250IntfAlarms based on Integer32"""
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
        *(("no-alarms", 1),
          ("red-alarm-declared", 2),
          ("unframed-all-ones-detected", 4),
          ("yellow-alarm-detected", 3))
    )


_Ty3250IntfAlarms_Type.__name__ = "Integer32"
_Ty3250IntfAlarms_Object = MibTableColumn
ty3250IntfAlarms = _Ty3250IntfAlarms_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 13, 1, 5),
    _Ty3250IntfAlarms_Type()
)
ty3250IntfAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty3250IntfAlarms.setStatus("mandatory")
_Ty3250PerfT1CurrentTable_Object = MibTable
ty3250PerfT1CurrentTable = _Ty3250PerfT1CurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 14)
)
if mibBuilder.loadTexts:
    ty3250PerfT1CurrentTable.setStatus("mandatory")
_Ty3250T1CurrentEntry_Object = MibTableRow
ty3250T1CurrentEntry = _Ty3250T1CurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 14, 1)
)
ty3250T1CurrentEntry.setIndexNames(
    (0, "TY3250I-MIB", "ty3250T1CurrentIndex"),
)
if mibBuilder.loadTexts:
    ty3250T1CurrentEntry.setStatus("mandatory")


class _Ty3250T1CurrentIndex_Type(Integer32):
    """Custom type ty3250T1CurrentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Ty3250T1CurrentIndex_Type.__name__ = "Integer32"
_Ty3250T1CurrentIndex_Object = MibTableColumn
ty3250T1CurrentIndex = _Ty3250T1CurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 14, 1, 1),
    _Ty3250T1CurrentIndex_Type()
)
ty3250T1CurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty3250T1CurrentIndex.setStatus("mandatory")
_Ty3250T1CurrentCrc6Events_Type = Gauge32
_Ty3250T1CurrentCrc6Events_Object = MibTableColumn
ty3250T1CurrentCrc6Events = _Ty3250T1CurrentCrc6Events_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 14, 1, 2),
    _Ty3250T1CurrentCrc6Events_Type()
)
ty3250T1CurrentCrc6Events.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty3250T1CurrentCrc6Events.setStatus("mandatory")
_Ty3250T1CurrentOofEvents_Type = Gauge32
_Ty3250T1CurrentOofEvents_Object = MibTableColumn
ty3250T1CurrentOofEvents = _Ty3250T1CurrentOofEvents_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 14, 1, 3),
    _Ty3250T1CurrentOofEvents_Type()
)
ty3250T1CurrentOofEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty3250T1CurrentOofEvents.setStatus("mandatory")
_Ty3250T1CurrentESs_Type = Gauge32
_Ty3250T1CurrentESs_Object = MibTableColumn
ty3250T1CurrentESs = _Ty3250T1CurrentESs_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 14, 1, 4),
    _Ty3250T1CurrentESs_Type()
)
ty3250T1CurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty3250T1CurrentESs.setStatus("mandatory")
_Ty3250T1CurrentSESs_Type = Gauge32
_Ty3250T1CurrentSESs_Object = MibTableColumn
ty3250T1CurrentSESs = _Ty3250T1CurrentSESs_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 14, 1, 5),
    _Ty3250T1CurrentSESs_Type()
)
ty3250T1CurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty3250T1CurrentSESs.setStatus("mandatory")
_Ty3250T1CurrentSEFSs_Type = Gauge32
_Ty3250T1CurrentSEFSs_Object = MibTableColumn
ty3250T1CurrentSEFSs = _Ty3250T1CurrentSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 14, 1, 6),
    _Ty3250T1CurrentSEFSs_Type()
)
ty3250T1CurrentSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty3250T1CurrentSEFSs.setStatus("mandatory")
_Ty3250T1CurrentUASs_Type = Gauge32
_Ty3250T1CurrentUASs_Object = MibTableColumn
ty3250T1CurrentUASs = _Ty3250T1CurrentUASs_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 14, 1, 7),
    _Ty3250T1CurrentUASs_Type()
)
ty3250T1CurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty3250T1CurrentUASs.setStatus("mandatory")
_Ty3250T1CurrentCSSs_Type = Gauge32
_Ty3250T1CurrentCSSs_Object = MibTableColumn
ty3250T1CurrentCSSs = _Ty3250T1CurrentCSSs_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 14, 1, 8),
    _Ty3250T1CurrentCSSs_Type()
)
ty3250T1CurrentCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty3250T1CurrentCSSs.setStatus("mandatory")
_Ty3250T1CurrentBESs_Type = Gauge32
_Ty3250T1CurrentBESs_Object = MibTableColumn
ty3250T1CurrentBESs = _Ty3250T1CurrentBESs_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 14, 1, 9),
    _Ty3250T1CurrentBESs_Type()
)
ty3250T1CurrentBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty3250T1CurrentBESs.setStatus("mandatory")
_Ty3250T1CurrentLCVs_Type = Gauge32
_Ty3250T1CurrentLCVs_Object = MibTableColumn
ty3250T1CurrentLCVs = _Ty3250T1CurrentLCVs_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 14, 1, 10),
    _Ty3250T1CurrentLCVs_Type()
)
ty3250T1CurrentLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty3250T1CurrentLCVs.setStatus("mandatory")
_Ty3250PerfT1IntervalTable_Object = MibTable
ty3250PerfT1IntervalTable = _Ty3250PerfT1IntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 15)
)
if mibBuilder.loadTexts:
    ty3250PerfT1IntervalTable.setStatus("mandatory")
_Ty3250T1IntervalEntry_Object = MibTableRow
ty3250T1IntervalEntry = _Ty3250T1IntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 15, 1)
)
ty3250T1IntervalEntry.setIndexNames(
    (0, "TY3250I-MIB", "ty3250T1IntervalIndex"),
    (0, "TY3250I-MIB", "ty3250T1IntervalNumber"),
)
if mibBuilder.loadTexts:
    ty3250T1IntervalEntry.setStatus("mandatory")


class _Ty3250T1IntervalIndex_Type(Integer32):
    """Custom type ty3250T1IntervalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Ty3250T1IntervalIndex_Type.__name__ = "Integer32"
_Ty3250T1IntervalIndex_Object = MibTableColumn
ty3250T1IntervalIndex = _Ty3250T1IntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 15, 1, 1),
    _Ty3250T1IntervalIndex_Type()
)
ty3250T1IntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty3250T1IntervalIndex.setStatus("mandatory")


class _Ty3250T1IntervalNumber_Type(Integer32):
    """Custom type ty3250T1IntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_Ty3250T1IntervalNumber_Type.__name__ = "Integer32"
_Ty3250T1IntervalNumber_Object = MibTableColumn
ty3250T1IntervalNumber = _Ty3250T1IntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 15, 1, 2),
    _Ty3250T1IntervalNumber_Type()
)
ty3250T1IntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty3250T1IntervalNumber.setStatus("mandatory")
_Ty3250T1IntervalESs_Type = Gauge32
_Ty3250T1IntervalESs_Object = MibTableColumn
ty3250T1IntervalESs = _Ty3250T1IntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 15, 1, 3),
    _Ty3250T1IntervalESs_Type()
)
ty3250T1IntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty3250T1IntervalESs.setStatus("mandatory")
_Ty3250T1IntervalSESs_Type = Gauge32
_Ty3250T1IntervalSESs_Object = MibTableColumn
ty3250T1IntervalSESs = _Ty3250T1IntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 15, 1, 4),
    _Ty3250T1IntervalSESs_Type()
)
ty3250T1IntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty3250T1IntervalSESs.setStatus("mandatory")
_Ty3250T1IntervalSEFSs_Type = Gauge32
_Ty3250T1IntervalSEFSs_Object = MibTableColumn
ty3250T1IntervalSEFSs = _Ty3250T1IntervalSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 15, 1, 5),
    _Ty3250T1IntervalSEFSs_Type()
)
ty3250T1IntervalSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty3250T1IntervalSEFSs.setStatus("mandatory")
_Ty3250T1IntervalUASs_Type = Gauge32
_Ty3250T1IntervalUASs_Object = MibTableColumn
ty3250T1IntervalUASs = _Ty3250T1IntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 15, 1, 6),
    _Ty3250T1IntervalUASs_Type()
)
ty3250T1IntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty3250T1IntervalUASs.setStatus("mandatory")
_Ty3250T1IntervalCSSs_Type = Gauge32
_Ty3250T1IntervalCSSs_Object = MibTableColumn
ty3250T1IntervalCSSs = _Ty3250T1IntervalCSSs_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 15, 1, 7),
    _Ty3250T1IntervalCSSs_Type()
)
ty3250T1IntervalCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty3250T1IntervalCSSs.setStatus("mandatory")
_Ty3250T1IntervalBESs_Type = Gauge32
_Ty3250T1IntervalBESs_Object = MibTableColumn
ty3250T1IntervalBESs = _Ty3250T1IntervalBESs_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 15, 1, 8),
    _Ty3250T1IntervalBESs_Type()
)
ty3250T1IntervalBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty3250T1IntervalBESs.setStatus("mandatory")
_Ty3250T1IntervalLCVs_Type = Gauge32
_Ty3250T1IntervalLCVs_Object = MibTableColumn
ty3250T1IntervalLCVs = _Ty3250T1IntervalLCVs_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 15, 1, 9),
    _Ty3250T1IntervalLCVs_Type()
)
ty3250T1IntervalLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty3250T1IntervalLCVs.setStatus("mandatory")
_Ty3250PerfT1TotalTable_Object = MibTable
ty3250PerfT1TotalTable = _Ty3250PerfT1TotalTable_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 16)
)
if mibBuilder.loadTexts:
    ty3250PerfT1TotalTable.setStatus("mandatory")
_Ty3250T1TotalEntry_Object = MibTableRow
ty3250T1TotalEntry = _Ty3250T1TotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 16, 1)
)
ty3250T1TotalEntry.setIndexNames(
    (0, "TY3250I-MIB", "ty3250T1TotalIndex"),
)
if mibBuilder.loadTexts:
    ty3250T1TotalEntry.setStatus("mandatory")


class _Ty3250T1TotalIndex_Type(Integer32):
    """Custom type ty3250T1TotalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Ty3250T1TotalIndex_Type.__name__ = "Integer32"
_Ty3250T1TotalIndex_Object = MibTableColumn
ty3250T1TotalIndex = _Ty3250T1TotalIndex_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 16, 1, 1),
    _Ty3250T1TotalIndex_Type()
)
ty3250T1TotalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty3250T1TotalIndex.setStatus("mandatory")
_Ty3250T1TotalESs_Type = Gauge32
_Ty3250T1TotalESs_Object = MibTableColumn
ty3250T1TotalESs = _Ty3250T1TotalESs_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 16, 1, 2),
    _Ty3250T1TotalESs_Type()
)
ty3250T1TotalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty3250T1TotalESs.setStatus("mandatory")
_Ty3250T1TotalSESs_Type = Gauge32
_Ty3250T1TotalSESs_Object = MibTableColumn
ty3250T1TotalSESs = _Ty3250T1TotalSESs_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 16, 1, 3),
    _Ty3250T1TotalSESs_Type()
)
ty3250T1TotalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty3250T1TotalSESs.setStatus("mandatory")
_Ty3250T1TotalSEFSs_Type = Gauge32
_Ty3250T1TotalSEFSs_Object = MibTableColumn
ty3250T1TotalSEFSs = _Ty3250T1TotalSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 16, 1, 4),
    _Ty3250T1TotalSEFSs_Type()
)
ty3250T1TotalSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty3250T1TotalSEFSs.setStatus("mandatory")
_Ty3250T1TotalUASs_Type = Gauge32
_Ty3250T1TotalUASs_Object = MibTableColumn
ty3250T1TotalUASs = _Ty3250T1TotalUASs_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 16, 1, 5),
    _Ty3250T1TotalUASs_Type()
)
ty3250T1TotalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty3250T1TotalUASs.setStatus("mandatory")
_Ty3250T1TotalCSSs_Type = Gauge32
_Ty3250T1TotalCSSs_Object = MibTableColumn
ty3250T1TotalCSSs = _Ty3250T1TotalCSSs_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 16, 1, 6),
    _Ty3250T1TotalCSSs_Type()
)
ty3250T1TotalCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty3250T1TotalCSSs.setStatus("mandatory")
_Ty3250T1TotalBESs_Type = Gauge32
_Ty3250T1TotalBESs_Object = MibTableColumn
ty3250T1TotalBESs = _Ty3250T1TotalBESs_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 16, 1, 7),
    _Ty3250T1TotalBESs_Type()
)
ty3250T1TotalBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty3250T1TotalBESs.setStatus("mandatory")
_Ty3250T1TotalLCVs_Type = Gauge32
_Ty3250T1TotalLCVs_Object = MibTableColumn
ty3250T1TotalLCVs = _Ty3250T1TotalLCVs_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 16, 1, 8),
    _Ty3250T1TotalLCVs_Type()
)
ty3250T1TotalLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty3250T1TotalLCVs.setStatus("mandatory")
_Ty3250T1PerfCmdTypeTable_Object = MibTable
ty3250T1PerfCmdTypeTable = _Ty3250T1PerfCmdTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 17)
)
if mibBuilder.loadTexts:
    ty3250T1PerfCmdTypeTable.setStatus("mandatory")
_Ty3250T1PerfCmdType_Object = MibTableRow
ty3250T1PerfCmdType = _Ty3250T1PerfCmdType_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 17, 1)
)
ty3250T1PerfCmdType.setIndexNames(
    (0, "TY3250I-MIB", "ty3250T1CommandIndex"),
)
if mibBuilder.loadTexts:
    ty3250T1PerfCmdType.setStatus("mandatory")


class _Ty3250T1CommandIndex_Type(Integer32):
    """Custom type ty3250T1CommandIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Ty3250T1CommandIndex_Type.__name__ = "Integer32"
_Ty3250T1CommandIndex_Object = MibTableColumn
ty3250T1CommandIndex = _Ty3250T1CommandIndex_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 17, 1, 1),
    _Ty3250T1CommandIndex_Type()
)
ty3250T1CommandIndex.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    ty3250T1CommandIndex.setStatus("mandatory")


class _Ty3250T1PerfFreezeState_Type(Integer32):
    """Custom type ty3250T1PerfFreezeState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("freeze-reg", 1),
          ("unfreeze-reg", 2))
    )


_Ty3250T1PerfFreezeState_Type.__name__ = "Integer32"
_Ty3250T1PerfFreezeState_Object = MibTableColumn
ty3250T1PerfFreezeState = _Ty3250T1PerfFreezeState_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 17, 1, 2),
    _Ty3250T1PerfFreezeState_Type()
)
ty3250T1PerfFreezeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ty3250T1PerfFreezeState.setStatus("mandatory")


class _Ty3250T1PerfClearEvents_Type(Integer32):
    """Custom type ty3250T1PerfClearEvents based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear-events", 1)
    )


_Ty3250T1PerfClearEvents_Type.__name__ = "Integer32"
_Ty3250T1PerfClearEvents_Object = MibTableColumn
ty3250T1PerfClearEvents = _Ty3250T1PerfClearEvents_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 17, 1, 3),
    _Ty3250T1PerfClearEvents_Type()
)
ty3250T1PerfClearEvents.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    ty3250T1PerfClearEvents.setStatus("mandatory")


class _Ty3250T1PerfClearAll_Type(Integer32):
    """Custom type ty3250T1PerfClearAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear-all", 1)
    )


_Ty3250T1PerfClearAll_Type.__name__ = "Integer32"
_Ty3250T1PerfClearAll_Object = MibTableColumn
ty3250T1PerfClearAll = _Ty3250T1PerfClearAll_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 17, 1, 4),
    _Ty3250T1PerfClearAll_Type()
)
ty3250T1PerfClearAll.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    ty3250T1PerfClearAll.setStatus("mandatory")


class _Ty3250AlarmType_Type(Integer32):
    """Custom type ty3250AlarmType based on Integer32"""
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
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("authentication", 2),
          ("cold-start", 1),
          ("configuration-update", 14),
          ("diagnostic-clear", 16),
          ("diagnostic-state", 15),
          ("t1-controlled-slip", 13),
          ("t1-netw-ais-clear", 12),
          ("t1-netw-ais-detect", 11),
          ("t1-netw-carrier-detect", 4),
          ("t1-netw-carrier-loss", 3),
          ("t1-netw-red-alarm-clear", 8),
          ("t1-netw-red-alarm-declare", 7),
          ("t1-netw-sync-acquire", 6),
          ("t1-netw-sync-loss-declare", 5),
          ("t1-netw-yellow-alarm-clear", 10),
          ("t1-netw-yellow-alarm-detect", 9))
    )


_Ty3250AlarmType_Type.__name__ = "Integer32"
_Ty3250AlarmType_Object = MibScalar
ty3250AlarmType = _Ty3250AlarmType_Object(
    (1, 3, 6, 1, 4, 1, 466, 4, 18),
    _Ty3250AlarmType_Type()
)
ty3250AlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty3250AlarmType.setStatus("mandatory")

# Managed Objects groups


# Notification objects

ty3250Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 466, 4, 0, 0)
)
ty3250Trap.setObjects(
    ("TY3250I-MIB", "ty3250AlarmType")
)
if mibBuilder.loadTexts:
    ty3250Trap.setStatus(
        ""
    )

ty3250coldstart = NotificationType(
    (1, 3, 6, 1, 4, 1, 466, 4, 0, 1)
)
ty3250coldstart.setObjects(
    ("TY3250I-MIB", "ty3250AlarmType")
)
if mibBuilder.loadTexts:
    ty3250coldstart.setStatus(
        ""
    )

ty3250authentication = NotificationType(
    (1, 3, 6, 1, 4, 1, 466, 4, 0, 2)
)
ty3250authentication.setObjects(
    ("TY3250I-MIB", "ty3250AlarmType")
)
if mibBuilder.loadTexts:
    ty3250authentication.setStatus(
        ""
    )

ty3250t1netwcarrierloss = NotificationType(
    (1, 3, 6, 1, 4, 1, 466, 4, 0, 3)
)
ty3250t1netwcarrierloss.setObjects(
    ("TY3250I-MIB", "ty3250AlarmType")
)
if mibBuilder.loadTexts:
    ty3250t1netwcarrierloss.setStatus(
        ""
    )

ty3250t1netwcarrierdetect = NotificationType(
    (1, 3, 6, 1, 4, 1, 466, 4, 0, 4)
)
ty3250t1netwcarrierdetect.setObjects(
    ("TY3250I-MIB", "ty3250AlarmType")
)
if mibBuilder.loadTexts:
    ty3250t1netwcarrierdetect.setStatus(
        ""
    )

ty3250t1netwsynclossdeclare = NotificationType(
    (1, 3, 6, 1, 4, 1, 466, 4, 0, 5)
)
ty3250t1netwsynclossdeclare.setObjects(
    ("TY3250I-MIB", "ty3250AlarmType")
)
if mibBuilder.loadTexts:
    ty3250t1netwsynclossdeclare.setStatus(
        ""
    )

ty3250t1netwsyncacquire = NotificationType(
    (1, 3, 6, 1, 4, 1, 466, 4, 0, 6)
)
ty3250t1netwsyncacquire.setObjects(
    ("TY3250I-MIB", "ty3250AlarmType")
)
if mibBuilder.loadTexts:
    ty3250t1netwsyncacquire.setStatus(
        ""
    )

ty3250t1netwredalarmdeclare = NotificationType(
    (1, 3, 6, 1, 4, 1, 466, 4, 0, 7)
)
ty3250t1netwredalarmdeclare.setObjects(
    ("TY3250I-MIB", "ty3250AlarmType")
)
if mibBuilder.loadTexts:
    ty3250t1netwredalarmdeclare.setStatus(
        ""
    )

ty3250t1netwredalarmclear = NotificationType(
    (1, 3, 6, 1, 4, 1, 466, 4, 0, 8)
)
ty3250t1netwredalarmclear.setObjects(
    ("TY3250I-MIB", "ty3250AlarmType")
)
if mibBuilder.loadTexts:
    ty3250t1netwredalarmclear.setStatus(
        ""
    )

ty3250t1netwyellowalarmdetect = NotificationType(
    (1, 3, 6, 1, 4, 1, 466, 4, 0, 9)
)
ty3250t1netwyellowalarmdetect.setObjects(
    ("TY3250I-MIB", "ty3250AlarmType")
)
if mibBuilder.loadTexts:
    ty3250t1netwyellowalarmdetect.setStatus(
        ""
    )

ty3250t1netwyellowalarmclear = NotificationType(
    (1, 3, 6, 1, 4, 1, 466, 4, 0, 10)
)
ty3250t1netwyellowalarmclear.setObjects(
    ("TY3250I-MIB", "ty3250AlarmType")
)
if mibBuilder.loadTexts:
    ty3250t1netwyellowalarmclear.setStatus(
        ""
    )

ty3250t1netwaisdetect = NotificationType(
    (1, 3, 6, 1, 4, 1, 466, 4, 0, 11)
)
ty3250t1netwaisdetect.setObjects(
    ("TY3250I-MIB", "ty3250AlarmType")
)
if mibBuilder.loadTexts:
    ty3250t1netwaisdetect.setStatus(
        ""
    )

ty3250t1netwaisclear = NotificationType(
    (1, 3, 6, 1, 4, 1, 466, 4, 0, 12)
)
ty3250t1netwaisclear.setObjects(
    ("TY3250I-MIB", "ty3250AlarmType")
)
if mibBuilder.loadTexts:
    ty3250t1netwaisclear.setStatus(
        ""
    )

ty3250t1controlledslip = NotificationType(
    (1, 3, 6, 1, 4, 1, 466, 4, 0, 13)
)
ty3250t1controlledslip.setObjects(
    ("TY3250I-MIB", "ty3250AlarmType")
)
if mibBuilder.loadTexts:
    ty3250t1controlledslip.setStatus(
        ""
    )

ty3250configurationupdate = NotificationType(
    (1, 3, 6, 1, 4, 1, 466, 4, 0, 14)
)
ty3250configurationupdate.setObjects(
    ("TY3250I-MIB", "ty3250AlarmType")
)
if mibBuilder.loadTexts:
    ty3250configurationupdate.setStatus(
        ""
    )

ty3250diagnosticstate = NotificationType(
    (1, 3, 6, 1, 4, 1, 466, 4, 0, 15)
)
ty3250diagnosticstate.setObjects(
    ("TY3250I-MIB", "ty3250AlarmType")
)
if mibBuilder.loadTexts:
    ty3250diagnosticstate.setStatus(
        ""
    )

ty3250diagnosticclear = NotificationType(
    (1, 3, 6, 1, 4, 1, 466, 4, 0, 16)
)
ty3250diagnosticclear.setObjects(
    ("TY3250I-MIB", "ty3250AlarmType")
)
if mibBuilder.loadTexts:
    ty3250diagnosticclear.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TY3250I-MIB",
    **{"tylink": tylink,
       "ty3250": ty3250,
       "ty3250Trap": ty3250Trap,
       "ty3250coldstart": ty3250coldstart,
       "ty3250authentication": ty3250authentication,
       "ty3250t1netwcarrierloss": ty3250t1netwcarrierloss,
       "ty3250t1netwcarrierdetect": ty3250t1netwcarrierdetect,
       "ty3250t1netwsynclossdeclare": ty3250t1netwsynclossdeclare,
       "ty3250t1netwsyncacquire": ty3250t1netwsyncacquire,
       "ty3250t1netwredalarmdeclare": ty3250t1netwredalarmdeclare,
       "ty3250t1netwredalarmclear": ty3250t1netwredalarmclear,
       "ty3250t1netwyellowalarmdetect": ty3250t1netwyellowalarmdetect,
       "ty3250t1netwyellowalarmclear": ty3250t1netwyellowalarmclear,
       "ty3250t1netwaisdetect": ty3250t1netwaisdetect,
       "ty3250t1netwaisclear": ty3250t1netwaisclear,
       "ty3250t1controlledslip": ty3250t1controlledslip,
       "ty3250configurationupdate": ty3250configurationupdate,
       "ty3250diagnosticstate": ty3250diagnosticstate,
       "ty3250diagnosticclear": ty3250diagnosticclear,
       "ty3250SysTable": ty3250SysTable,
       "ty3250SysType": ty3250SysType,
       "ty3250SysSoftRev": ty3250SysSoftRev,
       "ty3250SysHardRev": ty3250SysHardRev,
       "ty3250SysNumT1Installed": ty3250SysNumT1Installed,
       "ty3250SysNumDteInstalled": ty3250SysNumDteInstalled,
       "ty3250SysNumCommInstalled": ty3250SysNumCommInstalled,
       "ty3250SysName": ty3250SysName,
       "ty3250SysResetNode": ty3250SysResetNode,
       "ty3250CfgT1Table": ty3250CfgT1Table,
       "ty3250CfgT1Framing": ty3250CfgT1Framing,
       "ty3250CfgT1LineEncoding": ty3250CfgT1LineEncoding,
       "ty3250CfgT1Density": ty3250CfgT1Density,
       "ty3250CfgT1Interface": ty3250CfgT1Interface,
       "ty3250CfgT1LboSetting": ty3250CfgT1LboSetting,
       "ty3250CfgT1Timing": ty3250CfgT1Timing,
       "ty3250CfgT1CicuitID": ty3250CfgT1CicuitID,
       "ty3250CfgDteTable": ty3250CfgDteTable,
       "ty3250CfgDteLineRate": ty3250CfgDteLineRate,
       "ty3250CfgDteChannelDensity": ty3250CfgDteChannelDensity,
       "ty3250CfgDteTiming": ty3250CfgDteTiming,
       "ty3250CfgDteClockMode": ty3250CfgDteClockMode,
       "ty3250CfgDteDataMode": ty3250CfgDteDataMode,
       "ty3250CfgDteIntfType": ty3250CfgDteIntfType,
       "ty3250CfgConnectTable": ty3250CfgConnectTable,
       "ty3250CfgConnAutoAssign": ty3250CfgConnAutoAssign,
       "ty3250ConnAutoT1Index": ty3250ConnAutoT1Index,
       "ty3250ConnStartDS0": ty3250ConnStartDS0,
       "ty3250ConnAutoPort": ty3250ConnAutoPort,
       "ty3250ConnAutoType": ty3250ConnAutoType,
       "ty3250ConnDteRate": ty3250ConnDteRate,
       "ty3250ConnDteDensity": ty3250ConnDteDensity,
       "ty3250ConnDs0Required": ty3250ConnDs0Required,
       "ty3250ConnAutoStatus": ty3250ConnAutoStatus,
       "ty3250CfgCurrentConnTable": ty3250CfgCurrentConnTable,
       "ty3250CfgCurrentConnections": ty3250CfgCurrentConnections,
       "ty3250T1Index": ty3250T1Index,
       "ty3250Ds0": ty3250Ds0,
       "ty3250DtePort": ty3250DtePort,
       "ty3250Type": ty3250Type,
       "ty3250CfgEditConnMenu": ty3250CfgEditConnMenu,
       "ty3250CfgEditConnCopyCurrtoEdit": ty3250CfgEditConnCopyCurrtoEdit,
       "ty3250CfgEditConnTable": ty3250CfgEditConnTable,
       "ty3250CfgEditConnEntry": ty3250CfgEditConnEntry,
       "ty3250ConnT1Index": ty3250ConnT1Index,
       "ty3250ConnDS0": ty3250ConnDS0,
       "ty3250ConnDTE": ty3250ConnDTE,
       "ty3250ConnType": ty3250ConnType,
       "ty3250CfgConnUpdate": ty3250CfgConnUpdate,
       "ty3250CfgConnUpdateCmd": ty3250CfgConnUpdateCmd,
       "ty3250CfgConnStatus": ty3250CfgConnStatus,
       "ty3250CfgEditConnClearEditBuff": ty3250CfgEditConnClearEditBuff,
       "ty3250CfgCommTable": ty3250CfgCommTable,
       "ty3250CfgCommFormat": ty3250CfgCommFormat,
       "ty3250CfgCommIntf": ty3250CfgCommIntf,
       "ty3250CfgCommIndex": ty3250CfgCommIndex,
       "ty3250CfgCommBaud": ty3250CfgCommBaud,
       "ty3250CfgCommDataBits": ty3250CfgCommDataBits,
       "ty3250CfgCommStopBits": ty3250CfgCommStopBits,
       "ty3250CfgCommParity": ty3250CfgCommParity,
       "ty3250CfgCommFlowCtrl": ty3250CfgCommFlowCtrl,
       "ty3250CfgCommModeTable": ty3250CfgCommModeTable,
       "ty3250CfgCommModeEntry": ty3250CfgCommModeEntry,
       "ty3250CfgCommModeIndex": ty3250CfgCommModeIndex,
       "ty3250CfgCommMode": ty3250CfgCommMode,
       "ty3250CfgCommMyIP": ty3250CfgCommMyIP,
       "ty3250CfgCommPeerIP": ty3250CfgCommPeerIP,
       "ty3250CfgCommMask": ty3250CfgCommMask,
       "ty3250CfgCommMaxMTU": ty3250CfgCommMaxMTU,
       "ty3250CfgSnmpTable": ty3250CfgSnmpTable,
       "ty3250SnmpEntry": ty3250SnmpEntry,
       "ty3250SnmpIndex": ty3250SnmpIndex,
       "ty3250SnmpManagerIP": ty3250SnmpManagerIP,
       "ty3250DiagT1Table": ty3250DiagT1Table,
       "ty3250DiagT1LocLineLpbk": ty3250DiagT1LocLineLpbk,
       "ty3250DiagT1LocPylLpbk": ty3250DiagT1LocPylLpbk,
       "ty3250DiagT1LocAggrLpbk": ty3250DiagT1LocAggrLpbk,
       "ty3250DiagT1RmtLpbkStatus": ty3250DiagT1RmtLpbkStatus,
       "ty3250DiagT1RmtLpbkCmd": ty3250DiagT1RmtLpbkCmd,
       "ty3250DiagDteTable": ty3250DiagDteTable,
       "ty3250DiagDteLocBidirLpbk": ty3250DiagDteLocBidirLpbk,
       "ty3250DiagDteRmtLpbkStatus": ty3250DiagDteRmtLpbkStatus,
       "ty3250DiagDteRmtLpbkCmd": ty3250DiagDteRmtLpbkCmd,
       "ty3250DiagBerTable": ty3250DiagBerTable,
       "ty3250DiagBerPattrn": ty3250DiagBerPattrn,
       "ty3250DiagBerState": ty3250DiagBerState,
       "ty3250DiagBerStatus": ty3250DiagBerStatus,
       "ty3250DiagBerErrors": ty3250DiagBerErrors,
       "ty3250DiagBerTimeElaps": ty3250DiagBerTimeElaps,
       "ty3250PortStatusTable": ty3250PortStatusTable,
       "ty3250PortStatus": ty3250PortStatus,
       "ty3250IntfIndex": ty3250IntfIndex,
       "ty3250IntfType": ty3250IntfType,
       "ty3250IntfMode": ty3250IntfMode,
       "ty3250IntfStatus": ty3250IntfStatus,
       "ty3250IntfAlarms": ty3250IntfAlarms,
       "ty3250PerfT1CurrentTable": ty3250PerfT1CurrentTable,
       "ty3250T1CurrentEntry": ty3250T1CurrentEntry,
       "ty3250T1CurrentIndex": ty3250T1CurrentIndex,
       "ty3250T1CurrentCrc6Events": ty3250T1CurrentCrc6Events,
       "ty3250T1CurrentOofEvents": ty3250T1CurrentOofEvents,
       "ty3250T1CurrentESs": ty3250T1CurrentESs,
       "ty3250T1CurrentSESs": ty3250T1CurrentSESs,
       "ty3250T1CurrentSEFSs": ty3250T1CurrentSEFSs,
       "ty3250T1CurrentUASs": ty3250T1CurrentUASs,
       "ty3250T1CurrentCSSs": ty3250T1CurrentCSSs,
       "ty3250T1CurrentBESs": ty3250T1CurrentBESs,
       "ty3250T1CurrentLCVs": ty3250T1CurrentLCVs,
       "ty3250PerfT1IntervalTable": ty3250PerfT1IntervalTable,
       "ty3250T1IntervalEntry": ty3250T1IntervalEntry,
       "ty3250T1IntervalIndex": ty3250T1IntervalIndex,
       "ty3250T1IntervalNumber": ty3250T1IntervalNumber,
       "ty3250T1IntervalESs": ty3250T1IntervalESs,
       "ty3250T1IntervalSESs": ty3250T1IntervalSESs,
       "ty3250T1IntervalSEFSs": ty3250T1IntervalSEFSs,
       "ty3250T1IntervalUASs": ty3250T1IntervalUASs,
       "ty3250T1IntervalCSSs": ty3250T1IntervalCSSs,
       "ty3250T1IntervalBESs": ty3250T1IntervalBESs,
       "ty3250T1IntervalLCVs": ty3250T1IntervalLCVs,
       "ty3250PerfT1TotalTable": ty3250PerfT1TotalTable,
       "ty3250T1TotalEntry": ty3250T1TotalEntry,
       "ty3250T1TotalIndex": ty3250T1TotalIndex,
       "ty3250T1TotalESs": ty3250T1TotalESs,
       "ty3250T1TotalSESs": ty3250T1TotalSESs,
       "ty3250T1TotalSEFSs": ty3250T1TotalSEFSs,
       "ty3250T1TotalUASs": ty3250T1TotalUASs,
       "ty3250T1TotalCSSs": ty3250T1TotalCSSs,
       "ty3250T1TotalBESs": ty3250T1TotalBESs,
       "ty3250T1TotalLCVs": ty3250T1TotalLCVs,
       "ty3250T1PerfCmdTypeTable": ty3250T1PerfCmdTypeTable,
       "ty3250T1PerfCmdType": ty3250T1PerfCmdType,
       "ty3250T1CommandIndex": ty3250T1CommandIndex,
       "ty3250T1PerfFreezeState": ty3250T1PerfFreezeState,
       "ty3250T1PerfClearEvents": ty3250T1PerfClearEvents,
       "ty3250T1PerfClearAll": ty3250T1PerfClearAll,
       "ty3250AlarmType": ty3250AlarmType}
)
