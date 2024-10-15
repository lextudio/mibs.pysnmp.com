# SNMP MIB module (MRV-IN-REACH-RADIUS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MRV-IN-REACH-RADIUS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:23:46 2024
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

(mrvInReachProductDivision,) = mibBuilder.importSymbols(
    "MRV-IN-REACH-PRODUCT-DIVISION-MIB",
    "mrvInReachProductDivision")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XRadius_ObjectIdentity = ObjectIdentity
xRadius = _XRadius_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 35)
)
_XRadiusPort_ObjectIdentity = ObjectIdentity
xRadiusPort = _XRadiusPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 35, 1)
)
_XRadiusPortTable_Object = MibTable
xRadiusPortTable = _XRadiusPortTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 35, 1, 1)
)
if mibBuilder.loadTexts:
    xRadiusPortTable.setStatus("mandatory")
_XRadiusPortEntry_Object = MibTableRow
xRadiusPortEntry = _XRadiusPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 35, 1, 1, 1)
)
xRadiusPortEntry.setIndexNames(
    (0, "MRV-IN-REACH-RADIUS-MIB", "xRadiusPortIndex"),
)
if mibBuilder.loadTexts:
    xRadiusPortEntry.setStatus("mandatory")
_XRadiusPortIndex_Type = Integer32
_XRadiusPortIndex_Object = MibTableColumn
xRadiusPortIndex = _XRadiusPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 35, 1, 1, 1, 1),
    _XRadiusPortIndex_Type()
)
xRadiusPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xRadiusPortIndex.setStatus("mandatory")


class _XRadiusPortStatus_Type(Integer32):
    """Custom type xRadiusPortStatus based on Integer32"""
    defaultValue = 1

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


_XRadiusPortStatus_Type.__name__ = "Integer32"
_XRadiusPortStatus_Object = MibTableColumn
xRadiusPortStatus = _XRadiusPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 35, 1, 1, 1, 2),
    _XRadiusPortStatus_Type()
)
xRadiusPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xRadiusPortStatus.setStatus("mandatory")


class _XRadiusPortSolicitStatus_Type(Integer32):
    """Custom type xRadiusPortSolicitStatus based on Integer32"""
    defaultValue = 1

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


_XRadiusPortSolicitStatus_Type.__name__ = "Integer32"
_XRadiusPortSolicitStatus_Object = MibTableColumn
xRadiusPortSolicitStatus = _XRadiusPortSolicitStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 35, 1, 1, 1, 3),
    _XRadiusPortSolicitStatus_Type()
)
xRadiusPortSolicitStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xRadiusPortSolicitStatus.setStatus("mandatory")


class _XRadiusAcctPortStatus_Type(Integer32):
    """Custom type xRadiusAcctPortStatus based on Integer32"""
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
          ("enabled", 2),
          ("limited", 3))
    )


_XRadiusAcctPortStatus_Type.__name__ = "Integer32"
_XRadiusAcctPortStatus_Object = MibTableColumn
xRadiusAcctPortStatus = _XRadiusAcctPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 35, 1, 1, 1, 4),
    _XRadiusAcctPortStatus_Type()
)
xRadiusAcctPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xRadiusAcctPortStatus.setStatus("mandatory")
_XRadiusCircuit_ObjectIdentity = ObjectIdentity
xRadiusCircuit = _XRadiusCircuit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 35, 2)
)
_XRadiusCircuitTable_Object = MibTable
xRadiusCircuitTable = _XRadiusCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 35, 2, 1)
)
if mibBuilder.loadTexts:
    xRadiusCircuitTable.setStatus("mandatory")
_XRadiusCircuitEntry_Object = MibTableRow
xRadiusCircuitEntry = _XRadiusCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 35, 2, 1, 1)
)
xRadiusCircuitEntry.setIndexNames(
    (0, "MRV-IN-REACH-RADIUS-MIB", "xRadiusCircuitIndex"),
)
if mibBuilder.loadTexts:
    xRadiusCircuitEntry.setStatus("mandatory")
_XRadiusCircuitIndex_Type = Integer32
_XRadiusCircuitIndex_Object = MibTableColumn
xRadiusCircuitIndex = _XRadiusCircuitIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 35, 2, 1, 1, 1),
    _XRadiusCircuitIndex_Type()
)
xRadiusCircuitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xRadiusCircuitIndex.setStatus("mandatory")


class _XRadiusCircAcctOnOff_Type(Integer32):
    """Custom type xRadiusCircAcctOnOff based on Integer32"""
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
          ("enabled", 2),
          ("limited", 3))
    )


_XRadiusCircAcctOnOff_Type.__name__ = "Integer32"
_XRadiusCircAcctOnOff_Object = MibTableColumn
xRadiusCircAcctOnOff = _XRadiusCircAcctOnOff_Object(
    (1, 3, 6, 1, 4, 1, 33, 35, 2, 1, 1, 2),
    _XRadiusCircAcctOnOff_Type()
)
xRadiusCircAcctOnOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xRadiusCircAcctOnOff.setStatus("mandatory")
_XRadiusConfig_ObjectIdentity = ObjectIdentity
xRadiusConfig = _XRadiusConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 35, 3)
)


class _XRadiusAuthServerPort_Type(Integer32):
    """Custom type xRadiusAuthServerPort based on Integer32"""
    defaultValue = 1645

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_XRadiusAuthServerPort_Type.__name__ = "Integer32"
_XRadiusAuthServerPort_Object = MibScalar
xRadiusAuthServerPort = _XRadiusAuthServerPort_Object(
    (1, 3, 6, 1, 4, 1, 33, 35, 3, 1),
    _XRadiusAuthServerPort_Type()
)
xRadiusAuthServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xRadiusAuthServerPort.setStatus("mandatory")


class _XRadiusAcctServerPort_Type(Integer32):
    """Custom type xRadiusAcctServerPort based on Integer32"""
    defaultValue = 1646

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_XRadiusAcctServerPort_Type.__name__ = "Integer32"
_XRadiusAcctServerPort_Object = MibScalar
xRadiusAcctServerPort = _XRadiusAcctServerPort_Object(
    (1, 3, 6, 1, 4, 1, 33, 35, 3, 2),
    _XRadiusAcctServerPort_Type()
)
xRadiusAcctServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xRadiusAcctServerPort.setStatus("mandatory")


class _XRadiusTimeout_Type(Integer32):
    """Custom type xRadiusTimeout based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_XRadiusTimeout_Type.__name__ = "Integer32"
_XRadiusTimeout_Object = MibScalar
xRadiusTimeout = _XRadiusTimeout_Object(
    (1, 3, 6, 1, 4, 1, 33, 35, 3, 3),
    _XRadiusTimeout_Type()
)
xRadiusTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xRadiusTimeout.setStatus("mandatory")


class _XRadiusServerRetries_Type(Integer32):
    """Custom type xRadiusServerRetries based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_XRadiusServerRetries_Type.__name__ = "Integer32"
_XRadiusServerRetries_Object = MibScalar
xRadiusServerRetries = _XRadiusServerRetries_Object(
    (1, 3, 6, 1, 4, 1, 33, 35, 3, 4),
    _XRadiusServerRetries_Type()
)
xRadiusServerRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xRadiusServerRetries.setStatus("mandatory")


class _XRadiusAcctLogAttempts_Type(Integer32):
    """Custom type xRadiusAcctLogAttempts based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50000),
    )


_XRadiusAcctLogAttempts_Type.__name__ = "Integer32"
_XRadiusAcctLogAttempts_Object = MibScalar
xRadiusAcctLogAttempts = _XRadiusAcctLogAttempts_Object(
    (1, 3, 6, 1, 4, 1, 33, 35, 3, 5),
    _XRadiusAcctLogAttempts_Type()
)
xRadiusAcctLogAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xRadiusAcctLogAttempts.setStatus("mandatory")


class _XRadiusChapChallengeSize_Type(Integer32):
    """Custom type xRadiusChapChallengeSize based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 128),
    )


_XRadiusChapChallengeSize_Type.__name__ = "Integer32"
_XRadiusChapChallengeSize_Object = MibScalar
xRadiusChapChallengeSize = _XRadiusChapChallengeSize_Object(
    (1, 3, 6, 1, 4, 1, 33, 35, 3, 6),
    _XRadiusChapChallengeSize_Type()
)
xRadiusChapChallengeSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xRadiusChapChallengeSize.setStatus("mandatory")


class _XRadiusLogging_Type(Integer32):
    """Custom type xRadiusLogging based on Integer32"""
    defaultValue = 1

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


_XRadiusLogging_Type.__name__ = "Integer32"
_XRadiusLogging_Object = MibScalar
xRadiusLogging = _XRadiusLogging_Object(
    (1, 3, 6, 1, 4, 1, 33, 35, 3, 7),
    _XRadiusLogging_Type()
)
xRadiusLogging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xRadiusLogging.setStatus("mandatory")


class _XRadiusMessage_Type(DisplayString):
    """Custom type xRadiusMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(40, 40),
    )


_XRadiusMessage_Type.__name__ = "DisplayString"
_XRadiusMessage_Object = MibScalar
xRadiusMessage = _XRadiusMessage_Object(
    (1, 3, 6, 1, 4, 1, 33, 35, 3, 8),
    _XRadiusMessage_Type()
)
xRadiusMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xRadiusMessage.setStatus("mandatory")
_XRadiusServers_ObjectIdentity = ObjectIdentity
xRadiusServers = _XRadiusServers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 35, 4)
)
_XRadServer1SubGrp_ObjectIdentity = ObjectIdentity
xRadServer1SubGrp = _XRadServer1SubGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 35, 4, 1)
)


class _XRadiusServerName1_Type(OctetString):
    """Custom type xRadiusServerName1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(51, 51),
    )


_XRadiusServerName1_Type.__name__ = "OctetString"
_XRadiusServerName1_Object = MibScalar
xRadiusServerName1 = _XRadiusServerName1_Object(
    (1, 3, 6, 1, 4, 1, 33, 35, 4, 1, 1),
    _XRadiusServerName1_Type()
)
xRadiusServerName1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xRadiusServerName1.setStatus("mandatory")


class _XRadiusSecret1_Type(OctetString):
    """Custom type xRadiusSecret1 based on OctetString"""
    defaultValue = OctetString("Default_Secret")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_XRadiusSecret1_Type.__name__ = "OctetString"
_XRadiusSecret1_Object = MibScalar
xRadiusSecret1 = _XRadiusSecret1_Object(
    (1, 3, 6, 1, 4, 1, 33, 35, 4, 1, 2),
    _XRadiusSecret1_Type()
)
xRadiusSecret1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xRadiusSecret1.setStatus("obsolete")
_XRadiusServerAccess1_Type = Counter32
_XRadiusServerAccess1_Object = MibScalar
xRadiusServerAccess1 = _XRadiusServerAccess1_Object(
    (1, 3, 6, 1, 4, 1, 33, 35, 4, 1, 3),
    _XRadiusServerAccess1_Type()
)
xRadiusServerAccess1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xRadiusServerAccess1.setStatus("mandatory")
_XRadiusServerAccessFailed1_Type = Counter32
_XRadiusServerAccessFailed1_Object = MibScalar
xRadiusServerAccessFailed1 = _XRadiusServerAccessFailed1_Object(
    (1, 3, 6, 1, 4, 1, 33, 35, 4, 1, 4),
    _XRadiusServerAccessFailed1_Type()
)
xRadiusServerAccessFailed1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xRadiusServerAccessFailed1.setStatus("mandatory")
_XRadServer2SubGrp_ObjectIdentity = ObjectIdentity
xRadServer2SubGrp = _XRadServer2SubGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 35, 4, 2)
)


class _XRadiusServerName2_Type(OctetString):
    """Custom type xRadiusServerName2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(51, 51),
    )


_XRadiusServerName2_Type.__name__ = "OctetString"
_XRadiusServerName2_Object = MibScalar
xRadiusServerName2 = _XRadiusServerName2_Object(
    (1, 3, 6, 1, 4, 1, 33, 35, 4, 2, 1),
    _XRadiusServerName2_Type()
)
xRadiusServerName2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xRadiusServerName2.setStatus("mandatory")


class _XRadiusSecret2_Type(OctetString):
    """Custom type xRadiusSecret2 based on OctetString"""
    defaultValue = OctetString("Default_Secret")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_XRadiusSecret2_Type.__name__ = "OctetString"
_XRadiusSecret2_Object = MibScalar
xRadiusSecret2 = _XRadiusSecret2_Object(
    (1, 3, 6, 1, 4, 1, 33, 35, 4, 2, 2),
    _XRadiusSecret2_Type()
)
xRadiusSecret2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xRadiusSecret2.setStatus("obsolete")
_XRadiusServerAccess2_Type = Counter32
_XRadiusServerAccess2_Object = MibScalar
xRadiusServerAccess2 = _XRadiusServerAccess2_Object(
    (1, 3, 6, 1, 4, 1, 33, 35, 4, 2, 3),
    _XRadiusServerAccess2_Type()
)
xRadiusServerAccess2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xRadiusServerAccess2.setStatus("mandatory")
_XRadiusServerAccessFailed2_Type = Counter32
_XRadiusServerAccessFailed2_Object = MibScalar
xRadiusServerAccessFailed2 = _XRadiusServerAccessFailed2_Object(
    (1, 3, 6, 1, 4, 1, 33, 35, 4, 2, 4),
    _XRadiusServerAccessFailed2_Type()
)
xRadiusServerAccessFailed2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xRadiusServerAccessFailed2.setStatus("mandatory")
_XRadiusCounters_ObjectIdentity = ObjectIdentity
xRadiusCounters = _XRadiusCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 35, 5)
)
_XRadAuthCtsSubGrp_ObjectIdentity = ObjectIdentity
xRadAuthCtsSubGrp = _XRadAuthCtsSubGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 35, 5, 1)
)
_XRadiusLogins_Type = Counter32
_XRadiusLogins_Object = MibScalar
xRadiusLogins = _XRadiusLogins_Object(
    (1, 3, 6, 1, 4, 1, 33, 35, 5, 1, 1),
    _XRadiusLogins_Type()
)
xRadiusLogins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xRadiusLogins.setStatus("mandatory")
_XRadiusLoginsFailed_Type = Counter32
_XRadiusLoginsFailed_Object = MibScalar
xRadiusLoginsFailed = _XRadiusLoginsFailed_Object(
    (1, 3, 6, 1, 4, 1, 33, 35, 5, 1, 2),
    _XRadiusLoginsFailed_Type()
)
xRadiusLoginsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xRadiusLoginsFailed.setStatus("mandatory")
_XRadiusConfigFailed_Type = Counter32
_XRadiusConfigFailed_Object = MibScalar
xRadiusConfigFailed = _XRadiusConfigFailed_Object(
    (1, 3, 6, 1, 4, 1, 33, 35, 5, 1, 3),
    _XRadiusConfigFailed_Type()
)
xRadiusConfigFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xRadiusConfigFailed.setStatus("mandatory")
_XRadiusPolicyFailed_Type = Counter32
_XRadiusPolicyFailed_Object = MibScalar
xRadiusPolicyFailed = _XRadiusPolicyFailed_Object(
    (1, 3, 6, 1, 4, 1, 33, 35, 5, 1, 4),
    _XRadiusPolicyFailed_Type()
)
xRadiusPolicyFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xRadiusPolicyFailed.setStatus("mandatory")
_XRadAcctCtsSubGrp_ObjectIdentity = ObjectIdentity
xRadAcctCtsSubGrp = _XRadAcctCtsSubGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 35, 5, 2)
)
_XRadiusAcctSuccess_Type = Counter32
_XRadiusAcctSuccess_Object = MibScalar
xRadiusAcctSuccess = _XRadiusAcctSuccess_Object(
    (1, 3, 6, 1, 4, 1, 33, 35, 5, 2, 1),
    _XRadiusAcctSuccess_Type()
)
xRadiusAcctSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xRadiusAcctSuccess.setStatus("mandatory")
_XRadiusAcctFailed_Type = Counter32
_XRadiusAcctFailed_Object = MibScalar
xRadiusAcctFailed = _XRadiusAcctFailed_Object(
    (1, 3, 6, 1, 4, 1, 33, 35, 5, 2, 2),
    _XRadiusAcctFailed_Type()
)
xRadiusAcctFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xRadiusAcctFailed.setStatus("mandatory")
_XRadiusAcctReqWait_Type = Counter32
_XRadiusAcctReqWait_Object = MibScalar
xRadiusAcctReqWait = _XRadiusAcctReqWait_Object(
    (1, 3, 6, 1, 4, 1, 33, 35, 5, 2, 3),
    _XRadiusAcctReqWait_Type()
)
xRadiusAcctReqWait.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xRadiusAcctReqWait.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MRV-IN-REACH-RADIUS-MIB",
    **{"xRadius": xRadius,
       "xRadiusPort": xRadiusPort,
       "xRadiusPortTable": xRadiusPortTable,
       "xRadiusPortEntry": xRadiusPortEntry,
       "xRadiusPortIndex": xRadiusPortIndex,
       "xRadiusPortStatus": xRadiusPortStatus,
       "xRadiusPortSolicitStatus": xRadiusPortSolicitStatus,
       "xRadiusAcctPortStatus": xRadiusAcctPortStatus,
       "xRadiusCircuit": xRadiusCircuit,
       "xRadiusCircuitTable": xRadiusCircuitTable,
       "xRadiusCircuitEntry": xRadiusCircuitEntry,
       "xRadiusCircuitIndex": xRadiusCircuitIndex,
       "xRadiusCircAcctOnOff": xRadiusCircAcctOnOff,
       "xRadiusConfig": xRadiusConfig,
       "xRadiusAuthServerPort": xRadiusAuthServerPort,
       "xRadiusAcctServerPort": xRadiusAcctServerPort,
       "xRadiusTimeout": xRadiusTimeout,
       "xRadiusServerRetries": xRadiusServerRetries,
       "xRadiusAcctLogAttempts": xRadiusAcctLogAttempts,
       "xRadiusChapChallengeSize": xRadiusChapChallengeSize,
       "xRadiusLogging": xRadiusLogging,
       "xRadiusMessage": xRadiusMessage,
       "xRadiusServers": xRadiusServers,
       "xRadServer1SubGrp": xRadServer1SubGrp,
       "xRadiusServerName1": xRadiusServerName1,
       "xRadiusSecret1": xRadiusSecret1,
       "xRadiusServerAccess1": xRadiusServerAccess1,
       "xRadiusServerAccessFailed1": xRadiusServerAccessFailed1,
       "xRadServer2SubGrp": xRadServer2SubGrp,
       "xRadiusServerName2": xRadiusServerName2,
       "xRadiusSecret2": xRadiusSecret2,
       "xRadiusServerAccess2": xRadiusServerAccess2,
       "xRadiusServerAccessFailed2": xRadiusServerAccessFailed2,
       "xRadiusCounters": xRadiusCounters,
       "xRadAuthCtsSubGrp": xRadAuthCtsSubGrp,
       "xRadiusLogins": xRadiusLogins,
       "xRadiusLoginsFailed": xRadiusLoginsFailed,
       "xRadiusConfigFailed": xRadiusConfigFailed,
       "xRadiusPolicyFailed": xRadiusPolicyFailed,
       "xRadAcctCtsSubGrp": xRadAcctCtsSubGrp,
       "xRadiusAcctSuccess": xRadiusAcctSuccess,
       "xRadiusAcctFailed": xRadiusAcctFailed,
       "xRadiusAcctReqWait": xRadiusAcctReqWait}
)
