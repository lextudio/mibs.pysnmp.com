# SNMP MIB module (ExtendAirG2) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ExtendAirG2
# Produced by pysmi-1.5.4 at Mon Oct 14 21:43:17 2024
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

(systemConfig,) = mibBuilder.importSymbols(
    "ExaltComProducts",
    "systemConfig")

(AcmBaseModulationT,
 AcmPolicyT,
 AcmTargetModulationT,
 BandwidthT,
 BuzTimeoutT,
 DiplexerConfigG2T,
 ExaltEnableT,
 ModulationT,
 RadioSourceT,
 RadioTxPwr15gT) = mibBuilder.importSymbols(
    "ExaltComm",
    "AcmBaseModulationT",
    "AcmPolicyT",
    "AcmTargetModulationT",
    "BandwidthT",
    "BuzTimeoutT",
    "DiplexerConfigG2T",
    "ExaltEnableT",
    "ModulationT",
    "RadioSourceT",
    "RadioTxPwr15gT")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

extendAirG2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 1, 57)
)
extendAirG2.setRevisions(
        ("2013-04-26 10:21",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ExtendAirG2TxPower_Type = RadioTxPwr15gT
_ExtendAirG2TxPower_Object = MibScalar
extendAirG2TxPower = _ExtendAirG2TxPower_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 1, 57, 1),
    _ExtendAirG2TxPower_Type()
)
extendAirG2TxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extendAirG2TxPower.setStatus("current")
if mibBuilder.loadTexts:
    extendAirG2TxPower.setUnits("Tenths of dBm.")
_ExtendAirG2Bandwidth_Type = BandwidthT
_ExtendAirG2Bandwidth_Object = MibScalar
extendAirG2Bandwidth = _ExtendAirG2Bandwidth_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 1, 57, 2),
    _ExtendAirG2Bandwidth_Type()
)
extendAirG2Bandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extendAirG2Bandwidth.setStatus("current")
if mibBuilder.loadTexts:
    extendAirG2Bandwidth.setUnits("kHz")
_ExtendAirG2Modulation_Type = ModulationT
_ExtendAirG2Modulation_Object = MibScalar
extendAirG2Modulation = _ExtendAirG2Modulation_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 1, 57, 3),
    _ExtendAirG2Modulation_Type()
)
extendAirG2Modulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extendAirG2Modulation.setStatus("current")


class _ExtendAirG2TXfrequency_Type(DisplayString):
    """Custom type extendAirG2TXfrequency based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 9),
    )


_ExtendAirG2TXfrequency_Type.__name__ = "DisplayString"
_ExtendAirG2TXfrequency_Object = MibScalar
extendAirG2TXfrequency = _ExtendAirG2TXfrequency_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 1, 57, 4),
    _ExtendAirG2TXfrequency_Type()
)
extendAirG2TXfrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extendAirG2TXfrequency.setStatus("current")
if mibBuilder.loadTexts:
    extendAirG2TXfrequency.setUnits("MHz")


class _ExtendAirG2RXfrequency_Type(DisplayString):
    """Custom type extendAirG2RXfrequency based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 9),
    )


_ExtendAirG2RXfrequency_Type.__name__ = "DisplayString"
_ExtendAirG2RXfrequency_Object = MibScalar
extendAirG2RXfrequency = _ExtendAirG2RXfrequency_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 1, 57, 5),
    _ExtendAirG2RXfrequency_Type()
)
extendAirG2RXfrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extendAirG2RXfrequency.setStatus("current")
if mibBuilder.loadTexts:
    extendAirG2RXfrequency.setUnits("MHz")
_ExtendAirG2DiplexerConfiguration_Type = DiplexerConfigG2T
_ExtendAirG2DiplexerConfiguration_Object = MibScalar
extendAirG2DiplexerConfiguration = _ExtendAirG2DiplexerConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 1, 57, 6),
    _ExtendAirG2DiplexerConfiguration_Type()
)
extendAirG2DiplexerConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extendAirG2DiplexerConfiguration.setStatus("current")


class _ExtendAirG2InsertionLoss_Type(Integer32):
    """Custom type extendAirG2InsertionLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_ExtendAirG2InsertionLoss_Type.__name__ = "Integer32"
_ExtendAirG2InsertionLoss_Object = MibScalar
extendAirG2InsertionLoss = _ExtendAirG2InsertionLoss_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 1, 57, 7),
    _ExtendAirG2InsertionLoss_Type()
)
extendAirG2InsertionLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extendAirG2InsertionLoss.setStatus("current")
if mibBuilder.loadTexts:
    extendAirG2InsertionLoss.setUnits("Hundredth dBm")
_ExtendAirG2BuzTimeout_Type = BuzTimeoutT
_ExtendAirG2BuzTimeout_Object = MibScalar
extendAirG2BuzTimeout = _ExtendAirG2BuzTimeout_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 1, 57, 8),
    _ExtendAirG2BuzTimeout_Type()
)
extendAirG2BuzTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extendAirG2BuzTimeout.setStatus("current")
_ExtendAirG2AcmMode_Type = ExaltEnableT
_ExtendAirG2AcmMode_Object = MibScalar
extendAirG2AcmMode = _ExtendAirG2AcmMode_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 1, 57, 9),
    _ExtendAirG2AcmMode_Type()
)
extendAirG2AcmMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extendAirG2AcmMode.setStatus("current")
_ExtendAirG2AcmPolicy_Type = AcmPolicyT
_ExtendAirG2AcmPolicy_Object = MibScalar
extendAirG2AcmPolicy = _ExtendAirG2AcmPolicy_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 1, 57, 10),
    _ExtendAirG2AcmPolicy_Type()
)
extendAirG2AcmPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extendAirG2AcmPolicy.setStatus("current")
_ExtendAirG2AcmBaseModulation_Type = AcmBaseModulationT
_ExtendAirG2AcmBaseModulation_Object = MibScalar
extendAirG2AcmBaseModulation = _ExtendAirG2AcmBaseModulation_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 1, 57, 11),
    _ExtendAirG2AcmBaseModulation_Type()
)
extendAirG2AcmBaseModulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extendAirG2AcmBaseModulation.setStatus("current")
_ExtendAirG2AcmTargetModulation_Type = AcmTargetModulationT
_ExtendAirG2AcmTargetModulation_Object = MibScalar
extendAirG2AcmTargetModulation = _ExtendAirG2AcmTargetModulation_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 1, 57, 12),
    _ExtendAirG2AcmTargetModulation_Type()
)
extendAirG2AcmTargetModulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extendAirG2AcmTargetModulation.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ExtendAirG2",
    **{"extendAirG2": extendAirG2,
       "extendAirG2TxPower": extendAirG2TxPower,
       "extendAirG2Bandwidth": extendAirG2Bandwidth,
       "extendAirG2Modulation": extendAirG2Modulation,
       "extendAirG2TXfrequency": extendAirG2TXfrequency,
       "extendAirG2RXfrequency": extendAirG2RXfrequency,
       "extendAirG2DiplexerConfiguration": extendAirG2DiplexerConfiguration,
       "extendAirG2InsertionLoss": extendAirG2InsertionLoss,
       "extendAirG2BuzTimeout": extendAirG2BuzTimeout,
       "extendAirG2AcmMode": extendAirG2AcmMode,
       "extendAirG2AcmPolicy": extendAirG2AcmPolicy,
       "extendAirG2AcmBaseModulation": extendAirG2AcmBaseModulation,
       "extendAirG2AcmTargetModulation": extendAirG2AcmTargetModulation}
)
