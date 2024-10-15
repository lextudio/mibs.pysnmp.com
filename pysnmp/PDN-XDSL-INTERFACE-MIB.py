# SNMP MIB module (PDN-XDSL-INTERFACE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PDN-XDSL-INTERFACE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:38:16 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(pdn_xdsl,) = mibBuilder.importSymbols(
    "PDN-HEADER-MIB",
    "pdn-xdsl")

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
    "iso")

(DisplayString,
 RowStatus,
 TAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XdslIfConfigMIBObjects_ObjectIdentity = ObjectIdentity
xdslIfConfigMIBObjects = _XdslIfConfigMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 2)
)
_XdslDevGenericIfConfig_ObjectIdentity = ObjectIdentity
xdslDevGenericIfConfig = _XdslDevGenericIfConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 2, 1)
)
_XdslDevGenericIfConfigTable_Object = MibTable
xdslDevGenericIfConfigTable = _XdslDevGenericIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 2, 1, 1)
)
if mibBuilder.loadTexts:
    xdslDevGenericIfConfigTable.setStatus("mandatory")
_XdslDevGenericIfConfigEntry_Object = MibTableRow
xdslDevGenericIfConfigEntry = _XdslDevGenericIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 2, 1, 1, 1)
)
xdslDevGenericIfConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xdslDevGenericIfConfigEntry.setStatus("mandatory")


class _XdslDevGenericIfConfigPortSpeedBehaviour_Type(Integer32):
    """Custom type xdslDevGenericIfConfigPortSpeedBehaviour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("adaptive", 2),
          ("fixed", 1))
    )


_XdslDevGenericIfConfigPortSpeedBehaviour_Type.__name__ = "Integer32"
_XdslDevGenericIfConfigPortSpeedBehaviour_Object = MibTableColumn
xdslDevGenericIfConfigPortSpeedBehaviour = _XdslDevGenericIfConfigPortSpeedBehaviour_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 2, 1, 1, 1, 1),
    _XdslDevGenericIfConfigPortSpeedBehaviour_Type()
)
xdslDevGenericIfConfigPortSpeedBehaviour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdslDevGenericIfConfigPortSpeedBehaviour.setStatus("mandatory")
_XdslDevGenericIfConfigMarginThreshold_Type = Integer32
_XdslDevGenericIfConfigMarginThreshold_Object = MibTableColumn
xdslDevGenericIfConfigMarginThreshold = _XdslDevGenericIfConfigMarginThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 2, 1, 1, 1, 2),
    _XdslDevGenericIfConfigMarginThreshold_Type()
)
xdslDevGenericIfConfigMarginThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdslDevGenericIfConfigMarginThreshold.setStatus("mandatory")


class _XdslDevGenericIfConfigPortID_Type(DisplayString):
    """Custom type xdslDevGenericIfConfigPortID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_XdslDevGenericIfConfigPortID_Type.__name__ = "DisplayString"
_XdslDevGenericIfConfigPortID_Object = MibTableColumn
xdslDevGenericIfConfigPortID = _XdslDevGenericIfConfigPortID_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 2, 1, 1, 1, 3),
    _XdslDevGenericIfConfigPortID_Type()
)
xdslDevGenericIfConfigPortID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdslDevGenericIfConfigPortID.setStatus("mandatory")
_XdslDevGenericIfConfigLinkUpDownTransitionThreshold_Type = Integer32
_XdslDevGenericIfConfigLinkUpDownTransitionThreshold_Object = MibTableColumn
xdslDevGenericIfConfigLinkUpDownTransitionThreshold = _XdslDevGenericIfConfigLinkUpDownTransitionThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 2, 1, 1, 1, 4),
    _XdslDevGenericIfConfigLinkUpDownTransitionThreshold_Type()
)
xdslDevGenericIfConfigLinkUpDownTransitionThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdslDevGenericIfConfigLinkUpDownTransitionThreshold.setStatus("mandatory")


class _XdslDevGenericIfConfigLineEncodeType_Type(Integer32):
    """Custom type xdslDevGenericIfConfigLineEncodeType based on Integer32"""
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
        *(("cap", 2),
          ("dmt", 6),
          ("g-lite", 5),
          ("mvl", 4),
          ("other", 1),
          ("twoB1q", 3))
    )


_XdslDevGenericIfConfigLineEncodeType_Type.__name__ = "Integer32"
_XdslDevGenericIfConfigLineEncodeType_Object = MibTableColumn
xdslDevGenericIfConfigLineEncodeType = _XdslDevGenericIfConfigLineEncodeType_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 2, 1, 1, 1, 5),
    _XdslDevGenericIfConfigLineEncodeType_Type()
)
xdslDevGenericIfConfigLineEncodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdslDevGenericIfConfigLineEncodeType.setStatus("mandatory")


class _XdslDevGenericIfConfigLineRateMode_Type(Integer32):
    """Custom type xdslDevGenericIfConfigLineRateMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nx128", 2),
          ("standard", 1))
    )


_XdslDevGenericIfConfigLineRateMode_Type.__name__ = "Integer32"
_XdslDevGenericIfConfigLineRateMode_Object = MibTableColumn
xdslDevGenericIfConfigLineRateMode = _XdslDevGenericIfConfigLineRateMode_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 2, 1, 1, 1, 6),
    _XdslDevGenericIfConfigLineRateMode_Type()
)
xdslDevGenericIfConfigLineRateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdslDevGenericIfConfigLineRateMode.setStatus("mandatory")
_XdslDevRADSLSpecificIfConfig_ObjectIdentity = ObjectIdentity
xdslDevRADSLSpecificIfConfig = _XdslDevRADSLSpecificIfConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 2, 2)
)
_XdslDevRADSLSpecificIfConfigTable_Object = MibTable
xdslDevRADSLSpecificIfConfigTable = _XdslDevRADSLSpecificIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 2, 2, 1)
)
if mibBuilder.loadTexts:
    xdslDevRADSLSpecificIfConfigTable.setStatus("mandatory")
_XdslDevRADSLSpecificIfConfigEntry_Object = MibTableRow
xdslDevRADSLSpecificIfConfigEntry = _XdslDevRADSLSpecificIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 2, 2, 1, 1)
)
xdslDevRADSLSpecificIfConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xdslDevRADSLSpecificIfConfigEntry.setStatus("mandatory")
_XdslDevRADSLSpecificIfConfigUpFixedPortSpeed_Type = Integer32
_XdslDevRADSLSpecificIfConfigUpFixedPortSpeed_Object = MibTableColumn
xdslDevRADSLSpecificIfConfigUpFixedPortSpeed = _XdslDevRADSLSpecificIfConfigUpFixedPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 2, 2, 1, 1, 1),
    _XdslDevRADSLSpecificIfConfigUpFixedPortSpeed_Type()
)
xdslDevRADSLSpecificIfConfigUpFixedPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdslDevRADSLSpecificIfConfigUpFixedPortSpeed.setStatus("mandatory")
_XdslDevRADSLSpecificIfConfigDownFixedPortSpeed_Type = Integer32
_XdslDevRADSLSpecificIfConfigDownFixedPortSpeed_Object = MibTableColumn
xdslDevRADSLSpecificIfConfigDownFixedPortSpeed = _XdslDevRADSLSpecificIfConfigDownFixedPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 2, 2, 1, 1, 2),
    _XdslDevRADSLSpecificIfConfigDownFixedPortSpeed_Type()
)
xdslDevRADSLSpecificIfConfigDownFixedPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdslDevRADSLSpecificIfConfigDownFixedPortSpeed.setStatus("mandatory")
_XdslDevRADSLSpecificIfConfigUpAdaptiveUpperBoundPortSpeed_Type = Integer32
_XdslDevRADSLSpecificIfConfigUpAdaptiveUpperBoundPortSpeed_Object = MibTableColumn
xdslDevRADSLSpecificIfConfigUpAdaptiveUpperBoundPortSpeed = _XdslDevRADSLSpecificIfConfigUpAdaptiveUpperBoundPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 2, 2, 1, 1, 3),
    _XdslDevRADSLSpecificIfConfigUpAdaptiveUpperBoundPortSpeed_Type()
)
xdslDevRADSLSpecificIfConfigUpAdaptiveUpperBoundPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdslDevRADSLSpecificIfConfigUpAdaptiveUpperBoundPortSpeed.setStatus("mandatory")
_XdslDevRADSLSpecificIfConfigUpAdaptiveLowerBoundPortSpeed_Type = Integer32
_XdslDevRADSLSpecificIfConfigUpAdaptiveLowerBoundPortSpeed_Object = MibTableColumn
xdslDevRADSLSpecificIfConfigUpAdaptiveLowerBoundPortSpeed = _XdslDevRADSLSpecificIfConfigUpAdaptiveLowerBoundPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 2, 2, 1, 1, 4),
    _XdslDevRADSLSpecificIfConfigUpAdaptiveLowerBoundPortSpeed_Type()
)
xdslDevRADSLSpecificIfConfigUpAdaptiveLowerBoundPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdslDevRADSLSpecificIfConfigUpAdaptiveLowerBoundPortSpeed.setStatus("mandatory")
_XdslDevRADSLSpecificIfConfigDownAdaptiveUpperBoundPortSpeed_Type = Integer32
_XdslDevRADSLSpecificIfConfigDownAdaptiveUpperBoundPortSpeed_Object = MibTableColumn
xdslDevRADSLSpecificIfConfigDownAdaptiveUpperBoundPortSpeed = _XdslDevRADSLSpecificIfConfigDownAdaptiveUpperBoundPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 2, 2, 1, 1, 5),
    _XdslDevRADSLSpecificIfConfigDownAdaptiveUpperBoundPortSpeed_Type()
)
xdslDevRADSLSpecificIfConfigDownAdaptiveUpperBoundPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdslDevRADSLSpecificIfConfigDownAdaptiveUpperBoundPortSpeed.setStatus("mandatory")
_XdslDevRADSLSpecificIfConfigDownAdaptiveLowerBoundPortSpeed_Type = Integer32
_XdslDevRADSLSpecificIfConfigDownAdaptiveLowerBoundPortSpeed_Object = MibTableColumn
xdslDevRADSLSpecificIfConfigDownAdaptiveLowerBoundPortSpeed = _XdslDevRADSLSpecificIfConfigDownAdaptiveLowerBoundPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 2, 2, 1, 1, 6),
    _XdslDevRADSLSpecificIfConfigDownAdaptiveLowerBoundPortSpeed_Type()
)
xdslDevRADSLSpecificIfConfigDownAdaptiveLowerBoundPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdslDevRADSLSpecificIfConfigDownAdaptiveLowerBoundPortSpeed.setStatus("mandatory")


class _XdslDevRADSLSpecificIfConfigReedSolomonDownFwdErrCorrection_Type(Integer32):
    """Custom type xdslDevRADSLSpecificIfConfigReedSolomonDownFwdErrCorrection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("minimizeDelay", 2),
          ("minimizeError", 1),
          ("reedSolomonNotSupported", 3))
    )


_XdslDevRADSLSpecificIfConfigReedSolomonDownFwdErrCorrection_Type.__name__ = "Integer32"
_XdslDevRADSLSpecificIfConfigReedSolomonDownFwdErrCorrection_Object = MibTableColumn
xdslDevRADSLSpecificIfConfigReedSolomonDownFwdErrCorrection = _XdslDevRADSLSpecificIfConfigReedSolomonDownFwdErrCorrection_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 2, 2, 1, 1, 7),
    _XdslDevRADSLSpecificIfConfigReedSolomonDownFwdErrCorrection_Type()
)
xdslDevRADSLSpecificIfConfigReedSolomonDownFwdErrCorrection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdslDevRADSLSpecificIfConfigReedSolomonDownFwdErrCorrection.setStatus("mandatory")


class _XdslDevRADSLSpecificIfConfigStartUpMargin_Type(Integer32):
    """Custom type xdslDevRADSLSpecificIfConfigStartUpMargin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-3, 9),
    )


_XdslDevRADSLSpecificIfConfigStartUpMargin_Type.__name__ = "Integer32"
_XdslDevRADSLSpecificIfConfigStartUpMargin_Object = MibTableColumn
xdslDevRADSLSpecificIfConfigStartUpMargin = _XdslDevRADSLSpecificIfConfigStartUpMargin_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 2, 2, 1, 1, 8),
    _XdslDevRADSLSpecificIfConfigStartUpMargin_Type()
)
xdslDevRADSLSpecificIfConfigStartUpMargin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdslDevRADSLSpecificIfConfigStartUpMargin.setStatus("mandatory")
_XdslDevRADSLSpecificIfConfigTxPowerAttenuation_Type = Integer32
_XdslDevRADSLSpecificIfConfigTxPowerAttenuation_Object = MibTableColumn
xdslDevRADSLSpecificIfConfigTxPowerAttenuation = _XdslDevRADSLSpecificIfConfigTxPowerAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 2, 2, 1, 1, 9),
    _XdslDevRADSLSpecificIfConfigTxPowerAttenuation_Type()
)
xdslDevRADSLSpecificIfConfigTxPowerAttenuation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdslDevRADSLSpecificIfConfigTxPowerAttenuation.setStatus("mandatory")
_XdslDevRADSLSpecificIfConfigSnTxPowerAttenuation_Type = Integer32
_XdslDevRADSLSpecificIfConfigSnTxPowerAttenuation_Object = MibTableColumn
xdslDevRADSLSpecificIfConfigSnTxPowerAttenuation = _XdslDevRADSLSpecificIfConfigSnTxPowerAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 2, 2, 1, 1, 10),
    _XdslDevRADSLSpecificIfConfigSnTxPowerAttenuation_Type()
)
xdslDevRADSLSpecificIfConfigSnTxPowerAttenuation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdslDevRADSLSpecificIfConfigSnTxPowerAttenuation.setStatus("mandatory")
_XdslDevMVLSpecificIfConfig_ObjectIdentity = ObjectIdentity
xdslDevMVLSpecificIfConfig = _XdslDevMVLSpecificIfConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 2, 3)
)
_XdslDevMVLSpecificIfConfigTable_Object = MibTable
xdslDevMVLSpecificIfConfigTable = _XdslDevMVLSpecificIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 2, 3, 1)
)
if mibBuilder.loadTexts:
    xdslDevMVLSpecificIfConfigTable.setStatus("mandatory")
_XdslDevMVLSpecificIfConfigEntry_Object = MibTableRow
xdslDevMVLSpecificIfConfigEntry = _XdslDevMVLSpecificIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 2, 3, 1, 1)
)
xdslDevMVLSpecificIfConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xdslDevMVLSpecificIfConfigEntry.setStatus("mandatory")
_XdslDevMVLSpecificIfConfigMaxPortSpeed_Type = Integer32
_XdslDevMVLSpecificIfConfigMaxPortSpeed_Object = MibTableColumn
xdslDevMVLSpecificIfConfigMaxPortSpeed = _XdslDevMVLSpecificIfConfigMaxPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 2, 3, 1, 1, 1),
    _XdslDevMVLSpecificIfConfigMaxPortSpeed_Type()
)
xdslDevMVLSpecificIfConfigMaxPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdslDevMVLSpecificIfConfigMaxPortSpeed.setStatus("mandatory")
_XdslDevMVLSpecificIfConfigOnHookTxPowerAttenuation_Type = Integer32
_XdslDevMVLSpecificIfConfigOnHookTxPowerAttenuation_Object = MibTableColumn
xdslDevMVLSpecificIfConfigOnHookTxPowerAttenuation = _XdslDevMVLSpecificIfConfigOnHookTxPowerAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 2, 3, 1, 1, 2),
    _XdslDevMVLSpecificIfConfigOnHookTxPowerAttenuation_Type()
)
xdslDevMVLSpecificIfConfigOnHookTxPowerAttenuation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdslDevMVLSpecificIfConfigOnHookTxPowerAttenuation.setStatus("mandatory")
_XdslDevMVLSpecificIfConfigOffHookTxPowerAttenuation_Type = Integer32
_XdslDevMVLSpecificIfConfigOffHookTxPowerAttenuation_Object = MibTableColumn
xdslDevMVLSpecificIfConfigOffHookTxPowerAttenuation = _XdslDevMVLSpecificIfConfigOffHookTxPowerAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 2, 3, 1, 1, 3),
    _XdslDevMVLSpecificIfConfigOffHookTxPowerAttenuation_Type()
)
xdslDevMVLSpecificIfConfigOffHookTxPowerAttenuation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdslDevMVLSpecificIfConfigOffHookTxPowerAttenuation.setStatus("mandatory")
_XdslDevSDSLSpecificIfConfig_ObjectIdentity = ObjectIdentity
xdslDevSDSLSpecificIfConfig = _XdslDevSDSLSpecificIfConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 2, 4)
)
_XdslDevSDSLSpecificIfConfigTable_Object = MibTable
xdslDevSDSLSpecificIfConfigTable = _XdslDevSDSLSpecificIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 2, 4, 1)
)
if mibBuilder.loadTexts:
    xdslDevSDSLSpecificIfConfigTable.setStatus("mandatory")
_XdslDevSDSLSpecificIfConfigEntry_Object = MibTableRow
xdslDevSDSLSpecificIfConfigEntry = _XdslDevSDSLSpecificIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 2, 4, 1, 1)
)
xdslDevSDSLSpecificIfConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xdslDevSDSLSpecificIfConfigEntry.setStatus("mandatory")
_XdslDevSDSLSpecificIfConfigFixedPortSpeed_Type = Integer32
_XdslDevSDSLSpecificIfConfigFixedPortSpeed_Object = MibTableColumn
xdslDevSDSLSpecificIfConfigFixedPortSpeed = _XdslDevSDSLSpecificIfConfigFixedPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 2, 4, 1, 1, 1),
    _XdslDevSDSLSpecificIfConfigFixedPortSpeed_Type()
)
xdslDevSDSLSpecificIfConfigFixedPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdslDevSDSLSpecificIfConfigFixedPortSpeed.setStatus("mandatory")
_XdslDevSDSLSpecificIfConfigMaxPortSpeed_Type = Integer32
_XdslDevSDSLSpecificIfConfigMaxPortSpeed_Object = MibTableColumn
xdslDevSDSLSpecificIfConfigMaxPortSpeed = _XdslDevSDSLSpecificIfConfigMaxPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 2, 4, 1, 1, 2),
    _XdslDevSDSLSpecificIfConfigMaxPortSpeed_Type()
)
xdslDevSDSLSpecificIfConfigMaxPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdslDevSDSLSpecificIfConfigMaxPortSpeed.setStatus("mandatory")


class _XdslDevSDSLSpecificIfConfigFixedPortSpeedNx128Mode_Type(Integer32):
    """Custom type xdslDevSDSLSpecificIfConfigFixedPortSpeedNx128Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XdslDevSDSLSpecificIfConfigFixedPortSpeedNx128Mode_Type.__name__ = "Integer32"
_XdslDevSDSLSpecificIfConfigFixedPortSpeedNx128Mode_Object = MibTableColumn
xdslDevSDSLSpecificIfConfigFixedPortSpeedNx128Mode = _XdslDevSDSLSpecificIfConfigFixedPortSpeedNx128Mode_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 2, 4, 1, 1, 3),
    _XdslDevSDSLSpecificIfConfigFixedPortSpeedNx128Mode_Type()
)
xdslDevSDSLSpecificIfConfigFixedPortSpeedNx128Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdslDevSDSLSpecificIfConfigFixedPortSpeedNx128Mode.setStatus("mandatory")


class _XdslDevSDSLSpecificIfConfigMaxPortSpeedNx128Mode_Type(Integer32):
    """Custom type xdslDevSDSLSpecificIfConfigMaxPortSpeedNx128Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XdslDevSDSLSpecificIfConfigMaxPortSpeedNx128Mode_Type.__name__ = "Integer32"
_XdslDevSDSLSpecificIfConfigMaxPortSpeedNx128Mode_Object = MibTableColumn
xdslDevSDSLSpecificIfConfigMaxPortSpeedNx128Mode = _XdslDevSDSLSpecificIfConfigMaxPortSpeedNx128Mode_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 2, 4, 1, 1, 4),
    _XdslDevSDSLSpecificIfConfigMaxPortSpeedNx128Mode_Type()
)
xdslDevSDSLSpecificIfConfigMaxPortSpeedNx128Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdslDevSDSLSpecificIfConfigMaxPortSpeedNx128Mode.setStatus("mandatory")
_XdslDevIDSLSpecificIfConfig_ObjectIdentity = ObjectIdentity
xdslDevIDSLSpecificIfConfig = _XdslDevIDSLSpecificIfConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 2, 5)
)
_XdslDevIDSLSpecificIfConfigTable_Object = MibTable
xdslDevIDSLSpecificIfConfigTable = _XdslDevIDSLSpecificIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 2, 5, 1)
)
if mibBuilder.loadTexts:
    xdslDevIDSLSpecificIfConfigTable.setStatus("mandatory")
_XdslDevIDSLSpecificIfConfigEntry_Object = MibTableRow
xdslDevIDSLSpecificIfConfigEntry = _XdslDevIDSLSpecificIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 2, 5, 1, 1)
)
xdslDevIDSLSpecificIfConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xdslDevIDSLSpecificIfConfigEntry.setStatus("mandatory")
_XdslDevIDSLSpecificIfConfigPortSpeed_Type = Integer32
_XdslDevIDSLSpecificIfConfigPortSpeed_Object = MibTableColumn
xdslDevIDSLSpecificIfConfigPortSpeed = _XdslDevIDSLSpecificIfConfigPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 2, 5, 1, 1, 1),
    _XdslDevIDSLSpecificIfConfigPortSpeed_Type()
)
xdslDevIDSLSpecificIfConfigPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdslDevIDSLSpecificIfConfigPortSpeed.setStatus("mandatory")


class _XdslDevIDSLSpecificIfConfigTimingPortTransceiverMode_Type(Integer32):
    """Custom type xdslDevIDSLSpecificIfConfigTimingPortTransceiverMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("localTiming", 2),
          ("networkTiming", 1))
    )


_XdslDevIDSLSpecificIfConfigTimingPortTransceiverMode_Type.__name__ = "Integer32"
_XdslDevIDSLSpecificIfConfigTimingPortTransceiverMode_Object = MibTableColumn
xdslDevIDSLSpecificIfConfigTimingPortTransceiverMode = _XdslDevIDSLSpecificIfConfigTimingPortTransceiverMode_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 2, 5, 1, 1, 2),
    _XdslDevIDSLSpecificIfConfigTimingPortTransceiverMode_Type()
)
xdslDevIDSLSpecificIfConfigTimingPortTransceiverMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdslDevIDSLSpecificIfConfigTimingPortTransceiverMode.setStatus("mandatory")
_XdslIfConfigMIBTraps_ObjectIdentity = ObjectIdentity
xdslIfConfigMIBTraps = _XdslIfConfigMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 9, 4)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PDN-XDSL-INTERFACE-MIB",
    **{"xdslIfConfigMIBObjects": xdslIfConfigMIBObjects,
       "xdslDevGenericIfConfig": xdslDevGenericIfConfig,
       "xdslDevGenericIfConfigTable": xdslDevGenericIfConfigTable,
       "xdslDevGenericIfConfigEntry": xdslDevGenericIfConfigEntry,
       "xdslDevGenericIfConfigPortSpeedBehaviour": xdslDevGenericIfConfigPortSpeedBehaviour,
       "xdslDevGenericIfConfigMarginThreshold": xdslDevGenericIfConfigMarginThreshold,
       "xdslDevGenericIfConfigPortID": xdslDevGenericIfConfigPortID,
       "xdslDevGenericIfConfigLinkUpDownTransitionThreshold": xdslDevGenericIfConfigLinkUpDownTransitionThreshold,
       "xdslDevGenericIfConfigLineEncodeType": xdslDevGenericIfConfigLineEncodeType,
       "xdslDevGenericIfConfigLineRateMode": xdslDevGenericIfConfigLineRateMode,
       "xdslDevRADSLSpecificIfConfig": xdslDevRADSLSpecificIfConfig,
       "xdslDevRADSLSpecificIfConfigTable": xdslDevRADSLSpecificIfConfigTable,
       "xdslDevRADSLSpecificIfConfigEntry": xdslDevRADSLSpecificIfConfigEntry,
       "xdslDevRADSLSpecificIfConfigUpFixedPortSpeed": xdslDevRADSLSpecificIfConfigUpFixedPortSpeed,
       "xdslDevRADSLSpecificIfConfigDownFixedPortSpeed": xdslDevRADSLSpecificIfConfigDownFixedPortSpeed,
       "xdslDevRADSLSpecificIfConfigUpAdaptiveUpperBoundPortSpeed": xdslDevRADSLSpecificIfConfigUpAdaptiveUpperBoundPortSpeed,
       "xdslDevRADSLSpecificIfConfigUpAdaptiveLowerBoundPortSpeed": xdslDevRADSLSpecificIfConfigUpAdaptiveLowerBoundPortSpeed,
       "xdslDevRADSLSpecificIfConfigDownAdaptiveUpperBoundPortSpeed": xdslDevRADSLSpecificIfConfigDownAdaptiveUpperBoundPortSpeed,
       "xdslDevRADSLSpecificIfConfigDownAdaptiveLowerBoundPortSpeed": xdslDevRADSLSpecificIfConfigDownAdaptiveLowerBoundPortSpeed,
       "xdslDevRADSLSpecificIfConfigReedSolomonDownFwdErrCorrection": xdslDevRADSLSpecificIfConfigReedSolomonDownFwdErrCorrection,
       "xdslDevRADSLSpecificIfConfigStartUpMargin": xdslDevRADSLSpecificIfConfigStartUpMargin,
       "xdslDevRADSLSpecificIfConfigTxPowerAttenuation": xdslDevRADSLSpecificIfConfigTxPowerAttenuation,
       "xdslDevRADSLSpecificIfConfigSnTxPowerAttenuation": xdslDevRADSLSpecificIfConfigSnTxPowerAttenuation,
       "xdslDevMVLSpecificIfConfig": xdslDevMVLSpecificIfConfig,
       "xdslDevMVLSpecificIfConfigTable": xdslDevMVLSpecificIfConfigTable,
       "xdslDevMVLSpecificIfConfigEntry": xdslDevMVLSpecificIfConfigEntry,
       "xdslDevMVLSpecificIfConfigMaxPortSpeed": xdslDevMVLSpecificIfConfigMaxPortSpeed,
       "xdslDevMVLSpecificIfConfigOnHookTxPowerAttenuation": xdslDevMVLSpecificIfConfigOnHookTxPowerAttenuation,
       "xdslDevMVLSpecificIfConfigOffHookTxPowerAttenuation": xdslDevMVLSpecificIfConfigOffHookTxPowerAttenuation,
       "xdslDevSDSLSpecificIfConfig": xdslDevSDSLSpecificIfConfig,
       "xdslDevSDSLSpecificIfConfigTable": xdslDevSDSLSpecificIfConfigTable,
       "xdslDevSDSLSpecificIfConfigEntry": xdslDevSDSLSpecificIfConfigEntry,
       "xdslDevSDSLSpecificIfConfigFixedPortSpeed": xdslDevSDSLSpecificIfConfigFixedPortSpeed,
       "xdslDevSDSLSpecificIfConfigMaxPortSpeed": xdslDevSDSLSpecificIfConfigMaxPortSpeed,
       "xdslDevSDSLSpecificIfConfigFixedPortSpeedNx128Mode": xdslDevSDSLSpecificIfConfigFixedPortSpeedNx128Mode,
       "xdslDevSDSLSpecificIfConfigMaxPortSpeedNx128Mode": xdslDevSDSLSpecificIfConfigMaxPortSpeedNx128Mode,
       "xdslDevIDSLSpecificIfConfig": xdslDevIDSLSpecificIfConfig,
       "xdslDevIDSLSpecificIfConfigTable": xdslDevIDSLSpecificIfConfigTable,
       "xdslDevIDSLSpecificIfConfigEntry": xdslDevIDSLSpecificIfConfigEntry,
       "xdslDevIDSLSpecificIfConfigPortSpeed": xdslDevIDSLSpecificIfConfigPortSpeed,
       "xdslDevIDSLSpecificIfConfigTimingPortTransceiverMode": xdslDevIDSLSpecificIfConfigTimingPortTransceiverMode,
       "xdslIfConfigMIBTraps": xdslIfConfigMIBTraps}
)
