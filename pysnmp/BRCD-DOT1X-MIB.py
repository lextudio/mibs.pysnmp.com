# SNMP MIB module (BRCD-DOT1X-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BRCD-DOT1X-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:48:35 2024
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

brcdDot1xAuth = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 38)
)
brcdDot1xAuth.setRevisions(
        ("2010-09-30 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class VlanId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )



# MIB Managed Objects in the order of their OIDs

_BrcdDot1xAuthGlobalConfigGroup_ObjectIdentity = ObjectIdentity
brcdDot1xAuthGlobalConfigGroup = _BrcdDot1xAuthGlobalConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 38, 1)
)


class _BrcdDot1xAuthGlobalConfigQuietperiod_Type(Unsigned32):
    """Custom type brcdDot1xAuthGlobalConfigQuietperiod based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967294),
    )


_BrcdDot1xAuthGlobalConfigQuietperiod_Type.__name__ = "Unsigned32"
_BrcdDot1xAuthGlobalConfigQuietperiod_Object = MibScalar
brcdDot1xAuthGlobalConfigQuietperiod = _BrcdDot1xAuthGlobalConfigQuietperiod_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 38, 1, 1),
    _BrcdDot1xAuthGlobalConfigQuietperiod_Type()
)
brcdDot1xAuthGlobalConfigQuietperiod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brcdDot1xAuthGlobalConfigQuietperiod.setStatus("current")
if mibBuilder.loadTexts:
    brcdDot1xAuthGlobalConfigQuietperiod.setUnits("seconds")


class _BrcdDot1xAuthGlobalConfigTxPeriod_Type(Unsigned32):
    """Custom type brcdDot1xAuthGlobalConfigTxPeriod based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967294),
    )


_BrcdDot1xAuthGlobalConfigTxPeriod_Type.__name__ = "Unsigned32"
_BrcdDot1xAuthGlobalConfigTxPeriod_Object = MibScalar
brcdDot1xAuthGlobalConfigTxPeriod = _BrcdDot1xAuthGlobalConfigTxPeriod_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 38, 1, 2),
    _BrcdDot1xAuthGlobalConfigTxPeriod_Type()
)
brcdDot1xAuthGlobalConfigTxPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brcdDot1xAuthGlobalConfigTxPeriod.setStatus("current")
if mibBuilder.loadTexts:
    brcdDot1xAuthGlobalConfigTxPeriod.setUnits("seconds")


class _BrcdDot1xAuthGlobalConfigSuppTimeOut_Type(Unsigned32):
    """Custom type brcdDot1xAuthGlobalConfigSuppTimeOut based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967294),
    )


_BrcdDot1xAuthGlobalConfigSuppTimeOut_Type.__name__ = "Unsigned32"
_BrcdDot1xAuthGlobalConfigSuppTimeOut_Object = MibScalar
brcdDot1xAuthGlobalConfigSuppTimeOut = _BrcdDot1xAuthGlobalConfigSuppTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 38, 1, 3),
    _BrcdDot1xAuthGlobalConfigSuppTimeOut_Type()
)
brcdDot1xAuthGlobalConfigSuppTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brcdDot1xAuthGlobalConfigSuppTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    brcdDot1xAuthGlobalConfigSuppTimeOut.setUnits("seconds")


class _BrcdDot1xAuthGlobalConfigAuthServerTimeOut_Type(Unsigned32):
    """Custom type brcdDot1xAuthGlobalConfigAuthServerTimeOut based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967294),
    )


_BrcdDot1xAuthGlobalConfigAuthServerTimeOut_Type.__name__ = "Unsigned32"
_BrcdDot1xAuthGlobalConfigAuthServerTimeOut_Object = MibScalar
brcdDot1xAuthGlobalConfigAuthServerTimeOut = _BrcdDot1xAuthGlobalConfigAuthServerTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 38, 1, 4),
    _BrcdDot1xAuthGlobalConfigAuthServerTimeOut_Type()
)
brcdDot1xAuthGlobalConfigAuthServerTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brcdDot1xAuthGlobalConfigAuthServerTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    brcdDot1xAuthGlobalConfigAuthServerTimeOut.setUnits("seconds")


class _BrcdDot1xAuthGlobalConfigMaxReq_Type(Unsigned32):
    """Custom type brcdDot1xAuthGlobalConfigMaxReq based on Unsigned32"""
    defaultValue = 2


_BrcdDot1xAuthGlobalConfigMaxReq_Object = MibScalar
brcdDot1xAuthGlobalConfigMaxReq = _BrcdDot1xAuthGlobalConfigMaxReq_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 38, 1, 5),
    _BrcdDot1xAuthGlobalConfigMaxReq_Type()
)
brcdDot1xAuthGlobalConfigMaxReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brcdDot1xAuthGlobalConfigMaxReq.setStatus("current")


class _BrcdDot1xAuthGlobalConfigReAuthMax_Type(Unsigned32):
    """Custom type brcdDot1xAuthGlobalConfigReAuthMax based on Unsigned32"""
    defaultValue = 2


_BrcdDot1xAuthGlobalConfigReAuthMax_Object = MibScalar
brcdDot1xAuthGlobalConfigReAuthMax = _BrcdDot1xAuthGlobalConfigReAuthMax_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 38, 1, 6),
    _BrcdDot1xAuthGlobalConfigReAuthMax_Type()
)
brcdDot1xAuthGlobalConfigReAuthMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brcdDot1xAuthGlobalConfigReAuthMax.setStatus("current")


class _BrcdDot1xAuthGlobalConfigReAuthPeriod_Type(Unsigned32):
    """Custom type brcdDot1xAuthGlobalConfigReAuthPeriod based on Unsigned32"""
    defaultValue = 3600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967294),
    )


_BrcdDot1xAuthGlobalConfigReAuthPeriod_Type.__name__ = "Unsigned32"
_BrcdDot1xAuthGlobalConfigReAuthPeriod_Object = MibScalar
brcdDot1xAuthGlobalConfigReAuthPeriod = _BrcdDot1xAuthGlobalConfigReAuthPeriod_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 38, 1, 7),
    _BrcdDot1xAuthGlobalConfigReAuthPeriod_Type()
)
brcdDot1xAuthGlobalConfigReAuthPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brcdDot1xAuthGlobalConfigReAuthPeriod.setStatus("current")
if mibBuilder.loadTexts:
    brcdDot1xAuthGlobalConfigReAuthPeriod.setUnits("seconds")
_BrcdDot1xAuthGlobalConfigProtocolVersion_Type = Unsigned32
_BrcdDot1xAuthGlobalConfigProtocolVersion_Object = MibScalar
brcdDot1xAuthGlobalConfigProtocolVersion = _BrcdDot1xAuthGlobalConfigProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 38, 1, 8),
    _BrcdDot1xAuthGlobalConfigProtocolVersion_Type()
)
brcdDot1xAuthGlobalConfigProtocolVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdDot1xAuthGlobalConfigProtocolVersion.setStatus("current")
_BrcdDot1xAuthGlobalConfigTotalPortsEnabled_Type = Unsigned32
_BrcdDot1xAuthGlobalConfigTotalPortsEnabled_Object = MibScalar
brcdDot1xAuthGlobalConfigTotalPortsEnabled = _BrcdDot1xAuthGlobalConfigTotalPortsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 38, 1, 9),
    _BrcdDot1xAuthGlobalConfigTotalPortsEnabled_Type()
)
brcdDot1xAuthGlobalConfigTotalPortsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdDot1xAuthGlobalConfigTotalPortsEnabled.setStatus("current")


class _BrcdDot1xAuthGlobalConfigReauthStatus_Type(EnabledStatus):
    """Custom type brcdDot1xAuthGlobalConfigReauthStatus based on EnabledStatus"""


_BrcdDot1xAuthGlobalConfigReauthStatus_Object = MibScalar
brcdDot1xAuthGlobalConfigReauthStatus = _BrcdDot1xAuthGlobalConfigReauthStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 38, 1, 10),
    _BrcdDot1xAuthGlobalConfigReauthStatus_Type()
)
brcdDot1xAuthGlobalConfigReauthStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brcdDot1xAuthGlobalConfigReauthStatus.setStatus("current")
_BrcdDot1xAuthGlobalConfigMacSessionMaxAge_Type = Unsigned32
_BrcdDot1xAuthGlobalConfigMacSessionMaxAge_Object = MibScalar
brcdDot1xAuthGlobalConfigMacSessionMaxAge = _BrcdDot1xAuthGlobalConfigMacSessionMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 38, 1, 11),
    _BrcdDot1xAuthGlobalConfigMacSessionMaxAge_Type()
)
brcdDot1xAuthGlobalConfigMacSessionMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brcdDot1xAuthGlobalConfigMacSessionMaxAge.setStatus("current")


class _BrcdDot1xAuthGlobalConfigNoAgingDeniedSessions_Type(EnabledStatus):
    """Custom type brcdDot1xAuthGlobalConfigNoAgingDeniedSessions based on EnabledStatus"""


_BrcdDot1xAuthGlobalConfigNoAgingDeniedSessions_Object = MibScalar
brcdDot1xAuthGlobalConfigNoAgingDeniedSessions = _BrcdDot1xAuthGlobalConfigNoAgingDeniedSessions_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 38, 1, 12),
    _BrcdDot1xAuthGlobalConfigNoAgingDeniedSessions_Type()
)
brcdDot1xAuthGlobalConfigNoAgingDeniedSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brcdDot1xAuthGlobalConfigNoAgingDeniedSessions.setStatus("current")


class _BrcdDot1xAuthGlobalConfigNoAgingPermittedSessions_Type(EnabledStatus):
    """Custom type brcdDot1xAuthGlobalConfigNoAgingPermittedSessions based on EnabledStatus"""


_BrcdDot1xAuthGlobalConfigNoAgingPermittedSessions_Object = MibScalar
brcdDot1xAuthGlobalConfigNoAgingPermittedSessions = _BrcdDot1xAuthGlobalConfigNoAgingPermittedSessions_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 38, 1, 13),
    _BrcdDot1xAuthGlobalConfigNoAgingPermittedSessions_Type()
)
brcdDot1xAuthGlobalConfigNoAgingPermittedSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brcdDot1xAuthGlobalConfigNoAgingPermittedSessions.setStatus("current")


class _BrcdDot1xAuthGlobalConfigAuthFailAction_Type(Integer32):
    """Custom type brcdDot1xAuthGlobalConfigAuthFailAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("blockTraffic", 1),
          ("restrictedVlan", 2))
    )


_BrcdDot1xAuthGlobalConfigAuthFailAction_Type.__name__ = "Integer32"
_BrcdDot1xAuthGlobalConfigAuthFailAction_Object = MibScalar
brcdDot1xAuthGlobalConfigAuthFailAction = _BrcdDot1xAuthGlobalConfigAuthFailAction_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 38, 1, 14),
    _BrcdDot1xAuthGlobalConfigAuthFailAction_Type()
)
brcdDot1xAuthGlobalConfigAuthFailAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brcdDot1xAuthGlobalConfigAuthFailAction.setStatus("current")
_BrcdDot1xAuthPortStatistics_ObjectIdentity = ObjectIdentity
brcdDot1xAuthPortStatistics = _BrcdDot1xAuthPortStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 38, 2)
)
_BrcdDot1xAuthPortStatTable_Object = MibTable
brcdDot1xAuthPortStatTable = _BrcdDot1xAuthPortStatTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 38, 2, 1)
)
if mibBuilder.loadTexts:
    brcdDot1xAuthPortStatTable.setStatus("current")
_BrcdDot1xAuthPortStatEntry_Object = MibTableRow
brcdDot1xAuthPortStatEntry = _BrcdDot1xAuthPortStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 38, 2, 1, 1)
)
brcdDot1xAuthPortStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    brcdDot1xAuthPortStatEntry.setStatus("current")
_BrcdDot1xAuthPortStatRxEAPFrames_Type = Counter32
_BrcdDot1xAuthPortStatRxEAPFrames_Object = MibTableColumn
brcdDot1xAuthPortStatRxEAPFrames = _BrcdDot1xAuthPortStatRxEAPFrames_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 38, 2, 1, 1, 1),
    _BrcdDot1xAuthPortStatRxEAPFrames_Type()
)
brcdDot1xAuthPortStatRxEAPFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdDot1xAuthPortStatRxEAPFrames.setStatus("current")
_BrcdDot1xAuthPortStatTxEAPFrames_Type = Counter32
_BrcdDot1xAuthPortStatTxEAPFrames_Object = MibTableColumn
brcdDot1xAuthPortStatTxEAPFrames = _BrcdDot1xAuthPortStatTxEAPFrames_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 38, 2, 1, 1, 2),
    _BrcdDot1xAuthPortStatTxEAPFrames_Type()
)
brcdDot1xAuthPortStatTxEAPFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdDot1xAuthPortStatTxEAPFrames.setStatus("current")
_BrcdDot1xAuthPortStatRxEAPStartFrames_Type = Counter32
_BrcdDot1xAuthPortStatRxEAPStartFrames_Object = MibTableColumn
brcdDot1xAuthPortStatRxEAPStartFrames = _BrcdDot1xAuthPortStatRxEAPStartFrames_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 38, 2, 1, 1, 3),
    _BrcdDot1xAuthPortStatRxEAPStartFrames_Type()
)
brcdDot1xAuthPortStatRxEAPStartFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdDot1xAuthPortStatRxEAPStartFrames.setStatus("current")
_BrcdDot1xAuthPortStatRxEAPLogOffFrames_Type = Counter32
_BrcdDot1xAuthPortStatRxEAPLogOffFrames_Object = MibTableColumn
brcdDot1xAuthPortStatRxEAPLogOffFrames = _BrcdDot1xAuthPortStatRxEAPLogOffFrames_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 38, 2, 1, 1, 4),
    _BrcdDot1xAuthPortStatRxEAPLogOffFrames_Type()
)
brcdDot1xAuthPortStatRxEAPLogOffFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdDot1xAuthPortStatRxEAPLogOffFrames.setStatus("current")
_BrcdDot1xAuthPortStatRxEAPRespIdFrames_Type = Counter32
_BrcdDot1xAuthPortStatRxEAPRespIdFrames_Object = MibTableColumn
brcdDot1xAuthPortStatRxEAPRespIdFrames = _BrcdDot1xAuthPortStatRxEAPRespIdFrames_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 38, 2, 1, 1, 5),
    _BrcdDot1xAuthPortStatRxEAPRespIdFrames_Type()
)
brcdDot1xAuthPortStatRxEAPRespIdFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdDot1xAuthPortStatRxEAPRespIdFrames.setStatus("current")
_BrcdDot1xAuthPortStatTxEAPReqIdFrames_Type = Counter32
_BrcdDot1xAuthPortStatTxEAPReqIdFrames_Object = MibTableColumn
brcdDot1xAuthPortStatTxEAPReqIdFrames = _BrcdDot1xAuthPortStatTxEAPReqIdFrames_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 38, 2, 1, 1, 6),
    _BrcdDot1xAuthPortStatTxEAPReqIdFrames_Type()
)
brcdDot1xAuthPortStatTxEAPReqIdFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdDot1xAuthPortStatTxEAPReqIdFrames.setStatus("current")
_BrcdDot1xAuthPortStatRxEAPInvalidFrames_Type = Counter32
_BrcdDot1xAuthPortStatRxEAPInvalidFrames_Object = MibTableColumn
brcdDot1xAuthPortStatRxEAPInvalidFrames = _BrcdDot1xAuthPortStatRxEAPInvalidFrames_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 38, 2, 1, 1, 7),
    _BrcdDot1xAuthPortStatRxEAPInvalidFrames_Type()
)
brcdDot1xAuthPortStatRxEAPInvalidFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdDot1xAuthPortStatRxEAPInvalidFrames.setStatus("current")
_BrcdDot1xAuthPortStatEAPLastFrameVersionRx_Type = Unsigned32
_BrcdDot1xAuthPortStatEAPLastFrameVersionRx_Object = MibTableColumn
brcdDot1xAuthPortStatEAPLastFrameVersionRx = _BrcdDot1xAuthPortStatEAPLastFrameVersionRx_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 38, 2, 1, 1, 8),
    _BrcdDot1xAuthPortStatEAPLastFrameVersionRx_Type()
)
brcdDot1xAuthPortStatEAPLastFrameVersionRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdDot1xAuthPortStatEAPLastFrameVersionRx.setStatus("current")
_BrcdDot1xAuthPortStatRxEAPRespOrIdFrames_Type = Counter32
_BrcdDot1xAuthPortStatRxEAPRespOrIdFrames_Object = MibTableColumn
brcdDot1xAuthPortStatRxEAPRespOrIdFrames = _BrcdDot1xAuthPortStatRxEAPRespOrIdFrames_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 38, 2, 1, 1, 9),
    _BrcdDot1xAuthPortStatRxEAPRespOrIdFrames_Type()
)
brcdDot1xAuthPortStatRxEAPRespOrIdFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdDot1xAuthPortStatRxEAPRespOrIdFrames.setStatus("current")
_BrcdDot1xAuthPortStatRxLengthErrorFrame_Type = Integer32
_BrcdDot1xAuthPortStatRxLengthErrorFrame_Object = MibTableColumn
brcdDot1xAuthPortStatRxLengthErrorFrame = _BrcdDot1xAuthPortStatRxLengthErrorFrame_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 38, 2, 1, 1, 10),
    _BrcdDot1xAuthPortStatRxLengthErrorFrame_Type()
)
brcdDot1xAuthPortStatRxLengthErrorFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdDot1xAuthPortStatRxLengthErrorFrame.setStatus("current")
_BrcdDot1xAuthPortStatTxRequestFrames_Type = Counter32
_BrcdDot1xAuthPortStatTxRequestFrames_Object = MibTableColumn
brcdDot1xAuthPortStatTxRequestFrames = _BrcdDot1xAuthPortStatTxRequestFrames_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 38, 2, 1, 1, 11),
    _BrcdDot1xAuthPortStatTxRequestFrames_Type()
)
brcdDot1xAuthPortStatTxRequestFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdDot1xAuthPortStatTxRequestFrames.setStatus("current")
_BrcdDot1xAuthPortStatLastEAPFrameSource_Type = MacAddress
_BrcdDot1xAuthPortStatLastEAPFrameSource_Object = MibTableColumn
brcdDot1xAuthPortStatLastEAPFrameSource = _BrcdDot1xAuthPortStatLastEAPFrameSource_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 38, 2, 1, 1, 12),
    _BrcdDot1xAuthPortStatLastEAPFrameSource_Type()
)
brcdDot1xAuthPortStatLastEAPFrameSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdDot1xAuthPortStatLastEAPFrameSource.setStatus("current")
_BrcdDot1xAuthPortConfig_ObjectIdentity = ObjectIdentity
brcdDot1xAuthPortConfig = _BrcdDot1xAuthPortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 38, 3)
)
_BrcdDot1xAuthPortConfigTable_Object = MibTable
brcdDot1xAuthPortConfigTable = _BrcdDot1xAuthPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 38, 3, 1)
)
if mibBuilder.loadTexts:
    brcdDot1xAuthPortConfigTable.setStatus("current")
_BrcdDot1xAuthPortConfigEntry_Object = MibTableRow
brcdDot1xAuthPortConfigEntry = _BrcdDot1xAuthPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 38, 3, 1, 1)
)
brcdDot1xAuthPortConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    brcdDot1xAuthPortConfigEntry.setStatus("current")


class _BrcdDot1xAuthPortConfigPortControl_Type(Integer32):
    """Custom type brcdDot1xAuthPortConfigPortControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("controlauto", 2),
          ("forceAuthorized", 3),
          ("forceUnauthorized", 1))
    )


_BrcdDot1xAuthPortConfigPortControl_Type.__name__ = "Integer32"
_BrcdDot1xAuthPortConfigPortControl_Object = MibTableColumn
brcdDot1xAuthPortConfigPortControl = _BrcdDot1xAuthPortConfigPortControl_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 38, 3, 1, 1, 1),
    _BrcdDot1xAuthPortConfigPortControl_Type()
)
brcdDot1xAuthPortConfigPortControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brcdDot1xAuthPortConfigPortControl.setStatus("current")
_BrcdDot1xAuthPortConfigFilterStrictSec_Type = EnabledStatus
_BrcdDot1xAuthPortConfigFilterStrictSec_Object = MibTableColumn
brcdDot1xAuthPortConfigFilterStrictSec = _BrcdDot1xAuthPortConfigFilterStrictSec_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 38, 3, 1, 1, 2),
    _BrcdDot1xAuthPortConfigFilterStrictSec_Type()
)
brcdDot1xAuthPortConfigFilterStrictSec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brcdDot1xAuthPortConfigFilterStrictSec.setStatus("current")
_BrcdDot1xAuthPortConfigDot1xOnPort_Type = EnabledStatus
_BrcdDot1xAuthPortConfigDot1xOnPort_Object = MibTableColumn
brcdDot1xAuthPortConfigDot1xOnPort = _BrcdDot1xAuthPortConfigDot1xOnPort_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 38, 3, 1, 1, 3),
    _BrcdDot1xAuthPortConfigDot1xOnPort_Type()
)
brcdDot1xAuthPortConfigDot1xOnPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brcdDot1xAuthPortConfigDot1xOnPort.setStatus("current")
_BrcdDot1xAuthPortState_ObjectIdentity = ObjectIdentity
brcdDot1xAuthPortState = _BrcdDot1xAuthPortState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 38, 4)
)
_BrcdDot1xAuthPortStateTable_Object = MibTable
brcdDot1xAuthPortStateTable = _BrcdDot1xAuthPortStateTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 38, 4, 1)
)
if mibBuilder.loadTexts:
    brcdDot1xAuthPortStateTable.setStatus("current")
_BrcdDot1xAuthPortStateEntry_Object = MibTableRow
brcdDot1xAuthPortStateEntry = _BrcdDot1xAuthPortStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 38, 4, 1, 1)
)
brcdDot1xAuthPortStateEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    brcdDot1xAuthPortStateEntry.setStatus("current")
_BrcdDot1xAuthPortStateMacSessions_Type = Unsigned32
_BrcdDot1xAuthPortStateMacSessions_Object = MibTableColumn
brcdDot1xAuthPortStateMacSessions = _BrcdDot1xAuthPortStateMacSessions_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 38, 4, 1, 1, 1),
    _BrcdDot1xAuthPortStateMacSessions_Type()
)
brcdDot1xAuthPortStateMacSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdDot1xAuthPortStateMacSessions.setStatus("current")
_BrcdDot1xAuthPortStateAuthMacSessions_Type = Unsigned32
_BrcdDot1xAuthPortStateAuthMacSessions_Object = MibTableColumn
brcdDot1xAuthPortStateAuthMacSessions = _BrcdDot1xAuthPortStateAuthMacSessions_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 38, 4, 1, 1, 2),
    _BrcdDot1xAuthPortStateAuthMacSessions_Type()
)
brcdDot1xAuthPortStateAuthMacSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdDot1xAuthPortStateAuthMacSessions.setStatus("current")
_BrcdDot1xAuthPortStateOriginalPVID_Type = Unsigned32
_BrcdDot1xAuthPortStateOriginalPVID_Object = MibTableColumn
brcdDot1xAuthPortStateOriginalPVID = _BrcdDot1xAuthPortStateOriginalPVID_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 38, 4, 1, 1, 3),
    _BrcdDot1xAuthPortStateOriginalPVID_Type()
)
brcdDot1xAuthPortStateOriginalPVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdDot1xAuthPortStateOriginalPVID.setStatus("current")
_BrcdDot1xAuthPortStatePVIDMacTotal_Type = Unsigned32
_BrcdDot1xAuthPortStatePVIDMacTotal_Object = MibTableColumn
brcdDot1xAuthPortStatePVIDMacTotal = _BrcdDot1xAuthPortStatePVIDMacTotal_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 38, 4, 1, 1, 4),
    _BrcdDot1xAuthPortStatePVIDMacTotal_Type()
)
brcdDot1xAuthPortStatePVIDMacTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdDot1xAuthPortStatePVIDMacTotal.setStatus("current")
_BrcdDot1xAuthPortStatePVIDMacAuthorized_Type = Unsigned32
_BrcdDot1xAuthPortStatePVIDMacAuthorized_Object = MibTableColumn
brcdDot1xAuthPortStatePVIDMacAuthorized = _BrcdDot1xAuthPortStatePVIDMacAuthorized_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 38, 4, 1, 1, 5),
    _BrcdDot1xAuthPortStatePVIDMacAuthorized_Type()
)
brcdDot1xAuthPortStatePVIDMacAuthorized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdDot1xAuthPortStatePVIDMacAuthorized.setStatus("current")


class _BrcdDot1xAuthPortStatePortVlanState_Type(Integer32):
    """Custom type brcdDot1xAuthPortStatePortVlanState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 3),
          ("radius", 1),
          ("restricted", 2))
    )


_BrcdDot1xAuthPortStatePortVlanState_Type.__name__ = "Integer32"
_BrcdDot1xAuthPortStatePortVlanState_Object = MibTableColumn
brcdDot1xAuthPortStatePortVlanState = _BrcdDot1xAuthPortStatePortVlanState_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 38, 4, 1, 1, 6),
    _BrcdDot1xAuthPortStatePortVlanState_Type()
)
brcdDot1xAuthPortStatePortVlanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdDot1xAuthPortStatePortVlanState.setStatus("current")
_BrcdDot1xAuthPortStatePVID_Type = Unsigned32
_BrcdDot1xAuthPortStatePVID_Object = MibTableColumn
brcdDot1xAuthPortStatePVID = _BrcdDot1xAuthPortStatePVID_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 38, 4, 1, 1, 7),
    _BrcdDot1xAuthPortStatePVID_Type()
)
brcdDot1xAuthPortStatePVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdDot1xAuthPortStatePVID.setStatus("current")
_BrcdDot1xAuthPortStateRestrictPVID_Type = Unsigned32
_BrcdDot1xAuthPortStateRestrictPVID_Object = MibTableColumn
brcdDot1xAuthPortStateRestrictPVID = _BrcdDot1xAuthPortStateRestrictPVID_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 38, 4, 1, 1, 8),
    _BrcdDot1xAuthPortStateRestrictPVID_Type()
)
brcdDot1xAuthPortStateRestrictPVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdDot1xAuthPortStateRestrictPVID.setStatus("current")
_BrcdDot1xAuthPortStateRadiusAssignPVID_Type = Unsigned32
_BrcdDot1xAuthPortStateRadiusAssignPVID_Object = MibTableColumn
brcdDot1xAuthPortStateRadiusAssignPVID = _BrcdDot1xAuthPortStateRadiusAssignPVID_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 38, 4, 1, 1, 9),
    _BrcdDot1xAuthPortStateRadiusAssignPVID_Type()
)
brcdDot1xAuthPortStateRadiusAssignPVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdDot1xAuthPortStateRadiusAssignPVID.setStatus("current")
_BrcdDot1xAuthMacSession_ObjectIdentity = ObjectIdentity
brcdDot1xAuthMacSession = _BrcdDot1xAuthMacSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 38, 5)
)
_BrcdDot1xAuthMacSessionTable_Object = MibTable
brcdDot1xAuthMacSessionTable = _BrcdDot1xAuthMacSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 38, 5, 1)
)
if mibBuilder.loadTexts:
    brcdDot1xAuthMacSessionTable.setStatus("current")
_BrcdDot1xAuthMacSessionEntry_Object = MibTableRow
brcdDot1xAuthMacSessionEntry = _BrcdDot1xAuthMacSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 38, 5, 1, 1)
)
brcdDot1xAuthMacSessionEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "BRCD-DOT1X-MIB", "brcdDot1xAuthMacSessionAuthMac"),
)
if mibBuilder.loadTexts:
    brcdDot1xAuthMacSessionEntry.setStatus("current")
_BrcdDot1xAuthMacSessionAuthMac_Type = MacAddress
_BrcdDot1xAuthMacSessionAuthMac_Object = MibTableColumn
brcdDot1xAuthMacSessionAuthMac = _BrcdDot1xAuthMacSessionAuthMac_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 38, 5, 1, 1, 1),
    _BrcdDot1xAuthMacSessionAuthMac_Type()
)
brcdDot1xAuthMacSessionAuthMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brcdDot1xAuthMacSessionAuthMac.setStatus("current")
_BrcdDot1xAuthMacSessionUserName_Type = SnmpAdminString
_BrcdDot1xAuthMacSessionUserName_Object = MibTableColumn
brcdDot1xAuthMacSessionUserName = _BrcdDot1xAuthMacSessionUserName_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 38, 5, 1, 1, 2),
    _BrcdDot1xAuthMacSessionUserName_Type()
)
brcdDot1xAuthMacSessionUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdDot1xAuthMacSessionUserName.setStatus("current")
_BrcdDot1xAuthMacSessionIncomingVlanId_Type = VlanId
_BrcdDot1xAuthMacSessionIncomingVlanId_Object = MibTableColumn
brcdDot1xAuthMacSessionIncomingVlanId = _BrcdDot1xAuthMacSessionIncomingVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 38, 5, 1, 1, 3),
    _BrcdDot1xAuthMacSessionIncomingVlanId_Type()
)
brcdDot1xAuthMacSessionIncomingVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdDot1xAuthMacSessionIncomingVlanId.setStatus("current")
_BrcdDot1xAuthMacSessionCurrentVlanId_Type = VlanId
_BrcdDot1xAuthMacSessionCurrentVlanId_Object = MibTableColumn
brcdDot1xAuthMacSessionCurrentVlanId = _BrcdDot1xAuthMacSessionCurrentVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 38, 5, 1, 1, 4),
    _BrcdDot1xAuthMacSessionCurrentVlanId_Type()
)
brcdDot1xAuthMacSessionCurrentVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdDot1xAuthMacSessionCurrentVlanId.setStatus("current")


class _BrcdDot1xAuthMacSessionAccessStatus_Type(Integer32):
    """Custom type brcdDot1xAuthMacSessionAccessStatus based on Integer32"""
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
        *(("blocked", 2),
          ("init", 4),
          ("permit", 1),
          ("restrict", 3))
    )


_BrcdDot1xAuthMacSessionAccessStatus_Type.__name__ = "Integer32"
_BrcdDot1xAuthMacSessionAccessStatus_Object = MibTableColumn
brcdDot1xAuthMacSessionAccessStatus = _BrcdDot1xAuthMacSessionAccessStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 38, 5, 1, 1, 5),
    _BrcdDot1xAuthMacSessionAccessStatus_Type()
)
brcdDot1xAuthMacSessionAccessStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdDot1xAuthMacSessionAccessStatus.setStatus("current")
_BrcdDot1xAuthMacSessionMaxAge_Type = Unsigned32
_BrcdDot1xAuthMacSessionMaxAge_Object = MibTableColumn
brcdDot1xAuthMacSessionMaxAge = _BrcdDot1xAuthMacSessionMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 38, 5, 1, 1, 6),
    _BrcdDot1xAuthMacSessionMaxAge_Type()
)
brcdDot1xAuthMacSessionMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdDot1xAuthMacSessionMaxAge.setStatus("current")


class _BrcdDot1xAuthMacSessionAddrType_Type(InetAddressType):
    """Custom type brcdDot1xAuthMacSessionAddrType based on InetAddressType"""


_BrcdDot1xAuthMacSessionAddrType_Object = MibTableColumn
brcdDot1xAuthMacSessionAddrType = _BrcdDot1xAuthMacSessionAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 38, 5, 1, 1, 7),
    _BrcdDot1xAuthMacSessionAddrType_Type()
)
brcdDot1xAuthMacSessionAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdDot1xAuthMacSessionAddrType.setStatus("current")
_BrcdDot1xAuthMacSessionIpAddr_Type = InetAddress
_BrcdDot1xAuthMacSessionIpAddr_Object = MibTableColumn
brcdDot1xAuthMacSessionIpAddr = _BrcdDot1xAuthMacSessionIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 38, 5, 1, 1, 8),
    _BrcdDot1xAuthMacSessionIpAddr_Type()
)
brcdDot1xAuthMacSessionIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdDot1xAuthMacSessionIpAddr.setStatus("current")


class _BrcdDot1xAuthMacSessionAging_Type(Integer32):
    """Custom type brcdDot1xAuthMacSessionAging based on Integer32"""
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
        *(("ena", 3),
          ("hardware", 2),
          ("notapplicable", 4),
          ("software", 1))
    )


_BrcdDot1xAuthMacSessionAging_Type.__name__ = "Integer32"
_BrcdDot1xAuthMacSessionAging_Object = MibTableColumn
brcdDot1xAuthMacSessionAging = _BrcdDot1xAuthMacSessionAging_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 38, 5, 1, 1, 9),
    _BrcdDot1xAuthMacSessionAging_Type()
)
brcdDot1xAuthMacSessionAging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdDot1xAuthMacSessionAging.setStatus("current")
_BrcdDot1xAuthGlobalAdminGroup_ObjectIdentity = ObjectIdentity
brcdDot1xAuthGlobalAdminGroup = _BrcdDot1xAuthGlobalAdminGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 38, 6)
)


class _BrcdDot1xAuthGlobalAdminConfigStatus_Type(EnabledStatus):
    """Custom type brcdDot1xAuthGlobalAdminConfigStatus based on EnabledStatus"""


_BrcdDot1xAuthGlobalAdminConfigStatus_Object = MibScalar
brcdDot1xAuthGlobalAdminConfigStatus = _BrcdDot1xAuthGlobalAdminConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 38, 6, 1),
    _BrcdDot1xAuthGlobalAdminConfigStatus_Type()
)
brcdDot1xAuthGlobalAdminConfigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brcdDot1xAuthGlobalAdminConfigStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BRCD-DOT1X-MIB",
    **{"VlanId": VlanId,
       "brcdDot1xAuth": brcdDot1xAuth,
       "brcdDot1xAuthGlobalConfigGroup": brcdDot1xAuthGlobalConfigGroup,
       "brcdDot1xAuthGlobalConfigQuietperiod": brcdDot1xAuthGlobalConfigQuietperiod,
       "brcdDot1xAuthGlobalConfigTxPeriod": brcdDot1xAuthGlobalConfigTxPeriod,
       "brcdDot1xAuthGlobalConfigSuppTimeOut": brcdDot1xAuthGlobalConfigSuppTimeOut,
       "brcdDot1xAuthGlobalConfigAuthServerTimeOut": brcdDot1xAuthGlobalConfigAuthServerTimeOut,
       "brcdDot1xAuthGlobalConfigMaxReq": brcdDot1xAuthGlobalConfigMaxReq,
       "brcdDot1xAuthGlobalConfigReAuthMax": brcdDot1xAuthGlobalConfigReAuthMax,
       "brcdDot1xAuthGlobalConfigReAuthPeriod": brcdDot1xAuthGlobalConfigReAuthPeriod,
       "brcdDot1xAuthGlobalConfigProtocolVersion": brcdDot1xAuthGlobalConfigProtocolVersion,
       "brcdDot1xAuthGlobalConfigTotalPortsEnabled": brcdDot1xAuthGlobalConfigTotalPortsEnabled,
       "brcdDot1xAuthGlobalConfigReauthStatus": brcdDot1xAuthGlobalConfigReauthStatus,
       "brcdDot1xAuthGlobalConfigMacSessionMaxAge": brcdDot1xAuthGlobalConfigMacSessionMaxAge,
       "brcdDot1xAuthGlobalConfigNoAgingDeniedSessions": brcdDot1xAuthGlobalConfigNoAgingDeniedSessions,
       "brcdDot1xAuthGlobalConfigNoAgingPermittedSessions": brcdDot1xAuthGlobalConfigNoAgingPermittedSessions,
       "brcdDot1xAuthGlobalConfigAuthFailAction": brcdDot1xAuthGlobalConfigAuthFailAction,
       "brcdDot1xAuthPortStatistics": brcdDot1xAuthPortStatistics,
       "brcdDot1xAuthPortStatTable": brcdDot1xAuthPortStatTable,
       "brcdDot1xAuthPortStatEntry": brcdDot1xAuthPortStatEntry,
       "brcdDot1xAuthPortStatRxEAPFrames": brcdDot1xAuthPortStatRxEAPFrames,
       "brcdDot1xAuthPortStatTxEAPFrames": brcdDot1xAuthPortStatTxEAPFrames,
       "brcdDot1xAuthPortStatRxEAPStartFrames": brcdDot1xAuthPortStatRxEAPStartFrames,
       "brcdDot1xAuthPortStatRxEAPLogOffFrames": brcdDot1xAuthPortStatRxEAPLogOffFrames,
       "brcdDot1xAuthPortStatRxEAPRespIdFrames": brcdDot1xAuthPortStatRxEAPRespIdFrames,
       "brcdDot1xAuthPortStatTxEAPReqIdFrames": brcdDot1xAuthPortStatTxEAPReqIdFrames,
       "brcdDot1xAuthPortStatRxEAPInvalidFrames": brcdDot1xAuthPortStatRxEAPInvalidFrames,
       "brcdDot1xAuthPortStatEAPLastFrameVersionRx": brcdDot1xAuthPortStatEAPLastFrameVersionRx,
       "brcdDot1xAuthPortStatRxEAPRespOrIdFrames": brcdDot1xAuthPortStatRxEAPRespOrIdFrames,
       "brcdDot1xAuthPortStatRxLengthErrorFrame": brcdDot1xAuthPortStatRxLengthErrorFrame,
       "brcdDot1xAuthPortStatTxRequestFrames": brcdDot1xAuthPortStatTxRequestFrames,
       "brcdDot1xAuthPortStatLastEAPFrameSource": brcdDot1xAuthPortStatLastEAPFrameSource,
       "brcdDot1xAuthPortConfig": brcdDot1xAuthPortConfig,
       "brcdDot1xAuthPortConfigTable": brcdDot1xAuthPortConfigTable,
       "brcdDot1xAuthPortConfigEntry": brcdDot1xAuthPortConfigEntry,
       "brcdDot1xAuthPortConfigPortControl": brcdDot1xAuthPortConfigPortControl,
       "brcdDot1xAuthPortConfigFilterStrictSec": brcdDot1xAuthPortConfigFilterStrictSec,
       "brcdDot1xAuthPortConfigDot1xOnPort": brcdDot1xAuthPortConfigDot1xOnPort,
       "brcdDot1xAuthPortState": brcdDot1xAuthPortState,
       "brcdDot1xAuthPortStateTable": brcdDot1xAuthPortStateTable,
       "brcdDot1xAuthPortStateEntry": brcdDot1xAuthPortStateEntry,
       "brcdDot1xAuthPortStateMacSessions": brcdDot1xAuthPortStateMacSessions,
       "brcdDot1xAuthPortStateAuthMacSessions": brcdDot1xAuthPortStateAuthMacSessions,
       "brcdDot1xAuthPortStateOriginalPVID": brcdDot1xAuthPortStateOriginalPVID,
       "brcdDot1xAuthPortStatePVIDMacTotal": brcdDot1xAuthPortStatePVIDMacTotal,
       "brcdDot1xAuthPortStatePVIDMacAuthorized": brcdDot1xAuthPortStatePVIDMacAuthorized,
       "brcdDot1xAuthPortStatePortVlanState": brcdDot1xAuthPortStatePortVlanState,
       "brcdDot1xAuthPortStatePVID": brcdDot1xAuthPortStatePVID,
       "brcdDot1xAuthPortStateRestrictPVID": brcdDot1xAuthPortStateRestrictPVID,
       "brcdDot1xAuthPortStateRadiusAssignPVID": brcdDot1xAuthPortStateRadiusAssignPVID,
       "brcdDot1xAuthMacSession": brcdDot1xAuthMacSession,
       "brcdDot1xAuthMacSessionTable": brcdDot1xAuthMacSessionTable,
       "brcdDot1xAuthMacSessionEntry": brcdDot1xAuthMacSessionEntry,
       "brcdDot1xAuthMacSessionAuthMac": brcdDot1xAuthMacSessionAuthMac,
       "brcdDot1xAuthMacSessionUserName": brcdDot1xAuthMacSessionUserName,
       "brcdDot1xAuthMacSessionIncomingVlanId": brcdDot1xAuthMacSessionIncomingVlanId,
       "brcdDot1xAuthMacSessionCurrentVlanId": brcdDot1xAuthMacSessionCurrentVlanId,
       "brcdDot1xAuthMacSessionAccessStatus": brcdDot1xAuthMacSessionAccessStatus,
       "brcdDot1xAuthMacSessionMaxAge": brcdDot1xAuthMacSessionMaxAge,
       "brcdDot1xAuthMacSessionAddrType": brcdDot1xAuthMacSessionAddrType,
       "brcdDot1xAuthMacSessionIpAddr": brcdDot1xAuthMacSessionIpAddr,
       "brcdDot1xAuthMacSessionAging": brcdDot1xAuthMacSessionAging,
       "brcdDot1xAuthGlobalAdminGroup": brcdDot1xAuthGlobalAdminGroup,
       "brcdDot1xAuthGlobalAdminConfigStatus": brcdDot1xAuthGlobalAdminConfigStatus}
)
