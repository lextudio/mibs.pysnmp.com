# SNMP MIB module (BSC3270-OPT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BSC3270-OPT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:49:40 2024
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
_Cdx6500PPCTBSC3270PortTable_Object = MibTable
cdx6500PPCTBSC3270PortTable = _Cdx6500PPCTBSC3270PortTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 10)
)
if mibBuilder.loadTexts:
    cdx6500PPCTBSC3270PortTable.setStatus("mandatory")
_Cdx6500PPCTBSC3270PortEntry_Object = MibTableRow
cdx6500PPCTBSC3270PortEntry = _Cdx6500PPCTBSC3270PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 10, 1)
)
cdx6500PPCTBSC3270PortEntry.setIndexNames(
    (0, "BSC3270-OPT-MIB", "cdx6500BSC3270PortNumber"),
)
if mibBuilder.loadTexts:
    cdx6500PPCTBSC3270PortEntry.setStatus("mandatory")


class _Cdx6500BSC3270PortNumber_Type(Integer32):
    """Custom type cdx6500BSC3270PortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_Cdx6500BSC3270PortNumber_Type.__name__ = "Integer32"
_Cdx6500BSC3270PortNumber_Object = MibTableColumn
cdx6500BSC3270PortNumber = _Cdx6500BSC3270PortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 10, 1, 1),
    _Cdx6500BSC3270PortNumber_Type()
)
cdx6500BSC3270PortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSC3270PortNumber.setStatus("mandatory")


class _Cdx6500BSC3270PADType_Type(Integer32):
    """Custom type cdx6500BSC3270PADType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("hpad", 1),
          ("newvalTpad", 50),
          ("tpad", 0))
    )


_Cdx6500BSC3270PADType_Type.__name__ = "Integer32"
_Cdx6500BSC3270PADType_Object = MibTableColumn
cdx6500BSC3270PADType = _Cdx6500BSC3270PADType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 10, 1, 2),
    _Cdx6500BSC3270PADType_Type()
)
cdx6500BSC3270PADType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSC3270PADType.setStatus("mandatory")


class _Cdx6500BSC3270ClockSource_Type(Integer32):
    """Custom type cdx6500BSC3270ClockSource based on Integer32"""
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


_Cdx6500BSC3270ClockSource_Type.__name__ = "Integer32"
_Cdx6500BSC3270ClockSource_Object = MibTableColumn
cdx6500BSC3270ClockSource = _Cdx6500BSC3270ClockSource_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 10, 1, 3),
    _Cdx6500BSC3270ClockSource_Type()
)
cdx6500BSC3270ClockSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSC3270ClockSource.setStatus("mandatory")


class _Cdx6500BSC3270ClockSpeed_Type(Integer32):
    """Custom type cdx6500BSC3270ClockSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1200, 19200),
    )


_Cdx6500BSC3270ClockSpeed_Type.__name__ = "Integer32"
_Cdx6500BSC3270ClockSpeed_Object = MibTableColumn
cdx6500BSC3270ClockSpeed = _Cdx6500BSC3270ClockSpeed_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 10, 1, 4),
    _Cdx6500BSC3270ClockSpeed_Type()
)
cdx6500BSC3270ClockSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSC3270ClockSpeed.setStatus("mandatory")


class _Cdx6500BSC3270Contention_Type(Integer32):
    """Custom type cdx6500BSC3270Contention based on Integer32"""
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


_Cdx6500BSC3270Contention_Type.__name__ = "Integer32"
_Cdx6500BSC3270Contention_Object = MibTableColumn
cdx6500BSC3270Contention = _Cdx6500BSC3270Contention_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 10, 1, 5),
    _Cdx6500BSC3270Contention_Type()
)
cdx6500BSC3270Contention.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSC3270Contention.setStatus("mandatory")


class _Cdx6500BSC3270NumDevices_Type(Integer32):
    """Custom type cdx6500BSC3270NumDevices based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Cdx6500BSC3270NumDevices_Type.__name__ = "Integer32"
_Cdx6500BSC3270NumDevices_Object = MibTableColumn
cdx6500BSC3270NumDevices = _Cdx6500BSC3270NumDevices_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 10, 1, 6),
    _Cdx6500BSC3270NumDevices_Type()
)
cdx6500BSC3270NumDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSC3270NumDevices.setStatus("mandatory")


class _Cdx6500BSC3270ServTimer_Type(Integer32):
    """Custom type cdx6500BSC3270ServTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_Cdx6500BSC3270ServTimer_Type.__name__ = "Integer32"
_Cdx6500BSC3270ServTimer_Object = MibTableColumn
cdx6500BSC3270ServTimer = _Cdx6500BSC3270ServTimer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 10, 1, 7),
    _Cdx6500BSC3270ServTimer_Type()
)
cdx6500BSC3270ServTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSC3270ServTimer.setStatus("mandatory")


class _Cdx6500BSC3270ErrThreshCount_Type(Integer32):
    """Custom type cdx6500BSC3270ErrThreshCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500BSC3270ErrThreshCount_Type.__name__ = "Integer32"
_Cdx6500BSC3270ErrThreshCount_Object = MibTableColumn
cdx6500BSC3270ErrThreshCount = _Cdx6500BSC3270ErrThreshCount_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 10, 1, 8),
    _Cdx6500BSC3270ErrThreshCount_Type()
)
cdx6500BSC3270ErrThreshCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSC3270ErrThreshCount.setStatus("mandatory")


class _Cdx6500BSC3270ResponseTimeout_Type(Integer32):
    """Custom type cdx6500BSC3270ResponseTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500BSC3270ResponseTimeout_Type.__name__ = "Integer32"
_Cdx6500BSC3270ResponseTimeout_Object = MibTableColumn
cdx6500BSC3270ResponseTimeout = _Cdx6500BSC3270ResponseTimeout_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 10, 1, 9),
    _Cdx6500BSC3270ResponseTimeout_Type()
)
cdx6500BSC3270ResponseTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSC3270ResponseTimeout.setStatus("mandatory")


class _Cdx6500BSC3270HostPADTimeout_Type(Integer32):
    """Custom type cdx6500BSC3270HostPADTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500BSC3270HostPADTimeout_Type.__name__ = "Integer32"
_Cdx6500BSC3270HostPADTimeout_Object = MibTableColumn
cdx6500BSC3270HostPADTimeout = _Cdx6500BSC3270HostPADTimeout_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 10, 1, 10),
    _Cdx6500BSC3270HostPADTimeout_Type()
)
cdx6500BSC3270HostPADTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSC3270HostPADTimeout.setStatus("mandatory")


class _Cdx6500BSC3270InterBuffTimeout_Type(Integer32):
    """Custom type cdx6500BSC3270InterBuffTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500BSC3270InterBuffTimeout_Type.__name__ = "Integer32"
_Cdx6500BSC3270InterBuffTimeout_Object = MibTableColumn
cdx6500BSC3270InterBuffTimeout = _Cdx6500BSC3270InterBuffTimeout_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 10, 1, 11),
    _Cdx6500BSC3270InterBuffTimeout_Type()
)
cdx6500BSC3270InterBuffTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSC3270InterBuffTimeout.setStatus("mandatory")


class _Cdx6500BSC3270IdleDevTimeout_Type(Integer32):
    """Custom type cdx6500BSC3270IdleDevTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cdx6500BSC3270IdleDevTimeout_Type.__name__ = "Integer32"
_Cdx6500BSC3270IdleDevTimeout_Object = MibTableColumn
cdx6500BSC3270IdleDevTimeout = _Cdx6500BSC3270IdleDevTimeout_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 10, 1, 12),
    _Cdx6500BSC3270IdleDevTimeout_Type()
)
cdx6500BSC3270IdleDevTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSC3270IdleDevTimeout.setStatus("mandatory")


class _Cdx6500BSC3270PrintDisconTimer_Type(Integer32):
    """Custom type cdx6500BSC3270PrintDisconTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cdx6500BSC3270PrintDisconTimer_Type.__name__ = "Integer32"
_Cdx6500BSC3270PrintDisconTimer_Object = MibTableColumn
cdx6500BSC3270PrintDisconTimer = _Cdx6500BSC3270PrintDisconTimer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 10, 1, 13),
    _Cdx6500BSC3270PrintDisconTimer_Type()
)
cdx6500BSC3270PrintDisconTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSC3270PrintDisconTimer.setStatus("mandatory")


class _Cdx6500BSC3270SignonKey_Type(Integer32):
    """Custom type cdx6500BSC3270SignonKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(74,
              75,
              76,
              122,
              123,
              124,
              193,
              194,
              195,
              196,
              197,
              198,
              199,
              200,
              201,
              241,
              242,
              243,
              244,
              245,
              246,
              247,
              248,
              249)
        )
    )
    namedValues = NamedValues(
        *(("pf1", 241),
          ("pf10", 122),
          ("pf11", 123),
          ("pf12", 124),
          ("pf13", 193),
          ("pf14", 194),
          ("pf15", 195),
          ("pf16", 196),
          ("pf17", 197),
          ("pf18", 198),
          ("pf19", 199),
          ("pf2", 242),
          ("pf20", 200),
          ("pf21", 201),
          ("pf22", 74),
          ("pf23", 75),
          ("pf24", 76),
          ("pf3", 243),
          ("pf4", 244),
          ("pf5", 245),
          ("pf6", 246),
          ("pf7", 247),
          ("pf8", 248),
          ("pf9", 249))
    )


_Cdx6500BSC3270SignonKey_Type.__name__ = "Integer32"
_Cdx6500BSC3270SignonKey_Object = MibTableColumn
cdx6500BSC3270SignonKey = _Cdx6500BSC3270SignonKey_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 10, 1, 14),
    _Cdx6500BSC3270SignonKey_Type()
)
cdx6500BSC3270SignonKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSC3270SignonKey.setStatus("mandatory")


class _Cdx6500BSC3270DiscKey_Type(Integer32):
    """Custom type cdx6500BSC3270DiscKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(74,
              75,
              76,
              122,
              123,
              124,
              193,
              194,
              195,
              196,
              197,
              198,
              199,
              200,
              201,
              241,
              242,
              243,
              244,
              245,
              246,
              247,
              248,
              249)
        )
    )
    namedValues = NamedValues(
        *(("pf1", 241),
          ("pf10", 122),
          ("pf11", 123),
          ("pf12", 124),
          ("pf13", 193),
          ("pf14", 194),
          ("pf15", 195),
          ("pf16", 196),
          ("pf17", 197),
          ("pf18", 198),
          ("pf19", 199),
          ("pf2", 242),
          ("pf20", 200),
          ("pf21", 201),
          ("pf22", 74),
          ("pf23", 75),
          ("pf24", 76),
          ("pf3", 243),
          ("pf4", 244),
          ("pf5", 245),
          ("pf6", 246),
          ("pf7", 247),
          ("pf8", 248),
          ("pf9", 249))
    )


_Cdx6500BSC3270DiscKey_Type.__name__ = "Integer32"
_Cdx6500BSC3270DiscKey_Object = MibTableColumn
cdx6500BSC3270DiscKey = _Cdx6500BSC3270DiscKey_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 10, 1, 15),
    _Cdx6500BSC3270DiscKey_Type()
)
cdx6500BSC3270DiscKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSC3270DiscKey.setStatus("mandatory")


class _Cdx6500BSC3270CharSet_Type(Integer32):
    """Custom type cdx6500BSC3270CharSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 0),
          ("ebcdic", 1),
          ("newvalAscii", 50))
    )


_Cdx6500BSC3270CharSet_Type.__name__ = "Integer32"
_Cdx6500BSC3270CharSet_Object = MibTableColumn
cdx6500BSC3270CharSet = _Cdx6500BSC3270CharSet_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 10, 1, 16),
    _Cdx6500BSC3270CharSet_Type()
)
cdx6500BSC3270CharSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSC3270CharSet.setStatus("mandatory")


class _Cdx6500BSC3270PortSubAddr_Type(DisplayString):
    """Custom type cdx6500BSC3270PortSubAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_Cdx6500BSC3270PortSubAddr_Type.__name__ = "DisplayString"
_Cdx6500BSC3270PortSubAddr_Object = MibTableColumn
cdx6500BSC3270PortSubAddr = _Cdx6500BSC3270PortSubAddr_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 10, 1, 17),
    _Cdx6500BSC3270PortSubAddr_Type()
)
cdx6500BSC3270PortSubAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSC3270PortSubAddr.setStatus("mandatory")


class _Cdx6500BSC3270PortOptions_Type(DisplayString):
    """Custom type cdx6500BSC3270PortOptions based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 16),
    )


_Cdx6500BSC3270PortOptions_Type.__name__ = "DisplayString"
_Cdx6500BSC3270PortOptions_Object = MibTableColumn
cdx6500BSC3270PortOptions = _Cdx6500BSC3270PortOptions_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 10, 1, 18),
    _Cdx6500BSC3270PortOptions_Type()
)
cdx6500BSC3270PortOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSC3270PortOptions.setStatus("mandatory")


class _Cdx6500BSC3270RestrictConnDest_Type(DisplayString):
    """Custom type cdx6500BSC3270RestrictConnDest based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2),
    )


_Cdx6500BSC3270RestrictConnDest_Type.__name__ = "DisplayString"
_Cdx6500BSC3270RestrictConnDest_Object = MibTableColumn
cdx6500BSC3270RestrictConnDest = _Cdx6500BSC3270RestrictConnDest_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 10, 1, 19),
    _Cdx6500BSC3270RestrictConnDest_Type()
)
cdx6500BSC3270RestrictConnDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSC3270RestrictConnDest.setStatus("mandatory")


class _Cdx6500bsc3270ElectricalInterfaceType_Type(Integer32):
    """Custom type cdx6500bsc3270ElectricalInterfaceType based on Integer32"""
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


_Cdx6500bsc3270ElectricalInterfaceType_Type.__name__ = "Integer32"
_Cdx6500bsc3270ElectricalInterfaceType_Object = MibScalar
cdx6500bsc3270ElectricalInterfaceType = _Cdx6500bsc3270ElectricalInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 10, 1, 20),
    _Cdx6500bsc3270ElectricalInterfaceType_Type()
)
cdx6500bsc3270ElectricalInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500bsc3270ElectricalInterfaceType.setStatus("mandatory")


class _Cdx6500bsc3270V24ElectricalInterfaceOption_Type(Integer32):
    """Custom type cdx6500bsc3270V24ElectricalInterfaceOption based on Integer32"""
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


_Cdx6500bsc3270V24ElectricalInterfaceOption_Type.__name__ = "Integer32"
_Cdx6500bsc3270V24ElectricalInterfaceOption_Object = MibScalar
cdx6500bsc3270V24ElectricalInterfaceOption = _Cdx6500bsc3270V24ElectricalInterfaceOption_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 10, 1, 21),
    _Cdx6500bsc3270V24ElectricalInterfaceOption_Type()
)
cdx6500bsc3270V24ElectricalInterfaceOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500bsc3270V24ElectricalInterfaceOption.setStatus("mandatory")


class _Cdx6500bsc3270HighSpeedElectricalInterfaceOption_Type(Integer32):
    """Custom type cdx6500bsc3270HighSpeedElectricalInterfaceOption based on Integer32"""
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


_Cdx6500bsc3270HighSpeedElectricalInterfaceOption_Type.__name__ = "Integer32"
_Cdx6500bsc3270HighSpeedElectricalInterfaceOption_Object = MibScalar
cdx6500bsc3270HighSpeedElectricalInterfaceOption = _Cdx6500bsc3270HighSpeedElectricalInterfaceOption_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 10, 1, 22),
    _Cdx6500bsc3270HighSpeedElectricalInterfaceOption_Type()
)
cdx6500bsc3270HighSpeedElectricalInterfaceOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500bsc3270HighSpeedElectricalInterfaceOption.setStatus("mandatory")
_Cdx6500PCTBSC3270DeviceGroup_ObjectIdentity = ObjectIdentity
cdx6500PCTBSC3270DeviceGroup = _Cdx6500PCTBSC3270DeviceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 4)
)
_Cdx6500PBCTBSC3270DevTable_Object = MibTable
cdx6500PBCTBSC3270DevTable = _Cdx6500PBCTBSC3270DevTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cdx6500PBCTBSC3270DevTable.setStatus("mandatory")
_Cdx6500PBCTBSC3270DevEntry_Object = MibTableRow
cdx6500PBCTBSC3270DevEntry = _Cdx6500PBCTBSC3270DevEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 4, 1, 1)
)
cdx6500PBCTBSC3270DevEntry.setIndexNames(
    (0, "BSC3270-OPT-MIB", "cdx6500BSC3270DevPortNumber"),
    (0, "BSC3270-OPT-MIB", "cdx6500BSC3270DevEntry"),
)
if mibBuilder.loadTexts:
    cdx6500PBCTBSC3270DevEntry.setStatus("mandatory")


class _Cdx6500BSC3270DevPortNumber_Type(Integer32):
    """Custom type cdx6500BSC3270DevPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_Cdx6500BSC3270DevPortNumber_Type.__name__ = "Integer32"
_Cdx6500BSC3270DevPortNumber_Object = MibTableColumn
cdx6500BSC3270DevPortNumber = _Cdx6500BSC3270DevPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 4, 1, 1, 1),
    _Cdx6500BSC3270DevPortNumber_Type()
)
cdx6500BSC3270DevPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSC3270DevPortNumber.setStatus("mandatory")


class _Cdx6500BSC3270DevEntry_Type(Integer32):
    """Custom type cdx6500BSC3270DevEntry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Cdx6500BSC3270DevEntry_Type.__name__ = "Integer32"
_Cdx6500BSC3270DevEntry_Object = MibTableColumn
cdx6500BSC3270DevEntry = _Cdx6500BSC3270DevEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 4, 1, 1, 2),
    _Cdx6500BSC3270DevEntry_Type()
)
cdx6500BSC3270DevEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSC3270DevEntry.setStatus("mandatory")


class _Cdx6500BSC3270BSCControlUnitAddr_Type(DisplayString):
    """Custom type cdx6500BSC3270BSCControlUnitAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_Cdx6500BSC3270BSCControlUnitAddr_Type.__name__ = "DisplayString"
_Cdx6500BSC3270BSCControlUnitAddr_Object = MibTableColumn
cdx6500BSC3270BSCControlUnitAddr = _Cdx6500BSC3270BSCControlUnitAddr_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 4, 1, 1, 3),
    _Cdx6500BSC3270BSCControlUnitAddr_Type()
)
cdx6500BSC3270BSCControlUnitAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSC3270BSCControlUnitAddr.setStatus("mandatory")


class _Cdx6500BSC3270BSCDevAddr_Type(DisplayString):
    """Custom type cdx6500BSC3270BSCDevAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_Cdx6500BSC3270BSCDevAddr_Type.__name__ = "DisplayString"
_Cdx6500BSC3270BSCDevAddr_Object = MibTableColumn
cdx6500BSC3270BSCDevAddr = _Cdx6500BSC3270BSCDevAddr_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 4, 1, 1, 4),
    _Cdx6500BSC3270BSCDevAddr_Type()
)
cdx6500BSC3270BSCDevAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSC3270BSCDevAddr.setStatus("mandatory")


class _Cdx6500BSC3270DSPDevType_Type(Integer32):
    """Custom type cdx6500BSC3270DSPDevType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("newvalTerm", 50),
          ("prin", 1),
          ("term", 0))
    )


_Cdx6500BSC3270DSPDevType_Type.__name__ = "Integer32"
_Cdx6500BSC3270DSPDevType_Object = MibTableColumn
cdx6500BSC3270DSPDevType = _Cdx6500BSC3270DSPDevType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 4, 1, 1, 5),
    _Cdx6500BSC3270DSPDevType_Type()
)
cdx6500BSC3270DSPDevType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSC3270DSPDevType.setStatus("mandatory")


class _Cdx6500BSC3270DSPControl_Type(DisplayString):
    """Custom type cdx6500BSC3270DSPControl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 30),
    )


_Cdx6500BSC3270DSPControl_Type.__name__ = "DisplayString"
_Cdx6500BSC3270DSPControl_Object = MibTableColumn
cdx6500BSC3270DSPControl = _Cdx6500BSC3270DSPControl_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 4, 1, 1, 6),
    _Cdx6500BSC3270DSPControl_Type()
)
cdx6500BSC3270DSPControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSC3270DSPControl.setStatus("mandatory")


class _Cdx6500BSC3270DevControl_Type(DisplayString):
    """Custom type cdx6500BSC3270DevControl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 32),
    )


_Cdx6500BSC3270DevControl_Type.__name__ = "DisplayString"
_Cdx6500BSC3270DevControl_Object = MibTableColumn
cdx6500BSC3270DevControl = _Cdx6500BSC3270DevControl_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 4, 1, 1, 7),
    _Cdx6500BSC3270DevControl_Type()
)
cdx6500BSC3270DevControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSC3270DevControl.setStatus("mandatory")


class _Cdx6500BSC3270DSPDevCharacteristics_Type(DisplayString):
    """Custom type cdx6500BSC3270DSPDevCharacteristics based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 21),
    )


_Cdx6500BSC3270DSPDevCharacteristics_Type.__name__ = "DisplayString"
_Cdx6500BSC3270DSPDevCharacteristics_Object = MibTableColumn
cdx6500BSC3270DSPDevCharacteristics = _Cdx6500BSC3270DSPDevCharacteristics_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 4, 1, 1, 8),
    _Cdx6500BSC3270DSPDevCharacteristics_Type()
)
cdx6500BSC3270DSPDevCharacteristics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSC3270DSPDevCharacteristics.setStatus("mandatory")


class _Cdx6500BSC3270DSPDevFormatSize_Type(Integer32):
    """Custom type cdx6500BSC3270DSPDevFormatSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              50)
        )
    )
    namedValues = NamedValues(
        *(("format1920", 2),
          ("format2650", 3),
          ("format3440", 4),
          ("format3564", 5),
          ("format480", 0),
          ("format960", 1),
          ("newvalFormat480", 50))
    )


_Cdx6500BSC3270DSPDevFormatSize_Type.__name__ = "Integer32"
_Cdx6500BSC3270DSPDevFormatSize_Object = MibTableColumn
cdx6500BSC3270DSPDevFormatSize = _Cdx6500BSC3270DSPDevFormatSize_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 4, 1, 1, 9),
    _Cdx6500BSC3270DSPDevFormatSize_Type()
)
cdx6500BSC3270DSPDevFormatSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSC3270DSPDevFormatSize.setStatus("mandatory")


class _Cdx6500BSC3270DSPCharSetCapability_Type(DisplayString):
    """Custom type cdx6500BSC3270DSPCharSetCapability based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 13),
    )


_Cdx6500BSC3270DSPCharSetCapability_Type.__name__ = "DisplayString"
_Cdx6500BSC3270DSPCharSetCapability_Object = MibTableColumn
cdx6500BSC3270DSPCharSetCapability = _Cdx6500BSC3270DSPCharSetCapability_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 4, 1, 1, 10),
    _Cdx6500BSC3270DSPCharSetCapability_Type()
)
cdx6500BSC3270DSPCharSetCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSC3270DSPCharSetCapability.setStatus("mandatory")


class _Cdx6500BSC3270ConnReqMode_Type(Integer32):
    """Custom type cdx6500BSC3270ConnReqMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Cdx6500BSC3270ConnReqMode_Type.__name__ = "Integer32"
_Cdx6500BSC3270ConnReqMode_Object = MibTableColumn
cdx6500BSC3270ConnReqMode = _Cdx6500BSC3270ConnReqMode_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 4, 1, 1, 11),
    _Cdx6500BSC3270ConnReqMode_Type()
)
cdx6500BSC3270ConnReqMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSC3270ConnReqMode.setStatus("mandatory")


class _Cdx6500BSC3270DestControlUnitAddr_Type(DisplayString):
    """Custom type cdx6500BSC3270DestControlUnitAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_Cdx6500BSC3270DestControlUnitAddr_Type.__name__ = "DisplayString"
_Cdx6500BSC3270DestControlUnitAddr_Object = MibTableColumn
cdx6500BSC3270DestControlUnitAddr = _Cdx6500BSC3270DestControlUnitAddr_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 4, 1, 1, 12),
    _Cdx6500BSC3270DestControlUnitAddr_Type()
)
cdx6500BSC3270DestControlUnitAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSC3270DestControlUnitAddr.setStatus("mandatory")


class _Cdx6500BSC3270DestDevAddr_Type(DisplayString):
    """Custom type cdx6500BSC3270DestDevAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_Cdx6500BSC3270DestDevAddr_Type.__name__ = "DisplayString"
_Cdx6500BSC3270DestDevAddr_Object = MibTableColumn
cdx6500BSC3270DestDevAddr = _Cdx6500BSC3270DestDevAddr_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 4, 1, 1, 13),
    _Cdx6500BSC3270DestDevAddr_Type()
)
cdx6500BSC3270DestDevAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSC3270DestDevAddr.setStatus("mandatory")


class _Cdx6500BSC3270AutocallMnemonic_Type(DisplayString):
    """Custom type cdx6500BSC3270AutocallMnemonic based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Cdx6500BSC3270AutocallMnemonic_Type.__name__ = "DisplayString"
_Cdx6500BSC3270AutocallMnemonic_Object = MibTableColumn
cdx6500BSC3270AutocallMnemonic = _Cdx6500BSC3270AutocallMnemonic_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 4, 1, 1, 14),
    _Cdx6500BSC3270AutocallMnemonic_Type()
)
cdx6500BSC3270AutocallMnemonic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSC3270AutocallMnemonic.setStatus("mandatory")


class _Cdx6500BSC3270DSPApplicationIdent_Type(Integer32):
    """Custom type cdx6500BSC3270DSPApplicationIdent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cdx6500BSC3270DSPApplicationIdent_Type.__name__ = "Integer32"
_Cdx6500BSC3270DSPApplicationIdent_Object = MibTableColumn
cdx6500BSC3270DSPApplicationIdent = _Cdx6500BSC3270DSPApplicationIdent_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 4, 1, 1, 15),
    _Cdx6500BSC3270DSPApplicationIdent_Type()
)
cdx6500BSC3270DSPApplicationIdent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSC3270DSPApplicationIdent.setStatus("mandatory")


class _Cdx6500BSC3270DSPCompatibility_Type(Integer32):
    """Custom type cdx6500BSC3270DSPCompatibility based on Integer32"""
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


_Cdx6500BSC3270DSPCompatibility_Type.__name__ = "Integer32"
_Cdx6500BSC3270DSPCompatibility_Object = MibTableColumn
cdx6500BSC3270DSPCompatibility = _Cdx6500BSC3270DSPCompatibility_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 4, 1, 1, 16),
    _Cdx6500BSC3270DSPCompatibility_Type()
)
cdx6500BSC3270DSPCompatibility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSC3270DSPCompatibility.setStatus("mandatory")


class _Cdx6500BSC3270BillRec_Type(Integer32):
    """Custom type cdx6500BSC3270BillRec based on Integer32"""
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


_Cdx6500BSC3270BillRec_Type.__name__ = "Integer32"
_Cdx6500BSC3270BillRec_Object = MibTableColumn
cdx6500BSC3270BillRec = _Cdx6500BSC3270BillRec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 4, 1, 1, 17),
    _Cdx6500BSC3270BillRec_Type()
)
cdx6500BSC3270BillRec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSC3270BillRec.setStatus("mandatory")


class _Cdx6500BSC3270TrafficPriority_Type(Integer32):
    """Custom type cdx6500BSC3270TrafficPriority based on Integer32"""
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


_Cdx6500BSC3270TrafficPriority_Type.__name__ = "Integer32"
_Cdx6500BSC3270TrafficPriority_Object = MibTableColumn
cdx6500BSC3270TrafficPriority = _Cdx6500BSC3270TrafficPriority_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 4, 1, 1, 18),
    _Cdx6500BSC3270TrafficPriority_Type()
)
cdx6500BSC3270TrafficPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSC3270TrafficPriority.setStatus("optional")
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
_Cdx6500PPSTBSC3270PortTable_Object = MibTable
cdx6500PPSTBSC3270PortTable = _Cdx6500PPSTBSC3270PortTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 10)
)
if mibBuilder.loadTexts:
    cdx6500PPSTBSC3270PortTable.setStatus("mandatory")
_Cdx6500PPSTBSC3270PortEntry_Object = MibTableRow
cdx6500PPSTBSC3270PortEntry = _Cdx6500PPSTBSC3270PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 10, 1)
)
cdx6500PPSTBSC3270PortEntry.setIndexNames(
    (0, "BSC3270-OPT-MIB", "cdx6500BSC3270StatPortNumber"),
)
if mibBuilder.loadTexts:
    cdx6500PPSTBSC3270PortEntry.setStatus("mandatory")


class _Cdx6500BSC3270StatPortNumber_Type(Integer32):
    """Custom type cdx6500BSC3270StatPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_Cdx6500BSC3270StatPortNumber_Type.__name__ = "Integer32"
_Cdx6500BSC3270StatPortNumber_Object = MibTableColumn
cdx6500BSC3270StatPortNumber = _Cdx6500BSC3270StatPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 10, 1, 1),
    _Cdx6500BSC3270StatPortNumber_Type()
)
cdx6500BSC3270StatPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSC3270StatPortNumber.setStatus("mandatory")


class _Cdx6500BSC3270PortStatus_Type(Integer32):
    """Custom type cdx6500BSC3270PortStatus based on Integer32"""
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


_Cdx6500BSC3270PortStatus_Type.__name__ = "Integer32"
_Cdx6500BSC3270PortStatus_Object = MibTableColumn
cdx6500BSC3270PortStatus = _Cdx6500BSC3270PortStatus_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 10, 1, 2),
    _Cdx6500BSC3270PortStatus_Type()
)
cdx6500BSC3270PortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSC3270PortStatus.setStatus("mandatory")


class _Cdx6500BSC3270PortState_Type(DisplayString):
    """Custom type cdx6500BSC3270PortState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 10),
    )


_Cdx6500BSC3270PortState_Type.__name__ = "DisplayString"
_Cdx6500BSC3270PortState_Object = MibTableColumn
cdx6500BSC3270PortState = _Cdx6500BSC3270PortState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 10, 1, 3),
    _Cdx6500BSC3270PortState_Type()
)
cdx6500BSC3270PortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSC3270PortState.setStatus("mandatory")
_Cdx6500BSC3270PortSpeed_Type = Integer32
_Cdx6500BSC3270PortSpeed_Object = MibTableColumn
cdx6500BSC3270PortSpeed = _Cdx6500BSC3270PortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 10, 1, 4),
    _Cdx6500BSC3270PortSpeed_Type()
)
cdx6500BSC3270PortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSC3270PortSpeed.setStatus("mandatory")


class _Cdx6500BSC3270PortUtilIn_Type(Integer32):
    """Custom type cdx6500BSC3270PortUtilIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Cdx6500BSC3270PortUtilIn_Type.__name__ = "Integer32"
_Cdx6500BSC3270PortUtilIn_Object = MibTableColumn
cdx6500BSC3270PortUtilIn = _Cdx6500BSC3270PortUtilIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 10, 1, 5),
    _Cdx6500BSC3270PortUtilIn_Type()
)
cdx6500BSC3270PortUtilIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSC3270PortUtilIn.setStatus("mandatory")


class _Cdx6500BSC3270PortUtilOut_Type(Integer32):
    """Custom type cdx6500BSC3270PortUtilOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Cdx6500BSC3270PortUtilOut_Type.__name__ = "Integer32"
_Cdx6500BSC3270PortUtilOut_Object = MibTableColumn
cdx6500BSC3270PortUtilOut = _Cdx6500BSC3270PortUtilOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 10, 1, 6),
    _Cdx6500BSC3270PortUtilOut_Type()
)
cdx6500BSC3270PortUtilOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSC3270PortUtilOut.setStatus("mandatory")
_Cdx6500BSC3270InMsgs_Type = Counter32
_Cdx6500BSC3270InMsgs_Object = MibTableColumn
cdx6500BSC3270InMsgs = _Cdx6500BSC3270InMsgs_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 10, 1, 7),
    _Cdx6500BSC3270InMsgs_Type()
)
cdx6500BSC3270InMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSC3270InMsgs.setStatus("mandatory")
_Cdx6500BSC3270OutMsgs_Type = Counter32
_Cdx6500BSC3270OutMsgs_Object = MibTableColumn
cdx6500BSC3270OutMsgs = _Cdx6500BSC3270OutMsgs_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 10, 1, 8),
    _Cdx6500BSC3270OutMsgs_Type()
)
cdx6500BSC3270OutMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSC3270OutMsgs.setStatus("mandatory")
_Cdx6500BSC3270InChars_Type = Counter32
_Cdx6500BSC3270InChars_Object = MibTableColumn
cdx6500BSC3270InChars = _Cdx6500BSC3270InChars_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 10, 1, 9),
    _Cdx6500BSC3270InChars_Type()
)
cdx6500BSC3270InChars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSC3270InChars.setStatus("mandatory")
_Cdx6500BSC3270OutChars_Type = Counter32
_Cdx6500BSC3270OutChars_Object = MibTableColumn
cdx6500BSC3270OutChars = _Cdx6500BSC3270OutChars_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 10, 1, 10),
    _Cdx6500BSC3270OutChars_Type()
)
cdx6500BSC3270OutChars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSC3270OutChars.setStatus("mandatory")


class _Cdx6500BSC3270CharRateIn_Type(Integer32):
    """Custom type cdx6500BSC3270CharRateIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Cdx6500BSC3270CharRateIn_Type.__name__ = "Integer32"
_Cdx6500BSC3270CharRateIn_Object = MibTableColumn
cdx6500BSC3270CharRateIn = _Cdx6500BSC3270CharRateIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 10, 1, 11),
    _Cdx6500BSC3270CharRateIn_Type()
)
cdx6500BSC3270CharRateIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSC3270CharRateIn.setStatus("mandatory")


class _Cdx6500BSC3270CharRateOut_Type(Integer32):
    """Custom type cdx6500BSC3270CharRateOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Cdx6500BSC3270CharRateOut_Type.__name__ = "Integer32"
_Cdx6500BSC3270CharRateOut_Object = MibTableColumn
cdx6500BSC3270CharRateOut = _Cdx6500BSC3270CharRateOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 10, 1, 12),
    _Cdx6500BSC3270CharRateOut_Type()
)
cdx6500BSC3270CharRateOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSC3270CharRateOut.setStatus("mandatory")
_Cdx6500BSC3270CrcBccErrs_Type = Counter32
_Cdx6500BSC3270CrcBccErrs_Object = MibTableColumn
cdx6500BSC3270CrcBccErrs = _Cdx6500BSC3270CrcBccErrs_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 10, 1, 13),
    _Cdx6500BSC3270CrcBccErrs_Type()
)
cdx6500BSC3270CrcBccErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSC3270CrcBccErrs.setStatus("mandatory")
_Cdx6500BSC3270InPosAcks_Type = Counter32
_Cdx6500BSC3270InPosAcks_Object = MibTableColumn
cdx6500BSC3270InPosAcks = _Cdx6500BSC3270InPosAcks_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 10, 1, 14),
    _Cdx6500BSC3270InPosAcks_Type()
)
cdx6500BSC3270InPosAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSC3270InPosAcks.setStatus("mandatory")
_Cdx6500BSC3270OutPosAcks_Type = Counter32
_Cdx6500BSC3270OutPosAcks_Object = MibTableColumn
cdx6500BSC3270OutPosAcks = _Cdx6500BSC3270OutPosAcks_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 10, 1, 15),
    _Cdx6500BSC3270OutPosAcks_Type()
)
cdx6500BSC3270OutPosAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSC3270OutPosAcks.setStatus("mandatory")
_Cdx6500BSC3270InNegAcks_Type = Counter32
_Cdx6500BSC3270InNegAcks_Object = MibTableColumn
cdx6500BSC3270InNegAcks = _Cdx6500BSC3270InNegAcks_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 10, 1, 16),
    _Cdx6500BSC3270InNegAcks_Type()
)
cdx6500BSC3270InNegAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSC3270InNegAcks.setStatus("mandatory")
_Cdx6500BSC3270OutNegAcks_Type = Counter32
_Cdx6500BSC3270OutNegAcks_Object = MibTableColumn
cdx6500BSC3270OutNegAcks = _Cdx6500BSC3270OutNegAcks_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 10, 1, 17),
    _Cdx6500BSC3270OutNegAcks_Type()
)
cdx6500BSC3270OutNegAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSC3270OutNegAcks.setStatus("mandatory")
_Cdx6500BSC3270MsgRateIn_Type = Counter32
_Cdx6500BSC3270MsgRateIn_Object = MibTableColumn
cdx6500BSC3270MsgRateIn = _Cdx6500BSC3270MsgRateIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 10, 1, 18),
    _Cdx6500BSC3270MsgRateIn_Type()
)
cdx6500BSC3270MsgRateIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSC3270MsgRateIn.setStatus("mandatory")
_Cdx6500BSC3270MsgRateOut_Type = Counter32
_Cdx6500BSC3270MsgRateOut_Object = MibTableColumn
cdx6500BSC3270MsgRateOut = _Cdx6500BSC3270MsgRateOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 10, 1, 19),
    _Cdx6500BSC3270MsgRateOut_Type()
)
cdx6500BSC3270MsgRateOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSC3270MsgRateOut.setStatus("mandatory")
_Cdx6500BSC3270InEnq_Type = Counter32
_Cdx6500BSC3270InEnq_Object = MibTableColumn
cdx6500BSC3270InEnq = _Cdx6500BSC3270InEnq_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 10, 1, 20),
    _Cdx6500BSC3270InEnq_Type()
)
cdx6500BSC3270InEnq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSC3270InEnq.setStatus("mandatory")
_Cdx6500BSC3270OutEnq_Type = Counter32
_Cdx6500BSC3270OutEnq_Object = MibTableColumn
cdx6500BSC3270OutEnq = _Cdx6500BSC3270OutEnq_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 10, 1, 21),
    _Cdx6500BSC3270OutEnq_Type()
)
cdx6500BSC3270OutEnq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSC3270OutEnq.setStatus("mandatory")
_Cdx6500BSC3270NumRetran_Type = Counter32
_Cdx6500BSC3270NumRetran_Object = MibTableColumn
cdx6500BSC3270NumRetran = _Cdx6500BSC3270NumRetran_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 10, 1, 22),
    _Cdx6500BSC3270NumRetran_Type()
)
cdx6500BSC3270NumRetran.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500BSC3270NumRetran.setStatus("mandatory")
_Cdx6500Controls_ObjectIdentity = ObjectIdentity
cdx6500Controls = _Cdx6500Controls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BSC3270-OPT-MIB",
    **{"DisplayString": DisplayString,
       "codex": codex,
       "cdxProductSpecific": cdxProductSpecific,
       "cdx6500": cdx6500,
       "cdx6500Configuration": cdx6500Configuration,
       "cdx6500CfgProtocolGroup": cdx6500CfgProtocolGroup,
       "cdx6500PCTPortProtocolGroup": cdx6500PCTPortProtocolGroup,
       "cdx6500PPCTBSC3270PortTable": cdx6500PPCTBSC3270PortTable,
       "cdx6500PPCTBSC3270PortEntry": cdx6500PPCTBSC3270PortEntry,
       "cdx6500BSC3270PortNumber": cdx6500BSC3270PortNumber,
       "cdx6500BSC3270PADType": cdx6500BSC3270PADType,
       "cdx6500BSC3270ClockSource": cdx6500BSC3270ClockSource,
       "cdx6500BSC3270ClockSpeed": cdx6500BSC3270ClockSpeed,
       "cdx6500BSC3270Contention": cdx6500BSC3270Contention,
       "cdx6500BSC3270NumDevices": cdx6500BSC3270NumDevices,
       "cdx6500BSC3270ServTimer": cdx6500BSC3270ServTimer,
       "cdx6500BSC3270ErrThreshCount": cdx6500BSC3270ErrThreshCount,
       "cdx6500BSC3270ResponseTimeout": cdx6500BSC3270ResponseTimeout,
       "cdx6500BSC3270HostPADTimeout": cdx6500BSC3270HostPADTimeout,
       "cdx6500BSC3270InterBuffTimeout": cdx6500BSC3270InterBuffTimeout,
       "cdx6500BSC3270IdleDevTimeout": cdx6500BSC3270IdleDevTimeout,
       "cdx6500BSC3270PrintDisconTimer": cdx6500BSC3270PrintDisconTimer,
       "cdx6500BSC3270SignonKey": cdx6500BSC3270SignonKey,
       "cdx6500BSC3270DiscKey": cdx6500BSC3270DiscKey,
       "cdx6500BSC3270CharSet": cdx6500BSC3270CharSet,
       "cdx6500BSC3270PortSubAddr": cdx6500BSC3270PortSubAddr,
       "cdx6500BSC3270PortOptions": cdx6500BSC3270PortOptions,
       "cdx6500BSC3270RestrictConnDest": cdx6500BSC3270RestrictConnDest,
       "cdx6500bsc3270ElectricalInterfaceType": cdx6500bsc3270ElectricalInterfaceType,
       "cdx6500bsc3270V24ElectricalInterfaceOption": cdx6500bsc3270V24ElectricalInterfaceOption,
       "cdx6500bsc3270HighSpeedElectricalInterfaceOption": cdx6500bsc3270HighSpeedElectricalInterfaceOption,
       "cdx6500PCTBSC3270DeviceGroup": cdx6500PCTBSC3270DeviceGroup,
       "cdx6500PBCTBSC3270DevTable": cdx6500PBCTBSC3270DevTable,
       "cdx6500PBCTBSC3270DevEntry": cdx6500PBCTBSC3270DevEntry,
       "cdx6500BSC3270DevPortNumber": cdx6500BSC3270DevPortNumber,
       "cdx6500BSC3270DevEntry": cdx6500BSC3270DevEntry,
       "cdx6500BSC3270BSCControlUnitAddr": cdx6500BSC3270BSCControlUnitAddr,
       "cdx6500BSC3270BSCDevAddr": cdx6500BSC3270BSCDevAddr,
       "cdx6500BSC3270DSPDevType": cdx6500BSC3270DSPDevType,
       "cdx6500BSC3270DSPControl": cdx6500BSC3270DSPControl,
       "cdx6500BSC3270DevControl": cdx6500BSC3270DevControl,
       "cdx6500BSC3270DSPDevCharacteristics": cdx6500BSC3270DSPDevCharacteristics,
       "cdx6500BSC3270DSPDevFormatSize": cdx6500BSC3270DSPDevFormatSize,
       "cdx6500BSC3270DSPCharSetCapability": cdx6500BSC3270DSPCharSetCapability,
       "cdx6500BSC3270ConnReqMode": cdx6500BSC3270ConnReqMode,
       "cdx6500BSC3270DestControlUnitAddr": cdx6500BSC3270DestControlUnitAddr,
       "cdx6500BSC3270DestDevAddr": cdx6500BSC3270DestDevAddr,
       "cdx6500BSC3270AutocallMnemonic": cdx6500BSC3270AutocallMnemonic,
       "cdx6500BSC3270DSPApplicationIdent": cdx6500BSC3270DSPApplicationIdent,
       "cdx6500BSC3270DSPCompatibility": cdx6500BSC3270DSPCompatibility,
       "cdx6500BSC3270BillRec": cdx6500BSC3270BillRec,
       "cdx6500BSC3270TrafficPriority": cdx6500BSC3270TrafficPriority,
       "cdx6500Statistics": cdx6500Statistics,
       "cdx6500StatProtocolGroup": cdx6500StatProtocolGroup,
       "cdx6500PSTPortProtocolGroup": cdx6500PSTPortProtocolGroup,
       "cdx6500PPSTBSC3270PortTable": cdx6500PPSTBSC3270PortTable,
       "cdx6500PPSTBSC3270PortEntry": cdx6500PPSTBSC3270PortEntry,
       "cdx6500BSC3270StatPortNumber": cdx6500BSC3270StatPortNumber,
       "cdx6500BSC3270PortStatus": cdx6500BSC3270PortStatus,
       "cdx6500BSC3270PortState": cdx6500BSC3270PortState,
       "cdx6500BSC3270PortSpeed": cdx6500BSC3270PortSpeed,
       "cdx6500BSC3270PortUtilIn": cdx6500BSC3270PortUtilIn,
       "cdx6500BSC3270PortUtilOut": cdx6500BSC3270PortUtilOut,
       "cdx6500BSC3270InMsgs": cdx6500BSC3270InMsgs,
       "cdx6500BSC3270OutMsgs": cdx6500BSC3270OutMsgs,
       "cdx6500BSC3270InChars": cdx6500BSC3270InChars,
       "cdx6500BSC3270OutChars": cdx6500BSC3270OutChars,
       "cdx6500BSC3270CharRateIn": cdx6500BSC3270CharRateIn,
       "cdx6500BSC3270CharRateOut": cdx6500BSC3270CharRateOut,
       "cdx6500BSC3270CrcBccErrs": cdx6500BSC3270CrcBccErrs,
       "cdx6500BSC3270InPosAcks": cdx6500BSC3270InPosAcks,
       "cdx6500BSC3270OutPosAcks": cdx6500BSC3270OutPosAcks,
       "cdx6500BSC3270InNegAcks": cdx6500BSC3270InNegAcks,
       "cdx6500BSC3270OutNegAcks": cdx6500BSC3270OutNegAcks,
       "cdx6500BSC3270MsgRateIn": cdx6500BSC3270MsgRateIn,
       "cdx6500BSC3270MsgRateOut": cdx6500BSC3270MsgRateOut,
       "cdx6500BSC3270InEnq": cdx6500BSC3270InEnq,
       "cdx6500BSC3270OutEnq": cdx6500BSC3270OutEnq,
       "cdx6500BSC3270NumRetran": cdx6500BSC3270NumRetran,
       "cdx6500Controls": cdx6500Controls}
)
