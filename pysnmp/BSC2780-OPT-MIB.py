# SNMP MIB module (BSC2780-OPT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BSC2780-OPT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:49:39 2024
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



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Codex_ObjectIdentity = ObjectIdentity
codex = _Codex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449)
)
_CdxProductSpecific_ObjectIdentity = ObjectIdentity
cdxProductSpecific = _CdxProductSpecific_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2)
)
_Cdx6500_ObjectIdentity = ObjectIdentity
cdx6500 = _Cdx6500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1)
)
_Cdx6500Configuration_ObjectIdentity = ObjectIdentity
cdx6500Configuration = _Cdx6500Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2)
)
_Cdx6500CfgProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500CfgProtocolGroup = _Cdx6500CfgProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1)
)
_Cdx6500PCTPortProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500PCTPortProtocolGroup = _Cdx6500PCTPortProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1)
)
_Cdx6500PPCTBSC2780Table_Object = MibTable
cdx6500PPCTBSC2780Table = _Cdx6500PPCTBSC2780Table_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 11)
)
if mibBuilder.loadTexts:
    cdx6500PPCTBSC2780Table.setStatus("mandatory")
_Cdx6500bsc2780PortConfigEntry_Object = MibTableRow
cdx6500bsc2780PortConfigEntry = _Cdx6500bsc2780PortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 11, 1)
)
cdx6500bsc2780PortConfigEntry.setIndexNames(
    (0, "BSC2780-OPT-MIB", "cdx6500bsc2780PortNumber"),
)
if mibBuilder.loadTexts:
    cdx6500bsc2780PortConfigEntry.setStatus("mandatory")


class _Cdx6500bsc2780PortNumber_Type(Integer32):
    """Custom type cdx6500bsc2780PortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_Cdx6500bsc2780PortNumber_Type.__name__ = "Integer32"
_Cdx6500bsc2780PortNumber_Object = MibTableColumn
cdx6500bsc2780PortNumber = _Cdx6500bsc2780PortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 11, 1, 1),
    _Cdx6500bsc2780PortNumber_Type()
)
cdx6500bsc2780PortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500bsc2780PortNumber.setStatus("mandatory")


class _Cdx6500bsc2780ClockSource_Type(Integer32):
    """Custom type cdx6500bsc2780ClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("ext", 1),
          ("int", 0),
          ("newvalInt", 50))
    )


_Cdx6500bsc2780ClockSource_Type.__name__ = "Integer32"
_Cdx6500bsc2780ClockSource_Object = MibTableColumn
cdx6500bsc2780ClockSource = _Cdx6500bsc2780ClockSource_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 11, 1, 2),
    _Cdx6500bsc2780ClockSource_Type()
)
cdx6500bsc2780ClockSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500bsc2780ClockSource.setStatus("mandatory")


class _Cdx6500bsc2780ClockSpeed_Type(Integer32):
    """Custom type cdx6500bsc2780ClockSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1200, 19200),
    )


_Cdx6500bsc2780ClockSpeed_Type.__name__ = "Integer32"
_Cdx6500bsc2780ClockSpeed_Object = MibTableColumn
cdx6500bsc2780ClockSpeed = _Cdx6500bsc2780ClockSpeed_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 11, 1, 3),
    _Cdx6500bsc2780ClockSpeed_Type()
)
cdx6500bsc2780ClockSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500bsc2780ClockSpeed.setStatus("mandatory")


class _Cdx6500bsc2780Contention_Type(Integer32):
    """Custom type cdx6500bsc2780Contention based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("fdx", 1),
          ("hdx", 0),
          ("newvalHdx", 50))
    )


_Cdx6500bsc2780Contention_Type.__name__ = "Integer32"
_Cdx6500bsc2780Contention_Object = MibTableColumn
cdx6500bsc2780Contention = _Cdx6500bsc2780Contention_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 11, 1, 4),
    _Cdx6500bsc2780Contention_Type()
)
cdx6500bsc2780Contention.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500bsc2780Contention.setStatus("mandatory")


class _Cdx6500bsc2780ErrThreshCount_Type(Integer32):
    """Custom type cdx6500bsc2780ErrThreshCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500bsc2780ErrThreshCount_Type.__name__ = "Integer32"
_Cdx6500bsc2780ErrThreshCount_Object = MibTableColumn
cdx6500bsc2780ErrThreshCount = _Cdx6500bsc2780ErrThreshCount_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 11, 1, 5),
    _Cdx6500bsc2780ErrThreshCount_Type()
)
cdx6500bsc2780ErrThreshCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500bsc2780ErrThreshCount.setStatus("mandatory")


class _Cdx6500bsc2780DisConnOnError_Type(Integer32):
    """Custom type cdx6500bsc2780DisConnOnError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("newvalNo", 50),
          ("no", 0),
          ("yes", 1))
    )


_Cdx6500bsc2780DisConnOnError_Type.__name__ = "Integer32"
_Cdx6500bsc2780DisConnOnError_Object = MibTableColumn
cdx6500bsc2780DisConnOnError = _Cdx6500bsc2780DisConnOnError_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 11, 1, 6),
    _Cdx6500bsc2780DisConnOnError_Type()
)
cdx6500bsc2780DisConnOnError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500bsc2780DisConnOnError.setStatus("mandatory")


class _Cdx6500bsc2780ConnType_Type(Integer32):
    """Custom type cdx6500bsc2780ConnType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              5,
              13,
              14,
              16,
              19,
              50)
        )
    )
    namedValues = NamedValues(
        *(("dimo", 5),
          ("dimoh", 19),
          ("emri", 3),
          ("emrih", 16),
          ("newvalSimp", 50),
          ("rs366", 14),
          ("simp", 0),
          ("v25b", 13))
    )


_Cdx6500bsc2780ConnType_Type.__name__ = "Integer32"
_Cdx6500bsc2780ConnType_Object = MibTableColumn
cdx6500bsc2780ConnType = _Cdx6500bsc2780ConnType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 11, 1, 7),
    _Cdx6500bsc2780ConnType_Type()
)
cdx6500bsc2780ConnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500bsc2780ConnType.setStatus("mandatory")


class _Cdx6500bsc2780InterBuffTimeout_Type(Integer32):
    """Custom type cdx6500bsc2780InterBuffTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500bsc2780InterBuffTimeout_Type.__name__ = "Integer32"
_Cdx6500bsc2780InterBuffTimeout_Object = MibTableColumn
cdx6500bsc2780InterBuffTimeout = _Cdx6500bsc2780InterBuffTimeout_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 11, 1, 8),
    _Cdx6500bsc2780InterBuffTimeout_Type()
)
cdx6500bsc2780InterBuffTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500bsc2780InterBuffTimeout.setStatus("mandatory")


class _Cdx6500bsc2780PortSubAddr_Type(DisplayString):
    """Custom type cdx6500bsc2780PortSubAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_Cdx6500bsc2780PortSubAddr_Type.__name__ = "DisplayString"
_Cdx6500bsc2780PortSubAddr_Object = MibTableColumn
cdx6500bsc2780PortSubAddr = _Cdx6500bsc2780PortSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 11, 1, 9),
    _Cdx6500bsc2780PortSubAddr_Type()
)
cdx6500bsc2780PortSubAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500bsc2780PortSubAddr.setStatus("mandatory")


class _Cdx6500bsc2780ReConnRetry_Type(Integer32):
    """Custom type cdx6500bsc2780ReConnRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cdx6500bsc2780ReConnRetry_Type.__name__ = "Integer32"
_Cdx6500bsc2780ReConnRetry_Object = MibTableColumn
cdx6500bsc2780ReConnRetry = _Cdx6500bsc2780ReConnRetry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 11, 1, 10),
    _Cdx6500bsc2780ReConnRetry_Type()
)
cdx6500bsc2780ReConnRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500bsc2780ReConnRetry.setStatus("mandatory")


class _Cdx6500bsc2780AutocallMnemonic_Type(DisplayString):
    """Custom type cdx6500bsc2780AutocallMnemonic based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Cdx6500bsc2780AutocallMnemonic_Type.__name__ = "DisplayString"
_Cdx6500bsc2780AutocallMnemonic_Object = MibTableColumn
cdx6500bsc2780AutocallMnemonic = _Cdx6500bsc2780AutocallMnemonic_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 11, 1, 11),
    _Cdx6500bsc2780AutocallMnemonic_Type()
)
cdx6500bsc2780AutocallMnemonic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500bsc2780AutocallMnemonic.setStatus("mandatory")


class _Cdx6500bsc2780RestrictConnDest_Type(DisplayString):
    """Custom type cdx6500bsc2780RestrictConnDest based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Cdx6500bsc2780RestrictConnDest_Type.__name__ = "DisplayString"
_Cdx6500bsc2780RestrictConnDest_Object = MibTableColumn
cdx6500bsc2780RestrictConnDest = _Cdx6500bsc2780RestrictConnDest_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 11, 1, 12),
    _Cdx6500bsc2780RestrictConnDest_Type()
)
cdx6500bsc2780RestrictConnDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500bsc2780RestrictConnDest.setStatus("mandatory")


class _Cdx6500bsc2780BillRec_Type(Integer32):
    """Custom type cdx6500bsc2780BillRec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("newvalOff", 50),
          ("off", 0),
          ("on", 1))
    )


_Cdx6500bsc2780BillRec_Type.__name__ = "Integer32"
_Cdx6500bsc2780BillRec_Object = MibTableColumn
cdx6500bsc2780BillRec = _Cdx6500bsc2780BillRec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 11, 1, 13),
    _Cdx6500bsc2780BillRec_Type()
)
cdx6500bsc2780BillRec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500bsc2780BillRec.setStatus("mandatory")


class _Cdx6500bsc2780DSRfollowSVC_Type(Integer32):
    """Custom type cdx6500bsc2780DSRfollowSVC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("newvalNo", 50),
          ("no", 0),
          ("yes", 1))
    )


_Cdx6500bsc2780DSRfollowSVC_Type.__name__ = "Integer32"
_Cdx6500bsc2780DSRfollowSVC_Object = MibTableColumn
cdx6500bsc2780DSRfollowSVC = _Cdx6500bsc2780DSRfollowSVC_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 11, 1, 14),
    _Cdx6500bsc2780DSRfollowSVC_Type()
)
cdx6500bsc2780DSRfollowSVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500bsc2780DSRfollowSVC.setStatus("mandatory")


class _Cdx6500bsc2780DSRholdTime_Type(Integer32):
    """Custom type cdx6500bsc2780DSRholdTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 3000),
    )


_Cdx6500bsc2780DSRholdTime_Type.__name__ = "Integer32"
_Cdx6500bsc2780DSRholdTime_Object = MibTableColumn
cdx6500bsc2780DSRholdTime = _Cdx6500bsc2780DSRholdTime_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 11, 1, 15),
    _Cdx6500bsc2780DSRholdTime_Type()
)
cdx6500bsc2780DSRholdTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500bsc2780DSRholdTime.setStatus("mandatory")


class _Cdx6500bsc2780PortOption_Type(Integer32):
    """Custom type cdx6500bsc2780PortOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("deprecatedObj", 1)
    )


_Cdx6500bsc2780PortOption_Type.__name__ = "Integer32"
_Cdx6500bsc2780PortOption_Object = MibTableColumn
cdx6500bsc2780PortOption = _Cdx6500bsc2780PortOption_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 11, 1, 16),
    _Cdx6500bsc2780PortOption_Type()
)
cdx6500bsc2780PortOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500bsc2780PortOption.setStatus("deprecated")


class _Cdx6500bsc2780TrafficPriority_Type(Integer32):
    """Custom type cdx6500bsc2780TrafficPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              50)
        )
    )
    namedValues = NamedValues(
        *(("hiPriority", 2),
          ("lowPriority", 0),
          ("medPriority", 1),
          ("newvalLowPriority", 50),
          ("xpPriority", 3))
    )


_Cdx6500bsc2780TrafficPriority_Type.__name__ = "Integer32"
_Cdx6500bsc2780TrafficPriority_Object = MibTableColumn
cdx6500bsc2780TrafficPriority = _Cdx6500bsc2780TrafficPriority_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 11, 1, 17),
    _Cdx6500bsc2780TrafficPriority_Type()
)
cdx6500bsc2780TrafficPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500bsc2780TrafficPriority.setStatus("optional")


class _Cdx6500bsc2780PortOptString_Type(DisplayString):
    """Custom type cdx6500bsc2780PortOptString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 32),
    )


_Cdx6500bsc2780PortOptString_Type.__name__ = "DisplayString"
_Cdx6500bsc2780PortOptString_Object = MibTableColumn
cdx6500bsc2780PortOptString = _Cdx6500bsc2780PortOptString_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 11, 1, 18),
    _Cdx6500bsc2780PortOptString_Type()
)
cdx6500bsc2780PortOptString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500bsc2780PortOptString.setStatus("mandatory")


class _Cdx6500bsc2780IdleDiscTimer_Type(Integer32):
    """Custom type cdx6500bsc2780IdleDiscTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_Cdx6500bsc2780IdleDiscTimer_Type.__name__ = "Integer32"
_Cdx6500bsc2780IdleDiscTimer_Object = MibTableColumn
cdx6500bsc2780IdleDiscTimer = _Cdx6500bsc2780IdleDiscTimer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 11, 1, 19),
    _Cdx6500bsc2780IdleDiscTimer_Type()
)
cdx6500bsc2780IdleDiscTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500bsc2780IdleDiscTimer.setStatus("mandatory")


class _Cdx6500bsc2780ElectricalInterfaceType_Type(Integer32):
    """Custom type cdx6500bsc2780ElectricalInterfaceType based on Integer32"""
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
        *(("none", 5),
          ("v24", 1),
          ("v35", 2),
          ("v36", 3),
          ("x21", 4))
    )


_Cdx6500bsc2780ElectricalInterfaceType_Type.__name__ = "Integer32"
_Cdx6500bsc2780ElectricalInterfaceType_Object = MibTableColumn
cdx6500bsc2780ElectricalInterfaceType = _Cdx6500bsc2780ElectricalInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 11, 1, 20),
    _Cdx6500bsc2780ElectricalInterfaceType_Type()
)
cdx6500bsc2780ElectricalInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500bsc2780ElectricalInterfaceType.setStatus("mandatory")


class _Cdx6500bsc2780V24ElectricalInterfaceOption_Type(Integer32):
    """Custom type cdx6500bsc2780V24ElectricalInterfaceOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ri", 1),
          ("tm", 2))
    )


_Cdx6500bsc2780V24ElectricalInterfaceOption_Type.__name__ = "Integer32"
_Cdx6500bsc2780V24ElectricalInterfaceOption_Object = MibTableColumn
cdx6500bsc2780V24ElectricalInterfaceOption = _Cdx6500bsc2780V24ElectricalInterfaceOption_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 11, 1, 21),
    _Cdx6500bsc2780V24ElectricalInterfaceOption_Type()
)
cdx6500bsc2780V24ElectricalInterfaceOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500bsc2780V24ElectricalInterfaceOption.setStatus("mandatory")


class _Cdx6500bsc2780HighSpeedElectricalInterfaceOption_Type(Integer32):
    """Custom type cdx6500bsc2780HighSpeedElectricalInterfaceOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("xover", 2))
    )


_Cdx6500bsc2780HighSpeedElectricalInterfaceOption_Type.__name__ = "Integer32"
_Cdx6500bsc2780HighSpeedElectricalInterfaceOption_Object = MibTableColumn
cdx6500bsc2780HighSpeedElectricalInterfaceOption = _Cdx6500bsc2780HighSpeedElectricalInterfaceOption_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 11, 1, 22),
    _Cdx6500bsc2780HighSpeedElectricalInterfaceOption_Type()
)
cdx6500bsc2780HighSpeedElectricalInterfaceOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500bsc2780HighSpeedElectricalInterfaceOption.setStatus("mandatory")


class _Cdx6500bsc2780RemoteType_Type(Integer32):
    """Custom type cdx6500bsc2780RemoteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("snaint", 2),
          ("t2780", 1))
    )


_Cdx6500bsc2780RemoteType_Type.__name__ = "Integer32"
_Cdx6500bsc2780RemoteType_Object = MibTableColumn
cdx6500bsc2780RemoteType = _Cdx6500bsc2780RemoteType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 11, 1, 23),
    _Cdx6500bsc2780RemoteType_Type()
)
cdx6500bsc2780RemoteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500bsc2780RemoteType.setStatus("mandatory")
_Cdx6500Statistics_ObjectIdentity = ObjectIdentity
cdx6500Statistics = _Cdx6500Statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3)
)
_Cdx6500StatProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500StatProtocolGroup = _Cdx6500StatProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1)
)
_Cdx6500PSTPortProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500PSTPortProtocolGroup = _Cdx6500PSTPortProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1)
)
_Cdx6500PPSTBSC2780Table_Object = MibTable
cdx6500PPSTBSC2780Table = _Cdx6500PPSTBSC2780Table_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 11)
)
if mibBuilder.loadTexts:
    cdx6500PPSTBSC2780Table.setStatus("mandatory")
_Cdx6500bsc2780PortStatEntry_Object = MibTableRow
cdx6500bsc2780PortStatEntry = _Cdx6500bsc2780PortStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 11, 1)
)
cdx6500bsc2780PortStatEntry.setIndexNames(
    (0, "BSC2780-OPT-MIB", "cdx6500bsc2780StatPortNumber"),
)
if mibBuilder.loadTexts:
    cdx6500bsc2780PortStatEntry.setStatus("mandatory")


class _Cdx6500bsc2780StatPortNumber_Type(Integer32):
    """Custom type cdx6500bsc2780StatPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_Cdx6500bsc2780StatPortNumber_Type.__name__ = "Integer32"
_Cdx6500bsc2780StatPortNumber_Object = MibTableColumn
cdx6500bsc2780StatPortNumber = _Cdx6500bsc2780StatPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 11, 1, 1),
    _Cdx6500bsc2780StatPortNumber_Type()
)
cdx6500bsc2780StatPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500bsc2780StatPortNumber.setStatus("mandatory")


class _Cdx6500bsc2780PortStatus_Type(Integer32):
    """Custom type cdx6500bsc2780PortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              50)
        )
    )
    namedValues = NamedValues(
        *(("busyOut", 2),
          ("disabled", 0),
          ("down", 4),
          ("enabled", 1),
          ("newvalDisabled", 50),
          ("up", 3))
    )


_Cdx6500bsc2780PortStatus_Type.__name__ = "Integer32"
_Cdx6500bsc2780PortStatus_Object = MibTableColumn
cdx6500bsc2780PortStatus = _Cdx6500bsc2780PortStatus_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 11, 1, 2),
    _Cdx6500bsc2780PortStatus_Type()
)
cdx6500bsc2780PortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500bsc2780PortStatus.setStatus("mandatory")


class _Cdx6500bsc2780PortState_Type(DisplayString):
    """Custom type cdx6500bsc2780PortState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 10),
    )


_Cdx6500bsc2780PortState_Type.__name__ = "DisplayString"
_Cdx6500bsc2780PortState_Object = MibTableColumn
cdx6500bsc2780PortState = _Cdx6500bsc2780PortState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 11, 1, 3),
    _Cdx6500bsc2780PortState_Type()
)
cdx6500bsc2780PortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500bsc2780PortState.setStatus("mandatory")
_Cdx6500bsc2780PortSpeed_Type = Integer32
_Cdx6500bsc2780PortSpeed_Object = MibTableColumn
cdx6500bsc2780PortSpeed = _Cdx6500bsc2780PortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 11, 1, 4),
    _Cdx6500bsc2780PortSpeed_Type()
)
cdx6500bsc2780PortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500bsc2780PortSpeed.setStatus("mandatory")


class _Cdx6500bsc2780PortUtilIn_Type(Integer32):
    """Custom type cdx6500bsc2780PortUtilIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Cdx6500bsc2780PortUtilIn_Type.__name__ = "Integer32"
_Cdx6500bsc2780PortUtilIn_Object = MibTableColumn
cdx6500bsc2780PortUtilIn = _Cdx6500bsc2780PortUtilIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 11, 1, 5),
    _Cdx6500bsc2780PortUtilIn_Type()
)
cdx6500bsc2780PortUtilIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500bsc2780PortUtilIn.setStatus("mandatory")


class _Cdx6500bsc2780PortUtilOut_Type(Integer32):
    """Custom type cdx6500bsc2780PortUtilOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Cdx6500bsc2780PortUtilOut_Type.__name__ = "Integer32"
_Cdx6500bsc2780PortUtilOut_Object = MibTableColumn
cdx6500bsc2780PortUtilOut = _Cdx6500bsc2780PortUtilOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 11, 1, 6),
    _Cdx6500bsc2780PortUtilOut_Type()
)
cdx6500bsc2780PortUtilOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500bsc2780PortUtilOut.setStatus("mandatory")
_Cdx6500bsc2780InMsgs_Type = Counter32
_Cdx6500bsc2780InMsgs_Object = MibTableColumn
cdx6500bsc2780InMsgs = _Cdx6500bsc2780InMsgs_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 11, 1, 7),
    _Cdx6500bsc2780InMsgs_Type()
)
cdx6500bsc2780InMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500bsc2780InMsgs.setStatus("mandatory")
_Cdx6500bsc2780OutMsgs_Type = Counter32
_Cdx6500bsc2780OutMsgs_Object = MibTableColumn
cdx6500bsc2780OutMsgs = _Cdx6500bsc2780OutMsgs_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 11, 1, 8),
    _Cdx6500bsc2780OutMsgs_Type()
)
cdx6500bsc2780OutMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500bsc2780OutMsgs.setStatus("mandatory")
_Cdx6500bsc2780InChars_Type = Counter32
_Cdx6500bsc2780InChars_Object = MibTableColumn
cdx6500bsc2780InChars = _Cdx6500bsc2780InChars_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 11, 1, 9),
    _Cdx6500bsc2780InChars_Type()
)
cdx6500bsc2780InChars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500bsc2780InChars.setStatus("mandatory")
_Cdx6500bsc2780OutChars_Type = Counter32
_Cdx6500bsc2780OutChars_Object = MibTableColumn
cdx6500bsc2780OutChars = _Cdx6500bsc2780OutChars_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 11, 1, 10),
    _Cdx6500bsc2780OutChars_Type()
)
cdx6500bsc2780OutChars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500bsc2780OutChars.setStatus("mandatory")


class _Cdx6500bsc2780CharRateIn_Type(Integer32):
    """Custom type cdx6500bsc2780CharRateIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Cdx6500bsc2780CharRateIn_Type.__name__ = "Integer32"
_Cdx6500bsc2780CharRateIn_Object = MibTableColumn
cdx6500bsc2780CharRateIn = _Cdx6500bsc2780CharRateIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 11, 1, 11),
    _Cdx6500bsc2780CharRateIn_Type()
)
cdx6500bsc2780CharRateIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500bsc2780CharRateIn.setStatus("mandatory")


class _Cdx6500bsc2780CharRateOut_Type(Integer32):
    """Custom type cdx6500bsc2780CharRateOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Cdx6500bsc2780CharRateOut_Type.__name__ = "Integer32"
_Cdx6500bsc2780CharRateOut_Object = MibTableColumn
cdx6500bsc2780CharRateOut = _Cdx6500bsc2780CharRateOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 11, 1, 12),
    _Cdx6500bsc2780CharRateOut_Type()
)
cdx6500bsc2780CharRateOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500bsc2780CharRateOut.setStatus("mandatory")
_Cdx6500bsc2780CrcBccErrs_Type = Counter32
_Cdx6500bsc2780CrcBccErrs_Object = MibTableColumn
cdx6500bsc2780CrcBccErrs = _Cdx6500bsc2780CrcBccErrs_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 11, 1, 13),
    _Cdx6500bsc2780CrcBccErrs_Type()
)
cdx6500bsc2780CrcBccErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500bsc2780CrcBccErrs.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BSC2780-OPT-MIB",
    **{"DisplayString": DisplayString,
       "codex": codex,
       "cdxProductSpecific": cdxProductSpecific,
       "cdx6500": cdx6500,
       "cdx6500Configuration": cdx6500Configuration,
       "cdx6500CfgProtocolGroup": cdx6500CfgProtocolGroup,
       "cdx6500PCTPortProtocolGroup": cdx6500PCTPortProtocolGroup,
       "cdx6500PPCTBSC2780Table": cdx6500PPCTBSC2780Table,
       "cdx6500bsc2780PortConfigEntry": cdx6500bsc2780PortConfigEntry,
       "cdx6500bsc2780PortNumber": cdx6500bsc2780PortNumber,
       "cdx6500bsc2780ClockSource": cdx6500bsc2780ClockSource,
       "cdx6500bsc2780ClockSpeed": cdx6500bsc2780ClockSpeed,
       "cdx6500bsc2780Contention": cdx6500bsc2780Contention,
       "cdx6500bsc2780ErrThreshCount": cdx6500bsc2780ErrThreshCount,
       "cdx6500bsc2780DisConnOnError": cdx6500bsc2780DisConnOnError,
       "cdx6500bsc2780ConnType": cdx6500bsc2780ConnType,
       "cdx6500bsc2780InterBuffTimeout": cdx6500bsc2780InterBuffTimeout,
       "cdx6500bsc2780PortSubAddr": cdx6500bsc2780PortSubAddr,
       "cdx6500bsc2780ReConnRetry": cdx6500bsc2780ReConnRetry,
       "cdx6500bsc2780AutocallMnemonic": cdx6500bsc2780AutocallMnemonic,
       "cdx6500bsc2780RestrictConnDest": cdx6500bsc2780RestrictConnDest,
       "cdx6500bsc2780BillRec": cdx6500bsc2780BillRec,
       "cdx6500bsc2780DSRfollowSVC": cdx6500bsc2780DSRfollowSVC,
       "cdx6500bsc2780DSRholdTime": cdx6500bsc2780DSRholdTime,
       "cdx6500bsc2780PortOption": cdx6500bsc2780PortOption,
       "cdx6500bsc2780TrafficPriority": cdx6500bsc2780TrafficPriority,
       "cdx6500bsc2780PortOptString": cdx6500bsc2780PortOptString,
       "cdx6500bsc2780IdleDiscTimer": cdx6500bsc2780IdleDiscTimer,
       "cdx6500bsc2780ElectricalInterfaceType": cdx6500bsc2780ElectricalInterfaceType,
       "cdx6500bsc2780V24ElectricalInterfaceOption": cdx6500bsc2780V24ElectricalInterfaceOption,
       "cdx6500bsc2780HighSpeedElectricalInterfaceOption": cdx6500bsc2780HighSpeedElectricalInterfaceOption,
       "cdx6500bsc2780RemoteType": cdx6500bsc2780RemoteType,
       "cdx6500Statistics": cdx6500Statistics,
       "cdx6500StatProtocolGroup": cdx6500StatProtocolGroup,
       "cdx6500PSTPortProtocolGroup": cdx6500PSTPortProtocolGroup,
       "cdx6500PPSTBSC2780Table": cdx6500PPSTBSC2780Table,
       "cdx6500bsc2780PortStatEntry": cdx6500bsc2780PortStatEntry,
       "cdx6500bsc2780StatPortNumber": cdx6500bsc2780StatPortNumber,
       "cdx6500bsc2780PortStatus": cdx6500bsc2780PortStatus,
       "cdx6500bsc2780PortState": cdx6500bsc2780PortState,
       "cdx6500bsc2780PortSpeed": cdx6500bsc2780PortSpeed,
       "cdx6500bsc2780PortUtilIn": cdx6500bsc2780PortUtilIn,
       "cdx6500bsc2780PortUtilOut": cdx6500bsc2780PortUtilOut,
       "cdx6500bsc2780InMsgs": cdx6500bsc2780InMsgs,
       "cdx6500bsc2780OutMsgs": cdx6500bsc2780OutMsgs,
       "cdx6500bsc2780InChars": cdx6500bsc2780InChars,
       "cdx6500bsc2780OutChars": cdx6500bsc2780OutChars,
       "cdx6500bsc2780CharRateIn": cdx6500bsc2780CharRateIn,
       "cdx6500bsc2780CharRateOut": cdx6500bsc2780CharRateOut,
       "cdx6500bsc2780CrcBccErrs": cdx6500bsc2780CrcBccErrs}
)
