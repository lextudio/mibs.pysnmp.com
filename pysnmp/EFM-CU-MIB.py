# SNMP MIB module (EFM-CU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EFM-CU-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:36:41 2024
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

(InterfaceIndex,
 ifIndex,
 ifSpeed) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex",
    "ifSpeed")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(ietfDrafts,) = mibBuilder.importSymbols(
    "Zhone",
    "ietfDrafts")


# MODULE-IDENTITY

efmCuMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7)
)
efmCuMIB.setRevisions(
        ("2012-06-29 00:00",
         "2005-04-04 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ProfileIndex(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )



class ProfileIndexOrZero(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class ProfileIndexList(OctetString, TextualConvention):
    status = "current"
    displayHint = "1d:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )



class TruthValueOrUnknown(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1),
          ("unknown", 0))
    )



# MIB Managed Objects in the order of their OIDs

_EfmCuObjects_ObjectIdentity = ObjectIdentity
efmCuObjects = _EfmCuObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1)
)
_EfmCuPort_ObjectIdentity = ObjectIdentity
efmCuPort = _EfmCuPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 1)
)
_EfmCuPortNotifications_ObjectIdentity = ObjectIdentity
efmCuPortNotifications = _EfmCuPortNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 1, 0)
)
_EfmCuPortConfTable_Object = MibTable
efmCuPortConfTable = _EfmCuPortConfTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 1, 1)
)
if mibBuilder.loadTexts:
    efmCuPortConfTable.setStatus("current")
_EfmCuPortConfEntry_Object = MibTableRow
efmCuPortConfEntry = _EfmCuPortConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 1, 1, 1)
)
efmCuPortConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    efmCuPortConfEntry.setStatus("current")


class _EfmCuPAFAdminState_Type(Integer32):
    """Custom type efmCuPAFAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_EfmCuPAFAdminState_Type.__name__ = "Integer32"
_EfmCuPAFAdminState_Object = MibTableColumn
efmCuPAFAdminState = _EfmCuPAFAdminState_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 1, 1, 1, 1),
    _EfmCuPAFAdminState_Type()
)
efmCuPAFAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    efmCuPAFAdminState.setStatus("current")


class _EfmCuPAFDiscoveryCode_Type(PhysAddress):
    """Custom type efmCuPAFDiscoveryCode based on PhysAddress"""
    defaultHexValue = "000000000000"


_EfmCuPAFDiscoveryCode_Object = MibTableColumn
efmCuPAFDiscoveryCode = _EfmCuPAFDiscoveryCode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 1, 1, 1, 2),
    _EfmCuPAFDiscoveryCode_Type()
)
efmCuPAFDiscoveryCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    efmCuPAFDiscoveryCode.setStatus("current")


class _EfmCuAdminProfile_Type(ProfileIndexList):
    """Custom type efmCuAdminProfile based on ProfileIndexList"""
    defaultHexValue = "01"


_EfmCuAdminProfile_Object = MibTableColumn
efmCuAdminProfile = _EfmCuAdminProfile_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 1, 1, 1, 3),
    _EfmCuAdminProfile_Type()
)
efmCuAdminProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    efmCuAdminProfile.setStatus("current")


class _EfmCuTargetDataRate_Type(Unsigned32):
    """Custom type efmCuTargetDataRate based on Unsigned32"""
    defaultValue = 50000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000),
        ValueRangeConstraint(999999, 999999),
    )


_EfmCuTargetDataRate_Type.__name__ = "Unsigned32"
_EfmCuTargetDataRate_Object = MibTableColumn
efmCuTargetDataRate = _EfmCuTargetDataRate_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 1, 1, 1, 4),
    _EfmCuTargetDataRate_Type()
)
efmCuTargetDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    efmCuTargetDataRate.setStatus("current")
if mibBuilder.loadTexts:
    efmCuTargetDataRate.setUnits("Kbps")


class _EfmCuTargetWorstCaseSnrMgn_Type(Integer32):
    """Custom type efmCuTargetWorstCaseSnrMgn based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10, 21),
    )


_EfmCuTargetWorstCaseSnrMgn_Type.__name__ = "Integer32"
_EfmCuTargetWorstCaseSnrMgn_Object = MibTableColumn
efmCuTargetWorstCaseSnrMgn = _EfmCuTargetWorstCaseSnrMgn_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 1, 1, 1, 5),
    _EfmCuTargetWorstCaseSnrMgn_Type()
)
efmCuTargetWorstCaseSnrMgn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    efmCuTargetWorstCaseSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    efmCuTargetWorstCaseSnrMgn.setUnits("dB")


class _EfmCuThreshLowBandwidth_Type(Unsigned32):
    """Custom type efmCuThreshLowBandwidth based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_EfmCuThreshLowBandwidth_Type.__name__ = "Unsigned32"
_EfmCuThreshLowBandwidth_Object = MibTableColumn
efmCuThreshLowBandwidth = _EfmCuThreshLowBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 1, 1, 1, 6),
    _EfmCuThreshLowBandwidth_Type()
)
efmCuThreshLowBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    efmCuThreshLowBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    efmCuThreshLowBandwidth.setUnits("Kbps")


class _EfmCuLowBandwidthEnable_Type(TruthValue):
    """Custom type efmCuLowBandwidthEnable based on TruthValue"""


_EfmCuLowBandwidthEnable_Object = MibTableColumn
efmCuLowBandwidthEnable = _EfmCuLowBandwidthEnable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 1, 1, 1, 7),
    _EfmCuLowBandwidthEnable_Type()
)
efmCuLowBandwidthEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    efmCuLowBandwidthEnable.setStatus("current")


class _EfmCuTargetCurrentConditionMode_Type(TruthValue):
    """Custom type efmCuTargetCurrentConditionMode based on TruthValue"""


_EfmCuTargetCurrentConditionMode_Object = MibTableColumn
efmCuTargetCurrentConditionMode = _EfmCuTargetCurrentConditionMode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 1, 1, 1, 8),
    _EfmCuTargetCurrentConditionMode_Type()
)
efmCuTargetCurrentConditionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    efmCuTargetCurrentConditionMode.setStatus("current")


class _EfmCuTargetCurrentConditionSnrMgn_Type(Integer32):
    """Custom type efmCuTargetCurrentConditionSnrMgn based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10, 21),
    )


_EfmCuTargetCurrentConditionSnrMgn_Type.__name__ = "Integer32"
_EfmCuTargetCurrentConditionSnrMgn_Object = MibTableColumn
efmCuTargetCurrentConditionSnrMgn = _EfmCuTargetCurrentConditionSnrMgn_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 1, 1, 1, 9),
    _EfmCuTargetCurrentConditionSnrMgn_Type()
)
efmCuTargetCurrentConditionSnrMgn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    efmCuTargetCurrentConditionSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    efmCuTargetCurrentConditionSnrMgn.setUnits("dB")


class _EfmCuTargetWorstCaseMode_Type(TruthValue):
    """Custom type efmCuTargetWorstCaseMode based on TruthValue"""


_EfmCuTargetWorstCaseMode_Object = MibTableColumn
efmCuTargetWorstCaseMode = _EfmCuTargetWorstCaseMode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 1, 1, 1, 10),
    _EfmCuTargetWorstCaseMode_Type()
)
efmCuTargetWorstCaseMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    efmCuTargetWorstCaseMode.setStatus("current")


class _EfmCuPAFAutoDiscovery_Type(Integer32):
    """Custom type efmCuPAFAutoDiscovery based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("optional", 2),
          ("required", 3))
    )


_EfmCuPAFAutoDiscovery_Type.__name__ = "Integer32"
_EfmCuPAFAutoDiscovery_Object = MibTableColumn
efmCuPAFAutoDiscovery = _EfmCuPAFAutoDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 1, 1, 1, 11),
    _EfmCuPAFAutoDiscovery_Type()
)
efmCuPAFAutoDiscovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    efmCuPAFAutoDiscovery.setStatus("current")


class _EfmCuPmeErrorClearStats_Type(Integer32):
    """Custom type efmCuPmeErrorClearStats based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clearStats", 2),
          ("normalStats", 1))
    )


_EfmCuPmeErrorClearStats_Type.__name__ = "Integer32"
_EfmCuPmeErrorClearStats_Object = MibTableColumn
efmCuPmeErrorClearStats = _EfmCuPmeErrorClearStats_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 1, 1, 1, 12),
    _EfmCuPmeErrorClearStats_Type()
)
efmCuPmeErrorClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    efmCuPmeErrorClearStats.setStatus("current")


class _EfmCuPmeSnrClearStats_Type(Integer32):
    """Custom type efmCuPmeSnrClearStats based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clearStats", 2),
          ("normalStats", 1))
    )


_EfmCuPmeSnrClearStats_Type.__name__ = "Integer32"
_EfmCuPmeSnrClearStats_Object = MibTableColumn
efmCuPmeSnrClearStats = _EfmCuPmeSnrClearStats_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 1, 1, 1, 13),
    _EfmCuPmeSnrClearStats_Type()
)
efmCuPmeSnrClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    efmCuPmeSnrClearStats.setStatus("current")
_EfmCuPortCapabilityTable_Object = MibTable
efmCuPortCapabilityTable = _EfmCuPortCapabilityTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 1, 2)
)
if mibBuilder.loadTexts:
    efmCuPortCapabilityTable.setStatus("current")
_EfmCuPortCapabilityEntry_Object = MibTableRow
efmCuPortCapabilityEntry = _EfmCuPortCapabilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 1, 2, 1)
)
efmCuPortCapabilityEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    efmCuPortCapabilityEntry.setStatus("current")
_EfmCuPAFSupported_Type = TruthValue
_EfmCuPAFSupported_Object = MibTableColumn
efmCuPAFSupported = _EfmCuPAFSupported_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 1, 2, 1, 1),
    _EfmCuPAFSupported_Type()
)
efmCuPAFSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efmCuPAFSupported.setStatus("current")
_EfmCuPeerPAFSupported_Type = TruthValueOrUnknown
_EfmCuPeerPAFSupported_Object = MibTableColumn
efmCuPeerPAFSupported = _EfmCuPeerPAFSupported_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 1, 2, 1, 2),
    _EfmCuPeerPAFSupported_Type()
)
efmCuPeerPAFSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efmCuPeerPAFSupported.setStatus("current")


class _EfmCuPAFCapacity_Type(Unsigned32):
    """Custom type efmCuPAFCapacity based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_EfmCuPAFCapacity_Type.__name__ = "Unsigned32"
_EfmCuPAFCapacity_Object = MibTableColumn
efmCuPAFCapacity = _EfmCuPAFCapacity_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 1, 2, 1, 3),
    _EfmCuPAFCapacity_Type()
)
efmCuPAFCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efmCuPAFCapacity.setStatus("current")


class _EfmCuPeerPAFCapacity_Type(Unsigned32):
    """Custom type efmCuPeerPAFCapacity based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 32),
    )


_EfmCuPeerPAFCapacity_Type.__name__ = "Unsigned32"
_EfmCuPeerPAFCapacity_Object = MibTableColumn
efmCuPeerPAFCapacity = _EfmCuPeerPAFCapacity_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 1, 2, 1, 4),
    _EfmCuPeerPAFCapacity_Type()
)
efmCuPeerPAFCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efmCuPeerPAFCapacity.setStatus("current")
_EfmCuPortStatusTable_Object = MibTable
efmCuPortStatusTable = _EfmCuPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 1, 3)
)
if mibBuilder.loadTexts:
    efmCuPortStatusTable.setStatus("current")
_EfmCuPortStatusEntry_Object = MibTableRow
efmCuPortStatusEntry = _EfmCuPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 1, 3, 1)
)
efmCuPortStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    efmCuPortStatusEntry.setStatus("current")


class _EfmCuFltStatus_Type(Bits):
    """Custom type efmCuFltStatus based on Bits"""
    namedValues = NamedValues(
        *(("lowBandwidth", 2),
          ("noPeer", 0),
          ("pmeSubTypeMismatch", 1))
    )

_EfmCuFltStatus_Type.__name__ = "Bits"
_EfmCuFltStatus_Object = MibTableColumn
efmCuFltStatus = _EfmCuFltStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 1, 3, 1, 1),
    _EfmCuFltStatus_Type()
)
efmCuFltStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efmCuFltStatus.setStatus("current")


class _EfmCuPortSide_Type(Integer32):
    """Custom type efmCuPortSide based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("office", 2),
          ("subscriber", 1),
          ("unknown", 3))
    )


_EfmCuPortSide_Type.__name__ = "Integer32"
_EfmCuPortSide_Object = MibTableColumn
efmCuPortSide = _EfmCuPortSide_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 1, 3, 1, 2),
    _EfmCuPortSide_Type()
)
efmCuPortSide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efmCuPortSide.setStatus("current")


class _EfmCuNumPMEs_Type(Unsigned32):
    """Custom type efmCuNumPMEs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_EfmCuNumPMEs_Type.__name__ = "Unsigned32"
_EfmCuNumPMEs_Object = MibTableColumn
efmCuNumPMEs = _EfmCuNumPMEs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 1, 3, 1, 3),
    _EfmCuNumPMEs_Type()
)
efmCuNumPMEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efmCuNumPMEs.setStatus("current")
_EfmCuPAFInErrors_Type = Counter32
_EfmCuPAFInErrors_Object = MibTableColumn
efmCuPAFInErrors = _EfmCuPAFInErrors_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 1, 3, 1, 4),
    _EfmCuPAFInErrors_Type()
)
efmCuPAFInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efmCuPAFInErrors.setStatus("current")
_EfmCuPAFInSmallFragments_Type = Counter32
_EfmCuPAFInSmallFragments_Object = MibTableColumn
efmCuPAFInSmallFragments = _EfmCuPAFInSmallFragments_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 1, 3, 1, 5),
    _EfmCuPAFInSmallFragments_Type()
)
efmCuPAFInSmallFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efmCuPAFInSmallFragments.setStatus("current")
_EfmCuPAFInLargeFragments_Type = Counter32
_EfmCuPAFInLargeFragments_Object = MibTableColumn
efmCuPAFInLargeFragments = _EfmCuPAFInLargeFragments_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 1, 3, 1, 6),
    _EfmCuPAFInLargeFragments_Type()
)
efmCuPAFInLargeFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efmCuPAFInLargeFragments.setStatus("current")
_EfmCuPAFInBadFragments_Type = Counter32
_EfmCuPAFInBadFragments_Object = MibTableColumn
efmCuPAFInBadFragments = _EfmCuPAFInBadFragments_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 1, 3, 1, 7),
    _EfmCuPAFInBadFragments_Type()
)
efmCuPAFInBadFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efmCuPAFInBadFragments.setStatus("current")
_EfmCuPAFInLostFragments_Type = Counter32
_EfmCuPAFInLostFragments_Object = MibTableColumn
efmCuPAFInLostFragments = _EfmCuPAFInLostFragments_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 1, 3, 1, 8),
    _EfmCuPAFInLostFragments_Type()
)
efmCuPAFInLostFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efmCuPAFInLostFragments.setStatus("current")
_EfmCuPAFInLostStarts_Type = Counter32
_EfmCuPAFInLostStarts_Object = MibTableColumn
efmCuPAFInLostStarts = _EfmCuPAFInLostStarts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 1, 3, 1, 9),
    _EfmCuPAFInLostStarts_Type()
)
efmCuPAFInLostStarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efmCuPAFInLostStarts.setStatus("current")
_EfmCuPAFInLostEnds_Type = Counter32
_EfmCuPAFInLostEnds_Object = MibTableColumn
efmCuPAFInLostEnds = _EfmCuPAFInLostEnds_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 1, 3, 1, 10),
    _EfmCuPAFInLostEnds_Type()
)
efmCuPAFInLostEnds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efmCuPAFInLostEnds.setStatus("current")
_EfmCuPAFInOverflows_Type = Counter32
_EfmCuPAFInOverflows_Object = MibTableColumn
efmCuPAFInOverflows = _EfmCuPAFInOverflows_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 1, 3, 1, 11),
    _EfmCuPAFInOverflows_Type()
)
efmCuPAFInOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efmCuPAFInOverflows.setStatus("current")
_EfmCuPme_ObjectIdentity = ObjectIdentity
efmCuPme = _EfmCuPme_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2)
)
_EfmCuPmeNotifications_ObjectIdentity = ObjectIdentity
efmCuPmeNotifications = _EfmCuPmeNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 0)
)
_EfmCuPmeConfTable_Object = MibTable
efmCuPmeConfTable = _EfmCuPmeConfTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 1)
)
if mibBuilder.loadTexts:
    efmCuPmeConfTable.setStatus("current")
_EfmCuPmeConfEntry_Object = MibTableRow
efmCuPmeConfEntry = _EfmCuPmeConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 1, 1)
)
efmCuPmeConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    efmCuPmeConfEntry.setStatus("current")


class _EfmCuPmeAdminSubType_Type(Integer32):
    """Custom type efmCuPmeAdminSubType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("ieee10PassTSO", 3),
          ("ieee10PassTSR", 4),
          ("ieee10PassTSor2BaseTLO", 7),
          ("ieee2BaseTLO", 1),
          ("ieee2BaseTLR", 2),
          ("ieee2BaseTLor10PassTSO", 6),
          ("ieee2BaseTLor10PassTSR", 5))
    )


_EfmCuPmeAdminSubType_Type.__name__ = "Integer32"
_EfmCuPmeAdminSubType_Object = MibTableColumn
efmCuPmeAdminSubType = _EfmCuPmeAdminSubType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 1, 1, 1),
    _EfmCuPmeAdminSubType_Type()
)
efmCuPmeAdminSubType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    efmCuPmeAdminSubType.setStatus("current")


class _EfmCuPmeAdminProfile_Type(ProfileIndexOrZero):
    """Custom type efmCuPmeAdminProfile based on ProfileIndexOrZero"""
    defaultValue = 0


_EfmCuPmeAdminProfile_Object = MibTableColumn
efmCuPmeAdminProfile = _EfmCuPmeAdminProfile_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 1, 1, 2),
    _EfmCuPmeAdminProfile_Type()
)
efmCuPmeAdminProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    efmCuPmeAdminProfile.setStatus("current")


class _EfmCuPAFRemoteDiscoveryCode_Type(PhysAddress):
    """Custom type efmCuPAFRemoteDiscoveryCode based on PhysAddress"""
    defaultHexValue = "000000000000"


_EfmCuPAFRemoteDiscoveryCode_Object = MibTableColumn
efmCuPAFRemoteDiscoveryCode = _EfmCuPAFRemoteDiscoveryCode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 1, 1, 3),
    _EfmCuPAFRemoteDiscoveryCode_Type()
)
efmCuPAFRemoteDiscoveryCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    efmCuPAFRemoteDiscoveryCode.setStatus("current")


class _EfmCuPmeThreshLineAtn_Type(Integer32):
    """Custom type efmCuPmeThreshLineAtn based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-127, 128),
    )


_EfmCuPmeThreshLineAtn_Type.__name__ = "Integer32"
_EfmCuPmeThreshLineAtn_Object = MibTableColumn
efmCuPmeThreshLineAtn = _EfmCuPmeThreshLineAtn_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 1, 1, 4),
    _EfmCuPmeThreshLineAtn_Type()
)
efmCuPmeThreshLineAtn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    efmCuPmeThreshLineAtn.setStatus("current")
if mibBuilder.loadTexts:
    efmCuPmeThreshLineAtn.setUnits("dB")


class _EfmCuPmeThreshMinSnrMgn_Type(Integer32):
    """Custom type efmCuPmeThreshMinSnrMgn based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-127, 128),
    )


_EfmCuPmeThreshMinSnrMgn_Type.__name__ = "Integer32"
_EfmCuPmeThreshMinSnrMgn_Object = MibTableColumn
efmCuPmeThreshMinSnrMgn = _EfmCuPmeThreshMinSnrMgn_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 1, 1, 5),
    _EfmCuPmeThreshMinSnrMgn_Type()
)
efmCuPmeThreshMinSnrMgn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    efmCuPmeThreshMinSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    efmCuPmeThreshMinSnrMgn.setUnits("dB")


class _EfmCuPmeLineAtnCrossingEnable_Type(TruthValue):
    """Custom type efmCuPmeLineAtnCrossingEnable based on TruthValue"""


_EfmCuPmeLineAtnCrossingEnable_Object = MibTableColumn
efmCuPmeLineAtnCrossingEnable = _EfmCuPmeLineAtnCrossingEnable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 1, 1, 6),
    _EfmCuPmeLineAtnCrossingEnable_Type()
)
efmCuPmeLineAtnCrossingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    efmCuPmeLineAtnCrossingEnable.setStatus("current")


class _EfmCuPmeSnrMgnCrossingTrapEnable_Type(TruthValue):
    """Custom type efmCuPmeSnrMgnCrossingTrapEnable based on TruthValue"""


_EfmCuPmeSnrMgnCrossingTrapEnable_Object = MibTableColumn
efmCuPmeSnrMgnCrossingTrapEnable = _EfmCuPmeSnrMgnCrossingTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 1, 1, 7),
    _EfmCuPmeSnrMgnCrossingTrapEnable_Type()
)
efmCuPmeSnrMgnCrossingTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    efmCuPmeSnrMgnCrossingTrapEnable.setStatus("current")


class _EfmCuPmeDeviceFaultEnable_Type(TruthValue):
    """Custom type efmCuPmeDeviceFaultEnable based on TruthValue"""


_EfmCuPmeDeviceFaultEnable_Object = MibTableColumn
efmCuPmeDeviceFaultEnable = _EfmCuPmeDeviceFaultEnable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 1, 1, 8),
    _EfmCuPmeDeviceFaultEnable_Type()
)
efmCuPmeDeviceFaultEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    efmCuPmeDeviceFaultEnable.setStatus("current")


class _EfmCuPmeConfigInitFailEnable_Type(TruthValue):
    """Custom type efmCuPmeConfigInitFailEnable based on TruthValue"""


_EfmCuPmeConfigInitFailEnable_Object = MibTableColumn
efmCuPmeConfigInitFailEnable = _EfmCuPmeConfigInitFailEnable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 1, 1, 9),
    _EfmCuPmeConfigInitFailEnable_Type()
)
efmCuPmeConfigInitFailEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    efmCuPmeConfigInitFailEnable.setStatus("current")


class _EfmCuPmeProtocolInitFailEnable_Type(TruthValue):
    """Custom type efmCuPmeProtocolInitFailEnable based on TruthValue"""


_EfmCuPmeProtocolInitFailEnable_Object = MibTableColumn
efmCuPmeProtocolInitFailEnable = _EfmCuPmeProtocolInitFailEnable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 1, 1, 10),
    _EfmCuPmeProtocolInitFailEnable_Type()
)
efmCuPmeProtocolInitFailEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    efmCuPmeProtocolInitFailEnable.setStatus("current")


class _EfmCuPmeThreshMaxSnrMgnDelta_Type(Integer32):
    """Custom type efmCuPmeThreshMaxSnrMgnDelta based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_EfmCuPmeThreshMaxSnrMgnDelta_Type.__name__ = "Integer32"
_EfmCuPmeThreshMaxSnrMgnDelta_Object = MibTableColumn
efmCuPmeThreshMaxSnrMgnDelta = _EfmCuPmeThreshMaxSnrMgnDelta_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 1, 1, 11),
    _EfmCuPmeThreshMaxSnrMgnDelta_Type()
)
efmCuPmeThreshMaxSnrMgnDelta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    efmCuPmeThreshMaxSnrMgnDelta.setStatus("current")
if mibBuilder.loadTexts:
    efmCuPmeThreshMaxSnrMgnDelta.setUnits("dB")


class _EfmCuPmeMaintenanceMode_Type(Integer32):
    """Custom type efmCuPmeMaintenanceMode based on Integer32"""
    defaultValue = 1

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
        *(("automaticContinuous", 5),
          ("automaticDaily", 4),
          ("automaticOnce", 3),
          ("manual", 2),
          ("off", 1))
    )


_EfmCuPmeMaintenanceMode_Type.__name__ = "Integer32"
_EfmCuPmeMaintenanceMode_Object = MibTableColumn
efmCuPmeMaintenanceMode = _EfmCuPmeMaintenanceMode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 1, 1, 12),
    _EfmCuPmeMaintenanceMode_Type()
)
efmCuPmeMaintenanceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    efmCuPmeMaintenanceMode.setStatus("current")


class _EfmCuPmeMaintenanceStartTime_Type(DisplayString):
    """Custom type efmCuPmeMaintenanceStartTime based on DisplayString"""
    defaultValue = OctetString("00:00")


_EfmCuPmeMaintenanceStartTime_Object = MibTableColumn
efmCuPmeMaintenanceStartTime = _EfmCuPmeMaintenanceStartTime_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 1, 1, 13),
    _EfmCuPmeMaintenanceStartTime_Type()
)
efmCuPmeMaintenanceStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    efmCuPmeMaintenanceStartTime.setStatus("current")


class _EfmCuPmeMaintenanceEndTime_Type(DisplayString):
    """Custom type efmCuPmeMaintenanceEndTime based on DisplayString"""
    defaultValue = OctetString("23:59")


_EfmCuPmeMaintenanceEndTime_Object = MibTableColumn
efmCuPmeMaintenanceEndTime = _EfmCuPmeMaintenanceEndTime_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 1, 1, 14),
    _EfmCuPmeMaintenanceEndTime_Type()
)
efmCuPmeMaintenanceEndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    efmCuPmeMaintenanceEndTime.setStatus("current")


class _EfmCuPmeSnrMonitoringInterval_Type(DisplayString):
    """Custom type efmCuPmeSnrMonitoringInterval based on DisplayString"""
    defaultValue = OctetString("01:00")


_EfmCuPmeSnrMonitoringInterval_Object = MibTableColumn
efmCuPmeSnrMonitoringInterval = _EfmCuPmeSnrMonitoringInterval_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 1, 1, 15),
    _EfmCuPmeSnrMonitoringInterval_Type()
)
efmCuPmeSnrMonitoringInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    efmCuPmeSnrMonitoringInterval.setStatus("current")


class _EfmCuPmeErrorThreshMonEnable_Type(TruthValue):
    """Custom type efmCuPmeErrorThreshMonEnable based on TruthValue"""


_EfmCuPmeErrorThreshMonEnable_Object = MibTableColumn
efmCuPmeErrorThreshMonEnable = _EfmCuPmeErrorThreshMonEnable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 1, 1, 16),
    _EfmCuPmeErrorThreshMonEnable_Type()
)
efmCuPmeErrorThreshMonEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    efmCuPmeErrorThreshMonEnable.setStatus("current")


class _EfmCuPmeErrorThreshMonNotifyEnable_Type(TruthValue):
    """Custom type efmCuPmeErrorThreshMonNotifyEnable based on TruthValue"""


_EfmCuPmeErrorThreshMonNotifyEnable_Object = MibTableColumn
efmCuPmeErrorThreshMonNotifyEnable = _EfmCuPmeErrorThreshMonNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 1, 1, 17),
    _EfmCuPmeErrorThreshMonNotifyEnable_Type()
)
efmCuPmeErrorThreshMonNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    efmCuPmeErrorThreshMonNotifyEnable.setStatus("current")


class _EfmCuPmeErrorThreshMonInterval_Type(Unsigned32):
    """Custom type efmCuPmeErrorThreshMonInterval based on Unsigned32"""
    defaultValue = 12

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 65535),
    )


_EfmCuPmeErrorThreshMonInterval_Type.__name__ = "Unsigned32"
_EfmCuPmeErrorThreshMonInterval_Object = MibTableColumn
efmCuPmeErrorThreshMonInterval = _EfmCuPmeErrorThreshMonInterval_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 1, 1, 18),
    _EfmCuPmeErrorThreshMonInterval_Type()
)
efmCuPmeErrorThreshMonInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    efmCuPmeErrorThreshMonInterval.setStatus("current")


class _EfmCuPmeErrorThreshMonClrInterval_Type(Unsigned32):
    """Custom type efmCuPmeErrorThreshMonClrInterval based on Unsigned32"""
    defaultValue = 1800

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 65535),
    )


_EfmCuPmeErrorThreshMonClrInterval_Type.__name__ = "Unsigned32"
_EfmCuPmeErrorThreshMonClrInterval_Object = MibTableColumn
efmCuPmeErrorThreshMonClrInterval = _EfmCuPmeErrorThreshMonClrInterval_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 1, 1, 19),
    _EfmCuPmeErrorThreshMonClrInterval_Type()
)
efmCuPmeErrorThreshMonClrInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    efmCuPmeErrorThreshMonClrInterval.setStatus("current")


class _EfmCuPmeLinkTrfcDisablTrapEnable_Type(Integer32):
    """Custom type efmCuPmeLinkTrfcDisablTrapEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_EfmCuPmeLinkTrfcDisablTrapEnable_Type.__name__ = "Integer32"
_EfmCuPmeLinkTrfcDisablTrapEnable_Object = MibTableColumn
efmCuPmeLinkTrfcDisablTrapEnable = _EfmCuPmeLinkTrfcDisablTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 1, 1, 20),
    _EfmCuPmeLinkTrfcDisablTrapEnable_Type()
)
efmCuPmeLinkTrfcDisablTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    efmCuPmeLinkTrfcDisablTrapEnable.setStatus("current")
_EfmCuPmeCapabilityTable_Object = MibTable
efmCuPmeCapabilityTable = _EfmCuPmeCapabilityTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 2)
)
if mibBuilder.loadTexts:
    efmCuPmeCapabilityTable.setStatus("current")
_EfmCuPmeCapabilityEntry_Object = MibTableRow
efmCuPmeCapabilityEntry = _EfmCuPmeCapabilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 2, 1)
)
efmCuPmeCapabilityEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    efmCuPmeCapabilityEntry.setStatus("current")


class _EfmCuPmeSubTypesSupported_Type(Bits):
    """Custom type efmCuPmeSubTypesSupported based on Bits"""
    namedValues = NamedValues(
        *(("ieee10PassTSO", 2),
          ("ieee10PassTSR", 3),
          ("ieee2BaseTLO", 0),
          ("ieee2BaseTLR", 1))
    )

_EfmCuPmeSubTypesSupported_Type.__name__ = "Bits"
_EfmCuPmeSubTypesSupported_Object = MibTableColumn
efmCuPmeSubTypesSupported = _EfmCuPmeSubTypesSupported_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 2, 1, 1),
    _EfmCuPmeSubTypesSupported_Type()
)
efmCuPmeSubTypesSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efmCuPmeSubTypesSupported.setStatus("current")
_EfmCuPmeStatusTable_Object = MibTable
efmCuPmeStatusTable = _EfmCuPmeStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 3)
)
if mibBuilder.loadTexts:
    efmCuPmeStatusTable.setStatus("current")
_EfmCuPmeStatusEntry_Object = MibTableRow
efmCuPmeStatusEntry = _EfmCuPmeStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 3, 1)
)
efmCuPmeStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    efmCuPmeStatusEntry.setStatus("current")


class _EfmCuPmeOperStatus_Type(Integer32):
    """Custom type efmCuPmeOperStatus based on Integer32"""
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
        *(("downNotReady", 2),
          ("downReady", 3),
          ("init", 4),
          ("up", 1))
    )


_EfmCuPmeOperStatus_Type.__name__ = "Integer32"
_EfmCuPmeOperStatus_Object = MibTableColumn
efmCuPmeOperStatus = _EfmCuPmeOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 3, 1, 1),
    _EfmCuPmeOperStatus_Type()
)
efmCuPmeOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efmCuPmeOperStatus.setStatus("current")


class _EfmCuPmeFltStatus_Type(Bits):
    """Custom type efmCuPmeFltStatus based on Bits"""
    namedValues = NamedValues(
        *(("configInitFailure", 4),
          ("deviceFault", 3),
          ("lineAtnDefect", 2),
          ("lossOfFraming", 0),
          ("protocolInitFailure", 5),
          ("snrMgnDefect", 1))
    )

_EfmCuPmeFltStatus_Type.__name__ = "Bits"
_EfmCuPmeFltStatus_Object = MibTableColumn
efmCuPmeFltStatus = _EfmCuPmeFltStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 3, 1, 2),
    _EfmCuPmeFltStatus_Type()
)
efmCuPmeFltStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efmCuPmeFltStatus.setStatus("current")


class _EfmCuPmeOperSubType_Type(Integer32):
    """Custom type efmCuPmeOperSubType based on Integer32"""
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
        *(("ieee10PassTSO", 3),
          ("ieee10PassTSR", 4),
          ("ieee2BaseTLO", 1),
          ("ieee2BaseTLR", 2))
    )


_EfmCuPmeOperSubType_Type.__name__ = "Integer32"
_EfmCuPmeOperSubType_Object = MibTableColumn
efmCuPmeOperSubType = _EfmCuPmeOperSubType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 3, 1, 3),
    _EfmCuPmeOperSubType_Type()
)
efmCuPmeOperSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efmCuPmeOperSubType.setStatus("current")
_EfmCuPmeOperProfile_Type = ProfileIndexOrZero
_EfmCuPmeOperProfile_Object = MibTableColumn
efmCuPmeOperProfile = _EfmCuPmeOperProfile_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 3, 1, 4),
    _EfmCuPmeOperProfile_Type()
)
efmCuPmeOperProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efmCuPmeOperProfile.setStatus("current")


class _EfmCuPmeSnrMgn_Type(Integer32):
    """Custom type efmCuPmeSnrMgn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-127, 128),
        ValueRangeConstraint(65535, 65535),
    )


_EfmCuPmeSnrMgn_Type.__name__ = "Integer32"
_EfmCuPmeSnrMgn_Object = MibTableColumn
efmCuPmeSnrMgn = _EfmCuPmeSnrMgn_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 3, 1, 5),
    _EfmCuPmeSnrMgn_Type()
)
efmCuPmeSnrMgn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efmCuPmeSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    efmCuPmeSnrMgn.setUnits("dB")


class _EfmCuPmePeerSnrMgn_Type(Integer32):
    """Custom type efmCuPmePeerSnrMgn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-127, 128),
        ValueRangeConstraint(65535, 65535),
    )


_EfmCuPmePeerSnrMgn_Type.__name__ = "Integer32"
_EfmCuPmePeerSnrMgn_Object = MibTableColumn
efmCuPmePeerSnrMgn = _EfmCuPmePeerSnrMgn_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 3, 1, 6),
    _EfmCuPmePeerSnrMgn_Type()
)
efmCuPmePeerSnrMgn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efmCuPmePeerSnrMgn.setStatus("current")
if mibBuilder.loadTexts:
    efmCuPmePeerSnrMgn.setUnits("dB")


class _EfmCuPmeLineAtn_Type(Integer32):
    """Custom type efmCuPmeLineAtn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-127, 128),
        ValueRangeConstraint(65535, 65535),
    )


_EfmCuPmeLineAtn_Type.__name__ = "Integer32"
_EfmCuPmeLineAtn_Object = MibTableColumn
efmCuPmeLineAtn = _EfmCuPmeLineAtn_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 3, 1, 7),
    _EfmCuPmeLineAtn_Type()
)
efmCuPmeLineAtn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efmCuPmeLineAtn.setStatus("current")
if mibBuilder.loadTexts:
    efmCuPmeLineAtn.setUnits("dB")


class _EfmCuPmePeerLineAtn_Type(Integer32):
    """Custom type efmCuPmePeerLineAtn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-127, 128),
        ValueRangeConstraint(65535, 65535),
    )


_EfmCuPmePeerLineAtn_Type.__name__ = "Integer32"
_EfmCuPmePeerLineAtn_Object = MibTableColumn
efmCuPmePeerLineAtn = _EfmCuPmePeerLineAtn_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 3, 1, 8),
    _EfmCuPmePeerLineAtn_Type()
)
efmCuPmePeerLineAtn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efmCuPmePeerLineAtn.setStatus("current")
if mibBuilder.loadTexts:
    efmCuPmePeerLineAtn.setUnits("dB")
_EfmCuPmeTCCodingErrors_Type = Counter32
_EfmCuPmeTCCodingErrors_Object = MibTableColumn
efmCuPmeTCCodingErrors = _EfmCuPmeTCCodingErrors_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 3, 1, 9),
    _EfmCuPmeTCCodingErrors_Type()
)
efmCuPmeTCCodingErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efmCuPmeTCCodingErrors.setStatus("current")
_EfmCuPmeTCCrcErrors_Type = Counter32
_EfmCuPmeTCCrcErrors_Object = MibTableColumn
efmCuPmeTCCrcErrors = _EfmCuPmeTCCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 3, 1, 10),
    _EfmCuPmeTCCrcErrors_Type()
)
efmCuPmeTCCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efmCuPmeTCCrcErrors.setStatus("current")
_EfmCuPmeSnrCrossingCnt_Type = Counter32
_EfmCuPmeSnrCrossingCnt_Object = MibTableColumn
efmCuPmeSnrCrossingCnt = _EfmCuPmeSnrCrossingCnt_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 3, 1, 11),
    _EfmCuPmeSnrCrossingCnt_Type()
)
efmCuPmeSnrCrossingCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efmCuPmeSnrCrossingCnt.setStatus("current")
_EfmCuPmeTCDownCnt_Type = Counter32
_EfmCuPmeTCDownCnt_Object = MibTableColumn
efmCuPmeTCDownCnt = _EfmCuPmeTCDownCnt_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 3, 1, 12),
    _EfmCuPmeTCDownCnt_Type()
)
efmCuPmeTCDownCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efmCuPmeTCDownCnt.setStatus("current")
_EfmCuPmeErrorTCDownCnt_Type = Counter32
_EfmCuPmeErrorTCDownCnt_Object = MibTableColumn
efmCuPmeErrorTCDownCnt = _EfmCuPmeErrorTCDownCnt_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 3, 1, 13),
    _EfmCuPmeErrorTCDownCnt_Type()
)
efmCuPmeErrorTCDownCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efmCuPmeErrorTCDownCnt.setStatus("current")
_EfmCuPmeErrorRestartCnt_Type = Counter32
_EfmCuPmeErrorRestartCnt_Object = MibTableColumn
efmCuPmeErrorRestartCnt = _EfmCuPmeErrorRestartCnt_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 3, 1, 14),
    _EfmCuPmeErrorRestartCnt_Type()
)
efmCuPmeErrorRestartCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efmCuPmeErrorRestartCnt.setStatus("current")
_EfmCuPmeSnrRestartCnt_Type = Counter32
_EfmCuPmeSnrRestartCnt_Object = MibTableColumn
efmCuPmeSnrRestartCnt = _EfmCuPmeSnrRestartCnt_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 3, 1, 15),
    _EfmCuPmeSnrRestartCnt_Type()
)
efmCuPmeSnrRestartCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efmCuPmeSnrRestartCnt.setStatus("current")
_EfmCuPmeErrorConsecutiveSec_Type = Counter32
_EfmCuPmeErrorConsecutiveSec_Object = MibTableColumn
efmCuPmeErrorConsecutiveSec = _EfmCuPmeErrorConsecutiveSec_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 3, 1, 16),
    _EfmCuPmeErrorConsecutiveSec_Type()
)
efmCuPmeErrorConsecutiveSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efmCuPmeErrorConsecutiveSec.setStatus("current")
_EfmCuPmeErrorMaxConsecutiveSec_Type = Counter32
_EfmCuPmeErrorMaxConsecutiveSec_Object = MibTableColumn
efmCuPmeErrorMaxConsecutiveSec = _EfmCuPmeErrorMaxConsecutiveSec_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 3, 1, 17),
    _EfmCuPmeErrorMaxConsecutiveSec_Type()
)
efmCuPmeErrorMaxConsecutiveSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efmCuPmeErrorMaxConsecutiveSec.setStatus("current")
_EfmCuPme2B_ObjectIdentity = ObjectIdentity
efmCuPme2B = _EfmCuPme2B_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 5)
)
_EfmCuPme2BProfileTable_Object = MibTable
efmCuPme2BProfileTable = _EfmCuPme2BProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 5, 2)
)
if mibBuilder.loadTexts:
    efmCuPme2BProfileTable.setStatus("current")
_EfmCuPme2BProfileEntry_Object = MibTableRow
efmCuPme2BProfileEntry = _EfmCuPme2BProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 5, 2, 1)
)
efmCuPme2BProfileEntry.setIndexNames(
    (0, "EFM-CU-MIB", "efmCuPme2BProfileIndex"),
)
if mibBuilder.loadTexts:
    efmCuPme2BProfileEntry.setStatus("current")
_EfmCuPme2BProfileIndex_Type = ProfileIndex
_EfmCuPme2BProfileIndex_Object = MibTableColumn
efmCuPme2BProfileIndex = _EfmCuPme2BProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 5, 2, 1, 1),
    _EfmCuPme2BProfileIndex_Type()
)
efmCuPme2BProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    efmCuPme2BProfileIndex.setStatus("current")


class _EfmCuPme2BProfileDescr_Type(SnmpAdminString):
    """Custom type efmCuPme2BProfileDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EfmCuPme2BProfileDescr_Type.__name__ = "SnmpAdminString"
_EfmCuPme2BProfileDescr_Object = MibTableColumn
efmCuPme2BProfileDescr = _EfmCuPme2BProfileDescr_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 5, 2, 1, 2),
    _EfmCuPme2BProfileDescr_Type()
)
efmCuPme2BProfileDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    efmCuPme2BProfileDescr.setStatus("current")


class _EfmCuPme2BRegion_Type(Integer32):
    """Custom type efmCuPme2BRegion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("region1", 1),
          ("region2", 2))
    )


_EfmCuPme2BRegion_Type.__name__ = "Integer32"
_EfmCuPme2BRegion_Object = MibTableColumn
efmCuPme2BRegion = _EfmCuPme2BRegion_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 5, 2, 1, 3),
    _EfmCuPme2BRegion_Type()
)
efmCuPme2BRegion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    efmCuPme2BRegion.setStatus("current")


class _EfmCuPme2BDataRate_Type(Unsigned32):
    """Custom type efmCuPme2BDataRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15352),
    )


_EfmCuPme2BDataRate_Type.__name__ = "Unsigned32"
_EfmCuPme2BDataRate_Object = MibTableColumn
efmCuPme2BDataRate = _EfmCuPme2BDataRate_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 5, 2, 1, 4),
    _EfmCuPme2BDataRate_Type()
)
efmCuPme2BDataRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    efmCuPme2BDataRate.setStatus("current")
if mibBuilder.loadTexts:
    efmCuPme2BDataRate.setUnits("Kbps")


class _EfmCuPme2BPower_Type(Unsigned32):
    """Custom type efmCuPme2BPower based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 42),
    )


_EfmCuPme2BPower_Type.__name__ = "Unsigned32"
_EfmCuPme2BPower_Object = MibTableColumn
efmCuPme2BPower = _EfmCuPme2BPower_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 5, 2, 1, 5),
    _EfmCuPme2BPower_Type()
)
efmCuPme2BPower.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    efmCuPme2BPower.setStatus("current")
if mibBuilder.loadTexts:
    efmCuPme2BPower.setUnits("0.5 dBm")


class _EfmCuPme2BConstellation_Type(Integer32):
    """Custom type efmCuPme2BConstellation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("adaptive", 0),
          ("tcpam128", 6),
          ("tcpam16", 1),
          ("tcpam32", 2),
          ("tcpam4", 3),
          ("tcpam64", 5),
          ("tcpam8", 4))
    )


_EfmCuPme2BConstellation_Type.__name__ = "Integer32"
_EfmCuPme2BConstellation_Object = MibTableColumn
efmCuPme2BConstellation = _EfmCuPme2BConstellation_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 5, 2, 1, 6),
    _EfmCuPme2BConstellation_Type()
)
efmCuPme2BConstellation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    efmCuPme2BConstellation.setStatus("current")
_EfmCuPme2BProfileRowStatus_Type = RowStatus
_EfmCuPme2BProfileRowStatus_Object = MibTableColumn
efmCuPme2BProfileRowStatus = _EfmCuPme2BProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 5, 2, 1, 7),
    _EfmCuPme2BProfileRowStatus_Type()
)
efmCuPme2BProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    efmCuPme2BProfileRowStatus.setStatus("current")


class _EfmCuPmeNtr_Type(Integer32):
    """Custom type efmCuPmeNtr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("localOsc", 1),
          ("refClk8khz", 2))
    )


_EfmCuPmeNtr_Type.__name__ = "Integer32"
_EfmCuPmeNtr_Object = MibTableColumn
efmCuPmeNtr = _EfmCuPmeNtr_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 5, 2, 1, 8),
    _EfmCuPmeNtr_Type()
)
efmCuPmeNtr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    efmCuPmeNtr.setStatus("current")
_EfmCuPme10P_ObjectIdentity = ObjectIdentity
efmCuPme10P = _EfmCuPme10P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 6)
)
_EfmCuPme10PProfileTable_Object = MibTable
efmCuPme10PProfileTable = _EfmCuPme10PProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    efmCuPme10PProfileTable.setStatus("current")
_EfmCuPme10PProfileEntry_Object = MibTableRow
efmCuPme10PProfileEntry = _EfmCuPme10PProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 6, 1, 1)
)
efmCuPme10PProfileEntry.setIndexNames(
    (0, "EFM-CU-MIB", "efmCuPme10PProfileIndex"),
)
if mibBuilder.loadTexts:
    efmCuPme10PProfileEntry.setStatus("current")
_EfmCuPme10PProfileIndex_Type = ProfileIndex
_EfmCuPme10PProfileIndex_Object = MibTableColumn
efmCuPme10PProfileIndex = _EfmCuPme10PProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 6, 1, 1, 1),
    _EfmCuPme10PProfileIndex_Type()
)
efmCuPme10PProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    efmCuPme10PProfileIndex.setStatus("current")


class _EfmCuPme10PProfileDescr_Type(SnmpAdminString):
    """Custom type efmCuPme10PProfileDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EfmCuPme10PProfileDescr_Type.__name__ = "SnmpAdminString"
_EfmCuPme10PProfileDescr_Object = MibTableColumn
efmCuPme10PProfileDescr = _EfmCuPme10PProfileDescr_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 6, 1, 1, 2),
    _EfmCuPme10PProfileDescr_Type()
)
efmCuPme10PProfileDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    efmCuPme10PProfileDescr.setStatus("current")


class _EfmCuPme10PBandplanPSDMskProfile_Type(Integer32):
    """Custom type efmCuPme10PBandplanPSDMskProfile based on Integer32"""
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
              29)
        )
    )
    namedValues = NamedValues(
        *(("profile1", 1),
          ("profile10", 10),
          ("profile11", 11),
          ("profile12", 12),
          ("profile13", 13),
          ("profile14", 14),
          ("profile15", 15),
          ("profile16", 16),
          ("profile17", 17),
          ("profile18", 18),
          ("profile19", 19),
          ("profile2", 2),
          ("profile20", 20),
          ("profile21", 21),
          ("profile22", 22),
          ("profile23", 23),
          ("profile24", 24),
          ("profile25", 25),
          ("profile26", 26),
          ("profile27", 27),
          ("profile28", 28),
          ("profile29", 29),
          ("profile3", 3),
          ("profile4", 4),
          ("profile5", 5),
          ("profile6", 6),
          ("profile7", 7),
          ("profile8", 8),
          ("profile9", 9))
    )


_EfmCuPme10PBandplanPSDMskProfile_Type.__name__ = "Integer32"
_EfmCuPme10PBandplanPSDMskProfile_Object = MibTableColumn
efmCuPme10PBandplanPSDMskProfile = _EfmCuPme10PBandplanPSDMskProfile_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 6, 1, 1, 3),
    _EfmCuPme10PBandplanPSDMskProfile_Type()
)
efmCuPme10PBandplanPSDMskProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    efmCuPme10PBandplanPSDMskProfile.setStatus("current")


class _EfmCuPme10PUPBOReferenceProfile_Type(Integer32):
    """Custom type efmCuPme10PUPBOReferenceProfile based on Integer32"""
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
        *(("profile1", 1),
          ("profile2", 2),
          ("profile3", 3),
          ("profile4", 4),
          ("profile5", 5),
          ("profile6", 6),
          ("profile7", 7),
          ("profile8", 8),
          ("profile9", 9))
    )


_EfmCuPme10PUPBOReferenceProfile_Type.__name__ = "Integer32"
_EfmCuPme10PUPBOReferenceProfile_Object = MibTableColumn
efmCuPme10PUPBOReferenceProfile = _EfmCuPme10PUPBOReferenceProfile_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 6, 1, 1, 4),
    _EfmCuPme10PUPBOReferenceProfile_Type()
)
efmCuPme10PUPBOReferenceProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    efmCuPme10PUPBOReferenceProfile.setStatus("current")


class _EfmCuPme10PBandNotchProfiles_Type(Bits):
    """Custom type efmCuPme10PBandNotchProfiles based on Bits"""
    namedValues = NamedValues(
        *(("profile0", 0),
          ("profile1", 1),
          ("profile10", 10),
          ("profile11", 11),
          ("profile2", 2),
          ("profile3", 3),
          ("profile4", 4),
          ("profile5", 5),
          ("profile6", 6),
          ("profile7", 7),
          ("profile8", 8),
          ("profile9", 9))
    )

_EfmCuPme10PBandNotchProfiles_Type.__name__ = "Bits"
_EfmCuPme10PBandNotchProfiles_Object = MibTableColumn
efmCuPme10PBandNotchProfiles = _EfmCuPme10PBandNotchProfiles_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 6, 1, 1, 5),
    _EfmCuPme10PBandNotchProfiles_Type()
)
efmCuPme10PBandNotchProfiles.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    efmCuPme10PBandNotchProfiles.setStatus("current")


class _EfmCuPme10PPayloadURateProfile_Type(Integer32):
    """Custom type efmCuPme10PPayloadURateProfile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              10,
              15,
              20,
              25,
              30,
              50,
              70,
              100)
        )
    )
    namedValues = NamedValues(
        *(("profile10", 10),
          ("profile100", 100),
          ("profile15", 15),
          ("profile20", 20),
          ("profile25", 25),
          ("profile30", 30),
          ("profile5", 5),
          ("profile50", 50),
          ("profile70", 70))
    )


_EfmCuPme10PPayloadURateProfile_Type.__name__ = "Integer32"
_EfmCuPme10PPayloadURateProfile_Object = MibTableColumn
efmCuPme10PPayloadURateProfile = _EfmCuPme10PPayloadURateProfile_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 6, 1, 1, 6),
    _EfmCuPme10PPayloadURateProfile_Type()
)
efmCuPme10PPayloadURateProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    efmCuPme10PPayloadURateProfile.setStatus("current")


class _EfmCuPme10PPayloadDRateProfile_Type(Integer32):
    """Custom type efmCuPme10PPayloadDRateProfile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              10,
              15,
              20,
              25,
              30,
              50,
              70,
              100,
              140,
              200)
        )
    )
    namedValues = NamedValues(
        *(("profile10", 10),
          ("profile100", 100),
          ("profile140", 140),
          ("profile15", 15),
          ("profile20", 20),
          ("profile200", 200),
          ("profile25", 25),
          ("profile30", 30),
          ("profile5", 5),
          ("profile50", 50),
          ("profile70", 70))
    )


_EfmCuPme10PPayloadDRateProfile_Type.__name__ = "Integer32"
_EfmCuPme10PPayloadDRateProfile_Object = MibTableColumn
efmCuPme10PPayloadDRateProfile = _EfmCuPme10PPayloadDRateProfile_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 6, 1, 1, 7),
    _EfmCuPme10PPayloadDRateProfile_Type()
)
efmCuPme10PPayloadDRateProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    efmCuPme10PPayloadDRateProfile.setStatus("current")
_EfmCuPme10PProfileRowStatus_Type = RowStatus
_EfmCuPme10PProfileRowStatus_Object = MibTableColumn
efmCuPme10PProfileRowStatus = _EfmCuPme10PProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 6, 1, 1, 8),
    _EfmCuPme10PProfileRowStatus_Type()
)
efmCuPme10PProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    efmCuPme10PProfileRowStatus.setStatus("current")
_EfmCuPme10PStatusTable_Object = MibTable
efmCuPme10PStatusTable = _EfmCuPme10PStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 6, 2)
)
if mibBuilder.loadTexts:
    efmCuPme10PStatusTable.setStatus("current")
_EfmCuPme10PStatusEntry_Object = MibTableRow
efmCuPme10PStatusEntry = _EfmCuPme10PStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 6, 2, 1)
)
if mibBuilder.loadTexts:
    efmCuPme10PStatusEntry.setStatus("current")


class _EfmCuPme10PElectricalLength_Type(Integer32):
    """Custom type efmCuPme10PElectricalLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8192),
        ValueRangeConstraint(65535, 65535),
    )


_EfmCuPme10PElectricalLength_Type.__name__ = "Integer32"
_EfmCuPme10PElectricalLength_Object = MibTableColumn
efmCuPme10PElectricalLength = _EfmCuPme10PElectricalLength_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 6, 2, 1, 1),
    _EfmCuPme10PElectricalLength_Type()
)
efmCuPme10PElectricalLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efmCuPme10PElectricalLength.setStatus("current")
if mibBuilder.loadTexts:
    efmCuPme10PElectricalLength.setUnits("m")
_EfmCuPme10PFECCorrectedBlocks_Type = Counter32
_EfmCuPme10PFECCorrectedBlocks_Object = MibTableColumn
efmCuPme10PFECCorrectedBlocks = _EfmCuPme10PFECCorrectedBlocks_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 6, 2, 1, 2),
    _EfmCuPme10PFECCorrectedBlocks_Type()
)
efmCuPme10PFECCorrectedBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efmCuPme10PFECCorrectedBlocks.setStatus("current")
_EfmCuPme10PFECUncorrectedBlocks_Type = Counter32
_EfmCuPme10PFECUncorrectedBlocks_Object = MibTableColumn
efmCuPme10PFECUncorrectedBlocks = _EfmCuPme10PFECUncorrectedBlocks_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 6, 2, 1, 3),
    _EfmCuPme10PFECUncorrectedBlocks_Type()
)
efmCuPme10PFECUncorrectedBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efmCuPme10PFECUncorrectedBlocks.setStatus("current")
_IfAvailableStackTable_Object = MibTable
ifAvailableStackTable = _IfAvailableStackTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 3)
)
if mibBuilder.loadTexts:
    ifAvailableStackTable.setStatus("current")
_IfAvailableStackEntry_Object = MibTableRow
ifAvailableStackEntry = _IfAvailableStackEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 3, 1)
)
ifAvailableStackEntry.setIndexNames(
    (0, "EFM-CU-MIB", "ifAvailableStackHigherLayer"),
    (0, "EFM-CU-MIB", "ifAvailableStackLowerLayer"),
)
if mibBuilder.loadTexts:
    ifAvailableStackEntry.setStatus("current")
_IfAvailableStackHigherLayer_Type = InterfaceIndex
_IfAvailableStackHigherLayer_Object = MibTableColumn
ifAvailableStackHigherLayer = _IfAvailableStackHigherLayer_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 3, 1, 1),
    _IfAvailableStackHigherLayer_Type()
)
ifAvailableStackHigherLayer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ifAvailableStackHigherLayer.setStatus("current")
_IfAvailableStackLowerLayer_Type = InterfaceIndex
_IfAvailableStackLowerLayer_Object = MibTableColumn
ifAvailableStackLowerLayer = _IfAvailableStackLowerLayer_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 3, 1, 2),
    _IfAvailableStackLowerLayer_Type()
)
ifAvailableStackLowerLayer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ifAvailableStackLowerLayer.setStatus("current")


class _IfAvailableStackStatus_Type(Integer32):
    """Custom type ifAvailableStackStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("capable", 1),
          ("outOfService", 2))
    )


_IfAvailableStackStatus_Type.__name__ = "Integer32"
_IfAvailableStackStatus_Object = MibTableColumn
ifAvailableStackStatus = _IfAvailableStackStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 3, 1, 3),
    _IfAvailableStackStatus_Type()
)
ifAvailableStackStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifAvailableStackStatus.setStatus("current")
_EfmCuRegeneratorStats_ObjectIdentity = ObjectIdentity
efmCuRegeneratorStats = _EfmCuRegeneratorStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 4)
)
_EfmCuRegeneratorStatusTable_Object = MibTable
efmCuRegeneratorStatusTable = _EfmCuRegeneratorStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 4, 1)
)
if mibBuilder.loadTexts:
    efmCuRegeneratorStatusTable.setStatus("current")
_EfmCuRegeneratorStatusEntry_Object = MibTableRow
efmCuRegeneratorStatusEntry = _EfmCuRegeneratorStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 4, 1, 1)
)
efmCuRegeneratorStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "EFM-CU-MIB", "efmCuRegenIndex"),
    (0, "EFM-CU-MIB", "efmCuRegenSide"),
)
if mibBuilder.loadTexts:
    efmCuRegeneratorStatusEntry.setStatus("current")


class _EfmCuRegenIndex_Type(Integer32):
    """Custom type efmCuRegenIndex based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("ltu-c", 1),
          ("ltu-r", 2),
          ("regenerator-1", 3),
          ("regenerator-2", 4),
          ("regenerator-3", 5),
          ("regenerator-4", 6),
          ("regenerator-5", 7),
          ("regenerator-6", 8),
          ("regenerator-7", 9),
          ("regenerator-8", 10))
    )


_EfmCuRegenIndex_Type.__name__ = "Integer32"
_EfmCuRegenIndex_Object = MibTableColumn
efmCuRegenIndex = _EfmCuRegenIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 4, 1, 1, 1),
    _EfmCuRegenIndex_Type()
)
efmCuRegenIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    efmCuRegenIndex.setStatus("current")
if mibBuilder.loadTexts:
    efmCuRegenIndex.setUnits("Address")


class _EfmCuRegenSide_Type(Integer32):
    """Custom type efmCuRegenSide based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("customer", 2),
          ("network", 1))
    )


_EfmCuRegenSide_Type.__name__ = "Integer32"
_EfmCuRegenSide_Object = MibTableColumn
efmCuRegenSide = _EfmCuRegenSide_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 4, 1, 1, 2),
    _EfmCuRegenSide_Type()
)
efmCuRegenSide.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    efmCuRegenSide.setStatus("current")
if mibBuilder.loadTexts:
    efmCuRegenSide.setUnits("Side")
_EfmCuRegenSNR_Type = Integer32
_EfmCuRegenSNR_Object = MibTableColumn
efmCuRegenSNR = _EfmCuRegenSNR_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 4, 1, 1, 3),
    _EfmCuRegenSNR_Type()
)
efmCuRegenSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efmCuRegenSNR.setStatus("current")
if mibBuilder.loadTexts:
    efmCuRegenSNR.setUnits("tenths of dB")
_EfmCuRegenLineAttn_Type = Integer32
_EfmCuRegenLineAttn_Object = MibTableColumn
efmCuRegenLineAttn = _EfmCuRegenLineAttn_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 4, 1, 1, 4),
    _EfmCuRegenLineAttn_Type()
)
efmCuRegenLineAttn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efmCuRegenLineAttn.setStatus("current")
if mibBuilder.loadTexts:
    efmCuRegenLineAttn.setUnits("tenths of dB")
_EfmCuRegenCRC_Type = Counter32
_EfmCuRegenCRC_Object = MibTableColumn
efmCuRegenCRC = _EfmCuRegenCRC_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 4, 1, 1, 5),
    _EfmCuRegenCRC_Type()
)
efmCuRegenCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efmCuRegenCRC.setStatus("current")
if mibBuilder.loadTexts:
    efmCuRegenCRC.setUnits("Errors")
_EfmCuRegenES_Type = Counter32
_EfmCuRegenES_Object = MibTableColumn
efmCuRegenES = _EfmCuRegenES_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 4, 1, 1, 6),
    _EfmCuRegenES_Type()
)
efmCuRegenES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efmCuRegenES.setStatus("current")
if mibBuilder.loadTexts:
    efmCuRegenES.setUnits("Seconds")
_EfmCuRegenSES_Type = Counter32
_EfmCuRegenSES_Object = MibTableColumn
efmCuRegenSES = _EfmCuRegenSES_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 4, 1, 1, 7),
    _EfmCuRegenSES_Type()
)
efmCuRegenSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efmCuRegenSES.setStatus("current")
if mibBuilder.loadTexts:
    efmCuRegenSES.setUnits("Seconds")
_EfmCuRegenUAS_Type = Counter32
_EfmCuRegenUAS_Object = MibTableColumn
efmCuRegenUAS = _EfmCuRegenUAS_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 4, 1, 1, 8),
    _EfmCuRegenUAS_Type()
)
efmCuRegenUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efmCuRegenUAS.setStatus("current")
if mibBuilder.loadTexts:
    efmCuRegenUAS.setUnits("Seconds")
_EfmCuRegenLOSWS_Type = Counter32
_EfmCuRegenLOSWS_Object = MibTableColumn
efmCuRegenLOSWS = _EfmCuRegenLOSWS_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 4, 1, 1, 9),
    _EfmCuRegenLOSWS_Type()
)
efmCuRegenLOSWS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efmCuRegenLOSWS.setStatus("current")
if mibBuilder.loadTexts:
    efmCuRegenLOSWS.setUnits("Seconds")


class _EfmCuRegenDCAlarm_Type(Integer32):
    """Custom type efmCuRegenDCAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_EfmCuRegenDCAlarm_Type.__name__ = "Integer32"
_EfmCuRegenDCAlarm_Object = MibTableColumn
efmCuRegenDCAlarm = _EfmCuRegenDCAlarm_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 4, 1, 1, 10),
    _EfmCuRegenDCAlarm_Type()
)
efmCuRegenDCAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efmCuRegenDCAlarm.setStatus("current")
if mibBuilder.loadTexts:
    efmCuRegenDCAlarm.setUnits("Alarm")


class _EfmCuRegenClearCounts_Type(Integer32):
    """Custom type efmCuRegenClearCounts based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clearCounts", 2),
          ("normalCounts", 1))
    )


_EfmCuRegenClearCounts_Type.__name__ = "Integer32"
_EfmCuRegenClearCounts_Object = MibTableColumn
efmCuRegenClearCounts = _EfmCuRegenClearCounts_Object(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 4, 1, 1, 11),
    _EfmCuRegenClearCounts_Type()
)
efmCuRegenClearCounts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    efmCuRegenClearCounts.setStatus("current")
_EfmCuConformance_ObjectIdentity = ObjectIdentity
efmCuConformance = _EfmCuConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 2)
)
_EfmCuGroups_ObjectIdentity = ObjectIdentity
efmCuGroups = _EfmCuGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 2, 1)
)
_EfmCuCompliances_ObjectIdentity = ObjectIdentity
efmCuCompliances = _EfmCuCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 2, 2)
)
efmCuPmeStatusEntry.registerAugmentions(
    ("EFM-CU-MIB",
     "efmCuPme10PStatusEntry")
)
efmCuPme10PStatusEntry.setIndexNames(*efmCuPmeStatusEntry.getIndexNames())

# Managed Objects groups

efmCuBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 2, 1, 1)
)
efmCuBasicGroup.setObjects(
      *(("EFM-CU-MIB", "efmCuPAFSupported"),
        ("EFM-CU-MIB", "efmCuAdminProfile"),
        ("EFM-CU-MIB", "efmCuTargetDataRate"),
        ("EFM-CU-MIB", "efmCuTargetWorstCaseSnrMgn"),
        ("EFM-CU-MIB", "efmCuPortSide"),
        ("EFM-CU-MIB", "efmCuFltStatus"),
        ("EFM-CU-MIB", "efmCuTargetCurrentConditionMode"),
        ("EFM-CU-MIB", "efmCuTargetCurrentConditionSnrMgn"),
        ("EFM-CU-MIB", "efmCuTargetWorstCaseMode"))
)
if mibBuilder.loadTexts:
    efmCuBasicGroup.setStatus("current")

efmCuPAFGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 2, 1, 2)
)
efmCuPAFGroup.setObjects(
      *(("EFM-CU-MIB", "efmCuPeerPAFSupported"),
        ("EFM-CU-MIB", "efmCuPAFCapacity"),
        ("EFM-CU-MIB", "efmCuPeerPAFCapacity"),
        ("EFM-CU-MIB", "efmCuPAFAdminState"),
        ("EFM-CU-MIB", "efmCuPAFDiscoveryCode"),
        ("EFM-CU-MIB", "efmCuPAFRemoteDiscoveryCode"),
        ("EFM-CU-MIB", "efmCuNumPMEs"),
        ("EFM-CU-MIB", "ifAvailableStackStatus"))
)
if mibBuilder.loadTexts:
    efmCuPAFGroup.setStatus("current")

ifStackCapabilityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 2, 1, 3)
)
ifStackCapabilityGroup.setObjects(
    ("EFM-CU-MIB", "ifAvailableStackStatus")
)
if mibBuilder.loadTexts:
    ifStackCapabilityGroup.setStatus("current")

efmCuPAFErrorsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 2, 1, 4)
)
efmCuPAFErrorsGroup.setObjects(
      *(("EFM-CU-MIB", "efmCuPAFInErrors"),
        ("EFM-CU-MIB", "efmCuPAFInSmallFragments"),
        ("EFM-CU-MIB", "efmCuPAFInLargeFragments"),
        ("EFM-CU-MIB", "efmCuPAFInBadFragments"),
        ("EFM-CU-MIB", "efmCuPAFInLostFragments"),
        ("EFM-CU-MIB", "efmCuPAFInLostStarts"),
        ("EFM-CU-MIB", "efmCuPAFInLostEnds"),
        ("EFM-CU-MIB", "efmCuPAFInOverflows"))
)
if mibBuilder.loadTexts:
    efmCuPAFErrorsGroup.setStatus("current")

efmCuPmeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 2, 1, 5)
)
efmCuPmeGroup.setObjects(
      *(("EFM-CU-MIB", "efmCuPmeAdminProfile"),
        ("EFM-CU-MIB", "efmCuPmeOperStatus"),
        ("EFM-CU-MIB", "efmCuPmeFltStatus"),
        ("EFM-CU-MIB", "efmCuPmeSubTypesSupported"),
        ("EFM-CU-MIB", "efmCuPmeAdminSubType"),
        ("EFM-CU-MIB", "efmCuPmeOperSubType"),
        ("EFM-CU-MIB", "efmCuPAFRemoteDiscoveryCode"),
        ("EFM-CU-MIB", "efmCuPmeOperProfile"),
        ("EFM-CU-MIB", "efmCuPmeSnrMgn"),
        ("EFM-CU-MIB", "efmCuPmePeerSnrMgn"),
        ("EFM-CU-MIB", "efmCuPmeLineAtn"),
        ("EFM-CU-MIB", "efmCuPmePeerLineAtn"),
        ("EFM-CU-MIB", "efmCuPmeTCCodingErrors"),
        ("EFM-CU-MIB", "efmCuPmeTCCrcErrors"),
        ("EFM-CU-MIB", "efmCuPmeThreshLineAtn"),
        ("EFM-CU-MIB", "efmCuPmeThreshMinSnrMgn"),
        ("EFM-CU-MIB", "efmCuPmeThreshMaxSnrMgnDelta"))
)
if mibBuilder.loadTexts:
    efmCuPmeGroup.setStatus("current")

efmCuAlarmConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 2, 1, 6)
)
efmCuAlarmConfGroup.setObjects(
      *(("EFM-CU-MIB", "efmCuThreshLowBandwidth"),
        ("EFM-CU-MIB", "efmCuLowBandwidthEnable"),
        ("EFM-CU-MIB", "efmCuPmeThreshLineAtn"),
        ("EFM-CU-MIB", "efmCuPmeLineAtnCrossingEnable"),
        ("EFM-CU-MIB", "efmCuPmeThreshMinSnrMgn"),
        ("EFM-CU-MIB", "efmCuPmeSnrMgnCrossingTrapEnable"),
        ("EFM-CU-MIB", "efmCuPmeLineAtnCrossingEnable"),
        ("EFM-CU-MIB", "efmCuPmeDeviceFaultEnable"),
        ("EFM-CU-MIB", "efmCuPmeConfigInitFailEnable"),
        ("EFM-CU-MIB", "efmCuPmeProtocolInitFailEnable"),
        ("EFM-CU-MIB", "efmCuPmeThreshMaxSnrMgnDelta"),
        ("EFM-CU-MIB", "efmCuPmeMaintenanceMode"),
        ("EFM-CU-MIB", "efmCuPmeMaintenanceStartTime"),
        ("EFM-CU-MIB", "efmCuPmeMaintenanceEndTime"),
        ("EFM-CU-MIB", "efmCuPmeSnrMonitoringInterval"))
)
if mibBuilder.loadTexts:
    efmCuAlarmConfGroup.setStatus("current")

efmCuPme2BProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 2, 1, 8)
)
efmCuPme2BProfileGroup.setObjects(
      *(("EFM-CU-MIB", "efmCuPme2BProfileDescr"),
        ("EFM-CU-MIB", "efmCuPme2BRegion"),
        ("EFM-CU-MIB", "efmCuPme2BDataRate"),
        ("EFM-CU-MIB", "efmCuPme2BPower"),
        ("EFM-CU-MIB", "efmCuPme2BConstellation"),
        ("EFM-CU-MIB", "efmCuPme2BProfileRowStatus"))
)
if mibBuilder.loadTexts:
    efmCuPme2BProfileGroup.setStatus("current")

efmCuPme10PProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 2, 1, 9)
)
efmCuPme10PProfileGroup.setObjects(
      *(("EFM-CU-MIB", "efmCuPme10PProfileDescr"),
        ("EFM-CU-MIB", "efmCuPme10PBandplanPSDMskProfile"),
        ("EFM-CU-MIB", "efmCuPme10PUPBOReferenceProfile"),
        ("EFM-CU-MIB", "efmCuPme10PBandNotchProfiles"),
        ("EFM-CU-MIB", "efmCuPme10PPayloadURateProfile"),
        ("EFM-CU-MIB", "efmCuPme10PPayloadDRateProfile"),
        ("EFM-CU-MIB", "efmCuPme10PProfileRowStatus"))
)
if mibBuilder.loadTexts:
    efmCuPme10PProfileGroup.setStatus("current")

efmCuPme10PStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 2, 1, 10)
)
efmCuPme10PStatusGroup.setObjects(
      *(("EFM-CU-MIB", "efmCuPme10PElectricalLength"),
        ("EFM-CU-MIB", "efmCuPme10PFECCorrectedBlocks"),
        ("EFM-CU-MIB", "efmCuPme10PFECUncorrectedBlocks"))
)
if mibBuilder.loadTexts:
    efmCuPme10PStatusGroup.setStatus("current")


# Notification objects

efmCuLowBandwidth = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 1, 0, 1)
)
efmCuLowBandwidth.setObjects(
      *(("IF-MIB", "ifSpeed"),
        ("EFM-CU-MIB", "efmCuThreshLowBandwidth"))
)
if mibBuilder.loadTexts:
    efmCuLowBandwidth.setStatus(
        "current"
    )

efmCuPmeLineAtnCrossing = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 0, 1)
)
efmCuPmeLineAtnCrossing.setObjects(
      *(("EFM-CU-MIB", "efmCuPmeLineAtn"),
        ("EFM-CU-MIB", "efmCuPmeThreshLineAtn"))
)
if mibBuilder.loadTexts:
    efmCuPmeLineAtnCrossing.setStatus(
        "current"
    )

efmCuPmeSnrMgnCrossing = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 0, 2)
)
efmCuPmeSnrMgnCrossing.setObjects(
      *(("EFM-CU-MIB", "efmCuPmeSnrMgn"),
        ("EFM-CU-MIB", "efmCuPmeThreshMinSnrMgn"),
        ("EFM-CU-MIB", "efmCuPmeThreshMaxSnrMgnDelta"))
)
if mibBuilder.loadTexts:
    efmCuPmeSnrMgnCrossing.setStatus(
        "current"
    )

efmCuPmeDeviceFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 0, 3)
)
efmCuPmeDeviceFault.setObjects(
    ("EFM-CU-MIB", "efmCuPmeFltStatus")
)
if mibBuilder.loadTexts:
    efmCuPmeDeviceFault.setStatus(
        "current"
    )

efmCuPmeConfigInitFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 0, 4)
)
efmCuPmeConfigInitFailure.setObjects(
      *(("EFM-CU-MIB", "efmCuPmeFltStatus"),
        ("EFM-CU-MIB", "efmCuAdminProfile"),
        ("EFM-CU-MIB", "efmCuPmeAdminProfile"))
)
if mibBuilder.loadTexts:
    efmCuPmeConfigInitFailure.setStatus(
        "current"
    )

efmCuPmeProtocolInitFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 0, 5)
)
efmCuPmeProtocolInitFailure.setObjects(
      *(("EFM-CU-MIB", "efmCuPmeFltStatus"),
        ("EFM-CU-MIB", "efmCuPmeOperSubType"))
)
if mibBuilder.loadTexts:
    efmCuPmeProtocolInitFailure.setStatus(
        "current"
    )

efmCuPmeSnrMgnCrossingClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 0, 6)
)
efmCuPmeSnrMgnCrossingClear.setObjects(
      *(("EFM-CU-MIB", "efmCuPmeSnrMgn"),
        ("EFM-CU-MIB", "efmCuPmeThreshMinSnrMgn"),
        ("EFM-CU-MIB", "efmCuPmeThreshMaxSnrMgnDelta"))
)
if mibBuilder.loadTexts:
    efmCuPmeSnrMgnCrossingClear.setStatus(
        "current"
    )

efmCuPmeErrorThreshEfmTrafficDisable = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 0, 7)
)
efmCuPmeErrorThreshEfmTrafficDisable.setObjects(
    ("EFM-CU-MIB", "efmCuPmeErrorThreshMonInterval")
)
if mibBuilder.loadTexts:
    efmCuPmeErrorThreshEfmTrafficDisable.setStatus(
        "current"
    )

efmCuPmeErrorThreshEfmTrafficEnable = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 0, 8)
)
efmCuPmeErrorThreshEfmTrafficEnable.setObjects(
    ("EFM-CU-MIB", "efmCuPmeErrorThreshMonClrInterval")
)
if mibBuilder.loadTexts:
    efmCuPmeErrorThreshEfmTrafficEnable.setStatus(
        "current"
    )

efmCuPmeBondGroupTrafficDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 0, 9)
)
if mibBuilder.loadTexts:
    efmCuPmeBondGroupTrafficDisabled.setStatus(
        "current"
    )

efmCuPmeBondGroupTrafficEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 0, 10)
)
if mibBuilder.loadTexts:
    efmCuPmeBondGroupTrafficEnabled.setStatus(
        "current"
    )

efmCuPmeLinkTrafficDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 0, 11)
)
if mibBuilder.loadTexts:
    efmCuPmeLinkTrafficDisabled.setStatus(
        "current"
    )

efmCuPmeLinkTrafficEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 1, 2, 0, 12)
)
if mibBuilder.loadTexts:
    efmCuPmeLinkTrafficEnabled.setStatus(
        "current"
    )


# Notifications groups

efmCuNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 2, 1, 7)
)
efmCuNotificationGroup.setObjects(
      *(("EFM-CU-MIB", "efmCuLowBandwidth"),
        ("EFM-CU-MIB", "efmCuPmeLineAtnCrossing"),
        ("EFM-CU-MIB", "efmCuPmeSnrMgnCrossing"),
        ("EFM-CU-MIB", "efmCuPmeDeviceFault"),
        ("EFM-CU-MIB", "efmCuPmeConfigInitFailure"),
        ("EFM-CU-MIB", "efmCuPmeProtocolInitFailure"),
        ("EFM-CU-MIB", "efmCuPmeSnrMgnCrossingClear"))
)
if mibBuilder.loadTexts:
    efmCuNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

efmCuCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5504, 10, 1, 7, 2, 2, 1)
)
if mibBuilder.loadTexts:
    efmCuCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EFM-CU-MIB",
    **{"ProfileIndex": ProfileIndex,
       "ProfileIndexOrZero": ProfileIndexOrZero,
       "ProfileIndexList": ProfileIndexList,
       "TruthValueOrUnknown": TruthValueOrUnknown,
       "efmCuMIB": efmCuMIB,
       "efmCuObjects": efmCuObjects,
       "efmCuPort": efmCuPort,
       "efmCuPortNotifications": efmCuPortNotifications,
       "efmCuLowBandwidth": efmCuLowBandwidth,
       "efmCuPortConfTable": efmCuPortConfTable,
       "efmCuPortConfEntry": efmCuPortConfEntry,
       "efmCuPAFAdminState": efmCuPAFAdminState,
       "efmCuPAFDiscoveryCode": efmCuPAFDiscoveryCode,
       "efmCuAdminProfile": efmCuAdminProfile,
       "efmCuTargetDataRate": efmCuTargetDataRate,
       "efmCuTargetWorstCaseSnrMgn": efmCuTargetWorstCaseSnrMgn,
       "efmCuThreshLowBandwidth": efmCuThreshLowBandwidth,
       "efmCuLowBandwidthEnable": efmCuLowBandwidthEnable,
       "efmCuTargetCurrentConditionMode": efmCuTargetCurrentConditionMode,
       "efmCuTargetCurrentConditionSnrMgn": efmCuTargetCurrentConditionSnrMgn,
       "efmCuTargetWorstCaseMode": efmCuTargetWorstCaseMode,
       "efmCuPAFAutoDiscovery": efmCuPAFAutoDiscovery,
       "efmCuPmeErrorClearStats": efmCuPmeErrorClearStats,
       "efmCuPmeSnrClearStats": efmCuPmeSnrClearStats,
       "efmCuPortCapabilityTable": efmCuPortCapabilityTable,
       "efmCuPortCapabilityEntry": efmCuPortCapabilityEntry,
       "efmCuPAFSupported": efmCuPAFSupported,
       "efmCuPeerPAFSupported": efmCuPeerPAFSupported,
       "efmCuPAFCapacity": efmCuPAFCapacity,
       "efmCuPeerPAFCapacity": efmCuPeerPAFCapacity,
       "efmCuPortStatusTable": efmCuPortStatusTable,
       "efmCuPortStatusEntry": efmCuPortStatusEntry,
       "efmCuFltStatus": efmCuFltStatus,
       "efmCuPortSide": efmCuPortSide,
       "efmCuNumPMEs": efmCuNumPMEs,
       "efmCuPAFInErrors": efmCuPAFInErrors,
       "efmCuPAFInSmallFragments": efmCuPAFInSmallFragments,
       "efmCuPAFInLargeFragments": efmCuPAFInLargeFragments,
       "efmCuPAFInBadFragments": efmCuPAFInBadFragments,
       "efmCuPAFInLostFragments": efmCuPAFInLostFragments,
       "efmCuPAFInLostStarts": efmCuPAFInLostStarts,
       "efmCuPAFInLostEnds": efmCuPAFInLostEnds,
       "efmCuPAFInOverflows": efmCuPAFInOverflows,
       "efmCuPme": efmCuPme,
       "efmCuPmeNotifications": efmCuPmeNotifications,
       "efmCuPmeLineAtnCrossing": efmCuPmeLineAtnCrossing,
       "efmCuPmeSnrMgnCrossing": efmCuPmeSnrMgnCrossing,
       "efmCuPmeDeviceFault": efmCuPmeDeviceFault,
       "efmCuPmeConfigInitFailure": efmCuPmeConfigInitFailure,
       "efmCuPmeProtocolInitFailure": efmCuPmeProtocolInitFailure,
       "efmCuPmeSnrMgnCrossingClear": efmCuPmeSnrMgnCrossingClear,
       "efmCuPmeErrorThreshEfmTrafficDisable": efmCuPmeErrorThreshEfmTrafficDisable,
       "efmCuPmeErrorThreshEfmTrafficEnable": efmCuPmeErrorThreshEfmTrafficEnable,
       "efmCuPmeBondGroupTrafficDisabled": efmCuPmeBondGroupTrafficDisabled,
       "efmCuPmeBondGroupTrafficEnabled": efmCuPmeBondGroupTrafficEnabled,
       "efmCuPmeLinkTrafficDisabled": efmCuPmeLinkTrafficDisabled,
       "efmCuPmeLinkTrafficEnabled": efmCuPmeLinkTrafficEnabled,
       "efmCuPmeConfTable": efmCuPmeConfTable,
       "efmCuPmeConfEntry": efmCuPmeConfEntry,
       "efmCuPmeAdminSubType": efmCuPmeAdminSubType,
       "efmCuPmeAdminProfile": efmCuPmeAdminProfile,
       "efmCuPAFRemoteDiscoveryCode": efmCuPAFRemoteDiscoveryCode,
       "efmCuPmeThreshLineAtn": efmCuPmeThreshLineAtn,
       "efmCuPmeThreshMinSnrMgn": efmCuPmeThreshMinSnrMgn,
       "efmCuPmeLineAtnCrossingEnable": efmCuPmeLineAtnCrossingEnable,
       "efmCuPmeSnrMgnCrossingTrapEnable": efmCuPmeSnrMgnCrossingTrapEnable,
       "efmCuPmeDeviceFaultEnable": efmCuPmeDeviceFaultEnable,
       "efmCuPmeConfigInitFailEnable": efmCuPmeConfigInitFailEnable,
       "efmCuPmeProtocolInitFailEnable": efmCuPmeProtocolInitFailEnable,
       "efmCuPmeThreshMaxSnrMgnDelta": efmCuPmeThreshMaxSnrMgnDelta,
       "efmCuPmeMaintenanceMode": efmCuPmeMaintenanceMode,
       "efmCuPmeMaintenanceStartTime": efmCuPmeMaintenanceStartTime,
       "efmCuPmeMaintenanceEndTime": efmCuPmeMaintenanceEndTime,
       "efmCuPmeSnrMonitoringInterval": efmCuPmeSnrMonitoringInterval,
       "efmCuPmeErrorThreshMonEnable": efmCuPmeErrorThreshMonEnable,
       "efmCuPmeErrorThreshMonNotifyEnable": efmCuPmeErrorThreshMonNotifyEnable,
       "efmCuPmeErrorThreshMonInterval": efmCuPmeErrorThreshMonInterval,
       "efmCuPmeErrorThreshMonClrInterval": efmCuPmeErrorThreshMonClrInterval,
       "efmCuPmeLinkTrfcDisablTrapEnable": efmCuPmeLinkTrfcDisablTrapEnable,
       "efmCuPmeCapabilityTable": efmCuPmeCapabilityTable,
       "efmCuPmeCapabilityEntry": efmCuPmeCapabilityEntry,
       "efmCuPmeSubTypesSupported": efmCuPmeSubTypesSupported,
       "efmCuPmeStatusTable": efmCuPmeStatusTable,
       "efmCuPmeStatusEntry": efmCuPmeStatusEntry,
       "efmCuPmeOperStatus": efmCuPmeOperStatus,
       "efmCuPmeFltStatus": efmCuPmeFltStatus,
       "efmCuPmeOperSubType": efmCuPmeOperSubType,
       "efmCuPmeOperProfile": efmCuPmeOperProfile,
       "efmCuPmeSnrMgn": efmCuPmeSnrMgn,
       "efmCuPmePeerSnrMgn": efmCuPmePeerSnrMgn,
       "efmCuPmeLineAtn": efmCuPmeLineAtn,
       "efmCuPmePeerLineAtn": efmCuPmePeerLineAtn,
       "efmCuPmeTCCodingErrors": efmCuPmeTCCodingErrors,
       "efmCuPmeTCCrcErrors": efmCuPmeTCCrcErrors,
       "efmCuPmeSnrCrossingCnt": efmCuPmeSnrCrossingCnt,
       "efmCuPmeTCDownCnt": efmCuPmeTCDownCnt,
       "efmCuPmeErrorTCDownCnt": efmCuPmeErrorTCDownCnt,
       "efmCuPmeErrorRestartCnt": efmCuPmeErrorRestartCnt,
       "efmCuPmeSnrRestartCnt": efmCuPmeSnrRestartCnt,
       "efmCuPmeErrorConsecutiveSec": efmCuPmeErrorConsecutiveSec,
       "efmCuPmeErrorMaxConsecutiveSec": efmCuPmeErrorMaxConsecutiveSec,
       "efmCuPme2B": efmCuPme2B,
       "efmCuPme2BProfileTable": efmCuPme2BProfileTable,
       "efmCuPme2BProfileEntry": efmCuPme2BProfileEntry,
       "efmCuPme2BProfileIndex": efmCuPme2BProfileIndex,
       "efmCuPme2BProfileDescr": efmCuPme2BProfileDescr,
       "efmCuPme2BRegion": efmCuPme2BRegion,
       "efmCuPme2BDataRate": efmCuPme2BDataRate,
       "efmCuPme2BPower": efmCuPme2BPower,
       "efmCuPme2BConstellation": efmCuPme2BConstellation,
       "efmCuPme2BProfileRowStatus": efmCuPme2BProfileRowStatus,
       "efmCuPmeNtr": efmCuPmeNtr,
       "efmCuPme10P": efmCuPme10P,
       "efmCuPme10PProfileTable": efmCuPme10PProfileTable,
       "efmCuPme10PProfileEntry": efmCuPme10PProfileEntry,
       "efmCuPme10PProfileIndex": efmCuPme10PProfileIndex,
       "efmCuPme10PProfileDescr": efmCuPme10PProfileDescr,
       "efmCuPme10PBandplanPSDMskProfile": efmCuPme10PBandplanPSDMskProfile,
       "efmCuPme10PUPBOReferenceProfile": efmCuPme10PUPBOReferenceProfile,
       "efmCuPme10PBandNotchProfiles": efmCuPme10PBandNotchProfiles,
       "efmCuPme10PPayloadURateProfile": efmCuPme10PPayloadURateProfile,
       "efmCuPme10PPayloadDRateProfile": efmCuPme10PPayloadDRateProfile,
       "efmCuPme10PProfileRowStatus": efmCuPme10PProfileRowStatus,
       "efmCuPme10PStatusTable": efmCuPme10PStatusTable,
       "efmCuPme10PStatusEntry": efmCuPme10PStatusEntry,
       "efmCuPme10PElectricalLength": efmCuPme10PElectricalLength,
       "efmCuPme10PFECCorrectedBlocks": efmCuPme10PFECCorrectedBlocks,
       "efmCuPme10PFECUncorrectedBlocks": efmCuPme10PFECUncorrectedBlocks,
       "ifAvailableStackTable": ifAvailableStackTable,
       "ifAvailableStackEntry": ifAvailableStackEntry,
       "ifAvailableStackHigherLayer": ifAvailableStackHigherLayer,
       "ifAvailableStackLowerLayer": ifAvailableStackLowerLayer,
       "ifAvailableStackStatus": ifAvailableStackStatus,
       "efmCuRegeneratorStats": efmCuRegeneratorStats,
       "efmCuRegeneratorStatusTable": efmCuRegeneratorStatusTable,
       "efmCuRegeneratorStatusEntry": efmCuRegeneratorStatusEntry,
       "efmCuRegenIndex": efmCuRegenIndex,
       "efmCuRegenSide": efmCuRegenSide,
       "efmCuRegenSNR": efmCuRegenSNR,
       "efmCuRegenLineAttn": efmCuRegenLineAttn,
       "efmCuRegenCRC": efmCuRegenCRC,
       "efmCuRegenES": efmCuRegenES,
       "efmCuRegenSES": efmCuRegenSES,
       "efmCuRegenUAS": efmCuRegenUAS,
       "efmCuRegenLOSWS": efmCuRegenLOSWS,
       "efmCuRegenDCAlarm": efmCuRegenDCAlarm,
       "efmCuRegenClearCounts": efmCuRegenClearCounts,
       "efmCuConformance": efmCuConformance,
       "efmCuGroups": efmCuGroups,
       "efmCuBasicGroup": efmCuBasicGroup,
       "efmCuPAFGroup": efmCuPAFGroup,
       "ifStackCapabilityGroup": ifStackCapabilityGroup,
       "efmCuPAFErrorsGroup": efmCuPAFErrorsGroup,
       "efmCuPmeGroup": efmCuPmeGroup,
       "efmCuAlarmConfGroup": efmCuAlarmConfGroup,
       "efmCuNotificationGroup": efmCuNotificationGroup,
       "efmCuPme2BProfileGroup": efmCuPme2BProfileGroup,
       "efmCuPme10PProfileGroup": efmCuPme10PProfileGroup,
       "efmCuPme10PStatusGroup": efmCuPme10PStatusGroup,
       "efmCuCompliances": efmCuCompliances,
       "efmCuCompliance": efmCuCompliance}
)
