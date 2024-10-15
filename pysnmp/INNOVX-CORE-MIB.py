# SNMP MIB module (INNOVX-CORE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INNOVX-CORE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:06 2024
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

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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

_Gdc_ObjectIdentity = ObjectIdentity
gdc = _Gdc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498)
)
_Framerelay_ObjectIdentity = ObjectIdentity
framerelay = _Framerelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 22)
)
_Innovx_ObjectIdentity = ObjectIdentity
innovx = _Innovx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 22, 1)
)
_CoreGroup_ObjectIdentity = ObjectIdentity
coreGroup = _CoreGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 1)
)
_CoreAdmin_ObjectIdentity = ObjectIdentity
coreAdmin = _CoreAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 1, 1)
)


class _InnovxMIBversion_Type(DisplayString):
    """Custom type innovxMIBversion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_InnovxMIBversion_Type.__name__ = "DisplayString"
_InnovxMIBversion_Object = MibScalar
innovxMIBversion = _InnovxMIBversion_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 1, 1, 1),
    _InnovxMIBversion_Type()
)
innovxMIBversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    innovxMIBversion.setStatus("mandatory")


class _InnovxFirmwareVersion_Type(DisplayString):
    """Custom type innovxFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_InnovxFirmwareVersion_Type.__name__ = "DisplayString"
_InnovxFirmwareVersion_Object = MibScalar
innovxFirmwareVersion = _InnovxFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 1, 1, 2),
    _InnovxFirmwareVersion_Type()
)
innovxFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    innovxFirmwareVersion.setStatus("mandatory")


class _InnovxSerialNumber_Type(DisplayString):
    """Custom type innovxSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_InnovxSerialNumber_Type.__name__ = "DisplayString"
_InnovxSerialNumber_Object = MibScalar
innovxSerialNumber = _InnovxSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 1, 1, 3),
    _InnovxSerialNumber_Type()
)
innovxSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    innovxSerialNumber.setStatus("mandatory")


class _InnovxHardwareVersion_Type(DisplayString):
    """Custom type innovxHardwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_InnovxHardwareVersion_Type.__name__ = "DisplayString"
_InnovxHardwareVersion_Object = MibScalar
innovxHardwareVersion = _InnovxHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 1, 1, 4),
    _InnovxHardwareVersion_Type()
)
innovxHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    innovxHardwareVersion.setStatus("mandatory")


class _InnovxHardwareDescription_Type(DisplayString):
    """Custom type innovxHardwareDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )


_InnovxHardwareDescription_Type.__name__ = "DisplayString"
_InnovxHardwareDescription_Object = MibScalar
innovxHardwareDescription = _InnovxHardwareDescription_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 1, 1, 5),
    _InnovxHardwareDescription_Type()
)
innovxHardwareDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    innovxHardwareDescription.setStatus("mandatory")


class _InnovxBootCodeVersion_Type(DisplayString):
    """Custom type innovxBootCodeVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_InnovxBootCodeVersion_Type.__name__ = "DisplayString"
_InnovxBootCodeVersion_Object = MibScalar
innovxBootCodeVersion = _InnovxBootCodeVersion_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 1, 1, 6),
    _InnovxBootCodeVersion_Type()
)
innovxBootCodeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    innovxBootCodeVersion.setStatus("mandatory")


class _InnovxHardwareOptions_Type(OctetString):
    """Custom type innovxHardwareOptions based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_InnovxHardwareOptions_Type.__name__ = "OctetString"
_InnovxHardwareOptions_Object = MibScalar
innovxHardwareOptions = _InnovxHardwareOptions_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 1, 1, 7),
    _InnovxHardwareOptions_Type()
)
innovxHardwareOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    innovxHardwareOptions.setStatus("mandatory")
_CmnTrapAddrTable_Object = MibTable
cmnTrapAddrTable = _CmnTrapAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 1, 1, 8)
)
if mibBuilder.loadTexts:
    cmnTrapAddrTable.setStatus("mandatory")
_CmnTrapAddrEntry_Object = MibTableRow
cmnTrapAddrEntry = _CmnTrapAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 1, 1, 8, 1)
)
cmnTrapAddrEntry.setIndexNames(
    (0, "INNOVX-CORE-MIB", "cmnTrapAddrIpDest"),
)
if mibBuilder.loadTexts:
    cmnTrapAddrEntry.setStatus("mandatory")
_CmnTrapAddrIpDest_Type = IpAddress
_CmnTrapAddrIpDest_Object = MibTableColumn
cmnTrapAddrIpDest = _CmnTrapAddrIpDest_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 1, 1, 8, 1, 1),
    _CmnTrapAddrIpDest_Type()
)
cmnTrapAddrIpDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmnTrapAddrIpDest.setStatus("mandatory")


class _CmnTrapAddrCommunity_Type(DisplayString):
    """Custom type cmnTrapAddrCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CmnTrapAddrCommunity_Type.__name__ = "DisplayString"
_CmnTrapAddrCommunity_Object = MibTableColumn
cmnTrapAddrCommunity = _CmnTrapAddrCommunity_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 1, 1, 8, 1, 2),
    _CmnTrapAddrCommunity_Type()
)
cmnTrapAddrCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmnTrapAddrCommunity.setStatus("mandatory")


class _CmnTrapAddrStatus_Type(Integer32):
    """Custom type cmnTrapAddrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_CmnTrapAddrStatus_Type.__name__ = "Integer32"
_CmnTrapAddrStatus_Object = MibTableColumn
cmnTrapAddrStatus = _CmnTrapAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 1, 1, 8, 1, 3),
    _CmnTrapAddrStatus_Type()
)
cmnTrapAddrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmnTrapAddrStatus.setStatus("mandatory")
_CoreReset_ObjectIdentity = ObjectIdentity
coreReset = _CoreReset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 1, 2)
)


class _InnovxSoftReset_Type(Integer32):
    """Custom type innovxSoftReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("reset", 2))
    )


_InnovxSoftReset_Type.__name__ = "Integer32"
_InnovxSoftReset_Object = MibScalar
innovxSoftReset = _InnovxSoftReset_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 1, 2, 1),
    _InnovxSoftReset_Type()
)
innovxSoftReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    innovxSoftReset.setStatus("mandatory")


class _InnovxStatsReset_Type(Integer32):
    """Custom type innovxStatsReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("reset", 2))
    )


_InnovxStatsReset_Type.__name__ = "Integer32"
_InnovxStatsReset_Object = MibScalar
innovxStatsReset = _InnovxStatsReset_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 1, 2, 2),
    _InnovxStatsReset_Type()
)
innovxStatsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    innovxStatsReset.setStatus("mandatory")
_CoreDiags_ObjectIdentity = ObjectIdentity
coreDiags = _CoreDiags_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 1, 3)
)


class _InnovxSelfTest_Type(Integer32):
    """Custom type innovxSelfTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("start-test", 2))
    )


_InnovxSelfTest_Type.__name__ = "Integer32"
_InnovxSelfTest_Object = MibScalar
innovxSelfTest = _InnovxSelfTest_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 1, 3, 1),
    _InnovxSelfTest_Type()
)
innovxSelfTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    innovxSelfTest.setStatus("mandatory")


class _InnovxSelfTestStatus_Type(Integer32):
    """Custom type innovxSelfTestStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal-complete-fail", 2),
          ("normal-complete-pass", 1),
          ("test-in-progress", 3))
    )


_InnovxSelfTestStatus_Type.__name__ = "Integer32"
_InnovxSelfTestStatus_Object = MibScalar
innovxSelfTestStatus = _InnovxSelfTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 1, 3, 2),
    _InnovxSelfTestStatus_Type()
)
innovxSelfTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    innovxSelfTestStatus.setStatus("mandatory")
_CoreStatus_ObjectIdentity = ObjectIdentity
coreStatus = _CoreStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 1, 4)
)


class _InnovxLedStatus_Type(OctetString):
    """Custom type innovxLedStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_InnovxLedStatus_Type.__name__ = "OctetString"
_InnovxLedStatus_Object = MibScalar
innovxLedStatus = _InnovxLedStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 1, 4, 1),
    _InnovxLedStatus_Type()
)
innovxLedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    innovxLedStatus.setStatus("mandatory")


class _InnovxPortStatus_Type(OctetString):
    """Custom type innovxPortStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_InnovxPortStatus_Type.__name__ = "OctetString"
_InnovxPortStatus_Object = MibScalar
innovxPortStatus = _InnovxPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 1, 4, 2),
    _InnovxPortStatus_Type()
)
innovxPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    innovxPortStatus.setStatus("mandatory")


class _InnovxPortFrameCounts_Type(OctetString):
    """Custom type innovxPortFrameCounts based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_InnovxPortFrameCounts_Type.__name__ = "OctetString"
_InnovxPortFrameCounts_Object = MibScalar
innovxPortFrameCounts = _InnovxPortFrameCounts_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 1, 4, 3),
    _InnovxPortFrameCounts_Type()
)
innovxPortFrameCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    innovxPortFrameCounts.setStatus("mandatory")
_CoreTrapArgs_ObjectIdentity = ObjectIdentity
coreTrapArgs = _CoreTrapArgs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 1, 5)
)


class _InnovxTrapSeverity_Type(Integer32):
    """Custom type innovxTrapSeverity based on Integer32"""
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
        *(("critical", 1),
          ("info", 5),
          ("major", 2),
          ("minor", 3),
          ("warning", 4))
    )


_InnovxTrapSeverity_Type.__name__ = "Integer32"
_InnovxTrapSeverity_Object = MibScalar
innovxTrapSeverity = _InnovxTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 1, 5, 1),
    _InnovxTrapSeverity_Type()
)
innovxTrapSeverity.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    innovxTrapSeverity.setStatus("mandatory")


class _InnovxTrapState_Type(DisplayString):
    """Custom type innovxTrapState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_InnovxTrapState_Type.__name__ = "DisplayString"
_InnovxTrapState_Object = MibScalar
innovxTrapState = _InnovxTrapState_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 1, 5, 2),
    _InnovxTrapState_Type()
)
innovxTrapState.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    innovxTrapState.setStatus("mandatory")


class _InnovxTrapDescription_Type(DisplayString):
    """Custom type innovxTrapDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_InnovxTrapDescription_Type.__name__ = "DisplayString"
_InnovxTrapDescription_Object = MibScalar
innovxTrapDescription = _InnovxTrapDescription_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 1, 5, 3),
    _InnovxTrapDescription_Type()
)
innovxTrapDescription.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    innovxTrapDescription.setStatus("mandatory")


class _InnovxTrapThreshold_Type(DisplayString):
    """Custom type innovxTrapThreshold based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_InnovxTrapThreshold_Type.__name__ = "DisplayString"
_InnovxTrapThreshold_Object = MibScalar
innovxTrapThreshold = _InnovxTrapThreshold_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 1, 5, 4),
    _InnovxTrapThreshold_Type()
)
innovxTrapThreshold.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    innovxTrapThreshold.setStatus("mandatory")


class _InnovxTrapActualValue_Type(DisplayString):
    """Custom type innovxTrapActualValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_InnovxTrapActualValue_Type.__name__ = "DisplayString"
_InnovxTrapActualValue_Object = MibScalar
innovxTrapActualValue = _InnovxTrapActualValue_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 1, 5, 5),
    _InnovxTrapActualValue_Type()
)
innovxTrapActualValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    innovxTrapActualValue.setStatus("mandatory")


class _InnovxTrapDlci_Type(Integer32):
    """Custom type innovxTrapDlci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 991),
    )


_InnovxTrapDlci_Type.__name__ = "Integer32"
_InnovxTrapDlci_Object = MibScalar
innovxTrapDlci = _InnovxTrapDlci_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 1, 5, 6),
    _InnovxTrapDlci_Type()
)
innovxTrapDlci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    innovxTrapDlci.setStatus("mandatory")


class _InnovxpvcIdentifier_Type(DisplayString):
    """Custom type innovxpvcIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_InnovxpvcIdentifier_Type.__name__ = "DisplayString"
_InnovxpvcIdentifier_Object = MibScalar
innovxpvcIdentifier = _InnovxpvcIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 1, 5, 7),
    _InnovxpvcIdentifier_Type()
)
innovxpvcIdentifier.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    innovxpvcIdentifier.setStatus("mandatory")
_CoreAggRate_ObjectIdentity = ObjectIdentity
coreAggRate = _CoreAggRate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 1, 6)
)


class _Ap553DS0Format_Type(Integer32):
    """Custom type ap553DS0Format based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nx56k", 1),
          ("nx64k", 2))
    )


_Ap553DS0Format_Type.__name__ = "Integer32"
_Ap553DS0Format_Object = MibScalar
ap553DS0Format = _Ap553DS0Format_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 1, 6, 1),
    _Ap553DS0Format_Type()
)
ap553DS0Format.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap553DS0Format.setStatus("mandatory")


class _Ap553NumberOfDS0s_Type(Integer32):
    """Custom type ap553NumberOfDS0s based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Ap553NumberOfDS0s_Type.__name__ = "Integer32"
_Ap553NumberOfDS0s_Object = MibScalar
ap553NumberOfDS0s = _Ap553NumberOfDS0s_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 1, 6, 2),
    _Ap553NumberOfDS0s_Type()
)
ap553NumberOfDS0s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ap553NumberOfDS0s.setStatus("mandatory")
_CoreFeatures_ObjectIdentity = ObjectIdentity
coreFeatures = _CoreFeatures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 1, 7)
)
_InnovxFeatureTable_Object = MibTable
innovxFeatureTable = _InnovxFeatureTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 1, 7, 1)
)
if mibBuilder.loadTexts:
    innovxFeatureTable.setStatus("mandatory")
_InnovxFeatureEntry_Object = MibTableRow
innovxFeatureEntry = _InnovxFeatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 1, 7, 1, 1)
)
innovxFeatureEntry.setIndexNames(
    (0, "INNOVX-CORE-MIB", "innovxFeatureIndex"),
)
if mibBuilder.loadTexts:
    innovxFeatureEntry.setStatus("mandatory")


class _InnovxFeatureIndex_Type(Integer32):
    """Custom type innovxFeatureIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_InnovxFeatureIndex_Type.__name__ = "Integer32"
_InnovxFeatureIndex_Object = MibTableColumn
innovxFeatureIndex = _InnovxFeatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 1, 7, 1, 1, 1),
    _InnovxFeatureIndex_Type()
)
innovxFeatureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    innovxFeatureIndex.setStatus("mandatory")
_InnovxFeatureName_Type = DisplayString
_InnovxFeatureName_Object = MibTableColumn
innovxFeatureName = _InnovxFeatureName_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 1, 7, 1, 1, 2),
    _InnovxFeatureName_Type()
)
innovxFeatureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    innovxFeatureName.setStatus("mandatory")


class _InnovxFeatureEnable_Type(Integer32):
    """Custom type innovxFeatureEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_InnovxFeatureEnable_Type.__name__ = "Integer32"
_InnovxFeatureEnable_Object = MibTableColumn
innovxFeatureEnable = _InnovxFeatureEnable_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 1, 7, 1, 1, 3),
    _InnovxFeatureEnable_Type()
)
innovxFeatureEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    innovxFeatureEnable.setStatus("mandatory")


class _InnovxFeatureStatus_Type(Integer32):
    """Custom type innovxFeatureStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_InnovxFeatureStatus_Type.__name__ = "Integer32"
_InnovxFeatureStatus_Object = MibTableColumn
innovxFeatureStatus = _InnovxFeatureStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 1, 7, 1, 1, 4),
    _InnovxFeatureStatus_Type()
)
innovxFeatureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    innovxFeatureStatus.setStatus("mandatory")
_LinkProbe_ObjectIdentity = ObjectIdentity
linkProbe = _LinkProbe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 2)
)
_LiuGroup_ObjectIdentity = ObjectIdentity
liuGroup = _LiuGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 3)
)
_CasGroup_ObjectIdentity = ObjectIdentity
casGroup = _CasGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 4)
)
_DdsGroup_ObjectIdentity = ObjectIdentity
ddsGroup = _DdsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 5)
)
_DteGroup_ObjectIdentity = ObjectIdentity
dteGroup = _DteGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 6)
)

# Managed Objects groups


# Notification objects

innovxAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 498, 22, 1, 0, 1)
)
innovxAlarmTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("INNOVX-CORE-MIB", "innovxTrapSeverity"),
        ("INNOVX-CORE-MIB", "innovxTrapState"),
        ("INNOVX-CORE-MIB", "innovxTrapDescription"),
        ("INNOVX-CORE-MIB", "innovxTrapThreshold"),
        ("INNOVX-CORE-MIB", "innovxTrapActualValue"),
        ("INNOVX-CORE-MIB", "innovxTrapDlci"),
        ("INNOVX-CORE-MIB", "innovxpvcIdentifier"))
)
if mibBuilder.loadTexts:
    innovxAlarmTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INNOVX-CORE-MIB",
    **{"gdc": gdc,
       "framerelay": framerelay,
       "innovx": innovx,
       "innovxAlarmTrap": innovxAlarmTrap,
       "coreGroup": coreGroup,
       "coreAdmin": coreAdmin,
       "innovxMIBversion": innovxMIBversion,
       "innovxFirmwareVersion": innovxFirmwareVersion,
       "innovxSerialNumber": innovxSerialNumber,
       "innovxHardwareVersion": innovxHardwareVersion,
       "innovxHardwareDescription": innovxHardwareDescription,
       "innovxBootCodeVersion": innovxBootCodeVersion,
       "innovxHardwareOptions": innovxHardwareOptions,
       "cmnTrapAddrTable": cmnTrapAddrTable,
       "cmnTrapAddrEntry": cmnTrapAddrEntry,
       "cmnTrapAddrIpDest": cmnTrapAddrIpDest,
       "cmnTrapAddrCommunity": cmnTrapAddrCommunity,
       "cmnTrapAddrStatus": cmnTrapAddrStatus,
       "coreReset": coreReset,
       "innovxSoftReset": innovxSoftReset,
       "innovxStatsReset": innovxStatsReset,
       "coreDiags": coreDiags,
       "innovxSelfTest": innovxSelfTest,
       "innovxSelfTestStatus": innovxSelfTestStatus,
       "coreStatus": coreStatus,
       "innovxLedStatus": innovxLedStatus,
       "innovxPortStatus": innovxPortStatus,
       "innovxPortFrameCounts": innovxPortFrameCounts,
       "coreTrapArgs": coreTrapArgs,
       "innovxTrapSeverity": innovxTrapSeverity,
       "innovxTrapState": innovxTrapState,
       "innovxTrapDescription": innovxTrapDescription,
       "innovxTrapThreshold": innovxTrapThreshold,
       "innovxTrapActualValue": innovxTrapActualValue,
       "innovxTrapDlci": innovxTrapDlci,
       "innovxpvcIdentifier": innovxpvcIdentifier,
       "coreAggRate": coreAggRate,
       "ap553DS0Format": ap553DS0Format,
       "ap553NumberOfDS0s": ap553NumberOfDS0s,
       "coreFeatures": coreFeatures,
       "innovxFeatureTable": innovxFeatureTable,
       "innovxFeatureEntry": innovxFeatureEntry,
       "innovxFeatureIndex": innovxFeatureIndex,
       "innovxFeatureName": innovxFeatureName,
       "innovxFeatureEnable": innovxFeatureEnable,
       "innovxFeatureStatus": innovxFeatureStatus,
       "linkProbe": linkProbe,
       "liuGroup": liuGroup,
       "casGroup": casGroup,
       "ddsGroup": ddsGroup,
       "dteGroup": dteGroup}
)
