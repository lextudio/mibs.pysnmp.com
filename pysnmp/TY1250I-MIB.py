# SNMP MIB module (TY1250I-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TY1250I-MIB
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
_Dsucsu_ObjectIdentity = ObjectIdentity
dsucsu = _Dsucsu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 466, 1)
)
_Tyview_ObjectIdentity = ObjectIdentity
tyview = _Tyview_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 466, 2)
)
_Ty1250_ObjectIdentity = ObjectIdentity
ty1250 = _Ty1250_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 466, 3)
)
_Ty1250SysTable_ObjectIdentity = ObjectIdentity
ty1250SysTable = _Ty1250SysTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 466, 3, 1)
)


class _Ty1250SysType_Type(DisplayString):
    """Custom type ty1250SysType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_Ty1250SysType_Type.__name__ = "DisplayString"
_Ty1250SysType_Object = MibScalar
ty1250SysType = _Ty1250SysType_Object(
    (1, 3, 6, 1, 4, 1, 466, 3, 1, 1),
    _Ty1250SysType_Type()
)
ty1250SysType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty1250SysType.setStatus("mandatory")


class _Ty1250SysSoftRev_Type(DisplayString):
    """Custom type ty1250SysSoftRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_Ty1250SysSoftRev_Type.__name__ = "DisplayString"
_Ty1250SysSoftRev_Object = MibScalar
ty1250SysSoftRev = _Ty1250SysSoftRev_Object(
    (1, 3, 6, 1, 4, 1, 466, 3, 1, 2),
    _Ty1250SysSoftRev_Type()
)
ty1250SysSoftRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty1250SysSoftRev.setStatus("mandatory")


class _Ty1250SysHardRev_Type(DisplayString):
    """Custom type ty1250SysHardRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_Ty1250SysHardRev_Type.__name__ = "DisplayString"
_Ty1250SysHardRev_Object = MibScalar
ty1250SysHardRev = _Ty1250SysHardRev_Object(
    (1, 3, 6, 1, 4, 1, 466, 3, 1, 3),
    _Ty1250SysHardRev_Type()
)
ty1250SysHardRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty1250SysHardRev.setStatus("mandatory")


class _Ty1250SysNumNetInstalled_Type(Integer32):
    """Custom type ty1250SysNumNetInstalled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Ty1250SysNumNetInstalled_Type.__name__ = "Integer32"
_Ty1250SysNumNetInstalled_Object = MibScalar
ty1250SysNumNetInstalled = _Ty1250SysNumNetInstalled_Object(
    (1, 3, 6, 1, 4, 1, 466, 3, 1, 4),
    _Ty1250SysNumNetInstalled_Type()
)
ty1250SysNumNetInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty1250SysNumNetInstalled.setStatus("mandatory")


class _Ty1250SysNumDteInstalled_Type(Integer32):
    """Custom type ty1250SysNumDteInstalled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Ty1250SysNumDteInstalled_Type.__name__ = "Integer32"
_Ty1250SysNumDteInstalled_Object = MibScalar
ty1250SysNumDteInstalled = _Ty1250SysNumDteInstalled_Object(
    (1, 3, 6, 1, 4, 1, 466, 3, 1, 5),
    _Ty1250SysNumDteInstalled_Type()
)
ty1250SysNumDteInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty1250SysNumDteInstalled.setStatus("mandatory")


class _Ty1250SysNumMaintInstalled_Type(Integer32):
    """Custom type ty1250SysNumMaintInstalled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Ty1250SysNumMaintInstalled_Type.__name__ = "Integer32"
_Ty1250SysNumMaintInstalled_Object = MibScalar
ty1250SysNumMaintInstalled = _Ty1250SysNumMaintInstalled_Object(
    (1, 3, 6, 1, 4, 1, 466, 3, 1, 6),
    _Ty1250SysNumMaintInstalled_Type()
)
ty1250SysNumMaintInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty1250SysNumMaintInstalled.setStatus("mandatory")


class _Ty1250SysName_Type(DisplayString):
    """Custom type ty1250SysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Ty1250SysName_Type.__name__ = "DisplayString"
_Ty1250SysName_Object = MibScalar
ty1250SysName = _Ty1250SysName_Object(
    (1, 3, 6, 1, 4, 1, 466, 3, 1, 7),
    _Ty1250SysName_Type()
)
ty1250SysName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ty1250SysName.setStatus("mandatory")
_Ty1250CfgAppTable_ObjectIdentity = ObjectIdentity
ty1250CfgAppTable = _Ty1250CfgAppTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 466, 3, 2)
)


class _Ty1250CfgAppClockSource_Type(Integer32):
    """Custom type ty1250CfgAppClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("internal", 1),
          ("network", 2))
    )


_Ty1250CfgAppClockSource_Type.__name__ = "Integer32"
_Ty1250CfgAppClockSource_Object = MibScalar
ty1250CfgAppClockSource = _Ty1250CfgAppClockSource_Object(
    (1, 3, 6, 1, 4, 1, 466, 3, 2, 2),
    _Ty1250CfgAppClockSource_Type()
)
ty1250CfgAppClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ty1250CfgAppClockSource.setStatus("mandatory")


class _Ty1250CfgAppCircuitId_Type(DisplayString):
    """Custom type ty1250CfgAppCircuitId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_Ty1250CfgAppCircuitId_Type.__name__ = "DisplayString"
_Ty1250CfgAppCircuitId_Object = MibScalar
ty1250CfgAppCircuitId = _Ty1250CfgAppCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 466, 3, 2, 3),
    _Ty1250CfgAppCircuitId_Type()
)
ty1250CfgAppCircuitId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ty1250CfgAppCircuitId.setStatus("mandatory")
_Ty1250CfgNetTable_ObjectIdentity = ObjectIdentity
ty1250CfgNetTable = _Ty1250CfgNetTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 466, 3, 3)
)


class _Ty1250CfgNetGlareType_Type(Integer32):
    """Custom type ty1250CfgNetGlareType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external-glare", 1),
          ("internal-glare", 2))
    )


_Ty1250CfgNetGlareType_Type.__name__ = "Integer32"
_Ty1250CfgNetGlareType_Object = MibScalar
ty1250CfgNetGlareType = _Ty1250CfgNetGlareType_Object(
    (1, 3, 6, 1, 4, 1, 466, 3, 3, 4),
    _Ty1250CfgNetGlareType_Type()
)
ty1250CfgNetGlareType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ty1250CfgNetGlareType.setStatus("mandatory")


class _Ty1250CfgNetEchoCan_Type(Integer32):
    """Custom type ty1250CfgNetEchoCan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable-echo-cancellers", 2),
          ("ignore-echo-cancellers", 1))
    )


_Ty1250CfgNetEchoCan_Type.__name__ = "Integer32"
_Ty1250CfgNetEchoCan_Object = MibScalar
ty1250CfgNetEchoCan = _Ty1250CfgNetEchoCan_Object(
    (1, 3, 6, 1, 4, 1, 466, 3, 3, 5),
    _Ty1250CfgNetEchoCan_Type()
)
ty1250CfgNetEchoCan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ty1250CfgNetEchoCan.setStatus("mandatory")


class _Ty1250CfgNetAnsMode_Type(Integer32):
    """Custom type ty1250CfgNetAnsMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic-answer", 2),
          ("manual-answer", 1))
    )


_Ty1250CfgNetAnsMode_Type.__name__ = "Integer32"
_Ty1250CfgNetAnsMode_Object = MibScalar
ty1250CfgNetAnsMode = _Ty1250CfgNetAnsMode_Object(
    (1, 3, 6, 1, 4, 1, 466, 3, 3, 6),
    _Ty1250CfgNetAnsMode_Type()
)
ty1250CfgNetAnsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ty1250CfgNetAnsMode.setStatus("mandatory")


class _Ty1250CfgNetDialTimeout_Type(Integer32):
    """Custom type ty1250CfgNetDialTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Ty1250CfgNetDialTimeout_Type.__name__ = "Integer32"
_Ty1250CfgNetDialTimeout_Object = MibScalar
ty1250CfgNetDialTimeout = _Ty1250CfgNetDialTimeout_Object(
    (1, 3, 6, 1, 4, 1, 466, 3, 3, 7),
    _Ty1250CfgNetDialTimeout_Type()
)
ty1250CfgNetDialTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ty1250CfgNetDialTimeout.setStatus("mandatory")


class _Ty1250CfgNetNumRedial_Type(Integer32):
    """Custom type ty1250CfgNetNumRedial based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Ty1250CfgNetNumRedial_Type.__name__ = "Integer32"
_Ty1250CfgNetNumRedial_Object = MibScalar
ty1250CfgNetNumRedial = _Ty1250CfgNetNumRedial_Object(
    (1, 3, 6, 1, 4, 1, 466, 3, 3, 8),
    _Ty1250CfgNetNumRedial_Type()
)
ty1250CfgNetNumRedial.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ty1250CfgNetNumRedial.setStatus("mandatory")


class _Ty1250CfgNetRedialDelay_Type(Integer32):
    """Custom type ty1250CfgNetRedialDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Ty1250CfgNetRedialDelay_Type.__name__ = "Integer32"
_Ty1250CfgNetRedialDelay_Object = MibScalar
ty1250CfgNetRedialDelay = _Ty1250CfgNetRedialDelay_Object(
    (1, 3, 6, 1, 4, 1, 466, 3, 3, 9),
    _Ty1250CfgNetRedialDelay_Type()
)
ty1250CfgNetRedialDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ty1250CfgNetRedialDelay.setStatus("mandatory")


class _Ty1250CfgNetDefNum2Dial_Type(DisplayString):
    """Custom type ty1250CfgNetDefNum2Dial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Ty1250CfgNetDefNum2Dial_Type.__name__ = "DisplayString"
_Ty1250CfgNetDefNum2Dial_Object = MibScalar
ty1250CfgNetDefNum2Dial = _Ty1250CfgNetDefNum2Dial_Object(
    (1, 3, 6, 1, 4, 1, 466, 3, 3, 10),
    _Ty1250CfgNetDefNum2Dial_Type()
)
ty1250CfgNetDefNum2Dial.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ty1250CfgNetDefNum2Dial.setStatus("mandatory")


class _Ty1250CfgNetType_Type(Integer32):
    """Custom type ty1250CfgNetType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dedicated", 1),
          ("switch56", 2))
    )


_Ty1250CfgNetType_Type.__name__ = "Integer32"
_Ty1250CfgNetType_Object = MibScalar
ty1250CfgNetType = _Ty1250CfgNetType_Object(
    (1, 3, 6, 1, 4, 1, 466, 3, 3, 11),
    _Ty1250CfgNetType_Type()
)
ty1250CfgNetType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ty1250CfgNetType.setStatus("mandatory")


class _Ty1250CfgNetBPVThresholding_Type(Integer32):
    """Custom type ty1250CfgNetBPVThresholding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable-thresholding", 2),
          ("thresholding-at-10E-4", 1))
    )


_Ty1250CfgNetBPVThresholding_Type.__name__ = "Integer32"
_Ty1250CfgNetBPVThresholding_Object = MibScalar
ty1250CfgNetBPVThresholding = _Ty1250CfgNetBPVThresholding_Object(
    (1, 3, 6, 1, 4, 1, 466, 3, 3, 12),
    _Ty1250CfgNetBPVThresholding_Type()
)
ty1250CfgNetBPVThresholding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ty1250CfgNetBPVThresholding.setStatus("mandatory")
_Ty1250CfgDteTable_ObjectIdentity = ObjectIdentity
ty1250CfgDteTable = _Ty1250CfgDteTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 466, 3, 4)
)


class _Ty1250CfgDteType_Type(Integer32):
    """Custom type ty1250CfgDteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rs449", 3),
          ("v35", 2))
    )


_Ty1250CfgDteType_Type.__name__ = "Integer32"
_Ty1250CfgDteType_Object = MibScalar
ty1250CfgDteType = _Ty1250CfgDteType_Object(
    (1, 3, 6, 1, 4, 1, 466, 3, 4, 1),
    _Ty1250CfgDteType_Type()
)
ty1250CfgDteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty1250CfgDteType.setStatus("mandatory")


class _Ty1250CfgDteClockInvert_Type(Integer32):
    """Custom type ty1250CfgDteClockInvert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invert-dte-clock", 2),
          ("normal-dte-clock", 1))
    )


_Ty1250CfgDteClockInvert_Type.__name__ = "Integer32"
_Ty1250CfgDteClockInvert_Object = MibScalar
ty1250CfgDteClockInvert = _Ty1250CfgDteClockInvert_Object(
    (1, 3, 6, 1, 4, 1, 466, 3, 4, 5),
    _Ty1250CfgDteClockInvert_Type()
)
ty1250CfgDteClockInvert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ty1250CfgDteClockInvert.setStatus("mandatory")


class _Ty1250CfgDteTiming_Type(Integer32):
    """Custom type ty1250CfgDteTiming based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loop1-timing", 1),
          ("loop2-timing", 2))
    )


_Ty1250CfgDteTiming_Type.__name__ = "Integer32"
_Ty1250CfgDteTiming_Object = MibScalar
ty1250CfgDteTiming = _Ty1250CfgDteTiming_Object(
    (1, 3, 6, 1, 4, 1, 466, 3, 4, 6),
    _Ty1250CfgDteTiming_Type()
)
ty1250CfgDteTiming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ty1250CfgDteTiming.setStatus("mandatory")
_Ty1250CfgDialTable_ObjectIdentity = ObjectIdentity
ty1250CfgDialTable = _Ty1250CfgDialTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 466, 3, 5)
)


class _Ty1250CfgDialButton_Type(Integer32):
    """Custom type ty1250CfgDialButton based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable-button", 2),
          ("enable-button", 1))
    )


_Ty1250CfgDialButton_Type.__name__ = "Integer32"
_Ty1250CfgDialButton_Object = MibScalar
ty1250CfgDialButton = _Ty1250CfgDialButton_Object(
    (1, 3, 6, 1, 4, 1, 466, 3, 5, 1),
    _Ty1250CfgDialButton_Type()
)
ty1250CfgDialButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ty1250CfgDialButton.setStatus("mandatory")


class _Ty1250CfgDialDtr_Type(Integer32):
    """Custom type ty1250CfgDialDtr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable-dtr", 2),
          ("enable-dtr", 1))
    )


_Ty1250CfgDialDtr_Type.__name__ = "Integer32"
_Ty1250CfgDialDtr_Object = MibScalar
ty1250CfgDialDtr = _Ty1250CfgDialDtr_Object(
    (1, 3, 6, 1, 4, 1, 466, 3, 5, 2),
    _Ty1250CfgDialDtr_Type()
)
ty1250CfgDialDtr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ty1250CfgDialDtr.setStatus("mandatory")


class _Ty1250CfgDialRtsDisc_Type(Integer32):
    """Custom type ty1250CfgDialRtsDisc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable-rts", 2),
          ("enable-rts", 1))
    )


_Ty1250CfgDialRtsDisc_Type.__name__ = "Integer32"
_Ty1250CfgDialRtsDisc_Object = MibScalar
ty1250CfgDialRtsDisc = _Ty1250CfgDialRtsDisc_Object(
    (1, 3, 6, 1, 4, 1, 466, 3, 5, 3),
    _Ty1250CfgDialRtsDisc_Type()
)
ty1250CfgDialRtsDisc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ty1250CfgDialRtsDisc.setStatus("mandatory")


class _Ty1250CfgDialRi_Type(Integer32):
    """Custom type ty1250CfgDialRi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable-ri", 2),
          ("enable-ri", 1))
    )


_Ty1250CfgDialRi_Type.__name__ = "Integer32"
_Ty1250CfgDialRi_Object = MibScalar
ty1250CfgDialRi = _Ty1250CfgDialRi_Object(
    (1, 3, 6, 1, 4, 1, 466, 3, 5, 4),
    _Ty1250CfgDialRi_Type()
)
ty1250CfgDialRi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ty1250CfgDialRi.setStatus("mandatory")
_Ty1250CfgMaintTable_Object = MibTable
ty1250CfgMaintTable = _Ty1250CfgMaintTable_Object(
    (1, 3, 6, 1, 4, 1, 466, 3, 6)
)
if mibBuilder.loadTexts:
    ty1250CfgMaintTable.setStatus("mandatory")
_Ty1250CfgMaintEntry_Object = MibTableRow
ty1250CfgMaintEntry = _Ty1250CfgMaintEntry_Object(
    (1, 3, 6, 1, 4, 1, 466, 3, 6, 1)
)
ty1250CfgMaintEntry.setIndexNames(
    (0, "TY1250I-MIB", "ty1250CfgMaintIndex"),
)
if mibBuilder.loadTexts:
    ty1250CfgMaintEntry.setStatus("mandatory")


class _Ty1250CfgMaintIndex_Type(Integer32):
    """Custom type ty1250CfgMaintIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Ty1250CfgMaintIndex_Type.__name__ = "Integer32"
_Ty1250CfgMaintIndex_Object = MibTableColumn
ty1250CfgMaintIndex = _Ty1250CfgMaintIndex_Object(
    (1, 3, 6, 1, 4, 1, 466, 3, 6, 1, 1),
    _Ty1250CfgMaintIndex_Type()
)
ty1250CfgMaintIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty1250CfgMaintIndex.setStatus("mandatory")


class _Ty1250CfgMaintMode_Type(Integer32):
    """Custom type ty1250CfgMaintMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("ascii-vt100", 4),
          ("cslip", 8),
          ("slip", 7))
    )


_Ty1250CfgMaintMode_Type.__name__ = "Integer32"
_Ty1250CfgMaintMode_Object = MibTableColumn
ty1250CfgMaintMode = _Ty1250CfgMaintMode_Object(
    (1, 3, 6, 1, 4, 1, 466, 3, 6, 1, 2),
    _Ty1250CfgMaintMode_Type()
)
ty1250CfgMaintMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ty1250CfgMaintMode.setStatus("mandatory")


class _Ty1250CfgMaintBaud_Type(Integer32):
    """Custom type ty1250CfgMaintBaud based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("baud-19200", 5),
          ("baud-2400", 2),
          ("baud-9600", 4))
    )


_Ty1250CfgMaintBaud_Type.__name__ = "Integer32"
_Ty1250CfgMaintBaud_Object = MibTableColumn
ty1250CfgMaintBaud = _Ty1250CfgMaintBaud_Object(
    (1, 3, 6, 1, 4, 1, 466, 3, 6, 1, 3),
    _Ty1250CfgMaintBaud_Type()
)
ty1250CfgMaintBaud.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ty1250CfgMaintBaud.setStatus("mandatory")


class _Ty1250CfgMaintDataBits_Type(Integer32):
    """Custom type ty1250CfgMaintDataBits based on Integer32"""
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


_Ty1250CfgMaintDataBits_Type.__name__ = "Integer32"
_Ty1250CfgMaintDataBits_Object = MibTableColumn
ty1250CfgMaintDataBits = _Ty1250CfgMaintDataBits_Object(
    (1, 3, 6, 1, 4, 1, 466, 3, 6, 1, 4),
    _Ty1250CfgMaintDataBits_Type()
)
ty1250CfgMaintDataBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ty1250CfgMaintDataBits.setStatus("mandatory")


class _Ty1250CfgMaintStopBits_Type(Integer32):
    """Custom type ty1250CfgMaintStopBits based on Integer32"""
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


_Ty1250CfgMaintStopBits_Type.__name__ = "Integer32"
_Ty1250CfgMaintStopBits_Object = MibTableColumn
ty1250CfgMaintStopBits = _Ty1250CfgMaintStopBits_Object(
    (1, 3, 6, 1, 4, 1, 466, 3, 6, 1, 5),
    _Ty1250CfgMaintStopBits_Type()
)
ty1250CfgMaintStopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ty1250CfgMaintStopBits.setStatus("mandatory")


class _Ty1250CfgMaintParity_Type(Integer32):
    """Custom type ty1250CfgMaintParity based on Integer32"""
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


_Ty1250CfgMaintParity_Type.__name__ = "Integer32"
_Ty1250CfgMaintParity_Object = MibTableColumn
ty1250CfgMaintParity = _Ty1250CfgMaintParity_Object(
    (1, 3, 6, 1, 4, 1, 466, 3, 6, 1, 6),
    _Ty1250CfgMaintParity_Type()
)
ty1250CfgMaintParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ty1250CfgMaintParity.setStatus("mandatory")


class _Ty1250CfgMaintFlowCtrl_Type(Integer32):
    """Custom type ty1250CfgMaintFlowCtrl based on Integer32"""
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


_Ty1250CfgMaintFlowCtrl_Type.__name__ = "Integer32"
_Ty1250CfgMaintFlowCtrl_Object = MibTableColumn
ty1250CfgMaintFlowCtrl = _Ty1250CfgMaintFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 466, 3, 6, 1, 7),
    _Ty1250CfgMaintFlowCtrl_Type()
)
ty1250CfgMaintFlowCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ty1250CfgMaintFlowCtrl.setStatus("mandatory")
_Ty1250CfgSlipTable_ObjectIdentity = ObjectIdentity
ty1250CfgSlipTable = _Ty1250CfgSlipTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 466, 3, 8)
)
_Ty1250CfgSlipMyIP_Type = IpAddress
_Ty1250CfgSlipMyIP_Object = MibScalar
ty1250CfgSlipMyIP = _Ty1250CfgSlipMyIP_Object(
    (1, 3, 6, 1, 4, 1, 466, 3, 8, 1),
    _Ty1250CfgSlipMyIP_Type()
)
ty1250CfgSlipMyIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ty1250CfgSlipMyIP.setStatus("mandatory")
_Ty1250CfgSlipPeerIP_Type = IpAddress
_Ty1250CfgSlipPeerIP_Object = MibScalar
ty1250CfgSlipPeerIP = _Ty1250CfgSlipPeerIP_Object(
    (1, 3, 6, 1, 4, 1, 466, 3, 8, 2),
    _Ty1250CfgSlipPeerIP_Type()
)
ty1250CfgSlipPeerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ty1250CfgSlipPeerIP.setStatus("mandatory")
_Ty1250CfgSlipMask_Type = IpAddress
_Ty1250CfgSlipMask_Object = MibScalar
ty1250CfgSlipMask = _Ty1250CfgSlipMask_Object(
    (1, 3, 6, 1, 4, 1, 466, 3, 8, 3),
    _Ty1250CfgSlipMask_Type()
)
ty1250CfgSlipMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ty1250CfgSlipMask.setStatus("mandatory")


class _Ty1250CfgSlipMaxMTU_Type(Integer32):
    """Custom type ty1250CfgSlipMaxMTU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Ty1250CfgSlipMaxMTU_Type.__name__ = "Integer32"
_Ty1250CfgSlipMaxMTU_Object = MibScalar
ty1250CfgSlipMaxMTU = _Ty1250CfgSlipMaxMTU_Object(
    (1, 3, 6, 1, 4, 1, 466, 3, 8, 4),
    _Ty1250CfgSlipMaxMTU_Type()
)
ty1250CfgSlipMaxMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ty1250CfgSlipMaxMTU.setStatus("mandatory")
_Ty1250CallTable_ObjectIdentity = ObjectIdentity
ty1250CallTable = _Ty1250CallTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 466, 3, 9)
)


class _Ty1250CallStatus_Type(Integer32):
    """Custom type ty1250CallStatus based on Integer32"""
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
              253,
              254)
        )
    )
    namedValues = NamedValues(
        *(("active", 7),
          ("busy", 4),
          ("dialing", 3),
          ("idle", 2),
          ("incoming-call", 8),
          ("line-down", 254),
          ("line-in-maintenance", 253),
          ("none", 1),
          ("redialing", 6),
          ("waiting-for-redial", 5))
    )


_Ty1250CallStatus_Type.__name__ = "Integer32"
_Ty1250CallStatus_Object = MibScalar
ty1250CallStatus = _Ty1250CallStatus_Object(
    (1, 3, 6, 1, 4, 1, 466, 3, 9, 1),
    _Ty1250CallStatus_Type()
)
ty1250CallStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty1250CallStatus.setStatus("mandatory")


class _Ty1250CallNumber_Type(DisplayString):
    """Custom type ty1250CallNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Ty1250CallNumber_Type.__name__ = "DisplayString"
_Ty1250CallNumber_Object = MibScalar
ty1250CallNumber = _Ty1250CallNumber_Object(
    (1, 3, 6, 1, 4, 1, 466, 3, 9, 2),
    _Ty1250CallNumber_Type()
)
ty1250CallNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ty1250CallNumber.setStatus("mandatory")
_Ty1250CallUpTime_Type = TimeTicks
_Ty1250CallUpTime_Object = MibScalar
ty1250CallUpTime = _Ty1250CallUpTime_Object(
    (1, 3, 6, 1, 4, 1, 466, 3, 9, 3),
    _Ty1250CallUpTime_Type()
)
ty1250CallUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty1250CallUpTime.setStatus("mandatory")


class _Ty1250CallState_Type(Integer32):
    """Custom type ty1250CallState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("answer", 3),
          ("connect", 1),
          ("disconnect", 2))
    )


_Ty1250CallState_Type.__name__ = "Integer32"
_Ty1250CallState_Object = MibScalar
ty1250CallState = _Ty1250CallState_Object(
    (1, 3, 6, 1, 4, 1, 466, 3, 9, 4),
    _Ty1250CallState_Type()
)
ty1250CallState.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    ty1250CallState.setStatus("mandatory")
_Ty1250DiagUnitTable_ObjectIdentity = ObjectIdentity
ty1250DiagUnitTable = _Ty1250DiagUnitTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 466, 3, 10)
)


class _Ty1250DiagUnitLocLoop_Type(Integer32):
    """Custom type ty1250DiagUnitLocLoop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable-loopback-mode", 2),
          ("enable-loopback-mode", 1))
    )


_Ty1250DiagUnitLocLoop_Type.__name__ = "Integer32"
_Ty1250DiagUnitLocLoop_Object = MibScalar
ty1250DiagUnitLocLoop = _Ty1250DiagUnitLocLoop_Object(
    (1, 3, 6, 1, 4, 1, 466, 3, 10, 1),
    _Ty1250DiagUnitLocLoop_Type()
)
ty1250DiagUnitLocLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ty1250DiagUnitLocLoop.setStatus("mandatory")


class _Ty1250DiagUnitReset_Type(Integer32):
    """Custom type ty1250DiagUnitReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset-unit", 1)
    )


_Ty1250DiagUnitReset_Type.__name__ = "Integer32"
_Ty1250DiagUnitReset_Object = MibScalar
ty1250DiagUnitReset = _Ty1250DiagUnitReset_Object(
    (1, 3, 6, 1, 4, 1, 466, 3, 10, 2),
    _Ty1250DiagUnitReset_Type()
)
ty1250DiagUnitReset.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    ty1250DiagUnitReset.setStatus("mandatory")
_Ty1250DiagNetTable_ObjectIdentity = ObjectIdentity
ty1250DiagNetTable = _Ty1250DiagNetTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 466, 3, 11)
)


class _Ty1250DiagNetLineStatus_Type(Integer32):
    """Custom type ty1250DiagNetLineStatus based on Integer32"""
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
        *(("bpv-threshold-failure", 4),
          ("in-sync", 1),
          ("loss-of-signal", 5),
          ("out-of-frame", 3),
          ("out-of-service", 2),
          ("simplex-current-loopback", 6))
    )


_Ty1250DiagNetLineStatus_Type.__name__ = "Integer32"
_Ty1250DiagNetLineStatus_Object = MibScalar
ty1250DiagNetLineStatus = _Ty1250DiagNetLineStatus_Object(
    (1, 3, 6, 1, 4, 1, 466, 3, 11, 1),
    _Ty1250DiagNetLineStatus_Type()
)
ty1250DiagNetLineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty1250DiagNetLineStatus.setStatus("mandatory")


class _Ty1250DiagNetLclLpbk_Type(Integer32):
    """Custom type ty1250DiagNetLclLpbk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable-loopback-mode", 2),
          ("enable-loopback-mode", 1))
    )


_Ty1250DiagNetLclLpbk_Type.__name__ = "Integer32"
_Ty1250DiagNetLclLpbk_Object = MibScalar
ty1250DiagNetLclLpbk = _Ty1250DiagNetLclLpbk_Object(
    (1, 3, 6, 1, 4, 1, 466, 3, 11, 2),
    _Ty1250DiagNetLclLpbk_Type()
)
ty1250DiagNetLclLpbk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ty1250DiagNetLclLpbk.setStatus("mandatory")


class _Ty1250DiagNetRmtLpbk_Type(Integer32):
    """Custom type ty1250DiagNetRmtLpbk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no-loop-from-remote", 1),
          ("non-latching-loop", 3),
          ("simplex-current-loop", 2))
    )


_Ty1250DiagNetRmtLpbk_Type.__name__ = "Integer32"
_Ty1250DiagNetRmtLpbk_Object = MibScalar
ty1250DiagNetRmtLpbk = _Ty1250DiagNetRmtLpbk_Object(
    (1, 3, 6, 1, 4, 1, 466, 3, 11, 3),
    _Ty1250DiagNetRmtLpbk_Type()
)
ty1250DiagNetRmtLpbk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty1250DiagNetRmtLpbk.setStatus("mandatory")
_Ty1250DiagDteTable_ObjectIdentity = ObjectIdentity
ty1250DiagDteTable = _Ty1250DiagDteTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 466, 3, 12)
)


class _Ty1250DiagDteSigRTS_Type(Integer32):
    """Custom type ty1250DiagDteSigRTS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rts-signal-off", 2),
          ("rts-signal-on", 1))
    )


_Ty1250DiagDteSigRTS_Type.__name__ = "Integer32"
_Ty1250DiagDteSigRTS_Object = MibScalar
ty1250DiagDteSigRTS = _Ty1250DiagDteSigRTS_Object(
    (1, 3, 6, 1, 4, 1, 466, 3, 12, 1),
    _Ty1250DiagDteSigRTS_Type()
)
ty1250DiagDteSigRTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty1250DiagDteSigRTS.setStatus("mandatory")


class _Ty1250DiagDteSigDTR_Type(Integer32):
    """Custom type ty1250DiagDteSigDTR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dtr-signal-off", 2),
          ("dtr-signal-on", 1))
    )


_Ty1250DiagDteSigDTR_Type.__name__ = "Integer32"
_Ty1250DiagDteSigDTR_Object = MibScalar
ty1250DiagDteSigDTR = _Ty1250DiagDteSigDTR_Object(
    (1, 3, 6, 1, 4, 1, 466, 3, 12, 2),
    _Ty1250DiagDteSigDTR_Type()
)
ty1250DiagDteSigDTR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty1250DiagDteSigDTR.setStatus("mandatory")


class _Ty1250DiagDteLclLpbk_Type(Integer32):
    """Custom type ty1250DiagDteLclLpbk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable-loopback-mode", 2),
          ("enable-loopback-mode", 1))
    )


_Ty1250DiagDteLclLpbk_Type.__name__ = "Integer32"
_Ty1250DiagDteLclLpbk_Object = MibScalar
ty1250DiagDteLclLpbk = _Ty1250DiagDteLclLpbk_Object(
    (1, 3, 6, 1, 4, 1, 466, 3, 12, 5),
    _Ty1250DiagDteLclLpbk_Type()
)
ty1250DiagDteLclLpbk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ty1250DiagDteLclLpbk.setStatus("mandatory")


class _Ty1250DiagDteV54Lpbk_Type(Integer32):
    """Custom type ty1250DiagDteV54Lpbk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loopback-disable", 2),
          ("loopback-enable", 1))
    )


_Ty1250DiagDteV54Lpbk_Type.__name__ = "Integer32"
_Ty1250DiagDteV54Lpbk_Object = MibScalar
ty1250DiagDteV54Lpbk = _Ty1250DiagDteV54Lpbk_Object(
    (1, 3, 6, 1, 4, 1, 466, 3, 12, 6),
    _Ty1250DiagDteV54Lpbk_Type()
)
ty1250DiagDteV54Lpbk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty1250DiagDteV54Lpbk.setStatus("mandatory")


class _Ty1250DiagDteBerState_Type(Integer32):
    """Custom type ty1250DiagDteBerState based on Integer32"""
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
        *(("clear-error-bert-test", 4),
          ("inject-error-bert-test", 3),
          ("start-bert-test", 1),
          ("stop-bert-test", 2))
    )


_Ty1250DiagDteBerState_Type.__name__ = "Integer32"
_Ty1250DiagDteBerState_Object = MibScalar
ty1250DiagDteBerState = _Ty1250DiagDteBerState_Object(
    (1, 3, 6, 1, 4, 1, 466, 3, 12, 7),
    _Ty1250DiagDteBerState_Type()
)
ty1250DiagDteBerState.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    ty1250DiagDteBerState.setStatus("mandatory")


class _Ty1250DiagDteBerStatus_Type(Integer32):
    """Custom type ty1250DiagDteBerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bert-in-sync", 3),
          ("bert-off", 1),
          ("bert-out-of-sync", 2))
    )


_Ty1250DiagDteBerStatus_Type.__name__ = "Integer32"
_Ty1250DiagDteBerStatus_Object = MibScalar
ty1250DiagDteBerStatus = _Ty1250DiagDteBerStatus_Object(
    (1, 3, 6, 1, 4, 1, 466, 3, 12, 8),
    _Ty1250DiagDteBerStatus_Type()
)
ty1250DiagDteBerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty1250DiagDteBerStatus.setStatus("mandatory")
_Ty1250DiagDteBerErrors_Type = Counter32
_Ty1250DiagDteBerErrors_Object = MibScalar
ty1250DiagDteBerErrors = _Ty1250DiagDteBerErrors_Object(
    (1, 3, 6, 1, 4, 1, 466, 3, 12, 9),
    _Ty1250DiagDteBerErrors_Type()
)
ty1250DiagDteBerErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty1250DiagDteBerErrors.setStatus("mandatory")
_Ty1250DiagDteBerErrSec_Type = Counter32
_Ty1250DiagDteBerErrSec_Object = MibScalar
ty1250DiagDteBerErrSec = _Ty1250DiagDteBerErrSec_Object(
    (1, 3, 6, 1, 4, 1, 466, 3, 12, 10),
    _Ty1250DiagDteBerErrSec_Type()
)
ty1250DiagDteBerErrSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty1250DiagDteBerErrSec.setStatus("mandatory")
_Ty1250DiagDteBerTimeElaps_Type = TimeTicks
_Ty1250DiagDteBerTimeElaps_Object = MibScalar
ty1250DiagDteBerTimeElaps = _Ty1250DiagDteBerTimeElaps_Object(
    (1, 3, 6, 1, 4, 1, 466, 3, 12, 11),
    _Ty1250DiagDteBerTimeElaps_Type()
)
ty1250DiagDteBerTimeElaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty1250DiagDteBerTimeElaps.setStatus("mandatory")
_Ty1250DiagDteBerResyncs_Type = Counter32
_Ty1250DiagDteBerResyncs_Object = MibScalar
ty1250DiagDteBerResyncs = _Ty1250DiagDteBerResyncs_Object(
    (1, 3, 6, 1, 4, 1, 466, 3, 12, 12),
    _Ty1250DiagDteBerResyncs_Type()
)
ty1250DiagDteBerResyncs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty1250DiagDteBerResyncs.setStatus("mandatory")


class _Ty1250DiagDteRmtV54Lpbk_Type(Integer32):
    """Custom type ty1250DiagDteRmtV54Lpbk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("transmit-code-disable", 4),
          ("transmit-code-enable", 3))
    )


_Ty1250DiagDteRmtV54Lpbk_Type.__name__ = "Integer32"
_Ty1250DiagDteRmtV54Lpbk_Object = MibScalar
ty1250DiagDteRmtV54Lpbk = _Ty1250DiagDteRmtV54Lpbk_Object(
    (1, 3, 6, 1, 4, 1, 466, 3, 12, 13),
    _Ty1250DiagDteRmtV54Lpbk_Type()
)
ty1250DiagDteRmtV54Lpbk.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    ty1250DiagDteRmtV54Lpbk.setStatus("mandatory")


class _Ty1250AlarmType_Type(Integer32):
    """Custom type ty1250AlarmType based on Integer32"""
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
              25,
              26,
              27,
              28,
              29,
              30,
              31)
        )
    )
    namedValues = NamedValues(
        *(("bad-config-in-set", 7),
          ("bert-test-pattern-completed", 24),
          ("bert-test-pattern-failure", 29),
          ("bert-test-pattern-initiated", 23),
          ("bpv-threshold-acceptable", 10),
          ("bpv-threshold-exceeded", 9),
          ("config-local-update", 8),
          ("connect-failure", 4),
          ("connected", 3),
          ("disconnected", 6),
          ("incoming-call", 5),
          ("line-failure", 1),
          ("line-in-service", 2),
          ("local-dte-loopback-disabled", 26),
          ("local-dte-loopback-enabled", 25),
          ("local-dte-loopback-failure", 30),
          ("local-network-loopback-disabled", 14),
          ("local-network-loopback-enabled", 13),
          ("local-network-loopback-failure", 28),
          ("local-unit-loopback-disabled", 12),
          ("local-unit-loopback-enabled", 11),
          ("local-unit-loopback-failure", 27),
          ("remote-network-non-latching-loopback-disabled", 18),
          ("remote-network-non-latching-loopback-enabled", 17),
          ("remote-network-simplex-loopback-disabled", 16),
          ("remote-network-simplex-loopback-enabled", 15),
          ("v54-loop-down-completed", 20),
          ("v54-loop-up-initiated", 19),
          ("v54-loopback-disabled-by-remote", 22),
          ("v54-loopback-enabled-by-remote", 21),
          ("v54-loopback-failure", 31))
    )


_Ty1250AlarmType_Type.__name__ = "Integer32"
_Ty1250AlarmType_Object = MibScalar
ty1250AlarmType = _Ty1250AlarmType_Object(
    (1, 3, 6, 1, 4, 1, 466, 3, 13),
    _Ty1250AlarmType_Type()
)
ty1250AlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty1250AlarmType.setStatus("mandatory")
_Ty1250CfgSnmpTable_ObjectIdentity = ObjectIdentity
ty1250CfgSnmpTable = _Ty1250CfgSnmpTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 466, 3, 14)
)
_Ty1250CfgSnmpManagerIP_Type = IpAddress
_Ty1250CfgSnmpManagerIP_Object = MibScalar
ty1250CfgSnmpManagerIP = _Ty1250CfgSnmpManagerIP_Object(
    (1, 3, 6, 1, 4, 1, 466, 3, 14, 1),
    _Ty1250CfgSnmpManagerIP_Type()
)
ty1250CfgSnmpManagerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ty1250CfgSnmpManagerIP.setStatus("mandatory")
_Ty1250StatsDteTable_ObjectIdentity = ObjectIdentity
ty1250StatsDteTable = _Ty1250StatsDteTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 466, 3, 15)
)
_Ty1250StatsDteTxByteCount_Type = Integer32
_Ty1250StatsDteTxByteCount_Object = MibScalar
ty1250StatsDteTxByteCount = _Ty1250StatsDteTxByteCount_Object(
    (1, 3, 6, 1, 4, 1, 466, 3, 15, 1),
    _Ty1250StatsDteTxByteCount_Type()
)
ty1250StatsDteTxByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty1250StatsDteTxByteCount.setStatus("mandatory")
_Ty1250StatsDteRxByteCount_Type = Integer32
_Ty1250StatsDteRxByteCount_Object = MibScalar
ty1250StatsDteRxByteCount = _Ty1250StatsDteRxByteCount_Object(
    (1, 3, 6, 1, 4, 1, 466, 3, 15, 2),
    _Ty1250StatsDteRxByteCount_Type()
)
ty1250StatsDteRxByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty1250StatsDteRxByteCount.setStatus("mandatory")


class _Ty1250StatsDteClearStats_Type(Integer32):
    """Custom type ty1250StatsDteClearStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear-statistics", 1)
    )


_Ty1250StatsDteClearStats_Type.__name__ = "Integer32"
_Ty1250StatsDteClearStats_Object = MibScalar
ty1250StatsDteClearStats = _Ty1250StatsDteClearStats_Object(
    (1, 3, 6, 1, 4, 1, 466, 3, 15, 3),
    _Ty1250StatsDteClearStats_Type()
)
ty1250StatsDteClearStats.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    ty1250StatsDteClearStats.setStatus("mandatory")
_Ty1250StatsNetTable_ObjectIdentity = ObjectIdentity
ty1250StatsNetTable = _Ty1250StatsNetTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 466, 3, 16)
)
_Ty1250StatsNetLoopLength_Type = Integer32
_Ty1250StatsNetLoopLength_Object = MibScalar
ty1250StatsNetLoopLength = _Ty1250StatsNetLoopLength_Object(
    (1, 3, 6, 1, 4, 1, 466, 3, 16, 1),
    _Ty1250StatsNetLoopLength_Type()
)
ty1250StatsNetLoopLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty1250StatsNetLoopLength.setStatus("mandatory")
_Ty1250StatsNetBpvCount_Type = Integer32
_Ty1250StatsNetBpvCount_Object = MibScalar
ty1250StatsNetBpvCount = _Ty1250StatsNetBpvCount_Object(
    (1, 3, 6, 1, 4, 1, 466, 3, 16, 2),
    _Ty1250StatsNetBpvCount_Type()
)
ty1250StatsNetBpvCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty1250StatsNetBpvCount.setStatus("mandatory")
_Ty1250StatsNetTxByteCount_Type = Integer32
_Ty1250StatsNetTxByteCount_Object = MibScalar
ty1250StatsNetTxByteCount = _Ty1250StatsNetTxByteCount_Object(
    (1, 3, 6, 1, 4, 1, 466, 3, 16, 3),
    _Ty1250StatsNetTxByteCount_Type()
)
ty1250StatsNetTxByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty1250StatsNetTxByteCount.setStatus("mandatory")
_Ty1250StatsNetRxByteCount_Type = Integer32
_Ty1250StatsNetRxByteCount_Object = MibScalar
ty1250StatsNetRxByteCount = _Ty1250StatsNetRxByteCount_Object(
    (1, 3, 6, 1, 4, 1, 466, 3, 16, 4),
    _Ty1250StatsNetRxByteCount_Type()
)
ty1250StatsNetRxByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ty1250StatsNetRxByteCount.setStatus("mandatory")


class _Ty1250StatsNetClearStats_Type(Integer32):
    """Custom type ty1250StatsNetClearStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear-statistics", 1)
    )


_Ty1250StatsNetClearStats_Type.__name__ = "Integer32"
_Ty1250StatsNetClearStats_Object = MibScalar
ty1250StatsNetClearStats = _Ty1250StatsNetClearStats_Object(
    (1, 3, 6, 1, 4, 1, 466, 3, 16, 5),
    _Ty1250StatsNetClearStats_Type()
)
ty1250StatsNetClearStats.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    ty1250StatsNetClearStats.setStatus("mandatory")
_Ty1250CfgTelnetTable_ObjectIdentity = ObjectIdentity
ty1250CfgTelnetTable = _Ty1250CfgTelnetTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 466, 3, 17)
)


class _Ty1250CfgTelnetEnable_Type(Integer32):
    """Custom type ty1250CfgTelnetEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable-telnet", 2),
          ("enable-telnet", 1))
    )


_Ty1250CfgTelnetEnable_Type.__name__ = "Integer32"
_Ty1250CfgTelnetEnable_Object = MibScalar
ty1250CfgTelnetEnable = _Ty1250CfgTelnetEnable_Object(
    (1, 3, 6, 1, 4, 1, 466, 3, 17, 1),
    _Ty1250CfgTelnetEnable_Type()
)
ty1250CfgTelnetEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ty1250CfgTelnetEnable.setStatus("mandatory")


class _Ty1250CfgTelnetAutoLogOut_Type(Integer32):
    """Custom type ty1250CfgTelnetAutoLogOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("autologout-at-15-minutes", 1),
          ("disable-autologout", 2))
    )


_Ty1250CfgTelnetAutoLogOut_Type.__name__ = "Integer32"
_Ty1250CfgTelnetAutoLogOut_Object = MibScalar
ty1250CfgTelnetAutoLogOut = _Ty1250CfgTelnetAutoLogOut_Object(
    (1, 3, 6, 1, 4, 1, 466, 3, 17, 2),
    _Ty1250CfgTelnetAutoLogOut_Type()
)
ty1250CfgTelnetAutoLogOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ty1250CfgTelnetAutoLogOut.setStatus("mandatory")

# Managed Objects groups


# Notification objects

ty1250Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 466, 3, 0, 0)
)
ty1250Trap.setObjects(
    ("TY1250I-MIB", "ty1250AlarmType")
)
if mibBuilder.loadTexts:
    ty1250Trap.setStatus(
        ""
    )

ty1250LineFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 466, 3, 0, 1)
)
ty1250LineFailureTrap.setObjects(
    ("TY1250I-MIB", "ty1250AlarmType")
)
if mibBuilder.loadTexts:
    ty1250LineFailureTrap.setStatus(
        ""
    )

ty1250LineInServiceTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 466, 3, 0, 2)
)
ty1250LineInServiceTrap.setObjects(
    ("TY1250I-MIB", "ty1250AlarmType")
)
if mibBuilder.loadTexts:
    ty1250LineInServiceTrap.setStatus(
        ""
    )

ty1250ConnectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 466, 3, 0, 3)
)
ty1250ConnectedTrap.setObjects(
    ("TY1250I-MIB", "ty1250AlarmType")
)
if mibBuilder.loadTexts:
    ty1250ConnectedTrap.setStatus(
        ""
    )

ty1250ConnectFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 466, 3, 0, 4)
)
ty1250ConnectFailureTrap.setObjects(
    ("TY1250I-MIB", "ty1250AlarmType")
)
if mibBuilder.loadTexts:
    ty1250ConnectFailureTrap.setStatus(
        ""
    )

ty1250IncomingCallTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 466, 3, 0, 5)
)
ty1250IncomingCallTrap.setObjects(
    ("TY1250I-MIB", "ty1250AlarmType")
)
if mibBuilder.loadTexts:
    ty1250IncomingCallTrap.setStatus(
        ""
    )

ty1250DisconnectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 466, 3, 0, 6)
)
ty1250DisconnectedTrap.setObjects(
    ("TY1250I-MIB", "ty1250AlarmType")
)
if mibBuilder.loadTexts:
    ty1250DisconnectedTrap.setStatus(
        ""
    )

ty1250BadConfigTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 466, 3, 0, 7)
)
ty1250BadConfigTrap.setObjects(
    ("TY1250I-MIB", "ty1250AlarmType")
)
if mibBuilder.loadTexts:
    ty1250BadConfigTrap.setStatus(
        ""
    )

ty1250LocalConfigTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 466, 3, 0, 8)
)
ty1250LocalConfigTrap.setObjects(
    ("TY1250I-MIB", "ty1250AlarmType")
)
if mibBuilder.loadTexts:
    ty1250LocalConfigTrap.setStatus(
        ""
    )

ty1250BPVThresholdExceededTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 466, 3, 0, 9)
)
ty1250BPVThresholdExceededTrap.setObjects(
    ("TY1250I-MIB", "ty1250AlarmType")
)
if mibBuilder.loadTexts:
    ty1250BPVThresholdExceededTrap.setStatus(
        ""
    )

ty1250BPVThresholdAcceptableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 466, 3, 0, 10)
)
ty1250BPVThresholdAcceptableTrap.setObjects(
    ("TY1250I-MIB", "ty1250AlarmType")
)
if mibBuilder.loadTexts:
    ty1250BPVThresholdAcceptableTrap.setStatus(
        ""
    )

ty1250LocalUnitLoopbackEnabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 466, 3, 0, 11)
)
ty1250LocalUnitLoopbackEnabledTrap.setObjects(
    ("TY1250I-MIB", "ty1250AlarmType")
)
if mibBuilder.loadTexts:
    ty1250LocalUnitLoopbackEnabledTrap.setStatus(
        ""
    )

ty1250LocalUnitLoopbackDisabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 466, 3, 0, 12)
)
ty1250LocalUnitLoopbackDisabledTrap.setObjects(
    ("TY1250I-MIB", "ty1250AlarmType")
)
if mibBuilder.loadTexts:
    ty1250LocalUnitLoopbackDisabledTrap.setStatus(
        ""
    )

ty1250LocalNetLoopbackEnabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 466, 3, 0, 13)
)
ty1250LocalNetLoopbackEnabledTrap.setObjects(
    ("TY1250I-MIB", "ty1250AlarmType")
)
if mibBuilder.loadTexts:
    ty1250LocalNetLoopbackEnabledTrap.setStatus(
        ""
    )

ty1250LocalNetLoopbackDisabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 466, 3, 0, 14)
)
ty1250LocalNetLoopbackDisabledTrap.setObjects(
    ("TY1250I-MIB", "ty1250AlarmType")
)
if mibBuilder.loadTexts:
    ty1250LocalNetLoopbackDisabledTrap.setStatus(
        ""
    )

ty1250SimplexCurrentLoopbackEnabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 466, 3, 0, 15)
)
ty1250SimplexCurrentLoopbackEnabledTrap.setObjects(
    ("TY1250I-MIB", "ty1250AlarmType")
)
if mibBuilder.loadTexts:
    ty1250SimplexCurrentLoopbackEnabledTrap.setStatus(
        ""
    )

ty1250SimplexCurrentLoopbackDisabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 466, 3, 0, 16)
)
ty1250SimplexCurrentLoopbackDisabledTrap.setObjects(
    ("TY1250I-MIB", "ty1250AlarmType")
)
if mibBuilder.loadTexts:
    ty1250SimplexCurrentLoopbackDisabledTrap.setStatus(
        ""
    )

ty1250NonLatchingLoopbackEnabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 466, 3, 0, 17)
)
ty1250NonLatchingLoopbackEnabledTrap.setObjects(
    ("TY1250I-MIB", "ty1250AlarmType")
)
if mibBuilder.loadTexts:
    ty1250NonLatchingLoopbackEnabledTrap.setStatus(
        ""
    )

ty1250NonLatchingLoopbackDisabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 466, 3, 0, 18)
)
ty1250NonLatchingLoopbackDisabledTrap.setObjects(
    ("TY1250I-MIB", "ty1250AlarmType")
)
if mibBuilder.loadTexts:
    ty1250NonLatchingLoopbackDisabledTrap.setStatus(
        ""
    )

ty1250V54LoopUpInitiatedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 466, 3, 0, 19)
)
ty1250V54LoopUpInitiatedTrap.setObjects(
    ("TY1250I-MIB", "ty1250AlarmType")
)
if mibBuilder.loadTexts:
    ty1250V54LoopUpInitiatedTrap.setStatus(
        ""
    )

ty1250V54LoopDownCompletedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 466, 3, 0, 20)
)
ty1250V54LoopDownCompletedTrap.setObjects(
    ("TY1250I-MIB", "ty1250AlarmType")
)
if mibBuilder.loadTexts:
    ty1250V54LoopDownCompletedTrap.setStatus(
        ""
    )

ty1250V54LoopbackEnabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 466, 3, 0, 21)
)
ty1250V54LoopbackEnabledTrap.setObjects(
    ("TY1250I-MIB", "ty1250AlarmType")
)
if mibBuilder.loadTexts:
    ty1250V54LoopbackEnabledTrap.setStatus(
        ""
    )

ty1250V54LoopbackDisabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 466, 3, 0, 22)
)
ty1250V54LoopbackDisabledTrap.setObjects(
    ("TY1250I-MIB", "ty1250AlarmType")
)
if mibBuilder.loadTexts:
    ty1250V54LoopbackDisabledTrap.setStatus(
        ""
    )

ty1250BertInitiatedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 466, 3, 0, 23)
)
ty1250BertInitiatedTrap.setObjects(
    ("TY1250I-MIB", "ty1250AlarmType")
)
if mibBuilder.loadTexts:
    ty1250BertInitiatedTrap.setStatus(
        ""
    )

ty1250BertCompletedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 466, 3, 0, 24)
)
ty1250BertCompletedTrap.setObjects(
    ("TY1250I-MIB", "ty1250AlarmType")
)
if mibBuilder.loadTexts:
    ty1250BertCompletedTrap.setStatus(
        ""
    )

ty1250LocalDteLoopbackEnabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 466, 3, 0, 25)
)
ty1250LocalDteLoopbackEnabledTrap.setObjects(
    ("TY1250I-MIB", "ty1250AlarmType")
)
if mibBuilder.loadTexts:
    ty1250LocalDteLoopbackEnabledTrap.setStatus(
        ""
    )

ty1250LocalDteLoopbackDisabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 466, 3, 0, 26)
)
ty1250LocalDteLoopbackDisabledTrap.setObjects(
    ("TY1250I-MIB", "ty1250AlarmType")
)
if mibBuilder.loadTexts:
    ty1250LocalDteLoopbackDisabledTrap.setStatus(
        ""
    )

ty1250LocalUnitLoopbackFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 466, 3, 0, 27)
)
ty1250LocalUnitLoopbackFailedTrap.setObjects(
    ("TY1250I-MIB", "ty1250AlarmType")
)
if mibBuilder.loadTexts:
    ty1250LocalUnitLoopbackFailedTrap.setStatus(
        ""
    )

ty1250LocalNetLoopbackFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 466, 3, 0, 28)
)
ty1250LocalNetLoopbackFailedTrap.setObjects(
    ("TY1250I-MIB", "ty1250AlarmType")
)
if mibBuilder.loadTexts:
    ty1250LocalNetLoopbackFailedTrap.setStatus(
        ""
    )

ty1250BertFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 466, 3, 0, 29)
)
ty1250BertFailedTrap.setObjects(
    ("TY1250I-MIB", "ty1250AlarmType")
)
if mibBuilder.loadTexts:
    ty1250BertFailedTrap.setStatus(
        ""
    )

ty1250LocalDteLoopbackFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 466, 3, 0, 30)
)
ty1250LocalDteLoopbackFailedTrap.setObjects(
    ("TY1250I-MIB", "ty1250AlarmType")
)
if mibBuilder.loadTexts:
    ty1250LocalDteLoopbackFailedTrap.setStatus(
        ""
    )

ty1250V54LoopbackFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 466, 3, 0, 31)
)
ty1250V54LoopbackFailedTrap.setObjects(
    ("TY1250I-MIB", "ty1250AlarmType")
)
if mibBuilder.loadTexts:
    ty1250V54LoopbackFailedTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TY1250I-MIB",
    **{"tylink": tylink,
       "dsucsu": dsucsu,
       "tyview": tyview,
       "ty1250": ty1250,
       "ty1250Trap": ty1250Trap,
       "ty1250LineFailureTrap": ty1250LineFailureTrap,
       "ty1250LineInServiceTrap": ty1250LineInServiceTrap,
       "ty1250ConnectedTrap": ty1250ConnectedTrap,
       "ty1250ConnectFailureTrap": ty1250ConnectFailureTrap,
       "ty1250IncomingCallTrap": ty1250IncomingCallTrap,
       "ty1250DisconnectedTrap": ty1250DisconnectedTrap,
       "ty1250BadConfigTrap": ty1250BadConfigTrap,
       "ty1250LocalConfigTrap": ty1250LocalConfigTrap,
       "ty1250BPVThresholdExceededTrap": ty1250BPVThresholdExceededTrap,
       "ty1250BPVThresholdAcceptableTrap": ty1250BPVThresholdAcceptableTrap,
       "ty1250LocalUnitLoopbackEnabledTrap": ty1250LocalUnitLoopbackEnabledTrap,
       "ty1250LocalUnitLoopbackDisabledTrap": ty1250LocalUnitLoopbackDisabledTrap,
       "ty1250LocalNetLoopbackEnabledTrap": ty1250LocalNetLoopbackEnabledTrap,
       "ty1250LocalNetLoopbackDisabledTrap": ty1250LocalNetLoopbackDisabledTrap,
       "ty1250SimplexCurrentLoopbackEnabledTrap": ty1250SimplexCurrentLoopbackEnabledTrap,
       "ty1250SimplexCurrentLoopbackDisabledTrap": ty1250SimplexCurrentLoopbackDisabledTrap,
       "ty1250NonLatchingLoopbackEnabledTrap": ty1250NonLatchingLoopbackEnabledTrap,
       "ty1250NonLatchingLoopbackDisabledTrap": ty1250NonLatchingLoopbackDisabledTrap,
       "ty1250V54LoopUpInitiatedTrap": ty1250V54LoopUpInitiatedTrap,
       "ty1250V54LoopDownCompletedTrap": ty1250V54LoopDownCompletedTrap,
       "ty1250V54LoopbackEnabledTrap": ty1250V54LoopbackEnabledTrap,
       "ty1250V54LoopbackDisabledTrap": ty1250V54LoopbackDisabledTrap,
       "ty1250BertInitiatedTrap": ty1250BertInitiatedTrap,
       "ty1250BertCompletedTrap": ty1250BertCompletedTrap,
       "ty1250LocalDteLoopbackEnabledTrap": ty1250LocalDteLoopbackEnabledTrap,
       "ty1250LocalDteLoopbackDisabledTrap": ty1250LocalDteLoopbackDisabledTrap,
       "ty1250LocalUnitLoopbackFailedTrap": ty1250LocalUnitLoopbackFailedTrap,
       "ty1250LocalNetLoopbackFailedTrap": ty1250LocalNetLoopbackFailedTrap,
       "ty1250BertFailedTrap": ty1250BertFailedTrap,
       "ty1250LocalDteLoopbackFailedTrap": ty1250LocalDteLoopbackFailedTrap,
       "ty1250V54LoopbackFailedTrap": ty1250V54LoopbackFailedTrap,
       "ty1250SysTable": ty1250SysTable,
       "ty1250SysType": ty1250SysType,
       "ty1250SysSoftRev": ty1250SysSoftRev,
       "ty1250SysHardRev": ty1250SysHardRev,
       "ty1250SysNumNetInstalled": ty1250SysNumNetInstalled,
       "ty1250SysNumDteInstalled": ty1250SysNumDteInstalled,
       "ty1250SysNumMaintInstalled": ty1250SysNumMaintInstalled,
       "ty1250SysName": ty1250SysName,
       "ty1250CfgAppTable": ty1250CfgAppTable,
       "ty1250CfgAppClockSource": ty1250CfgAppClockSource,
       "ty1250CfgAppCircuitId": ty1250CfgAppCircuitId,
       "ty1250CfgNetTable": ty1250CfgNetTable,
       "ty1250CfgNetGlareType": ty1250CfgNetGlareType,
       "ty1250CfgNetEchoCan": ty1250CfgNetEchoCan,
       "ty1250CfgNetAnsMode": ty1250CfgNetAnsMode,
       "ty1250CfgNetDialTimeout": ty1250CfgNetDialTimeout,
       "ty1250CfgNetNumRedial": ty1250CfgNetNumRedial,
       "ty1250CfgNetRedialDelay": ty1250CfgNetRedialDelay,
       "ty1250CfgNetDefNum2Dial": ty1250CfgNetDefNum2Dial,
       "ty1250CfgNetType": ty1250CfgNetType,
       "ty1250CfgNetBPVThresholding": ty1250CfgNetBPVThresholding,
       "ty1250CfgDteTable": ty1250CfgDteTable,
       "ty1250CfgDteType": ty1250CfgDteType,
       "ty1250CfgDteClockInvert": ty1250CfgDteClockInvert,
       "ty1250CfgDteTiming": ty1250CfgDteTiming,
       "ty1250CfgDialTable": ty1250CfgDialTable,
       "ty1250CfgDialButton": ty1250CfgDialButton,
       "ty1250CfgDialDtr": ty1250CfgDialDtr,
       "ty1250CfgDialRtsDisc": ty1250CfgDialRtsDisc,
       "ty1250CfgDialRi": ty1250CfgDialRi,
       "ty1250CfgMaintTable": ty1250CfgMaintTable,
       "ty1250CfgMaintEntry": ty1250CfgMaintEntry,
       "ty1250CfgMaintIndex": ty1250CfgMaintIndex,
       "ty1250CfgMaintMode": ty1250CfgMaintMode,
       "ty1250CfgMaintBaud": ty1250CfgMaintBaud,
       "ty1250CfgMaintDataBits": ty1250CfgMaintDataBits,
       "ty1250CfgMaintStopBits": ty1250CfgMaintStopBits,
       "ty1250CfgMaintParity": ty1250CfgMaintParity,
       "ty1250CfgMaintFlowCtrl": ty1250CfgMaintFlowCtrl,
       "ty1250CfgSlipTable": ty1250CfgSlipTable,
       "ty1250CfgSlipMyIP": ty1250CfgSlipMyIP,
       "ty1250CfgSlipPeerIP": ty1250CfgSlipPeerIP,
       "ty1250CfgSlipMask": ty1250CfgSlipMask,
       "ty1250CfgSlipMaxMTU": ty1250CfgSlipMaxMTU,
       "ty1250CallTable": ty1250CallTable,
       "ty1250CallStatus": ty1250CallStatus,
       "ty1250CallNumber": ty1250CallNumber,
       "ty1250CallUpTime": ty1250CallUpTime,
       "ty1250CallState": ty1250CallState,
       "ty1250DiagUnitTable": ty1250DiagUnitTable,
       "ty1250DiagUnitLocLoop": ty1250DiagUnitLocLoop,
       "ty1250DiagUnitReset": ty1250DiagUnitReset,
       "ty1250DiagNetTable": ty1250DiagNetTable,
       "ty1250DiagNetLineStatus": ty1250DiagNetLineStatus,
       "ty1250DiagNetLclLpbk": ty1250DiagNetLclLpbk,
       "ty1250DiagNetRmtLpbk": ty1250DiagNetRmtLpbk,
       "ty1250DiagDteTable": ty1250DiagDteTable,
       "ty1250DiagDteSigRTS": ty1250DiagDteSigRTS,
       "ty1250DiagDteSigDTR": ty1250DiagDteSigDTR,
       "ty1250DiagDteLclLpbk": ty1250DiagDteLclLpbk,
       "ty1250DiagDteV54Lpbk": ty1250DiagDteV54Lpbk,
       "ty1250DiagDteBerState": ty1250DiagDteBerState,
       "ty1250DiagDteBerStatus": ty1250DiagDteBerStatus,
       "ty1250DiagDteBerErrors": ty1250DiagDteBerErrors,
       "ty1250DiagDteBerErrSec": ty1250DiagDteBerErrSec,
       "ty1250DiagDteBerTimeElaps": ty1250DiagDteBerTimeElaps,
       "ty1250DiagDteBerResyncs": ty1250DiagDteBerResyncs,
       "ty1250DiagDteRmtV54Lpbk": ty1250DiagDteRmtV54Lpbk,
       "ty1250AlarmType": ty1250AlarmType,
       "ty1250CfgSnmpTable": ty1250CfgSnmpTable,
       "ty1250CfgSnmpManagerIP": ty1250CfgSnmpManagerIP,
       "ty1250StatsDteTable": ty1250StatsDteTable,
       "ty1250StatsDteTxByteCount": ty1250StatsDteTxByteCount,
       "ty1250StatsDteRxByteCount": ty1250StatsDteRxByteCount,
       "ty1250StatsDteClearStats": ty1250StatsDteClearStats,
       "ty1250StatsNetTable": ty1250StatsNetTable,
       "ty1250StatsNetLoopLength": ty1250StatsNetLoopLength,
       "ty1250StatsNetBpvCount": ty1250StatsNetBpvCount,
       "ty1250StatsNetTxByteCount": ty1250StatsNetTxByteCount,
       "ty1250StatsNetRxByteCount": ty1250StatsNetRxByteCount,
       "ty1250StatsNetClearStats": ty1250StatsNetClearStats,
       "ty1250CfgTelnetTable": ty1250CfgTelnetTable,
       "ty1250CfgTelnetEnable": ty1250CfgTelnetEnable,
       "ty1250CfgTelnetAutoLogOut": ty1250CfgTelnetAutoLogOut}
)
