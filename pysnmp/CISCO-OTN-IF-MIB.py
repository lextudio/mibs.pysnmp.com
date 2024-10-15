# SNMP MIB module (CISCO-OTN-IF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-OTN-IF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:06:32 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(ifIndex,
 ifName) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex",
    "ifName")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoOtnIfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 639)
)
ciscoOtnIfMIB.setRevisions(
        ("2016-05-25 00:00",
         "2011-01-24 00:00",
         "2008-09-11 00:00",
         "2007-10-10 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CoiIntervalType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fifteenMin", 1),
          ("oneDay", 2),
          ("thirtySecond", 3))
    )



class CoiMonitorType(Integer32, TextualConvention):
    status = "current"
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
        *(("path", 1),
          ("section", 2),
          ("tcm1", 3),
          ("tcm2", 4))
    )



class CoiOtnThresholdType(Integer32, TextualConvention):
    status = "current"
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
        *(("bbe", 5),
          ("bber", 8),
          ("es", 2),
          ("esr", 6),
          ("fc", 1),
          ("ses", 3),
          ("sesr", 7),
          ("uas", 4))
    )



class CoiOpticalWavelength(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1528770, 1604030),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoOtnIfMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoOtnIfMIBNotifs = _CiscoOtnIfMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 0)
)
_CiscoOtnIfMIBObjects_ObjectIdentity = ObjectIdentity
ciscoOtnIfMIBObjects = _CiscoOtnIfMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1)
)
_CoiDwdmInterface_ObjectIdentity = ObjectIdentity
coiDwdmInterface = _CoiDwdmInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 1)
)
_CoiIfControllerTable_Object = MibTable
coiIfControllerTable = _CoiIfControllerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 1, 1)
)
if mibBuilder.loadTexts:
    coiIfControllerTable.setStatus("current")
_CoiIfControllerEntry_Object = MibTableRow
coiIfControllerEntry = _CoiIfControllerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 1, 1, 1)
)
coiIfControllerEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    coiIfControllerEntry.setStatus("current")


class _CoiIfControllerLoopback_Type(Integer32):
    """Custom type coiIfControllerLoopback based on Integer32"""
    defaultValue = 1

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
        *(("diagnosticLoop", 3),
          ("lineLoop", 4),
          ("noLoop", 1),
          ("otherLoop", 2))
    )


_CoiIfControllerLoopback_Type.__name__ = "Integer32"
_CoiIfControllerLoopback_Object = MibTableColumn
coiIfControllerLoopback = _CoiIfControllerLoopback_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 1, 1, 1, 1),
    _CoiIfControllerLoopback_Type()
)
coiIfControllerLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coiIfControllerLoopback.setStatus("current")


class _CoiIfControllerWavelength_Type(CoiOpticalWavelength):
    """Custom type coiIfControllerWavelength based on CoiOpticalWavelength"""
    defaultValue = 1529553


_CoiIfControllerWavelength_Object = MibTableColumn
coiIfControllerWavelength = _CoiIfControllerWavelength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 1, 1, 1, 2),
    _CoiIfControllerWavelength_Type()
)
coiIfControllerWavelength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coiIfControllerWavelength.setStatus("current")


class _CoiIfControllerLaserAdminStatus_Type(Integer32):
    """Custom type coiIfControllerLaserAdminStatus based on Integer32"""
    defaultValue = 1

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


_CoiIfControllerLaserAdminStatus_Type.__name__ = "Integer32"
_CoiIfControllerLaserAdminStatus_Object = MibTableColumn
coiIfControllerLaserAdminStatus = _CoiIfControllerLaserAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 1, 1, 1, 3),
    _CoiIfControllerLaserAdminStatus_Type()
)
coiIfControllerLaserAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coiIfControllerLaserAdminStatus.setStatus("current")


class _CoiIfControllerLaserOperStatus_Type(Integer32):
    """Custom type coiIfControllerLaserOperStatus based on Integer32"""
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


_CoiIfControllerLaserOperStatus_Type.__name__ = "Integer32"
_CoiIfControllerLaserOperStatus_Object = MibTableColumn
coiIfControllerLaserOperStatus = _CoiIfControllerLaserOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 1, 1, 1, 4),
    _CoiIfControllerLaserOperStatus_Type()
)
coiIfControllerLaserOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiIfControllerLaserOperStatus.setStatus("current")


class _CoiIfControllerOtnStatus_Type(TruthValue):
    """Custom type coiIfControllerOtnStatus based on TruthValue"""


_CoiIfControllerOtnStatus_Object = MibTableColumn
coiIfControllerOtnStatus = _CoiIfControllerOtnStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 1, 1, 1, 5),
    _CoiIfControllerOtnStatus_Type()
)
coiIfControllerOtnStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coiIfControllerOtnStatus.setStatus("current")


class _CoiIfControllerFECMode_Type(Integer32):
    """Custom type coiIfControllerFECMode based on Integer32"""
    defaultValue = 3

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
              9)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enableEnhanced", 3),
          ("enableEnhancedI4", 4),
          ("enableEnhancedI7", 5),
          ("enableEnhancedSD20", 9),
          ("enableEnhancedSD7", 8),
          ("enableHighGain", 6),
          ("enableLongHaul", 7),
          ("enableStandard", 2))
    )


_CoiIfControllerFECMode_Type.__name__ = "Integer32"
_CoiIfControllerFECMode_Object = MibTableColumn
coiIfControllerFECMode = _CoiIfControllerFECMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 1, 1, 1, 6),
    _CoiIfControllerFECMode_Type()
)
coiIfControllerFECMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coiIfControllerFECMode.setStatus("current")


class _CoiIfControllerTDCOperMode_Type(Integer32):
    """Custom type coiIfControllerTDCOperMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2))
    )


_CoiIfControllerTDCOperMode_Type.__name__ = "Integer32"
_CoiIfControllerTDCOperMode_Object = MibTableColumn
coiIfControllerTDCOperMode = _CoiIfControllerTDCOperMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 1, 1, 1, 7),
    _CoiIfControllerTDCOperMode_Type()
)
coiIfControllerTDCOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiIfControllerTDCOperMode.setStatus("current")


class _CoiIfControllerTDCOperStatus_Type(Integer32):
    """Custom type coiIfControllerTDCOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("acquiring", 2),
          ("disabled", 1),
          ("locked", 3))
    )


_CoiIfControllerTDCOperStatus_Type.__name__ = "Integer32"
_CoiIfControllerTDCOperStatus_Object = MibTableColumn
coiIfControllerTDCOperStatus = _CoiIfControllerTDCOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 1, 1, 1, 8),
    _CoiIfControllerTDCOperStatus_Type()
)
coiIfControllerTDCOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiIfControllerTDCOperStatus.setStatus("current")


class _CoiIfControllerTDCOperSetting_Type(Integer32):
    """Custom type coiIfControllerTDCOperSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2000, 2000),
    )


_CoiIfControllerTDCOperSetting_Type.__name__ = "Integer32"
_CoiIfControllerTDCOperSetting_Object = MibTableColumn
coiIfControllerTDCOperSetting = _CoiIfControllerTDCOperSetting_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 1, 1, 1, 9),
    _CoiIfControllerTDCOperSetting_Type()
)
coiIfControllerTDCOperSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiIfControllerTDCOperSetting.setStatus("current")
if mibBuilder.loadTexts:
    coiIfControllerTDCOperSetting.setUnits("ps/nm - picoseconds per nanometer")


class _CoiIfControllerPreFECBERMantissa_Type(Integer32):
    """Custom type coiIfControllerPreFECBERMantissa based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_CoiIfControllerPreFECBERMantissa_Type.__name__ = "Integer32"
_CoiIfControllerPreFECBERMantissa_Object = MibTableColumn
coiIfControllerPreFECBERMantissa = _CoiIfControllerPreFECBERMantissa_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 1, 1, 1, 10),
    _CoiIfControllerPreFECBERMantissa_Type()
)
coiIfControllerPreFECBERMantissa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiIfControllerPreFECBERMantissa.setStatus("current")


class _CoiIfControllerPreFECBERExponent_Type(Integer32):
    """Custom type coiIfControllerPreFECBERExponent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-30, 0),
    )


_CoiIfControllerPreFECBERExponent_Type.__name__ = "Integer32"
_CoiIfControllerPreFECBERExponent_Object = MibTableColumn
coiIfControllerPreFECBERExponent = _CoiIfControllerPreFECBERExponent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 1, 1, 1, 11),
    _CoiIfControllerPreFECBERExponent_Type()
)
coiIfControllerPreFECBERExponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiIfControllerPreFECBERExponent.setStatus("current")


class _CoiIfControllerQFactor_Type(Integer32):
    """Custom type coiIfControllerQFactor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_CoiIfControllerQFactor_Type.__name__ = "Integer32"
_CoiIfControllerQFactor_Object = MibTableColumn
coiIfControllerQFactor = _CoiIfControllerQFactor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 1, 1, 1, 12),
    _CoiIfControllerQFactor_Type()
)
coiIfControllerQFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiIfControllerQFactor.setStatus("current")
if mibBuilder.loadTexts:
    coiIfControllerQFactor.setUnits("one hundredths of a dB")


class _CoiIfControllerQMargin_Type(Integer32):
    """Custom type coiIfControllerQMargin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_CoiIfControllerQMargin_Type.__name__ = "Integer32"
_CoiIfControllerQMargin_Object = MibTableColumn
coiIfControllerQMargin = _CoiIfControllerQMargin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 1, 1, 1, 13),
    _CoiIfControllerQMargin_Type()
)
coiIfControllerQMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiIfControllerQMargin.setStatus("current")
if mibBuilder.loadTexts:
    coiIfControllerQMargin.setUnits("one hundredths of a dBQ")


class _CoiIfControllerOTNValidIntervals_Type(Unsigned32):
    """Custom type coiIfControllerOTNValidIntervals based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_CoiIfControllerOTNValidIntervals_Type.__name__ = "Unsigned32"
_CoiIfControllerOTNValidIntervals_Object = MibTableColumn
coiIfControllerOTNValidIntervals = _CoiIfControllerOTNValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 1, 1, 1, 14),
    _CoiIfControllerOTNValidIntervals_Type()
)
coiIfControllerOTNValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiIfControllerOTNValidIntervals.setStatus("current")


class _CoiIfControllerFECValidIntervals_Type(Unsigned32):
    """Custom type coiIfControllerFECValidIntervals based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_CoiIfControllerFECValidIntervals_Type.__name__ = "Unsigned32"
_CoiIfControllerFECValidIntervals_Object = MibTableColumn
coiIfControllerFECValidIntervals = _CoiIfControllerFECValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 1, 1, 1, 15),
    _CoiIfControllerFECValidIntervals_Type()
)
coiIfControllerFECValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiIfControllerFECValidIntervals.setStatus("current")


class _CoiOtnIfOTUStatus_Type(Bits):
    """Custom type coiOtnIfOTUStatus based on Bits"""
    namedValues = NamedValues(
        *(("ais", 6),
          ("bdi", 4),
          ("fecMismatch", 7),
          ("fecUncorrectedWord", 8),
          ("lof", 2),
          ("lom", 3),
          ("los", 1),
          ("noDefect", 0),
          ("tim", 5))
    )

_CoiOtnIfOTUStatus_Type.__name__ = "Bits"
_CoiOtnIfOTUStatus_Object = MibTableColumn
coiOtnIfOTUStatus = _CoiOtnIfOTUStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 1, 1, 1, 16),
    _CoiOtnIfOTUStatus_Type()
)
coiOtnIfOTUStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOtnIfOTUStatus.setStatus("current")


class _CoiOtnIfODUStatus_Type(Bits):
    """Custom type coiOtnIfODUStatus based on Bits"""
    namedValues = NamedValues(
        *(("ais", 5),
          ("bdi", 4),
          ("lck", 2),
          ("noDefect", 0),
          ("oci", 1),
          ("tim", 3))
    )

_CoiOtnIfODUStatus_Type.__name__ = "Bits"
_CoiOtnIfODUStatus_Object = MibTableColumn
coiOtnIfODUStatus = _CoiOtnIfODUStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 1, 1, 1, 17),
    _CoiOtnIfODUStatus_Type()
)
coiOtnIfODUStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOtnIfODUStatus.setStatus("current")
_CoiDwdmIfOtn_ObjectIdentity = ObjectIdentity
coiDwdmIfOtn = _CoiDwdmIfOtn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 2)
)
_CoiOtnNearEndThresholdsTable_Object = MibTable
coiOtnNearEndThresholdsTable = _CoiOtnNearEndThresholdsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 2, 1)
)
if mibBuilder.loadTexts:
    coiOtnNearEndThresholdsTable.setStatus("current")
_CoiOtnNearEndThresholdsEntry_Object = MibTableRow
coiOtnNearEndThresholdsEntry = _CoiOtnNearEndThresholdsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 2, 1, 1)
)
coiOtnNearEndThresholdsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-OTN-IF-MIB", "coiOtnNearEndThreshIntervalType"),
    (0, "CISCO-OTN-IF-MIB", "coiOtnNearEndThreshMonType"),
    (0, "CISCO-OTN-IF-MIB", "coiOtnNearEndThresholdType"),
)
if mibBuilder.loadTexts:
    coiOtnNearEndThresholdsEntry.setStatus("current")
_CoiOtnNearEndThreshIntervalType_Type = CoiIntervalType
_CoiOtnNearEndThreshIntervalType_Object = MibTableColumn
coiOtnNearEndThreshIntervalType = _CoiOtnNearEndThreshIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 2, 1, 1, 1),
    _CoiOtnNearEndThreshIntervalType_Type()
)
coiOtnNearEndThreshIntervalType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coiOtnNearEndThreshIntervalType.setStatus("current")
_CoiOtnNearEndThreshMonType_Type = CoiMonitorType
_CoiOtnNearEndThreshMonType_Object = MibTableColumn
coiOtnNearEndThreshMonType = _CoiOtnNearEndThreshMonType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 2, 1, 1, 2),
    _CoiOtnNearEndThreshMonType_Type()
)
coiOtnNearEndThreshMonType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coiOtnNearEndThreshMonType.setStatus("current")
_CoiOtnNearEndThresholdType_Type = CoiOtnThresholdType
_CoiOtnNearEndThresholdType_Object = MibTableColumn
coiOtnNearEndThresholdType = _CoiOtnNearEndThresholdType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 2, 1, 1, 3),
    _CoiOtnNearEndThresholdType_Type()
)
coiOtnNearEndThresholdType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coiOtnNearEndThresholdType.setStatus("current")
_CoiOtnNearEndThreshValue_Type = Unsigned32
_CoiOtnNearEndThreshValue_Object = MibTableColumn
coiOtnNearEndThreshValue = _CoiOtnNearEndThreshValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 2, 1, 1, 4),
    _CoiOtnNearEndThreshValue_Type()
)
coiOtnNearEndThreshValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    coiOtnNearEndThreshValue.setStatus("current")


class _CoiOtnNearEndThreshStorageType_Type(StorageType):
    """Custom type coiOtnNearEndThreshStorageType based on StorageType"""


_CoiOtnNearEndThreshStorageType_Object = MibTableColumn
coiOtnNearEndThreshStorageType = _CoiOtnNearEndThreshStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 2, 1, 1, 5),
    _CoiOtnNearEndThreshStorageType_Type()
)
coiOtnNearEndThreshStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    coiOtnNearEndThreshStorageType.setStatus("current")
_CoiOtnNearEndThreshStatus_Type = RowStatus
_CoiOtnNearEndThreshStatus_Object = MibTableColumn
coiOtnNearEndThreshStatus = _CoiOtnNearEndThreshStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 2, 1, 1, 6),
    _CoiOtnNearEndThreshStatus_Type()
)
coiOtnNearEndThreshStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    coiOtnNearEndThreshStatus.setStatus("current")
_CoiOtnFarEndThresholdsTable_Object = MibTable
coiOtnFarEndThresholdsTable = _CoiOtnFarEndThresholdsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 2, 2)
)
if mibBuilder.loadTexts:
    coiOtnFarEndThresholdsTable.setStatus("current")
_CoiOtnFarEndThresholdsEntry_Object = MibTableRow
coiOtnFarEndThresholdsEntry = _CoiOtnFarEndThresholdsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 2, 2, 1)
)
coiOtnFarEndThresholdsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-OTN-IF-MIB", "coiOtnFarEndThreshIntervalType"),
    (0, "CISCO-OTN-IF-MIB", "coiOtnFarEndThreshMonType"),
    (0, "CISCO-OTN-IF-MIB", "coiOtnFarEndThresholdType"),
)
if mibBuilder.loadTexts:
    coiOtnFarEndThresholdsEntry.setStatus("current")
_CoiOtnFarEndThreshIntervalType_Type = CoiIntervalType
_CoiOtnFarEndThreshIntervalType_Object = MibTableColumn
coiOtnFarEndThreshIntervalType = _CoiOtnFarEndThreshIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 2, 2, 1, 1),
    _CoiOtnFarEndThreshIntervalType_Type()
)
coiOtnFarEndThreshIntervalType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coiOtnFarEndThreshIntervalType.setStatus("current")
_CoiOtnFarEndThreshMonType_Type = CoiMonitorType
_CoiOtnFarEndThreshMonType_Object = MibTableColumn
coiOtnFarEndThreshMonType = _CoiOtnFarEndThreshMonType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 2, 2, 1, 2),
    _CoiOtnFarEndThreshMonType_Type()
)
coiOtnFarEndThreshMonType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coiOtnFarEndThreshMonType.setStatus("current")
_CoiOtnFarEndThresholdType_Type = CoiOtnThresholdType
_CoiOtnFarEndThresholdType_Object = MibTableColumn
coiOtnFarEndThresholdType = _CoiOtnFarEndThresholdType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 2, 2, 1, 3),
    _CoiOtnFarEndThresholdType_Type()
)
coiOtnFarEndThresholdType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coiOtnFarEndThresholdType.setStatus("current")
_CoiOtnFarEndThreshValue_Type = Unsigned32
_CoiOtnFarEndThreshValue_Object = MibTableColumn
coiOtnFarEndThreshValue = _CoiOtnFarEndThreshValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 2, 2, 1, 4),
    _CoiOtnFarEndThreshValue_Type()
)
coiOtnFarEndThreshValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    coiOtnFarEndThreshValue.setStatus("current")


class _CoiOtnFarEndThreshStorageType_Type(StorageType):
    """Custom type coiOtnFarEndThreshStorageType based on StorageType"""


_CoiOtnFarEndThreshStorageType_Object = MibTableColumn
coiOtnFarEndThreshStorageType = _CoiOtnFarEndThreshStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 2, 2, 1, 5),
    _CoiOtnFarEndThreshStorageType_Type()
)
coiOtnFarEndThreshStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    coiOtnFarEndThreshStorageType.setStatus("current")
_CoiOtnFarEndThreshStatus_Type = RowStatus
_CoiOtnFarEndThreshStatus_Object = MibTableColumn
coiOtnFarEndThreshStatus = _CoiOtnFarEndThreshStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 2, 2, 1, 6),
    _CoiOtnFarEndThreshStatus_Type()
)
coiOtnFarEndThreshStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    coiOtnFarEndThreshStatus.setStatus("current")
_CoiOtnNearEndCurrentTable_Object = MibTable
coiOtnNearEndCurrentTable = _CoiOtnNearEndCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 2, 3)
)
if mibBuilder.loadTexts:
    coiOtnNearEndCurrentTable.setStatus("current")
_CoiOtnNearEndCurrentEntry_Object = MibTableRow
coiOtnNearEndCurrentEntry = _CoiOtnNearEndCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 2, 3, 1)
)
coiOtnNearEndCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-OTN-IF-MIB", "coiOtnNearEndCurIntervalType"),
    (0, "CISCO-OTN-IF-MIB", "coiOtnNearEndCurrentMonType"),
)
if mibBuilder.loadTexts:
    coiOtnNearEndCurrentEntry.setStatus("current")
_CoiOtnNearEndCurIntervalType_Type = CoiIntervalType
_CoiOtnNearEndCurIntervalType_Object = MibTableColumn
coiOtnNearEndCurIntervalType = _CoiOtnNearEndCurIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 2, 3, 1, 1),
    _CoiOtnNearEndCurIntervalType_Type()
)
coiOtnNearEndCurIntervalType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coiOtnNearEndCurIntervalType.setStatus("current")
_CoiOtnNearEndCurrentMonType_Type = CoiMonitorType
_CoiOtnNearEndCurrentMonType_Object = MibTableColumn
coiOtnNearEndCurrentMonType = _CoiOtnNearEndCurrentMonType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 2, 3, 1, 2),
    _CoiOtnNearEndCurrentMonType_Type()
)
coiOtnNearEndCurrentMonType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coiOtnNearEndCurrentMonType.setStatus("current")
_CoiOtnNearEndCurrentFCs_Type = Counter32
_CoiOtnNearEndCurrentFCs_Object = MibTableColumn
coiOtnNearEndCurrentFCs = _CoiOtnNearEndCurrentFCs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 2, 3, 1, 3),
    _CoiOtnNearEndCurrentFCs_Type()
)
coiOtnNearEndCurrentFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOtnNearEndCurrentFCs.setStatus("current")
_CoiOtnNearEndCurrentESs_Type = Counter32
_CoiOtnNearEndCurrentESs_Object = MibTableColumn
coiOtnNearEndCurrentESs = _CoiOtnNearEndCurrentESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 2, 3, 1, 4),
    _CoiOtnNearEndCurrentESs_Type()
)
coiOtnNearEndCurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOtnNearEndCurrentESs.setStatus("current")
_CoiOtnNearEndCurrentSESs_Type = Counter32
_CoiOtnNearEndCurrentSESs_Object = MibTableColumn
coiOtnNearEndCurrentSESs = _CoiOtnNearEndCurrentSESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 2, 3, 1, 5),
    _CoiOtnNearEndCurrentSESs_Type()
)
coiOtnNearEndCurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOtnNearEndCurrentSESs.setStatus("current")
_CoiOtnNearEndCurrentUASs_Type = Counter32
_CoiOtnNearEndCurrentUASs_Object = MibTableColumn
coiOtnNearEndCurrentUASs = _CoiOtnNearEndCurrentUASs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 2, 3, 1, 6),
    _CoiOtnNearEndCurrentUASs_Type()
)
coiOtnNearEndCurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOtnNearEndCurrentUASs.setStatus("current")
_CoiOtnNearEndCurrentBBEs_Type = Counter32
_CoiOtnNearEndCurrentBBEs_Object = MibTableColumn
coiOtnNearEndCurrentBBEs = _CoiOtnNearEndCurrentBBEs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 2, 3, 1, 7),
    _CoiOtnNearEndCurrentBBEs_Type()
)
coiOtnNearEndCurrentBBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOtnNearEndCurrentBBEs.setStatus("current")
_CoiOtnNearEndCurrentESRs_Type = Counter32
_CoiOtnNearEndCurrentESRs_Object = MibTableColumn
coiOtnNearEndCurrentESRs = _CoiOtnNearEndCurrentESRs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 2, 3, 1, 8),
    _CoiOtnNearEndCurrentESRs_Type()
)
coiOtnNearEndCurrentESRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOtnNearEndCurrentESRs.setStatus("current")
_CoiOtnNearEndCurrentSESRs_Type = Counter32
_CoiOtnNearEndCurrentSESRs_Object = MibTableColumn
coiOtnNearEndCurrentSESRs = _CoiOtnNearEndCurrentSESRs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 2, 3, 1, 9),
    _CoiOtnNearEndCurrentSESRs_Type()
)
coiOtnNearEndCurrentSESRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOtnNearEndCurrentSESRs.setStatus("current")
_CoiOtnNearEndCurrentBBERs_Type = Counter32
_CoiOtnNearEndCurrentBBERs_Object = MibTableColumn
coiOtnNearEndCurrentBBERs = _CoiOtnNearEndCurrentBBERs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 2, 3, 1, 10),
    _CoiOtnNearEndCurrentBBERs_Type()
)
coiOtnNearEndCurrentBBERs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOtnNearEndCurrentBBERs.setStatus("current")
_CoiOtnFarEndCurrentTable_Object = MibTable
coiOtnFarEndCurrentTable = _CoiOtnFarEndCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 2, 4)
)
if mibBuilder.loadTexts:
    coiOtnFarEndCurrentTable.setStatus("current")
_CoiOtnFarEndCurrentEntry_Object = MibTableRow
coiOtnFarEndCurrentEntry = _CoiOtnFarEndCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 2, 4, 1)
)
coiOtnFarEndCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-OTN-IF-MIB", "coiOtnFarEndCurIntervalType"),
    (0, "CISCO-OTN-IF-MIB", "coiOtnFarEndCurrentMonType"),
)
if mibBuilder.loadTexts:
    coiOtnFarEndCurrentEntry.setStatus("current")
_CoiOtnFarEndCurIntervalType_Type = CoiIntervalType
_CoiOtnFarEndCurIntervalType_Object = MibTableColumn
coiOtnFarEndCurIntervalType = _CoiOtnFarEndCurIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 2, 4, 1, 1),
    _CoiOtnFarEndCurIntervalType_Type()
)
coiOtnFarEndCurIntervalType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coiOtnFarEndCurIntervalType.setStatus("current")
_CoiOtnFarEndCurrentMonType_Type = CoiMonitorType
_CoiOtnFarEndCurrentMonType_Object = MibTableColumn
coiOtnFarEndCurrentMonType = _CoiOtnFarEndCurrentMonType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 2, 4, 1, 2),
    _CoiOtnFarEndCurrentMonType_Type()
)
coiOtnFarEndCurrentMonType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coiOtnFarEndCurrentMonType.setStatus("current")
_CoiOtnFarEndCurrentFCs_Type = Counter32
_CoiOtnFarEndCurrentFCs_Object = MibTableColumn
coiOtnFarEndCurrentFCs = _CoiOtnFarEndCurrentFCs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 2, 4, 1, 3),
    _CoiOtnFarEndCurrentFCs_Type()
)
coiOtnFarEndCurrentFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOtnFarEndCurrentFCs.setStatus("current")
_CoiOtnFarEndCurrentESs_Type = Counter32
_CoiOtnFarEndCurrentESs_Object = MibTableColumn
coiOtnFarEndCurrentESs = _CoiOtnFarEndCurrentESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 2, 4, 1, 4),
    _CoiOtnFarEndCurrentESs_Type()
)
coiOtnFarEndCurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOtnFarEndCurrentESs.setStatus("current")
_CoiOtnFarEndCurrentSESs_Type = Counter32
_CoiOtnFarEndCurrentSESs_Object = MibTableColumn
coiOtnFarEndCurrentSESs = _CoiOtnFarEndCurrentSESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 2, 4, 1, 5),
    _CoiOtnFarEndCurrentSESs_Type()
)
coiOtnFarEndCurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOtnFarEndCurrentSESs.setStatus("current")
_CoiOtnFarEndCurrentUASs_Type = Counter32
_CoiOtnFarEndCurrentUASs_Object = MibTableColumn
coiOtnFarEndCurrentUASs = _CoiOtnFarEndCurrentUASs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 2, 4, 1, 6),
    _CoiOtnFarEndCurrentUASs_Type()
)
coiOtnFarEndCurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOtnFarEndCurrentUASs.setStatus("current")
_CoiOtnFarEndCurrentBBEs_Type = Counter32
_CoiOtnFarEndCurrentBBEs_Object = MibTableColumn
coiOtnFarEndCurrentBBEs = _CoiOtnFarEndCurrentBBEs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 2, 4, 1, 7),
    _CoiOtnFarEndCurrentBBEs_Type()
)
coiOtnFarEndCurrentBBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOtnFarEndCurrentBBEs.setStatus("current")
_CoiOtnFarEndCurrentESRs_Type = Counter32
_CoiOtnFarEndCurrentESRs_Object = MibTableColumn
coiOtnFarEndCurrentESRs = _CoiOtnFarEndCurrentESRs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 2, 4, 1, 8),
    _CoiOtnFarEndCurrentESRs_Type()
)
coiOtnFarEndCurrentESRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOtnFarEndCurrentESRs.setStatus("current")
_CoiOtnFarEndCurrentSESRs_Type = Counter32
_CoiOtnFarEndCurrentSESRs_Object = MibTableColumn
coiOtnFarEndCurrentSESRs = _CoiOtnFarEndCurrentSESRs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 2, 4, 1, 9),
    _CoiOtnFarEndCurrentSESRs_Type()
)
coiOtnFarEndCurrentSESRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOtnFarEndCurrentSESRs.setStatus("current")
_CoiOtnFarEndCurrentBBERs_Type = Counter32
_CoiOtnFarEndCurrentBBERs_Object = MibTableColumn
coiOtnFarEndCurrentBBERs = _CoiOtnFarEndCurrentBBERs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 2, 4, 1, 10),
    _CoiOtnFarEndCurrentBBERs_Type()
)
coiOtnFarEndCurrentBBERs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOtnFarEndCurrentBBERs.setStatus("current")
_CoiOtnNearEndIntervalTable_Object = MibTable
coiOtnNearEndIntervalTable = _CoiOtnNearEndIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 2, 5)
)
if mibBuilder.loadTexts:
    coiOtnNearEndIntervalTable.setStatus("current")
_CoiOtnNearEndIntervalEntry_Object = MibTableRow
coiOtnNearEndIntervalEntry = _CoiOtnNearEndIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 2, 5, 1)
)
coiOtnNearEndIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-OTN-IF-MIB", "coiOtnNearEndIntervalType"),
    (0, "CISCO-OTN-IF-MIB", "coiOtnNearEndIntervalMonType"),
    (0, "CISCO-OTN-IF-MIB", "coiOtnNearEndIntervalNum"),
)
if mibBuilder.loadTexts:
    coiOtnNearEndIntervalEntry.setStatus("current")
_CoiOtnNearEndIntervalType_Type = CoiIntervalType
_CoiOtnNearEndIntervalType_Object = MibTableColumn
coiOtnNearEndIntervalType = _CoiOtnNearEndIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 2, 5, 1, 1),
    _CoiOtnNearEndIntervalType_Type()
)
coiOtnNearEndIntervalType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coiOtnNearEndIntervalType.setStatus("current")
_CoiOtnNearEndIntervalMonType_Type = CoiMonitorType
_CoiOtnNearEndIntervalMonType_Object = MibTableColumn
coiOtnNearEndIntervalMonType = _CoiOtnNearEndIntervalMonType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 2, 5, 1, 2),
    _CoiOtnNearEndIntervalMonType_Type()
)
coiOtnNearEndIntervalMonType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coiOtnNearEndIntervalMonType.setStatus("current")


class _CoiOtnNearEndIntervalNum_Type(Integer32):
    """Custom type coiOtnNearEndIntervalNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_CoiOtnNearEndIntervalNum_Type.__name__ = "Integer32"
_CoiOtnNearEndIntervalNum_Object = MibTableColumn
coiOtnNearEndIntervalNum = _CoiOtnNearEndIntervalNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 2, 5, 1, 3),
    _CoiOtnNearEndIntervalNum_Type()
)
coiOtnNearEndIntervalNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coiOtnNearEndIntervalNum.setStatus("current")
_CoiOtnNearEndIntervalFCs_Type = Counter32
_CoiOtnNearEndIntervalFCs_Object = MibTableColumn
coiOtnNearEndIntervalFCs = _CoiOtnNearEndIntervalFCs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 2, 5, 1, 4),
    _CoiOtnNearEndIntervalFCs_Type()
)
coiOtnNearEndIntervalFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOtnNearEndIntervalFCs.setStatus("current")
_CoiOtnNearEndIntervalESs_Type = Counter32
_CoiOtnNearEndIntervalESs_Object = MibTableColumn
coiOtnNearEndIntervalESs = _CoiOtnNearEndIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 2, 5, 1, 5),
    _CoiOtnNearEndIntervalESs_Type()
)
coiOtnNearEndIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOtnNearEndIntervalESs.setStatus("current")
_CoiOtnNearEndIntervalSESs_Type = Counter32
_CoiOtnNearEndIntervalSESs_Object = MibTableColumn
coiOtnNearEndIntervalSESs = _CoiOtnNearEndIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 2, 5, 1, 6),
    _CoiOtnNearEndIntervalSESs_Type()
)
coiOtnNearEndIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOtnNearEndIntervalSESs.setStatus("current")
_CoiOtnNearEndIntervalUASs_Type = Counter32
_CoiOtnNearEndIntervalUASs_Object = MibTableColumn
coiOtnNearEndIntervalUASs = _CoiOtnNearEndIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 2, 5, 1, 7),
    _CoiOtnNearEndIntervalUASs_Type()
)
coiOtnNearEndIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOtnNearEndIntervalUASs.setStatus("current")
_CoiOtnNearEndIntervalBBEs_Type = Counter32
_CoiOtnNearEndIntervalBBEs_Object = MibTableColumn
coiOtnNearEndIntervalBBEs = _CoiOtnNearEndIntervalBBEs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 2, 5, 1, 8),
    _CoiOtnNearEndIntervalBBEs_Type()
)
coiOtnNearEndIntervalBBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOtnNearEndIntervalBBEs.setStatus("current")
_CoiOtnNearEndIntervalESRs_Type = Counter32
_CoiOtnNearEndIntervalESRs_Object = MibTableColumn
coiOtnNearEndIntervalESRs = _CoiOtnNearEndIntervalESRs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 2, 5, 1, 9),
    _CoiOtnNearEndIntervalESRs_Type()
)
coiOtnNearEndIntervalESRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOtnNearEndIntervalESRs.setStatus("current")
_CoiOtnNearEndIntervalSESRs_Type = Counter32
_CoiOtnNearEndIntervalSESRs_Object = MibTableColumn
coiOtnNearEndIntervalSESRs = _CoiOtnNearEndIntervalSESRs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 2, 5, 1, 10),
    _CoiOtnNearEndIntervalSESRs_Type()
)
coiOtnNearEndIntervalSESRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOtnNearEndIntervalSESRs.setStatus("current")
_CoiOtnNearEndIntervalBBERs_Type = Counter32
_CoiOtnNearEndIntervalBBERs_Object = MibTableColumn
coiOtnNearEndIntervalBBERs = _CoiOtnNearEndIntervalBBERs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 2, 5, 1, 11),
    _CoiOtnNearEndIntervalBBERs_Type()
)
coiOtnNearEndIntervalBBERs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOtnNearEndIntervalBBERs.setStatus("current")
_CoiOtnNearEndIntervalValidData_Type = TruthValue
_CoiOtnNearEndIntervalValidData_Object = MibTableColumn
coiOtnNearEndIntervalValidData = _CoiOtnNearEndIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 2, 5, 1, 12),
    _CoiOtnNearEndIntervalValidData_Type()
)
coiOtnNearEndIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOtnNearEndIntervalValidData.setStatus("current")
_CoiOtnFarEndIntervalTable_Object = MibTable
coiOtnFarEndIntervalTable = _CoiOtnFarEndIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 2, 6)
)
if mibBuilder.loadTexts:
    coiOtnFarEndIntervalTable.setStatus("current")
_CoiOtnFarEndIntervalEntry_Object = MibTableRow
coiOtnFarEndIntervalEntry = _CoiOtnFarEndIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 2, 6, 1)
)
coiOtnFarEndIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-OTN-IF-MIB", "coiOtnFarEndIntervalType"),
    (0, "CISCO-OTN-IF-MIB", "coiOtnFarEndIntervalMonType"),
    (0, "CISCO-OTN-IF-MIB", "coiOtnFarEndIntervalNum"),
)
if mibBuilder.loadTexts:
    coiOtnFarEndIntervalEntry.setStatus("current")
_CoiOtnFarEndIntervalType_Type = CoiIntervalType
_CoiOtnFarEndIntervalType_Object = MibTableColumn
coiOtnFarEndIntervalType = _CoiOtnFarEndIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 2, 6, 1, 1),
    _CoiOtnFarEndIntervalType_Type()
)
coiOtnFarEndIntervalType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coiOtnFarEndIntervalType.setStatus("current")
_CoiOtnFarEndIntervalMonType_Type = CoiMonitorType
_CoiOtnFarEndIntervalMonType_Object = MibTableColumn
coiOtnFarEndIntervalMonType = _CoiOtnFarEndIntervalMonType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 2, 6, 1, 2),
    _CoiOtnFarEndIntervalMonType_Type()
)
coiOtnFarEndIntervalMonType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coiOtnFarEndIntervalMonType.setStatus("current")


class _CoiOtnFarEndIntervalNum_Type(Integer32):
    """Custom type coiOtnFarEndIntervalNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_CoiOtnFarEndIntervalNum_Type.__name__ = "Integer32"
_CoiOtnFarEndIntervalNum_Object = MibTableColumn
coiOtnFarEndIntervalNum = _CoiOtnFarEndIntervalNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 2, 6, 1, 3),
    _CoiOtnFarEndIntervalNum_Type()
)
coiOtnFarEndIntervalNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coiOtnFarEndIntervalNum.setStatus("current")
_CoiOtnFarEndIntervalFCs_Type = Counter32
_CoiOtnFarEndIntervalFCs_Object = MibTableColumn
coiOtnFarEndIntervalFCs = _CoiOtnFarEndIntervalFCs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 2, 6, 1, 4),
    _CoiOtnFarEndIntervalFCs_Type()
)
coiOtnFarEndIntervalFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOtnFarEndIntervalFCs.setStatus("current")
_CoiOtnFarEndIntervalESs_Type = Counter32
_CoiOtnFarEndIntervalESs_Object = MibTableColumn
coiOtnFarEndIntervalESs = _CoiOtnFarEndIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 2, 6, 1, 5),
    _CoiOtnFarEndIntervalESs_Type()
)
coiOtnFarEndIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOtnFarEndIntervalESs.setStatus("current")
_CoiOtnFarEndIntervalSESs_Type = Counter32
_CoiOtnFarEndIntervalSESs_Object = MibTableColumn
coiOtnFarEndIntervalSESs = _CoiOtnFarEndIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 2, 6, 1, 6),
    _CoiOtnFarEndIntervalSESs_Type()
)
coiOtnFarEndIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOtnFarEndIntervalSESs.setStatus("current")
_CoiOtnFarEndIntervalUASs_Type = Counter32
_CoiOtnFarEndIntervalUASs_Object = MibTableColumn
coiOtnFarEndIntervalUASs = _CoiOtnFarEndIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 2, 6, 1, 7),
    _CoiOtnFarEndIntervalUASs_Type()
)
coiOtnFarEndIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOtnFarEndIntervalUASs.setStatus("current")
_CoiOtnFarEndIntervalBBEs_Type = Counter32
_CoiOtnFarEndIntervalBBEs_Object = MibTableColumn
coiOtnFarEndIntervalBBEs = _CoiOtnFarEndIntervalBBEs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 2, 6, 1, 8),
    _CoiOtnFarEndIntervalBBEs_Type()
)
coiOtnFarEndIntervalBBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOtnFarEndIntervalBBEs.setStatus("current")
_CoiOtnFarEndIntervalESRs_Type = Counter32
_CoiOtnFarEndIntervalESRs_Object = MibTableColumn
coiOtnFarEndIntervalESRs = _CoiOtnFarEndIntervalESRs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 2, 6, 1, 9),
    _CoiOtnFarEndIntervalESRs_Type()
)
coiOtnFarEndIntervalESRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOtnFarEndIntervalESRs.setStatus("current")
_CoiOtnFarEndIntervalSESRs_Type = Counter32
_CoiOtnFarEndIntervalSESRs_Object = MibTableColumn
coiOtnFarEndIntervalSESRs = _CoiOtnFarEndIntervalSESRs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 2, 6, 1, 10),
    _CoiOtnFarEndIntervalSESRs_Type()
)
coiOtnFarEndIntervalSESRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOtnFarEndIntervalSESRs.setStatus("current")
_CoiOtnFarEndIntervalBBERs_Type = Counter32
_CoiOtnFarEndIntervalBBERs_Object = MibTableColumn
coiOtnFarEndIntervalBBERs = _CoiOtnFarEndIntervalBBERs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 2, 6, 1, 11),
    _CoiOtnFarEndIntervalBBERs_Type()
)
coiOtnFarEndIntervalBBERs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOtnFarEndIntervalBBERs.setStatus("current")
_CoiOtnFarEndIntervalValidData_Type = TruthValue
_CoiOtnFarEndIntervalValidData_Object = MibTableColumn
coiOtnFarEndIntervalValidData = _CoiOtnFarEndIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 2, 6, 1, 12),
    _CoiOtnFarEndIntervalValidData_Type()
)
coiOtnFarEndIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiOtnFarEndIntervalValidData.setStatus("current")
_CoiOtnIfNotifEnabled_Type = TruthValue
_CoiOtnIfNotifEnabled_Object = MibScalar
coiOtnIfNotifEnabled = _CoiOtnIfNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 2, 7),
    _CoiOtnIfNotifEnabled_Type()
)
coiOtnIfNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coiOtnIfNotifEnabled.setStatus("current")
_CoiDwdmIfFEC_ObjectIdentity = ObjectIdentity
coiDwdmIfFEC = _CoiDwdmIfFEC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 3)
)
_CoiFECThresholdsTable_Object = MibTable
coiFECThresholdsTable = _CoiFECThresholdsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 3, 1)
)
if mibBuilder.loadTexts:
    coiFECThresholdsTable.setStatus("current")
_CoiFECThresholdsEntry_Object = MibTableRow
coiFECThresholdsEntry = _CoiFECThresholdsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 3, 1, 1)
)
coiFECThresholdsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-OTN-IF-MIB", "coiFECThreshIntervalType"),
    (0, "CISCO-OTN-IF-MIB", "coiFECThreshType"),
)
if mibBuilder.loadTexts:
    coiFECThresholdsEntry.setStatus("current")
_CoiFECThreshIntervalType_Type = CoiIntervalType
_CoiFECThreshIntervalType_Object = MibTableColumn
coiFECThreshIntervalType = _CoiFECThreshIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 3, 1, 1, 1),
    _CoiFECThreshIntervalType_Type()
)
coiFECThreshIntervalType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coiFECThreshIntervalType.setStatus("current")


class _CoiFECThreshType_Type(Integer32):
    """Custom type coiFECThreshType based on Integer32"""
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
        *(("bitErrCor", 1),
          ("byteErrcor", 2),
          ("oneErrDet", 4),
          ("unCorWords", 5),
          ("zeroErrDet", 3))
    )


_CoiFECThreshType_Type.__name__ = "Integer32"
_CoiFECThreshType_Object = MibTableColumn
coiFECThreshType = _CoiFECThreshType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 3, 1, 1, 2),
    _CoiFECThreshType_Type()
)
coiFECThreshType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coiFECThreshType.setStatus("current")
_CoiFECThreshValue_Type = Unsigned32
_CoiFECThreshValue_Object = MibTableColumn
coiFECThreshValue = _CoiFECThreshValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 3, 1, 1, 3),
    _CoiFECThreshValue_Type()
)
coiFECThreshValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    coiFECThreshValue.setStatus("current")


class _CoiFECThreshStorageType_Type(StorageType):
    """Custom type coiFECThreshStorageType based on StorageType"""


_CoiFECThreshStorageType_Object = MibTableColumn
coiFECThreshStorageType = _CoiFECThreshStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 3, 1, 1, 4),
    _CoiFECThreshStorageType_Type()
)
coiFECThreshStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    coiFECThreshStorageType.setStatus("current")
_CoiFECThreshStatus_Type = RowStatus
_CoiFECThreshStatus_Object = MibTableColumn
coiFECThreshStatus = _CoiFECThreshStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 3, 1, 1, 5),
    _CoiFECThreshStatus_Type()
)
coiFECThreshStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    coiFECThreshStatus.setStatus("current")
_CoiFECCurrentTable_Object = MibTable
coiFECCurrentTable = _CoiFECCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 3, 2)
)
if mibBuilder.loadTexts:
    coiFECCurrentTable.setStatus("current")
_CoiFECCurrentEntry_Object = MibTableRow
coiFECCurrentEntry = _CoiFECCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 3, 2, 1)
)
coiFECCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-OTN-IF-MIB", "coiFECCurIntervalType"),
)
if mibBuilder.loadTexts:
    coiFECCurrentEntry.setStatus("current")
_CoiFECCurIntervalType_Type = CoiIntervalType
_CoiFECCurIntervalType_Object = MibTableColumn
coiFECCurIntervalType = _CoiFECCurIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 3, 2, 1, 1),
    _CoiFECCurIntervalType_Type()
)
coiFECCurIntervalType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coiFECCurIntervalType.setStatus("current")
_CoiFECCurrentCorBitErrs_Type = Counter64
_CoiFECCurrentCorBitErrs_Object = MibTableColumn
coiFECCurrentCorBitErrs = _CoiFECCurrentCorBitErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 3, 2, 1, 2),
    _CoiFECCurrentCorBitErrs_Type()
)
coiFECCurrentCorBitErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFECCurrentCorBitErrs.setStatus("current")
_CoiFECCurrentCorByteErrs_Type = Counter64
_CoiFECCurrentCorByteErrs_Object = MibTableColumn
coiFECCurrentCorByteErrs = _CoiFECCurrentCorByteErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 3, 2, 1, 3),
    _CoiFECCurrentCorByteErrs_Type()
)
coiFECCurrentCorByteErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFECCurrentCorByteErrs.setStatus("current")
_CoiFECCurrentDetZeroErrs_Type = Counter64
_CoiFECCurrentDetZeroErrs_Object = MibTableColumn
coiFECCurrentDetZeroErrs = _CoiFECCurrentDetZeroErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 3, 2, 1, 4),
    _CoiFECCurrentDetZeroErrs_Type()
)
coiFECCurrentDetZeroErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFECCurrentDetZeroErrs.setStatus("current")
_CoiFECCurrentDetOneErrs_Type = Counter64
_CoiFECCurrentDetOneErrs_Object = MibTableColumn
coiFECCurrentDetOneErrs = _CoiFECCurrentDetOneErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 3, 2, 1, 5),
    _CoiFECCurrentDetOneErrs_Type()
)
coiFECCurrentDetOneErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFECCurrentDetOneErrs.setStatus("current")
_CoiFECCurrentUncorWords_Type = Counter64
_CoiFECCurrentUncorWords_Object = MibTableColumn
coiFECCurrentUncorWords = _CoiFECCurrentUncorWords_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 3, 2, 1, 6),
    _CoiFECCurrentUncorWords_Type()
)
coiFECCurrentUncorWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFECCurrentUncorWords.setStatus("current")
_CoiFECCurrentPreFECMin_Type = SnmpAdminString
_CoiFECCurrentPreFECMin_Object = MibTableColumn
coiFECCurrentPreFECMin = _CoiFECCurrentPreFECMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 3, 2, 1, 7),
    _CoiFECCurrentPreFECMin_Type()
)
coiFECCurrentPreFECMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFECCurrentPreFECMin.setStatus("current")
_CoiFECCurrentPreFECMax_Type = SnmpAdminString
_CoiFECCurrentPreFECMax_Object = MibTableColumn
coiFECCurrentPreFECMax = _CoiFECCurrentPreFECMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 3, 2, 1, 8),
    _CoiFECCurrentPreFECMax_Type()
)
coiFECCurrentPreFECMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFECCurrentPreFECMax.setStatus("current")
_CoiFECCurrentPreFECAvg_Type = SnmpAdminString
_CoiFECCurrentPreFECAvg_Object = MibTableColumn
coiFECCurrentPreFECAvg = _CoiFECCurrentPreFECAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 3, 2, 1, 9),
    _CoiFECCurrentPreFECAvg_Type()
)
coiFECCurrentPreFECAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFECCurrentPreFECAvg.setStatus("current")
_CoiFECCurrentPostFECMin_Type = SnmpAdminString
_CoiFECCurrentPostFECMin_Object = MibTableColumn
coiFECCurrentPostFECMin = _CoiFECCurrentPostFECMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 3, 2, 1, 10),
    _CoiFECCurrentPostFECMin_Type()
)
coiFECCurrentPostFECMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFECCurrentPostFECMin.setStatus("current")
_CoiFECCurrentPostFECMax_Type = SnmpAdminString
_CoiFECCurrentPostFECMax_Object = MibTableColumn
coiFECCurrentPostFECMax = _CoiFECCurrentPostFECMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 3, 2, 1, 11),
    _CoiFECCurrentPostFECMax_Type()
)
coiFECCurrentPostFECMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFECCurrentPostFECMax.setStatus("current")
_CoiFECCurrentPostFECAvg_Type = SnmpAdminString
_CoiFECCurrentPostFECAvg_Object = MibTableColumn
coiFECCurrentPostFECAvg = _CoiFECCurrentPostFECAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 3, 2, 1, 12),
    _CoiFECCurrentPostFECAvg_Type()
)
coiFECCurrentPostFECAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFECCurrentPostFECAvg.setStatus("current")
_CoiFECCurrentQFactorMin_Type = SnmpAdminString
_CoiFECCurrentQFactorMin_Object = MibTableColumn
coiFECCurrentQFactorMin = _CoiFECCurrentQFactorMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 3, 2, 1, 13),
    _CoiFECCurrentQFactorMin_Type()
)
coiFECCurrentQFactorMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFECCurrentQFactorMin.setStatus("current")
_CoiFECCurrentQFactorMax_Type = SnmpAdminString
_CoiFECCurrentQFactorMax_Object = MibTableColumn
coiFECCurrentQFactorMax = _CoiFECCurrentQFactorMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 3, 2, 1, 14),
    _CoiFECCurrentQFactorMax_Type()
)
coiFECCurrentQFactorMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFECCurrentQFactorMax.setStatus("current")
_CoiFECCurrentQFactorAvg_Type = SnmpAdminString
_CoiFECCurrentQFactorAvg_Object = MibTableColumn
coiFECCurrentQFactorAvg = _CoiFECCurrentQFactorAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 3, 2, 1, 15),
    _CoiFECCurrentQFactorAvg_Type()
)
coiFECCurrentQFactorAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFECCurrentQFactorAvg.setStatus("current")
_CoiFECCurrentQMarginMin_Type = SnmpAdminString
_CoiFECCurrentQMarginMin_Object = MibTableColumn
coiFECCurrentQMarginMin = _CoiFECCurrentQMarginMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 3, 2, 1, 16),
    _CoiFECCurrentQMarginMin_Type()
)
coiFECCurrentQMarginMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFECCurrentQMarginMin.setStatus("current")
_CoiFECCurrentQMarginMax_Type = SnmpAdminString
_CoiFECCurrentQMarginMax_Object = MibTableColumn
coiFECCurrentQMarginMax = _CoiFECCurrentQMarginMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 3, 2, 1, 17),
    _CoiFECCurrentQMarginMax_Type()
)
coiFECCurrentQMarginMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFECCurrentQMarginMax.setStatus("current")
_CoiFECCurrentQMarginAvg_Type = SnmpAdminString
_CoiFECCurrentQMarginAvg_Object = MibTableColumn
coiFECCurrentQMarginAvg = _CoiFECCurrentQMarginAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 3, 2, 1, 18),
    _CoiFECCurrentQMarginAvg_Type()
)
coiFECCurrentQMarginAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFECCurrentQMarginAvg.setStatus("current")
_CoiFECIntervalTable_Object = MibTable
coiFECIntervalTable = _CoiFECIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 3, 3)
)
if mibBuilder.loadTexts:
    coiFECIntervalTable.setStatus("current")
_CoiFECIntervalEntry_Object = MibTableRow
coiFECIntervalEntry = _CoiFECIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 3, 3, 1)
)
coiFECIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-OTN-IF-MIB", "coiFECIntervalType"),
    (0, "CISCO-OTN-IF-MIB", "coiFECIntervalNum"),
)
if mibBuilder.loadTexts:
    coiFECIntervalEntry.setStatus("current")
_CoiFECIntervalType_Type = CoiIntervalType
_CoiFECIntervalType_Object = MibTableColumn
coiFECIntervalType = _CoiFECIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 3, 3, 1, 1),
    _CoiFECIntervalType_Type()
)
coiFECIntervalType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coiFECIntervalType.setStatus("current")


class _CoiFECIntervalNum_Type(Integer32):
    """Custom type coiFECIntervalNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_CoiFECIntervalNum_Type.__name__ = "Integer32"
_CoiFECIntervalNum_Object = MibTableColumn
coiFECIntervalNum = _CoiFECIntervalNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 3, 3, 1, 2),
    _CoiFECIntervalNum_Type()
)
coiFECIntervalNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coiFECIntervalNum.setStatus("current")
_CoiFECIntervalCorBitErrs_Type = Counter64
_CoiFECIntervalCorBitErrs_Object = MibTableColumn
coiFECIntervalCorBitErrs = _CoiFECIntervalCorBitErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 3, 3, 1, 3),
    _CoiFECIntervalCorBitErrs_Type()
)
coiFECIntervalCorBitErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFECIntervalCorBitErrs.setStatus("current")
_CoiFECIntervalCorByteErrs_Type = Counter64
_CoiFECIntervalCorByteErrs_Object = MibTableColumn
coiFECIntervalCorByteErrs = _CoiFECIntervalCorByteErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 3, 3, 1, 4),
    _CoiFECIntervalCorByteErrs_Type()
)
coiFECIntervalCorByteErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFECIntervalCorByteErrs.setStatus("current")
_CoiFECIntervalDetZeroErrs_Type = Counter64
_CoiFECIntervalDetZeroErrs_Object = MibTableColumn
coiFECIntervalDetZeroErrs = _CoiFECIntervalDetZeroErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 3, 3, 1, 5),
    _CoiFECIntervalDetZeroErrs_Type()
)
coiFECIntervalDetZeroErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFECIntervalDetZeroErrs.setStatus("current")
_CoiFECIntervalDetOneErrs_Type = Counter64
_CoiFECIntervalDetOneErrs_Object = MibTableColumn
coiFECIntervalDetOneErrs = _CoiFECIntervalDetOneErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 3, 3, 1, 6),
    _CoiFECIntervalDetOneErrs_Type()
)
coiFECIntervalDetOneErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFECIntervalDetOneErrs.setStatus("current")
_CoiFECIntervalUncorWords_Type = Counter64
_CoiFECIntervalUncorWords_Object = MibTableColumn
coiFECIntervalUncorWords = _CoiFECIntervalUncorWords_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 3, 3, 1, 7),
    _CoiFECIntervalUncorWords_Type()
)
coiFECIntervalUncorWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFECIntervalUncorWords.setStatus("current")
_CoiFECIntervalValidData_Type = TruthValue
_CoiFECIntervalValidData_Object = MibTableColumn
coiFECIntervalValidData = _CoiFECIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 3, 3, 1, 8),
    _CoiFECIntervalValidData_Type()
)
coiFECIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFECIntervalValidData.setStatus("current")
_CoiFECIntervalPreFECMin_Type = SnmpAdminString
_CoiFECIntervalPreFECMin_Object = MibTableColumn
coiFECIntervalPreFECMin = _CoiFECIntervalPreFECMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 3, 3, 1, 9),
    _CoiFECIntervalPreFECMin_Type()
)
coiFECIntervalPreFECMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFECIntervalPreFECMin.setStatus("current")
_CoiFECIntervalPreFECMax_Type = SnmpAdminString
_CoiFECIntervalPreFECMax_Object = MibTableColumn
coiFECIntervalPreFECMax = _CoiFECIntervalPreFECMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 3, 3, 1, 10),
    _CoiFECIntervalPreFECMax_Type()
)
coiFECIntervalPreFECMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFECIntervalPreFECMax.setStatus("current")
_CoiFECIntervalPreFECAvg_Type = SnmpAdminString
_CoiFECIntervalPreFECAvg_Object = MibTableColumn
coiFECIntervalPreFECAvg = _CoiFECIntervalPreFECAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 3, 3, 1, 11),
    _CoiFECIntervalPreFECAvg_Type()
)
coiFECIntervalPreFECAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFECIntervalPreFECAvg.setStatus("current")
_CoiFECIntervalPostFECMin_Type = SnmpAdminString
_CoiFECIntervalPostFECMin_Object = MibTableColumn
coiFECIntervalPostFECMin = _CoiFECIntervalPostFECMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 3, 3, 1, 12),
    _CoiFECIntervalPostFECMin_Type()
)
coiFECIntervalPostFECMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFECIntervalPostFECMin.setStatus("current")
_CoiFECIntervalPostFECMax_Type = SnmpAdminString
_CoiFECIntervalPostFECMax_Object = MibTableColumn
coiFECIntervalPostFECMax = _CoiFECIntervalPostFECMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 3, 3, 1, 13),
    _CoiFECIntervalPostFECMax_Type()
)
coiFECIntervalPostFECMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFECIntervalPostFECMax.setStatus("current")
_CoiFECIntervalPostFECAvg_Type = SnmpAdminString
_CoiFECIntervalPostFECAvg_Object = MibTableColumn
coiFECIntervalPostFECAvg = _CoiFECIntervalPostFECAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 3, 3, 1, 14),
    _CoiFECIntervalPostFECAvg_Type()
)
coiFECIntervalPostFECAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFECIntervalPostFECAvg.setStatus("current")
_CoiFECIntervalQFactorMin_Type = SnmpAdminString
_CoiFECIntervalQFactorMin_Object = MibTableColumn
coiFECIntervalQFactorMin = _CoiFECIntervalQFactorMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 3, 3, 1, 15),
    _CoiFECIntervalQFactorMin_Type()
)
coiFECIntervalQFactorMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFECIntervalQFactorMin.setStatus("current")
_CoiFECIntervalQFactorMax_Type = SnmpAdminString
_CoiFECIntervalQFactorMax_Object = MibTableColumn
coiFECIntervalQFactorMax = _CoiFECIntervalQFactorMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 3, 3, 1, 16),
    _CoiFECIntervalQFactorMax_Type()
)
coiFECIntervalQFactorMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFECIntervalQFactorMax.setStatus("current")
_CoiFECIntervalQFactorAvg_Type = SnmpAdminString
_CoiFECIntervalQFactorAvg_Object = MibTableColumn
coiFECIntervalQFactorAvg = _CoiFECIntervalQFactorAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 3, 3, 1, 17),
    _CoiFECIntervalQFactorAvg_Type()
)
coiFECIntervalQFactorAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFECIntervalQFactorAvg.setStatus("current")
_CoiFECIntervalQMarginMin_Type = SnmpAdminString
_CoiFECIntervalQMarginMin_Object = MibTableColumn
coiFECIntervalQMarginMin = _CoiFECIntervalQMarginMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 3, 3, 1, 18),
    _CoiFECIntervalQMarginMin_Type()
)
coiFECIntervalQMarginMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFECIntervalQMarginMin.setStatus("current")
_CoiFECIntervalQMarginMax_Type = SnmpAdminString
_CoiFECIntervalQMarginMax_Object = MibTableColumn
coiFECIntervalQMarginMax = _CoiFECIntervalQMarginMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 3, 3, 1, 19),
    _CoiFECIntervalQMarginMax_Type()
)
coiFECIntervalQMarginMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFECIntervalQMarginMax.setStatus("current")
_CoiFECIntervalQMarginAvg_Type = SnmpAdminString
_CoiFECIntervalQMarginAvg_Object = MibTableColumn
coiFECIntervalQMarginAvg = _CoiFECIntervalQMarginAvg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 1, 3, 3, 1, 20),
    _CoiFECIntervalQMarginAvg_Type()
)
coiFECIntervalQMarginAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coiFECIntervalQMarginAvg.setStatus("current")
_CiscoOtnIfMIBConformance_ObjectIdentity = ObjectIdentity
ciscoOtnIfMIBConformance = _CiscoOtnIfMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 2)
)
_CiscoOtnIfMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoOtnIfMIBCompliances = _CiscoOtnIfMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 2, 1)
)
_CiscoOtnIfMIBGroups_ObjectIdentity = ObjectIdentity
ciscoOtnIfMIBGroups = _CiscoOtnIfMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 2, 2)
)

# Managed Objects groups

coiIfControllerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 2, 2, 1)
)
coiIfControllerGroup.setObjects(
      *(("CISCO-OTN-IF-MIB", "coiIfControllerLoopback"),
        ("CISCO-OTN-IF-MIB", "coiIfControllerWavelength"),
        ("CISCO-OTN-IF-MIB", "coiIfControllerLaserAdminStatus"),
        ("CISCO-OTN-IF-MIB", "coiIfControllerLaserOperStatus"),
        ("CISCO-OTN-IF-MIB", "coiIfControllerOtnStatus"),
        ("CISCO-OTN-IF-MIB", "coiIfControllerFECMode"),
        ("CISCO-OTN-IF-MIB", "coiIfControllerTDCOperMode"),
        ("CISCO-OTN-IF-MIB", "coiIfControllerTDCOperStatus"),
        ("CISCO-OTN-IF-MIB", "coiIfControllerTDCOperSetting"),
        ("CISCO-OTN-IF-MIB", "coiIfControllerPreFECBERMantissa"),
        ("CISCO-OTN-IF-MIB", "coiIfControllerPreFECBERExponent"),
        ("CISCO-OTN-IF-MIB", "coiIfControllerQFactor"),
        ("CISCO-OTN-IF-MIB", "coiIfControllerQMargin"),
        ("CISCO-OTN-IF-MIB", "coiIfControllerOTNValidIntervals"),
        ("CISCO-OTN-IF-MIB", "coiIfControllerFECValidIntervals"))
)
if mibBuilder.loadTexts:
    coiIfControllerGroup.setStatus("current")

coiIfOtnNearEndCurrentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 2, 2, 3)
)
coiIfOtnNearEndCurrentGroup.setObjects(
      *(("CISCO-OTN-IF-MIB", "coiOtnNearEndThreshValue"),
        ("CISCO-OTN-IF-MIB", "coiOtnNearEndThreshStorageType"),
        ("CISCO-OTN-IF-MIB", "coiOtnNearEndThreshStatus"),
        ("CISCO-OTN-IF-MIB", "coiOtnNearEndCurrentFCs"),
        ("CISCO-OTN-IF-MIB", "coiOtnNearEndCurrentESs"),
        ("CISCO-OTN-IF-MIB", "coiOtnNearEndCurrentSESs"),
        ("CISCO-OTN-IF-MIB", "coiOtnNearEndCurrentUASs"),
        ("CISCO-OTN-IF-MIB", "coiOtnNearEndCurrentBBEs"),
        ("CISCO-OTN-IF-MIB", "coiOtnNearEndCurrentESRs"),
        ("CISCO-OTN-IF-MIB", "coiOtnNearEndCurrentSESRs"),
        ("CISCO-OTN-IF-MIB", "coiOtnNearEndCurrentBBERs"))
)
if mibBuilder.loadTexts:
    coiIfOtnNearEndCurrentGroup.setStatus("current")

coiIfOtnNearEndIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 2, 2, 4)
)
coiIfOtnNearEndIntervalGroup.setObjects(
      *(("CISCO-OTN-IF-MIB", "coiOtnNearEndThreshValue"),
        ("CISCO-OTN-IF-MIB", "coiOtnNearEndThreshStorageType"),
        ("CISCO-OTN-IF-MIB", "coiOtnNearEndThreshStatus"),
        ("CISCO-OTN-IF-MIB", "coiOtnNearEndIntervalFCs"),
        ("CISCO-OTN-IF-MIB", "coiOtnNearEndIntervalESs"),
        ("CISCO-OTN-IF-MIB", "coiOtnNearEndIntervalSESs"),
        ("CISCO-OTN-IF-MIB", "coiOtnNearEndIntervalUASs"),
        ("CISCO-OTN-IF-MIB", "coiOtnNearEndIntervalBBEs"),
        ("CISCO-OTN-IF-MIB", "coiOtnNearEndIntervalESRs"),
        ("CISCO-OTN-IF-MIB", "coiOtnNearEndIntervalSESRs"),
        ("CISCO-OTN-IF-MIB", "coiOtnNearEndIntervalBBERs"),
        ("CISCO-OTN-IF-MIB", "coiOtnNearEndIntervalValidData"))
)
if mibBuilder.loadTexts:
    coiIfOtnNearEndIntervalGroup.setStatus("current")

coiIfOtnFarEndCurrentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 2, 2, 5)
)
coiIfOtnFarEndCurrentGroup.setObjects(
      *(("CISCO-OTN-IF-MIB", "coiOtnFarEndThreshValue"),
        ("CISCO-OTN-IF-MIB", "coiOtnFarEndThreshStorageType"),
        ("CISCO-OTN-IF-MIB", "coiOtnFarEndThreshStatus"),
        ("CISCO-OTN-IF-MIB", "coiOtnFarEndCurrentFCs"),
        ("CISCO-OTN-IF-MIB", "coiOtnFarEndCurrentESs"),
        ("CISCO-OTN-IF-MIB", "coiOtnFarEndCurrentSESs"),
        ("CISCO-OTN-IF-MIB", "coiOtnFarEndCurrentUASs"),
        ("CISCO-OTN-IF-MIB", "coiOtnFarEndCurrentBBEs"),
        ("CISCO-OTN-IF-MIB", "coiOtnFarEndCurrentESRs"),
        ("CISCO-OTN-IF-MIB", "coiOtnFarEndCurrentSESRs"),
        ("CISCO-OTN-IF-MIB", "coiOtnFarEndCurrentBBERs"))
)
if mibBuilder.loadTexts:
    coiIfOtnFarEndCurrentGroup.setStatus("current")

coiIfOtnFarEndIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 2, 2, 6)
)
coiIfOtnFarEndIntervalGroup.setObjects(
      *(("CISCO-OTN-IF-MIB", "coiOtnFarEndThreshValue"),
        ("CISCO-OTN-IF-MIB", "coiOtnFarEndThreshStorageType"),
        ("CISCO-OTN-IF-MIB", "coiOtnFarEndThreshStatus"),
        ("CISCO-OTN-IF-MIB", "coiOtnFarEndIntervalFCs"),
        ("CISCO-OTN-IF-MIB", "coiOtnFarEndIntervalESs"),
        ("CISCO-OTN-IF-MIB", "coiOtnFarEndIntervalSESs"),
        ("CISCO-OTN-IF-MIB", "coiOtnFarEndIntervalUASs"),
        ("CISCO-OTN-IF-MIB", "coiOtnFarEndIntervalBBEs"),
        ("CISCO-OTN-IF-MIB", "coiOtnFarEndIntervalESRs"),
        ("CISCO-OTN-IF-MIB", "coiOtnFarEndIntervalSESRs"),
        ("CISCO-OTN-IF-MIB", "coiOtnFarEndIntervalBBERs"),
        ("CISCO-OTN-IF-MIB", "coiOtnFarEndIntervalValidData"))
)
if mibBuilder.loadTexts:
    coiIfOtnFarEndIntervalGroup.setStatus("current")

coiIfOtnGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 2, 2, 7)
)
coiIfOtnGroup.setObjects(
      *(("CISCO-OTN-IF-MIB", "coiOtnNearEndThreshValue"),
        ("CISCO-OTN-IF-MIB", "coiOtnNearEndThreshStorageType"),
        ("CISCO-OTN-IF-MIB", "coiOtnNearEndThreshStatus"),
        ("CISCO-OTN-IF-MIB", "coiOtnNearEndCurrentFCs"),
        ("CISCO-OTN-IF-MIB", "coiOtnNearEndCurrentESs"),
        ("CISCO-OTN-IF-MIB", "coiOtnNearEndCurrentSESs"),
        ("CISCO-OTN-IF-MIB", "coiOtnNearEndCurrentUASs"),
        ("CISCO-OTN-IF-MIB", "coiOtnNearEndCurrentBBEs"),
        ("CISCO-OTN-IF-MIB", "coiOtnNearEndCurrentESRs"),
        ("CISCO-OTN-IF-MIB", "coiOtnNearEndCurrentSESRs"),
        ("CISCO-OTN-IF-MIB", "coiOtnNearEndCurrentBBERs"),
        ("CISCO-OTN-IF-MIB", "coiOtnNearEndIntervalFCs"),
        ("CISCO-OTN-IF-MIB", "coiOtnNearEndIntervalESs"),
        ("CISCO-OTN-IF-MIB", "coiOtnNearEndIntervalSESs"),
        ("CISCO-OTN-IF-MIB", "coiOtnNearEndIntervalUASs"),
        ("CISCO-OTN-IF-MIB", "coiOtnNearEndIntervalBBEs"),
        ("CISCO-OTN-IF-MIB", "coiOtnNearEndIntervalESRs"),
        ("CISCO-OTN-IF-MIB", "coiOtnNearEndIntervalSESRs"),
        ("CISCO-OTN-IF-MIB", "coiOtnNearEndIntervalBBERs"),
        ("CISCO-OTN-IF-MIB", "coiOtnNearEndIntervalValidData"),
        ("CISCO-OTN-IF-MIB", "coiOtnFarEndThreshValue"),
        ("CISCO-OTN-IF-MIB", "coiOtnFarEndThreshStorageType"),
        ("CISCO-OTN-IF-MIB", "coiOtnFarEndThreshStatus"),
        ("CISCO-OTN-IF-MIB", "coiOtnFarEndCurrentFCs"),
        ("CISCO-OTN-IF-MIB", "coiOtnFarEndCurrentESs"),
        ("CISCO-OTN-IF-MIB", "coiOtnFarEndCurrentSESs"),
        ("CISCO-OTN-IF-MIB", "coiOtnFarEndCurrentUASs"),
        ("CISCO-OTN-IF-MIB", "coiOtnFarEndCurrentBBEs"),
        ("CISCO-OTN-IF-MIB", "coiOtnFarEndCurrentESRs"),
        ("CISCO-OTN-IF-MIB", "coiOtnFarEndCurrentSESRs"),
        ("CISCO-OTN-IF-MIB", "coiOtnFarEndCurrentBBERs"),
        ("CISCO-OTN-IF-MIB", "coiOtnFarEndIntervalFCs"),
        ("CISCO-OTN-IF-MIB", "coiOtnFarEndIntervalESs"),
        ("CISCO-OTN-IF-MIB", "coiOtnFarEndIntervalSESs"),
        ("CISCO-OTN-IF-MIB", "coiOtnFarEndIntervalUASs"),
        ("CISCO-OTN-IF-MIB", "coiOtnFarEndIntervalBBEs"),
        ("CISCO-OTN-IF-MIB", "coiOtnFarEndIntervalESRs"),
        ("CISCO-OTN-IF-MIB", "coiOtnFarEndIntervalSESRs"),
        ("CISCO-OTN-IF-MIB", "coiOtnFarEndIntervalBBERs"),
        ("CISCO-OTN-IF-MIB", "coiOtnFarEndIntervalValidData"))
)
if mibBuilder.loadTexts:
    coiIfOtnGroup.setStatus("current")

coiIfFECGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 2, 2, 8)
)
coiIfFECGroup.setObjects(
      *(("CISCO-OTN-IF-MIB", "coiFECThreshValue"),
        ("CISCO-OTN-IF-MIB", "coiFECThreshStorageType"),
        ("CISCO-OTN-IF-MIB", "coiFECThreshStatus"),
        ("CISCO-OTN-IF-MIB", "coiFECCurrentCorBitErrs"),
        ("CISCO-OTN-IF-MIB", "coiFECCurrentCorByteErrs"),
        ("CISCO-OTN-IF-MIB", "coiFECCurrentDetZeroErrs"),
        ("CISCO-OTN-IF-MIB", "coiFECCurrentDetOneErrs"),
        ("CISCO-OTN-IF-MIB", "coiFECCurrentUncorWords"),
        ("CISCO-OTN-IF-MIB", "coiFECIntervalCorBitErrs"),
        ("CISCO-OTN-IF-MIB", "coiFECIntervalCorByteErrs"),
        ("CISCO-OTN-IF-MIB", "coiFECIntervalDetZeroErrs"),
        ("CISCO-OTN-IF-MIB", "coiFECIntervalDetOneErrs"),
        ("CISCO-OTN-IF-MIB", "coiFECIntervalUncorWords"),
        ("CISCO-OTN-IF-MIB", "coiFECIntervalValidData"))
)
if mibBuilder.loadTexts:
    coiIfFECGroup.setStatus("current")

coiIfFECCurrentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 2, 2, 9)
)
coiIfFECCurrentGroup.setObjects(
      *(("CISCO-OTN-IF-MIB", "coiFECThreshValue"),
        ("CISCO-OTN-IF-MIB", "coiFECThreshStorageType"),
        ("CISCO-OTN-IF-MIB", "coiFECThreshStatus"),
        ("CISCO-OTN-IF-MIB", "coiFECCurrentCorBitErrs"),
        ("CISCO-OTN-IF-MIB", "coiFECCurrentCorByteErrs"),
        ("CISCO-OTN-IF-MIB", "coiFECCurrentDetZeroErrs"),
        ("CISCO-OTN-IF-MIB", "coiFECCurrentDetOneErrs"),
        ("CISCO-OTN-IF-MIB", "coiFECCurrentUncorWords"))
)
if mibBuilder.loadTexts:
    coiIfFECCurrentGroup.setStatus("deprecated")

coiIfFECIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 2, 2, 10)
)
coiIfFECIntervalGroup.setObjects(
      *(("CISCO-OTN-IF-MIB", "coiFECThreshValue"),
        ("CISCO-OTN-IF-MIB", "coiFECThreshStorageType"),
        ("CISCO-OTN-IF-MIB", "coiFECThreshStatus"),
        ("CISCO-OTN-IF-MIB", "coiFECIntervalCorBitErrs"),
        ("CISCO-OTN-IF-MIB", "coiFECIntervalCorByteErrs"),
        ("CISCO-OTN-IF-MIB", "coiFECIntervalDetZeroErrs"),
        ("CISCO-OTN-IF-MIB", "coiFECIntervalDetOneErrs"),
        ("CISCO-OTN-IF-MIB", "coiFECIntervalUncorWords"),
        ("CISCO-OTN-IF-MIB", "coiFECIntervalValidData"))
)
if mibBuilder.loadTexts:
    coiIfFECIntervalGroup.setStatus("deprecated")

coiIfOtnNotifEnableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 2, 2, 11)
)
coiIfOtnNotifEnableGroup.setObjects(
    ("CISCO-OTN-IF-MIB", "coiOtnIfNotifEnabled")
)
if mibBuilder.loadTexts:
    coiIfOtnNotifEnableGroup.setStatus("current")

coiIfOtnNotifStatusObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 2, 2, 12)
)
coiIfOtnNotifStatusObjectGroup.setObjects(
      *(("CISCO-OTN-IF-MIB", "coiOtnIfOTUStatus"),
        ("CISCO-OTN-IF-MIB", "coiOtnIfODUStatus"))
)
if mibBuilder.loadTexts:
    coiIfOtnNotifStatusObjectGroup.setStatus("current")

coiIfFECCurrentGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 2, 2, 14)
)
coiIfFECCurrentGroup1.setObjects(
      *(("CISCO-OTN-IF-MIB", "coiFECThreshValue"),
        ("CISCO-OTN-IF-MIB", "coiFECThreshStorageType"),
        ("CISCO-OTN-IF-MIB", "coiFECThreshStatus"),
        ("CISCO-OTN-IF-MIB", "coiFECCurrentCorBitErrs"),
        ("CISCO-OTN-IF-MIB", "coiFECCurrentCorByteErrs"),
        ("CISCO-OTN-IF-MIB", "coiFECCurrentDetZeroErrs"),
        ("CISCO-OTN-IF-MIB", "coiFECCurrentDetOneErrs"),
        ("CISCO-OTN-IF-MIB", "coiFECCurrentUncorWords"),
        ("CISCO-OTN-IF-MIB", "coiFECCurrentPreFECMin"),
        ("CISCO-OTN-IF-MIB", "coiFECCurrentPreFECMax"),
        ("CISCO-OTN-IF-MIB", "coiFECCurrentPreFECAvg"),
        ("CISCO-OTN-IF-MIB", "coiFECCurrentPostFECMin"),
        ("CISCO-OTN-IF-MIB", "coiFECCurrentPostFECMax"),
        ("CISCO-OTN-IF-MIB", "coiFECCurrentPostFECAvg"),
        ("CISCO-OTN-IF-MIB", "coiFECCurrentQFactorMin"),
        ("CISCO-OTN-IF-MIB", "coiFECCurrentQFactorMax"),
        ("CISCO-OTN-IF-MIB", "coiFECCurrentQFactorAvg"),
        ("CISCO-OTN-IF-MIB", "coiFECCurrentQMarginMin"),
        ("CISCO-OTN-IF-MIB", "coiFECCurrentQMarginMax"),
        ("CISCO-OTN-IF-MIB", "coiFECCurrentQMarginAvg"))
)
if mibBuilder.loadTexts:
    coiIfFECCurrentGroup1.setStatus("current")

coiIfFECIntervalGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 2, 2, 15)
)
coiIfFECIntervalGroup1.setObjects(
      *(("CISCO-OTN-IF-MIB", "coiFECThreshValue"),
        ("CISCO-OTN-IF-MIB", "coiFECThreshStorageType"),
        ("CISCO-OTN-IF-MIB", "coiFECThreshStatus"),
        ("CISCO-OTN-IF-MIB", "coiFECIntervalCorBitErrs"),
        ("CISCO-OTN-IF-MIB", "coiFECIntervalCorByteErrs"),
        ("CISCO-OTN-IF-MIB", "coiFECIntervalDetZeroErrs"),
        ("CISCO-OTN-IF-MIB", "coiFECIntervalDetOneErrs"),
        ("CISCO-OTN-IF-MIB", "coiFECIntervalUncorWords"),
        ("CISCO-OTN-IF-MIB", "coiFECIntervalValidData"),
        ("CISCO-OTN-IF-MIB", "coiFECIntervalPreFECMin"),
        ("CISCO-OTN-IF-MIB", "coiFECIntervalPreFECMax"),
        ("CISCO-OTN-IF-MIB", "coiFECIntervalPreFECAvg"),
        ("CISCO-OTN-IF-MIB", "coiFECIntervalPostFECMin"),
        ("CISCO-OTN-IF-MIB", "coiFECIntervalPostFECMax"),
        ("CISCO-OTN-IF-MIB", "coiFECIntervalPostFECAvg"),
        ("CISCO-OTN-IF-MIB", "coiFECIntervalQFactorMin"),
        ("CISCO-OTN-IF-MIB", "coiFECIntervalQFactorMax"),
        ("CISCO-OTN-IF-MIB", "coiFECIntervalQFactorAvg"),
        ("CISCO-OTN-IF-MIB", "coiFECIntervalQMarginMin"),
        ("CISCO-OTN-IF-MIB", "coiFECIntervalQMarginMax"),
        ("CISCO-OTN-IF-MIB", "coiFECIntervalQMarginAvg"))
)
if mibBuilder.loadTexts:
    coiIfFECIntervalGroup1.setStatus("current")


# Notification objects

coiOtnIfOTUStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 0, 1)
)
coiOtnIfOTUStatusChange.setObjects(
      *(("IF-MIB", "ifName"),
        ("CISCO-OTN-IF-MIB", "coiOtnIfOTUStatus"))
)
if mibBuilder.loadTexts:
    coiOtnIfOTUStatusChange.setStatus(
        "current"
    )

coiOtnIfODUStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 0, 2)
)
coiOtnIfODUStatusChange.setObjects(
      *(("IF-MIB", "ifName"),
        ("CISCO-OTN-IF-MIB", "coiOtnIfODUStatus"))
)
if mibBuilder.loadTexts:
    coiOtnIfODUStatusChange.setStatus(
        "current"
    )


# Notifications groups

coiIfOtnNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 2, 2, 13)
)
coiIfOtnNotifGroup.setObjects(
      *(("CISCO-OTN-IF-MIB", "coiOtnIfOTUStatusChange"),
        ("CISCO-OTN-IF-MIB", "coiOtnIfODUStatusChange"))
)
if mibBuilder.loadTexts:
    coiIfOtnNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoOtnIfMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoOtnIfMIBCompliance.setStatus(
        "deprecated"
    )

ciscoOtnIfMIBCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoOtnIfMIBCompliance1.setStatus(
        "deprecated"
    )

ciscoOtnIfMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 639, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoOtnIfMIBCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-OTN-IF-MIB",
    **{"CoiIntervalType": CoiIntervalType,
       "CoiMonitorType": CoiMonitorType,
       "CoiOtnThresholdType": CoiOtnThresholdType,
       "CoiOpticalWavelength": CoiOpticalWavelength,
       "ciscoOtnIfMIB": ciscoOtnIfMIB,
       "ciscoOtnIfMIBNotifs": ciscoOtnIfMIBNotifs,
       "coiOtnIfOTUStatusChange": coiOtnIfOTUStatusChange,
       "coiOtnIfODUStatusChange": coiOtnIfODUStatusChange,
       "ciscoOtnIfMIBObjects": ciscoOtnIfMIBObjects,
       "coiDwdmInterface": coiDwdmInterface,
       "coiIfControllerTable": coiIfControllerTable,
       "coiIfControllerEntry": coiIfControllerEntry,
       "coiIfControllerLoopback": coiIfControllerLoopback,
       "coiIfControllerWavelength": coiIfControllerWavelength,
       "coiIfControllerLaserAdminStatus": coiIfControllerLaserAdminStatus,
       "coiIfControllerLaserOperStatus": coiIfControllerLaserOperStatus,
       "coiIfControllerOtnStatus": coiIfControllerOtnStatus,
       "coiIfControllerFECMode": coiIfControllerFECMode,
       "coiIfControllerTDCOperMode": coiIfControllerTDCOperMode,
       "coiIfControllerTDCOperStatus": coiIfControllerTDCOperStatus,
       "coiIfControllerTDCOperSetting": coiIfControllerTDCOperSetting,
       "coiIfControllerPreFECBERMantissa": coiIfControllerPreFECBERMantissa,
       "coiIfControllerPreFECBERExponent": coiIfControllerPreFECBERExponent,
       "coiIfControllerQFactor": coiIfControllerQFactor,
       "coiIfControllerQMargin": coiIfControllerQMargin,
       "coiIfControllerOTNValidIntervals": coiIfControllerOTNValidIntervals,
       "coiIfControllerFECValidIntervals": coiIfControllerFECValidIntervals,
       "coiOtnIfOTUStatus": coiOtnIfOTUStatus,
       "coiOtnIfODUStatus": coiOtnIfODUStatus,
       "coiDwdmIfOtn": coiDwdmIfOtn,
       "coiOtnNearEndThresholdsTable": coiOtnNearEndThresholdsTable,
       "coiOtnNearEndThresholdsEntry": coiOtnNearEndThresholdsEntry,
       "coiOtnNearEndThreshIntervalType": coiOtnNearEndThreshIntervalType,
       "coiOtnNearEndThreshMonType": coiOtnNearEndThreshMonType,
       "coiOtnNearEndThresholdType": coiOtnNearEndThresholdType,
       "coiOtnNearEndThreshValue": coiOtnNearEndThreshValue,
       "coiOtnNearEndThreshStorageType": coiOtnNearEndThreshStorageType,
       "coiOtnNearEndThreshStatus": coiOtnNearEndThreshStatus,
       "coiOtnFarEndThresholdsTable": coiOtnFarEndThresholdsTable,
       "coiOtnFarEndThresholdsEntry": coiOtnFarEndThresholdsEntry,
       "coiOtnFarEndThreshIntervalType": coiOtnFarEndThreshIntervalType,
       "coiOtnFarEndThreshMonType": coiOtnFarEndThreshMonType,
       "coiOtnFarEndThresholdType": coiOtnFarEndThresholdType,
       "coiOtnFarEndThreshValue": coiOtnFarEndThreshValue,
       "coiOtnFarEndThreshStorageType": coiOtnFarEndThreshStorageType,
       "coiOtnFarEndThreshStatus": coiOtnFarEndThreshStatus,
       "coiOtnNearEndCurrentTable": coiOtnNearEndCurrentTable,
       "coiOtnNearEndCurrentEntry": coiOtnNearEndCurrentEntry,
       "coiOtnNearEndCurIntervalType": coiOtnNearEndCurIntervalType,
       "coiOtnNearEndCurrentMonType": coiOtnNearEndCurrentMonType,
       "coiOtnNearEndCurrentFCs": coiOtnNearEndCurrentFCs,
       "coiOtnNearEndCurrentESs": coiOtnNearEndCurrentESs,
       "coiOtnNearEndCurrentSESs": coiOtnNearEndCurrentSESs,
       "coiOtnNearEndCurrentUASs": coiOtnNearEndCurrentUASs,
       "coiOtnNearEndCurrentBBEs": coiOtnNearEndCurrentBBEs,
       "coiOtnNearEndCurrentESRs": coiOtnNearEndCurrentESRs,
       "coiOtnNearEndCurrentSESRs": coiOtnNearEndCurrentSESRs,
       "coiOtnNearEndCurrentBBERs": coiOtnNearEndCurrentBBERs,
       "coiOtnFarEndCurrentTable": coiOtnFarEndCurrentTable,
       "coiOtnFarEndCurrentEntry": coiOtnFarEndCurrentEntry,
       "coiOtnFarEndCurIntervalType": coiOtnFarEndCurIntervalType,
       "coiOtnFarEndCurrentMonType": coiOtnFarEndCurrentMonType,
       "coiOtnFarEndCurrentFCs": coiOtnFarEndCurrentFCs,
       "coiOtnFarEndCurrentESs": coiOtnFarEndCurrentESs,
       "coiOtnFarEndCurrentSESs": coiOtnFarEndCurrentSESs,
       "coiOtnFarEndCurrentUASs": coiOtnFarEndCurrentUASs,
       "coiOtnFarEndCurrentBBEs": coiOtnFarEndCurrentBBEs,
       "coiOtnFarEndCurrentESRs": coiOtnFarEndCurrentESRs,
       "coiOtnFarEndCurrentSESRs": coiOtnFarEndCurrentSESRs,
       "coiOtnFarEndCurrentBBERs": coiOtnFarEndCurrentBBERs,
       "coiOtnNearEndIntervalTable": coiOtnNearEndIntervalTable,
       "coiOtnNearEndIntervalEntry": coiOtnNearEndIntervalEntry,
       "coiOtnNearEndIntervalType": coiOtnNearEndIntervalType,
       "coiOtnNearEndIntervalMonType": coiOtnNearEndIntervalMonType,
       "coiOtnNearEndIntervalNum": coiOtnNearEndIntervalNum,
       "coiOtnNearEndIntervalFCs": coiOtnNearEndIntervalFCs,
       "coiOtnNearEndIntervalESs": coiOtnNearEndIntervalESs,
       "coiOtnNearEndIntervalSESs": coiOtnNearEndIntervalSESs,
       "coiOtnNearEndIntervalUASs": coiOtnNearEndIntervalUASs,
       "coiOtnNearEndIntervalBBEs": coiOtnNearEndIntervalBBEs,
       "coiOtnNearEndIntervalESRs": coiOtnNearEndIntervalESRs,
       "coiOtnNearEndIntervalSESRs": coiOtnNearEndIntervalSESRs,
       "coiOtnNearEndIntervalBBERs": coiOtnNearEndIntervalBBERs,
       "coiOtnNearEndIntervalValidData": coiOtnNearEndIntervalValidData,
       "coiOtnFarEndIntervalTable": coiOtnFarEndIntervalTable,
       "coiOtnFarEndIntervalEntry": coiOtnFarEndIntervalEntry,
       "coiOtnFarEndIntervalType": coiOtnFarEndIntervalType,
       "coiOtnFarEndIntervalMonType": coiOtnFarEndIntervalMonType,
       "coiOtnFarEndIntervalNum": coiOtnFarEndIntervalNum,
       "coiOtnFarEndIntervalFCs": coiOtnFarEndIntervalFCs,
       "coiOtnFarEndIntervalESs": coiOtnFarEndIntervalESs,
       "coiOtnFarEndIntervalSESs": coiOtnFarEndIntervalSESs,
       "coiOtnFarEndIntervalUASs": coiOtnFarEndIntervalUASs,
       "coiOtnFarEndIntervalBBEs": coiOtnFarEndIntervalBBEs,
       "coiOtnFarEndIntervalESRs": coiOtnFarEndIntervalESRs,
       "coiOtnFarEndIntervalSESRs": coiOtnFarEndIntervalSESRs,
       "coiOtnFarEndIntervalBBERs": coiOtnFarEndIntervalBBERs,
       "coiOtnFarEndIntervalValidData": coiOtnFarEndIntervalValidData,
       "coiOtnIfNotifEnabled": coiOtnIfNotifEnabled,
       "coiDwdmIfFEC": coiDwdmIfFEC,
       "coiFECThresholdsTable": coiFECThresholdsTable,
       "coiFECThresholdsEntry": coiFECThresholdsEntry,
       "coiFECThreshIntervalType": coiFECThreshIntervalType,
       "coiFECThreshType": coiFECThreshType,
       "coiFECThreshValue": coiFECThreshValue,
       "coiFECThreshStorageType": coiFECThreshStorageType,
       "coiFECThreshStatus": coiFECThreshStatus,
       "coiFECCurrentTable": coiFECCurrentTable,
       "coiFECCurrentEntry": coiFECCurrentEntry,
       "coiFECCurIntervalType": coiFECCurIntervalType,
       "coiFECCurrentCorBitErrs": coiFECCurrentCorBitErrs,
       "coiFECCurrentCorByteErrs": coiFECCurrentCorByteErrs,
       "coiFECCurrentDetZeroErrs": coiFECCurrentDetZeroErrs,
       "coiFECCurrentDetOneErrs": coiFECCurrentDetOneErrs,
       "coiFECCurrentUncorWords": coiFECCurrentUncorWords,
       "coiFECCurrentPreFECMin": coiFECCurrentPreFECMin,
       "coiFECCurrentPreFECMax": coiFECCurrentPreFECMax,
       "coiFECCurrentPreFECAvg": coiFECCurrentPreFECAvg,
       "coiFECCurrentPostFECMin": coiFECCurrentPostFECMin,
       "coiFECCurrentPostFECMax": coiFECCurrentPostFECMax,
       "coiFECCurrentPostFECAvg": coiFECCurrentPostFECAvg,
       "coiFECCurrentQFactorMin": coiFECCurrentQFactorMin,
       "coiFECCurrentQFactorMax": coiFECCurrentQFactorMax,
       "coiFECCurrentQFactorAvg": coiFECCurrentQFactorAvg,
       "coiFECCurrentQMarginMin": coiFECCurrentQMarginMin,
       "coiFECCurrentQMarginMax": coiFECCurrentQMarginMax,
       "coiFECCurrentQMarginAvg": coiFECCurrentQMarginAvg,
       "coiFECIntervalTable": coiFECIntervalTable,
       "coiFECIntervalEntry": coiFECIntervalEntry,
       "coiFECIntervalType": coiFECIntervalType,
       "coiFECIntervalNum": coiFECIntervalNum,
       "coiFECIntervalCorBitErrs": coiFECIntervalCorBitErrs,
       "coiFECIntervalCorByteErrs": coiFECIntervalCorByteErrs,
       "coiFECIntervalDetZeroErrs": coiFECIntervalDetZeroErrs,
       "coiFECIntervalDetOneErrs": coiFECIntervalDetOneErrs,
       "coiFECIntervalUncorWords": coiFECIntervalUncorWords,
       "coiFECIntervalValidData": coiFECIntervalValidData,
       "coiFECIntervalPreFECMin": coiFECIntervalPreFECMin,
       "coiFECIntervalPreFECMax": coiFECIntervalPreFECMax,
       "coiFECIntervalPreFECAvg": coiFECIntervalPreFECAvg,
       "coiFECIntervalPostFECMin": coiFECIntervalPostFECMin,
       "coiFECIntervalPostFECMax": coiFECIntervalPostFECMax,
       "coiFECIntervalPostFECAvg": coiFECIntervalPostFECAvg,
       "coiFECIntervalQFactorMin": coiFECIntervalQFactorMin,
       "coiFECIntervalQFactorMax": coiFECIntervalQFactorMax,
       "coiFECIntervalQFactorAvg": coiFECIntervalQFactorAvg,
       "coiFECIntervalQMarginMin": coiFECIntervalQMarginMin,
       "coiFECIntervalQMarginMax": coiFECIntervalQMarginMax,
       "coiFECIntervalQMarginAvg": coiFECIntervalQMarginAvg,
       "ciscoOtnIfMIBConformance": ciscoOtnIfMIBConformance,
       "ciscoOtnIfMIBCompliances": ciscoOtnIfMIBCompliances,
       "ciscoOtnIfMIBCompliance": ciscoOtnIfMIBCompliance,
       "ciscoOtnIfMIBCompliance1": ciscoOtnIfMIBCompliance1,
       "ciscoOtnIfMIBCompliance2": ciscoOtnIfMIBCompliance2,
       "ciscoOtnIfMIBGroups": ciscoOtnIfMIBGroups,
       "coiIfControllerGroup": coiIfControllerGroup,
       "coiIfOtnNearEndCurrentGroup": coiIfOtnNearEndCurrentGroup,
       "coiIfOtnNearEndIntervalGroup": coiIfOtnNearEndIntervalGroup,
       "coiIfOtnFarEndCurrentGroup": coiIfOtnFarEndCurrentGroup,
       "coiIfOtnFarEndIntervalGroup": coiIfOtnFarEndIntervalGroup,
       "coiIfOtnGroup": coiIfOtnGroup,
       "coiIfFECGroup": coiIfFECGroup,
       "coiIfFECCurrentGroup": coiIfFECCurrentGroup,
       "coiIfFECIntervalGroup": coiIfFECIntervalGroup,
       "coiIfOtnNotifEnableGroup": coiIfOtnNotifEnableGroup,
       "coiIfOtnNotifStatusObjectGroup": coiIfOtnNotifStatusObjectGroup,
       "coiIfOtnNotifGroup": coiIfOtnNotifGroup,
       "coiIfFECCurrentGroup1": coiIfFECCurrentGroup1,
       "coiIfFECIntervalGroup1": coiIfFECIntervalGroup1}
)
